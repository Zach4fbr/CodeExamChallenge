`timescale 1ns / 1ps

//module definition

module xor2 (
	input logic a_i,
	input logic b_i,
	output logic s_o
);

    assign s_o = a_i ^ b_i;
    endmodule : xor2
