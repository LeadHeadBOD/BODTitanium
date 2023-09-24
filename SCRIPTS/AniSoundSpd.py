##///
##||| ANISOUNDSPD.PY TITANIUM
##||| Change list:
##||| * Fixed spit attack sound
##||| * Commented out non-existant animations.
##\\\ 

import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosAranitaCalled=0
def AsignarSonidosAranita(Personaje):
	from AniSoundSpdX import *

	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoSpd)
	per.AddEventSound('weapon_block', GolpeArmaArmaSpd)
	per.AddEventSound('impale', TajoEmpalanteSpd)
	per.AddEventSound('slash', TajoCortanteSpd)
	per.AddEventSound('mutilate', TajoMutilacionSpd)
	#per.AddEventSound('crush', GolpeContundenteSpd)
	
	
	global AsignarSonidosAranitaCalled
	if AsignarSonidosAranitaCalled:
		return
	AsignarSonidosAranitaCalled=1


	# Sonidos de animaciones

	

	per.AddAnimSound('Spd_g_01', GritoSpd1, 0.4118)
	
	per.AddAnimSound("Spd_g_spit", EscupeSpd, 0.4762)       # Was misnamed as "Spd_spit" -LeadHead
	
	per.AddAnimSound("Spd_walk_no", Movimiento3, 0.0534)
	per.AddAnimSound("Spd_walk_no", Movimiento2, 0.3000)
	per.AddAnimSound("Spd_walk_no", Movimiento3, 0.6500)
	per.AddAnimSound("Spd_walk_no", Movimiento2, 0.9000)
	
	per.AddAnimSound("Spd_dth0", MuerteSpd, 0.1000)  
	per.AddAnimSound("Spd_dth0", Derrite, 0.1200)  
	
	
	per.AddAnimSound("Spd_attack_b", Movimiento1, 0.0534)
	per.AddAnimSound("Spd_attack_b", Movimiento1, 0.3000)
	per.AddAnimSound("Spd_attack_b", Movimiento1, 0.6500)
	per.AddAnimSound("Spd_attack_b", Movimiento1, 0.9000)
	per.AddAnimSound("Spd_attack_f", Movimiento1, 0.0534)
	per.AddAnimSound("Spd_attack_f", Movimiento1, 0.3000)
	per.AddAnimSound("Spd_attack_f", Movimiento1, 0.6500)
	per.AddAnimSound("Spd_attack_f", Movimiento1, 0.9000)
	
	per.AddAnimSound("Spd_rlx_no", Movimiento3, 0.0534)
	per.AddAnimSound("Spd_rlx_no", Movimiento2, 0.3000)
	per.AddAnimSound("Spd_rlx_no", Movimiento3, 0.6500)
	per.AddAnimSound("Spd_rlx_no", Movimiento2, 0.9000)
	
	# per.AddAnimSound("Spd_rlx_lg", Movimiento3, 0.0534)     # PLAGUE: anim does not exist  
	# per.AddAnimSound("Spd_rlx_lg", Movimiento2, 0.3000)     #
	# per.AddAnimSound("Spd_rlx_lg", Movimiento3, 0.6500)     #
	# per.AddAnimSound("Spd_rlx_lg", Movimiento2, 0.9000)     #
	
	# per.AddAnimSound("Spd_rlx.max", Movimiento1, 0.0534)    # PLAGUE: Wtf is this format?
	# per.AddAnimSound("Spd_rlx.max", Movimiento1, 0.3000)    #
	# per.AddAnimSound("Spd_rlx.max", Movimiento1, 0.6500)    #
	# per.AddAnimSound("Spd_rlx.max", Movimiento1, 0.9000)    #
	
	
	
	



