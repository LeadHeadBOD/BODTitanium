##///
##||| GlmBAct.PY TITANIUM
##||| Change list:
##||| * g_spit fix
##\\\ 

import Bladex


def AddGolemActions (biped_name):

	####################################################################################
	#
	# Escalar + saltos
	#
	####################################################################################
	
	Bladex.AddBipedAction(biped_name,"clmb_low_1h","Glm_clmb_low",0.0,1.0,0)	
	Bladex.AddBipedAction(biped_name,"clmb_medlow_1h","Glm_clmb_low",0.0,1.0,0)	
	Bladex.AddBipedAction(biped_name,"clmb_medium_1h","Glm_clmb_low",0.0,1.0,0)	
	Bladex.AddBipedAction(biped_name,"clmb_high_1h","Glm_clmb_low",0.0,1.0,0)	
	
	
	
	####################################################################################
	#
	# Others
	#
	####################################################################################
	
	Bladex.AddBipedAction(biped_name,"slip","Glm_slip",0.0,1.0,0)	
	Bladex.AddBipedAction(biped_name,"slip_b","Glm_slip_b",0.0,1.0,0)	
	Bladex.AddBipedAction(biped_name,"derrape","Glm_derrape",0.14,1.0,0)	
	
	
	
	####################################################################################
	#
	# Relax.
	#
	####################################################################################
	
	Bladex.AddBipedAction(biped_name,"Rlx_no","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_1h","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_b","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_2h","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_s","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_2w","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_axe","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_sp","Glm_rlx_no",0.0,1.0,0)
	
	
	
	
	
	
	
	####################################################################################
	#
	# Pasos.- Andares
	#
	####################################################################################
	
	#Movement with shield -> !NPC only!!!!
	Bladex.AddBipedAction(biped_name,"Attack_f_s_nc","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_b_s_nc","Glm_rlx_no",0.0,1.0,0)
	
	
	#pasito
	Bladex.AddBipedAction(biped_name,"ShortStep_no","Glm_rlx_no", 0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"ShortStep_1h","Glm_rlx_no", 0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"ShortStep_2h","Glm_rlx_no", 0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"ShortStep_s","Glm_rlx_no", 0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"ShortStep_2w","Glm_rlx_no", 0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"ShortStep_sp","Glm_rlx_no", 0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"ShortStep_axe","Glm_rlx_no", 0.0,1.0,0)
	
	# Andar hacia atrás
	Bladex.AddBipedAction(biped_name,"WBK_b","Glm_wbk_no",0.0,1.0,0)	
	Bladex.AddBipedAction(biped_name,"WBK_no","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_1h","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_2h","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_s","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_sp","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_axe","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_2w","Glm_wbk_no",0.0,1.0,0)
	
	#Andar hacia delante
	Bladex.AddBipedAction(biped_name,"WLK_b","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WLK_no","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WLK_1h","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WLK_2h","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WLK_s","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WLK_2w","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WLK_axe","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WLK_sp","Glm_wlk_no",0.0,1.0,0)
	
	##Correr hacia delante
	#Bladex.AddBipedAction(biped_name,"JOG_b","Glm_jog_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"JOG_no","Glm_jog_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"JOG_s","Glm_jog_no,0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"JOG_1h","Glm_jog_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"JOG_2h","Glm_jog_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"JOG_2w","Glm_jog_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"JOG_axe","Glm_jog_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"JOG_sp","Glm_jog_no",0.0,1.0,0)
	
	#Correr hacia delante
	Bladex.AddBipedAction(biped_name,"JOG_b","Glm_jog_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"JOG_no","Glm_jog_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"JOG_s","Glm_jog_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"JOG_1h","Glm_jog_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"JOG_2h","Glm_jog_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"JOG_2w","Glm_jog_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"JOG_axe","Glm_jog_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"JOG_sp","Glm_jog_no",0.0,1.0,0)
	
	#Correr hacia atrás
	Bladex.AddBipedAction(biped_name,"WBK_JOG_b","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_JOG_no","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_JOG_s","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_JOG_1h","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_JOG_2h","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_JOG_sp","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_JOG_axe","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"WBK_JOG_2w","Glm_wbk_no",0.0,1.0,0)
	
	#Modo Sneak
	Bladex.AddBipedAction(biped_name,"SNK_b","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"SNK_no","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"SNK_s","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"SNK_1h","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"SNK_2h","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"SNK_sp","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"SNK_axe","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"SNK_2w","Glm_wlk_no",0.0,1.0,0)
	#
	##Correr hacia atrás
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_b","Glm_wbk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_no","Glm_wbk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_1h","Glm_wbk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_2h","Glm_wbk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_s","Glm_wbk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_2w","Glm_wbk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_axe","Glm_wbk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"WBK_JOG_sp","Glm_wbk_no",0.0,1.0,0)
	#
	##Modo sneak
	#Bladex.AddBipedAction(biped_name,"SNK_b","Glm_wlk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"SNK_no","Glm_wlk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"SNK_s", "Glm_wlk_no,0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"SNK_1h","Glm_wlk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"SNK_2h","Glm_wlk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"SNK_sp", "Glm_wlk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"SNK_2w","Glm_wlk_no",0.0,1.0,0)
	#Bladex.AddBipedAction(biped_name,"SNK_axe","Glm_wlk_no",0.0,1.0,0)
	
	
	
	
	
	####################################################################################
	#
	# Caidas.
	#
	####################################################################################
	
	Bladex.AddBipedAction(biped_name,"FllLow","Glm_fll_low",0.5,0.8,0)
	Bladex.AddBipedAction(biped_name,"FllMed","Glm_fll_low",0.37,0.8,0)
	Bladex.AddBipedAction(biped_name,"FllHigh","Glm_fll_low",0.1,0.8,0)
	Bladex.AddBipedAction(biped_name,"Dth_Fll","Dth_Fll_Glm",0.0,0.33,0)
	Bladex.AddBipedAction(biped_name,"Dth_Fll2","Dth_Fll2_Glm",0.11,0.9,0)
	
	
	
	
	####################################################################################
	#
	# Animaciones en combate
	#
	####################################################################################
	
	#MOvement without shield
	Bladex.AddBipedAction(biped_name,"Attack_f_no","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_b_no","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_r_no","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_l_no","Glm_wlk_no",0.0,1.0,0)
	
	
	Bladex.AddBipedAction(biped_name,"Attack_f_s","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_b_s","Glm_wbk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_r_s","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_l_s","Glm_wlk_no",0.0,1.0,0)
	
	#Relax
#	Bladex.AddBipedAction(biped_name,"Rlx_f","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Rlx_f_no","Glm_rlx_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"Attack_rlx_s","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Rlx_f_axe","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Rlx_f_sp","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Rlx_f_2w","Glm_rlx_no",0.0,1.0,0)
	
	
	#Dodges
	Bladex.AddBipedAction(biped_name,"D_b","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"D_l","Glm_wlk_no",0.0,1.0,0)
	Bladex.AddBipedAction(biped_name,"D_r","Glm_wlk_no",0.0,1.0,0)
	
#	#MOvement with 2hand sword
#	Bladex.AddBipedAction(biped_name,"Attack_f_2w","Glm_wlk_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_b_2w","Glm_wbk_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_r_2w","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_l_2w","Glm_rlx_no",0.0,1.0,0)
#	
#	#MOvement with axe
#	Bladex.AddBipedAction(biped_name,"Attack_f_axe","Glm_wlk_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_b_axe","Glm_wbk_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_r_axe","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_l_axe","Glm_rlx_no",0.0,1.0,0)
#	
#	
#	#MOvement with spear
#	Bladex.AddBipedAction(biped_name,"Attack_f_sp","Glm_wlk_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_b_sp","Glm_wbk_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_r_sp","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_l_sp","Glm_rlx_no",0.0,1.0,0)
#	
#	#Quick turns
#	Bladex.AddBipedAction(biped_name,"Attack_t_r","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_t_r_s","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_t_l","Glm_rlx_no",0.0,1.0,0)
#	Bladex.AddBipedAction(biped_name,"Attack_t_l_s","Glm_rlx_no",0.0,1.0,0)
	
	
	
	
	####################################################################################
	#
	# Ataques
	#
	####################################################################################
		
	Bladex.AddBipedAction(biped_name,"g_01","Glm_g_01",0.164,0.737,0)	
	Bladex.AddBipedAction(biped_name,"g_114","Glm_g_114",0.099,0.740,0)	
	Bladex.AddBipedAction(biped_name,"g_12","Glm_g_12",0.070,0.784,0)	
	Bladex.AddBipedAction(biped_name,"g_21_27","Glm_g_21_27",0.147,0.747,0)	
	Bladex.AddBipedAction(biped_name,"g_21","Glm_g_21",0.140,0.690,0)
	Bladex.AddBipedAction(biped_name,"g_31","Glm_g_31",0.093,0.722,0)		
	Bladex.AddBipedAction(biped_name,"g_spit","Glm_g_spit",0.14,0.90,0)		# was 0.0, 0.0
	Bladex.AddBipedAction(biped_name,"g_1tw","Glm_g_1tw",0.050,0.697,0)	
	
	
	
	
###################
#                 #
# Añadidos Luismi #
#                 #
###################
	
####  Muerte

	Bladex.AddBipedAction(biped_name,"dth0","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_c1","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_c2","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_c3","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_c4","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_c5","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_c6","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_c7","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth0",  "Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_n00","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_n01","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_n02","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_n03","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_n04","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_n05","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_n06","Glm_dth0",0.0,1.0,0)
	                       
	Bladex.AddBipedAction("Glm","dth_rock","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_rockfront","Glm_dth0",0.0,1.0,0)
	Bladex.AddBipedAction("Glm","dth_burn","Glm_dth0",0.0,1.0,0)		
	
	
	
#### Heridas

	Bladex.AddBipedAction(biped_name,"hurt_f_big","Glm_hurt_big",0.096,0.541,0)	
	Bladex.AddBipedAction(biped_name,"hurt_f_lite","Glm_rlx_no",0.200,0.500,0)	
	Bladex.AddBipedAction(biped_name,"hurt_f_head","Glm_hurt_big",0.096,0.541,0)	
	Bladex.AddBipedAction(biped_name,"hurt_f_breast","Glm_hurt_big",0.096,0.541,0)
	Bladex.AddBipedAction(biped_name,"hurt_f_back","Glm_hurt_big",0.096,0.541,0)
	Bladex.AddBipedAction(biped_name,"hurt_f_r_arm","Glm_rlx_no",0.200,0.500,0)
	Bladex.AddBipedAction(biped_name,"hurt_f_l_arm","Glm_rlx_no",0.200,0.500,0)
	Bladex.AddBipedAction(biped_name,"hurt_f_r_leg","Glm_rlx_no",0.200,0.500,0)
	Bladex.AddBipedAction(biped_name,"hurt_f_l_leg","Glm_rlx_no",0.200,0.500,0)
	Bladex.AddBipedAction(biped_name,"hurt_jog","Glm_hurt_big",0.096,0.541,0)
	Bladex.AddBipedAction(biped_name,"hurt_big","Glm_hurt_big",0.096,0.541,0)
	Bladex.AddBipedAction(biped_name,"hurt_head","Glm_hurt_big",0.096,0.541,0)
	Bladex.AddBipedAction(biped_name,"hurt_breast","Glm_hurt_big",0.096,0.541,0)
	Bladex.AddBipedAction(biped_name,"hurt_back","Glm_hurt_big",0.096,0.541,0)
	Bladex.AddBipedAction(biped_name,"hurt_r_arm","Glm_rlx_no",0.200,0.500,0)
	Bladex.AddBipedAction(biped_name,"hurt_l_arm","Glm_rlx_no",0.200,0.500,0)
	Bladex.AddBipedAction(biped_name,"hurt_r_leg","Glm_rlx_no",0.200,0.500,0)
	Bladex.AddBipedAction(biped_name,"hurt_l_leg","Glm_rlx_no",0.200,0.500,0)