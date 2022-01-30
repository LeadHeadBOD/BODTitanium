import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosGolem_icCalled=0
def AsignarSonidosGolem_ic(Personaje):
	
	from AniSoundGlm_icX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('impale', TajoEmpalanteGlm)
	per.AddEventSound('slash', TajoCortanteGlm)
	#per.AddEventSound('mutilate', TajoMutilacionGlm)
	per.AddEventSound('crush', GolpeContundenteGlm)
	
	
	global AsignarSonidosGolem_Called
	if AsignarSonidosGolem_icCalled:
		return
	AsignarSonidosGolem_icCalled=1

	



	# Sonidos de animaciones
	
	
	
	per.AddAnimSound('Glm_g_01', EsfuerzoGlm1, 0.3790)
	per.AddAnimSound('Glm_g_01', SesgadoGlm1, 0.4000)
	per.AddAnimSound('Glm_g_12', SesgadoGlm2, 0.3880)
	per.AddAnimSound('Glm_g_12', EsfuerzoGlm2, 0.3050)
	per.AddAnimSound('Glm_g_21', SesgadoGlm3, 0.3440)
	per.AddAnimSound('Glm_g_21', EsfuerzoGlm3, 0.3000)
	per.AddAnimSound('Glm_g_31', SesgadoGlm4, 0.3000)
	per.AddAnimSound('Glm_g_31', EsfuerzoGlm4, 0.2840)
	per.AddAnimSound('Glm_g_31', caidagolem2, 0.3240)
	per.AddAnimSound('Glm_g_114', SesgadoGlm5, 0.4350)
	per.AddAnimSound('Glm_g_114', EsfuerzoGlm5, 0.2390)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlm6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlm6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlm7, 0.5430)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlm7, 0.5430)
	per.AddAnimSound('Glm_g_1tw', CreaPiedraGlm, 0.2000)
	
	per.AddAnimSound('Glm_dth0', caidagolem, 0.7720)
	per.AddAnimSound('Glm_dth0', MuerteGlm1, 0.1590)
	per.AddAnimSound('Glm_dth2', caidagolem, 0.7720)
	per.AddAnimSound('Glm_dth2', MuerteGlm1, 0.1590)
	per.AddAnimSound('Glm_dth_c1', caidagolem, 0.9150)
	per.AddAnimSound('Glm_dth_c1', caidagolem2, 0.6270)
	per.AddAnimSound('Glm_dth_c1', MuerteGlm1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolem2, 0.5830)
	per.AddAnimSound('Glm_dth_i1', caidagolem3, 0.7020)
	per.AddAnimSound('Glm_dth_i1', MuerteGlm1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolem2, 0.3630)
	per.AddAnimSound('Glm_dth_i1', caidagolem3, 0.6200)
	per.AddAnimSound('Glm_dth_i1', MuerteGlm1, 0.1590)


	per.AddAnimSound('Glm_hurt_big', HeridaGlm1, 0.2000)
	per.AddAnimSound('Glm_hurt_lite', HeridaGlm2, 0.2000)
	
	
	
	