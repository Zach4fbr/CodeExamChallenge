library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity MUX_REG is
  port(
    clock_i: in std_logic;
    resetb_i: in std_logic;
    enable_in_i: in std_logic;
    data_i: in type_state;
    data_o: out type_state);
  end entity MUX_REG;

  architecture MUX_REG_arch of MUX_REG is
    --components
    component state_register is port(	
      clock_i  : in  std_logic;
      resetb_i : in  std_logic;
      data_i   : in  type_state;
      data_o   : out type_state);
    end component state_register;
    
    component mux_state is port(	
      enable_i: in std_logic;
      data0_i: in type_state;
      data1_i: in type_state;
      data_o : out type_state
    );
    end component mux_state;
    
    --signaux
    signal mux_reg_s: type_state;
    signal mux0_s: type_state;
    
    begin
    --part design
      C0: state_register port map(
        clock_i => clock_i,
        resetb_i => resetb_i,
        data_i => mux_reg_s,
        data_o => mux0_s		
      );
      C1: mux_state port map(
        data0_i => mux0_s,
        data1_i => data_i,
        data_o => mux_reg_s,
        enable_i => enable_in_i
      );   
      data_o <= mux0_s;
    end architecture MUX_REG_arch;

  
