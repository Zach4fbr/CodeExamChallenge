`timescale 1ns / 1ps

module xor_4bits_tb (
    //must remain empty
);
  //déclaration de variables internes (autant de I/O que de circuits à tester)
  logic [3:0] a_s;
  logic [3:0] b_s;
  logic [3:0] s_s;


  //instance du circuit de test (DUT = Device Under Test)
  xor_4bits DUT (
      .a_i(a_s),
      .b_i(b_s),
      .s_o(s_s)
  );


  //décrire les stimulis
  initial begin
    a_s = 4'b0000;  //a est est une variable de taille 4 : en bit (b), sa valeur est 0000
    b_s = 4'h0;  //idem mais en hexa 

    repeat (5) begin
      #7 a_s = ~a_s;
      #13 b_s = ~b_s;
    end
  end

endmodule : xor_4bits_tb
