import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosCaballeroOscuroCalled=0
def AsignarSonidosCaballeroOscuro(Personaje):

	
	from AniSoundDknX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoDkn)
	per.AddEventSound('weapon_block', GolpeArmaArmaDkn)
	per.AddEventSound('impale', TajoEmpalanteDkn)
	per.AddEventSound('slash', TajoCortanteDkn)
	per.AddEventSound('mutilate', TajoMutilacionDkn)
	per.AddEventSound('crush', GolpeContundenteDkn)
	
	
	global AsignarSonidosCaballeroOscuroCalled
	if AsignarSonidosCaballeroOscuroCalled:
		return
	AsignarSonidosCaballeroOscuroCalled=1

	
	
	# Sonidos de animaciones

	# Animation Alarm (We want a selection of sounds, so better link a function)
	per.AddAnimSound('Tkn_alarm01', DKnightKeepStill, 0.3300)
	per.AddAnimSound('Tkn_alarm02', DKnightKeepStill, 0.5500)
	
	per.AddAnimSound('Tkn_chg_r', Enfundar, 0.5000)
	per.AddAnimSound('Tkn_chg_r_l', Enfundar, 0.5000)
	per.AddAnimSound('Tkn_attack_chg_r_l', Enfundar, 0.5000)
	per.AddAnimSound('Tkn_attack_chg_r', Enfundar, 0.5000)
	per.AddAnimSound('Tkn_chg_r', Enfundar, 0.5000)
	per.AddAnimSound('Tkn_chg_r_l', Enfundar, 0.5000)
	per.AddAnimSound('Tkn_attack_chg_r_l', Enfundar, 0.5000)
	per.AddAnimSound('Tkn_attack_chg_l', Enfundar, 0.5000)
	
	
	#per.AddAnimSound('Tkn_g_21', EsfuerzoCorto3Dkn, 0.2000)
	#per.AddAnimSound('Tkn_g_21', EsfuerzoCorto2Dkn, 0.6778)
	per.AddAnimSound('Tkn_g_21', SesgadoCortoAgudo, 0.1778)
	per.AddAnimSound('Tkn_g_21', SesgadoCortoAgudo, 0.6444)

	#per.AddAnimSound('Tkn_g_17', EsfuerzoCorto3Dkn, 0.0597)
	per.AddAnimSound('Tkn_g_17', SesgadoCorto, 0.0746)

	per.AddAnimSound('Tkn_g_escape', EsfuerzoDknMediano, 0.3529)
	per.AddAnimSound('Tkn_g_escape', SesgadoLargoAgudo, 0.5765)

	per.AddAnimSound('Tkn_g_d_r', EsfuerzoDknMediano, 0.5059)
	#per.AddAnimSound('Tkn_g_d_r', EsfuerzoCorto2Dkn, 0.5059)
	per.AddAnimSound('Tkn_g_d_r', SesgadoCortoAgudo, 0.5294)

	per.AddAnimSound('Tkn_g_d_l', EsfuerzoDknMediano, 0.4725)
	#per.AddAnimSound('Tkn_g_d_l', EsfuerzoCorto3Dkn, 0.4725)
	per.AddAnimSound('Tkn_g_d_l', SesgadoCortoAgudo, 0.5165)

	#per.AddAnimSound('Tkn_g_03', EsfuerzoCorto5Dkn, 0.2388)
	per.AddAnimSound('Tkn_g_03', SesgadoLargoAgudo, 0.2836)

	per.AddAnimSound('Tkn_g_01', EsfuerzoGolpeAtrasDkn, 0.0820)
	per.AddAnimSound('Tkn_g_01', SesgadoLargoAgudo, 0.0984)

	#per.AddAnimSound('Tkn_g_02', EsfuerzoCorto2Dkn, 0.2687)
	per.AddAnimSound('Tkn_g_02', SesgadoLargoAgudo, 0.2836)

	#per.AddAnimSound('Tkn_g_07', EsfuerzoCorto3Dkn, 0.1642)
	per.AddAnimSound('Tkn_g_07', SesgadoLargoAgudo, 0.3284)


	per.AddAnimSound('Tkn_g_01', EsfuerzoCortoDkn, 0.3117)
	per.AddAnimSound('Tkn_g_02', EsfuerzoCorto1Dkn, 0.3026)
	per.AddAnimSound('Tkn_g_05', EsfuerzoCorto2Dkn, 0.5000)
	per.AddAnimSound('Tkn_g_06', EsfuerzoCorto3Dkn, 0.4342)
	per.AddAnimSound('Tkn_g_07', EsfuerzoCorto4Dkn, 0.3291)
	per.AddAnimSound('Tkn_g_08', EsfuerzoCorto5Dkn, 0.4030)
	per.AddAnimSound('Tkn_g_09', EsfuerzoCorto6Dkn, 0.3291)
	per.AddAnimSound('Tkn_g_01', SesgadoCorto, 0.3117)
	per.AddAnimSound('Tkn_g_02', SesgadoCortoAgudo, 0.3026)
	per.AddAnimSound('Tkn_g_05', SesgadoCortoGrave, 0.5000)
	per.AddAnimSound('Tkn_g_06', SesgadoCorto, 0.4342)
	per.AddAnimSound('Tkn_g_07', SesgadoCortoAgudo, 0.3291)
	per.AddAnimSound('Tkn_g_08', SesgadoCortoGrave, 0.4030)
	per.AddAnimSound('Tkn_g_09', SesgadoCorto, 0.3291)
	per.AddAnimSound('Tkn_g_11', EsfuerzoDknMediano, 0.2252)
	per.AddAnimSound('Tkn_g_12', EsfuerzoGolpeFrontalDkn, 0.5954)
	per.AddAnimSound('Tkn_g_13', EsfuerzoGolpeLateralDkn, 0.3053)
	per.AddAnimSound('Tkn_g_14', EsfuerzoGolpeCabezaDkn, 0.3969)
	per.AddAnimSound('Tkn_g_15', EsfuerzoGolpeAtrasDkn, 0.4628)
	per.AddAnimSound('Tkn_g_16', EsfuerzoGolpeFrontalDkn, 0.3200)
	per.AddAnimSound('Tkn_g_17', EsfuerzoGolpeLateralDkn, 0.4200)
	per.AddAnimSound('Tkn_g_18', EsfuerzoGolpeCabezaDkn, 0.4224)
	per.AddAnimSound('Tkn_g_11', SesgadoLargo, 0.4685)
	per.AddAnimSound('Tkn_g_12', SesgadoLargo, 0.5954)
	per.AddAnimSound('Tkn_g_13', SesgadoLargoAgudo, 0.3053)
	per.AddAnimSound('Tkn_g_14', SesgadoLargoGrave, 0.3969)
	per.AddAnimSound('Tkn_g_15', SesgadoLargo, 0.4628)
	per.AddAnimSound('Tkn_g_16', SesgadoLargoAgudo, 0.4681)
	per.AddAnimSound('Tkn_g_17', SesgadoLargoAgudo, 0.4427)
	per.AddAnimSound('Tkn_g_18', SesgadoLargoGrave, 0.4224)
	per.AddAnimSound('Tkn_g_22', EsfuerzoDknLargo, 0.4698)
	per.AddAnimSound('Tkn_g_26', EsfuerzoGolpeAtrasDkn, 0.3940)
	per.AddAnimSound('Tkn_g_22', SesgadoLargo, 0.4698)
	per.AddAnimSound('Tkn_g_26', SesgadoLargoAgudo, 0.7315)
	per.AddAnimSound('Tkn_g_31', EsfuerzoDknMediano, 0.2950)
	per.AddAnimSound('Tkn_g_31', SesgadoLargo, 0.2950)
	per.AddAnimSound('Tkn_g_31', SesgadoLargoAgudo, 0.4100)

	per.AddAnimSound('Tkn_clmb_medlow_1h', EsfuerzoCortoDkn, 0.2400)
	per.AddAnimSound('Tkn_clmb_medium_1h', EsfuerzoCortoDkn, 0.1389)
	per.AddAnimSound('Tkn_clmb_high_1h', EsfuerzoCortoDkn, 0.1552)
	per.AddAnimSound('Tkn_clmb_medlow_no', EsfuerzoCortoDkn, 0.4000)
	per.AddAnimSound('Tkn_clmb_medium_no', EsfuerzoCortoDkn, 0.1944)
	per.AddAnimSound('Tkn_clmb_high_no', EsfuerzoCortoDkn, 0.1552)
	per.AddAnimSound('Tkn_clmb_medium_1h', EsfuerzoCortoDkn, 0.1389)
	per.AddAnimSound('Tkn_clmb_high_1h', EsfuerzoDknMediano, 0.1000)
	per.AddAnimSound('Tkn_clmb_high_1h', EsfuerzoCortoDkn, 0.7862)
	per.AddAnimSound('Tkn_clmb_medium_no', EsfuerzoCortoDkn, 0.1944)
	per.AddAnimSound('Tkn_clmb_high_no', EsfuerzoDknMediano, 0.1552)
	per.AddAnimSound('Tkn_clmb_high_no', EsfuerzoCortoDkn, 0.1552)

      
	per.AddAnimSound("Tkn_dth0", MuerteDkn1, 0.1130)
	per.AddAnimSound("Tkn_dth0", CaidaDkn1, 0.8900)
	per.AddAnimSound("Tkn_dth_i1", MuerteDkn1, 0.1130)
	per.AddAnimSound("Tkn_dth_i2", MuerteDkn4, 0.1130)
	per.AddAnimSound("Tkn_dth_bl1", MuerteDkn2, 0.1130)
	per.AddAnimSound("Tkn_dth_bl2", MuerteDkn1, 0.1130)
	per.AddAnimSound("Tkn_dth_rock", MuerteDkn3, 0.1130)
	per.AddAnimSound("Tkn_dth_n00", CaidaDkn1, 0.8000)
	per.AddAnimSound("Tkn_dth_n01", MuerteDkn2, 0.1100)
	per.AddAnimSound("Tkn_dth_n01", CaidaDkn1, 0.7800)
	per.AddAnimSound("Tkn_dth_n02", MuerteDkn3, 0.1200)
	per.AddAnimSound("Tkn_dth_n02", CaidaDkn1, 0.8000)
	per.AddAnimSound("Tkn_dth_n03", MuerteDkn4, 0.1200)
	per.AddAnimSound("Tkn_dth_n03", CaidaDkn1, 0.7550)
	per.AddAnimSound("Tkn_dth_n04", MuerteDkn4, 0.1100)
	per.AddAnimSound("Tkn_dth_n04", CaidaDkn1, 0.7600)
	per.AddAnimSound("Tkn_dth_n05", MuerteDkn4, 0.1100)
	per.AddAnimSound("Tkn_dth_n05", CaidaDkn1, 0.7700)
	per.AddAnimSound("Tkn_dth_n06", MuerteDkn2, 0.1200)
	per.AddAnimSound("Tkn_dth_n06", CaidaDkn1, 0.7900)
	per.AddAnimSound("Tkn_dth_c1", DesangreDkn1, 0.1250)
	per.AddAnimSound("Tkn_dth_c1", CaidaDkn1, 0.7800)
	per.AddAnimSound("Tkn_dth_c1", DesangreDkn1, 0.2500)
	per.AddAnimSound("Tkn_dth_c2", DesangreDkn1, 0.1250)
	per.AddAnimSound("Tkn_dth_c2", DesangreDkn1, 0.2500)
	per.AddAnimSound("Tkn_dth_c2", CaidaDkn1, 0.7720)
	per.AddAnimSound("Tkn_dth_c2", CaidaDkn2, 0.8720)
	per.AddAnimSound("Tkn_dth_c3", DesangreDkn1, 0.1250)
	per.AddAnimSound("Tkn_dth_c3", DesangreDkn1, 0.2500)
	per.AddAnimSound("Tkn_dth_c3", CaidaDkn1, 0.7220)
	per.AddAnimSound("Tkn_dth_c4", DesangreDkn1, 0.1250)
	per.AddAnimSound("Tkn_dth_c4", DesangreDkn1, 0.2500)
	per.AddAnimSound("Tkn_dth_c4", CaidaDkn1, 0.7000)
	per.AddAnimSound("Tkn_dth_c4", CaidaDkn2, 0.8720)
	per.AddAnimSound("Tkn_dth_c5", DesangreDkn1, 0.1250)
	per.AddAnimSound("Tkn_dth_c5", DesangreDkn1, 0.2500)
	per.AddAnimSound("Tkn_dth_c5", CaidaDkn1, 0.7720)
	per.AddAnimSound("Tkn_dth_c5", CaidaDkn2, 0.5500)
	per.AddAnimSound("Tkn_dth_c6", DesangreDkn1, 0.1250)
	per.AddAnimSound("Tkn_dth_c6", DesangreDkn1, 0.2500)
	per.AddAnimSound("Tkn_dth_c6", CaidaDkn1, 0.7700)
	per.AddAnimSound("Tkn_dth_c7", DesangreDkn1, 0.1250)
	per.AddAnimSound("Tkn_dth_c7", DesangreDkn1, 0.2500)
	per.AddAnimSound("Tkn_dth_c7", CaidaDkn1, 0.6300)
	per.AddAnimSound("Tkn_dth_c7", CaidaDkn2, 0.6900)

	per.AddAnimSound('Tkn_hurt_jog', HeridaDkn1, 0.3000)
	per.AddAnimSound('Tkn_hurt_neck', HeridaDkn1, 0.3000)
	per.AddAnimSound('Tkn_hurt_breast', HeridaDkn1, 0.3000)
	per.AddAnimSound('Tkn_hurt_back', HeridaDkn1, 0.3000)
	per.AddAnimSound('Tkn_hurt_r_arm', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_l_arm', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_r_leg', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_l_leg', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_head', HeridaDkn3, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_neck', HeridaDkn3, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_breast', HeridaDkn3, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_back', HeridaDkn3, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_r_arm', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_l_arm', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_r_leg', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_l_leg', HeridaDkn2, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_lite', HeridaDkn3, 0.3000)
	per.AddAnimSound('Tkn_hurt_f_big', HeridaDkn3, 0.3000)
	per.AddAnimSound('Tkn_hurt_head', HeridaDkn3, 0.3000)

	
	
	per.AddAnimSound('Tkn_laugh', RisaDkn, 0.2351)
	per.AddAnimSound('Tkn_laugh', RisaDkn2, 0.6000)
	#per.AddAnimSound('Tkn_laugh', RespiraDkn2, 0.5000)
	per.AddAnimSound('Tkn_laugh', RespiraDkn2, 0.2000)
	per.AddAnimSound('Rgn_insult', AltoDkn, 0.2314)
	per.AddAnimSound('Rgn_insult', AltoDkn2, 0.7000)
	#per.AddAnimSound('Rgn_insult', RespiraDkn2, 0.5000)
	per.AddAnimSound('Rgn_insult', RespiraDkn1, 0.2000)
	
	per.AddAnimSound('Wlk_2h_Tkn',RespiraDkn2, 0.2000)
	#per.AddAnimSound('Wlk_2h_Tkn',RespiraDkn1, 0.5000)
	per.AddAnimSound('Wlk_2h_Tkn',RespiraDkn2, 0.8000)
	per.AddAnimSound('Wbk_2h_Tkn',RespiraDkn1, 0.2000)
	#per.AddAnimSound('Wbk_2h_Tkn',RespiraDkn1, 0.5000)
	per.AddAnimSound('Wbk_2h_Tkn',RespiraDkn2, 0.8000)
	
	per.AddAnimSound('Wlk_2h_Tkn',RespiraDkn1, 0.2000)
	#per.AddAnimSound('Wlk_2h_Tkn',RespiraDkn2, 0.5000)
	per.AddAnimSound('Wlk_2h_Tkn',RespiraDkn1, 0.8000)
	per.AddAnimSound('Wbk_2h_Tkn',RespiraDkn1, 0.2000)
	#per.AddAnimSound('Wbk_2h_Tkn',RespiraDkn2, 0.5000)
	per.AddAnimSound('Wbk_2h_Tkn',RespiraDkn1, 0.8000)
	
	
	#per.AddAnimSound('Tkn_attack_f',RespiraDkn2, 0.5000)
	#per.AddAnimSound('Tkn_attack_f',RespiraDkn1, 0.2000)
	#per.AddAnimSound('Tkn_attack_f',RespiraDkn2, 0.7000)
	#per.AddAnimSound('Tkn_attack_l',RespiraDkn2, 0.5000)
	per.AddAnimSound('Tkn_attack_l',RespiraDkn2, 0.2000)
	#per.AddAnimSound('Tkn_attack_l',RespiraDkn1, 0.7000)
	#per.AddAnimSound('Tkn_attack_r',RespiraDkn1, 0.2000)
	#per.AddAnimSound('Tkn_attack_r',RespiraDkn1, 0.5000)
	#per.AddAnimSound('Tkn_attack_r',RespiraDkn2, 0.8000)
	
	
	#per.AddAnimSound('Tkn_attack_r_s',RespiraDkn2, 0.5000)
	per.AddAnimSound('Tkn_attack_r_s',RespiraDkn1, 0.2000)
	#per.AddAnimSound('Tkn_attack_r_s',RespiraDkn2, 0.8000)
	#per.AddAnimSound('Tkn_attack_b',RespiraDkn2, 0.5000)
	per.AddAnimSound('Tkn_attack_b',RespiraDkn2, 0.2000)
	#per.AddAnimSound('Tkn_attack_b',RespiraDkn1, 0.8000)
	
	
	#per.AddAnimSound('Jog_1h_Tkn',RespiraDkn4, 0.5000)
	per.AddAnimSound('Jog_1h_Tkn',RespiraDkn3, 0.2000)
	per.AddAnimSound('Jog_1h_Tkn',RespiraDkn4, 0.8000)
	#per.AddAnimSound('Jog_2h_Tkn',RespiraDkn4, 0.5000)
	per.AddAnimSound('Jog_2h_Tkn',RespiraDkn4, 0.2000)
	per.AddAnimSound('Jog_2h_Tkn',RespiraDkn3, 0.8000)
	
	per.AddAnimSound('Rlx_1h_Tkn',RespiraDkn2, 0.2000)
	per.AddAnimSound('Rlx_1h_Tkn',RespiraDkn1, 0.8000)
	
	per.AddAnimSound('Rlx_no_Tkn',RespiraDkn2, 0.1000)
	per.AddAnimSound('Rlx_no_Tkn',RespiraDkn1, 0.3000)
	per.AddAnimSound('Rlx_no_Tkn',RespiraDkn2, 0.5000)
	per.AddAnimSound('Rlx_no_Tkn',RespiraDkn1, 0.7000)
	per.AddAnimSound('Rlx_no_Tkn',RespiraDkn2, 0.9000)
	
	
	per.AddAnimSound('Snk_1h_Tkn',RespiraDkn3, 0.2000)
	per.AddAnimSound('Snk_1h_Tkn',RespiraDkn4, 0.8000)
	
	per.AddAnimSound('Tkn_Rlx_f',RespiraDkn1, 0.2000)
	per.AddAnimSound('Tkn_Rlx_f',RespiraDkn2, 0.8000)
	





