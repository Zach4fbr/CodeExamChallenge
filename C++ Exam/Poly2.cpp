// Poly2.cpp
#include <iostream>
#include <list>
#include "Monome.h"
#include "Poly2.h"
using namespace std;

Poly2::Poly2(float* coe, int deg)
{
    for (int i = 0; i <= deg; i++) {
        if (coe[i] != 0) {
            Monome mono(coe[i], i);
            monomes.push_back(mono);
        }
    }
}

Poly2::Poly2(Monome* mono, int nbMono)
{
    for (int i = 0; i < nbMono; i++)
        monomes.push_back(mono[i]);
}

ostream& operator<<(ostream& flux, const Poly2& poly)
{
    list<Monome>::const_reverse_iterator it;
    for (it = poly.monomes.rbegin(); it != poly.monomes.rend(); it++)
        flux << *it << " ";

    return flux;
}
