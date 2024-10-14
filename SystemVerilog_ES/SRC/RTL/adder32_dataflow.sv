`timescale 1ns / 1ps

module adder32_dataflow #(
    parameter nb_bits = 32
)(
    input logic [nb_bits-1:0] a_i,
    input logic [nb_bits-1:0] b_i,
    output logic [nb_bits:0] sum_o
);
    // Dataflow description of the adder
    assign sum_o = a_i + b_i;

endmodule : adder32_dataflow
