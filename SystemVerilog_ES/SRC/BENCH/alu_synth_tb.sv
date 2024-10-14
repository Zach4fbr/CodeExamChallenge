`timescale 1ns/1ps

module alu_synth_tb();
    // Paramètre
    parameter int nb_bits = 32;

    // Signaux de test
    logic [nb_bits-1:0] a_i, b_i;
    logic clock_i, rst_n;
    logic [nb_bits:0] sum_o;

    // Instance de l'ALU
    alu_nb_bits32 DUT (
        .a_i(a_i),
        .b_i(b_i),
        .clock_i(clock_i),
        .rst_n(rst_n),
        .sum_o(sum_o)
    );

    // Générateur d'horloge (période de 10 ns)
    always #5 clock_i = ~clock_i;

    // Initialisation et stimuli
    initial begin
        // Initialisation des signaux
        clock_i = 0;
        rst_n = 0;
        a_i = 0;
        b_i = 0;

        // Attente de quelques cycles
        #20;

        // Sortie du reset
        rst_n = 1;
        
        // Test 1: Addition de 5 et 10
        a_i = 5;
        b_i = 10;
        #10;
        $display("Test 1: a_i = %d, b_i = %d, sum_o = %d", a_i, b_i, sum_o);

        // Test 2: Addition de 32'hFFFFFFFF et 1 (test du débordement)
        a_i = 32'hFFFFFFFF;
        b_i = 1;
        #10;
        $display("Test 2: a_i = %h, b_i = %h, sum_o = %h", a_i, b_i, sum_o);

        // Test 3: Addition de 32'h12345678 et 32'h87654321
        a_i = 32'h12345678;
        b_i = 32'h87654321;
        #10;
        $display("Test 3: a_i = %h, b_i = %h, sum_o = %h", a_i, b_i, sum_o);

        // Test 4: Addition de 0 et 0
        a_i = 0;
        b_i = 0;
        #10;
        $display("Test 4: a_i = %d, b_i = %d, sum_o = %d", a_i, b_i, sum_o);

        // Test 5: Addition de valeurs aléatoires
        a_i = $random;
        b_i = $random;
        #10;
        $display("Test 5: a_i = %h, b_i = %h, sum_o = %h", a_i, b_i, sum_o);
    end

endmodule: alu_synth_tb
