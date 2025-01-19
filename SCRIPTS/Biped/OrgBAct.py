##///
##||| ORGBACT.PY TITANIUM
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

Bladex.AddBipedAction("Org","clmb_low_1h","Ork_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Org","clmb_medlow_1h","Ork_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Org","clmb_medium_1h","Ork_clmb_medium_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Org","clmb_high_1h","Ork_clmb_medium_1h",0.0,1.0,0)	

Bladex.AddBipedAction("Org","LongJump1H","Ork_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Org","LongJumpNo","Ork_jmp_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Org","ShortJump","Ork_jmp_1h",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Org","slip","Ork_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Org","slip_b","Ork_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Org","derrape","Ork_derrape",0.0,1.0,0)	


Bladex.AddBipedAction("Org","b1","Ork_b1",0.0,1.0,0)	
Bladex.AddBipedAction("Org","b2","Ork_b2",0.0,1.0,0)	
Bladex.AddBipedAction("Org","b3","Ork_b3",0.0,1.0,0)	




####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Org","Rlx_no","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","Rlx_1h","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","Rlx_b","Rlx_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","Rlx_2h","Rlx_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","Rlx_s","Rlx_1h_Ork",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Org","LStepUp","Wlk_Ork","WlkUp_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Org","RStepUp","Wlk_Ork","WlkUp_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Org","LStairsUp","StairsUp_Ork","StairsUpP_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Org","RStairsUp","StairsUp_Ork","StairsUpP_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Org","LStepDown","Wlk_Ork","WlkDown_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Org","RStepDown","Wlk_Ork","WlkDown_Ork",0.5,1.0,0)

#Bladex.AddBipedAction("Org","LStairsDown","StairsDown_Ork",0.0,0.5,0)
#Bladex.AddBipedAction("Org","RStairsDown","StairsDown_Ork",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Org","WBK_b","Wbk_b_Ork",0.0,1.0,0)	
Bladex.AddBipedAction("Org","WBK_no","Ork_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Org","WBK_1h","Ork_attack_b",0.0,1.0,0)		
Bladex.AddBipedAction("Org","WBK_2h","Ork_attack_b",0.0,1.0,0)	
Bladex.AddBipedAction("Org","WBK_s","Ork_attack_b",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Org","WLK_b","Wlk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","WLK_no","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","WLK_1h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","WLK_2h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","WLK_s","Wlk_1h_Ork",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Org","WBK_JOG_b","Wbk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","WBK_JOG_no","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Org","WBK_JOG_s","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Org","WBK_JOG_1h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Org","WBK_JOG_2h","Ork_attack_b",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Org","JOG_b","Jog_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","JOG_no","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","JOG_s","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","JOG_1h","Jog_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","JOG_2h","Jog_1h_Ork",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Org","SNK_b","Wlk_b_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","SNK_no","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","SNK_s","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","SNK_1h","Wlk_1h_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","SNK_2h","Wlk_1h_Ork",0.0,1.0,0)

#Correr con escudo en modo no combate                                       
Bladex.AddBipedAction("Org","Attack_f_s_nc","Ork_attack_f_s",0.0,1.0,0)     
Bladex.AddBipedAction("Org","Attack_b_s_nc","Ork_attack_b_s",0.0,1.0,0)     
                                                                          
####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Org","FllLow","FallMed_Ork",0.37,0.8,0)
Bladex.AddBipedAction("Org","FllMed","FallMed_Ork",0.37,0.8,0)
Bladex.AddBipedAction("Org","FllHigh","FallHigh_Ork",0.1,0.8,0)
Bladex.AddBipedAction("Org","Dth_Fll","Dth_Fll_Ork",0.0,1.0,0)
Bladex.AddBipedAction("Org","Dth_Fll2","Dth_Fll2_Ork",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#MOvement without shield
Bladex.AddBipedAction("Org","Attack_f_1h","Ork_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Org","Attack_b_1h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Org","Attack_r_1h","Ork_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Org","Attack_l_1h","Ork_attack_l",0.0,1.0,0)

Bladex.AddBipedAction("Org","Attack_f_2h","Ork_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Org","Attack_b_2h","Ork_attack_b",0.0,1.0,0)
Bladex.AddBipedAction("Org","Attack_r_2h","Ork_attack_r",0.0,1.0,0)
Bladex.AddBipedAction("Org","Attack_l_2h","Ork_attack_l",0.0,1.0,0)

#Movement with shield
Bladex.AddBipedAction("Org","Shattack_f_2h","Ork_attack_f_s",0.0,1.0,0)
Bladex.AddBipedAction("Org","Shattack_b_2h","Ork_attack_b_s",0.0,1.0,0)
Bladex.AddBipedAction("Org","Shattack_r_2h","Ork_attack_r_s",0.0,1.0,0)
Bladex.AddBipedAction("Org","Shattack_l_2h","Ork_attack_l_s",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Org","Rlx_f_1h","Ork_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Org","Rlx_f_2h","Ork_attack_rlx",0.0,1.0,0)
Bladex.AddBipedAction("Org","Shattack_rlx_2h","Ork_attack_rlx_s",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Org","Attack_t_r","Ork_attack_t_r",0.0,1.0,0)
#Bladex.AddBipedAction("Org","Attack_t_r_s","Ork_attack_t_r_s",0.0,1.0,0)
#Bladex.AddBipedAction("Org","Attack_t_l","Ork_attack_t_l",0.0,1.0,0)
#Bladex.AddBipedAction("Org","Attack_t_l_s","Ork_attack_t_l_s",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Org","D_b","Ork_d_b",0.0,1.0,0)
Bladex.AddBipedAction("Org","D_l","Ork_d_l",0.0,1.0,0)
Bladex.AddBipedAction("Org","D_r","Ork_d_r",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################
	
Bladex.AddBipedAction("Org","g_01","Ork_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Org","g_02","Ork_g_02",0.0,1.0,0)	
Bladex.AddBipedAction("Org","g_06","Ork_g_06",0.0,1.0,0)	
Bladex.AddBipedAction("Org","g_15","Ork_g_15",0.0,1.0,0)
Bladex.AddBipedAction("Org","g_16","Ork_g_16",0.0,1.0,0)	
Bladex.AddBipedAction("Org","g_18","Ork_g_18",0.0,1.0,0)






####################################################################################
#
# Animaciones de vigia
#
####################################################################################


Bladex.AddBipedAction("Org","Wai_01","Ork_wai_01",0.0,1.0,0)
Bladex.AddBipedAction("Org","Wai_02","Ork_wai_02",0.0,1.0,0)

Bladex.AddBipedAction("Org","alarm01","Ork_alarm01",0.0,1.0,0)

Bladex.AddBipedAction("Org","patrol1","Ork_patrol1",0.0,1.0,0)
Bladex.AddBipedAction("Org","patrol2","Ork_patrol2",0.0,1.0,0)
Bladex.AddBipedAction("Org","fury","Ork_fury",0.0,1.0,0)

Bladex.AddBipedAction("Org","attack_look","Ork_attack_look",0.0,1.0,0)

Bladex.AddBipedAction("Org","order","Ork_order",0.0,1.0,0)

Bladex.AddBipedAction("Org","insult","Ork_insult",0.0,1.0,0)




####################################################################################
#
# Cambio de armas
#
####################################################################################


Bladex.AddBipedAction("Org","Attack_Chg_r_l","Ork_attack_chg_r_l",0.0,1.0,0)
Bladex.AddBipedAction("Org","Chg_r_l","Ork_attack_chg_r_l",0.0,1.0,0)

Bladex.AddBipedAction("Org","attack_drink","Ork_attack_drink",0.0,1.0,0)


####################################################################################
#
# Reacciones
#
####################################################################################


Bladex.AddBipedAction("Org","df_01","Ork_df_01",0.10,0.48,0)	
Bladex.AddBipedAction("Org","df_02","Ork_df_02",0.10,0.67,0)

Bladex.AddBipedAction("Org","sw_react","Ork_df_s_broken",0.35,1.0,0)

Bladex.AddBipedAction("Org","df_s_broken","Ork_df_s_broken",0.0,1.0,0)



	
Bladex.AddBipedAction("Org","hurt_f_lite","Ork_hurt_f_lite",0.14,0.65,0)	
Bladex.AddBipedAction("Org","hurt_f_big","Ork_hurt_f_big",0.10,0.59,0)	
Bladex.AddBipedAction("Org","hurt_f_head","Ork_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Org","hurt_f_breast","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Org","hurt_f_back","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Org","hurt_f_r_arm","Ork_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Org","hurt_f_l_arm","Ork_hurt_f_l_arm",0.10,0.58,0)	
Bladex.AddBipedAction("Org","hurt_f_r_leg","Ork_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Org","hurt_f_l_leg","Ork_hurt_f_l_leg",0.10,0.56,0)	
Bladex.AddBipedAction("Org","hurt_jog","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Org","hurt_head","Ork_hurt_f_head",0.11,0.60,0)	
Bladex.AddBipedAction("Org","hurt_breast","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Org","hurt_back","Ork_hurt_f_back",0.10,0.58,0)	
Bladex.AddBipedAction("Org","hurt_r_arm","Ork_hurt_f_r_arm",0.10,0.55,0)	
Bladex.AddBipedAction("Org","hurt_l_arm","Ork_hurt_f_l_arm",0.10,0.58,0)
Bladex.AddBipedAction("Org","hurt_r_leg","Ork_hurt_f_r_leg",0.10,0.54,0)	
Bladex.AddBipedAction("Org","hurt_l_leg","Ork_hurt_f_l_leg",0.10,0.56,0)



####################################################################################
#
# MUERTES
#
####################################################################################

Bladex.AddBipedAction("Org","dth_c1", "Ork_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_c2", "Ork_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_c3", "Ork_dth_c3",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_c4", "Ork_dth_c4",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_c5", "Ork_dth_c5",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_c6", "Ork_dth_c6",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_c7", "Ork_dth_c7",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth0",   "Ork_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_n00","Ork_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_n01","Ork_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_n02","Ork_dth_n02",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_n03","Ork_dth_n03",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_n04","Ork_dth_n04",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_n05","Ork_dth_n05",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_n06","Ork_dth_n06",0.0,1.0,0)

Bladex.AddBipedAction("Org","dth_rock","Ork_dth_rock",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_rockfront","Ork_dth_rockfront",0.0,1.0,0)
Bladex.AddBipedAction("Org","dth_burn","Ork_dth_burn",0.0,1.0,0)	







