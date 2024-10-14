/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP4
// Date      : Sat Oct 12 17:08:38 2024
/////////////////////////////////////////////////////////////


module alu_nb_bits32 ( a_i, b_i, clock_i, rst_n, sum_o );
  input [31:0] a_i;
  input [31:0] b_i;
  output [32:0] sum_o;
  input clock_i, rst_n;

  assign sum_o[0] = sum_o[32];
  assign sum_o[1] = sum_o[32];
  assign sum_o[2] = sum_o[32];
  assign sum_o[3] = sum_o[32];
  assign sum_o[4] = sum_o[32];
  assign sum_o[5] = sum_o[32];
  assign sum_o[6] = sum_o[32];
  assign sum_o[7] = sum_o[32];
  assign sum_o[8] = sum_o[32];
  assign sum_o[9] = sum_o[32];
  assign sum_o[10] = sum_o[32];
  assign sum_o[11] = sum_o[32];
  assign sum_o[12] = sum_o[32];
  assign sum_o[13] = sum_o[32];
  assign sum_o[14] = sum_o[32];
  assign sum_o[15] = sum_o[32];
  assign sum_o[16] = sum_o[32];
  assign sum_o[17] = sum_o[32];
  assign sum_o[18] = sum_o[32];
  assign sum_o[19] = sum_o[32];
  assign sum_o[20] = sum_o[32];
  assign sum_o[21] = sum_o[32];
  assign sum_o[22] = sum_o[32];
  assign sum_o[23] = sum_o[32];
  assign sum_o[24] = sum_o[32];
  assign sum_o[25] = sum_o[32];
  assign sum_o[26] = sum_o[32];
  assign sum_o[27] = sum_o[32];
  assign sum_o[28] = sum_o[32];
  assign sum_o[29] = sum_o[32];
  assign sum_o[30] = sum_o[32];
  assign sum_o[31] = sum_o[32];

  LOGIC0 U34 ( .Q(sum_o[32]) );
endmodule

