module counter #(
    nb_bits = 4
    )(
    input  logic clock_i,
    input  logic resetb_i,   // Reset, active low
    input  logic enable_i,   // Enable signal
    input  logic init_i,     //Keep count if disabled
    output logic [nb_bits-1:0] count_o  // 4-bit counter output
);

    // Déclaration des registres internes
    logic [nb_bits:0] count_s;

    // Counter logic
    always_ff @(posedge clock_i or negedge resetb_i) begin
        if (!resetb_i)
            count_s <= '0;  // Reset counter to 0
        else if (enable_i)
            if (init_i)
                count_s <= count_s + 1;  // Increment counter when enable is high
    end
    assign count_o = count_s;

endmodule
