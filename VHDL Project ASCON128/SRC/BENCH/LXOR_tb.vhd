library ieee;
use ieee.std_logic_1164.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity LXOR_tb is 
end LXOR_tb;

architecture LXOR_tb_arch of LXOR_tb is

  component LXOR
    port (
      data_in_i: in bit64;
      enable_data_in_i: in std_logic;
	  State_in_i : in type_state;
      State_out_o : out type_state
    );
  end component;

signal State_in_s : type_state;
signal State_out_s : type_state;
signal enable_s : std_logic;
signal data_s : bit64;

begin 
DUT : LXOR
  port map(
    data_in_i => data_s,
    enable_data_in_i => enable_s,
	  State_in_i => State_in_s,
    State_out_o => State_out_s);
 
    State_in_s(0) <= x"0000000011111111";
    State_in_s(1) <= x"0000000000000000";
    State_in_s(2) <= x"0000000000000000";
    State_in_s(3) <= x"1111111111111111";
    State_in_s(4) <= x"1111111111111111";
    data_s <= x"1111111111111111";
    enable_s <= '1';
end LXOR_tb_arch;

  

