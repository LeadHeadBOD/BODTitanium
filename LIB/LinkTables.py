##///
##||| LINKTABLES.PY TITANIUM
##||| Change list:
##||| * Added 2h parry reactions
##\\\ 

import Bladex


#
#
# 	Bladex.SetActionEventTable(biped_name,"clmb_low_1h","CLIMBING")
# 	1->Nombre bipedo
#	2->Nombvre accion ( mirar ficheros scripts\biped)
#	3->Tabla de repuesta a eventos (mirar ActionsTables.py en Scripts/biped)
#
#
#

def LinkMe(biped_name):

	####################################################################################
	#
	# Escalar + saltos
	#
	####################################################################################

	Bladex.SetActionEventTable(biped_name,"clmb_low_1h","CLIMBING")
	Bladex.SetActionEventTable(biped_name,"clmb_medlow_1h","CLIMBING")
	Bladex.SetActionEventTable(biped_name,"clmb_medium_1h","CLIMBING")
	Bladex.SetActionEventTable(biped_name,"clmb_high_1h","CLIMBING")

	Bladex.SetActionEventTable(biped_name,"LongJump1H","JUMPING")
	Bladex.SetActionEventTable(biped_name,"LongJumpNo","JUMPING")
	Bladex.SetActionEventTable(biped_name,"ShortJump","JUMPING")

	####################################################################################
	#
	# Others
	#
	####################################################################################

	Bladex.SetActionEventTable(biped_name,"slip","SLIPPING")
	Bladex.SetActionEventTable(biped_name,"slip_b","SLIPPING")

	Bladex.SetActionEventTable(biped_name,"derrape","SLIP_END")

	Bladex.SetActionEventTable(biped_name,"insult","INSULTING")

	Bladex.SetActionEventTable(biped_name,"b1","BOWING")
	Bladex.SetActionEventTable(biped_name,"b3","BOWING")
	Bladex.SetActionEventTable(biped_name,"b2","RELOADING")


	Bladex.SetActionEventTable(biped_name,"jog_turn","TURNING")
	Bladex.SetActionEventTable(biped_name,"wlk_turn","TURNING")
	Bladex.SetActionEventTable(biped_name,"snk_turn","TURNING")
	Bladex.SetActionEventTable(biped_name,"rlx_turn","TURNING")



	####################################################################################
	#
	# Relax.
	#
	####################################################################################

	Bladex.SetActionEventTable(biped_name,"Rlx_sp","Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_axe","Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_2w","Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_2h","Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_s","Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_1h","Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_b", "Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_no","Rlx")

	Bladex.SetActionEventTable(biped_name,"Rlx_block","Rlx")
	Bladex.SetActionEventTable(biped_name,"Rlx_vt","Rlx_vt")


	####################################################################################
	#
	# Pasos.- Andares
	#
	####################################################################################

	#Bladex.SetActionEventTable(biped_name,"LStepUp","LStepS")
	#Bladex.SetActionEventTable(biped_name,"LStairsUp","LStepS")
	#Bladex.SetActionEventTable(biped_name,"LStepDown","LStepS")
	#Bladex.SetActionEventTable(biped_name,"LStairsDown","LStepS")

	#Bladex.SetActionEventTable(biped_name,"RStepUp","RStepS")
	#Bladex.SetActionEventTable(biped_name,"RStairsUp","RStepS")
	#Bladex.SetActionEventTable(biped_name,"RStepDown","RStepS")
	#Bladex.SetActionEventTable(biped_name,"RStairsDown","RStepS")


	#Andar hacia detras
	Bladex.SetActionEventTable(biped_name,"WBK_sp","WBK")		
	Bladex.SetActionEventTable(biped_name,"WBK_axe","WBK")		
	Bladex.SetActionEventTable(biped_name,"WBK_2w","WBK")		
	Bladex.SetActionEventTable(biped_name,"WBK_2h","WBK")		
	Bladex.SetActionEventTable(biped_name,"WBK_s","WBK")		
	Bladex.SetActionEventTable(biped_name,"WBK_1h","WBK")		
	Bladex.SetActionEventTable(biped_name,"WBK_no","WBK")		
	Bladex.SetActionEventTable(biped_name,"WBK_b","WBK")		

	#Correr hacia detras
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_sp","WBK_JOG")		
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_axe","WBK_JOG")		
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_2w","WBK_JOG")		
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_2h","WBK_JOG")		
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_s","WBK_JOG")		
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_1h","WBK_JOG")		
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_no","WBK_JOG")		
	Bladex.SetActionEventTable(biped_name,"WBK_JOG_b","WBK_JOG")		


	# Andar hacia delante , WLK
	Bladex.SetActionEventTable(biped_name,"WLK_sp","WLK")
	Bladex.SetActionEventTable(biped_name,"WLK_axe","WLK")
	Bladex.SetActionEventTable(biped_name,"WLK_2w","WLK")
	Bladex.SetActionEventTable(biped_name,"WLK_2h","WLK")
	Bladex.SetActionEventTable(biped_name,"WLK_s","WLK")
	Bladex.SetActionEventTable(biped_name,"WLK_1h","WLK")
	Bladex.SetActionEventTable(biped_name,"WLK_no","WLK")
	Bladex.SetActionEventTable(biped_name,"WLK_b","WLK")		

	# Andar hacia delante , JOG
	Bladex.SetActionEventTable(biped_name,"JOG_sp","JOG")
	Bladex.SetActionEventTable(biped_name,"JOG_axe","JOG")
	Bladex.SetActionEventTable(biped_name,"JOG_2w","JOG")
	Bladex.SetActionEventTable(biped_name,"JOG_2h","JOG")
	Bladex.SetActionEventTable(biped_name,"JOG_s","JOG")
	Bladex.SetActionEventTable(biped_name,"JOG_1h","JOG")
	Bladex.SetActionEventTable(biped_name,"JOG_no","JOG")
	Bladex.SetActionEventTable(biped_name,"JOG_b","JOG")		


	# Andar hacia delante ,SNEAK
	Bladex.SetActionEventTable(biped_name,"SNK_sp","SNK")
	Bladex.SetActionEventTable(biped_name,"SNK_axe","SNK")
	Bladex.SetActionEventTable(biped_name,"SNK_2w","SNK")
	Bladex.SetActionEventTable(biped_name,"SNK_2h","SNK")
	Bladex.SetActionEventTable(biped_name,"SNK_s","SNK")
	Bladex.SetActionEventTable(biped_name,"SNK_1h","SNK")
	Bladex.SetActionEventTable(biped_name,"SNK_no","SNK")
	Bladex.SetActionEventTable(biped_name,"SNK_b","SNK")		

	#Andar con escudos
	Bladex.SetActionEventTable(biped_name,"Attack_f_s_nc","WLK")
	Bladex.SetActionEventTable(biped_name,"Attack_b_s_nc","WBK")


	####################################################################################
	#
	# Muertes
	#
	####################################################################################

	Bladex.SetActionEventTable(biped_name,"Dth0","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_burn","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_rock","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_rockfront","Dth")

	Bladex.SetActionEventTable(biped_name,"dth_n00","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_n01","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_n02","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_n03","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_n04","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_n05","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_n06","Dth")


	Bladex.SetActionEventTable(biped_name,"dth_c1","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_c2","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_c3","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_c4","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_c5","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_c6","Dth")
	Bladex.SetActionEventTable(biped_name,"dth_c7","Dth")



	####################################################################################
	#
	# Caidas.
	#
	####################################################################################

	Bladex.SetActionEventTable(biped_name,"FllLow","Fll")
	Bladex.SetActionEventTable(biped_name,"FllMed","Fll")
	Bladex.SetActionEventTable(biped_name,"FllHigh","Fll")
	Bladex.SetActionEventTable(biped_name,"Dth_Fll2","Dth_Fll2")

	Bladex.SetActionEventTable(biped_name,"Dth_Fll","Dth_Fll")


	####################################################################################
	#
	# Animaciones en combate -> NO ataques
	#
	####################################################################################

	#Facing in combat mode + angle fixing
	Bladex.SetActionEventTable(biped_name,"Rlx_f_no","FING_RLX")
	Bladex.SetActionEventTable(biped_name,"Rlx_f_s","FING_RLX")
	Bladex.SetActionEventTable(biped_name,"Rlx_f_1h","FING_RLX")	
	Bladex.SetActionEventTable(biped_name,"Rlx_f_2h","FING_RLX")	
	Bladex.SetActionEventTable(biped_name,"Rlx_f_2w","FING_RLX")	
	Bladex.SetActionEventTable(biped_name,"Rlx_f_axe","FING_RLX")	
	Bladex.SetActionEventTable(biped_name,"Rlx_f_sp","FING_RLX")	

	#Bladex.SetActionEventTable(biped_name,"Attack_rlx_s","FING_RLX")
	Bladex.SetActionEventTable(biped_name,"Shattack_rlx_2h","FING_RLX")
	Bladex.SetActionEventTable(biped_name,"Shattack_rlx_s","FING_RLX")

	# Facinf , forwards , with shield
	Bladex.SetActionEventTable(biped_name,"Shattack_f_s","FING_FRW_S")
	Bladex.SetActionEventTable(biped_name,"Shattack_f_2h","FING_FRW_S")
	
	#Facing , backwards , with shield
	Bladex.SetActionEventTable(biped_name,"Shattack_b_s","FING_BWD_S")
	Bladex.SetActionEventTable(biped_name,"Shattack_b_2h","FING_BWD_S")
	

	# Facinf , forwards , without shield 
	Bladex.SetActionEventTable(biped_name,"Attack_f_no","FING_FRW")
	Bladex.SetActionEventTable(biped_name,"Attack_f_s","FING_FRW")
	Bladex.SetActionEventTable(biped_name,"Attack_f_1h","FING_FRW")
	Bladex.SetActionEventTable(biped_name,"Attack_f_2h","FING_FRW")
	Bladex.SetActionEventTable(biped_name,"Attack_f_2w","FING_FRW")
	Bladex.SetActionEventTable(biped_name,"Attack_f_axe","FING_FRW")
	Bladex.SetActionEventTable(biped_name,"Attack_f_sp","FING_FRW")
	
	#Facing , backwards , without shield
	Bladex.SetActionEventTable(biped_name,"Attack_b_no","FING_BWD")
	Bladex.SetActionEventTable(biped_name,"Attack_b_s","FING_BWD")
	Bladex.SetActionEventTable(biped_name,"Attack_b_1h","FING_BWD")
	Bladex.SetActionEventTable(biped_name,"Attack_b_2h","FING_BWD")
	Bladex.SetActionEventTable(biped_name,"Attack_b_2w","FING_BWD")
	Bladex.SetActionEventTable(biped_name,"Attack_b_axe","FING_BWD")
	Bladex.SetActionEventTable(biped_name,"Attack_b_sp","FING_BWD")

	#Parrying with 2 handed sthing . Facing or NOT facing !	
	Bladex.SetActionEventTable(biped_name,"Parry_2w","PARRYING")
	Bladex.SetActionEventTable(biped_name,"Parry_axe","PARRYING")
	Bladex.SetActionEventTable(biped_name,"Parry_sp","PARRYING")



	# Facinf , strafe right , without shield 
	Bladex.SetActionEventTable(biped_name,"Attack_r_no","FING_RIGHT")
	Bladex.SetActionEventTable(biped_name,"Attack_r_s","FING_RIGHT")
	Bladex.SetActionEventTable(biped_name,"Attack_r_1h","FING_RIGHT")
	Bladex.SetActionEventTable(biped_name,"Attack_r_2h","FING_RIGHT")
	Bladex.SetActionEventTable(biped_name,"Attack_r_2w","FING_RIGHT")
	Bladex.SetActionEventTable(biped_name,"Attack_r_axe","FING_RIGHT")
	Bladex.SetActionEventTable(biped_name,"Attack_r_sp","FING_RIGHT")


	#Facing , strafe right , with shield -> no mpx!
	Bladex.SetActionEventTable(biped_name,"Shattack_r_s","FING_RIGHT_S")	
	Bladex.SetActionEventTable(biped_name,"Shattack_r_2h","FING_RIGHT_S")	

	# Facinf , strafe left , without shield 
	Bladex.SetActionEventTable(biped_name,"Attack_l_no","FING_LEFT")
	Bladex.SetActionEventTable(biped_name,"Attack_l_s","FING_LEFT")
	Bladex.SetActionEventTable(biped_name,"Attack_l_1h","FING_LEFT")
	Bladex.SetActionEventTable(biped_name,"Attack_l_2h","FING_LEFT")
	Bladex.SetActionEventTable(biped_name,"Attack_l_2w","FING_LEFT")
	Bladex.SetActionEventTable(biped_name,"Attack_l_axe","FING_LEFT")
	Bladex.SetActionEventTable(biped_name,"Attack_l_sp","FING_LEFT")

	#Facing , strafe left , shielded	
	Bladex.SetActionEventTable(biped_name,"Shattack_l_s","FING_LEFT_S")	
	Bladex.SetActionEventTable(biped_name,"Shattack_l_2h","FING_LEFT_S")
	

	####################################################################################
	#
	# Hurt ... (4 falling , etc)
	#
	####################################################################################		

	Bladex.SetActionEventTable(biped_name,"df_01","HURT")
	Bladex.SetActionEventTable(biped_name,"df_02","HURT")
	Bladex.SetActionEventTable(biped_name,"df_01_2w","HURT")	#	Added
	Bladex.SetActionEventTable(biped_name,"df_02_2w","HURT")	#	
	Bladex.SetActionEventTable(biped_name,"df_01_axe","HURT")	#	
	Bladex.SetActionEventTable(biped_name,"df_02_axe","HURT")	#	
	Bladex.SetActionEventTable(biped_name,"df_01_sp","HURT")	#	
	Bladex.SetActionEventTable(biped_name,"df_02_sp","HURT")	#			-LeadHead

	Bladex.SetActionEventTable(biped_name,"hurt_f_lite","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_big","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_head","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_breast","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_back","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_r_arm","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_l_arm","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_r_leg","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_f_l_leg","HURT")

	Bladex.SetActionEventTable(biped_name,"hurt_jog","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_head","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_breast","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_back","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_r_arm","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_l_arm","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_r_leg","HURT")
	Bladex.SetActionEventTable(biped_name,"hurt_l_leg","HURT")

	Bladex.SetActionEventTable(biped_name,"sw_react","HURT")

	
	""" do this now in the race combos files
	####################################################################################
	#
	# Animaciones en combate -> Ataques + Esquivas
	#
	####################################################################################		
	Bladex.SetActionEventTable(biped_name,"g_00","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_01","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_02","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_03","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_04","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_05","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_06","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_07","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_08","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_09","ATTACKING")
	
	Bladex.SetActionEventTable(biped_name,"g_10","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_11","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_12","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_13","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_14","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_15","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_16","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_17","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_18","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_19","ATTACKING")

	Bladex.SetActionEventTable(biped_name,"g_20","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_21","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_22","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_23","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_24","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_25","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_26","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_27","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_28","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_29","ATTACKING")

	Bladex.SetActionEventTable(biped_name,"g_30","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_31","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_32","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_33","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_34","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_35","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_36","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_37","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_38","ATTACKING")
	Bladex.SetActionEventTable(biped_name,"g_39","ATTACKING")



	Bladex.SetActionEventTable(biped_name,"D_r", "DODGING")
	Bladex.SetActionEventTable(biped_name,"D_l", "DODGING")
	Bladex.SetActionEventTable(biped_name,"D_b", "DODGING")
	
	"""
	


    ####################################################################################
    #
    # Interactive Various Actions (IVA)
    #
    ####################################################################################



	#Palancas	
	Bladex.SetActionEventTable(biped_name,"lvr_d","IVA")
	Bladex.SetActionEventTable(biped_name,"lvr_u","IVA")
	Bladex.SetActionEventTable(biped_name,"gulp00","IVA")
	Bladex.SetActionEventTable(biped_name,"drink","IVA")
	Bladex.SetActionEventTable(biped_name,"eat00","IVA")
	Bladex.SetActionEventTable(biped_name,"key","IVA")
	Bladex.SetActionEventTable(biped_name,"pulsador","IVA")
	
	Bladex.SetActionEventTable(biped_name,"tke_r_01",   "IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_02",   "IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_03",   "IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_04",   "IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_05",   "IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_key00","IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_key01","IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_key02","IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_key03","IVA")
	Bladex.SetActionEventTable(biped_name,"tke_r_key04","IVA")
	