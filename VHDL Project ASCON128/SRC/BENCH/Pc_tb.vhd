--library declaration
library ieee;
use ieee.std_logic_1164.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

--entité toujours vide dans un test bench
entity Pc_tb is 
end Pc_tb;

architecture Pc_tb_arch of Pc_tb is

  component Pc
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


begin --Pc_tb_arch
--component instantiation
DUT : Pc
  port map(
    Round_i => Round_s,
    State_in_i => State_in_s,
    State_out_o => State_out_s);

--stimuli description with inertial delay
Pstimuli : process
  begin
    Round_s <= "0000";
    State_in_s(0) <= x"80400c0600000000";
    State_in_s(1) <= x"0001020304050607";
    State_in_s(2) <= x"08090a0b0c0d0e0f";
    State_in_s(3) <= x"0001020304050607";
    State_in_s(4) <= x"08090a0b0c0d0e0f";
    wait;
  end process;

end Pc_tb_arch;

  

