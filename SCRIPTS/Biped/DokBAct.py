##///
##||| DOKBACT.PY TITANIUM
##||| Change list:
##||| * Normalized some animation lengths (effectively copy-paste of regular orc)
##||| 
##\\\ 

import Bladex


####################################################################################
#
# Escalar + saltos
#
####################################################################################

Bladex.AddBipedAction("Dok","clmb_low_1h","Ork_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","clmb_medlow_1h","Ork_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","clmb_medium_1h","Ork_clmb_medium_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","clmb_high_1h","Ork_clmb_medium_1h",0.0,1.0,0)	

Bladex.AddBipedAction("Dok","LongJump1H","Ork_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","LongJumpNo","Ork_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","ShortJump","Ork_jmp_1h",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Dok","slip","Ork_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","slip_b","Ork_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","derrape","Ork_derrape",0.0,1.0,0)	


Bladex.AddBipedAction("Dok","b1","Ork_b1",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","b2","Ork_b2",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","b3","Ork_b3",0.0,1.0,0)	




####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Dok","Rlx_no","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Rlx_1h","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Rlx_b","Rlx_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Rlx_2h","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Rlx_s","Rlx_1h_Ork",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Dok","LStepUp","Wlk_Ork","WlkUp_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Dok","RStepUp","Wlk_Ork","WlkUp_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Dok","LStairsUp","StairsUp_Ork","StairsUpP_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Dok","RStairsUp","StairsUp_Ork","StairsUpP_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Dok","LStepDown","Wlk_Ork","WlkDown_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Dok","RStepDown","Wlk_Ork","WlkDown_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Dok","LStairsDown","StairsDown_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Dok","RStairsDown","StairsDown_Ork",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Dok","WBK_b","Wbk_b_Ork",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","WBK_no","Ork_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","WBK_1h","Ork_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Dok","WBK_2h","Ork_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","WBK_s","Ork_attack_b",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Dok","WLK_b","Wlk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WLK_no","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WLK_1h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WLK_2h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WLK_s","Wlk_1h_Ork",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Dok","WBK_JOG_b","Wbk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WBK_JOG_no","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WBK_JOG_s","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WBK_JOG_1h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dok","WBK_JOG_2h","Ork_attack_b",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Dok","JOG_b","Jog_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","JOG_no","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","JOG_s","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","JOG_1h","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","JOG_2h","Jog_1h_Ork",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Dok","SNK_b","Wlk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","SNK_no","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","SNK_s","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","SNK_1h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","SNK_2h","Wlk_1h_Ork",0.0,1.0,0)

#Correr con escudo en modo no combate                                       
Bladex.AddBipedAction("Dok","Attack_f_s_nc","Ork_attack_f_s",0.0,1.0,0)     
Bladex.AddBipedAction("Dok","Attack_b_s_nc","Ork_attack_b_s",0.0,1.0,0)     
                                                                          
####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Dok","FllLow","FallMed_Ork",0.37,0.8,0)
Bladex.AddBipedAction("Dok","FllMed","FallMed_Ork",0.37,0.8,0)
Bladex.AddBipedAction("Dok","FllHigh","FallHigh_Ork",0.1,0.8,0)
Bladex.AddBipedAction("Dok","Dth_Fll","Dth_Fll_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Dth_Fll2","Dth_Fll2_Ork",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Dok","Attack_f_1h","Ork_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Attack_b_1h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Attack_r_1h","Ork_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Attack_l_1h","Ork_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Dok","Attack_f_2h","Ork_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Attack_b_2h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Attack_r_2h","Ork_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Attack_l_2h","Ork_attack_l",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Dok","Shattack_f_2h","Ork_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Shattack_b_2h","Ork_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Shattack_r_2h","Ork_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Shattack_l_2h","Ork_attack_l_s",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Dok","Rlx_f_1h","Ork_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Rlx_f_2h","Ork_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Shattack_rlx_2h","Ork_attack_rlx_s",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Dok","Attack_t_r","Ork_attack_t_r",0.0,1.0,0)
#Bladex.AddBipedAction("Dok","Attack_t_r_s","Ork_attack_t_r_s",0.0,1.0,0)
#Bladex.AddBipedAction("Dok","Attack_t_l","Ork_attack_t_l",0.0,1.0,0)
#Bladex.AddBipedAction("Dok","Attack_t_l_s","Ork_attack_t_l_s",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Dok","D_b","Ork_d_b",0.0,1.0,0)
Bladex.AddBipedAction("Dok","D_l","Ork_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Dok","D_r","Ork_d_r",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################
	
Bladex.AddBipedAction("Dok","g_01","Ork_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","g_02","Ork_g_02",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","g_06","Ork_g_06",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","g_15","Ork_g_15",0.0,1.0,0)
Bladex.AddBipedAction("Dok","g_16","Ork_g_16",0.0,1.0,0)	
Bladex.AddBipedAction("Dok","g_18","Ork_g_18",0.0,1.0,0)






####################################################################################
#
# Animaciones de vigia
#
####################################################################################


Bladex.AddBipedAction("Dok","Wai_01","Ork_wai_01",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Wai_02","Ork_wai_02",0.0,1.0,0)

Bladex.AddBipedAction("Dok","alarm01","Ork_alarm01",0.0,1.0,0)

Bladex.AddBipedAction("Dok","patrol1","Ork_patrol1",0.0,1.0,0)
Bladex.AddBipedAction("Dok","patrol2","Ork_patrol2",0.0,1.0,0)
Bladex.AddBipedAction("Dok","fury","Ork_fury",0.0,1.0,0)

Bladex.AddBipedAction("Dok","attack_look","Ork_attack_look",0.0,1.0,0)

Bladex.AddBipedAction("Dok","order","Ork_order",0.0,1.0,0)

Bladex.AddBipedAction("Dok","insult","Ork_insult",0.0,1.0,0)




####################################################################################
#
# Cambio de armas
#
####################################################################################


Bladex.AddBipedAction("Dok","Attack_Chg_r_l","Ork_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Dok","Chg_r_l","Ork_attack_chg_r_l",0.0,1.0,0)

Bladex.AddBipedAction("Dok","attack_drink","Ork_attack_drink",0.0,1.0,0)


####################################################################################
#
# Reacciones
#
####################################################################################


Bladex.AddBipedAction("Dok","df_01","Ork_df_01",0.10,0.48,0)	
Bladex.AddBipedAction("Dok","df_02","Ork_df_02",0.10,0.67,0)

Bladex.AddBipedAction("Dok","sw_react","Ork_df_s_broken",0.35,1.0,0)

Bladex.AddBipedAction("Dok","df_s_broken","Ork_df_s_broken",0.0,1.0,0)



	
Bladex.AddBipedAction("Dok","hurt_f_lite","Ork_hurt_f_lite",0.14,0.65,0)	
Bladex.AddBipedAction("Dok","hurt_f_big","Ork_hurt_f_big",0.10,0.59,0)	
Bladex.AddBipedAction("Dok","hurt_f_head","Ork_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Dok","hurt_f_breast","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Dok","hurt_f_back","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Dok","hurt_f_r_arm","Ork_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Dok","hurt_f_l_arm","Ork_hurt_f_l_arm",0.10,0.58,0)	
Bladex.AddBipedAction("Dok","hurt_f_r_leg","Ork_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Dok","hurt_f_l_leg","Ork_hurt_f_l_leg",0.10,0.56,0)	
Bladex.AddBipedAction("Dok","hurt_jog","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Dok","hurt_head","Ork_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Dok","hurt_breast","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Dok","hurt_back","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Dok","hurt_r_arm","Ork_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Dok","hurt_l_arm","Ork_hurt_f_l_arm",0.10,0.58,0)
Bladex.AddBipedAction("Dok","hurt_r_leg","Ork_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Dok","hurt_l_leg","Ork_hurt_f_l_leg",0.10,0.56,0)



####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Dok","dth_c1", "Ork_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_c2", "Ork_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_c3", "Ork_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_c4", "Ork_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_c5", "Ork_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_c6", "Ork_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_c7", "Ork_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth0",   "Ork_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_n00","Ork_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_n01","Ork_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_n02","Ork_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_n03","Ork_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_n04","Ork_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_n05","Ork_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_n06","Ork_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Dok","dth_rock","Ork_dth_rock",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_rockfront","Ork_dth_rockfront",0.0,1.0,0)
Bladex.AddBipedAction("Dok","dth_burn","Ork_dth_burn",0.0,1.0,0)	







