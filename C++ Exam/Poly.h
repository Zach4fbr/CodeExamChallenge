// Poly.h
#pragma once
#include <iostream>
#include "Monome.h"
using namespace std;

class Poly
{
public :
    Poly(int deg = 0);
    Poly(float* coe, int deg);
    Poly(const Monome* mono, int nbMono);

    Poly(const Poly& pol2);
    ~Poly();
    Poly& operator=(const Poly& pol2);

    friend ostream& operator<<(ostream& flux, const Poly& pol);

    int getDegre() const    { return degre; }
    float getCoeff(int deg) const;
    void setCoeff(int deg, float valCoeff);

    void ajusterDegre();
    float evaluer(float x) const;

private :
    float* coeff;
    int degre;

    void allouerEtCopier(float* coe, int deg);
};
