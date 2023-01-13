// Monome.cpp
#include <iostream>
#include "Monome.h"
using namespace std;

Monome::Monome()
{
    coeff = 0;
    degre = 0;
}

Monome::Monome(float coe, int deg)
{
    coeff = coe;
    degre = deg;
}

ostream& operator<<(ostream& flux, const Monome& mono)
{
    flux << mono.coeff;
    if (mono.degre != 0)
        flux << "X" << mono.degre;
    return flux;
}
