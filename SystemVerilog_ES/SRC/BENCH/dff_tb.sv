`timescale 1ns / 1ps
module dff_tb (
    // empty declarative part
);

    // Internal net declaration
    bit clock_s, resetb_s, d_s, q_s;

    // DUT : component instantiation
    dff DUT (
        .d_i(d_s),
        .resetb_i(resetb_s),
        .clock_i(clock_s),
        .q_o(q_s)
    );

    // clock generation
    initial begin
        clock_s = 1'b0;
        forever #5 clock_s = ~clock_s;
    end

    // stimuli
    initial begin
        resetb_s = 1'b0;
        d_s = 1'b0;
        #50;
        resetb_s = 1'b1;
        #25;
        d_s = 1'b1;
        #50;
        d_s = 1'b0;
        #50;
    end

endmodule : dff_tb
