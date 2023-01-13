library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity HXOR is 
port(	
    data_in_i: in bit64;
    enable_data_in_i: in std_logic;
	State_in_i : in type_state;
	State_out_o : out type_state
);
end entity HXOR;

architecture HXOR_arch of HXOR is
--declarative part
begin
	State_out_o(0) <= (State_in_i(0) xor data_in_i) when enable_data_in_i = '1' else 
					  (State_in_i(0));
	State_out_o(1) <= State_in_i(1);
	State_out_o(2) <= State_in_i(2);
	State_out_o(3) <= State_in_i(3);
	State_out_o(4) <= State_in_i(4); 
end architecture HXOR_arch;
