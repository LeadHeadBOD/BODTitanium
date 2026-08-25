##///
##||| AniSoundGdm.PY TITANIUM
##||| Change list:
##||| * added gdm-quake
##||| * added sounds for back attack
##\\\ 

import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosGreatDemonCalled=0
def AsignarSonidosGreatDemon(Personaje):
	from AniSoundGdmX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('impale', TajoEmpalanteGdm)
	per.AddEventSound('slash', TajoCortanteGdm)
	per.AddEventSound('mutilate', TajoMutilacionGdm)
	per.AddEventSound('crush', GolpeContundenteGdm)
	
	
	global AsignarSonidosGreatDemonCalled
	if AsignarSonidosGreatDemonCalled:
		return
	AsignarSonidosGreatDemonCalled=1


	# Sonidos de animaciones
	
	per.AddAnimSound('Gdm_g_back',SesgadoCortoGrave,0.2200)
	per.AddAnimSound('Gdm_g_back',EsfuerzoLargo1Gdm,0.2150)
	per.AddAnimSound('Gdm_g_back',SesgadoLargoGrave,0.2150)
	per.AddAnimSound('Gdm_g_claw',SesgadoLargoGrave,0.3200)
	per.AddAnimSound('Gdm_g_claw',EsfuerzoCorto1Gdm,0.3000)
	per.AddAnimSound('Gdm_g_claw',SesgadoCortoGrave,0.6960)
	per.AddAnimSound('Gdm_g_claw',EsfuerzoCorto2Gdm,0.6000)
	per.AddAnimSound('Gdm_g_01',EsfuerzoLargo2Gdm,0.1600)
	per.AddAnimSound('Gdm_g_01',SesgadoLargoGrave,0.3700)
	per.AddAnimSound('Gdm_g_12',EsfuerzoLargo3Gdm,0.1600)
	per.AddAnimSound('Gdm_g_12',SesgadoCortoGrave,0.3700)
	per.AddAnimSound('Gdm_g_12',EsfuerzoLargo1Gdm,0.1600)
	per.AddAnimSound('Gdm_g_12',SesgadoLargoGrave,0.3700)
	per.AddAnimSound('Gdm_g_12',EsfuerzoCorto1Gdm,0.7690)
	
	### Added 		-LeadHead
	per.AddAnimSound('Gdm_g_back',EsfuerzoLargo3Gdm,0.1600)
	per.AddAnimSound('Gdm_g_back',SesgadoCortoGrave,0.2850)
	per.AddAnimSound('Gdm_g_back',EsfuerzoLargo1Gdm,0.1600)
	per.AddAnimSound('Gdm_g_back',SesgadoLargoGrave,0.4200)
	per.AddAnimSound('Gdm_g_back',EsfuerzoCorto1Gdm,0.7690)

	per.AddAnimSound('Gdm_g_quake',EsfuerzoCorto1Gdm,0.1000)
	per.AddAnimSound('Gdm_g_quake',EsfuerzoCorto3Gdm,0.2000)
	per.AddAnimSound('Gdm_g_quake',SesgadoCortoGrave,0.2200)
	per.AddAnimSound('Gdm_g_quake',SesgadoCortoGrave,0.4850)	# Add
	per.AddAnimSound('Gdm_g_quake',EsfuerzoCorto1Gdm,0.6510)
	per.AddAnimSound('Gdm_g_quake',EsfuerzoCorto1Gdm,0.8750)
	per.AddAnimSound('Gdm_g_quake',gQuake,0.2820)				# Added -LeadHead
	per.AddAnimSound('Gdm_g_spitball',EsfuerzoLargo2Gdm,0.1500)
	per.AddAnimSound('Gdm_g_spitball',LanzarFuego1Gdm,0.4300)
	per.AddAnimSound('Gdm_g_spitball',SesgadoCortoGrave,0.4300)
	per.AddAnimSound('Gdm_g_spitball',EsfuerzoLargo1Gdm,0.8000)
	per.AddAnimSound('Gdm_g_spit_around',LanzarFuego2Gdm,0.1750)
	per.AddAnimSound('Gdm_g_spit_around',EsfuerzoCorto3Gdm,0.1750)
	per.AddAnimSound('Gdm_g_spit_around',LanzarFuego3Gdm,0.1100)
	per.AddAnimSound('Gdm_g_spit_around',RespiracionGdm1,0.8000)
	per.AddAnimSound('Gdm_g_spit_f',LanzarFuego2Gdm,0.1750)
	per.AddAnimSound('Gdm_g_spit_f',EsfuerzoCorto1Gdm,0.8900)
	per.AddAnimSound('Gdm_g_spit_f',LanzarFuego3Gdm,0.1100)
	per.AddAnimSound('Gdm_g_spit_f',EsfuerzoCorto3Gdm,0.5000)
	
	per.AddAnimSound('Gdm_hurt_big',herida1Gdm,0.1880)
	per.AddAnimSound('Gdm_hurt_big',herida2Gdm,0.4000)
	
	per.AddAnimSound('Gdm_mgc_df',herida1Gdm,0.1700)
	per.AddAnimSound('Gdm_mgc_df',herida2Gdm,0.6110)
	per.AddAnimSound('Gdm_mgc_df',Fuego2,0.2000)
	
	per.AddAnimSound('Gdm_mgc_hurt',herida1Gdm,0.1300)
	per.AddAnimSound('Gdm_mgc_hurt',herida2Gdm,0.6110)
	
	#per.AddAnimSound('Gdm_rlx_no',Herida1Gdm,0.6110)
	#per.AddAnimSound('Gdm_rlx_no',Herida1Gdm,0.6110)
	#per.AddAnimSound('Gdm_rlx_no',Herida1Gdm,0.6110)
	
	per.AddAnimSound('Gdm_take_lamp',EsfuerzoCorto2Gdm,0.1700)		#	PLAGUE: Wtf is this anim
	per.AddAnimSound('Gdm_take_lamp',EsfuerzoCorto1Gdm,0.6110)		#
	
	per.AddAnimSound('Gdm_wlk_no',EsfuerzoCorto2Gdm,0.1700)
	per.AddAnimSound('Gdm_wlk_no',EsfuerzoCorto1Gdm,0.6110)
	
	
	per.AddAnimSound('Gdm_wbk_no',EsfuerzoCorto2Gdm,0.1700)
	per.AddAnimSound('Gdm_wbk_no',EsfuerzoCorto1Gdm,0.6110)
	
	per.AddAnimSound('Gdm_appears',EsfuerzoCorto1Gdm,0.6110)
	
	per.AddAnimSound('Gdm_g_magic',Fuego1,0.1100)
	
	per.AddAnimSound('Gdm_dth0',MuerteGdm,0.1000)
	
	per.AddAnimSound('Gdm_rlx_no',RespiracionGdm1,0.1000)
	per.AddAnimSound('Gdm_rlx_no',RespiracionGdm2,0.3000)
	per.AddAnimSound('Gdm_rlx_no',RespiracionGdm1,0.6000)
	per.AddAnimSound('Gdm_rlx_no',RespiracionGdm2,0.9000)
	
	per.AddAnimSound('Gdm_wlk_no',RespiracionGdm1,0.1000)
	
	per.AddAnimSound('Gdm_wbk_no',RespiracionGdm1,0.1000)
	