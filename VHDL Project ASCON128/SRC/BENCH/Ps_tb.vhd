library ieee;
use ieee.std_logic_1164.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity Ps_tb is 
end Ps_tb;

architecture Ps_tb_arch of Ps_tb is

  component Ps
    port (
      State_in_i : in type_state;
      State_out_o : out type_state
    );
  end component;

-- component ports
signal State_in_s : type_state;
signal State_out_s : type_state;



begin --Ps_tb_arch
--component instantiation
DUT : Ps
  port map(
    State_in_i => State_in_s,
    State_out_o => State_out_s);

--stimuli description with inertial delay
Pstimuli : process
  begin  
    State_in_s(0) <= x"80400c0600000000";
    State_in_s(1) <= x"0001020304050607";
    State_in_s(2) <= x"08090a0b0c0d0eff";
    State_in_s(3) <= x"0001020304050607";
    State_in_s(4) <= x"08090a0b0c0d0e0f";
    wait;
  end process;

end Ps_tb_arch;

  


