`timescale 1ns / 1ps

module adder32_dataflow_tb ();
    // Parameters
    parameter int nb_bits = 32;
    
    // Testbench signals
    logic [nb_bits-1:0] a_s;
    logic [nb_bits-1:0] b_s;
    logic [nb_bits:0] sum_out_s;

    // Instantiate the adder
    adder32_structural #(
        .nb_bits(nb_bits)
    ) DUT (
        .a_i(a_s),
        .b_i(b_s),
        .sum_o(sum_out_s)
    );

    initial begin
        // Test Case 1: Add zero to zero
        a_s = 32'd0;
        b_s = 32'd0;
        #10;
        
        // Test Case 2: Add maximum unsigned values
        a_s = 32'hFFFFFFFF;
        b_s = 32'hFFFFFFFF;
        #10;
        
        // Test Case 3: Add random values
        a_s = 32'd12345678;
        b_s = 32'd87654321;
        #10;
        
        // Test Case 4: Add one to the maximum value
        a_s = 32'hFFFFFFFF;
        b_s = 32'd1;
        #10;
        
    end
endmodule : adder32_dataflow_tb
