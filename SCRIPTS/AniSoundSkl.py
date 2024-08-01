##///
##||| AniSoundSkl.PY TITANIUM
##||| Change list:
##||| * Added sounds for skeleton explosive death
##||| * 
##\\\ 


import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosEsqueletoCalled=0
def AsignarSonidosEsqueleto(Personaje):
	from AniSoundSklX import *

	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoSkl)
	per.AddEventSound('weapon_block', GolpeArmaArmaSkl)
	per.AddEventSound('impale', TajoEmpalanteSkl)
	per.AddEventSound('slash', TajoCortanteSkl)
	per.AddEventSound('mutilate', TajoMutilacionSkl)
	per.AddEventSound('crush', GolpeContundenteSkl)


	global AsignarSonidosEsqueletoCalled
	if AsignarSonidosEsqueletoCalled:
		return
	AsignarSonidosEsqueletoCalled=1


	# Sonidos de animaciones

	
	# Animation Speak01
	per.AddAnimSound('Skl_chg_r', Enfundar, 0.1254 )
	per.AddAnimSound('Skl_chg_r_l', Enfundar, 0.2584)
	per.AddAnimSound('Skl_attack_chg_r_l', Enfundar, 0.2356)
	per.AddAnimSound('Skl_attack_chg_r', Enfundar, 0.3654)
	per.AddAnimSound('Skl_chg_r', Enfundar, 0.2541)
	per.AddAnimSound('Skl_chg_r_l', Enfundar, 0.2586)
	per.AddAnimSound('Skl_attack_chg_r_l', Enfundar, 0.2546)
	per.AddAnimSound('Skl_attack_chg_r', Enfundar, 0.2586)

	per.AddAnimSound('Skl_g_01', EsfuerzoCorto6Skl, 0.2443)
	per.AddAnimSound('Skl_g_02', EsfuerzoCorto5Skl, 0.3493)
	#per.AddAnimSound('Skl_g_02', Relax1, 0.1200)
	per.AddAnimSound('Skl_g_05', EsfuerzoCorto2Skl, 0.2546)
	#per.AddAnimSound('Skl_g_05', Relax1, 0.9000)
	per.AddAnimSound('Skl_g_06', EsfuerzoCorto3Skl, 0.2584)
	#per.AddAnimSound('Skl_g_06', Relax2, 0.8000)
	per.AddAnimSound('Skl_g_07', EsfuerzoCorto4Skl, 0.2690)
	#per.AddAnimSound('Skl_g_07', Relax1, 0.8000)
	per.AddAnimSound('Skl_g_08', EsfuerzoCorto2Skl, 0.2548)
	#per.AddAnimSound('Skl_g_08', Relax2, 0.8000)
	per.AddAnimSound('Skl_g_09', EsfuerzoCorto6Skl, 0.2061)
	#per.AddAnimSound('Skl_g_09', Relax2, 0.8000)
	per.AddAnimSound('Skl_g_01', SesgadoCorto, 0.2519)
	per.AddAnimSound('Skl_g_02', SesgadoCortoAgudo, 0.3356)
	per.AddAnimSound('Skl_g_05', SesgadoCortoGrave, 0.5248)
	per.AddAnimSound('Skl_g_06', SesgadoCorto, 0.2589)
	per.AddAnimSound('Skl_g_07', SesgadoCortoAgudo, 0.2690)
	per.AddAnimSound('Skl_g_08', SesgadoCortoGrave, 0.2548)
	per.AddAnimSound('Skl_g_09', SesgadoCorto, 0.2061)
	per.AddAnimSound('Skl_g_11', EsfuerzoGolpeFrontalSkl, 0.2584)
	per.AddAnimSound('Skl_g_12', EsfuerzoGolpeFrontalSkl, 0.2546)
	per.AddAnimSound('Skl_g_13', EsfuerzoGolpeFrontalSkl, 0.2541)
	per.AddAnimSound('Skl_g_14', EsfuerzoGolpeLateralSkl, 0.2500)
	per.AddAnimSound('Skl_g_15', EsfuerzoGolpeLateralSkl, 0.2543)
	per.AddAnimSound('Skl_g_16', EsfuerzoGolpeLateralSkl, 0.3113)
	per.AddAnimSound('Skl_g_17', EsfuerzoGolpeLateralSkl, 0.1300)
	per.AddAnimSound('Skl_g_18', EsfuerzoGolpeArribaSkl, 0.3521)
	per.AddAnimSound('Skl_g_11', SesgadoLargo, 0.2584)
	per.AddAnimSound('Skl_g_12', SesgadoLargo, 0.2544)
	per.AddAnimSound('Skl_g_13', SesgadoLargoAgudo, 0.3254)
	per.AddAnimSound('Skl_g_14', SesgadoLargoGrave, 0.2541)
	per.AddAnimSound('Skl_g_15', SesgadoLargo, 0.5412)
	per.AddAnimSound('Skl_g_16', SesgadoLargoAgudo, 0.3113)
	per.AddAnimSound('Skl_g_17', SesgadoLargoAgudo, 0.2563)
	per.AddAnimSound('Skl_g_18', SesgadoLargoGrave, 0.4561)
	per.AddAnimSound('Skl_g_22', EsfuerzoGolpeAtrasSkl, 0.1224)
	per.AddAnimSound('Skl_g_26', EsfuerzoGolpeCabezaSkl, 0.2314)
	per.AddAnimSound('Skl_g_22', SesgadoLargo, 0.1224)
	per.AddAnimSound('Skl_g_22', SesgadoLargoAgudo, 0.2600)
	per.AddAnimSound('Skl_g_22', EsfuerzoGolpeCabezaSkl, 0.2600)
	per.AddAnimSound('Skl_g_22', SesgadoLargo, 0.4740)
	per.AddAnimSound('Skl_g_22', EsfuerzoCorto6Skl, 0.4740)
	per.AddAnimSound('Skl_g_26', SesgadoLargoAgudo, 0.2700)
	per.AddAnimSound('Skl_g_31', EsfuerzoGolpeAtrasSkl, 0.2584)
	per.AddAnimSound('Skl_g_31', SesgadoLargo, 0.3541)
	per.AddAnimSound('Skl_g_31', SesgadoLargoAgudo, 0.6214)
	per.AddAnimSound('Skl_clmb_medlow_1h', EsfuerzoCorto2Skl, 0.2584)
	per.AddAnimSound('Skl_clmb_medium_1h', EsfuerzoCorto2Skl, 0.2584)
	per.AddAnimSound('Skl_clmb_high_1h', EsfuerzoCorto1Skl, 0.2546)
	per.AddAnimSound('Skl_clmb_medlow_no', EsfuerzoCorto2Skl, 0.2558)
	per.AddAnimSound('Skl_clmb_medium_no', EsfuerzoCorto2Skl, 0.4125)
	per.AddAnimSound('Skl_clmb_high_no', EsfuerzoCorto1Skl, 0.2531)
	per.AddAnimSound('Skl_clmb_medium_1h', EsfuerzoCortoSkl, 0.2584)
	per.AddAnimSound('Skl_clmb_high_1h', EsfuerzoSklMediano, 0.2584)
	per.AddAnimSound('Skl_clmb_high_1h', EsfuerzoCortoSkl, 0.2584)
	per.AddAnimSound('Skl_clmb_medium_no', EsfuerzoCortoSkl, 0.3695)
	per.AddAnimSound('Skl_clmb_high_no', EsfuerzoSklMediano, 0.3214)
	per.AddAnimSound('Skl_clmb_high_no', EsfuerzoCortoSkl, 0.2584)

	per.AddAnimSound("Skl_dth0", MuerteSkl1, 0.1200)
	per.AddAnimSound("Skl_dth0", Caida, 0.1452)
	per.AddAnimSound("Skl_dth_n00", MuerteSkl2, 0.1000)
	per.AddAnimSound("Skl_dth_n00", Caida, 0.3560)
	per.AddAnimSound("Skl_dth_n00", Caida3, 0.5300)
	per.AddAnimSound("Skl_dth_n00", Caida2, 0.7000)
	per.AddAnimSound("Skl_dth_n01", MuerteSkl2, 0.1100)
	per.AddAnimSound("Skl_dth_n01", Caida, 0.3250)
	per.AddAnimSound("Skl_dth_n01", Caida2, 0.5590)
	per.AddAnimSound("Skl_dth_n01", Caida3, 0.6700)
	per.AddAnimSound("Skl_dth_n02", MuerteSkl4, 0.1200)
	per.AddAnimSound("Skl_dth_n02", Caida, 0.2000)
	per.AddAnimSound("Skl_dth_n02", Caida2, 0.6500)
	per.AddAnimSound("Skl_dth_n02", Caida3, 0.7500)
	per.AddAnimSound("Skl_dth_n03", MuerteSkl4, 0.1200)
	per.AddAnimSound("Skl_dth_n03", Caida, 0.1200)
	per.AddAnimSound("Skl_dth_n03", Caida2, 0.5150)
	per.AddAnimSound("Skl_dth_n03", Caida3, 0.4700)
	per.AddAnimSound("Skl_dth_n04", MuerteSkl1, 0.1100)
	per.AddAnimSound("Skl_dth_n04", Caida, 0.1200)
	per.AddAnimSound("Skl_dth_n04", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_n04", Caida3, 0.7480)
	per.AddAnimSound("Skl_dth_n04", Caida2, 0.7800)
	per.AddAnimSound("Skl_dth_n05", MuerteSkl1, 0.1100)
	per.AddAnimSound("Skl_dth_n05", Caida, 0.1500)
	per.AddAnimSound("Skl_dth_n05", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_n05", Caida2, 0.8800)
	per.AddAnimSound("Skl_dth_n06", MuerteSkl1, 0.1200)
	per.AddAnimSound("Skl_dth_n06", Caida, 0.1800)
	per.AddAnimSound("Skl_dth_n06", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_n06", Caida3, 0.5500)
	per.AddAnimSound("Skl_dth_n06", Caida2, 0.6000)
	per.AddAnimSound("Skl_dth_i1", MuerteSkl1, 0.2541)
	per.AddAnimSound("Skl_dth_i2", MuerteSkl2, 0.2145)
	per.AddAnimSound("Skl_dth_bl1", MuerteSkl3, 0.2145)
	per.AddAnimSound("Skl_dth_bl2", MuerteSkl4, 0.1234)
	per.AddAnimSound("Skl_dth_rock", MuerteSkl1, 0.2111)
	per.AddAnimSound("Skl_dth_c1", Caida, 0.1470)
	per.AddAnimSound("Skl_dth_c1", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_c1", Caida2, 0.6900)
	per.AddAnimSound("Skl_dth_c1", Caida3, 0.7900)
	per.AddAnimSound("Skl_dth_c2", Caida, 0.1900)
	per.AddAnimSound("Skl_dth_c2", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_c2", Caida2, 0.7800)
	per.AddAnimSound("Skl_dth_c2", Caida3, 0.8850)
	per.AddAnimSound("Skl_dth_c3", Caida, 0.1200)
	per.AddAnimSound("Skl_dth_c3", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_c3", Caida2, 0.6370)
	per.AddAnimSound("Skl_dth_c3", Caida3, 0.6800)
	per.AddAnimSound("Skl_dth_c4", Caida, 0.1200)
	per.AddAnimSound("Skl_dth_c4", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_c4", Caida2, 0.4640)
	per.AddAnimSound("Skl_dth_c4", Caida3, 0.7000)
	per.AddAnimSound("Skl_dth_c5", Caida, 0.1200)
	per.AddAnimSound("Skl_dth_c5", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_c5", Caida2, 0.5370)
	per.AddAnimSound("Skl_dth_c5", Caida3, 0.7800)
	per.AddAnimSound("Skl_dth_c6", Caida, 0.1200)
	per.AddAnimSound("Skl_dth_c6", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_c6", Caida2, 0.7700)
	
	per.AddAnimSound("Skl_dth_c7", Caida, 0.1200)
	per.AddAnimSound("Skl_dth_c7", Caida, 0.4500)
	per.AddAnimSound("Skl_dth_c7", Caida2, 0.6300)
	per.AddAnimSound("Skl_dth_c7", Caida3, 0.6900)
	
	per.AddAnimSound("Skl_dth_burn", MuerteQuemandoSkl, 0.1100)
	per.AddAnimSound("Skl_dth_fll", GritoCaida, 0.1100)
	per.AddAnimSound("Skl_dth_fll", GritoCaida, 0.1100)
	per.AddAnimSound("Kgt_dth_rockfront", AplastamientoSkl, 0.1000)
	per.AddAnimSound("Kgt_dth_rockfront", HeridaSkl2, 0.1000)
	per.AddAnimSound("Kgt_dth_rock", AplastamientoSkl, 0.1500)
	per.AddAnimSound("Kgt_dth_rock", HeridaSkl2, 0.1000)
    
	# per.AddAnimSound("Skl_dth_explo", AplastamientoSkl, 0.1300)  #Added. Placeholder sound for now. 
	per.AddAnimSound("Skl_dth_explo", TajoMutilacionSkl, 0.4000)  #                  -LeadHead


	per.AddAnimSound("Skl_hurt_jog", HeridaSkl1, 0.2514)
	per.AddAnimSound("Skl_hurt_neck", HeridaSkl2, 0.2145)
	per.AddAnimSound("Skl_hurt_breast", HeridaSkl3, 0.2541)
	per.AddAnimSound("Skl_hurt_back", HeridaSkl1, 0.1234)
	per.AddAnimSound("Skl_hurt_r_arm", HeridaSkl2, 0.1236)
	per.AddAnimSound("Skl_hurt_l_arm", HeridaSkl3, 0.1254)
	per.AddAnimSound("Skl_hurt_r_leg", HeridaSkl1, 0.3214)
	per.AddAnimSound("Skl_hurt_l_leg", HeridaSkl2, 0.1253)
	per.AddAnimSound("Skl_hurt_f_head", HeridaSkl3, 0.2314)
	per.AddAnimSound("Skl_hurt_f_neck", HeridaSkl2, 0.1235)
	per.AddAnimSound("Skl_hurt_f_breast", HeridaSkl1, 0.1245)
	per.AddAnimSound("Skl_hurt_f_back", HeridaSkl2, 0.5842)
	per.AddAnimSound("Skl_hurt_f_r_arm", HeridaSkl3, 0.5487)
	per.AddAnimSound("Skl_hurt_f_l_arm", HeridaSkl2, 0.2541)
	per.AddAnimSound("Skl_hurt_f_r_leg", HeridaSkl1, 0.2145)
	per.AddAnimSound("Skl_hurt_f_l_leg", HeridaSkl2, 0.1234)
	per.AddAnimSound("Skl_hurt_f_lite", HeridaSkl3, 0.1235)
	per.AddAnimSound("Skl_hurt_f_big", HeridaSkl2, 0.2145)
	per.AddAnimSound("Skl_hurt_head", HeridaSkl1, 0.1254)
	
	per.AddAnimSound("Skl_appears1", Generador, 0.1000)
	per.AddAnimSound("Skl_appears2", Generador, 0.1000)
	
	
	
	per.AddAnimSound("Rlx_1h_Skl", Relax1, 0.1500)
	per.AddAnimSound("Rlx_1h_Skl", Relax2, 0.3000)
	per.AddAnimSound("Rlx_1h_Skl", Relax1, 0.6000)
	per.AddAnimSound("Rlx_1h_Skl", Relax2, 0.9000)
	
#	per.AddAnimSound("Skl_attack_f", Relax1, 0.2500)
	#per.AddAnimSound("Skl_attack_f", Relax2, 0.5000)
	#per.AddAnimSound("Skl_attack_f", Relax1, 0.7500)
	#per.AddAnimSound("Skl_attack_f", Relax2, 0.9000)
	#per.AddAnimSound("Skl_attack_b", Relax1, 0.2500)
	#per.AddAnimSound("Skl_attack_b", Relax2, 0.5000)
	#per.AddAnimSound("Skl_attack_b", Relax1, 0.7250)
	#per.AddAnimSound("Skl_attack_b", Relax2, 0.9000)
	
	#per.AddAnimSound("Skl_attack_f_s", Relax1, 0.2500)
	##per.AddAnimSound("Skl_attack_f_s", Relax2, 0.5000)
	#per.AddAnimSound("Skl_attack_f_s", Relax1, 0.7500)
	#per.AddAnimSound("Skl_attack_f_s", Relax2, 0.9000)
	#per.AddAnimSound("Skl_attack_b_s", Relax1, 0.2500)
	#per.AddAnimSound("Skl_attack_b_s", Relax2, 0.5000)
	#per.AddAnimSound("Skl_attack_b_s", Relax1, 0.7250)
	#per.AddAnimSound("Skl_attack_b_s", Relax2, 0.9000)

	#per.AddAnimSound("Skl_attack_r_s", Relax1, 0.2500)
	#per.AddAnimSound("Skl_attack_r_s", Relax2, 0.5000)
	#per.AddAnimSound("Skl_attack_r_s", Relax1, 0.7500)
	#per.AddAnimSound("Skl_attack_r_s", Relax2, 0.9000)
	#per.AddAnimSound("Skl_attack_l_s", Relax1, 0.2500)
	#per.AddAnimSound("Skl_attack_l_s", Relax2, 0.5000)
	#per.AddAnimSound("Skl_attack_l_s", Relax1, 0.7250)
	#per.AddAnimSound("Skl_attack_l_s", Relax2, 0.9000)
	
	#per.AddAnimSound("Jog_1h_Skl", Relax1, 0.1500)
	#per.AddAnimSound("Jog_1h_Skl", Relax2, 0.3000)
	#per.AddAnimSound("Jog_1h_Skl", Relax1, 0.6000)
	#per.AddAnimSound("Jog_1h_Skl", Relax2, 0.9000)
	
	#per.AddAnimSound("Wlk_1h_Skl", Relax1, 0.1500)
	#per.AddAnimSound("Wlk_1h_Skl", Relax2, 0.3000)
	#per.AddAnimSound("Wlk_1h_Skl", Relax1, 0.6000)
	#per.AddAnimSound("Wlk_1h_Skl", Relax2, 0.9000)
	
	
	#per.AddAnimSound("Wbk_1h_Skl", Relax1, 0.1500)
	#per.AddAnimSound("Wbk_1h_Skl", Relax2, 0.3000)
	#per.AddAnimSound("Wbk_1h_Skl", Relax1, 0.6000)
	#per.AddAnimSound("Wbk_1h_Skl", Relax2, 0.9000)
	
