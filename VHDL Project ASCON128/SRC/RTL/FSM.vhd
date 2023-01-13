library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;

entity fsm is 
port(	
    clock_i: in std_logic;
    reset_o: in std_logic;
    start_i: in std_logic;
    data_valid_i: in std_logic;
    round_i: in bit4;
    block_i: in bit4;

    data_sel_o: out std_logic;
    en_reg_state_o: out std_logic;
    en_cipher_o: out std_logic;
    en_tag_o: out std_logic;
    cipher_valid_o: out std_logic;
    end_o: out std_logic;
    
    en_cpt_o: out std_logic;
    en_cpt_2_o: out std_logic;
    init_a_o: out std_logic;
    init_b_o: out std_logic;
    init_cpt_o: out std_logic;
    init_cpt_2_o: out std_logic;
    
    en_xor_key_full_o: out std_logic;
    en_xor_lsb_o: out std_logic;
    en_xor_data_o: out std_logic;
    en_xor_key_final_o: out std_logic;    
);
end entity fsm;

architecture fsm_arch of fsm is
--declarative part
--signal ...

begin
--part design
	
end architecture fsm_arch;

