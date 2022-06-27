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
	
	per.AddAnimSound('Ork_chg_r', Enfundar, 7)
	per.AddAnimSound('Ork_chg_r_l', Enfundar, 7)
	per.AddAnimSound('Ork_attack_chg_r_l', Enfundar, 8)
	per.AddAnimSound('Ork_attack_chg_r', Enfundar, 7)
	per.AddAnimSound('Ork_chg_r', Enfundar, 7)
	per.AddAnimSound('Ork_chg_r_l', Enfundar, 7)
	per.AddAnimSound('Ork_attack_chg_r_l', Enfundar, 8)
	per.AddAnimSound('Ork_attack_chg_r', Enfundar, 7)

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

	per.AddAnimSound("Ork_dth0", MuerteDok1, 1)
	per.AddAnimSound("Ork_dth_n00", MuerteDok1, 1)
	per.AddAnimSound("Ork_dth_n01", MuerteDok2, 3)
	per.AddAnimSound("Ork_dth_n02", MuerteDok3, 3)
	per.AddAnimSound("Ork_dth_n03", MuerteDok4, 3)
	per.AddAnimSound("Ork_dth_i1", MuerteDok1, 6)
	per.AddAnimSound("Ork_dth_i2", MuerteDok4, 4)
	per.AddAnimSound("Ork_dth_bl1", MuerteDok2, 4)
	per.AddAnimSound("Ork_dth_bl2", MuerteDok1, 3)
	per.AddAnimSound("Ork_dth_rock", MuerteDok3, 9)

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



