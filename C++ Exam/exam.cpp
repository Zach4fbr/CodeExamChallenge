// exam.cpp
#include "Monome.h"
#include "Poly.h"
#include "Polynome.h"
#include "Poly2.h"
using namespace std;

void tester_monome();
void tester_poly();
void tester_polynome();
void tester_polynome_IV();
void tester_poly2();

void tester_monome()
{
    cout << "TEST MONOME" << endl;
    Monome m0, m1(3, 4), m2(-2, 0);
    cout << m0 << " " << m1 << " " << m2 << endl;
}

void tester_poly()
{
    cout << endl << "TEST POLY" << endl;
    float t[] = { 0, 2, 0, 1, -9, 5 }; 
    Poly P1(t, 5);
    cout << P1 << endl;
    cout << "evaluation en 2 : " << P1.evaluer(2) << endl;
    P1.setCoeff(5, 0);
    P1.setCoeff(4, 0);
    cout << P1 << endl;
    P1.ajusterDegre();
    cout << "degre=" << P1.getDegre() << endl;

    Monome m[] = { Monome(-7, 0), Monome(5, 2), Monome(4, 12) };
    Poly P2(m, 3);
    cout << P2 << endl;
}

void tester_polynome()
{
    cout << endl << "TEST POLYNOME" <<endl;
    float t[] = { 1, 2, 0, -9, 5 }; 
    Monome m[] = { Monome(-4, 0), Monome(-2, 1), Monome(4, 5) };

    Polynome P1(t, 4), P2(m, 3);
    cout << "P1 : " << P1 << endl;
    cout << "P2 : " << P2 << endl;
    cout << "1.5 * P1 : " << 1.5 * P1 << endl;
    cout << "P1 + P2 : " << P1 + P2 << endl;
    cout << "P1 - P2 : " << P1 - P2 << endl;
    cout << "P1 * P2 : " << P1 * P2 << endl;
    cout << "P2(3) : " << P2(3) << endl;
}

void tester_polynome_IV()
{
    cout << endl << "TEST POLYNOME_IV" << endl;
    int r[] = {8, 7, 5};
    Polynome P1 = Polynome::creerParRacines(r, 3);
    cout << P1 << endl;
    // verification
    for (int i = 0; i < 3; i++)
        cout << "P(" << r[i] << ") = " << P1(r[i]) << endl;
    cout << P1(10) << endl;

    cout << Polynome::tchebychev(8) << endl;
}

void tester_poly2()
{
    cout << endl << "TEST POLY2" << endl;
    //Poly2 P0;
    //cout << P0 << endl;
    float t[] = { 1, 2, 0, -9, 5 }; 
    Monome m[] = { Monome(3, 0), Monome(2, 5), Monome(4, 12) };
    Poly2 P1(t, 4);
    cout << P1 << endl;
    Poly2 P2(m, 3);
    cout << P2 << endl;
}

int main(void)
{
    tester_monome();
    tester_poly();
    tester_polynome();
    tester_polynome_IV();
    tester_poly2();

    return 0;
}
