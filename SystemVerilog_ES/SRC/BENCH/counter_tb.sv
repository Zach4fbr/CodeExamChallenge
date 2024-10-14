`timescale 1ns / 1ps

module counter_tb ();

    parameter int nb_bits = 4;

    // Signal declarations
    logic clock_s;
    logic resetb_s;
    logic enable_s;
    logic init_s;
    logic [nb_bits-1:0] count_s;

    // Instantiate the counter module (DUT - Device Under Test)
    counter DUT (
        .clock_i(clock_s),
        .resetb_i(resetb_s),
        .enable_i(enable_s),
        .init_i(init_s),
        .count_o(count_s)
    );

    // Clock generation
    initial begin
        clock_s = 1'b0;
        forever #5 clock_s = ~clock_s;  // 10ns clock period
    end

    // Stimulus
    initial begin
        // Initialize signals
        resetb_s = 1'b0;  // Apply reset
        enable_s = 1'b0;  // Disable counter
        init_s = 1'b1;
        #12;

        // Release reset
        resetb_s = 1'b1;
        #10;

        // Enable counter and observe counting
        enable_s = 1'b1;
        #50;  // Observe counting for 50ns

        // Disable counter
        enable_s = 1'b0;
        #20;  // Observe no counting for 20ns

        // Enable counter again
        enable_s = 1'b1;
        #30;  // Observe counting for 30ns

        // Apply reset during counting
        resetb_s = 1'b0;  // Reset counter
        #10;
        resetb_s = 1'b1;  // Release reset
        #10;

        #20; 
        init_s = 1'b1;
        #20;
        init_s = 1'b0;
        #10; 
        
        // Final observation
        enable_s = 1'b1;
        #40;  // Observe counting

    end

endmodule : counter_tb
