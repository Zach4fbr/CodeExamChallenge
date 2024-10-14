#if not aldready defined
set PROJECT_NAME "."
set synth_dir "$PROJECT_NAME/SYNTH"
set rtl_dir "$PROJECT_NAME/SRC/RTL"
set synth2_dir "$PROJECT_NAME/SRC/GATES"
set top_name "xor_4bits"
#set clock_name "clock_i"

#liste des fichiers à analyser dans l'ordre


set rtl_list [ list \
		   $rtl_dir/xor_gate.sv\
		   $rtl_dir/xor_4bits.sv\
		  ]
#analyse des fichiers
analyze -library LIB_RTL  -format sverilog $rtl_list

#elaboration des fichiers analysées
elaborate $top_name  -library LIB_RTL

# exemple d'un cas ou il y a un parametre generique qui se nomme n_g et qui vaut 16
#elaborate $top_name  -library LIB_RTL -parameters "nb_bits_g=16"
current_design $top_name
link
ungroup -all
check_design
#sauvegarde après analyse et elaboration
write -format ddc -hierarchy -output $synth_dir/DDC/${top_name}_elab.ddc

#contraintes
set_operating_conditions -library c35_CORELIB_TYP nom_pvt
set_wire_load_model -name 10k -library c35_CORELIB_TYP
#set cycleTime 20 
#create_clock -name "clock" -period $cycleTime -waveform { 10 20  } $clock_name
#sauvegarde après analyse et elaboration
write -format ddc -hierarchy -output $synth_dir/DDC/${top_name}_const.ddc

#synthèse
compile -map_effort high -area_effort medium -incremental_mapping

#sauvegarde après analyse et elaboration
write -format ddc -hierarchy -output $synth_dir/DDC/${top_name}_synth.ddc

#generation du code vhdl
#change_names -rules vhdl -verbose -hierarchy -log_changes $synth_dir/RPT/${top_name}_rename_vhdl.txt
#write -format vhdl -hierarchy -output $synth2_dir/${top_name}_synth.vhd

#generation du code verilog
change_names -rules verilog -verbose -hierarchy -log_changes $synth_dir/RPT/${top_name}_rename_verilog.txt

write -format verilog -hierarchy -output $synth2_dir/${top_name}_synth.v
#generation du fichier sdf

write_sdf -version 2.1 $synth_dir/SDF/${top_name}_synth.sdf

#generation des rapports
report_design -nosplit  > $synth_dir/RPT/${top_name}_report_design.txt

report_hierarchy  > $synth_dir/RPT/${top_name}_report_hierarchy.txt

report_reference -hierarchy -nosplit > $synth_dir/RPT/${top_name}_report_reference.txt

report_port -nosplit -verbose >  $synth_dir/RPT/${top_name}_report_port.txt

report_area -nosplit -hierarchy >  $synth_dir/RPT/${top_name}_report_area.txt

#report_clock -nosplit >  $synth_dir/RPT/${top_name}_report_clock.txt

report_qor >  $synth_dir/RPT/${top_name}_report_qor.txt


# a completer

