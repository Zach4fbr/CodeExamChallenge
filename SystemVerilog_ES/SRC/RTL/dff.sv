module dff (
    input  logic d_i,
    input  logic clock_i,
    input  logic resetb_i,
    output logic q_o
);

    // Sequential process
    always_ff @(posedge clock_i or negedge resetb_i) begin : seq_0
        if (resetb_i == 1'b0)
            // Nonblocking assignment
            q_o <= 1'b0;
        else
            q_o <= d_i;
    end : seq_0

endmodule : dff
