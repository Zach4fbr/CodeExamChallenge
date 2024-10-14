`timescale 1ns / 1ps

//module definition

module xor_nbits #(
    parameter nb_g = 4
    )(
    input  logic [nb_g-1:0] a_i,
    input  logic [nb_g-1:0] b_i,
    output logic [nb_g-1:0] s_o
);

  assign s_o = a_i ^ b_i;
endmodule : xor_nbits
