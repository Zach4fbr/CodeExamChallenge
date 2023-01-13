--library declaration
library ieee;
use ieee.std_logic_1164.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

--entité toujours vide dans un test bench
entity Pl_tb is 
end Pl_tb;

architecture Pl_tb_arch of Pl_tb is

  component Pl
    port (
      State_in_i : in type_state;
      State_out_o : out type_state
    );
  end component;

-- component ports
signal State_in_s : type_state;
signal State_out_s : type_state;



begin --Pl_tb_arch
--component instantiation
DUT : Pl
  port map(
    State_in_i => State_in_s,
    State_out_o => State_out_s);

--stimuli description with inertial delay
Pstimuli : process
  begin
    State_in_s(0) <= x"8849060f0c0d0eff";
    State_in_s(1) <= x"80410e05040506f7";
    State_in_s(2) <= x"ffffffffffffff0f";
    State_in_s(3) <= x"80400406000000f0";
    State_in_s(4) <= x"0808080a08080808";
    wait;
  end process;

end Pl_tb_arch;

  


