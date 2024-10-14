/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP4
// Date      : Mon Sep 16 14:47:28 2024
/////////////////////////////////////////////////////////////


module xor_4bits ( a_i, b_i, s_o );
  input [3:0] a_i;
  input [3:0] b_i;
  output [3:0] s_o;


  XOR22 C13 ( .A(a_i[0]), .B(b_i[0]), .Q(s_o[0]) );
  XOR22 C12 ( .A(a_i[1]), .B(b_i[1]), .Q(s_o[1]) );
  XOR22 C11 ( .A(a_i[2]), .B(b_i[2]), .Q(s_o[2]) );
  XOR22 C10 ( .A(a_i[3]), .B(b_i[3]), .Q(s_o[3]) );
endmodule

