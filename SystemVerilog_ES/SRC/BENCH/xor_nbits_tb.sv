`timescale 1ns / 1ps

module xor_nbits_tb ();

    // Parameter definition for the number of bits
    parameter int nb_g = 16;  // nb of gate for the xor

    // Signal declarations
    //déclaration de variables internes (autant de I/O que de circuits à tester)
    logic [nb_g-1:0] a_s;
    logic [nb_g-1:0] b_s;
    logic [nb_g-1:0] s_s;


    //instance du circuit de test (DUT = Device Under Test)
    xor_nbits DUT (
        .a_i(a_s),
        .b_i(b_s),
        .s_o(s_s)
    );


    //décrire les stimulis
    initial begin
        a_s = 16'h0000;  //a est est une variable de taille 16 : en hexa (h), sa valeur est 0000
        b_s = 16'hffff;  //idem mais en hexa 

        repeat (5) begin
            #7 a_s = ~a_s;
            #13 b_s = ~b_s;
        end
    end

endmodule : xor_nbits_tb