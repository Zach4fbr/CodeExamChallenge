/////////////////////////////////////////////////////////////
// Created by: Synopsys Design Compiler(R)
// Version   : R-2020.09-SP4
// Date      : Mon Sep 16 14:19:37 2024
/////////////////////////////////////////////////////////////


module xor_4bits ( a_i, b_i, s_o );
  input [3:0] a_i;
  input [3:0] b_i;
  output [3:0] s_o;


  GTECH_XOR2 C10 ( .A(a_i[3]), .B(b_i[3]), .Z(s_o[3]) );
  GTECH_XOR2 C11 ( .A(a_i[2]), .B(b_i[2]), .Z(s_o[2]) );
  GTECH_XOR2 C12 ( .A(a_i[1]), .B(b_i[1]), .Z(s_o[1]) );
  GTECH_XOR2 C13 ( .A(a_i[0]), .B(b_i[0]), .Z(s_o[0]) );
endmodule

