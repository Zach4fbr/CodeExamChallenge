module alu #(
    parameter nb_bits = 32
    )(
    input  logic [nb_bits-1:0] a_i,      // Entrée a_i (nb_bits bits)
    input  logic [nb_bits-1:0] b_i,      // Entrée b_i (nb_bits bits)
    input  logic clock_i,             // Horloge
    input  logic rst_n,           // Reset actif bas
    output logic [nb_bits:0] sum_o     // Sortie sum_o (33 bits)
);

    // Déclaration des registres internes
    logic [nb_bits-1:0] a_reg, b_reg;   // Registres pour stocker a_i et b_i
    logic [nb_bits:0] sum_reg;        // Registre pour stocker sum_o

    // Instances des registres pour les entrées a_i et b_i
    register #(nb_bits) reg_a (
        .clock_i(clock_i),
        .resetb_i(rst_n),
        .data_i(a_i),
        .data_o(a_reg)
    );

    register #(nb_bits) reg_b (
        .clock_i(clock_i),
        .resetb_i(rst_n),
        .data_i(b_i),
        .data_o(b_reg)
    );

    // Instance de l'additionneur
    adder32_dataflow adder_inst (
        .a_i(a_reg),
        .b_i(b_reg),
        .sum_o(sum_reg)
    );

    // Instance du registre pour la sortie sum_o
    register #(nb_bits+1) reg_sum (
        .clock_i(clk),
        .resetb_i(rst_n),
        .data_i(sum_reg),
        .data_o(sum_o)
    );

endmodule
