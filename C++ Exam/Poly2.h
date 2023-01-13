// Poly2.h
#pragma once

#include <iostream>
#include <list>
#include "Monome.h"
using namespace std;

class Poly2
{
public :
    Poly2(float* coe, int deg);
    Poly2(Monome* mono, int nbMono);
    friend ostream& operator<<(ostream& flux, const Poly2& poly);

private :
    list<Monome> monomes;
};
