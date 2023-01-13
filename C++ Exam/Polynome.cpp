// Polynome.cpp
#include <iostream>
#include "Poly.h"
#include "Polynome.h"
using namespace std;

int max(int a, int b);

int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

Polynome::Polynome(int deg)
    : Poly(deg)
{
}

Polynome::Polynome(float* coe, int deg)
    : Poly(coe, deg)
{
}

Polynome::Polynome(const Monome* mono, int nbMono)
    : Poly(mono, nbMono)
{
}

// fonction amie pour avoir le reel en premier operande
Polynome operator*(float a, const Polynome& pol)
{
    int degre = pol.getDegre();
    Polynome polRes(degre);

    for (int i = 0; i <= degre; i++)
        polRes.setCoeff(i, a * pol.getCoeff(i));

    polRes.ajusterDegre();  // au cas ou on multiplie par un reel nul
    return polRes;
}

Polynome Polynome::operator+(const Polynome& pol2) const
{
    int degre = getDegre();
    int degre2 = pol2.getDegre();
    int degRes = max(degre, degre2);
    Polynome polRes(degRes);

    for (int i = 0; i <= degRes; i++) {
        float coeffRes = 0;
        if (i <= degre)
            coeffRes = getCoeff(i);
        if (i <= degre2)
            coeffRes += pol2.getCoeff(i);
        polRes.setCoeff(i, coeffRes);
    }

    polRes.ajusterDegre();  // l'addition a pu annuler des termes de haut degre
    return polRes;
}

Polynome Polynome::operator-(const Polynome& pol2) const
{
    // utilisation des operateurs d'addition et de multiplication par un reel
    return *this + (-1) * pol2;
}

Polynome Polynome::operator*(const Polynome& pol2) const
{
    int degre = getDegre();
    int degre2 = pol2.getDegre();
    Polynome polRes(degre + degre2);

    for (int i = 0; i <= degre; i++)
        for (int j = 0; j <= degre2; j++)
        {
            float coeffRes = polRes.getCoeff(i + j);
            coeffRes += getCoeff(i) * pol2.getCoeff(j);
            polRes.setCoeff(i + j, coeffRes);
        }

    polRes.ajusterDegre();  // au cas ou on multiplie par le polynome nul
    return polRes;
}

float Polynome::operator()(float x) const
{
    return evaluer(x);
}

Polynome Polynome::creerParRacines(const int* racines, int nbRacines)
{
    float t_1[] = { 1 };
    Polynome polRes(t_1, 0);    // polynome 1

    for (int i = 0; i < nbRacines; i++) {
        float ti[] = { (float)-racines[i], 1 };
        Polynome Pi(ti, 1);   // X - ieme_racine
        polRes = polRes * Pi;
    }

    return  polRes;
}

Polynome Polynome::tchebychev(int n)
{
    float t_1[] = { 1 }, t_X[] = { 0, 1 }, t_2X[] = { 0, 2 };
    Polynome T0(t_1, 0), T1(t_X, 1), P_2X(t_2X, 1);
    Polynome Tn;

    if (n == 0)
        Tn = T0;
    else if (n == 1)
        Tn = T1;
    else {
        Polynome Tn_2 = T0;
        Polynome Tn_1 = T1;
        for (int i = 2; i <= n; i++) {
            Tn = P_2X * Tn_1 - Tn_2;
            Tn_2 = Tn_1;
            Tn_1 = Tn;
        }
    }

    return Tn;
}
