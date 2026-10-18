##///
##||| TrlBAct.PY TITANIUM
##||| Change list:
##||| * Restored missing head hit reaction
##\\\ 

import Bladex

#import AnimationSets


#AnimationSets.LoadTrlAnimationSet("Trl")

############################################
#
#Relax
#
############################################

Bladex.AddBipedAction("Trl","Rlx_1h","Trl_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","Rlx_f_s","Trl_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","Rlx_no","Trl_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Rlx_b","Trl_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Rlx_2h","Trl_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Rlx_s","Trl_rlx_1h",0.0,1.0,0)



############################################
#
#Animaciones en combate
#
############################################


Bladex.AddBipedAction("Trl","Attack_f_1h","Trl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_b_1h","Trl_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_r_1h","Trl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_l_1h","Trl_attack_f",0.0,1.0,0)

Bladex.AddBipedAction("Trl","Attack_f_2h","Trl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_b_2h","Trl_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_r_2h","Trl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_l_2h","Trl_attack_f",0.0,1.0,0)

Bladex.AddBipedAction("Trl","Attack_f_s","Trl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_b_s","Trl_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_l_s","Trl_attack_f",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_r_s","Trl_attack_f",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","Rlx_f_1h","Trl_rlx_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","Rlx_f_2h","Trl_rlx_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Attack_rlx_s","Trl_rlx_1h",0.0,1.0,0)

############################################
#
#Ataques
#
############################################


Bladex.AddBipedAction("Trl","g_01","Trl_g_01",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_02","Trl_g_02",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_04","Trl_g_04",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_06","Trl_g_06",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_12","Trl_g_12",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_18","Trl_g_18",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_19","Trl_g_19",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_31","Trl_g_31",0.0,1.0,0)
Bladex.AddBipedAction("Trl","g_run","Trl_g_run",0.0,1.0,0)




####################################################################################
#
# Pasos.- Andares
#
####################################################################################



# Andar hacia atrás
Bladex.AddBipedAction("Trl","WBK_b","Trl_wbk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","WBK_no","Trl_wbk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","WBK_1h","Trl_wbk_no",0.0,1.0,0)		
Bladex.AddBipedAction("Trl","WBK_2h","Trl_wbk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","WBK_s","Trl_wbk_no",0.0,1.0,0)

#Andar hacia alante
Bladex.AddBipedAction("Trl","WLK_b","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WLK_no","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WLK_1h","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WLK_2h","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WLK_s","Trl_wlk_no",0.0,1.0,0)

#Correr hacia atrás
Bladex.AddBipedAction("Trl","WBK_JOG_b","Trl_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WBK_JOG_no","Trl_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WBK_JOG_s","Trl_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WBK_JOG_1h","Trl_wbk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","WBK_JOG_2h","Trl_wbk_no",0.0,1.0,0)

#Correr hacia delante
Bladex.AddBipedAction("Trl","JOG_b","Trl_jog_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","JOG_no","Trl_jog_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","JOG_s","Trl_jog_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","JOG_1h","Trl_jog_1h",0.0,1.0,0)
Bladex.AddBipedAction("Trl","JOG_2h","Trl_jog_1h",0.0,1.0,0)

#Modo sneak
Bladex.AddBipedAction("Trl","SNK_b","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","SNK_no","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","SNK_s","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","SNK_1h","Trl_wlk_no",0.0,1.0,0)
Bladex.AddBipedAction("Trl","SNK_2h","Trl_wlk_no",0.0,1.0,0)




####################################################################################
#
# Caidas.
#
####################################################################################

Bladex.AddBipedAction("Trl","FllLow","Trl_fll_low_1h",0.37,0.8,0)
Bladex.AddBipedAction("Trl","FllMed","Trl_fll_low_1h",0.37,0.8,0)
Bladex.AddBipedAction("Trl","FllHigh","Trl_fll_low_1h",0.1,0.8,0)
Bladex.AddBipedAction("Trl","Dth_Fll","Dth_Fll_Trl",0.0,1.0,0)
Bladex.AddBipedAction("Trl","Dth_Fll2","Dth_Fll2_Trl",0.0,1.0,0)



####################################################################################
#
# Escaladas
#
####################################################################################

Bladex.AddBipedAction("Trl","clmb_low_1h","Trl_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","clmb_medlow_1h","Trl_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","clmb_medium_1h","Trl_clmb_low_1h",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","clmb_high_1h","Trl_clmb_low_1h",0.0,1.0,0)	



####################################################################################
#
#Heridas
#
####################################################################################



####################################################################################
#
# Others
#
####################################################################################

Bladex.AddBipedAction("Trl","slip","Trl_wlk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","slip_b","Trl_wlk_no",0.0,1.0,0)	
Bladex.AddBipedAction("Trl","derrape","Trl_wlk_no",0.0,1.0,0)	






###################
#                 # 
# Añadidos Luismi #
#                 #
###################



####  Muertes


Bladex.AddBipedAction("Trl","dth_burned","Trl_dth_burned",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_c1","Trl_dth_c1",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_c2","Trl_dth_c2",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_n00","Trl_dth_n00",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_n01","Trl_dth_n01",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth0","Trl_dth0",0.0,1.0,0)

Bladex.AddBipedAction("Trl","dth_c3","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_c4","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_c5","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_c6","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_c7","Trl_dth0",0.0,1.0,0)
# Bladex.AddBipedAction("Trl","dth0",  "Trl_dth0",0.0,1.0,0)  # Commented out, dupe   -LeadHead
Bladex.AddBipedAction("Trl","dth_n02","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_n03","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_n04","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_n05","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_n06","Trl_dth0",0.0,1.0,0)
                       
Bladex.AddBipedAction("Trl","dth_rock","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_rockfront","Trl_dth0",0.0,1.0,0)
Bladex.AddBipedAction("Trl","dth_burn","Trl_dth0",0.0,1.0,0)	



####  Heridas


Bladex.AddBipedAction("Trl","hurt_f_big","Trl_hurt_big",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_f_lite","Trl_hurt_l_arm",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_f_head","Trl_hurt_head",0.0,1.0,0)     # Previously used Trl_hurt_breast   -LeadHead
Bladex.AddBipedAction("Trl","hurt_f_breast","Trl_hurt_breast",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_f_back","Trl_hurt_back",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_f_r_arm","Trl_hurt_r_arm",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_f_l_arm","Trl_hurt_l_arm",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_f_r_leg","Trl_hurt_r_leg",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_f_l_leg","Trl_hurt_l_leg",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_jog","Trl_hurt_jog",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_head","Trl_hurt_head",0.0,1.0,0)      # Previously used Trl_hurt_breast   -LeadHead
Bladex.AddBipedAction("Trl","hurt_breast","Trl_hurt_breast",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_back","Trl_hurt_back",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_r_arm","Trl_hurt_r_arm",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_l_arm","Trl_hurt_l_arm",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_r_leg","Trl_hurt_r_leg",0.0,1.0,0)
Bladex.AddBipedAction("Trl","hurt_l_leg","Trl_hurt_l_leg",0.0,1.0,0)
