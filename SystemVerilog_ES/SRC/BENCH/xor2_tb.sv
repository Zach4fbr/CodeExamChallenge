`timescale 1ns / 1ps

module xor2_tb (
    //must remain empty
);
    //déclaration de variables internes (autant de I/O que de circuits à tester)
    logic a_s;
    logic b_s;
    logic s_s;

    
    //instance du circuit de test (DUT = Device Under Test)
    xor2 DUT (
	.a_i(a_s),
	.b_i(b_s),
	.s_o(s_s)
    );

   
    //décrire les stimulis
    initial begin 
	a_s = 1'b0; //a est est une variable de taille 1 : en bit (b), sa valeur est 0
	b_s = 1'b0;

	repeat (5) begin 
	    #7 a_s = ~a_s;
	    #13 b_s = ~b_s;
	end
    end 

endmodule : xor2_tb

