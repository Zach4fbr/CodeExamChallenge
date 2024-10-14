/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP4
// Date      : Sat Oct 12 15:27:39 2024
/////////////////////////////////////////////////////////////


module xor_nbits_nb_g16 ( a_i, b_i, s_o );
  input [15:0] a_i;
  input [15:0] b_i;
  output [15:0] s_o;


  XOR22 C37 ( .A(a_i[0]), .B(b_i[0]), .Q(s_o[0]) );
  XOR22 C36 ( .A(a_i[1]), .B(b_i[1]), .Q(s_o[1]) );
  XOR22 C35 ( .A(a_i[2]), .B(b_i[2]), .Q(s_o[2]) );
  XOR22 C34 ( .A(a_i[3]), .B(b_i[3]), .Q(s_o[3]) );
  XOR22 C33 ( .A(a_i[4]), .B(b_i[4]), .Q(s_o[4]) );
  XOR22 C32 ( .A(a_i[5]), .B(b_i[5]), .Q(s_o[5]) );
  XOR22 C31 ( .A(a_i[6]), .B(b_i[6]), .Q(s_o[6]) );
  XOR22 C30 ( .A(a_i[7]), .B(b_i[7]), .Q(s_o[7]) );
  XOR22 C29 ( .A(a_i[8]), .B(b_i[8]), .Q(s_o[8]) );
  XOR22 C28 ( .A(a_i[9]), .B(b_i[9]), .Q(s_o[9]) );
  XOR22 C27 ( .A(a_i[10]), .B(b_i[10]), .Q(s_o[10]) );
  XOR22 C26 ( .A(a_i[11]), .B(b_i[11]), .Q(s_o[11]) );
  XOR22 C25 ( .A(a_i[12]), .B(b_i[12]), .Q(s_o[12]) );
  XOR22 C24 ( .A(a_i[13]), .B(b_i[13]), .Q(s_o[13]) );
  XOR22 C23 ( .A(a_i[14]), .B(b_i[14]), .Q(s_o[14]) );
  XOR22 C22 ( .A(a_i[15]), .B(b_i[15]), .Q(s_o[15]) );
endmodule

