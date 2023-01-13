library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity Ps is 
port(	
	State_in_i : in type_state;
	State_out_o : out type_state
);
end entity Ps;

architecture Ps_arch of Ps is
--declarative part
signal column_out_s: column;
signal column_in_s: column;
signal data_out_s: bit64;
begin
--part design
	--input column
colonne: for i in 0 to 63 generate
	column_in_s(i) <= State_in_i(0)(i) & State_in_i(1)(i) & State_in_i(2)(i) & State_in_i(3)(i) & State_in_i(4)(i);


	--calculus
   -- x  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F
 -- S(x) 04 0B 1F 14 1A 15 09 02 1B 05 08 12 1D 03 06 1C 1E 13 07 0E 00 0D 11 18 10 0C 01 19 16 0A 0F 17
   column_out_s(i) <=   ('0' & x"4") when column_in_s(i)="00000" else
   					 ('0' & x"B") when column_in_s(i)="00001" else
					 ('1' & x"F") when column_in_s(i)="00010" else
					 ('1' & x"4") when column_in_s(i)="00011" else
					 ('1' & x"A") when column_in_s(i)="00100" else
					 ('1' & x"5") when column_in_s(i)="00101" else
					 ('0' & x"9") when column_in_s(i)="00110" else
					 ('0' & x"2") when column_in_s(i)="00111" else
					 ('1' & x"B") when column_in_s(i)="01000" else
					 ('0' & x"5") when column_in_s(i)="01001" else
					 ('0' & x"8") when column_in_s(i)="01010" else
					 ('1' & x"2") when column_in_s(i)="01011" else
					 ('1' & x"D") when column_in_s(i)="01100" else
					 ('0' & x"3") when column_in_s(i)="01101" else
					 ('0' & x"6") when column_in_s(i)="01110" else
					 ('1' & x"C") when column_in_s(i)="01111" else
					 ('1' & x"E") when column_in_s(i)="10000" else
					 ('1' & x"3") when column_in_s(i)="10001" else
					 ('0' & x"7") when column_in_s(i)="10010" else
					 ('0' & x"E") when column_in_s(i)="10011" else
					 ('0' & x"0") when column_in_s(i)="10100" else
					 ('0' & x"D") when column_in_s(i)="10101" else
					 ('1' & x"1") when column_in_s(i)="10110" else
					 ('1' & x"8") when column_in_s(i)="10111" else
					 ('1' & x"0") when column_in_s(i)="11000" else
					 ('0' & x"C") when column_in_s(i)="11001" else
					 ('0' & x"1") when column_in_s(i)="11010" else
					 ('1' & x"9") when column_in_s(i)="11011" else
					 ('1' & x"6") when column_in_s(i)="11100" else
					 ('0' & x"A") when column_in_s(i)="11101" else
					 ('0' & x"F") when column_in_s(i)="11110" else
					 ('1' & x"7"); --when column_in_s(i)=x01F"0

	--output state 
	State_out_o(0)(i) <= column_out_s(i)(4); 
	State_out_o(1)(i) <= column_out_s(i)(3); 
	State_out_o(2)(i) <= column_out_s(i)(2); 
	State_out_o(3)(i) <= column_out_s(i)(1); 
	State_out_o(4)(i) <= column_out_s(i)(0);
	

end generate colonne; 
end architecture Ps_arch;