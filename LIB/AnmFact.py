##///
##||| ANMFACT.PY TITANIUM
##||| Change list:
##||| * Added b3 transitions for Tkn
##||| * Added transitions for Org and Dok
##||| * Commented out prisoner transition times, they only spam the console 
##||| * Sped up misc anims: LowFall, drink
##\\\ 


######TRANSICIONES: Bladex.AddTranTime("Ork"[personaje],""[anm_fuente],"Attack_f"[anm_destino],0.3[tiempo de interpolación],0/1[opcional la animación sale corrida(1) o no(0)])


import Bladex

#
# Barbarian set
#

def AnmFactBarbarian():
	Bladex.SetAnimationFactor("Bar_g_01",4)
	Bladex.SetAnimationFactor("Bar_g_02",4)
	Bladex.SetAnimationFactor("Bar_g_05",4)
	Bladex.SetAnimationFactor("Bar_g_06",4)
	Bladex.SetAnimationFactor("Bar_g_07",3.5)
	Bladex.SetAnimationFactor("Bar_g_08",4)
	Bladex.SetAnimationFactor("Bar_g_09",4)
	Bladex.SetAnimationFactor("Bar_g_01a",4)
	Bladex.SetAnimationFactor("Bar_g_02a",4)
	Bladex.SetAnimationFactor("Bar_g_05a",4)
	Bladex.SetAnimationFactor("Bar_g_06a",4)
	Bladex.SetAnimationFactor("Bar_g_07a",4)
	Bladex.SetAnimationFactor("Bar_g_08a",4)
	Bladex.SetAnimationFactor("Bar_g_09a",4)

	Bladex.SetAnimationFactor("Bar_g_11",4.7)
	Bladex.SetAnimationFactor("Bar_g_12",3.5)
	Bladex.SetAnimationFactor("Bar_g_13",3.5)
	Bladex.SetAnimationFactor("Bar_g_14",3.5)
	Bladex.SetAnimationFactor("Bar_g_15",3.5)
	Bladex.SetAnimationFactor("Bar_g_16",4.7)
	Bladex.SetAnimationFactor("Bar_g_17",4.7)
	Bladex.SetAnimationFactor("Bar_g_18",4.7)
	Bladex.SetAnimationFactor("Bar_g_19",3.5)

	Bladex.SetAnimationFactor("Bar_g_21",3.5)
	Bladex.SetAnimationFactor("Bar_g_22",3.5)
	Bladex.SetAnimationFactor("Bar_g_23",3.5)
	Bladex.SetAnimationFactor("Bar_g_26",3.5)
	Bladex.SetAnimationFactor("Bar_g_27",3.5)

	Bladex.SetAnimationFactor("Bar_g_31",3.5)
	
	Bladex.SetAnimationFactor("Bar_g_back",3)
	Bladex.SetAnimationFactor("Bar_g2h_21_7",4)
	Bladex.SetAnimationFactor("Bar_g2h_02kata",5.5)
	Bladex.SetAnimationFactor("Bar_g2h_21_2",4)
	Bladex.SetAnimationFactor("Bar_g2h_21_6kata",4.7)
	Bladex.SetAnimationFactor("Bar_g2h_b7",4.5)
	Bladex.SetAnimationFactor("Bar_g2h_b29",3.8)
	Bladex.SetAnimationFactor("Bar_g2h_12low",4)
	Bladex.SetAnimationFactor("Bar_g2h_19",2.7)
	Bladex.SetAnimationFactor("Bar_g2h_26_b6",4)
	Bladex.SetAnimationFactor("Bar_g2h_26",3)
	Bladex.SetAnimationFactor("Bar_g2h_31_2",3)
	Bladex.SetAnimationFactor("Bar_g2h_28",2.5)
	Bladex.SetAnimationFactor("Bar_g2h_b6",5)
	Bladex.SetAnimationFactor("Bar_g2h_b6kata",5)
	Bladex.SetAnimationFactor("Bar_g2h_b6low",3.8)
	Bladex.SetAnimationFactor("Bar_g2h_b6lowkata",3.8)
	Bladex.SetAnimationFactor("Bar_g2h_earthpow",1.45)
	Bladex.SetAnimationFactor("Bar_g2h_s7",3.6)
	Bladex.SetAnimationFactor("Bar_g2h_01",3.5)
	Bladex.SetAnimationFactor("Bar_g2h_02",3.8)
	Bladex.SetAnimationFactor("Bar_g2h_02low",3)
	Bladex.SetAnimationFactor("Bar_g2h_07",3)
	Bladex.SetAnimationFactor("Bar_g2h_08",3.8)
	Bladex.SetAnimationFactor("Bar_g2h_11",3.5)
	Bladex.SetAnimationFactor("Bar_g2h_12",3)
	Bladex.SetAnimationFactor("Bar_g2h_13",3.3)
	Bladex.SetAnimationFactor("Bar_g2h_17",3)
	Bladex.SetAnimationFactor("Bar_g2h_22kata_6",3)
	Bladex.SetAnimationFactor("Bar_g2h_26low_b6",3.6)
	Bladex.SetAnimationFactor("Bar_g2h_26low",3)
	Bladex.SetAnimationFactor("Bar_g2h_back",3)
	Bladex.SetAnimationFactor("Bar_g2h_s1",3)
	Bladex.SetAnimationFactor("Bar_g2h_s8",3.9)
	Bladex.SetAnimationFactor("Bar_g2h_s8kata",3.7)
	Bladex.SetAnimationFactor("Bar_g_axe01",4.3)
	Bladex.SetAnimationFactor("Bar_g_axe02",6.7)
	Bladex.SetAnimationFactor("Bar_g_axe08",3.5)
	Bladex.SetAnimationFactor("Bar_g_axe111",6.7)
	Bladex.SetAnimationFactor("Bar_g_axe211",5.8)
	Bladex.SetAnimationFactor("Bar_g_axe12",5.7)
	Bladex.SetAnimationFactor("Bar_g_axe13",5.9)
	Bladex.SetAnimationFactor("Bar_g_axe18",5.9)
	Bladex.SetAnimationFactor("Bar_g_axe21",4)
	Bladex.SetAnimationFactor("Bar_g_axe28",3.8)
	Bladex.SetAnimationFactor("Bar_g_axe30",4.8)
	Bladex.SetAnimationFactor("Bar_g_axe31",4.8)
	Bladex.SetAnimationFactor("Bar_g_axe32",4.65)
	Bladex.SetAnimationFactor("Bar_g_axe33",5.2)
	Bladex.SetAnimationFactor("Bar_g_axe34",4.4)
	Bladex.SetAnimationFactor("Bar_g_axe_b2kata",3)
	Bladex.SetAnimationFactor("Bar_g_axe08strong",2.6)
	Bladex.SetAnimationFactor("Bar_g_axe_3s2",3)
	Bladex.SetAnimationFactor("Bar_g_axe_32kata_b2",3)
	Bladex.SetAnimationFactor("Bar_g_axe_26kata",3)
	Bladex.SetAnimationFactor("Bar_g_axe_2katab6low",2.4)
	Bladex.SetAnimationFactor("Bar_g_bad_1h",3.6)
	Bladex.SetAnimationFactor("Bar_g_bad_no",3.6)
	Bladex.SetAnimationFactor("Bar_g_bad_spear",4.5)
	Bladex.SetAnimationFactor("Bar_g_bad_spear2",4.5)
	Bladex.SetAnimationFactor("Bar_g_draw_rlx",3.0)
	Bladex.SetAnimationFactor("Bar_g_draw_run",3.0)   
	Bladex.SetAnimationFactor("Bar_g_punch1",3.7)
	Bladex.SetAnimationFactor("Bar_g_punch2",3.3)
	Bladex.SetAnimationFactor("Bar_g_punch3",3.3)
	Bladex.SetAnimationFactor("Bar_g_punch4",3)
	Bladex.SetAnimationFactor("Bar_g_06lowkata_new",4)
	Bladex.SetAnimationFactor("Bar_g_d_r_axe",3)
	Bladex.SetAnimationFactor("Bar_g_d_l_axe",3)
	Bladex.SetAnimationFactor("Bar_parry_2w",2)
	Bladex.SetAnimationFactor("Bar_parry_axe",2)
	Bladex.SetAnimationFactor("Bar_df_01",1.4)
	Bladex.SetAnimationFactor("Bar_df_02",1.4)
	
	Bladex.SetAnimationFactor("Bar_g2h_d_r",3)
	Bladex.SetAnimationFactor("Bar_g2h_d_l",3)
	Bladex.SetAnimationFactor("Bar_g_magic",3)
	Bladex.SetAnimationFactor("Bar_g_magic2",3)	


	
	Bladex.SetAnimationFactor("Bar_1tw_h_f",3)
	Bladex.SetAnimationFactor("Bar_1tw_l_f",3)
	Bladex.SetAnimationFactor("Bar_b1",2)
	Bladex.SetAnimationFactor("Bar_b2",3)
	
	Bladex.SetAnimationFactor("Bar_attack_f",3)
	Bladex.SetAnimationFactor("Bar_attack_f_2w",1.6)
	Bladex.SetAnimationFactor("Bar_attack_b_2w",3)
	Bladex.SetAnimationFactor("Bar_attack_r_2w",1.35)
	Bladex.SetAnimationFactor("Bar_attack_l_2w",1.35)
	Bladex.SetAnimationFactor("Bar_attack_f_axe",1.6)
	Bladex.SetAnimationFactor("Bar_attack_b_axe",3)
	Bladex.SetAnimationFactor("Bar_jmp_no",1.40)
	Bladex.SetAnimationFactor("Bar_jmp_1h",1.40) 
	Bladex.SetAnimationFactor("Bar_jmph0_no",1.50) 




	###movimientos###

	Bladex.SetAnimationFactor("Jog_no_Bar",3.35)
	Bladex.SetAnimationFactor("Jog_1h_Bar",2.7)
	Bladex.SetAnimationFactor("Jog_b_Bar",1.25)
	Bladex.SetAnimationFactor("Wlk_no_Bar",1.6)
	Bladex.SetAnimationFactor("Wlk_1h_Bar",1.7)
	Bladex.SetAnimationFactor("Wlk_2h_Bar",1.7)
	Bladex.SetAnimationFactor("Wlk_2w_Bar",1.55)
	Bladex.SetAnimationFactor("Wlk_axe_Bar",1.55)
	Bladex.SetAnimationFactor("Wlk_s_Bar",1.5)
	Bladex.SetAnimationFactor("Wlk_b_Bar",1.65)
	Bladex.SetAnimationFactor("Wbk_2w_Bar",1.3)
	Bladex.SetAnimationFactor("Wbk_axe_Bar",1.6)
	Bladex.SetAnimationFactor("Wbk_no_Bar",1.5)
	Bladex.SetAnimationFactor("Wbk_1h_Bar",1.5)
	Bladex.SetAnimationFactor("Wbk_b_Bar",1.5)
	Bladex.SetAnimationFactor("Jog_axe_Bar",3.35)
	Bladex.SetAnimationFactor("Jog_2w_Bar",3.4)
	Bladex.SetAnimationFactor("Jog_2h_Bar",3.2)
	Bladex.SetAnimationFactor("Bar_jogb_axe",3.5)
	Bladex.SetAnimationFactor("Bar_wlk_turn",1.7)
	Bladex.SetAnimationFactor("Bar_snk_turn",1.5)
	Bladex.SetAnimationFactor("Bar_jog_turn",1.5)
	Bladex.SetAnimationFactor("Bar_rlx_turn",1.5)
	Bladex.SetAnimationFactor("Bar_rlx_vt",1.25)
	Bladex.SetAnimationFactor("Bar_attack_chg_r_l",1.33)
	Bladex.SetAnimationFactor("Bar_attack_chg_r",1.43)
	Bladex.SetAnimationFactor("Bar_attack_chg_l",1.33)
	Bladex.SetAnimationFactor("Bar_drp_l",1.6)
	Bladex.SetAnimationFactor("Bar_drp_r",1.8)
	Bladex.SetAnimationFactor("Bar_d_b_2w",1.2)
	Bladex.SetAnimationFactor("Bar_g2h_d_l",3.5)
	Bladex.SetAnimationFactor("Bar_g2h_d_r",3.5)
	
	Bladex.SetAnimationFactor("FallLow_Bar",1.8) ### Added -LeadHead
	Bladex.SetAnimationFactor("Bar_drink",1.3)


	#
	# TRANSICIONES DEL BaRbArO
	#
	Bladex.AddTranTime("Bar","","slip",0.3)
	Bladex.AddTranTime("Bar","slip","",0.4)

	Bladex.AddTranTime("Bar","FllHigh","",0.4)

	Bladex.AddTranTime("Bar","","ShortStep",0.3)
	Bladex.AddTranTime("Bar","ShortStep","",0.4)
	
	Bladex.AddTranTime("Bar","","g_d_l_axe",0.05,0)
	Bladex.AddTranTime("Bar","","g_d_r_axe",0.2,0)
	Bladex.AddTranTime("Bar","","g2h_d_r",0.05,0)
	Bladex.AddTranTime("Bar","","g2h_d_l",0.05,0)

	#Ejemplo de golpes -> Faltan muchos!
	Bladex.AddTranTime("Bar","g_08","g_01",0.1)
	Bladex.AddTranTime("Bar","g_08","g_02",0.05)
	
	"""### Smooth transitions for special attacks
	
	Bladex.AddTranTime("Bar","g_07","g_16",0.2)                 # 
	
	Bladex.AddTranTime("Bar","g_16","g_06lowkata_new",0.15)     # 
	
	Bladex.AddTranTime("Bar","g2h_b6kata","g2h_b7",0.25)        # Added, don't forget
	Bladex.AddTranTime("Bar","g2h_11","g2h_02kata",0.25)        #   -LeadHead
	Bladex.AddTranTime("Bar","g2h_s7","g2h_01",0.25)            #
	Bladex.AddTranTime("Bar","g2h_12low","g2h_02low",0.15)      #
	
	Bladex.AddTranTime("Bar","g2h_08","g2h_21_6kata",0.25)      #
	Bladex.AddTranTime("Bar","g2h_21_6kata","g2h_26_b6",0.25)   #
	
	Bladex.AddTranTime("Bar","g2h_b6kata","g2h_b6",0.24)        #
	
	Bladex.AddTranTime("Bar","g2h_b6kata","g2h_b6low",0.24)     #
	
	Bladex.AddTranTime("Bar","g2h_s7","g2h_13",0.18)            #
	
	Bladex.AddTranTime("Bar","g_axe02","g_axe33",0.24)          #

	Bladex.AddTranTime("Bar","g2h_02low","g2h_s8",0.20)         #

	Bladex.AddTranTime("Bar","g2h_b6kata","g2h_b29",0.28)       #

	Bladex.AddTranTime("Bar","g_axe13","g_axe34",0.24)          #
	
	Bladex.AddTranTime("Bar","g2h_08","g2h_28",0.25)            #
	
	Bladex.AddTranTime("Bar","g_axe08","g_axe30",0.15)          # To add later - Spike of Evil
                                                                # 
	# Bladex.AddTranTime("Bar","g_axe02","g_axe32",0.15)        # Overkill - Doom Axe. Currently does nothing because of overlap, needs adjustments to HitItp.
	
	Bladex.AddTranTime("Bar","g2h_b6kata","g2h_21_7",0.3)       #
	
	Bladex.AddTranTime("Bar","g2h_08","g_magic",0.45)           #
	Bladex.AddTranTime("Bar","g2h_08","g_magic2",0.55)          #

	Bladex.AddTranTime("Bar","g2h_21_6kata","g2h_21_2",0.25)    #
	Bladex.AddTranTime("Bar","g2h_26_b6","g2h_earthpow",0.75)   #

	Bladex.AddTranTime("Bar","","g_bad_sword",0.38)             # Parry animations do not get interpolated, perhaps because of ItpEvent
	Bladex.AddTranTime("Bar","","g_bad_spear2",0.38)            # or it's just the engine failing to understand what states is the character going from to.
	"""
                                                                
                                                                
	Bladex.AddTranTime("Bar","SNK","WLK",0.25)
	Bladex.AddTranTime("Bar","WLK","SNK",0.4)
	Bladex.AddTranTime("Bar","","SNK",0.6)

	Bladex.AddTranTime("Bar","JOG","WLK",0.3)
	Bladex.AddTranTime("Bar","WLK","JOG",0.27)
	Bladex.AddTranTime("Bar","","WLK",0.2)
	Bladex.AddTranTime("Bar","","wlk_turn",0.3)
	Bladex.AddTranTime("Bar","","jog_turn",0.2)
	Bladex.AddTranTime("Bar","LongJump1H","JOG",0.3)
	Bladex.AddTranTime("Bar","","LongJump1H",0.3)
	Bladex.AddTranTime("Bar","","LongJumpNo",0.3)
	Bladex.AddTranTime("Bar","","ShortJump",0.3)
	Bladex.AddTranTime("Bar","","JOG",0.2)
	Bladex.AddTranTime("Bar","","WBK_JOG",0.2)
	Bladex.AddTranTime("Bar","","WBK",0.2)
	Bladex.AddTranTime("Bar","WBK","JOG",0.2)
	Bladex.AddTranTime("Bar","WBK_JOG","JOG",0.2)


	Bladex.AddTranTime("Bar","","Rlx",0.35)
	Bladex.AddTranTime("Bar","Rlx","JOG",0.3)
	Bladex.AddTranTime("Bar","","Rlx_f",0.4)
	Bladex.AddTranTime("Bar","","Attack_rlx_s",0.2)

	Bladex.AddTranTime("Bar","","Attack_l_s",0.2)
	Bladex.AddTranTime("Bar","","Attack_l"  ,0.2)
	Bladex.AddTranTime("Bar","","Attack_r_s",0.2)
	Bladex.AddTranTime("Bar","","Attack_r"  ,0.2)
	Bladex.AddTranTime("Bar","","Attack_f_s",0.2)
	Bladex.AddTranTime("Bar","","Attack_f"  ,0.2)
	Bladex.AddTranTime("Bar","","Attack_b_s",0.2)
	Bladex.AddTranTime("Bar","","Attack_b"  ,0.2)
	Bladex.AddTranTime("Bar","","Rlx_vt",0.75)
	Bladex.AddTranTime("Bar","Rlx_vt","",0.25,0)
	Bladex.AddTranTime("Bar","","b3",0.3,0)






#
# Caballero set
#
def AnmFactKnight():
	Bladex.SetAnimationFactor("Kgt_hit_l",0.75)
	Bladex.SetAnimationFactor("Kgt_hit_r",0.75)
	Bladex.SetAnimationFactor("Kgt_g_01",3.2) 
	Bladex.SetAnimationFactor("Kgt_g_02",3.6)
	Bladex.SetAnimationFactor("Kgt_g_05",2.8)
	Bladex.SetAnimationFactor("Kgt_g_06",3.2)
	Bladex.SetAnimationFactor("Kgt_g_07",2.8)
	Bladex.SetAnimationFactor("Kgt_g_08",2.6)
	Bladex.SetAnimationFactor("Kgt_g_09",2.8)
	Bladex.SetAnimationFactor("Kgt_g_01a",4)
	Bladex.SetAnimationFactor("Kgt_g_02a",4)
	Bladex.SetAnimationFactor("Kgt_g_05a",4)
	Bladex.SetAnimationFactor("Kgt_g_06a",4)
	Bladex.SetAnimationFactor("Kgt_g_07a",4)
	Bladex.SetAnimationFactor("Kgt_g_08a",4)
	Bladex.SetAnimationFactor("Kgt_g_09a",4)

	Bladex.SetAnimationFactor("Kgt_g_11",3.5)
	Bladex.SetAnimationFactor("Kgt_g_12",3.5)
	Bladex.SetAnimationFactor("Kgt_g_13",3.5)
	Bladex.SetAnimationFactor("Kgt_g_14",3.5)
	Bladex.SetAnimationFactor("Kgt_g_15",3.5)
	Bladex.SetAnimationFactor("Kgt_g_16",3.5)
	Bladex.SetAnimationFactor("Kgt_g_17",3.5)
	Bladex.SetAnimationFactor("Kgt_g_18",3.5)
	Bladex.SetAnimationFactor("Kgt_g_19",3.5)

	Bladex.SetAnimationFactor("Kgt_g_21",3.5)
	Bladex.SetAnimationFactor("Kgt_g_22",3.5)
	Bladex.SetAnimationFactor("Kgt_g_23",3.5)
	Bladex.SetAnimationFactor("Kgt_g_26",3.5)
	Bladex.SetAnimationFactor("Kgt_g_27",3.5)

	Bladex.SetAnimationFactor("Kgt_g_31",3.5)
	 
	Bladex.SetAnimationFactor("Kgt_g_magic2",3)
	Bladex.SetAnimationFactor("Kgt_g_3s9_6new",4.2)
	Bladex.SetAnimationFactor("Kgt_g_28new",3)
	Bladex.SetAnimationFactor("Kgt_g_12_7_s1new",3.3)
	Bladex.SetAnimationFactor("Kgt_g_21_6_s8new",3)
	Bladex.SetAnimationFactor("Kgt_g_32_5_3new",3.6)
	Bladex.SetAnimationFactor("Kgt_g_29_3new",2.7)
	Bladex.SetAnimationFactor("Kgt_g_back",3)
	Bladex.SetAnimationFactor("Kgt_g_07_01_19_26low_new",3)
	Bladex.SetAnimationFactor("Kgt_g_19_bs1_new",4)
	Bladex.SetAnimationFactor("Kgt_g_01_7_new",3.7)
	Bladex.SetAnimationFactor("Kgt_g_01_new",3.3)
	Bladex.SetAnimationFactor("Kgt_g_01low_new",4.1)
	Bladex.SetAnimationFactor("Kgt_g_02_new",4.2)
	Bladex.SetAnimationFactor("Kgt_g_06lowkata_new",4)
	Bladex.SetAnimationFactor("Kgt_g_07_new",4)
	Bladex.SetAnimationFactor("Kgt_g_08_new",4.1)
	Bladex.SetAnimationFactor("Kgt_g_09_07_s6low_new",3.6)
	Bladex.SetAnimationFactor("Kgt_g_12_new",4)
	Bladex.SetAnimationFactor("Kgt_g_18_11_22_new",3.6)
	Bladex.SetAnimationFactor("Kgt_g_22kata_23_new",3)
	Bladex.SetAnimationFactor("Kgt_g_22lowkata_new",4.1)
	Bladex.SetAnimationFactor("Kgt_g_b06_new",4.5)
	Bladex.SetAnimationFactor("Kgt_g_27kata_new",3.5)
	Bladex.SetAnimationFactor("Kgt_g_26low_new",3)
	Bladex.SetAnimationFactor("Kgt_g_b32kata_new",4.8)
	Bladex.SetAnimationFactor("Kgt_g_s18_new",3)
	Bladex.SetAnimationFactor("Kgt_g_s19_new",4.5)
	Bladex.SetAnimationFactor("Kgt_g_s22low_new",3.3)
	Bladex.SetAnimationFactor("Kgt_g_s28kata_new",3.3)
	Bladex.SetAnimationFactor("Kgt_g_s3_new",3.5)
	Bladex.SetAnimationFactor("Kgt_g_sb25_new",3.7)
	Bladex.SetAnimationFactor("Kgt_g_draw_rlx",3.0)
	Bladex.SetAnimationFactor("Kgt_g_draw_run",3.0)
	Bladex.SetAnimationFactor("Kgt_g_bad_axe",5.5)
	Bladex.SetAnimationFactor("Kgt_g_bad_spear",4)
	Bladex.SetAnimationFactor("Kgt_g_bad_spear2",4)
	Bladex.SetAnimationFactor("Kgt_g_bad_sword",3.6)
	Bladex.SetAnimationFactor("Kgt_g_bad_1h",3.6)
	Bladex.SetAnimationFactor("Kgt_g_bad_no",3.6)
	Bladex.SetAnimationFactor("Kgt_g_bad_sword2",3.7)
	Bladex.SetAnimationFactor("Kgt_g_bad_sword3",3.5)
	Bladex.SetAnimationFactor("Kgt_g_punch1",3.7)
	Bladex.SetAnimationFactor("Kgt_g_punch2",3.7)
	Bladex.SetAnimationFactor("Kgt_g_kick",4.4)
	Bladex.SetAnimationFactor("Kgt_d_b",3.7)
	Bladex.SetAnimationFactor("Kgt_g_d_r",1.2)
	Bladex.SetAnimationFactor("Kgt_g_d_l",3.9)

	#Bladex.SetAnimationFactor("Kgt_attack_t_r",0.1)
	#Bladex.SetAnimationFactor("Kgt_attack_t_l",0.1)
	Bladex.SetAnimationFactor("Kgt_1tw_h_f",3)
	Bladex.SetAnimationFactor("Kgt_1tw_l_f",3)
	Bladex.SetAnimationFactor("Kgt_b1",2)
	Bladex.SetAnimationFactor("Kgt_b2",3)
	Bladex.SetAnimationFactor("Kgt_g_magic",3)
		
	Bladex.SetAnimationFactor("Kgt_jmp_no",1.25) 
	Bladex.SetAnimationFactor("Kgt_jmp_1h",1.25) 
	Bladex.SetAnimationFactor("Kgt_jmph0_no",1.3) 
	Bladex.SetAnimationFactor("Kgt_sword_reaction",0.7)
	Bladex.SetAnimationFactor("Kgt_parry2w",1.5)
	Bladex.SetAnimationFactor("Kgt_parryspear",1.5)


	###movimientos###

	Bladex.SetAnimationFactor("Kgt_attack_f",1.35)
	Bladex.SetAnimationFactor("Kgt_attack_b",1.1)
	Bladex.SetAnimationFactor("Kgt_attack_r",1.2)
	Bladex.SetAnimationFactor("Kgt_attack_l",1.2)
	Bladex.SetAnimationFactor("Jog_no_Kgt",3.5)
	Bladex.SetAnimationFactor("Jog_b_Kgt",1.3)
	Bladex.SetAnimationFactor("Jog_1h_Kgt",3.6)
	Bladex.SetAnimationFactor("Wlk_no_Kgt",1.35)
	Bladex.SetAnimationFactor("Wlk_b_Kgt",1.45)
	Bladex.SetAnimationFactor("Wbk_b_Kgt",2.3)
	Bladex.SetAnimationFactor("Wlk_1h_Kgt",1.5)
	Bladex.SetAnimationFactor("Wlk_2h_Kgt",1.5)
	Bladex.SetAnimationFactor("Wlk_s_Kgt",1.35)
	Bladex.SetAnimationFactor("Kgt_wlk_turn",1.6)
	Bladex.SetAnimationFactor("Kgt_snk_turn",1.7)
	Bladex.SetAnimationFactor("Kgt_jog_turn",1.5)
	Bladex.SetAnimationFactor("Kgt_jogb_2h",1.2)
	Bladex.SetAnimationFactor("Kgt_jogb_no",1.2)
	Bladex.SetAnimationFactor("Kgt_jogb_1h",1.2)
	Bladex.SetAnimationFactor("Kgt_jogb_s",1.2)
	Bladex.SetAnimationFactor("Kgt_jmph0_no",1.7)
	Bladex.SetAnimationFactor("Kgt_jmp_no",1.6)
	Bladex.SetAnimationFactor("Kgt_jmp_1h",1.5)
	Bladex.SetAnimationFactor("Kgt_rlx_turn",1.5)
	Bladex.SetAnimationFactor("Wbk_no_Kgt",2)
	Bladex.SetAnimationFactor("Wbk_2h_Kgt",2)
	Bladex.SetAnimationFactor("Wbk_1h_Kgt",2.2)
	Bladex.SetAnimationFactor("Kgt_rlx_vt",1.25)
	Bladex.SetAnimationFactor("Kgt_g_d_l",4.6)
	Bladex.SetAnimationFactor("Kgt_g_d_r",1.3)
	Bladex.SetAnimationFactor("Kgt_d_b",3.9)
	Bladex.SetAnimationFactor("Kgt_attack_chg_r_l",1.2)
	Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)
	Bladex.SetAnimationFactor("Kgt_attack_chg_l",1.5)
	Bladex.SetAnimationFactor("Kgt_drp_l",1.6)
	Bladex.SetAnimationFactor("Kgt_drp_r",1.6)
	Bladex.SetAnimationFactor("Kgt_tke_r_01",1.4)
	Bladex.SetAnimationFactor("Kgt_tke_r_02",1.4)
	Bladex.SetAnimationFactor("Kgt_tke_r_03",1.4)
	Bladex.SetAnimationFactor("Kgt_tke_r_04",1.4)
	
	Bladex.SetAnimationFactor("Kgt_attack_l_s",1.5)  
	Bladex.SetAnimationFactor("Kgt_attack_r_s",1.5)
	Bladex.SetAnimationFactor("Kgt_attack_f_s",1.5)
	Bladex.SetAnimationFactor("Kgt_attack_b_s",1.5)

	Bladex.SetAnimationFactor("FallLow_Kgt",1.8) ### Added -LeadHead
	Bladex.SetAnimationFactor("Kgt_drink",1.3)

	#
	# TRANSICIONES DEL CABALLERO
	#
	Bladex.AddTranTime("Knight","","slip",0.3)
	Bladex.AddTranTime("Knight","slip","",0.4)

	Bladex.AddTranTime("Knight","FllHigh","",0.4)

	Bladex.AddTranTime("Knight","","ShortStep",0.3)
	Bladex.AddTranTime("Knight","ShortStep","",0.4)
	Bladex.AddTranTime("Knight","","b3",0.3,0)


	#Ejemplo de golpes -> Faltan muchos!


	Bladex.AddTranTime("Knight","SNK","WLK",0.25)
	Bladex.AddTranTime("Knight","WLK","SNK",0.4)
	Bladex.AddTranTime("Knight","","SNK",0.6)

    
	Bladex.AddTranTime("Knight","","WLK",0.2)
	Bladex.AddTranTime("Knight","JOG","WLK",0.3)
	Bladex.AddTranTime("Knight","","JOG",0.2)
	Bladex.AddTranTime("Knight","WBK","JOG",0.2)
	Bladex.AddTranTime("Knight","","WBK_JOG",0.2)
	Bladex.AddTranTime("Knight","WBK_JOG","JOG",0.2)
	Bladex.AddTranTime("Knight","","WBK",0.2)
	Bladex.AddTranTime("Knight","","Wlk_turn",0.3)
	Bladex.AddTranTime("Knight","","Rlx_turn",0.25)
	Bladex.AddTranTime("Knight","","jog_turn",0.25)

	Bladex.AddTranTime("Knight","","Rlx",0.35)
	Bladex.AddTranTime("Knight","Rlx","JOG",0.3)
	Bladex.AddTranTime("Knight","","Rlx_f",0.25)
	Bladex.AddTranTime("Knight","","Attack_rlx_s",0.2)
	#Bladex.AddTranTime("Knight","","LongJump1H",0.2)
	Bladex.AddTranTime("Knight","","jmph0_no",0.2)
	Bladex.AddTranTime("Knight","","jmp_1h",0.2)
	Bladex.AddTranTime("Knight","","jmp_no",0.2)
	Bladex.AddTranTime("Knight","","1tw_h_f",0.3)
	#Bladex.AddTranTime("Knight","","drp_r",0.1)
	#Bladex.AddTranTime("Knight","","drp_l",0.1)

	Bladex.AddTranTime("Knight","","Attack_l_s",0.2)
	Bladex.AddTranTime("Knight","","Attack_l"  ,0.2)
	Bladex.AddTranTime("Knight","","Attack_r_s",0.2)
	Bladex.AddTranTime("Knight","","Attack_r"  ,0.2)
	Bladex.AddTranTime("Knight","","Attack_f_s",0.2)
	Bladex.AddTranTime("Knight","","Attack_f"  ,0.2)
	Bladex.AddTranTime("Knight","","Attack_b_s",0.2)
	Bladex.AddTranTime("Knight","","Attack_b"  ,0.2)

    #Bladex.AddTranTime("Knight","","g_08_new",0.2)
    #Bladex.AddTranTime("Knight","","g_12_new",0.2)
    #Bladex.AddTranTime("Knight","","g_b06_new",0.2)
    #Bladex.AddTranTime("Knight","","g_07_new",0.2)
    #Bladex.AddTranTime("Knight","","g_01low_new",0.2)
    
	Bladex.AddTranTime("Knight","","D_b",0.1)
	Bladex.AddTranTime("Knight","","D_r",0.1)
	Bladex.AddTranTime("Knight","","D_l",0.1)
	Bladex.AddTranTime("Knight","","g_d_l",0.05,0)
	Bladex.AddTranTime("Knight","","g_d_r",0.05,0)
	Bladex.AddTranTime("Knight","","Rlx_vt",0.75)
	Bladex.AddTranTime("Knight","Rlx_vt","",0.25,0)





#
#AMAZON Set
#
def AnmFactAmazon():
	
	Bladex.SetAnimationFactor("Amz_g_01",3.6)
	Bladex.SetAnimationFactor("Amz_g_02",3.6)
	Bladex.SetAnimationFactor("Amz_g_05",3.6)
	Bladex.SetAnimationFactor("Amz_g_06",3.6) 
	Bladex.SetAnimationFactor("Amz_g_07",3.6)
	Bladex.SetAnimationFactor("Amz_g_08",3.6)
	Bladex.SetAnimationFactor("Amz_g_09",3.6) 
#	Bladex.SetAnimationFactor("Amz_g_01a",4)
#	Bladex.SetAnimationFactor("Amz_g_02a",4)
#	Bladex.SetAnimationFactor("Amz_g_05a",4)
#	Bladex.SetAnimationFactor("Amz_g_06a",4)
#	Bladex.SetAnimationFactor("Amz_g_07a",4)
#	Bladex.SetAnimationFactor("Amz_g_08a",4)
#	Bladex.SetAnimationFactor("Amz_g_09a",4)

	Bladex.SetAnimationFactor("Amz_g_11",3.5)
	Bladex.SetAnimationFactor("Amz_g_12",3.5)
	Bladex.SetAnimationFactor("Amz_g_13",3.5)
	Bladex.SetAnimationFactor("Amz_g_14",3.5)
	Bladex.SetAnimationFactor("Amz_g_15",3.5)
	Bladex.SetAnimationFactor("Amz_g_16",3.5)
	Bladex.SetAnimationFactor("Amz_g_17",3.5)
	Bladex.SetAnimationFactor("Amz_g_18",3.5)
#	Bladex.SetAnimationFactor("Amz_g_19",3.5)

	Bladex.SetAnimationFactor("Amz_g_21",3.5)
	Bladex.SetAnimationFactor("Amz_g_22",3.5)
	Bladex.SetAnimationFactor("Amz_g_23",3.5)
	Bladex.SetAnimationFactor("Amz_g_26",3.5)
	Bladex.SetAnimationFactor("Amz_g_27",3.5)

	Bladex.SetAnimationFactor("Amz_g_31",3.5)
	
	Bladex.SetAnimationFactor("Amz_g_back",3)
	Bladex.SetAnimationFactor("Amz_g_3s9_6new",4.2)	
	Bladex.SetAnimationFactor("Amz_g_12_7_s1new",3)
	Bladex.SetAnimationFactor("Amz_g_28new",4.1)
	Bladex.SetAnimationFactor("Amz_g_27kata_new",3)
	Bladex.SetAnimationFactor("Amz_g_spear19",2.7)	
	Bladex.SetAnimationFactor("Amz_g_spear_b29",4.3)	
	Bladex.SetAnimationFactor("Amz_g_spear_2katab6low",3)
	Bladex.SetAnimationFactor("Amz_g_spear02",3.8)
	Bladex.SetAnimationFactor("Amz_g_spear02low",3.7)
	Bladex.SetAnimationFactor("Amz_g_spear08",3.4)
	Bladex.SetAnimationFactor("Amz_g_spear09",4)
	Bladex.SetAnimationFactor("Amz_g_spear12",4.5)
	Bladex.SetAnimationFactor("Amz_g_spear22",3.3)
	Bladex.SetAnimationFactor("Amz_g_spear26kata",4)
	Bladex.SetAnimationFactor("Amz_g_spear2katab2",4)
	Bladex.SetAnimationFactor("Amz_g_spear32kata_b2",3.4)
	Bladex.SetAnimationFactor("Amz_g_spear3s2",3.4)
	Bladex.SetAnimationFactor("Amz_g_spearb2kata",4)
	Bladex.SetAnimationFactor("Amz_g_spears1",3.4)
	Bladex.SetAnimationFactor("Amz_g_spears6",3.4)
	Bladex.SetAnimationFactor("Amz_g_spears8",3)
	Bladex.SetAnimationFactor("Amz_g_spear_back",3.0)
	Bladex.SetAnimationFactor("Amz_g_spear_sb11",4)    
	Bladex.SetAnimationFactor("Amz_g_spear17",3.4)    
	Bladex.SetAnimationFactor("Amz_g_spear16",3.1)           
	Bladex.SetAnimationFactor("Amz_g_spear_b6_26",3.3)
	Bladex.SetAnimationFactor("Amz_g_spear19_13",3)
	Bladex.SetAnimationFactor("Amz_g_spear_b06",4.5)
	Bladex.SetAnimationFactor("Amz_g_spear_bs21",3)
	Bladex.SetAnimationFactor("Amz_g_spear111",2)
	Bladex.SetAnimationFactor("Amz_g_spear_21",3.4)
	Bladex.SetAnimationFactor("Amz_g_spear13",4)
	Bladex.SetAnimationFactor("Amz_g_spear_kata23",3)
	Bladex.SetAnimationFactor("Amz_g_spear33",4.1)
	Bladex.SetAnimationFactor("Amz_g_spear19_bs1",3.8)
	Bladex.SetAnimationFactor("Amz_g_kick1",3.2)
	Bladex.SetAnimationFactor("Amz_g_kick2",3.5)
	Bladex.SetAnimationFactor("Amz_g_kick4",3.0)
	Bladex.SetAnimationFactor("Amz_g_kick5",2.4)
	Bladex.SetAnimationFactor("Amz_g_punch2",2)
	Bladex.SetAnimationFactor("Amz_g_punch1",3.0)
	Bladex.SetAnimationFactor("Amz_g_punch3",3.0)
	Bladex.SetAnimationFactor("Amz_g_bad_axe",4)
	Bladex.SetAnimationFactor("Amz_g_bad_sword",3)
	Bladex.SetAnimationFactor("Amz_g_bad_sword2",5.1)
	Bladex.SetAnimationFactor("Amz_g_bad_sword3",3)
	Bladex.SetAnimationFactor("Amz_g_bad_1h",3.6)
	Bladex.SetAnimationFactor("Amz_g_bad_no",3.6)
	Bladex.SetAnimationFactor("Amz_g_draw_rlx",3.0)
	Bladex.SetAnimationFactor("Amz_g_draw_run",3.0)
	Bladex.SetAnimationFactor("Amz_g_spear16low",3.5)
	Bladex.SetAnimationFactor("Amz_g_magic",3)
	Bladex.SetAnimationFactor("Amz_g_magic2",3)
	Bladex.SetAnimationFactor("Amz_g_06lowkata_new",4)









	Bladex.SetAnimationFactor("Amz_1tw_h_f",3)
	Bladex.SetAnimationFactor("Amz_1tw_l_f",3)
	Bladex.SetAnimationFactor("Amz_b1",2)
	Bladex.SetAnimationFactor("Amz_b2",3)
	Bladex.SetAnimationFactor("Amz_attack_f",3.8)
	Bladex.SetAnimationFactor("Amz_attack_b",3.8)
	Bladex.SetAnimationFactor("Amz_attack_f_s",3)
	Bladex.SetAnimationFactor("Amz_attack_b_s",3)
	Bladex.SetAnimationFactor("Amz_attack_f_no",3.6)
	Bladex.SetAnimationFactor("Amz_attack_b_no",3.6)
	Bladex.SetAnimationFactor("Amz_attack_f_2w",3)
	Bladex.SetAnimationFactor("Amz_attack_b_2w",3)
	Bladex.SetAnimationFactor("Amz_parry_2w",1.5)
	Bladex.SetAnimationFactor("Amz_parry_spear",2.1) 
	
	
	 

	###movimientos###

	Bladex.SetAnimationFactor("Amz_d_b",1)
	Bladex.SetAnimationFactor("Amz_d_l",1.2)
	Bladex.SetAnimationFactor("Amz_d_r",1.2)
	Bladex.SetAnimationFactor("Jog_no_Amz",2.7)
	Bladex.SetAnimationFactor("Jog_1h_Amz",1.4)
	Bladex.SetAnimationFactor("Wlk_no_Amz",1.55)
	Bladex.SetAnimationFactor("Wlk_1h_Amz",1.7)
	Bladex.SetAnimationFactor("Wlk_2h_Amz",1.7)
	Bladex.SetAnimationFactor("Wlk_2w_Amz",1.6)
	Bladex.SetAnimationFactor("Wlk_axe_Amz",1.6)
	Bladex.SetAnimationFactor("Wlk_s_Amz",1.5)
	Bladex.SetAnimationFactor("Wlk_spear_Amz",1.4)
	Bladex.SetAnimationFactor("Wlk_b_Amz",1.6)
	Bladex.SetAnimationFactor("Wbk_no_Amz",1.6)
	Bladex.SetAnimationFactor("Wbk_1h_Amz",1.5)
	Bladex.SetAnimationFactor("Wbk_2h_Amz",1.5)
	Bladex.SetAnimationFactor("Wbk_axe_Amz",1.5)
	Bladex.SetAnimationFactor("Wbk_2w_Amz",1.5)
	Bladex.SetAnimationFactor("Wbk_b_Amz",1.5)
	Bladex.SetAnimationFactor("Wbk_spear_Amz",1.6)
	Bladex.SetAnimationFactor("Jog_s_Amz",2.7)   
	Bladex.SetAnimationFactor("Jog_2w_Amz",3.3)
	Bladex.SetAnimationFactor("Jog_spear_Amz",3.4)
	Bladex.SetAnimationFactor("Jog_axe_Amz",2.5)
	Bladex.SetAnimationFactor("Jog_2h_Amz",3.4)    	
	Bladex.SetAnimationFactor("Jog_b_Amz",3.6)
	Bladex.SetAnimationFactor("Amz_jogb_no",3.5) 
	Bladex.SetAnimationFactor("Amz_jogb_spear",3.3)
	Bladex.SetAnimationFactor("Amz_jogb_axe",2.5)
	Bladex.SetAnimationFactor("Amz_jogb_2w",1.3)
	Bladex.SetAnimationFactor("Amz_jogb_b",1.3)
	Bladex.SetAnimationFactor("Amz_attack_f_spear",3.7) 
	Bladex.SetAnimationFactor("Amz_attack_b_spear",3.9)
	Bladex.SetAnimationFactor("Amz_attack_r_spear",1.2)
	Bladex.SetAnimationFactor("Amz_attack_l_spear",1.2)
	Bladex.SetAnimationFactor("Amz_derrape",3)
	Bladex.SetAnimationFactor("Amz_wlk_turn",2)
	Bladex.SetAnimationFactor("Amz_snk_turn",1.7)
	Bladex.SetAnimationFactor("Amz_jog_turn",1.8)
	Bladex.SetAnimationFactor("Amz_rlx_turn",1.3)
	Bladex.SetAnimationFactor("Amz_rlx_vt",1.25)
	Bladex.SetAnimationFactor("Amz_jmp_no",1.60)
	Bladex.SetAnimationFactor("Amz_jmp_1h",1.60) 
	Bladex.SetAnimationFactor("Amz_jmph0_no",1.60)
	Bladex.SetAnimationFactor("Amz_attack_chg_r_l",1)
	Bladex.SetAnimationFactor("Amz_attack_chg_l",1.45)
	Bladex.SetAnimationFactor("Amz_attack_chg_r",1.60)
	Bladex.SetAnimationFactor("Amz_drp_r",1.60)
	Bladex.SetAnimationFactor("Amz_drp_l",1.60)
	Bladex.SetAnimationFactor("Amz_tke_r_01",1.60)
	
	Bladex.SetAnimationFactor("FallLow_Amz",1.8) ### Added -LeadHead
	Bladex.SetAnimationFactor("Amz_drink",1.3)






	#
	# TRANSICIONES DE LA AMAZONA
	#
	Bladex.AddTranTime("Amz","","slip",0.3)
	Bladex.AddTranTime("Amz","slip","",0.4)

	Bladex.AddTranTime("Amz","FllHigh","",0.4)

	Bladex.AddTranTime("Amz","","ShortStep",0.3)
	Bladex.AddTranTime("Amz","ShortStep","",0.4)


	#Ejemplo de golpes -> Faltan muchos!
	Bladex.AddTranTime("Amz","g_08","g_01",0.1)
	Bladex.AddTranTime("Amz","g_08","g_02",0.05)

	Bladex.AddTranTime("Amz","WLK","SNK",0.5)
	Bladex.AddTranTime("Amz","","SNK",0.5)
	Bladex.AddTranTime("Amz","","WBK",0.2)
	Bladex.AddTranTime("Amz","","WBK_JOG",0.2)
	Bladex.AddTranTime("Amz","JOG","WLK",0.3)
	Bladex.AddTranTime("Amz","WLK","JOG",0.3)
	Bladex.AddTranTime("Amz","","JOG",0.2)
	Bladex.AddTranTime("Amz","","WLK",0.2)
	Bladex.AddTranTime("Amz","","b3",0.3,0)


	Bladex.AddTranTime("Amz","","Rlx",0.35)
	Bladex.AddTranTime("Amz","","Rlx_f",0.2)
	Bladex.AddTranTime("Amz","","Attack_rlx_s",0.4)

	Bladex.AddTranTime("Amz","","Attack_l_s",0.2)
	Bladex.AddTranTime("Amz","","Attack_l"  ,0.2)
	Bladex.AddTranTime("Amz","","Attack_r_s",0.2)
	Bladex.AddTranTime("Amz","","Attack_r"  ,0.2)
	Bladex.AddTranTime("Amz","","Attack_f_s",0.2)
	Bladex.AddTranTime("Amz","","Attack_f"  ,0.2)
	Bladex.AddTranTime("Amz","","Attack_b_s",0.2)
	Bladex.AddTranTime("Amz","","Attack_b"  ,0.2)

	Bladex.AddTranTime("Amz","","D_b",0.1)
	Bladex.AddTranTime("Amz","","D_r",0.1)
	Bladex.AddTranTime("Amz","","D_l",0.1)
	Bladex.AddTranTime("Amz","","Rlx_vt",0.75)
	Bladex.AddTranTime("Amz","Rlx_vt","",0.25,0)







#
#Dwarf Set
#
def AnmFactDwarf():
#	Bladex.SetAnimationFactor("Dwf_g_01",4)
#	Bladex.SetAnimationFactor("Dwf_g_02",4)
#	Bladex.SetAnimationFactor("Dwf_g_05",4)
#	Bladex.SetAnimationFactor("Dwf_g_06",4)
#	Bladex.SetAnimationFactor("Dwf_g_07",4)
#	Bladex.SetAnimationFactor("Dwf_g_08",4)
#	Bladex.SetAnimationFactor("Dwf_g_09",4)
#	Bladex.SetAnimationFactor("Dwf_g_01a",4)
#	Bladex.SetAnimationFactor("Dwf_g_02a",4)
#	Bladex.SetAnimationFactor("Dwf_g_05a",4)
#	Bladex.SetAnimationFactor("Dwf_g_06a",4)
#	Bladex.SetAnimationFactor("Dwf_g_07a",4)
#	Bladex.SetAnimationFactor("Dwf_g_08a",4)
#	Bladex.SetAnimationFactor("Dwf_g_09a",4)
#
#	Bladex.SetAnimationFactor("Dwf_g_11",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_12",3.1)
#	Bladex.SetAnimationFactor("Dwf_g_13",3.1)
#	Bladex.SetAnimationFactor("Dwf_g_14",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_15",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_16",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_17",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_18",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_19",3.5)
#
#	Bladex.SetAnimationFactor("Dwf_g_21",4.5)
#	Bladex.SetAnimationFactor("Dwf_g_22",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_23",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_26",3.5)
#	Bladex.SetAnimationFactor("Dwf_g_27",3.5)
#
#	Bladex.SetAnimationFactor("Dwf_g_31",3.5)

	#Bladex.SetAnimationFactor("Dwf_attack_t_r",0.1)
	#Bladex.SetAnimationFactor("Dwf_attack_t_l",0.1)
	Bladex.SetAnimationFactor("Dwf_1tw_h_f",3)
	Bladex.SetAnimationFactor("Dwf_1tw_l_f",3)
	Bladex.SetAnimationFactor("Dwf_b1",2)
	Bladex.SetAnimationFactor("Dwf_b2",3)


	###movimientos###

	Bladex.SetAnimationFactor("Jog_no_Dwf",3.5)
	Bladex.SetAnimationFactor("Jog_1h_Dwf",3.8)
	Bladex.SetAnimationFactor("Jog_2w_Dwf",1.1)
	Bladex.SetAnimationFactor("Jog_axe_Dwf",1.1)
	Bladex.SetAnimationFactor("Wlk_no_Dwf",1.55)
	Bladex.SetAnimationFactor("Wlk_1h_Dwf",1.4)
	Bladex.SetAnimationFactor("Wlk_b_Dwf",1.5)
	Bladex.SetAnimationFactor("Wlk_2w_Dwf",1.4)
	Bladex.SetAnimationFactor("Wlk_spear_Dwf",1.4)
	Bladex.SetAnimationFactor("Wbk_no_Dwf",1.6)
	Bladex.SetAnimationFactor("Wbk_b_Dwf",1.6)
	Bladex.SetAnimationFactor("Wbk_2w_Dwf",1.1)
	Bladex.SetAnimationFactor("Wbk_spear_Dwf",1.1)
	Bladex.SetAnimationFactor("Dwf_jogb_no",1.5)
	Bladex.SetAnimationFactor("Dwf_jogb_1h",1.5)
	Bladex.SetAnimationFactor("Dwf_jogb_2w",1.5)
	Bladex.SetAnimationFactor("Dwf_jogb_spear",1.5)
	Bladex.SetAnimationFactor("Dwf_snk_turn",1.7)
	Bladex.SetAnimationFactor("Dwf_jog_turn",1.4)
	Bladex.SetAnimationFactor("Dwf_rlx_turn",1.4)
	Bladex.SetAnimationFactor("Dwf_wlk_turn",1.3)
	Bladex.SetAnimationFactor("Dwf_attack_f",1.5)
	Bladex.SetAnimationFactor("Dwf_attack_b",1.3)
	Bladex.SetAnimationFactor("Dwf_attack_r",1)
	Bladex.SetAnimationFactor("Dwf_attack_l",1)
	
	Bladex.SetAnimationFactor("Dwf_g_back",3.7)
	Bladex.SetAnimationFactor("Dwf_g_bad_1h",3.6)
	Bladex.SetAnimationFactor("Dwf_g_bad_no",3.6)
	Bladex.SetAnimationFactor("Dwf_g_bad_axe",1.6)
	Bladex.SetAnimationFactor("Dwf_g_bad_spear",1.3)
	Bladex.SetAnimationFactor("Dwf_g_bad_spear2",1.3)		
	Bladex.SetAnimationFactor("Dwf_g_bad_sword1",1.2)		
	Bladex.SetAnimationFactor("Dwf_g_bad_sword2",1.2)
	Bladex.SetAnimationFactor("Dwf_g_bad_sword3",1.4)
	Bladex.SetAnimationFactor("Dwf_g_01",3.5)
	Bladex.SetAnimationFactor("Dwf_g_01a",3.5)   
	Bladex.SetAnimationFactor("Dwf_g_02",3.5)   
	Bladex.SetAnimationFactor("Dwf_g_02a",3.5)
	Bladex.SetAnimationFactor("Dwf_g_05",3.2)
	Bladex.SetAnimationFactor("Dwf_g_05a",3.2) 
	Bladex.SetAnimationFactor("Dwf_g_06",3.6)
	Bladex.SetAnimationFactor("Dwf_g_06a",3.3)    
	Bladex.SetAnimationFactor("Dwf_g_07",3.2) 
	Bladex.SetAnimationFactor("Dwf_g_07a",3.3)
	Bladex.SetAnimationFactor("Dwf_g_08",3.7)
	Bladex.SetAnimationFactor("Dwf_g_09",2.9)
	Bladex.SetAnimationFactor("Dwf_g_09a",3.3)
	Bladex.SetAnimationFactor("Dwf_g_11",3)
	Bladex.SetAnimationFactor("Dwf_g_12",3.1)
	Bladex.SetAnimationFactor("Dwf_g_13",3.1)
	Bladex.SetAnimationFactor("Dwf_g_14",3.4)
	Bladex.SetAnimationFactor("Dwf_g_15",3.4)
	Bladex.SetAnimationFactor("Dwf_g_16",3.1)
	Bladex.SetAnimationFactor("Dwf_g_17",3.1)
	Bladex.SetAnimationFactor("Dwf_g_18",3.6)
	Bladex.SetAnimationFactor("Dwf_g_21",5)
	Bladex.SetAnimationFactor("Dwf_g_22",2.8)
	Bladex.SetAnimationFactor("Dwf_g_23",3)
	Bladex.SetAnimationFactor("Dwf_g_26",3.3)
	Bladex.SetAnimationFactor("Dwf_g_27",3)
	Bladex.SetAnimationFactor("Dwf_g_31",3.8)
	Bladex.SetAnimationFactor("Dwf_g_s22low_new",3.7)
	Bladex.SetAnimationFactor("Dwf_g_01low_new",4.1)
	Bladex.SetAnimationFactor("Dwf_g_s18",3.7)
	Bladex.SetAnimationFactor("Dwf_g_s18_2h",3.4)
	Bladex.SetAnimationFactor("Dwf_g_s3_new",3)
	Bladex.SetAnimationFactor("Dwf_g_32_5_3new",3)
	Bladex.SetAnimationFactor("Dwf_g_27kata",3)
	Bladex.SetAnimationFactor("Dwf_g_punch1",3.7)
	Bladex.SetAnimationFactor("Dwf_g_punch2",3.7)
	Bladex.SetAnimationFactor("Dwf_g_kick",3.7)
	Bladex.SetAnimationFactor("Dwf_g_draw_rlx",3.0)
	Bladex.SetAnimationFactor("Dwf_g_draw_run",3.0)
	Bladex.SetAnimationFactor("Dwf_g_d_l",3.7)
	Bladex.SetAnimationFactor("Dwf_g_d_r",3.7)
	Bladex.SetAnimationFactor("Dwf_g_d_b",3.7)
	Bladex.SetAnimationFactor("Dwf_g_magic",3)
	Bladex.SetAnimationFactor("Dwf_g_magic2",3)
	Bladex.SetAnimationFactor("Dwf_g_06lowkata_new",4)
	Bladex.SetAnimationFactor("Dwf_sword_reaction",1.0)
	
	
	Bladex.SetAnimationFactor("Dwf_jmp_no",1.25)
	Bladex.SetAnimationFactor("Dwf_jmp_1h",1.25)
	Bladex.SetAnimationFactor("Dwf_jmph0_no",1.25)
	
	Bladex.SetAnimationFactor("FallLow_Dwf",1.8) ### Added 
	Bladex.SetAnimationFactor("Dwf_drink",1.45)	 ### 	-LeadHead



	#
	# TRANSICIONES DEL EnAnO
	#
	Bladex.AddTranTime("Dwf","","slip",0.3)
	Bladex.AddTranTime("Dwf","slip","",0.4)

	Bladex.AddTranTime("Dwf","FllHigh","",0.4)

	Bladex.AddTranTime("Dwf","","ShortStep",0.3)
	Bladex.AddTranTime("Dwf","ShortStep","",0.4)


	#Ejemplo de golpes -> Faltan muchos!
	Bladex.AddTranTime("Dwf","g_08","g_01",0.1)
	Bladex.AddTranTime("Dwf","g_08","g_02",0.05)


	Bladex.AddTranTime("Dwf","SNK","WLK",0.2)
	Bladex.AddTranTime("Dwf","WLK","SNK",0.5)
	Bladex.AddTranTime("Dwf","","SNK",0.5)

	Bladex.AddTranTime("Dwf","","WLK",0.2)
	Bladex.AddTranTime("Dwf","","JOG",0.2)
	Bladex.AddTranTime("Dwf","WLK","JOG",0.2)
	Bladex.AddTranTime("Dwf","WBK_JOG","WLK",0.2)

	Bladex.AddTranTime("Dwf","JOG","WLK",0.3)
	Bladex.AddTranTime("Dwf","JOG","WBK",0.2)
	Bladex.AddTranTime("Dwf","","WBK",0.2)
	Bladex.AddTranTime("Dwf","WBK","WBK_JOG",0.2)
	Bladex.AddTranTime("Dwf","JOG","WBK_JOG",0.2)

	Bladex.AddTranTime("Dwf","","Rlx",0.35)
	Bladex.AddTranTime("Dwf","","Rlx_f",0.35)
	Bladex.AddTranTime("Dwf","","Attack_rlx_s",0.2)

	Bladex.AddTranTime("Dwf","","Attack_l_s",0.2)
	Bladex.AddTranTime("Dwf","","Attack_l"  ,0.2)
	Bladex.AddTranTime("Dwf","","Attack_r_s",0.2)
	Bladex.AddTranTime("Dwf","","Attack_r"  ,0.2)
	Bladex.AddTranTime("Dwf","","Attack_f_s",0.2)
	Bladex.AddTranTime("Dwf","","Attack_f"  ,0.2)
	Bladex.AddTranTime("Dwf","","Attack_b_s",0.2)
	Bladex.AddTranTime("Dwf","","Attack_b"  ,0.2)
	Bladex.AddTranTime("Dwf","","b3"  ,0.3,0)

	Bladex.AddTranTime("Dwf","","D_l",0.15)
	Bladex.AddTranTime("Dwf","","D_b",0.15)
	Bladex.AddTranTime("Dwf","","D_r",0.15)
	Bladex.AddTranTime("Dwf","","Rlx_vt",0.75)
	Bladex.AddTranTime("Dwf","Rlx_vt","",0.25,0)
	
	### Attack anim experiments
	# Bladex.AddTranTime("Dwf","g_26","g_22",0.3)





#############################################################
#############################################################
#############################################################
#
#
#   E N E M I G O S
#
#
#############################################################
#############################################################
#############################################################







#
# Caballero Traitor
#
done_traitor=0
def AnmFactTraitorKnight():
	global done_traitor	
	if not done_traitor:
		"""
		Bladex.SetAnimationFactor("Tkn_wlk_1h",1)
		Bladex.SetAnimationFactor("Tkn_dth_sleep",1)
		Bladex.SetAnimationFactor("Tkn_dth_sleep_wall",1)
		Bladex.SetAnimationFactor("Tkn_walk_t",1)
		Bladex.SetAnimationFactor("Tkn_burn",1)
		Bladex.SetAnimationFactor("Tkn_burn_fall",1)
		Bladex.SetAnimationFactor("Tkn_rlx_1h",1)
		Bladex.SetAnimationFactor("Tkn_rlx_f_s",1)
		Bladex.SetAnimationFactor("Tkn_rlx_f",1)
		Bladex.SetAnimationFactor("Tkn_attack_f",1)
		Bladex.SetAnimationFactor("Tkn_attack_f_s",1)
		Bladex.SetAnimationFactor("Tkn_attack_b",1)
		Bladex.SetAnimationFactor("Tkn_attack_b_s",1)
		Bladex.SetAnimationFactor("Tkn_attack_r_s",1)
		Bladex.SetAnimationFactor("Tkn_attack_r",1)
		Bladex.SetAnimationFactor("Tkn_attack_l_s",1)
		Bladex.SetAnimationFactor("Tkn_attack_l",1)
		Bladex.SetAnimationFactor("Tkn_d_r",1)
		Bladex.SetAnimationFactor("Tkn_d_l",1)
		"""
		Bladex.SetAnimationFactor("Tkn_g_01",3.4)
		Bladex.SetAnimationFactor("Tkn_g_02",3.6) 
		Bladex.SetAnimationFactor("Tkn_g_05",2.8)
		Bladex.SetAnimationFactor("Tkn_g_06",3.2)
		Bladex.SetAnimationFactor("Tkn_g_07",3.5)
		Bladex.SetAnimationFactor("Tkn_g_08",3.5)
		Bladex.SetAnimationFactor("Tkn_g_09",2.8)
		Bladex.SetAnimationFactor("Tkn_g_01a",4)
		Bladex.SetAnimationFactor("Tkn_g_02a",4)
		Bladex.SetAnimationFactor("Tkn_g_05a",4)
		Bladex.SetAnimationFactor("Tkn_g_06a",4)
		Bladex.SetAnimationFactor("Tkn_g_07a",4)
		Bladex.SetAnimationFactor("Tkn_g_08a",4)
		Bladex.SetAnimationFactor("Tkn_g_09a",4)
		
		Bladex.SetAnimationFactor("Tkn_laugh",1.4)
		Bladex.SetAnimationFactor("Tkn_fury",3.4)
		Bladex.SetAnimationFactor("Tkn_b1",2)
		Bladex.SetAnimationFactor("Tkn_b2",3)
		Bladex.SetAnimationFactor("Tkn_sword_reaction",0.7)
	
		Bladex.SetAnimationFactor("Tkn_g_11",3.5)
		Bladex.SetAnimationFactor("Tkn_g_12",3.5)
		Bladex.SetAnimationFactor("Tkn_g_13",4.2)
		Bladex.SetAnimationFactor("Tkn_g_14",3.5)
		Bladex.SetAnimationFactor("Tkn_g_15",3.5)
		Bladex.SetAnimationFactor("Tkn_g_16",4.6)
		Bladex.SetAnimationFactor("Tkn_g_17",3.5)
		Bladex.SetAnimationFactor("Tkn_g_18",4.4)
		Bladex.SetAnimationFactor("Tkn_g_19",3.5)
	
		Bladex.SetAnimationFactor("Tkn_g_21",3.5)
		Bladex.SetAnimationFactor("Tkn_g_22",3.5)
		Bladex.SetAnimationFactor("Tkn_g_23",3.5)
		Bladex.SetAnimationFactor("Tkn_g_26",3.5)
		Bladex.SetAnimationFactor("Tkn_g_27",3.5)
	
		Bladex.SetAnimationFactor("Tkn_g_31",3.5)
	
		#
		# TRANSICIONES DEL CABALLERO TRAIDOR
		#
		Bladex.AddTranTime("Tkn","","Attack_f",0.2)
		Bladex.AddTranTime("Tkn","","Attack_r",0.2)
		Bladex.AddTranTime("Tkn","","Attack_l",0.2)
		Bladex.AddTranTime("Tkn","","Attack_b",0.2)
		Bladex.AddTranTime("Tkn","","Rlx",0.5)
		Bladex.AddTranTime("Tkn","","JOG",0.3)
		Bladex.AddTranTime("Tkn","","WLK",0.3)
		Bladex.AddTranTime("Tkn","","WBK",0.3)
		Bladex.AddTranTime("Tkn","","b3",0.3,0)         ### Added -LeadHead

		Bladex.AddTranTime("Dkn","","Attack_f",0.2)
		Bladex.AddTranTime("Dkn","","Attack_r",0.2)
		Bladex.AddTranTime("Dkn","","Attack_l",0.2)
		Bladex.AddTranTime("Dkn","","Attack_b",0.2)
		Bladex.AddTranTime("Dkn","","Rlx",0.5)
		Bladex.AddTranTime("Dkn","","JOG",0.3)
		Bladex.AddTranTime("Dkn","","WLK",0.3)
		Bladex.AddTranTime("Dkn","","WBK",0.3)
		Bladex.AddTranTime("Dkn","","b3",0.3,0)

		done_traitor=1
#
# Caballero Caos
#
def AnmFactChosKnight():
	Bladex.SetAnimationFactor("Chk_g_02",4.5)
	Bladex.SetAnimationFactor("Chk_g_01",5.5)
	Bladex.SetAnimationFactor("Chk_g_07",5)
	Bladex.SetAnimationFactor("Chk_g_08",6.2)
	Bladex.SetAnimationFactor("Chk_g_12",3.5)
	Bladex.SetAnimationFactor("Chk_g_18",3.5)
	Bladex.SetAnimationFactor("Chk_g_31",5.4)
	Bladex.SetAnimationFactor("Chk_g_magic",1.6)

	Bladex.SetAnimationFactor("Wbk_1h_Chk",2.4)
	Bladex.SetAnimationFactor("Wlk_1h_Chk",1.7)
	
	Bladex.SetAnimationFactor("Attack_f_s_Chk",1.0)
	Bladex.SetAnimationFactor("Attack_b_Chk",1.7) 
	Bladex.SetAnimationFactor("Attack_b_s_Chk",1.7)
	
	Bladex.SetAnimationFactor("Chk_hurt01",3)

	#
	# TRANSICIONES DEL CABALLERO CAOS
	#
	#Bladex.AddTranTime("Chk","","Rlx_1h_Chk",0.7)
	#Bladex.AddTranTime("Chk","","Rlx_f_Chk",0.7)
	#Bladex.AddTranTime("Chk","","Rlx_f_s_Chk",0.7)
	Bladex.AddTranTime("Chk","","",0.35)



#
# Ragnar
#
### PLAGUE: Ragnar is completely missing transitions?

def AnmFactRagnar():
	Bladex.SetAnimationFactor("Rgn_g_21",4)
	Bladex.SetAnimationFactor("Rgn_g_17",4)
	Bladex.SetAnimationFactor("Rgn_g_escape",4)
	Bladex.SetAnimationFactor("Rgn_g_d_r",4)
	Bladex.SetAnimationFactor("Rgn_g_d_l",4)
	Bladex.SetAnimationFactor("Rgn_g_03",4)
	Bladex.SetAnimationFactor("Rgn_g_01",4)
	Bladex.SetAnimationFactor("Rgn_g_02",4)
	Bladex.SetAnimationFactor("Rgn_g_07",4)







########################################
########################################
#              Troll   		       #
########################################
########################################
done_troll=0
def AnmFactTroll():
	global done_troll
	if not done_troll:
		Bladex.SetAnimationFactor("Trl_g_01",2.5)
		Bladex.SetAnimationFactor("Trl_g_02",3)
		Bladex.SetAnimationFactor("Trl_g_04",2.5)
		Bladex.SetAnimationFactor("Trl_g_06",3)
		Bladex.SetAnimationFactor("Trl_g_12",3.5)
		Bladex.SetAnimationFactor("Trl_g_18",3.5)
		Bladex.SetAnimationFactor("Trl_g_19",3)
		Bladex.SetAnimationFactor("Trl_g_31",5)
		Bladex.SetAnimationFactor("Trl_hurt_r_arm",5)
		Bladex.SetAnimationFactor("Trl_hurt_l_arm",5)
		Bladex.SetAnimationFactor("Trl_hurt_r_leg",5)
		Bladex.SetAnimationFactor("Trl_hurt_l_leg",5)
		Bladex.SetAnimationFactor("Trl_hurt_breast",5)
					
		Bladex.SetAnimationFactor("Trl_wlk_no",1.1)
		Bladex.SetAnimationFactor("Trl_attack_f",1.25) 
		Bladex.SetAnimationFactor("Trl_jog_1h",1.0) 

	
		#
		# TRANSICIONES DEL TROLL
		#
		Bladex.AddTranTime("Trl","","Attack_f",0.3)
		Bladex.AddTranTime("Trl","","Attack_b",0.3)
		Bladex.AddTranTime("Trl","","Rlx",0.5)
		Bladex.AddTranTime("Trl","","JOG",0.3)
		Bladex.AddTranTime("Trl","","WLK",0.3)
		Bladex.AddTranTime("Trl","","WBK",0.3)
		Bladex.AddTranTime("Trl","","g_19",0.2)
		Bladex.AddTranTime("Trl","","g_18",0.2)
		Bladex.AddTranTime("Trl","","g_31",0.2)
		done_troll=1



#
# Cosita
#
def AnmFactCosita():
	
	Bladex.SetAnimationFactor("Jog_no_Cos",1.3)
	Bladex.SetAnimationFactor("Cos_wbk_no",1.69)
	Bladex.SetAnimationFactor("Cos_wlk_no",1.21)
	Bladex.SetAnimationFactor("Cos_t_r_no",1.69)
	Bladex.SetAnimationFactor("Cos_t_l_no",1.69)
	Bladex.SetAnimationFactor("Cos_attack_f",1.68)
	Bladex.SetAnimationFactor("Cos_attack_b",1.96)
	Bladex.SetAnimationFactor("Cos_attack_r",1.4)
	Bladex.SetAnimationFactor("Cos_attack_l",1.4)

	#This ones done by Bob , I think
	#Bladex.SetAnimationFactor("Cos_jog_no",1.5)
		
	 
	Bladex.SetAnimationFactor("Cos_g_01",1.5)
    

	#
	# TRANSICIONES DE LA COSITA
	#
	Bladex.AddTranTime("Cos","","Attack_f",0.2)
	Bladex.AddTranTime("Cos","","Attack_r",0.2)
	Bladex.AddTranTime("Cos","","Attack_l",0.2)
	Bladex.AddTranTime("Cos","","Attack_b",0.1,0)
	Bladex.AddTranTime("Cos","","Rlx",0.5)
	Bladex.AddTranTime("Cos","","JOG",0.3)
	Bladex.AddTranTime("Cos","","WLK",0.3)
	Bladex.AddTranTime("Cos","","WBK",0.3)

	Bladex.AddTranTime("Cos","","g_01",0.2, 0)
	Bladex.AddTranTime("Cos","","Hurt_lite",0.3, 0)
	Bladex.AddTranTime("Cos","","Jmp_back1",0.3, 0)
	Bladex.AddTranTime("Cos","","Fly",0.3,0)
	Bladex.AddTranTime("Cos","","Dth_fly",0.3,0)




#
# Ork
#
done_ork= 0
def AnmFactOrk():
	global done_ork
	if not done_ork:
		Bladex.SetAnimationFactor("Ork_g_01",3.6)
		Bladex.SetAnimationFactor("Ork_g_02",3.6)
		Bladex.SetAnimationFactor("Ork_g_06",3.6)
		Bladex.SetAnimationFactor("Ork_g_15",3.8)
		Bladex.SetAnimationFactor("Ork_g_16",3.6)
		Bladex.SetAnimationFactor("Ork_g_18",4)
		Bladex.SetAnimationFactor("Ork_hurt_f_big",1.4)
		Bladex.SetAnimationFactor("Ork_attack_f",1.2)
		Bladex.SetAnimationFactor("Ork_attack_b",1.3)
		Bladex.SetAnimationFactor("Ork_attack_r",1.5)
		Bladex.SetAnimationFactor("Ork_attack_l",1.5)

	#
	# TRANSICIONES DEL ORCO
	#
		Bladex.AddTranTime("Ork","","Attack_f",0.2)
		Bladex.AddTranTime("Ork","","Attack_r",0.2)
		Bladex.AddTranTime("Ork","","Attack_l",0.2)
		Bladex.AddTranTime("Ork","","Attack_b",0.2)
		Bladex.AddTranTime("Ork","","Rlx",0.3)
		Bladex.AddTranTime("Ork","","JOG",0.3)
		Bladex.AddTranTime("Ork","","WLK",0.3)
		Bladex.AddTranTime("Ork","","WBK",0.3)
		Bladex.AddTranTime("Ork","","b3",0.3,0)
	    
		Bladex.AddTranTime("Org","","Attack_f",0.2)     # Have to add these, otherwise TranTimes don't work properly -LeadHead
		Bladex.AddTranTime("Org","","Attack_r",0.2)
		Bladex.AddTranTime("Org","","Attack_l",0.2)
		Bladex.AddTranTime("Org","","Attack_b",0.2)
		Bladex.AddTranTime("Org","","Rlx",0.3)
		Bladex.AddTranTime("Org","","JOG",0.3)
		Bladex.AddTranTime("Org","","WLK",0.3)
		Bladex.AddTranTime("Org","","WBK",0.3)
		Bladex.AddTranTime("Org","","b3",0.3,0)
	
		Bladex.AddTranTime("Dok","","Attack_f",0.2)
		Bladex.AddTranTime("Dok","","Attack_r",0.2)
		Bladex.AddTranTime("Dok","","Attack_l",0.2)
		Bladex.AddTranTime("Dok","","Attack_b",0.2)
		Bladex.AddTranTime("Dok","","Rlx",0.3)
		Bladex.AddTranTime("Dok","","JOG",0.3)
		Bladex.AddTranTime("Dok","","WLK",0.3)
		Bladex.AddTranTime("Dok","","WBK",0.3)
		Bladex.AddTranTime("Dok","","b3",0.3,0)
		done_ork=1



#
# GREAT Ork
#
def AnmFactGreatOrk():
	Bladex.SetAnimationFactor("Gok_g_01",3.4)
	Bladex.SetAnimationFactor("Gok_g_02",3.4)
	Bladex.SetAnimationFactor("Gok_g_06",3.4)
	Bladex.SetAnimationFactor("Gok_g_15",3.6)
	Bladex.SetAnimationFactor("Gok_g_16",3.4)
	Bladex.SetAnimationFactor("Gok_g_18",3.8)
	Bladex.SetAnimationFactor("Gok_hurt_f_big",1.3)
	Bladex.SetAnimationFactor("Gok_attack_f",1)
	Bladex.SetAnimationFactor("Gok_attack_b",1)
	Bladex.SetAnimationFactor("Gok_attack_r",1)
	Bladex.SetAnimationFactor("Gok_attack_l",1)
	
	#
	# TRANSICIONES DEL JEFE ORCO
	#
	Bladex.AddTranTime("Gok","","Attack_f",0.2)
	Bladex.AddTranTime("Gok","","Attack_r",0.2)
	Bladex.AddTranTime("Gok","","Attack_l",0.2)
	Bladex.AddTranTime("Gok","","Attack_b",0.2)
	Bladex.AddTranTime("Gok","","Rlx",0.35)
	Bladex.AddTranTime("Gok","","JOG",0.3)
	Bladex.AddTranTime("Gok","","WLK",0.3)
	Bladex.AddTranTime("Gok","","WBK",0.3)
	Bladex.AddTranTime("Gok","","b3",0.3,0)
	

#
# Skeleton
#
def AnmFactSkeleton():
	Bladex.SetAnimationFactor("Skl_g_01",4)
	Bladex.SetAnimationFactor("Skl_g_02",4)
	Bladex.SetAnimationFactor("Skl_g_07",4)
	Bladex.SetAnimationFactor("Skl_g_09",4)
	Bladex.SetAnimationFactor("Skl_g_16",4)
	Bladex.SetAnimationFactor("Skl_g_22",4)
	Bladex.SetAnimationFactor("Skl_g_18",4)
	Bladex.SetAnimationFactor("Skl_attack_hurt_f_big",2.5)
	Bladex.SetAnimationFactor("Skl_attack_f",1.7)
	Bladex.SetAnimationFactor("Jog_1h_Skl",1)
	Bladex.SetAnimationFactor("Skl_sword_reaction",0.7)
	
	#
	# TRANSICIONES DEL ESQUELETO
	#
	Bladex.AddTranTime("Skl","","Attack_f",0.2)
	Bladex.AddTranTime("Skl","","Attack_r",0.2)
	Bladex.AddTranTime("Skl","","Attack_l",0.2)
	Bladex.AddTranTime("Skl","","Attack_b",0.2)
	Bladex.AddTranTime("Skl","","Rlx_b",0.5,0)
	Bladex.AddTranTime("Skl","","Rlx",0.5)
	Bladex.AddTranTime("Skl","","JOG",0.3)
	Bladex.AddTranTime("Skl","","WLK",0.3)
	Bladex.AddTranTime("Skl","","WBK",0.3)
	Bladex.AddTranTime("Skl","","b3",0.3,0)


#
# Vampire
#
def AnmFactVampire():
	Bladex.SetAnimationFactor("Vmp_g_01",4)
	Bladex.SetAnimationFactor("Vmp_g_06",4)
	Bladex.SetAnimationFactor("Vmp_g_07",4)	
	Bladex.SetAnimationFactor("Vmp_g_26",4)	
	Bladex.SetAnimationFactor("Vmp_attack_b",1.6)
	Bladex.SetAnimationFactor("Vmp_attack_b_s",1.6)
	Bladex.SetAnimationFactor("Vmp_attack_f",1.6)
	Bladex.SetAnimationFactor("Vmp_attack_f_s",1.6)
	Bladex.SetAnimationFactor("Vmp_attack_l",1.6)
	Bladex.SetAnimationFactor("Vmp_attack_l_s",1.6)
	Bladex.SetAnimationFactor("Vmp_attack_r",1.6)
	Bladex.SetAnimationFactor("Vmp_attack_r_s",1.6)
	Bladex.SetAnimationFactor("Vmp_df_01",1.6)
	Bladex.SetAnimationFactor("Vmp_df_02",1.6)
	Bladex.SetAnimationFactor("Vmp_hurt_f_big",3.5)
	Bladex.SetAnimationFactor("Vmp_hurt_f_lite",4)
	Bladex.SetAnimationFactor("Vmp_insult",2)
	Bladex.SetAnimationFactor("Vmp_wbk_1h",1.6)
	Bladex.SetAnimationFactor("Vmp_wlk_1h",1.6)
	
########transiciones

	Bladex.AddTranTime("Vmp","","Rlx",0.4)
	Bladex.AddTranTime("Vmp","","Rlx_f",0.4)

	Bladex.AddTranTime("Vmp","","Attack_l_s",0.2)
	Bladex.AddTranTime("Vmp","","Attack_l"  ,0.2)
	Bladex.AddTranTime("Vmp","","Attack_r_s",0.2)
	Bladex.AddTranTime("Vmp","","Attack_r"  ,0.2)
	Bladex.AddTranTime("Vmp","","Attack_f_s",0.2)
	Bladex.AddTranTime("Vmp","","Attack_f"  ,0.2)
	Bladex.AddTranTime("Vmp","","Attack_b_s",0.2)
	Bladex.AddTranTime("Vmp","","Attack_b"  ,0.2)

#
# Lich
#
done_lich=0
def AnmFactLich():
	global done_lich
	if not done_lich:
		
		
		Bladex.SetAnimationFactor("Wlk_1h_Lch",1.35)
		Bladex.SetAnimationFactor("Lch_wbk_1h",1.0)
		Bladex.SetAnimationFactor("Lch_g_spit",1.5)
		Bladex.SetAnimationFactor("Lch_g_13",1.5)
		Bladex.SetAnimationFactor("Lch_g_18",1.5)
		Bladex.SetAnimationFactor("Lch_g_16",4.5)
		Bladex.SetAnimationFactor("Lch_g_12",4.5)
		Bladex.SetAnimationFactor("Lch_g_claw1",1.5)
		Bladex.SetAnimationFactor("Lch_g_claw2",1.5)
		Bladex.SetAnimationFactor("Lch_g_claw3",1.5)

		done_lich=1

	#
	# TRANSICIONES DEL LICH
	#
	Bladex.AddTranTime("Lch","","WLK",0.5)
	Bladex.AddTranTime("Lch","","Rlx",0.5)
	Bladex.AddTranTime("Lch","","g_16",0.4)
	Bladex.AddTranTime("Lch","","g_18",0.4)
	Bladex.AddTranTime("Lch","","g_spit",0.4)


#
# Little Demon
#
def AnmFactLittleDemon():
	Bladex.SetAnimationFactor("Ldm_g_03",3)
	Bladex.SetAnimationFactor("Ldm_g_06",3)
	Bladex.SetAnimationFactor("Ldm_g_07",3)
	Bladex.SetAnimationFactor("Ldm_g_22",3)
	Bladex.SetAnimationFactor("Ldm_g_27",3)
	Bladex.SetAnimationFactor("Ldm_g_jumpl",3)
	Bladex.SetAnimationFactor("Ldm_g_jumpr",3)
	Bladex.SetAnimationFactor("Ldm_g_spit",3)
	Bladex.AddTranTime("Ldm","","g_jumpl",0.1, 0)
	Bladex.AddTranTime("Ldm","","g_jumpr",0.1, 0)

#
# Great Demon
#	


def AnmFactGreatDemon():
	Bladex.AddTranTime("Gdm","","g_01",0.5, 0)
	Bladex.AddTranTime("Gdm","","appears",0.5, 0)
	Bladex.AddTranTime("Gdm","","g_12",0.5, 0)
	Bladex.AddTranTime("Gdm","","g_claw",0.5, 0)
	Bladex.AddTranTime("Gdm","","g_magic",0.3, 0)
	Bladex.AddTranTime("Gdm","","",0.5, 1)
	
	Bladex.SetAnimationFactor("Gdm_wlk_no",4)
	Bladex.SetAnimationFactor("Gdm_wbk_no",2)
	Bladex.SetAnimationFactor("Gdm_g_claw",1.5)
	Bladex.SetAnimationFactor("Gdm_g_spitball",1.8)
	Bladex.SetAnimationFactor("Gdm_g_spit_around",1.9)
	Bladex.SetAnimationFactor("Gdm_g_01",4.1)
	Bladex.SetAnimationFactor("Gdm_g_12",1.6)
	Bladex.SetAnimationFactor("Gdm_g_quake",1.4)

#
# Salamander
#
def AnmFactSalamander():
	Bladex.AddTranTime("Slm","","Hurt_f_big",0.1, 0)
	Bladex.AddTranTime("Slm","","Dth0",0.1, 0)
	Bladex.AddTranTime("Slm","","Jog_no_Slm",0.1, 0)
	Bladex.SetAnimationFactor("Slm_g_bite",1.7)
	Bladex.SetAnimationFactor("Slm_g_r",2.3)
	Bladex.SetAnimationFactor("Slm_hurt_f_big",2.5)
	Bladex.SetAnimationFactor("Slm_hurt_f_lite",3)
	Bladex.SetAnimationFactor("Slm_spit",2.3)
	Bladex.SetAnimationFactor("Jog_no_Slm",2.3)
	Bladex.SetAnimationFactor("Wbk_no_Slm",3.3)
	Bladex.SetAnimationFactor("Wlk_no_Slm",3.3)
	Bladex.SetAnimationFactor("FallMed_Slm",3.5)
	Bladex.SetAnimationFactor("FallLow_Slm",3.5)
	Bladex.SetAnimationFactor("FallHigh_Slm",3.5)
	
	#
	# TRANSICIONES DEL SALAMANDER
	#
	Bladex.AddTranTime("Slm","Jog_no_Slm","Wbk_no_Slm",0.4)
	Bladex.AddTranTime("Slm","Wbk_no_Slm","Jog_no_Slm",0.4)
	Bladex.AddTranTime("Slm","","Wbk_no_Slm",0.4)
	Bladex.AddTranTime("Slm","","Wlk_no_Slm",0.3)
	Bladex.AddTranTime("Slm","","Rlx",0.5)
	Bladex.AddTranTime("Slm","","Jog_no_Slm",0.4)
	Bladex.AddTranTime("Slm","","WLK",0.5)
	Bladex.AddTranTime("Slm","","WBK",0.5)
	Bladex.AddTranTime("Slm","","g_bite",0.2)
	Bladex.AddTranTime("Slm","","g_r",0.2)
	Bladex.AddTranTime("Slm","","g_spit",0.2)
	Bladex.AddTranTime("Slm","FallLow_Slm","",0.2)
	Bladex.AddTranTime("Slm","FallMed_Slm","",0.2)
	Bladex.AddTranTime("Slm","FallHigh_Slm","",0.2)

#
# Minotaur
#


def AnmFactMinotaur():
	
	Bladex.SetAnimationFactor("Jog_1h_Min",1.5)
	Bladex.SetAnimationFactor("Rlx_1h_Min",1)
	Bladex.SetAnimationFactor("Wlk_1h_Min",1.6)
	Bladex.SetAnimationFactor("Wbk_1h_Min",1.6)
	Bladex.SetAnimationFactor("Min_g_01",4.2) 
	Bladex.SetAnimationFactor("Min_g_07",4.9)
	Bladex.SetAnimationFactor("Min_g_08",4.7)
	Bladex.SetAnimationFactor("Min_g_12",3.5)
	Bladex.SetAnimationFactor("Min_g_31",3.5)
	Bladex.SetAnimationFactor("Min_eat",0.8)
	Bladex.SetAnimationFactor("Min_hurt_big",2)
	Bladex.SetAnimationFactor("Min_hurt_lite",2)
	
	#
	# TRANSICIONES MINOTAURO
	#
	Bladex.AddTranTime("Min","","JOG",0.2)
	Bladex.AddTranTime("Min","","WLK",0.25)
	Bladex.AddTranTime("Min","","WBK",0.3)
	Bladex.AddTranTime("Min","","Rlx",0.3)
	Bladex.AddTranTime("Min","","Min_hurt_big",0.2)
	Bladex.AddTranTime("Min","","Min_hurt_lite",0.2)
	
	pass        # PLAGUE: Why is this here?

#
# Dal-Gurak (the TORERO)
#
def AnmFactDalGurak():
	Bladex.AddTranTime("Dgk","","g_m01",0.2, 0)
	Bladex.AddTranTime("Dgk","","g_m02",0.2, 0)
	Bladex.AddTranTime("Dgk","","g_d_l",0.2, 0)
	Bladex.AddTranTime("Dgk","","g_d_r",0.2, 0)

	Bladex.SetAnimationFactor("Dgk_g_07_new",3.4)
	Bladex.SetAnimationFactor("Dgk_g_08_new",3.4)
	Bladex.SetAnimationFactor("Dgk_g_02_new",3.4)
	Bladex.SetAnimationFactor("Dgk_g_01_7_new",2.8)
	Bladex.SetAnimationFactor("Dgk_g_22lowkata_new",3.5)
	Bladex.SetAnimationFactor("Dgk_g_21_6_s8new",3.5)
	Bladex.SetAnimationFactor("Dgk_g_19_bs1_new",3.6)
	Bladex.SetAnimationFactor("Dgk_g_b32kata_new",3.6)
	Bladex.SetAnimationFactor("Dgk_g_29_3new",3.5)
	Bladex.SetAnimationFactor("Dgk_g_d_l",3.2)
	Bladex.SetAnimationFactor("Dgk_g_d_r",3.2)
	Bladex.SetAnimationFactor("Dgk_g_back",2.5)
	Bladex.SetAnimationFactor("Dgk_g_magic",4.4)
	Bladex.SetAnimationFactor("Dgk_g_magic2",4.4)
	
	
	Bladex.SetAnimationFactor("Dgk_attack_b",3)
	Bladex.SetAnimationFactor("Dgk_attack_b_s",3)
	Bladex.SetAnimationFactor("Dgk_attack_f",3)
	Bladex.SetAnimationFactor("Dgk_attack_f_s",3)
	Bladex.SetAnimationFactor("Dgk_attack_l",3)
	Bladex.SetAnimationFactor("Dgk_attack_r",3)
	Bladex.SetAnimationFactor("Dgk_attack_l_s",3)
	Bladex.SetAnimationFactor("Dgk_attack_r_s",3)
	Bladex.SetAnimationFactor("Dgk_catch",3)

	Bladex.SetAnimationFactor("Dgk_df_01",3)	
	Bladex.SetAnimationFactor("Dgk_df_02",3)
	Bladex.SetAnimationFactor("Dgk_hurt_big",3)
	Bladex.SetAnimationFactor("Dgk_hurt_lite",3)		
	Bladex.SetAnimationFactor("Dgk_hurt_chest",3)	
	Bladex.SetAnimationFactor("Dgk_hurt_back",3)	
	Bladex.SetAnimationFactor("Dgk_hurt_r_arm",3)	
	Bladex.SetAnimationFactor("Dgk_hurt_l_arm",3)	
	Bladex.SetAnimationFactor("Dgk_hurt_r_leg",3)	
	Bladex.SetAnimationFactor("Dgk_hurt_l_leg",3)	




#
# An-Ahkard (the Dark Lord)
#

def AnmFactAnAhkard():

	Bladex.AddTranTime("Ank","","g_mgc01",0.2, 0)
	Bladex.AddTranTime("Ank","","g_mgc02",0.2, 0)
	Bladex.AddTranTime("Ank","","g_mgc03",0.2, 0)
	Bladex.AddTranTime("Ank","","",0.8, 0)	
	
	Bladex.SetAnimationFactor("Ank_g_01",1.5)
	Bladex.SetAnimationFactor("Ank_g_02",1.5)
	Bladex.SetAnimationFactor("Ank_g_07",1.2)




done_golem= 0

def AnmFactGolem():
	global done_golem
	if not done_golem:
		#
		# Golems
		#
		Bladex.SetAnimationFactor("Glm_jog_no",1.2)
		Bladex.SetAnimationFactor("Glm_wbk_no",1.2)
		Bladex.SetAnimationFactor("Glm_wlk_no",1.2)
		Bladex.SetAnimationFactor("Glm_rlx_no",1.2)
		
		Bladex.SetAnimationFactor("Glm_g_01",1.25)
		Bladex.SetAnimationFactor("Glm_g_114",1.25)
		Bladex.SetAnimationFactor("Glm_g_12",1.25)
		Bladex.SetAnimationFactor("Glm_g_21_27",1.25)
		Bladex.SetAnimationFactor("Glm_g_21",1.25)
		Bladex.SetAnimationFactor("Glm_g_31",1.25)
		Bladex.SetAnimationFactor("Glm_1tw",1.25)
		
		Bladex.AddTranTime("Glm","","",0.4) #last thing
		done_golem=1
		
		
#
# Prisoner
#

# Bladex.AddTranTime("Prs_1","","",0.2, 0)
# Bladex.AddTranTime("Prs_2","","",0.2, 0)
# Bladex.AddTranTime("Prs_3","","",0.2, 0)
# Bladex.AddTranTime("Prs_4","","",0.2, 0)
# Bladex.AddTranTime("Prs_5","","",0.2, 0)
# Bladex.AddTranTime("Prs_6","","",0.2, 0)