// Poly.cpp
#include <iostream>
#include "Monome.h"
#include "Poly.h"
using namespace std;

Poly::Poly(int deg)
{
    degre = deg;
    coeff = new float[degre + 1];
    for (int i = 0; i <= degre; i++)
        coeff[i] = 0;
}

Poly::Poly(float* coe, int deg)
{
    allouerEtCopier(coe, deg);
}

Poly::Poly(const Monome* mono, int nbMono)
{
    degre = mono[nbMono - 1].getDegre();
    coeff = new float[degre + 1];

    for (int i = 0; i <= degre; i++)
        coeff[i] = 0;

    for (int i = 0; i < nbMono; i++)
        coeff[mono[i].getDegre()] = mono[i].getCoeff();
}

Poly::Poly(const Poly& pol2)
{
    allouerEtCopier(pol2.coeff, pol2.degre);
}

Poly::~Poly()
{
    delete [] coeff;
}


Poly& Poly::operator=(const Poly& pol2)
{
    if (&pol2 != this) {
        delete [] coeff;
        allouerEtCopier(pol2.coeff, pol2.degre);
    }
    
    return *this;
}

ostream& operator<<(ostream& flux, const Poly& pol)
{
    if (pol.degre == 0)
        flux << pol.coeff[0];
    else {
        for (int i = pol.degre; i >= 0; i--) {
            if (pol.coeff[i] != 0)
                flux << Monome(pol.coeff[i], i) << " ";
        }
    }

    return flux;
}

float Poly::getCoeff(int deg) const
{
    if (0 <= deg && deg <= degre)
        return coeff[deg];
    else
        return 0;
}

void Poly::setCoeff(int deg, float valCoeff)
{
    if (0 <= deg && deg <= degre)
        coeff[deg] = valCoeff;
}

void Poly::ajusterDegre()
{
    while (coeff[degre] == 0 && degre > 0)
        degre--;
}

float Poly::evaluer(float x) const
{
    float val = coeff[0];
    float xpuiss = 1;   // pour calcul des puissances successives de x

    for (int i = 1; i <= degre; i++) {
        xpuiss *= x;
        val += coeff[i] * xpuiss;
    }

    return val;
}

void Poly::allouerEtCopier(float* coe, int deg)
{
    degre = deg;
    coeff = new float[degre + 1];
    for (int i = 0; i <= degre; i++)
        coeff[i] = coe[i];
}
