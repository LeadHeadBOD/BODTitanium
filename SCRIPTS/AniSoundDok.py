##///
##||| ANISOUNDDOK.PY TITANIUM
##||| Change list:
##||| * Restored missing sounds (effectively copy-paste of regular orc)
##||| 
##\\\ 


import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosOrcoOscuroCalled=0
def AsignarSonidosOrcoOscuro(Personaje):

	from AniSoundDokX import *
	
	per=Bladex.GetEntity(Personaje)


	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoDok)
	per.AddEventSound('weapon_block', GolpeArmaArmaDok)
	per.AddEventSound('impale', TajoEmpalanteDok)
	per.AddEventSound('slash', TajoCortanteDok)
	per.AddEventSound('mutilate', TajoMutilacionDok)
	per.AddEventSound('crush', GolpeContundenteDok)


	global AsignarSonidosOrcoOscuroCalled
	if AsignarSonidosOrcoOscuroCalled:
		return
	AsignarSonidosOrcoOscuroCalled=1

	# Sonidos de animaciones

	# Animation Alarm (We want a selection of sounds, so better link a function)
	per.AddAnimSound('Ork_alarm01', InsultoDok, 0.3000)
	
	per.AddAnimSound('Ork_order', InsultoDok, 0.6610)
	per.AddAnimSound('Ork_order', GritoDok1, 0.1450)
	per.AddAnimSound('Ork_order', GritoDok2, 0.3920)
	
	#per.AddAnimSound('Ork_fury', Insulto, 0.6610)
	per.AddAnimSound('Ork_fury', GritoDok2, 0.3000)
	
	per.AddAnimSound('Ork_g_01', EsfuerzoCortoDok, 0.1883)
	per.AddAnimSound('Ork_g_02', EsfuerzoCorto1Dok, 0.2840)
	per.AddAnimSound('Ork_g_06', EsfuerzoCorto3Dok, 0.4583)
	per.AddAnimSound('Ork_g_01', SesgadoCorto, 0.1883)
	per.AddAnimSound('Ork_g_02', SesgadoCortoAgudo, 0.2840)
	per.AddAnimSound('Ork_g_06', SesgadoCorto, 0.4583)
	per.AddAnimSound('Ork_g_15', EsfuerzoGolpeLateralDok, 0.3651)
	per.AddAnimSound('Ork_g_16', EsfuerzoGolpeLateralDok, 0.4054)
	per.AddAnimSound('Ork_g_18', EsfuerzoGolpeArribaDok, 0.4634)
	per.AddAnimSound('Ork_g_15', SesgadoLargo, 0.3730)
	per.AddAnimSound('Ork_g_16', SesgadoLargoAgudo, 0.4054)
	per.AddAnimSound('Ork_g_18', SesgadoLargoGrave, 0.4878)

	per.AddAnimSound('Ork_clmb_medlow_1h', EsfuerzoCorto2Dok, 0.2400)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCorto2Dok, 0.1389)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto1Dok, 0.0862)
	per.AddAnimSound('Ork_clmb_medlow_no', EsfuerzoCorto2Dok, 0.4000)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCorto2Dok, 0.1944)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto1Dok, 0.1552)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCortoDok, 0.2400)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto3Dok, 0.1389)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCortoDok, 0.0862)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCortoDok, 0.4000)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto3Dok, 0.1944)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCortoDok, 0.1552)

	per.AddAnimSound("Ork_dth0", MuerteDok1, 0.1130)
	per.AddAnimSound("Ork_dth0", AndarDok1, 0.2000)
	per.AddAnimSound("Ork_dth0", AndarDok2, 0.4000)
	per.AddAnimSound("Ork_dth0", AndarDok1, 0.6000)
	per.AddAnimSound("Ork_dth0", AndarDok2, 0.7200)
	per.AddAnimSound("Ork_dth0", CaidaDok1, 0.8900)
	per.AddAnimSound("Ork_dth_i1", MuerteDok1, 0.1130)
	per.AddAnimSound("Ork_dth_i2", MuerteDok4, 0.1130)
	per.AddAnimSound("Ork_dth_bl1", MuerteDok2, 0.1130)
	per.AddAnimSound("Ork_dth_bl2", MuerteDok1, 0.1130)
	per.AddAnimSound("Ork_dth_rock", MuerteDok3, 0.1130)
	per.AddAnimSound("Ork_dth_n00", MuerteDok1, 0.1100)
	per.AddAnimSound("Ork_dth_n00", CaidaDok1, 0.8000)
	per.AddAnimSound("Ork_dth_n01", MuerteDok2, 0.1100)
	per.AddAnimSound("Ork_dth_n01", CaidaDok1, 0.7800)
	per.AddAnimSound("Ork_dth_n02", MuerteDok3, 0.1200)
	per.AddAnimSound("Ork_dth_n02", CaidaDok1, 0.8000)
	per.AddAnimSound("Ork_dth_n03", MuerteDok4, 0.1200)
	per.AddAnimSound("Ork_dth_n03", CaidaDok1, 0.7550)
	per.AddAnimSound("Ork_dth_n04", MuerteDok4, 0.1100)
	per.AddAnimSound("Ork_dth_n04", CaidaDok1, 0.7600)
	per.AddAnimSound("Ork_dth_n05", MuerteDok4, 0.1100)
	per.AddAnimSound("Ork_dth_n05", CaidaDok1, 0.7700)
	per.AddAnimSound("Ork_dth_n06", MuerteDok2, 0.1200)
	per.AddAnimSound("Ork_dth_n06", CaidaDok1, 0.7900)
	per.AddAnimSound("Ork_dth_c1", DesangreDok1, 0.1250)
	per.AddAnimSound("Ork_dth_c1", CaidaDok1, 0.7800)
	per.AddAnimSound("Ork_dth_c1", DesangreDok1, 0.2500)
	per.AddAnimSound("Ork_dth_c2", DesangreDok1, 0.1250)
	per.AddAnimSound("Ork_dth_c2", DesangreDok1, 0.2500)
	per.AddAnimSound("Ork_dth_c2", CaidaDok1, 0.7720)
	per.AddAnimSound("Ork_dth_c2", CaidaDok2, 0.8720)
	per.AddAnimSound("Ork_dth_c3", DesangreDok1, 0.1250)
	per.AddAnimSound("Ork_dth_c3", DesangreDok1, 0.2500)
	per.AddAnimSound("Ork_dth_c3", CaidaDok1, 0.7220)
	per.AddAnimSound("Ork_dth_c4", DesangreDok1, 0.1250)
	per.AddAnimSound("Ork_dth_c4", DesangreDok1, 0.2500)
	per.AddAnimSound("Ork_dth_c4", CaidaDok1, 0.7000)
	per.AddAnimSound("Ork_dth_c4", CaidaDok2, 0.8720)
	per.AddAnimSound("Ork_dth_c5", DesangreDok1, 0.1250)
	per.AddAnimSound("Ork_dth_c5", DesangreDok1, 0.2500)
	per.AddAnimSound("Ork_dth_c5", CaidaDok1, 0.7720)
	per.AddAnimSound("Ork_dth_c5", CaidaDok2, 0.5500)
	per.AddAnimSound("Ork_dth_c6", DesangreDok1, 0.1250)
	per.AddAnimSound("Ork_dth_c6", DesangreDok1, 0.2500)
	per.AddAnimSound("Ork_dth_c6", CaidaDok1, 0.7700)
	per.AddAnimSound("Ork_dth_c7", DesangreDok1, 0.1250)
	per.AddAnimSound("Ork_dth_c7", DesangreDok1, 0.2500)
	per.AddAnimSound("Ork_dth_c7", CaidaDok1, 0.6300)
	per.AddAnimSound("Ork_dth_c7", CaidaDok2, 0.6900)

	per.AddAnimSound("Ork_hurt_jog", HeridaDok1, 0.5714)
	per.AddAnimSound("Ork_hurt_neck", HeridaDok2, 0.3158)
	per.AddAnimSound("Ork_hurt_breast", HeridaDok2, 0.3889)
	per.AddAnimSound("Ork_hurt_back", HeridaDok2, 0.1282)
	per.AddAnimSound("Ork_hurt_r_arm", HeridaDok2, 0.4706)
	per.AddAnimSound("Ork_hurt_l_arm", HeridaDok3, 0.5333)
	per.AddAnimSound("Ork_hurt_r_leg", HeridaDok1, 0.4706)
	per.AddAnimSound("Ork_hurt_l_leg", HeridaDok2, 0.4375)
	per.AddAnimSound("Ork_hurt_f_head", HeridaDok3, 0.3333)
	per.AddAnimSound("Ork_hurt_f_neck", HeridaDok2, 0.3158)
	per.AddAnimSound("Ork_hurt_f_breast", HeridaDok2, 0.3889)
	per.AddAnimSound("Ork_hurt_f_back", HeridaDok2, 0.4211)
	per.AddAnimSound("Ork_hurt_f_r_arm", HeridaDok1, 0.2000)
	per.AddAnimSound("Ork_hurt_f_l_arm", HeridaDok3, 0.1786)
	per.AddAnimSound("Ork_hurt_f_r_leg", HeridaDok2, 0.4706)
	per.AddAnimSound("Ork_hurt_f_l_leg", HeridaDok2, 0.4375)
	per.AddAnimSound("Ork_hurt_f_lite", HeridaDok1, 0.4615)
	per.AddAnimSound("Ork_hurt_f_big", HeridaDok3, 0.5000)
	per.AddAnimSound("Ork_hurt_head", HeridaDok2, 0.6000)

	per.AddAnimSound("Ork_Rlx_1h_00", Relax1Dok, 0.3000)
	per.AddAnimSound("Ork_Rlx_1h_00", Relax2Dok, 0.6000)
	per.AddAnimSound("Ork_Rlx_b_00", Relax1Dok, 0.3000)
	per.AddAnimSound("Ork_Rlx_b_00", Relax2Dok, 0.6000)
	per.AddAnimSound("Ork_Rlx_cold_00", Relax1Dok, 0.3000)
	per.AddAnimSound("Ork_Rlx_cold_00", Relax2Dok, 0.6000)
	per.AddAnimSound("Rlx_no_Ork", Relax1Dok, 0.1500)
	per.AddAnimSound("Rlx_no_Ork", Relax2Dok, 0.3000)
	per.AddAnimSound("Rlx_no_Ork", Relax1Dok, 0.6000)
	per.AddAnimSound("Rlx_no_Ork", Relax2Dok, 0.9000)
	per.AddAnimSound("Ork_Rlx_fatigue_00", Relax1Dok, 0.3000)
	per.AddAnimSound("Ork_Rlx_fatigue_00", Relax2Dok, 0.6000)
	per.AddAnimSound("Rlx_1h_Ork", Relax1Dok, 0.3000)
	per.AddAnimSound("Rlx_1h_Ork", Relax2Dok, 0.6000)


	per.AddAnimSound("Ork_attack_f", GritoDok1, 0.1200)
	per.AddAnimSound("Ork_attack_f_s", GritoDok2, 0.1200)
	per.AddAnimSound("Ork_attack_b", GritoDok1, 0.1200)
	per.AddAnimSound("Ork_attack_b_s", GritoDok2, 0.1200)
	per.AddAnimSound("Ork_attack_r", GritoDok1, 0.1200)
	per.AddAnimSound("Ork_attack_r_s", GritoDok2, 0.1200)
	per.AddAnimSound("Ork_attack_d_b", GritoDok1, 0.1200)
	per.AddAnimSound("Ork_attack_d_r", GritoDok2, 0.1200)
	per.AddAnimSound("Ork_attack_d_l", GritoDok1, 0.1200)
	per.AddAnimSound("Ork_attack_l", GritoDok2, 0.1200)
	per.AddAnimSound("Ork_attack_l_s", GritoDok1, 0.1200)
	per.AddAnimSound("Ork_attack_rlx", GritoDok2, 0.1200)
	per.AddAnimSound("Ork_attack_rlx_s", GritoDok1, 0.1200)


	per.AddAnimSound("Ork_insult", InsultoDok, 0.1590)
	per.AddAnimSound("Ork_insult", Relax2Dok, 0.8000)


	per.AddAnimSound("Jog_1h_Ork", GritoDok2, 0.1100)
	per.AddAnimSound("Jog_1h_Ork", GritoDok2, 0.6000)

	per.AddAnimSound("Wlk_1h_Ork", Relax1Dok, 0.0534)
	per.AddAnimSound("Wlk_1h_Ork", Relax2Dok, 0.3000)
	per.AddAnimSound("Wlk_1h_Ork", Relax1Dok, 0.6000)
	per.AddAnimSound("Wlk_1h_Ork", Relax2Dok, 0.9000)
	
	per.AddAnimSound("Wlk_b_Ork", Relax1Dok, 0.0534)
	per.AddAnimSound("Wlk_b_Ork", Relax2Dok, 0.3000)
	per.AddAnimSound("Wlk_b_Ork", Relax1Dok, 0.6000)
	per.AddAnimSound("Wlk_b_Ork", Relax2Dok, 0.9000)
	
	per.AddAnimSound("Wbk_b_Ork", Relax1Dok, 0.0534)
	per.AddAnimSound("Wbk_b_Ork", Relax2Dok, 0.3000)
	per.AddAnimSound("Wbk_b_Ork", Relax1Dok, 0.6000)
	per.AddAnimSound("Wbk_b_Ork", Relax2Dok, 0.9000)
	
	per.AddAnimSound("Ork_patrol1", Relax1Dok, 0.0534)
	per.AddAnimSound("Ork_patrol1", Relax2Dok, 0.3000)
	per.AddAnimSound("Ork_patrol1", Relax1Dok, 0.6000)
	per.AddAnimSound("Ork_patrol1", Relax2Dok, 0.9000)
	
	per.AddAnimSound("Ork_patrol2", Relax1Dok, 0.0534)
	per.AddAnimSound("Ork_patrol2", Relax2Dok, 0.3000)
	per.AddAnimSound("Ork_patrol2", Relax1Dok, 0.6000)
	per.AddAnimSound("Ork_patrol2", Relax2Dok, 0.9000)
	
	per.AddAnimSound("Ork_attack_b", Relax1Dok, 0.0534)
	per.AddAnimSound("Ork_attack_b", Relax2Dok, 0.3000)
	per.AddAnimSound("Ork_attack_b", Relax1Dok, 0.6000)
	per.AddAnimSound("Ork_attack_b", Relax2Dok, 0.9000)



