library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library LIB_RTL;
use LIB_RTL.ascon_pack.all;



entity P is
port(
	State_in_i: in type_state;
	State_out_o: out type_state;
	Round_i: in bit4
    );
end entity P;
		
architecture P_arch of P is
--components
component Pc is port(	
	Round_i : in bit4;
	State_in_i : in type_state;
	State_out_o : out type_state
);
end component Pc;

component Ps is port(	
	State_in_i : in type_state;
	State_out_o : out type_state
);
end component Ps;

component Pl is port(	
	State_in_i : in type_state;
	State_out_o : out type_state
);
end component Pl;

--signaux
signal Pc_Ps_s: type_state;
signal Ps_Pl_s: type_state;
begin
--part design
	C0: Pc port map(
		Round_i => Round_i,
		State_in_i => State_in_i,
		State_out_o => Pc_Ps_s		
	);
	C1: Ps port map(
		State_in_i => Pc_Ps_s,
		State_out_o => Ps_Pl_s
	);
	C2: Pl port map(
		State_in_i => Ps_Pl_s,
		State_out_o => State_out_o
	);

end architecture P_arch;