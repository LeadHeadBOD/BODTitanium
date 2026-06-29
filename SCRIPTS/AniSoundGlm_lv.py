##///
##||| AniSoundGlm_lv.PY TITANIUM
##||| Change list:
##||| * Added sounds for spit attack
##\\\ 

import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************


AsignarSonidosGolem_lvCalled=0
def AsignarSonidosGolem_lv(Personaje):

	#Sonido continuo-> Nec uno por cada personaje!!!!
	import Actions
	Actions.LinkContinuosSound(Personaje,"../../sounds/m-loop-lavahervidero-1.wav")

	from AniSoundGlm_lvX import *

	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos
	#per.AddEventSound('shield_block', GolpeArmaEscudoGlmlv)
	#per.AddEventSound('weapon_block', GolpeArmaArmaGlmlv)
	per.AddEventSound('impale', TajoEmpalanteGlmlv)
	per.AddEventSound('slash', TajoCortanteGlmlv)
	per.AddEventSound('mutilate', TajoMutilacionGlmlv)
	per.AddEventSound('crush', GolpeContundenteGlmlv)


	global AsignarSonidosGolem_lvCalled
	if AsignarSonidosGolem_lvCalled:
		return
	AsignarSonidosGolem_lvCalled=1


	# Sonidos de animaciones


	per.AddAnimSound('Glm_g_01', EsfuerzoGlmlv1, 0.3790)
	per.AddAnimSound('Glm_g_01', SesgadoGlmlv1, 0.4000)
	per.AddAnimSound('Glm_g_12', SesgadoGlmlv2, 0.3880)
	per.AddAnimSound('Glm_g_12', EsfuerzoGlmlv2, 0.3050)
	per.AddAnimSound('Glm_g_21', SesgadoGlmlv3, 0.3440)
	per.AddAnimSound('Glm_g_21', EsfuerzoGlmlv3, 0.3000)
	per.AddAnimSound('Glm_g_31', SesgadoGlmlv4, 0.3000)
	per.AddAnimSound('Glm_g_31', EsfuerzoGlmlv4, 0.2840)
	per.AddAnimSound('Glm_g_31', caidaGlmlv2, 0.3240)
	per.AddAnimSound('Glm_g_114', SesgadoGlmlv5, 0.4350)
	per.AddAnimSound('Glm_g_114', EsfuerzoGlmlv5, 0.2390)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmlv6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmlv6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmlv7, 0.5430)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmlv7, 0.5430)
	per.AddAnimSound('Glm_g_1tw', CreaPiedraGlmlv, 0.2000)

	# add sounds for spitting	-LeadHead
	per.AddAnimSound('Glm_g_spit', EsfuerzoGlmlv1, 0.2000)
	per.AddAnimSound('Glm_g_spit', EsfuerzoGlmlv2, 0.3500)
	per.AddAnimSound('Glm_g_spit', LanzarFuego1GlmLv, 0.3600)

	per.AddAnimSound('Glm_dth0', caidaGlmlv, 0.7720)
	per.AddAnimSound('Glm_dth0', MuerteGlmlv1, 0.1590)
	per.AddAnimSound('Glm_dth2', caidaGlmlv, 0.7720)
	per.AddAnimSound('Glm_dth2', MuerteGlmlv1, 0.1590)
	per.AddAnimSound('Glm_dth_c1', caidaGlmlv, 0.9150)
	per.AddAnimSound('Glm_dth_c1', caidaGlmlv2, 0.6270)
	per.AddAnimSound('Glm_dth_c1', MuerteGlmlv1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidaGlmlv2, 0.5830)
	per.AddAnimSound('Glm_dth_i1', caidaGlmlv3, 0.7020)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmlv1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidaGlmlv2, 0.3630)
	per.AddAnimSound('Glm_dth_i1', caidaGlmlv3, 0.6200)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmlv1, 0.1590)


	per.AddAnimSound('Glm_hurt_big', HeridaGlmlv1, 0.1670)
	per.AddAnimSound('Glm_hurt_lite', HeridaGlmlv2, 0.1720)
