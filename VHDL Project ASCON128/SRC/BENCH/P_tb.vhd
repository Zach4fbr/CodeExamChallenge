--library declaration
library ieee;
use ieee.std_logic_1164.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

--entité toujours vide dans un test bench
entity P_tb is 
end P_tb;

architecture P_tb_arch of P_tb is

  component P
    port (
      Round_i : in bit4;
      State_in_i : in type_state;
      State_out_o : out type_state
    );
  end component;

-- component ports
signal State_in_s : type_state;
signal State_out_s : type_state;
signal Round_s : bit4;


begin --P_tb_arch
--component instantiation
DUT : P
  port map(
    Round_i => Round_s,
    State_in_i => State_in_s,
    State_out_o => State_out_s);

--stimuli description with inertial delay
Pstimuli : process
  begin
    --test round 4
    Round_s <= "0100";
    State_in_s(0) <= x"e6ee74eda90e8f61";
    State_in_s(1) <= x"a1d364f518e39fc2";
    State_in_s(2) <= x"d17f98ac9be2dd7f";
    State_in_s(3) <= x"448f5bd9015f7d6d";
    State_in_s(4) <= x"4f201960642f78aa";
    wait;
  end process;

end P_tb_arch;

  

