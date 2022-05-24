import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

#I dont know what this variable does, but it crashes if i dont comment it out
#Must do further testing, potentially can save performane
#Might be because I am testing on saved games
#AsignarSonidosGolem_icCalled=0
def AsignarSonidosGolem_ic(Personaje):
	
	from AniSoundGlm_icX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('impale', TajoEmpalanteGlmic)
	per.AddEventSound('slash', TajoCortanteGlmic)
	#per.AddEventSound('mutilate', TajoMutilacionGlm)
	per.AddEventSound('crush', GolpeContundenteGlmic)
    
    
	
	
#	global AsignarSonidosGolem_Called
#	if AsignarSonidosGolem_icCalled:
#		return
#	AsignarSonidosGolem_icCalled=1





	# Sonidos de animaciones
	
	
	
	per.AddAnimSound('Glm_g_01', EsfuerzoGlmic1, 0.3790)
	per.AddAnimSound('Glm_g_01', SesgadoGlmic1, 0.4000)
	per.AddAnimSound('Glm_g_12', SesgadoGlmic2, 0.3880)
	per.AddAnimSound('Glm_g_12', EsfuerzoGlmic2, 0.3050)
	per.AddAnimSound('Glm_g_21', SesgadoGlmic3, 0.3440)
	per.AddAnimSound('Glm_g_21', EsfuerzoGlmic3, 0.3000)
	per.AddAnimSound('Glm_g_31', SesgadoGlmic4, 0.3000)
	per.AddAnimSound('Glm_g_31', EsfuerzoGlmic4, 0.2840)
	per.AddAnimSound('Glm_g_31', caidagolemic2, 0.3240)
	per.AddAnimSound('Glm_g_114', SesgadoGlmic5, 0.4350)
	per.AddAnimSound('Glm_g_114', EsfuerzoGlmic5, 0.2390)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmic6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmic6, 0.2750)
	per.AddAnimSound('Glm_g_21_27', SesgadoGlmic7, 0.5430)
	per.AddAnimSound('Glm_g_21_27', EsfuerzoGlmic7, 0.5430)
	per.AddAnimSound('Glm_g_1tw', CreaPiedraGlmic, 0.2000)
	
	per.AddAnimSound('Glm_dth0', caidagolemic, 0.7720)
	per.AddAnimSound('Glm_dth0', MuerteGlmic1, 0.1590)
	per.AddAnimSound('Glm_dth2', caidagolemic, 0.7720)
	per.AddAnimSound('Glm_dth2', MuerteGlmic1, 0.1590)
	per.AddAnimSound('Glm_dth_c1', caidagolemic, 0.9150)
	per.AddAnimSound('Glm_dth_c1', caidagolemic2, 0.6270)
	per.AddAnimSound('Glm_dth_c1', MuerteGlmic1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolemic2, 0.5830)
	per.AddAnimSound('Glm_dth_i1', caidagolemic3, 0.7020)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmic1, 0.1590)
	per.AddAnimSound('Glm_dth_i1', caidagolemic2, 0.3630)
	per.AddAnimSound('Glm_dth_i1', caidagolemic3, 0.6200)
	per.AddAnimSound('Glm_dth_i1', MuerteGlmic1, 0.1590)


	per.AddAnimSound('Glm_hurt_big', HeridaGlmic1, 0.2000)
	per.AddAnimSound('Glm_hurt_lite', HeridaGlmic2, 0.2000)
	
	
	
	