##///
##||| AniSoundAnk.PY TITANIUM
##||| Change list:
##||| * Commented out non-existent attack
##||| *  "AsignarSonidosAnAhkard" should actually be "AsignarSonidosAnAhkardCalled" otherwise no sounds ever get assigned.
##\\\ 

import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosAnAhkardCalled=0
def AsignarSonidosAnAhkard(Personaje):


	from AniSoundAnkX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoAnk)
	per.AddEventSound('weapon_block', GolpeArmaArmaAnk)
	per.AddEventSound('impale', TajoEmpalanteAnk)
	per.AddEventSound('slash', TajoCortanteAnk)
	per.AddEventSound('mutilate', TajoMutilacionAnk)
	per.AddEventSound('crush', GolpeContundenteAnk)
	
	global AsignarSonidosAnAhkardCalled
	if AsignarSonidosAnAhkardCalled:
		return
	AsignarSonidosAnAhkardCalled=1




	# Sonidos de animaciones	
	
	per.AddAnimSound('Ank_g_mgc01', SesgadoCorto, 0.1790)
	per.AddAnimSound('Ank_g_mgc01', SesgadoLargo, 0.2390)
	per.AddAnimSound('Ank_g_mgc01', EsfuerzoGolpeArribaAnk, 0.4490)
	per.AddAnimSound('Ank_g_mgc01', SesgadoGrave, 0.5450)
	per.AddAnimSound('Ank_g_mgc01', RisaAnk1, 0.5200)
	per.AddAnimSound('Ank_g_mgc02', EsfuerzoGolpeFrontalAnk, 0.4700)
	per.AddAnimSound('Ank_g_mgc02', SesgadoGrave, 0.5520)
	per.AddAnimSound('Ank_g_mgc02', RisaAnk2, 0.5520)
	per.AddAnimSound('Ank_g_mgc03', SesgadoLargo, 0.3290)
	per.AddAnimSound('Ank_g_mgc03', SesgadoCorto, 0.6900)
	per.AddAnimSound('Ank_g_mgc03', EsfuerzoGolpeArribaAnk, 0.3000)
	
	per.AddAnimSound('Ank_g_01', EsfuerzoGolpeFrontalAnk, 0.2000)
	per.AddAnimSound('Ank_g_01', SesgadoCorto, 0.1000)
	per.AddAnimSound('Ank_g_01', SesgadoGrave, 0.3780)
	per.AddAnimSound('Ank_g_01', RespiracionAnk2, 0.5000)
	per.AddAnimSound('Ank_g_02', EsfuerzoGolpeArribaAnk, 0.2780)
	per.AddAnimSound('Ank_g_02', SesgadoGrave, 0.3250)
	per.AddAnimSound('Ank_g_02', SesgadoLargo, 0.3350)
	per.AddAnimSound('Ank_g_02', RespiracionAnk1, 0.5000)
	"""	The following animations do not exist. There is no point trying to assign any sounds to them. -LeadHead
	
    per.AddAnimSound('Ank_g_03', EsfuerzoGolpeFrontalAnk, 0.1700) 
	per.AddAnimSound('Ank_g_03', SesgadoGrave, 0.2000)
	per.AddAnimSound('Ank_g_03', SesgadoLargo, 0.2740)
	per.AddAnimSound('Ank_g_03', SesgadoCorto, 0.3150)
	per.AddAnimSound('Ank_g_03', SesgadoLargo, 0.3700)
	per.AddAnimSound('Ank_g_03', SesgadoCorto, 0.4250)
	per.AddAnimSound('Ank_g_03', SesgadoLargo, 0.4800)
	"""
	per.AddAnimSound('Ank_g_07', SesgadoLargo, 0.1100)
	per.AddAnimSound('Ank_g_07', EsfuerzoGolpeArribaAnk, 0.2900)
	per.AddAnimSound('Ank_g_07', SesgadoGrave, 0.3380)
	per.AddAnimSound('Ank_g_07', RisaAnk2, 0.3380)
	
	per.AddAnimSound('Ank_fll', CaidaAnk, 0.3170)
	per.AddAnimSound('Ank_fll', EsfuerzoCorto1Ank, 0.6000)
	
	per.AddAnimSound('Wbk_no_Ank', RisaAnk2, 0.1500)
	#per.AddAnimSound('Wbk_no_Ank', EsfuerzoCorto3Ank, 0.5900)
	
	per.AddAnimSound('Wlk_no_Ank', RisaAnk1, 0.1000)
	per.AddAnimSound('Wlk_no_Ank', EsfuerzoCorto3Ank, 0.3000)
	
	per.AddAnimSound('Rlx_no_Ank', RespiracionAnk1, 0.2500)
	per.AddAnimSound('Rlx_no_Ank', RespiracionAnk2, 0.6000)
	
	
	
	
	
	
	