##///
##||| AniSoundMin.PY TITANIUM
##||| Change list:
##||| * Fixed the mistimed "whooshing"
##||| * Commented out non-existent animations and moved all unused to bottom
##||| * Added sounds for the 2 death anims that had none
##\\\ 

import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosMinotaurCalled=0
def AsignarSonidosMinotaur(Personaje):
	from AniSoundMinX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoMin)
	per.AddEventSound('weapon_block', GolpeArmaArmaMin)
	per.AddEventSound('impale', TajoEmpalanteMin)
	per.AddEventSound('slash', TajoCortanteMin)
	per.AddEventSound('mutilate', TajoMutilacionMin)
	per.AddEventSound('crush', GolpeContundenteMin)


	# Sonidos de animaciones
	
	
	global AsignarSonidosMinotaurCalled
	if AsignarSonidosMinotaurCalled:
		return
	AsignarSonidosMinotaurCalled=1
	

	
	per.AddAnimSound('Min_g_01', AndarMin2, 0.1000)
	per.AddAnimSound('Min_g_01', MovimientoMin1, 0.1500)
	per.AddAnimSound('Min_g_01', EsfuerzoCorto1Min, 0.1883)
	per.AddAnimSound('Min_g_01', SesgadoCorto, 0.2840)
	per.AddAnimSound('Min_g_01', SesgadoCorto, 0.5230)		# Was 0.8320
	per.AddAnimSound('Min_g_01', MovimientoMin1, 0.5000)
	per.AddAnimSound('Min_g_01', MovimientoMin2, 0.9000)
	per.AddAnimSound('Min_g_01', MovimientoMin1, 0.7000)
	per.AddAnimSound('Min_g_01', AndarMin1, 0.4000)
	per.AddAnimSound('Min_g_01', AndarMin2, 0.6000)
	
	per.AddAnimSound('Min_g_07', SesgadoLargoGrave, 0.2680)
	per.AddAnimSound('Min_g_07', EsfuerzoCorto3Min, 0.2500)
	per.AddAnimSound('Min_g_07', EsfuerzoGolpeLateralMin, 0.6800)
	per.AddAnimSound('Min_g_07', AndarMin2, 0.4500)
	per.AddAnimSound('Min_g_07', AndarMin1, 0.8000)
	per.AddAnimSound('Min_g_07', AndarMin2, 0.1100)
	per.AddAnimSound('Min_g_07', MovimientoMin1, 0.4000)
	per.AddAnimSound('Min_g_07', MovimientoMin2, 0.6000)
	per.AddAnimSound('Min_g_07', MovimientoMin1, 0.8500)
	
	per.AddAnimSound('Min_g_08', SesgadoLargo, 0.2230)
	per.AddAnimSound('Min_g_08', EsfuerzoCorto4Min, 0.2100)
	per.AddAnimSound('Min_g_08', EsfuerzoGolpeArribaMin, 0.6050)
	per.AddAnimSound('Min_g_08', AndarMin1, 0.4000)
	per.AddAnimSound('Min_g_08', AndarMin2, 0.7500)
	per.AddAnimSound('Min_g_08', AndarMin1, 0.9000)
	per.AddAnimSound('Min_g_08', AndarMin1, 0.1100)
	per.AddAnimSound('Min_g_08', MovimientoMin1, 0.2000)
	per.AddAnimSound('Min_g_08', MovimientoMin2, 0.5000)
	per.AddAnimSound('Min_g_08', MovimientoMin1, 0.8000)
	
	per.AddAnimSound('Min_g_12', EsfuerzoCorto2Min, 0.2700)
	per.AddAnimSound('Min_g_12', SesgadoLargoAgudo, 0.2900)
	per.AddAnimSound('Min_g_12', EsfuerzoCorto4Min, 0.4900)
	per.AddAnimSound('Min_g_12', SesgadoLargo, 0.5080)
	per.AddAnimSound('Min_g_12', AndarMin1, 0.6500)
	per.AddAnimSound('Min_g_12', AndarMin2, 0.8000)
	per.AddAnimSound('Min_g_12', AndarMin2, 0.1500)
	per.AddAnimSound('Min_g_12', MovimientoMin2, 0.1200)
	per.AddAnimSound('Min_g_12', MovimientoMin1, 0.3500)
	per.AddAnimSound('Min_g_12', MovimientoMin2, 0.6000)
	per.AddAnimSound('Min_g_12', MovimientoMin1, 0.7500)
	
	per.AddAnimSound('Min_g_31', EsfuerzoCorto5Min, 0.1600)
	per.AddAnimSound('Min_g_31', SesgadoLargo, 0.1700)
	per.AddAnimSound('Min_g_31', SesgadoLargoAgudo, 0.4100)
	per.AddAnimSound('Min_g_31', EsfuerzoCorto1Min, 0.4000)
	per.AddAnimSound('Min_g_31', SesgadoLargoAgudo, 0.6200)
	per.AddAnimSound('Min_g_31', AndarMin2, 0.5000)
	per.AddAnimSound('Min_g_31', AndarMin1, 0.7500)
	per.AddAnimSound('Min_g_31', AndarMin2, 0.9000)
	per.AddAnimSound('Min_g_31', MovimientoMin1, 0.1200)
	per.AddAnimSound('Min_g_31', MovimientoMin2, 0.5500)
	per.AddAnimSound('Min_g_31', MovimientoMin1, 0.7000)
	per.AddAnimSound('Min_g_31', MovimientoMin2, 0.8500)
	
	
	

	#per.AddAnimSound('Min_clmb_medlow_1h', EsfuerzoCorto1Min, 0.2400)
	#per.AddAnimSound('Min_clmb_medium_1h', EsfuerzoCorto1Min, 0.1389)
	#per.AddAnimSound('Min_clmb_high_1h', EsfuerzoCorto1Min, 0.0862)
	#per.AddAnimSound('Min_clmb_medlow_no', EsfuerzoCortoMin, 0.4000)
	#per.AddAnimSound('Min_clmb_medium_no', EsfuerzoCortoMin, 0.1944)
	#per.AddAnimSound('Min_clmb_high_no', EsfuerzoCorto1Min, 0.1552)
	#per.AddAnimSound('Min_clmb_medium_1h', EsfuerzoCortoMin, 0.2400)
	#per.AddAnimSound('Min_clmb_high_1h', EsfuerzoCorto1Min, 0.1389)
	#per.AddAnimSound('Min_clmb_high_1h', EsfuerzoCortoMin, 0.0862)
	#per.AddAnimSound('Min_clmb_medium_no', EsfuerzoCortoMin, 0.4000)
	#per.AddAnimSound('Min_clmb_high_no', EsfuerzoCorto1Min, 0.1944)
	#per.AddAnimSound('Min_clmb_high_no', EsfuerzoCortoMin, 0.1552)


	per.AddAnimSound("Min_dth0", MuerteMin2, 0.1300)
	per.AddAnimSound("Min_dth0", AgonizaMin2, 0.4000)
	per.AddAnimSound("Min_dth0", CaidaMin1, 0.5000)
	
	### Added "Min_dth_c1"		-LeadHead
	per.AddAnimSound("Min_dth_c1", MovimientoMin2, 0.0930)
	per.AddAnimSound("Min_dth_c1", MovimientoMin1, 0.1530)
	per.AddAnimSound("Min_dth_c1", MovimientoMin2, 0.2680)
	per.AddAnimSound("Min_dth_c1", MovimientoMin1, 0.4110)
	per.AddAnimSound("Min_dth_c1", MovimientoMin1, 0.5620)
	per.AddAnimSound("Min_dth_c1", MovimientoMin1, 0.6660)
	per.AddAnimSound("Min_dth_c1", MovimientoMin2, 0.8640)
	per.AddAnimSound("Min_dth_c1", CaidaMin1,      0.8500)
	
	### Added "Min_dth_n00" 	-LeadHead
	per.AddAnimSound("Min_dth_n00", MovimientoMin2, 0.0740)
	per.AddAnimSound("Min_dth_n00", MuerteMin3,     0.9200)
	per.AddAnimSound("Min_dth_n00", MovimientoMin1, 0.1780)
	per.AddAnimSound("Min_dth_n00", MovimientoMin2, 0.2290)
	per.AddAnimSound("Min_dth_n00", MovimientoMin1, 0.3930)
	per.AddAnimSound("Min_dth_n00", MovimientoMin1, 0.5620)
	per.AddAnimSound("Min_dth_n00", MovimientoMin1, 0.6660)
	per.AddAnimSound("Min_dth_n00", MovimientoMin2, 0.8640)
	per.AddAnimSound("Min_dth_n00", CaidaMin1,      0.9110)
	
	#per.AddAnimSound("Min_dth_n00", MuerteMin2, 0.1200)
	#per.AddAnimSound("Min_dth_i1", MuerteMin1, 0.1200)
	#per.AddAnimSound("Min_dth_bl1", MuerteMin1, 0.1200)

	per.AddAnimSound("Min_hurt_jog", HeridaMin1, 0.5714)
	per.AddAnimSound("Min_hurt_neck", HeridaMin2, 0.3158)
	per.AddAnimSound("Min_hurt_breast", HeridaMin3, 0.3889)
	per.AddAnimSound("Min_hurt_back", HeridaMin4, 0.1282)
	per.AddAnimSound("Min_hurt_r_arm", HeridaMin2, 0.4706)
	per.AddAnimSound("Min_hurt_l_arm", HeridaMin1, 0.5333)
	per.AddAnimSound("Min_hurt_r_leg", HeridaMin3, 0.4706)
	per.AddAnimSound("Min_hurt_l_leg", HeridaMin4, 0.4375)
	per.AddAnimSound("Min_hurt_f_head", HeridaMin2, 0.3333)
	per.AddAnimSound("Min_hurt_f_neck", HeridaMin2, 0.3158)
	per.AddAnimSound("Min_hurt_f_breast", HeridaMin2, 0.3889)
	per.AddAnimSound("Min_hurt_f_back", HeridaMin3, 0.4211)
	per.AddAnimSound("Min_hurt_f_r_arm", HeridaMin1, 0.2000)
	per.AddAnimSound("Min_hurt_f_l_arm", HeridaMin2, 0.1786)
	per.AddAnimSound("Min_hurt_f_r_leg", HeridaMin4, 0.4706)
	per.AddAnimSound("Min_hurt_f_l_leg", HeridaMin2, 0.4375)
	per.AddAnimSound("Min_hurt_f_lite", HeridaMin2, 0.4615)
	per.AddAnimSound("Min_hurt_f_big", HeridaMin1, 0.5000)
	per.AddAnimSound("Min_hurt_head", HeridaMin2, 0.6000)
	per.AddAnimSound("Min_hurt_big", HeridaMin1, 0.1200)
	per.AddAnimSound("Min_hurt_big", HeridaMin4, 0.3350)
	per.AddAnimSound("Min_hurt_big", MuerteMin1, 0.6000)
	per.AddAnimSound("Min_hurt_lite", HeridaMin2, 0.1200)
	
	per.AddAnimSound("Wlk_1h_Min", AndarMin1, 0.1500)
	per.AddAnimSound("Wlk_1h_Min", MovimientoMin1, 0.3000)
	per.AddAnimSound("Wlk_1h_Min", AndarMin2, 0.4500)
	per.AddAnimSound("Wlk_1h_Min", MovimientoMin2, 0.6000)
	per.AddAnimSound("Wlk_1h_Min", AndarMin1, 0.7500)
	per.AddAnimSound("Wlk_1h_Min", MovimientoMin1, 0.9000)
	
	per.AddAnimSound("Wbk_1h_Min", AndarMin1, 0.1500)
	per.AddAnimSound("Wbk_1h_Min", MovimientoMin1, 0.3000)
	per.AddAnimSound("Wbk_1h_Min", AndarMin2, 0.4500)
	per.AddAnimSound("Wbk_1h_Min", MovimientoMin2, 0.6000)
	per.AddAnimSound("Wbk_1h_Min", AndarMin1, 0.7500)
	per.AddAnimSound("Wbk_1h_Min", MovimientoMin1, 0.9000)
	
	per.AddAnimSound("Jog_1h_Min", RespiraMin1, 0.1500)
	per.AddAnimSound("Jog_1h_Min", MovimientoMin1, 0.3000)
	per.AddAnimSound("Jog_1h_Min", RespiraMin2, 0.4500)
	per.AddAnimSound("Jog_1h_Min", MovimientoMin2, 0.6000)
	per.AddAnimSound("Jog_1h_Min", RespiraMin1, 0.7500)
	per.AddAnimSound("Jog_1h_Min", MovimientoMin1, 0.9000)
	
	per.AddAnimSound("Rlx_1h_Min", RespiraMin1, 0.1500)
	per.AddAnimSound("Rlx_1h_Min", MovimientoMin1, 0.3000)
	per.AddAnimSound("Rlx_1h_Min", RespiraMin2, 0.4500)
	per.AddAnimSound("Rlx_1h_Min", MovimientoMin2, 0.6000)
	per.AddAnimSound("Rlx_1h_Min", RespiraMin2, 0.7500)
	per.AddAnimSound("Rlx_1h_Min", MovimientoMin1, 0.9000)
	
	
	



	### PLAGUE: These anims don't exist???
	"""
	per.AddAnimSound('Min_g_02', AndarMin2, 0.1500)
	per.AddAnimSound('Min_g_02', MovimientoMin1, 0.1000)
	per.AddAnimSound('Min_g_02', MovimientoMin2, 0.4000)
	per.AddAnimSound('Min_g_02', MovimientoMin1, 0.5000)
	per.AddAnimSound('Min_g_02', MovimientoMin2, 0.7500)
	per.AddAnimSound('Min_g_02', MovimientoMin2, 0.9000)
	per.AddAnimSound('Min_g_02', EsfuerzoCorto3Min, 0.4583)
	per.AddAnimSound('Min_g_02', AndarMin1, 0.3000)
	per.AddAnimSound('Min_g_02', SesgadoCortoAgudo, 0.1883)
	per.AddAnimSound('Min_g_02', AndarMin2, 0.6000)
	per.AddAnimSound('Min_g_04', EsfuerzoGolpeArribaMin, 0.2840)
	per.AddAnimSound('Min_g_04', SesgadoCortoGrave, 0.4583)
	per.AddAnimSound('Min_g_04', AndarMin1, 0.1500)
	per.AddAnimSound('Min_g_04', MovimientoMin1, 0.3500)
	per.AddAnimSound('Min_g_04', MovimientoMin2, 0.6000)
	per.AddAnimSound('Min_g_04', MovimientoMin1, 0.9000)
	per.AddAnimSound('Min_g_06', EsfuerzoCorto1Min, 0.3651)
	per.AddAnimSound('Min_g_06', SesgadoCorto, 0.4054)
	per.AddAnimSound('Min_g_06', AndarMin2, 0.1500)
	per.AddAnimSound('Min_g_06', MovimientoMin2, 0.2500)
	per.AddAnimSound('Min_g_06', MovimientoMin1, 0.4500)
	per.AddAnimSound('Min_g_06', MovimientoMin2, 0.6000)
	per.AddAnimSound('Min_g_06', MovimientoMin1, 0.8000)
	per.AddAnimSound('Min_g_18', EsfuerzoGolpeArribaMin, 0.4054)
	per.AddAnimSound('Min_g_18', SesgadoLargoGrave, 0.4878)
	per.AddAnimSound('Min_g_18', AndarMin1, 0.1100)
	per.AddAnimSound('Min_g_18', AndarMin2, 0.3000)
	per.AddAnimSound('Min_g_18', AndarMin1, 0.7000)
	per.AddAnimSound('Min_g_18', MovimientoMin1, 0.2000)
	per.AddAnimSound('Min_g_18', MovimientoMin2, 0.3500)
	per.AddAnimSound('Min_g_18', MovimientoMin1, 0.6000)
	per.AddAnimSound('Min_g_18', MovimientoMin2, 0.8000)
	per.AddAnimSound('Min_g_19', EsfuerzoCorto1Min, 0.4224)
	per.AddAnimSound('Min_g_19', SesgadoLargoGrave, 0.4224)
	per.AddAnimSound('Min_g_19', AndarMin1, 0.1100)
	per.AddAnimSound('Min_g_19', AndarMin2, 0.2800)
	per.AddAnimSound('Min_g_19', AndarMin1, 0.6500)
	per.AddAnimSound('Min_g_19', AndarMin2, 0.8800)
	per.AddAnimSound('Min_g_19', MovimientoMin1, 0.2500)
	per.AddAnimSound('Min_g_19', MovimientoMin2, 0.6000)
	per.AddAnimSound('Min_g_19', MovimientoMin1, 0.8000)
	"""