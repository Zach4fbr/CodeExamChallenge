`timescale 1ns / 1ps

module register #(
    parameter nb_bits = 32
)(
    input  logic                 clock_i,   // clock input
    input  logic                 resetb_i,  // reset input (active low)
    input  logic [nb_bits-1:0]   data_i,    // input state data
    input  logic                 enable_i,  // input enable (keep data)
    output logic [nb_bits-1:0]   data_o     // output state data
);

    // Internal signal declaration
    logic [nb_bits-1:0] state_s;

    // Sequential process with asynchronous reset (active low)
    always_ff @(posedge clock_i or negedge resetb_i) begin
        if (!resetb_i) 
            state_s <= '0;  // Reset all elements to '0' (use '0' instead of '{default: '0})
        else 
            if (enable_i == 1'b1)
                state_s <= data_i;  // On clock edge, capture data_i
            else 
                state_s <= '0;
            
    end

    // Output assignment
    assign data_o = state_s;

endmodule : register
