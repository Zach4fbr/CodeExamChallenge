`timescale 1ns / 1ps

module adder32_structural #(
    parameter nb_bits = 32
)(
    input logic [nb_bits-1:0] a_i,
    input logic [nb_bits-1:0] b_i,
    output logic [nb_bits:0] sum_o
);
    // Internal net for carry signals
    logic [nb_bits-1:0] carry_s;

    // Generate the full adder logic for each bit
    genvar i;
    generate
        for (i = 0; i < nb_bits; i++) begin : adder_gen
            if (i == 0) begin
                // For the least significant bit, handle half-adder logic
                assign {carry_s[i], sum_o[i]} = a_i[i] + b_i[i];
            end else begin
                // For all other bits, handle full-adder logic
                assign {carry_s[i], sum_o[i]} = a_i[i] + b_i[i] + carry_s[i-1];
            end
        end
    endgenerate

    // Final carry out
    assign sum_o[nb_bits] = carry_s[nb_bits-1];

endmodule : adder32_structural
