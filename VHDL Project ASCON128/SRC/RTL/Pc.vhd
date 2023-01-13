library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity Pc is 
port(	
	Round_i : in bit4;
	State_in_i : in type_state;
	State_out_o : out type_state
);
end entity Pc;

architecture Pc_arch of Pc is
--declarative part
signal x0_in_s,x1_in_s,x2_in_s,x3_in_s,x4_in_s: bit64;
signal x0_out_s,x1_out_s,x2_out_s,x3_out_s,x4_out_s: bit64;
signal Cr_in_s : bit64;
begin
--part design
	--input Xi
	x0_in_s <= State_in_i(0); 
	x1_in_s <= State_in_i(1);
	x2_in_s <= State_in_i(2);
	x3_in_s <= State_in_i(3);
	x4_in_s <= State_in_i(4);
	
	--output xi
	x0_out_s <= x0_in_s;
	x1_out_s <= x1_in_s;
	x2_out_s <= x2_in_s xor Cr_in_s;
	x3_out_s <= x3_in_s;
	x4_out_s <= x4_in_s;

	--constant calculation
	Cr_in_s <= x"00000000000000" & round_constant(to_integer(unsigned(round_i)));
	--output state 
	State_out_o(0) <= x0_out_s;
	State_out_o(1) <= x1_out_s;
	State_out_o(2) <= x2_out_s;
	State_out_o(3) <= x3_out_s;
	State_out_o(4) <= x4_out_s; 
end architecture Pc_arch;

