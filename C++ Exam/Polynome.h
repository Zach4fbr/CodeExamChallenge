// Polynome.h
#pragma once
#include <iostream>
#include "Poly.h"

class Polynome : public Poly
{
public :
    Polynome(int deg = 0);
    Polynome(float* coe, int deg);
    Polynome(const Monome* mono, int nbMono);

    friend Polynome operator*(float a, const Polynome& pol);
    Polynome operator+(const Polynome& pol2) const;
    Polynome operator-(const Polynome& pol2) const;
    Polynome operator*(const Polynome& pol2) const;
    float operator()(float x) const;

    static Polynome creerParRacines(const int* racines, int nbRacines);
    static Polynome tchebychev(int n);

private :
};
