/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP4
// Date      : Sat Oct 12 15:47:38 2024
/////////////////////////////////////////////////////////////


module counter_nb_bits4 ( clock_i, resetb_i, enable_i, init_i, count_o );
  output [3:0] count_o;
  input clock_i, resetb_i, enable_i, init_i;
  wire   N4, N6, N7, N8, N9, N11, n1;
  wire   [3:2] add_20_carry;

  CLKIN6 I_1 ( .A(enable_i), .Q(N4) );
  DFEC1 count_s_reg_0_ ( .D(N6), .E(N11), .C(clock_i), .RN(resetb_i), .Q(
        count_o[0]) );
  DFEC1 count_s_reg_1_ ( .D(N7), .E(N11), .C(clock_i), .RN(resetb_i), .Q(
        count_o[1]) );
  DFEC1 count_s_reg_2_ ( .D(N8), .E(N11), .C(clock_i), .RN(resetb_i), .Q(
        count_o[2]) );
  DFEC1 count_s_reg_3_ ( .D(N9), .E(N11), .C(clock_i), .RN(resetb_i), .Q(
        count_o[3]) );
  NOR20 U3 ( .A(N4), .B(n1), .Q(N11) );
  CLKIN0 U4 ( .A(init_i), .Q(n1) );
  ADD22 add_20_U1_1_1 ( .A(count_o[1]), .B(count_o[0]), .CO(add_20_carry[2]), 
        .S(N7) );
  ADD22 add_20_U1_1_2 ( .A(count_o[2]), .B(add_20_carry[2]), .CO(
        add_20_carry[3]), .S(N8) );
  ADD22 add_20_U1_1_3 ( .A(count_o[3]), .B(add_20_carry[3]), .S(N9) );
  CLKIN0 U5 ( .A(count_o[0]), .Q(N6) );
endmodule

