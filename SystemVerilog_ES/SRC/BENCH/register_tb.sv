`timescale 1ns / 1ps

module register_tb ();

    // Parameter definition for the number of bits
    parameter int nb_bits = 32;  // 32-bit register for this testbench

    // Signal declarations
    logic clock_s;
    logic resetb_s;
    logic [nb_bits-1:0] data_in_s;
    logic enable_s;
    logic [nb_bits-1:0] data_out_s;

    // Instantiate the register module (DUT - Device Under Test)
    register #(
        .nb_bits(nb_bits)  // Pass the nb_bits parameter to the DUT
    ) DUT (    
        .clock_i(clock_s),
        .resetb_i(resetb_s),
        .data_i(data_in_s),
        .enable_i(enable_s),
        .data_o(data_out_s)
    );

    // Clock generation
    initial begin
        clock_s = 1'b0;
        forever #5 clock_s = ~clock_s;  // 10ns clock period
    end

    // Stimulus
    initial begin
        // Initialize signals
        resetb_s = 1'b0;
        data_in_s = 'hFFFFFFFF;  // Initialize input data
        enable_s = 1'b0;          // Disable the register initially
        #17;

        // Release reset and apply first test data with enable low (no change in output expected)
        resetb_s = 1'b1;
        #13;
        data_in_s = 'h000FFFFF;  // Apply new data
        enable_s = 1'b0;         // Keep enable low
        #10;
        
        // Enable the register and apply new data
        enable_s = 1'b1;
        data_in_s = 'hFFF00000;  // Apply new data with enable high (output should change)
        #10;

        // Change data with enable high
        data_in_s = 'h12345678;
        #10;

        // Disable the register (no change in output expected on data change)
        enable_s = 1'b0;
        data_in_s = 'h87654321;  // Apply new data with enable low (output should not change)
        #10;

        // Apply reset
        resetb_s = 1'b0;
        enable_s = 1'b1;  // Enable is high but reset should override it
        #12;
        resetb_s = 1'b1;
        #10;

        // Final data changes
        data_in_s = 'hDEADBEEF;  // Apply data with enable high
        
    end

endmodule : register_tb
