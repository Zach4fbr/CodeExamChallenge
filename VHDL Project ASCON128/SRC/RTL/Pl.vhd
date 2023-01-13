library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity Pl is 
port(	
	State_in_i : in type_state;
	State_out_o : out type_state
);
end entity Pl;

architecture Pl_arch of Pl is
--declarative part
signal x0_in_s,x1_in_s,x2_in_s,x3_in_s,x4_in_s: bit64;
signal x0_out_s,x1_out_s,x2_out_s,x3_out_s,x4_out_s: bit64;
begin
--part design
	x0_in_s <= State_in_i(0);
	x1_in_s <= State_in_i(1);
	x2_in_s <= State_in_i(2);
	x3_in_s <= State_in_i(3);
	x4_in_s <= State_in_i(4);
	x0_out_s <= x0_in_s   xor   (x0_in_s(18 downto 0) & x0_in_s(63 downto 19))  xor   (x0_in_s(27 downto 0) & x0_in_s(63 downto 28));
	x1_out_s <= x1_in_s   xor   (x1_in_s(60 downto 0) & x0_in_s(63 downto 61))  xor   (x1_in_s(38 downto 0) & x1_in_s(63 downto 39));
	x2_out_s <= x2_in_s   xor   (x2_in_s(0) & x2_in_s(63 downto 1))  xor   (x2_in_s(5 downto 0) & x2_in_s(63 downto 6));
	x3_out_s <= x3_in_s   xor   (x3_in_s(9 downto 0) & x3_in_s(63 downto 10))  xor   (x3_in_s(16 downto 0) & x3_in_s(63 downto 17));
	x4_out_s <= x4_in_s   xor   (x4_in_s(6 downto 0) & x4_in_s(63 downto 7))  xor   (x4_in_s(40 downto 0) & x4_in_s(63 downto 41));

	--output state 
	State_out_o(0) <= x0_out_s;
	State_out_o(1) <= x1_out_s;
	State_out_o(2) <= x2_out_s;
	State_out_o(3) <= x3_out_s;
	State_out_o(4) <= x4_out_s; 
end architecture Pl_arch;


