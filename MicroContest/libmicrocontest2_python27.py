# Python library for http://www.microcontest.com/
# author: tehron
# date: 2012-05-17
from hashlib import sha1
from urllib import urlencode
from urllib2 import *
import re
import functools
import cookielib
#import shelve

__all__ = ["get_currentversion", "check_version", "commence_contest", "Contest"]
__version__ = "2.2"

def get_currentversion():
	return __version__

def check_version():
	url = 'http://www.microcontest.com/version.php?lib=python'
	
	global cookiejar
	global urlopener

	cookiejar = cookielib.CookieJar()
	urlopener = build_opener(HTTPCookieProcessor(cookiejar))
	request = Request(url)
	urlinfo = urlopener.open(request)
	page = urlinfo.read()

	return __version__ == page
	
def commence_contest(cont_id, username=None, password=None):
    return Contest().commence(cont_id, username, password)

class Contest(object):
    """Note: Contest._opener may be used to open URLs with session cookies"""

    def __init__(self):
        self._variables = {}
        self._answer = []
        for t in [int, float, str]:
            setattr(self, "get_%s" % t.__name__, functools.partial(self.get_param, typ=t))

    def __getattr__(self, attr):
        s = self._variables[attr]
        try:
            v = float(s)
            try:
                return int(s)
            except ValueError:
                return v
        except ValueError:
            return s

    def commence(self, cont_id, username=None, password=None):
        if username is None and password is None:
            from credentials import username, password
        data = [("username", username), ("password", sha1(password).hexdigest()),
                ("ID", cont_id), ("contestlogin", 1), ("version", 2)]
        self._cont_id = cont_id
        self._variables = {}
        self._answer = []
        self._opener = build_opener(HTTPCookieProcessor())
        self._opener.addheaders = [("User-Agent", "microcontest.py/%s" % __version__)]
        self._parse(self._post("/contests/%i/contest.php" % cont_id, data))
        #sh = shelve.open(".mccache")
        #sh[self._cont_id] = self._variables
        #sh.close()
        return self

    def get_param(self, name, typ):
        """Use this to have control over the type or when there's a name clash."""
        return typ(self._variables[name])

    def append_answer(self, name, value):
        self._answer.append((name, str(value)))

    def submit_answer(self, answer=None):
        """answer may be a dict or list of (k,v) tuples."""
        page = self._post("/contests/%i/validation.php" % self._cont_id, answer or self._answer)
        self._result = dict([line.split(":", 1) for line in page.splitlines()])
        if self._result.has_key("error"):
            raise Error(self._result["error"])

        if int(self._result["success"]):
            if int(self._result["timeout"]):
                return "correct, but too slow"
            if int(self._result["already"]):
                return "correct, but already solved"
            return self._result["points"] + " points gained"
        if int(self._result["timeout"]):
            return "wrong, and too slow"
        return "wrong"

    def _post(self, path, data):
        return self._opener.open("http://www.microcontest.com" + path, urlencode(data)).read()

    def _parse(self, page):
        #open("contest.php", "wb").write(page)
        match = re.compile(r'Nombre_variables=(\d+)<br/>').match(page, 0)
        if not match:
            x = page.split(" : ", 1)
            if len(x) != 2:
                raise ParseError("Unknown server response: %r" % page)
            if x[0] == "Erreur authentification":
                raise AuthenticationError(x[1])
            if x[0] == "Erreur":
                raise Error(x[1])
            raise Exception(x[0], x[1])

        cnt = int(match.group(1))
        pos = match.end()

        try:
            while len(self._variables) < cnt:
                match = re.compile(r'\[([^\]]+)\]<br/>').match(page, pos)
                n = match.group(1)
                pos = match.end()
                match = re.compile(r'Longueur=(\d+)<br/>Valeur=').match(page, pos)
                if match:
                    l = int(match.group(1))
                    v = page[match.end():match.end() + l]
                    pos = match.end() + l
                    match = re.compile(r'<br/>').match(page, pos)
                    if not match:
                        print "Error: No <br/> at end of variable. Trying to fix..."
                        _pos = page.find("<br/>", pos)
                        if _pos < 0:
                            raise Exception("<br/> not found")
                        v += page[pos:_pos]
                        pos = _pos
                    pos += len("<br/>")
                else:
                    match = re.compile(r'Valeur=(.*?)<br/>').match(page, pos)
                    v = match.group(1)
                    pos = match.end()
                self._variables[n] = v
        except:
            import sys
            _, exc, tb = sys.exc_info()
            raise ParseError("Couldn't parse variables: %r" % page[pos:pos+50], exc), None, tb

class Error(Exception):
    def __init__(self, msg, cause=None):
        Exception.__init__(self, msg)
        self.cause = cause
    def __str__(self):
        s = Exception.__str__(self)
        if self.cause:
            s += "\ncaused by\n%s: %s" % (type(self.cause).__name__, self.cause)
        return s
class AuthenticationError(Error):
    pass
class ParseError(Error):
    pass
"""Full usage example for Contest 1:
contest1.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from microcontest import *

    # cont = commence_contest(1, "harry", "potter")
    # short form uses username, password from credentials.py
    cont = commence_contest(1)

    # a = int(cont.get_param("a"))
    # you can also use get_int, get_float, get_str
    # b = cont.get_int("b")
    # or use it that way (it tries to return the right type automagically)
    # s = cont.a + cont.b

    # then append the answer (here using the short version)
    # cont.append_answer("s", cont.a + cont.b)

    # then submit the answer and print result
    # print cont.submit_answer()
    # or pass tuples directly to submit_answer (here using the short version)
    print cont.submit_answer([("s", cont.a + cont.b)])
credentials.py
    username = "harry"
    password = "potter"
"""
"""
if __name__ == "__main__":
    for page, var in [
        ("Nombre_variables=2<br/>[a]<br/>Valeur=20<br/>[b]<br/>Valeur=5<br/>", [("a",20),("b",5)]),
        ("Nombre_variables=2<br/>[txt_crypte]<br/>Longueur=53<br/>Valeur=ZBMXEXLIHBKJNXEXYKHBWLXKTBMFHBGLOBYTIKXLEXEXOXKWNCHNK<br/>[key]<br/>Valeur=19<br/>", [("txt_crypte", "ZBMXEXLIHBKJNXEXYKHBWLXKTBMFHBGLOBYTIKXLEXEXOXKWNCHNK"), ("key", 19)]),
        ("Nombre_variables=1<br/>[var]<br/>Longueur=26<br/>Valeur=lol\n[stilldata]<br/>[haha]<br/>", [("var", "lol\n[stilldata]<br/>[haha]")])
    ]:
        cont = Contest()
        cont._parse(page)
        for n, v in var:
            try:
                assert getattr(cont, n) == v
            except AssertionError:
                print n, v
                raise
    print "All tests passed"
"""
