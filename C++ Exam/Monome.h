// Monome.h
#pragma once
#include <iostream>
using namespace std;

class Monome
{
public :
    Monome();
    Monome(float coe, int deg);
    float getCoeff() const  { return coeff; }
    int getDegre() const    { return degre; }
    friend ostream& operator<<(ostream& flux, const Monome& mono);

private :
    float coeff;
    int degre;
};
