import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosOrcoCalled=0
def AsignarSonidosOrco(Personaje):

	from AniSoundOrgX import *

	per=Bladex.GetEntity(Personaje)
	

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoOrk)
	per.AddEventSound('weapon_block', GolpeArmaArmaOrk)
	per.AddEventSound('impale', TajoEmpalanteOrk)
	per.AddEventSound('slash', TajoCortanteOrk)
	per.AddEventSound('mutilate', TajoMutilacionOrk)
	per.AddEventSound('crush', GolpeContundenteOrk)
	
	
	global AsignarSonidosOrcoCalled
	if AsignarSonidosOrcoCalled:
		return
	AsignarSonidosOrcoCalled=1


	# Sonidos de animaciones

	# Animation Alarm (We want a selection of sounds, so better link a function)
	per.AddAnimSound('Ork_alarm01', InsultoOrg, 0.3000)
	
	per.AddAnimSound('Ork_order', InsultoOrg, 0.6610)
	per.AddAnimSound('Ork_order', GritoOrc1, 0.1450)
	per.AddAnimSound('Ork_order', GritoOrc2, 0.3920)
	
	#per.AddAnimSound('Ork_fury', Insulto, 0.6610)
	per.AddAnimSound('Ork_fury', GritoOrc2, 0.3000)
	
	per.AddAnimSound('Ork_g_01', EsfuerzoCortoOrc, 0.1883)
	per.AddAnimSound('Ork_g_02', EsfuerzoCorto1Orc, 0.2840)
	per.AddAnimSound('Ork_g_06', EsfuerzoCorto3Orc, 0.4583)
	per.AddAnimSound('Ork_g_01', SesgadoCorto, 0.1883)
	per.AddAnimSound('Ork_g_02', SesgadoCortoAgudo, 0.2840)
	per.AddAnimSound('Ork_g_06', SesgadoCorto, 0.4583)
	per.AddAnimSound('Ork_g_15', EsfuerzoGolpeLateralOrc, 0.3651)
	per.AddAnimSound('Ork_g_16', EsfuerzoGolpeLateralOrc, 0.4054)
	per.AddAnimSound('Ork_g_18', EsfuerzoGolpeArribaOrc, 0.4634)
	per.AddAnimSound('Ork_g_15', SesgadoLargo, 0.3730)
	per.AddAnimSound('Ork_g_16', SesgadoLargoAgudo, 0.4054)
	per.AddAnimSound('Ork_g_18', SesgadoLargoGrave, 0.4878)

	per.AddAnimSound('Ork_clmb_medlow_1h', EsfuerzoCorto2Orc, 0.2400)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCorto2Orc, 0.1389)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto1Orc, 0.0862)
	per.AddAnimSound('Ork_clmb_medlow_no', EsfuerzoCorto2Orc, 0.4000)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCorto2Orc, 0.1944)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto1Orc, 0.1552)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCortoOrc, 0.2400)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto3Orc, 0.1389)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCortoOrc, 0.0862)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCortoOrc, 0.4000)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto3Orc, 0.1944)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCortoOrc, 0.1552)

	per.AddAnimSound("Ork_dth0", MuerteOrc1, 0.1130)
	per.AddAnimSound("Ork_dth0", AndarOrc1, 0.2000)
	per.AddAnimSound("Ork_dth0", AndarOrc2, 0.4000)
	per.AddAnimSound("Ork_dth0", AndarOrc1, 0.6000)
	per.AddAnimSound("Ork_dth0", AndarOrc2, 0.7200)
	per.AddAnimSound("Ork_dth0", CaidaOrc1, 0.8900)
	per.AddAnimSound("Ork_dth_i1", MuerteOrc1, 0.1130)
	per.AddAnimSound("Ork_dth_i2", MuerteOrc4, 0.1130)
	per.AddAnimSound("Ork_dth_bl1", MuerteOrc2, 0.1130)
	per.AddAnimSound("Ork_dth_bl2", MuerteOrc1, 0.1130)
	per.AddAnimSound("Ork_dth_rock", MuerteOrc3, 0.1130)
	per.AddAnimSound("Ork_dth_n00", MuerteOrc1, 0.1100)
	per.AddAnimSound("Ork_dth_n00", CaidaOrc1, 0.8000)
	per.AddAnimSound("Ork_dth_n01", MuerteOrc2, 0.1100)
	per.AddAnimSound("Ork_dth_n01", CaidaOrc1, 0.7800)
	per.AddAnimSound("Ork_dth_n02", MuerteOrc3, 0.1200)
	per.AddAnimSound("Ork_dth_n02", CaidaOrc1, 0.8000)
	per.AddAnimSound("Ork_dth_n03", MuerteOrc4, 0.1200)
	per.AddAnimSound("Ork_dth_n03", CaidaOrc1, 0.7550)
	per.AddAnimSound("Ork_dth_n04", MuerteOrc4, 0.1100)
	per.AddAnimSound("Ork_dth_n04", CaidaOrc1, 0.7600)
	per.AddAnimSound("Ork_dth_n05", MuerteOrc4, 0.1100)
	per.AddAnimSound("Ork_dth_n05", CaidaOrc1, 0.7700)
	per.AddAnimSound("Ork_dth_n06", MuerteOrc2, 0.1200)
	per.AddAnimSound("Ork_dth_n06", CaidaOrc1, 0.7900)
	per.AddAnimSound("Ork_dth_c1", DesangreOrc1, 0.1250)
	per.AddAnimSound("Ork_dth_c1", CaidaOrc1, 0.7800)
	per.AddAnimSound("Ork_dth_c1", DesangreOrc1, 0.2500)
	per.AddAnimSound("Ork_dth_c2", DesangreOrc1, 0.1250)
	per.AddAnimSound("Ork_dth_c2", DesangreOrc1, 0.2500)
	per.AddAnimSound("Ork_dth_c2", CaidaOrc1, 0.7720)
	per.AddAnimSound("Ork_dth_c2", CaidaOrc2, 0.8720)
	per.AddAnimSound("Ork_dth_c3", DesangreOrc1, 0.1250)
	per.AddAnimSound("Ork_dth_c3", DesangreOrc1, 0.2500)
	per.AddAnimSound("Ork_dth_c3", CaidaOrc1, 0.7220)
	per.AddAnimSound("Ork_dth_c4", DesangreOrc1, 0.1250)
	per.AddAnimSound("Ork_dth_c4", DesangreOrc1, 0.2500)
	per.AddAnimSound("Ork_dth_c4", CaidaOrc1, 0.7000)
	per.AddAnimSound("Ork_dth_c4", CaidaOrc2, 0.8720)
	per.AddAnimSound("Ork_dth_c5", DesangreOrc1, 0.1250)
	per.AddAnimSound("Ork_dth_c5", DesangreOrc1, 0.2500)
	per.AddAnimSound("Ork_dth_c5", CaidaOrc1, 0.7720)
	per.AddAnimSound("Ork_dth_c5", CaidaOrc2, 0.5500)
	per.AddAnimSound("Ork_dth_c6", DesangreOrc1, 0.1250)
	per.AddAnimSound("Ork_dth_c6", DesangreOrc1, 0.2500)
	per.AddAnimSound("Ork_dth_c6", CaidaOrc1, 0.7700)
	per.AddAnimSound("Ork_dth_c7", DesangreOrc1, 0.1250)
	per.AddAnimSound("Ork_dth_c7", DesangreOrc1, 0.2500)
	per.AddAnimSound("Ork_dth_c7", CaidaOrc1, 0.6300)
	per.AddAnimSound("Ork_dth_c7", CaidaOrc2, 0.6900)

	per.AddAnimSound("Ork_hurt_jog", HeridaOrc1, 0.5714)
	per.AddAnimSound("Ork_hurt_neck", HeridaOrc2, 0.3158)
	per.AddAnimSound("Ork_hurt_breast", HeridaOrc2, 0.3889)
	per.AddAnimSound("Ork_hurt_back", HeridaOrc2, 0.1282)
	per.AddAnimSound("Ork_hurt_r_arm", HeridaOrc2, 0.4706)
	per.AddAnimSound("Ork_hurt_l_arm", HeridaOrc3, 0.5333)
	per.AddAnimSound("Ork_hurt_r_leg", HeridaOrc1, 0.4706)
	per.AddAnimSound("Ork_hurt_l_leg", HeridaOrc2, 0.4375)
	per.AddAnimSound("Ork_hurt_f_head", HeridaOrc3, 0.3333)
	per.AddAnimSound("Ork_hurt_f_neck", HeridaOrc2, 0.3158)
	per.AddAnimSound("Ork_hurt_f_breast", HeridaOrc2, 0.3889)
	per.AddAnimSound("Ork_hurt_f_back", HeridaOrc2, 0.4211)
	per.AddAnimSound("Ork_hurt_f_r_arm", HeridaOrc1, 0.2000)
	per.AddAnimSound("Ork_hurt_f_l_arm", HeridaOrc3, 0.1786)
	per.AddAnimSound("Ork_hurt_f_r_leg", HeridaOrc2, 0.4706)
	per.AddAnimSound("Ork_hurt_f_l_leg", HeridaOrc2, 0.4375)
	per.AddAnimSound("Ork_hurt_f_lite", HeridaOrc1, 0.4615)
	per.AddAnimSound("Ork_hurt_f_big", HeridaOrc3, 0.5000)
	per.AddAnimSound("Ork_hurt_head", HeridaOrc2, 0.6000)

	per.AddAnimSound("Ork_Rlx_1h_00", Relax1, 0.3000)
	per.AddAnimSound("Ork_Rlx_1h_00", Relax2, 0.6000)
	per.AddAnimSound("Ork_Rlx_b_00", Relax1, 0.3000)
	per.AddAnimSound("Ork_Rlx_b_00", Relax2, 0.6000)
	per.AddAnimSound("Ork_Rlx_cold_00", Relax1, 0.3000)
	per.AddAnimSound("Ork_Rlx_cold_00", Relax2, 0.6000)
	per.AddAnimSound("Rlx_no_Ork", Relax1, 0.1500)
	per.AddAnimSound("Rlx_no_Ork", Relax2, 0.3000)
	per.AddAnimSound("Rlx_no_Ork", Relax1, 0.6000)
	per.AddAnimSound("Rlx_no_Ork", Relax2, 0.9000)
	per.AddAnimSound("Ork_Rlx_fatigue_00", Relax1, 0.3000)
	per.AddAnimSound("Ork_Rlx_fatigue_00", Relax2, 0.6000)
	per.AddAnimSound("Rlx_1h_Ork", Relax1, 0.3000)
	per.AddAnimSound("Rlx_1h_Ork", Relax2, 0.6000)


	per.AddAnimSound("Ork_attack_f", GritoOrc1, 0.1200)
	per.AddAnimSound("Ork_attack_f_s", GritoOrc2, 0.1200)
	per.AddAnimSound("Ork_attack_b", GritoOrc1, 0.1200)
	per.AddAnimSound("Ork_attack_b_s", GritoOrc2, 0.1200)
	per.AddAnimSound("Ork_attack_r", GritoOrc1, 0.1200)
	per.AddAnimSound("Ork_attack_r_s", GritoOrc2, 0.1200)
	per.AddAnimSound("Ork_attack_d_b", GritoOrc1, 0.1200)
	per.AddAnimSound("Ork_attack_d_r", GritoOrc2, 0.1200)
	per.AddAnimSound("Ork_attack_d_l", GritoOrc1, 0.1200)
	per.AddAnimSound("Ork_attack_l", GritoOrc2, 0.1200)
	per.AddAnimSound("Ork_attack_l_s", GritoOrc1, 0.1200)
	per.AddAnimSound("Ork_attack_rlx", GritoOrc2, 0.1200)
	per.AddAnimSound("Ork_attack_rlx_s", GritoOrc1, 0.1200)


	per.AddAnimSound("Ork_insult", InsultoOrg, 0.1590)
	per.AddAnimSound("Ork_insult", Relax2, 0.8000)


	per.AddAnimSound("Jog_1h_Ork", GritoOrc2, 0.1100)
	per.AddAnimSound("Jog_1h_Ork", GritoOrc2, 0.6000)

	per.AddAnimSound("Wlk_1h_Ork", Relax1, 0.0534)
	per.AddAnimSound("Wlk_1h_Ork", Relax2, 0.3000)
	per.AddAnimSound("Wlk_1h_Ork", Relax1, 0.6000)
	per.AddAnimSound("Wlk_1h_Ork", Relax2, 0.9000)
	
	per.AddAnimSound("Wlk_b_Ork", Relax1, 0.0534)
	per.AddAnimSound("Wlk_b_Ork", Relax2, 0.3000)
	per.AddAnimSound("Wlk_b_Ork", Relax1, 0.6000)
	per.AddAnimSound("Wlk_b_Ork", Relax2, 0.9000)
	
	per.AddAnimSound("Wbk_b_Ork", Relax1, 0.0534)
	per.AddAnimSound("Wbk_b_Ork", Relax2, 0.3000)
	per.AddAnimSound("Wbk_b_Ork", Relax1, 0.6000)
	per.AddAnimSound("Wbk_b_Ork", Relax2, 0.9000)
	
	per.AddAnimSound("Ork_patrol1", Relax1, 0.0534)
	per.AddAnimSound("Ork_patrol1", Relax2, 0.3000)
	per.AddAnimSound("Ork_patrol1", Relax1, 0.6000)
	per.AddAnimSound("Ork_patrol1", Relax2, 0.9000)
	
	per.AddAnimSound("Ork_patrol2", Relax1, 0.0534)
	per.AddAnimSound("Ork_patrol2", Relax2, 0.3000)
	per.AddAnimSound("Ork_patrol2", Relax1, 0.6000)
	per.AddAnimSound("Ork_patrol2", Relax2, 0.9000)
	
	per.AddAnimSound("Ork_attack_b", Relax1, 0.0534)
	per.AddAnimSound("Ork_attack_b", Relax2, 0.3000)
	per.AddAnimSound("Ork_attack_b", Relax1, 0.6000)
	per.AddAnimSound("Ork_attack_b", Relax2, 0.9000)



