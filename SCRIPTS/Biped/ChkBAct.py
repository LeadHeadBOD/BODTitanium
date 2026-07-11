##///
##||| ChkBAct.PY TITANIUM
##||| Change list:
##||| * Added unused rlx_no anim
##||| * No longer causes critical errors when spawned with no shield
##\\\ 

import Bladex

#import AnimationSets


#AnimationSets.LoadChkAnimationSet("Chk")

####################################################################################
#
# Escalar + saltos
#
####################################################################################

#Bladex.AddBipedAction("Chk","clmb_low_1h","Chk_clmb_low_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Chk","clmb_medlow_1h","Chk_clmb_medlow_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Chk","clmb_medium_1h","Chk_clmb_medium_1h",0.0,1.0,0)	
#Bladex.AddBipedAction("Chk","clmb_high_1h","Chk_clmb_high_1h",0.0,1.0,0)	

Bladex.AddBipedAction("Chk","LongJump1H","Wlk_1h_Chk",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","LongJumpNo","Wlk_1h_Chk",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","ShortJump","Wlk_1h_Chk",0.0,1.0,0)	



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Chk","slip","Chk_slip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","slip_b","Chk_slip_b",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","derrape","Chk_derrape",0.0,1.0,0)	


Bladex.AddBipedAction("Chk","appears","Chk_appears",0.0,1.0,0)
Bladex.AddBipedAction("Chk","disappear","Chk_disappear",0.0,1.0,0)
Bladex.AddBipedAction("Chk","powerup","Chk_powerup",0.0,1.0,0)

#Bladex.AddBipedAction("Chk","b1","Chk_b1",0.0,1.0,0)	
#Bladex.AddBipedAction("Chk","b2","Chk_b2",0.0,1.0,0)	
#Bladex.AddBipedAction("Chk","b3","Chk_b3",0.0,1.0,0)



####################################################################################
#
# Heridas
#
####################################################################################

Bladex.AddBipedAction("Chk","df_01","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","df_02","Chk_hurt01",0.0,1.0,0)

Bladex.AddBipedAction("Chk","df_s_broken","Chk_hurt01",0.0,1.0,0)

Bladex.AddBipedAction("Chk","sword_broken","Chk_hurt01",0.143,0.5,0)

Bladex.AddBipedAction("Chk","sw_react","Chk_hurt01",0.143,0.5,0)

	
Bladex.AddBipedAction("Chk","hurt_f_lite","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_f_big","Chk_hurt01",0.0,1.0,0)	

Bladex.AddBipedAction("Chk","hurt_f_head","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_f_breast","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_f_back","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_f_r_arm","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_f_l_arm","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_f_r_leg","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_f_l_leg","Chk_hurt_hip",0.0,1.0,0)	

Bladex.AddBipedAction("Chk","hurt_jog","Chk_hurt_hip",0.0,1.0,0)	

Bladex.AddBipedAction("Chk","hurt_head","Chk_hurt01",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_breast","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_back","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_r_arm","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_l_arm","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_r_leg","Chk_hurt_hip",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","hurt_l_leg","Chk_hurt_hip",0.0,1.0,0)
	
Bladex.AddBipedAction("Chk","dth_c1","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_c2","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_c3","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_c4","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_c5","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_c6","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_c7","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth0",  "Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_n00","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_n01","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_n02","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_n03","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_n04","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_n05","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_n06","Chk_dth0",0.0,1.0,0)

Bladex.AddBipedAction("Chk","dth_rock","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_rockfront","Chk_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Chk","dth_burn","Chk_dth0",0.0,1.0,0)	



####################################################################################
#
# Relax.
#
####################################################################################

Bladex.AddBipedAction("Chk","Rlx_no","Rlx_no_Chk",0.0,1.0,0)		# Previously used "Rlx_1h_Chk" anim		-LeadHead
Bladex.AddBipedAction("Chk","Rlx_1h","Rlx_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Rlx_b","Rlx_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Rlx_2h","Rlx_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Rlx_s","Rlx_f_s_Chk",0.0,1.0,0)

####################################################################################
#
# Pasos.- Andares
#
####################################################################################

#Bladex.AddBipedAction("Chk","LStepUp","Wlk_Chk","WlkUp_Chk",0.0,0.5,0)
#Bladex.AddBipedAction("Chk","RStepUp","Wlk_Chk","WlkUp_Chk",0.5,1.0,0)

#Bladex.AddBipedAction("Chk","LStairsUp","StairsUp_Chk","StairsUpP_Chk",0.0,0.5,0)
#Bladex.AddBipedAction("Chk","RStairsUp","StairsUp_Chk","StairsUpP_Chk",0.5,1.0,0)

#Bladex.AddBipedAction("Chk","LStepDown","Wlk_Chk","WlkDown_Chk",0.0,0.5,0)
#Bladex.AddBipedAction("Chk","RStepDown","Wlk_Chk","WlkDown_Chk",0.5,1.0,0)

#Bladex.AddBipedAction("Chk","LStairsDown","StairsDown_Chk",0.0,0.5,0)
#Bladex.AddBipedAction("Chk","RStairsDown","StairsDown_Chk",0.5,1.0,0)

# Andar hacia atrás
Bladex.AddBipedAction("Chk","WBK_b","Wbk_1h_Chk",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","WBK_no","Wbk_1h_Chk",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","WBK_1h","Wbk_1h_Chk",0.0,1.0,0)		
Bladex.AddBipedAction("Chk","WBK_2h","Wbk_1h_Chk",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","WBK_s","Attack_b_s_Chk",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Chk","WLK_b","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WLK_no","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WLK_1h","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WLK_2h","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WLK_s","Attack_f_s_Chk",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Chk","WBK_JOG_b","Wbk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WBK_JOG_no","Wbk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WBK_JOG_s","Attack_b_s_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WBK_JOG_1h","Wbk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","WBK_JOG_2h","Wbk_1h_Chk",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Chk","JOG_b","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","JOG_no","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","JOG_s","Attack_f_s_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","JOG_1h","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","JOG_2h","Wlk_1h_Chk",0.0,1.0,0)


#Modo sneak
Bladex.AddBipedAction("Chk","SNK_b","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","SNK_no","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","SNK_s","Attack_f_s_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","SNK_1h","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","SNK_2h","Wlk_1h_Chk",0.0,1.0,0)

#Correr con escudo en modo no combate                                       
Bladex.AddBipedAction("Chk","Attack_f_s_nc","Attack_f_s_Chk",0.0,1.0,0)     
Bladex.AddBipedAction("Chk","Attack_b_s_nc","Attack_b_s_Chk",0.0,1.0,0)     
                                                                          
####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Chk","FllLow","Rlx_1h_Chk",0,0.1,0)
Bladex.AddBipedAction("Chk","FllMed","Rlx_1h_Chk",0,0.1,0)
Bladex.AddBipedAction("Chk","FllHigh","Rlx_1h_Chk",0,0.1,0)
Bladex.AddBipedAction("Chk","Dth_Fll","Dth_Fll_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Dth_Fll2","Dth_Fll2_Chk",0.0,1.0,0)



####################################################################################
#
# Animaciones en combate
#
####################################################################################

#Movement with no shield (to prevent critical errors when no shield is equipped) -LeadHead
Bladex.AddBipedAction("Chk","Attack_f","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Attack_b","Attack_b_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Attack_r","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Attack_l","Wlk_1h_Chk",0.0,1.0,0)

#MOvement witht shield
Bladex.AddBipedAction("Chk","Attack_f_2h","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Attack_b_2h","Attack_b_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Attack_r_2h","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Attack_l_2h","Wlk_1h_Chk",0.0,1.0,0)

#Movement with shield held high
Bladex.AddBipedAction("Chk","Shattack_f_2h","Attack_f_s_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Shattack_b_2h","Attack_b_s_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Shattack_r_2h","Wlk_1h_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Shattack_l_2h","Wlk_1h_Chk",0.0,1.0,0)

#Relax
Bladex.AddBipedAction("Chk","Rlx_f_1h","Rlx_f_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Rlx_f_2h","Rlx_f_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Rlx_block","Rlx_f_s_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","Shattack_rlx_2h","Rlx_f_s_Chk",0.0,1.0,0)

#Quick turns
#Bladex.AddBipedAction("Chk","Attack_t_r","Chk_t_r_1h",0.0,1.0,0)
#Bladex.AddBipedAction("Chk","Attack_t_r_s","Chk_t_r_1h",0.0,1.0,0)
#Bladex.AddBipedAction("Chk","Attack_t_l","Chk_t_l_1h",0.0,1.0,0)
#Bladex.AddBipedAction("Chk","Attack_t_l_s","Chk_t_l_1h",0.0,1.0,0)


#Dodges
Bladex.AddBipedAction("Chk","D_b","Rlx_f_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","D_l","Rlx_f_Chk",0.0,1.0,0)
Bladex.AddBipedAction("Chk","D_r","Rlx_f_Chk",0.0,1.0,0)



####################################################################################
#
# Ataques
#
####################################################################################

Bladex.AddBipedAction("Chk","g_08","Chk_g_08",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","g_01","Chk_g_01",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","g_02","Chk_g_02",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","g_07","Chk_g_07",0.0,1.0,0)	
Bladex.AddBipedAction("Chk","g_18","Chk_g_18",0.0,0.788,0)
Bladex.AddBipedAction("Chk","g_12","Chk_g_12",0.0,1.0,0)
Bladex.AddBipedAction("Chk","g_31","Chk_g_31",0.0,1.0,0)
Bladex.AddBipedAction("Chk","g_magic","Chk_g_magic",0.0,1.0,0)



