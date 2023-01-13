--library declaration
library ieee;
use ieee.std_logic_1164.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

--entité toujours vide dans un test bench
entity MUX_REG_tb is 
end MUX_REG_tb;

architecture MUX_REG_tb_arch of MUX_REG_tb is

  component MUX_REG
    port (
        clock_i: in std_logic;
        resetb_i: in std_logic;
        enable_in_i: in std_logic;
        data_i: in type_state;
        data_o: out type_state
    );
  end component;

-- component ports
signal clock_s : std_logic;
signal reset_s : std_logic;
signal enable_s : std_logic;
signal data_i_s : type_state;
signal data_o_s : type_state;


begin --MUX_REG_tb_arch
--component instantiation
DUT : MUX_REG
  port map(
    clock_i => clock_s,
    resetb_i => reset_s,
    enable_in_i => enable_s,
    data_i => data_i_s,
    data_o => data_o_s);

--stimuli description with inertial delay
    clock_s <=  '0',
                '1' after 50 ns,
                '0' after 100 ns,
                '1' after 150 ns,
                '0' after 200 ns,
                '1' after 250 ns,
                '0' after 300 ns,
                '1' after 350 ns;
    data_i_s(0) <= x"80400c0600000000";
    data_i_s(1) <= x"0001020304050607";
    data_i_s(2) <= x"08090a0b0c0d0e0f";
    data_i_s(3) <= x"0001020304050607";
    data_i_s(4) <= x"08090a0b0c0d0e0f";
    enable_s <=  '1',
                 '0' after 200 ns;
    -- simulation d'un court-circuit/reset
    reset_s <=  '1',
                '0' after 280 ns;
end MUX_REG_tb_arch;

  

