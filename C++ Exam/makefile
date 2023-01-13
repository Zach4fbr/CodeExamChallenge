GCC = g++ -std=C++11

Monome.o : Monome.h Monome.cpp
	g++ -c Monome.cpp

Poly.o : Poly.h Poly.cpp
	g++ -c Poly.cpp

Polynome.o : Polynome.h Polynome.cpp
	g++ -c Polynome.cpp

Poly2.o : Poly2.h Poly2.cpp
	g++ -c Poly2.cpp

exam.o : Poly.h Polynome.h Poly2.h exam.cpp
	g++ -c exam.cpp

OBJ = Monome.o Poly.o Polynome.o Poly2.o exam.o

exam : $(OBJ)
	g++ $(OBJ) -o exam
