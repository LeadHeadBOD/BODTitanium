##///
##||| ANISOUNDORG.PY TITANIUM
##||| Change list:
##||| * CREATED
##\\\ 

import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosOrcoGoldCalled=0
def AsignarSonidosOrcoGold(Personaje):

	from AniSoundOrgX import *

	per=Bladex.GetEntity(Personaje)
	

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoOrg)
	per.AddEventSound('weapon_block', GolpeArmaArmaOrg)
	per.AddEventSound('impale', TajoEmpalanteOrg)
	per.AddEventSound('slash', TajoCortanteOrg)
	per.AddEventSound('mutilate', TajoMutilacionOrg)
	per.AddEventSound('crush', GolpeContundenteOrg)
	
	
	global AsignarSonidosOrcoGoldCalled
	if AsignarSonidosOrcoGoldCalled:
		return
	AsignarSonidosOrcoGoldCalled=1


	# Sonidos de animaciones

	# Animation Alarm (We want a selection of sounds, so better link a function)
	per.AddAnimSound('Ork_alarm01', InsultoOrg, 0.3000)
	
	per.AddAnimSound('Ork_order', InsultoOrg, 0.6610)
	per.AddAnimSound('Ork_order', GritoOrg1, 0.1450)
	per.AddAnimSound('Ork_order', GritoOrg2, 0.3920)
	
	#per.AddAnimSound('Ork_fury', Insulto, 0.6610)
	per.AddAnimSound('Ork_fury', GritoOrg2, 0.3000)
	
	per.AddAnimSound('Ork_g_01', EsfuerzoCortoOrg, 0.1883)
	per.AddAnimSound('Ork_g_02', EsfuerzoCorto1Org, 0.2840)
	per.AddAnimSound('Ork_g_06', EsfuerzoCorto3Org, 0.4583)
	per.AddAnimSound('Ork_g_01', SesgadoCorto, 0.1883)
	per.AddAnimSound('Ork_g_02', SesgadoCortoAgudo, 0.2840)
	per.AddAnimSound('Ork_g_06', SesgadoCorto, 0.4583)
	per.AddAnimSound('Ork_g_15', EsfuerzoGolpeLateralOrg, 0.3651)
	per.AddAnimSound('Ork_g_16', EsfuerzoGolpeLateralOrg, 0.4054)
	per.AddAnimSound('Ork_g_18', EsfuerzoGolpeArribaOrg, 0.4634)
	per.AddAnimSound('Ork_g_15', SesgadoLargo, 0.3730)
	per.AddAnimSound('Ork_g_16', SesgadoLargoAgudo, 0.4054)
	per.AddAnimSound('Ork_g_18', SesgadoLargoGrave, 0.4878)

	per.AddAnimSound('Ork_clmb_medlow_1h', EsfuerzoCorto2Org, 0.2400)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCorto2Org, 0.1389)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto1Org, 0.0862)
	per.AddAnimSound('Ork_clmb_medlow_no', EsfuerzoCorto2Org, 0.4000)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCorto2Org, 0.1944)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto1Org, 0.1552)
	per.AddAnimSound('Ork_clmb_medium_1h', EsfuerzoCortoOrg, 0.2400)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCorto3Org, 0.1389)
	per.AddAnimSound('Ork_clmb_high_1h', EsfuerzoCortoOrg, 0.0862)
	per.AddAnimSound('Ork_clmb_medium_no', EsfuerzoCortoOrg, 0.4000)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCorto3Org, 0.1944)
	per.AddAnimSound('Ork_clmb_high_no', EsfuerzoCortoOrg, 0.1552)

	per.AddAnimSound("Ork_dth0", MuerteOrg1, 0.1130)
	per.AddAnimSound("Ork_dth0", AndarOrg1, 0.2000)
	per.AddAnimSound("Ork_dth0", AndarOrg2, 0.4000)
	per.AddAnimSound("Ork_dth0", AndarOrg1, 0.6000)
	per.AddAnimSound("Ork_dth0", AndarOrg2, 0.7200)
	per.AddAnimSound("Ork_dth0", CaidaOrg1, 0.8900)
	per.AddAnimSound("Ork_dth_i1", MuerteOrg1, 0.1130)
	per.AddAnimSound("Ork_dth_i2", MuerteOrg4, 0.1130)
	per.AddAnimSound("Ork_dth_bl1", MuerteOrg2, 0.1130)
	per.AddAnimSound("Ork_dth_bl2", MuerteOrg1, 0.1130)
	per.AddAnimSound("Ork_dth_rock", MuerteOrg3, 0.1130)
	per.AddAnimSound("Ork_dth_n00", MuerteOrg1, 0.1100)
	per.AddAnimSound("Ork_dth_n00", CaidaOrg1, 0.8000)
	per.AddAnimSound("Ork_dth_n01", MuerteOrg2, 0.1100)
	per.AddAnimSound("Ork_dth_n01", CaidaOrg1, 0.7800)
	per.AddAnimSound("Ork_dth_n02", MuerteOrg3, 0.1200)
	per.AddAnimSound("Ork_dth_n02", CaidaOrg1, 0.8000)
	per.AddAnimSound("Ork_dth_n03", MuerteOrg4, 0.1200)
	per.AddAnimSound("Ork_dth_n03", CaidaOrg1, 0.7550)
	per.AddAnimSound("Ork_dth_n04", MuerteOrg4, 0.1100)
	per.AddAnimSound("Ork_dth_n04", CaidaOrg1, 0.7600)
	per.AddAnimSound("Ork_dth_n05", MuerteOrg4, 0.1100)
	per.AddAnimSound("Ork_dth_n05", CaidaOrg1, 0.7700)
	per.AddAnimSound("Ork_dth_n06", MuerteOrg2, 0.1200)
	per.AddAnimSound("Ork_dth_n06", CaidaOrg1, 0.7900)
	per.AddAnimSound("Ork_dth_c1", DesangreOrg1, 0.1250)
	per.AddAnimSound("Ork_dth_c1", CaidaOrg1, 0.7800)
	per.AddAnimSound("Ork_dth_c1", DesangreOrg1, 0.2500)
	per.AddAnimSound("Ork_dth_c2", DesangreOrg1, 0.1250)
	per.AddAnimSound("Ork_dth_c2", DesangreOrg1, 0.2500)
	per.AddAnimSound("Ork_dth_c2", CaidaOrg1, 0.7720)
	per.AddAnimSound("Ork_dth_c2", CaidaOrg2, 0.8720)
	per.AddAnimSound("Ork_dth_c3", DesangreOrg1, 0.1250)
	per.AddAnimSound("Ork_dth_c3", DesangreOrg1, 0.2500)
	per.AddAnimSound("Ork_dth_c3", CaidaOrg1, 0.7220)
	per.AddAnimSound("Ork_dth_c4", DesangreOrg1, 0.1250)
	per.AddAnimSound("Ork_dth_c4", DesangreOrg1, 0.2500)
	per.AddAnimSound("Ork_dth_c4", CaidaOrg1, 0.7000)
	per.AddAnimSound("Ork_dth_c4", CaidaOrg2, 0.8720)
	per.AddAnimSound("Ork_dth_c5", DesangreOrg1, 0.1250)
	per.AddAnimSound("Ork_dth_c5", DesangreOrg1, 0.2500)
	per.AddAnimSound("Ork_dth_c5", CaidaOrg1, 0.7720)
	per.AddAnimSound("Ork_dth_c5", CaidaOrg2, 0.5500)
	per.AddAnimSound("Ork_dth_c6", DesangreOrg1, 0.1250)
	per.AddAnimSound("Ork_dth_c6", DesangreOrg1, 0.2500)
	per.AddAnimSound("Ork_dth_c6", CaidaOrg1, 0.7700)
	per.AddAnimSound("Ork_dth_c7", DesangreOrg1, 0.1250)
	per.AddAnimSound("Ork_dth_c7", DesangreOrg1, 0.2500)
	per.AddAnimSound("Ork_dth_c7", CaidaOrg1, 0.6300)
	per.AddAnimSound("Ork_dth_c7", CaidaOrg2, 0.6900)

	per.AddAnimSound("Ork_hurt_jog", HeridaOrg1, 0.5714)
	per.AddAnimSound("Ork_hurt_neck", HeridaOrg2, 0.3158)
	per.AddAnimSound("Ork_hurt_breast", HeridaOrg2, 0.3889)
	per.AddAnimSound("Ork_hurt_back", HeridaOrg2, 0.1282)
	per.AddAnimSound("Ork_hurt_r_arm", HeridaOrg2, 0.4706)
	per.AddAnimSound("Ork_hurt_l_arm", HeridaOrg3, 0.5333)
	per.AddAnimSound("Ork_hurt_r_leg", HeridaOrg1, 0.4706)
	per.AddAnimSound("Ork_hurt_l_leg", HeridaOrg2, 0.4375)
	per.AddAnimSound("Ork_hurt_f_head", HeridaOrg3, 0.3333)
	per.AddAnimSound("Ork_hurt_f_neck", HeridaOrg2, 0.3158)
	per.AddAnimSound("Ork_hurt_f_breast", HeridaOrg2, 0.3889)
	per.AddAnimSound("Ork_hurt_f_back", HeridaOrg2, 0.4211)
	per.AddAnimSound("Ork_hurt_f_r_arm", HeridaOrg1, 0.2000)
	per.AddAnimSound("Ork_hurt_f_l_arm", HeridaOrg3, 0.1786)
	per.AddAnimSound("Ork_hurt_f_r_leg", HeridaOrg2, 0.4706)
	per.AddAnimSound("Ork_hurt_f_l_leg", HeridaOrg2, 0.4375)
	per.AddAnimSound("Ork_hurt_f_lite", HeridaOrg1, 0.4615)
	per.AddAnimSound("Ork_hurt_f_big", HeridaOrg3, 0.5000)
	per.AddAnimSound("Ork_hurt_head", HeridaOrg2, 0.6000)

	per.AddAnimSound("Ork_Rlx_1h_00", Relax1Org, 0.3000)
	per.AddAnimSound("Ork_Rlx_1h_00", Relax2Org, 0.6000)
	per.AddAnimSound("Ork_Rlx_b_00", Relax1Org, 0.3000)
	per.AddAnimSound("Ork_Rlx_b_00", Relax2Org, 0.6000)
	per.AddAnimSound("Ork_Rlx_cold_00", Relax1Org, 0.3000)
	per.AddAnimSound("Ork_Rlx_cold_00", Relax2Org, 0.6000)
	per.AddAnimSound("Rlx_no_Ork", Relax1Org, 0.1500)
	per.AddAnimSound("Rlx_no_Ork", Relax2Org, 0.3000)
	per.AddAnimSound("Rlx_no_Ork", Relax1Org, 0.6000)
	per.AddAnimSound("Rlx_no_Ork", Relax2Org, 0.9000)
	per.AddAnimSound("Ork_Rlx_fatigue_00", Relax1Org, 0.3000)
	per.AddAnimSound("Ork_Rlx_fatigue_00", Relax2Org, 0.6000)
	per.AddAnimSound("Rlx_1h_Ork", Relax1Org, 0.3000)
	per.AddAnimSound("Rlx_1h_Ork", Relax2Org, 0.6000)


	per.AddAnimSound("Ork_attack_f", GritoOrg1, 0.1200)
	per.AddAnimSound("Ork_attack_f_s", GritoOrg2, 0.1200)
	per.AddAnimSound("Ork_attack_b", GritoOrg1, 0.1200)
	per.AddAnimSound("Ork_attack_b_s", GritoOrg2, 0.1200)
	per.AddAnimSound("Ork_attack_r", GritoOrg1, 0.1200)
	per.AddAnimSound("Ork_attack_r_s", GritoOrg2, 0.1200)
	per.AddAnimSound("Ork_attack_d_b", GritoOrg1, 0.1200)
	per.AddAnimSound("Ork_attack_d_r", GritoOrg2, 0.1200)
	per.AddAnimSound("Ork_attack_d_l", GritoOrg1, 0.1200)
	per.AddAnimSound("Ork_attack_l", GritoOrg2, 0.1200)
	per.AddAnimSound("Ork_attack_l_s", GritoOrg1, 0.1200)
	per.AddAnimSound("Ork_attack_rlx", GritoOrg2, 0.1200)
	per.AddAnimSound("Ork_attack_rlx_s", GritoOrg1, 0.1200)


	per.AddAnimSound("Ork_insult", InsultoOrg, 0.1590)
	per.AddAnimSound("Ork_insult", Relax2Org, 0.8000)


	per.AddAnimSound("Jog_1h_Ork", GritoOrg2, 0.1100)
	per.AddAnimSound("Jog_1h_Ork", GritoOrg2, 0.6000)

	per.AddAnimSound("Wlk_1h_Ork", Relax1Org, 0.0534)
	per.AddAnimSound("Wlk_1h_Ork", Relax2Org, 0.3000)
	per.AddAnimSound("Wlk_1h_Ork", Relax1Org, 0.6000)
	per.AddAnimSound("Wlk_1h_Ork", Relax2Org, 0.9000)
	
	per.AddAnimSound("Wlk_b_Ork", Relax1Org, 0.0534)
	per.AddAnimSound("Wlk_b_Ork", Relax2Org, 0.3000)
	per.AddAnimSound("Wlk_b_Ork", Relax1Org, 0.6000)
	per.AddAnimSound("Wlk_b_Ork", Relax2Org, 0.9000)
	
	per.AddAnimSound("Wbk_b_Ork", Relax1Org, 0.0534)
	per.AddAnimSound("Wbk_b_Ork", Relax2Org, 0.3000)
	per.AddAnimSound("Wbk_b_Ork", Relax1Org, 0.6000)
	per.AddAnimSound("Wbk_b_Ork", Relax2Org, 0.9000)
	
	per.AddAnimSound("Ork_patrol1", Relax1Org, 0.0534)
	per.AddAnimSound("Ork_patrol1", Relax2Org, 0.3000)
	per.AddAnimSound("Ork_patrol1", Relax1Org, 0.6000)
	per.AddAnimSound("Ork_patrol1", Relax2Org, 0.9000)
	
	per.AddAnimSound("Ork_patrol2", Relax1Org, 0.0534)
	per.AddAnimSound("Ork_patrol2", Relax2Org, 0.3000)
	per.AddAnimSound("Ork_patrol2", Relax1Org, 0.6000)
	per.AddAnimSound("Ork_patrol2", Relax2Org, 0.9000)
	
	per.AddAnimSound("Ork_attack_b", Relax1Org, 0.0534)
	per.AddAnimSound("Ork_attack_b", Relax2Org, 0.3000)
	per.AddAnimSound("Ork_attack_b", Relax1Org, 0.6000)
	per.AddAnimSound("Ork_attack_b", Relax2Org, 0.9000)



