`timescale 1ns / 1ps

//module definition

module xor_4bits (
    input  logic [3:0] a_i,
    input  logic [3:0] b_i,
    output logic [3:0] s_o
);

  assign s_o = a_i ^ b_i;
endmodule : xor_4bits
