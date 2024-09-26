##///
##||| ANISOUNDKGT.PY TITANIUM
##||| Change list:
##||| * Added whoosh for Dodge attacks.
##||| * Commented duplicate entries for dodge sounds.
##||| * Reworked Fire Sword special attack sounds.
##||| * Additional whoosh for Sharp Sword speical. 
##||| * g_magic2 whoosh sound timing corrected
##||| * Ice Sword uses special wooshes.
##\\\ 

import Bladex
import NetSounds
import netgame

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************


def AsignarSonidosCaballero(Personaje):
	from AniSoundKgtX import *

	per=Bladex.GetEntity(Personaje)
	
	if netgame.GetNetState() !=2:
		# Sonidos de eventos
	
		per.AddEventSound('shield_block', GolpeArmaEscudo)
		per.AddEventSound('weapon_block', GolpeArmaArma)
		per.AddEventSound('impale', TajoEmpalante)
		per.AddEventSound('slash', TajoCortante)
		per.AddEventSound('mutilate', TajoMutilacion)
		per.AddEventSound('crush', GolpeContundente)



	# Sonidos de animaciones
	NetSounds.AddAnimSound(per,'Kgt_chg_r', Enfundar, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_chg_r', AndarKgt1, 0.3500)
	NetSounds.AddAnimSound(per,'Kgt_chg_l', CambiarEscudo, 0.3652)
	NetSounds.AddAnimSound(per,'Kgt_chg_r_l', Enfundar, 0.3599)
	NetSounds.AddAnimSound(per,'Kgt_chg_r_l', AndarKgt2, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r_l', Enfundar, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r_l', AndarKgt1, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r', Enfundar, 0.5)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r', AndarKgt1, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r', CambiarEscudo, 0.3652)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_l', CambiarEscudo, 0.3652)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key00', CogerArma, 0.5652)
	NetSounds.AddAnimSound(per,'Kgt_chg_l', CambiarEscudo, 0.3652)
	#NetSounds.AddAnimSound(per,'Kgt_the_r_Key00', CogerEspada, 0.3652)

	
	
	
	
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb01', AndarKgt10, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb01', EsfuerzoCortoBarb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb01_l', AndarKgt10, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb01_l', EsfuerzoCortoBarb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb01_r', AndarKgt10, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb01_r', EsfuerzoCortoBarb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb02', AndarKgt10, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb02', EsfuerzoCorto1Barb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb02_l', AndarKgt10, 0.20000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb02_l', EsfuerzoCorto1Barb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb02_r', AndarKgt10, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb02_r', EsfuerzoCorto1Barb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb03_l', AndarKgt10, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb03_l', EsfuerzoCorto1Barb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb03_r', AndarKgt10, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_jog_clmb03_r', EsfuerzoCorto1Barb, 0.1000)

	
	NetSounds.AddAnimSound(per,'Kgt_pour',SonidoVaciarBotella, 0.1234)
	
	NetSounds.AddAnimSound(per,'Wlk_2h_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wlk_2h_Kgt',AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Wbk_2h_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wbk_2h_Kgt',AndarKgt2, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wlk_1h_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wlk_1h_Kgt',AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Wbk_1h_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wbk_1h_Kgt',AndarKgt2, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wlk_no_Kgt',AndarKgt3, 0.0534)
	NetSounds.AddAnimSound(per,'Wlk_no_Kgt',AndarKgt4, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wlk_spear_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wlk_spear_Kgt',AndarKgt2, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wlk_s_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wlk_s_Kgt',AndarKgt2, 0.5000)
	
	
	NetSounds.AddAnimSound(per,'Wlk_2w_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wlk_2w_Kgt',AndarKgt2, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wlk_b_Kgt',AndarKgt1, 0.0534)
	NetSounds.AddAnimSound(per,'Wlk_b_Kgt',AndarKgt2, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wbk_no_Kgt',AndarKgt3, 0.0534)
	NetSounds.AddAnimSound(per,'Wbk_no_Kgt',AndarKgt4, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wbk_b_Kgt',AndarKgt3, 0.0534)
	NetSounds.AddAnimSound(per,'Wbk_b_Kgt',AndarKgt4, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wbk_2w_Kgt',AndarKgt3, 0.0534)
	NetSounds.AddAnimSound(per,'Wbk_2w_Kgt',AndarKgt4, 0.5000)
	
	NetSounds.AddAnimSound(per,'Wbk_spear_Kgt',AndarKgt3, 0.0534)
	NetSounds.AddAnimSound(per,'Wbk_spear_Kgt',AndarKgt4, 0.5000)
	
	NetSounds.AddAnimSound(per,'Jog_1h_Kgt',AndarKgt5, 0.1000)
	NetSounds.AddAnimSound(per,'Jog_1h_Kgt',AndarKgt6, 0.5500)
	#NetSounds.AddAnimSound(per,'Jog_1h_Kgt',AndarKgt5, 0.9000)
	
	NetSounds.AddAnimSound(per,'Jog_no_Kgt',AndarKgt5, 0.0534)
	NetSounds.AddAnimSound(per,'Jog_no_Kgt',AndarKgt6, 0.5000)
	
	NetSounds.AddAnimSound(per,'Jog_2w_Kgt',AndarKgt5, 0.0534)
	NetSounds.AddAnimSound(per,'Jog_2w_Kgt',AndarKgt6, 0.5000)
	
	NetSounds.AddAnimSound(per,'Jog_b_Kgt',AndarKgt5, 0.0534)
	NetSounds.AddAnimSound(per,'Jog_b_Kgt',AndarKgt6, 0.5000)
	
	NetSounds.AddAnimSound(per,'Jog_spear_Kgt',AndarKgt5, 0.0534)
	NetSounds.AddAnimSound(per,'Jog_spear_Kgt',AndarKgt6, 0.5000)
	
	NetSounds.AddAnimSound(per,'Kgt_jogb_no',AndarKgt5, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_no',AndarKgt6, 0.5500)
	
	NetSounds.AddAnimSound(per,'Kgt_jogb_2h',AndarKgt7, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_2h',AndarKgt8, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_2h',AndarKgt9, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_2h',AndarKgt7, 0.7000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_2h',AndarKgt8, 0.9000)
	
	NetSounds.AddAnimSound(per,'Kgt_jogb_1h',AndarKgt7, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_1h',AndarKgt8, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_1h',AndarKgt9, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_1h',AndarKgt7, 0.7000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_1h',AndarKgt8, 0.9000)
	
	NetSounds.AddAnimSound(per,'Kgt_jogb_spear',AndarKgt7, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_spear',AndarKgt8, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_spear',AndarKgt9, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_spear',AndarKgt7, 0.7000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_spear',AndarKgt8, 0.9000)
	
	NetSounds.AddAnimSound(per,'Kgt_jogb_sword',AndarKgt7, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_sword',AndarKgt8, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_sword',AndarKgt9, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_sword',AndarKgt7, 0.7000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_sword',AndarKgt8, 0.9000)
	
	NetSounds.AddAnimSound(per,'Kgt_jogb_s',AndarKgt7, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_s',AndarKgt8, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_s',AndarKgt9, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_s',AndarKgt7, 0.7000)
	NetSounds.AddAnimSound(per,'Kgt_jogb_s',AndarKgt8, 0.9000)
	
	NetSounds.AddAnimSound(per,'Kgt_d_r',EsfuerzoCortoBarb, 0.2100)
	NetSounds.AddAnimSound(per,'Kgt_d_l',EsfuerzoCorto1Barb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_d_b',EsfuerzoCorto2Barb, 0.2990)
	
	NetSounds.AddAnimSound(per,'Kgt_g_d_r',EsfuerzoCortoBarb, 0.2100)
	NetSounds.AddAnimSound(per,"Kgt_g_d_r",SesgadoCortoGrave, 0.4270)   # Added. -LeadHead
	NetSounds.AddAnimSound(per,'Kgt_g_d_l',EsfuerzoCortoBarb, 0.2100)
	NetSounds.AddAnimSound(per,"Kgt_g_d_l",SesgadoCortoGrave, 0.4140)   # Added. -LeadHead
	NetSounds.AddAnimSound(per,'Kgt_g_d_b',EsfuerzoCorto2Barb, 0.2990)
	
	
	
	NetSounds.AddAnimSound(per,"FallHigh_Kgt",CaidaKgt1, 0.1000)
	NetSounds.AddAnimSound(per,"FallHigh_Kgt",CaidaKgt2, 0.1700)
	NetSounds.AddAnimSound(per,"FallHigh_Kgt",SaltoCortoBarbaro2, 0.2000)
	NetSounds.AddAnimSound(per,"FallHigh_Kgt",AndarKgt1, 0.1800)
	NetSounds.AddAnimSound(per,"FallLow_Kgt",CaidaKgt3, 0.1180)
	NetSounds.AddAnimSound(per,"FallLow_Kgt",CaidaKgt4, 0.1300)
	NetSounds.AddAnimSound(per,"FallLow_Kgt",SaltoCortoBarbaro2, 0.1280)
	NetSounds.AddAnimSound(per,"FallLow_Kgt",AndarKgt1, 0.1250)
	NetSounds.AddAnimSound(per,"FallMed_Kgt",CaidaKgt3, 0.1180)
	NetSounds.AddAnimSound(per,"FallMed_Kgt",CaidaKgt4, 0.1300)
	NetSounds.AddAnimSound(per,"FallMed_Kgt",SaltoCortoBarbaro2, 0.1280)
	NetSounds.AddAnimSound(per,"FallMed_Kgt",AndarKgt1, 0.1250)
	
	


######
#	pruebas Armin



#	NetSounds.AddAnimSound(per,'Kgt_b2', SoltarArco, 0.1235)

#		SOLO DE PRUEBA IPTS 

#	NetSounds.AddAnimSound(per,'Kgt_b2', SoltarArco, 0.5412)
#	NetSounds.AddAnimSound(per,'Kgt_b1', TensarArco, 0.0564)
	


# 	PARA LA ANIMACON DEL MAPA DE RAGNAR AL EMPUJAR EL MURO

	NetSounds.AddAnimSound(per,'Kgt_push_wall', EsfuerzoCorto1Barb, 0.1524)
	NetSounds.AddAnimSound(per,'Kgt_push_wall', EsfuerzoBarbLargo, 0.1234)
	NetSounds.AddAnimSound(per,'Kgt_push_wall', EsfuerzoCortoBarb, 0.5214)
	#NetSounds.AddAnimSound(per,'Kgt_push_wall', EsfuerzoGolpeAtras1Barb, 0.5588)
	NetSounds.AddAnimSound(per,'Kgt_push_wall', EsfuerzoCorto1Barb, 0.8000)
	NetSounds.AddAnimSound(per,'Kgt_push_wall', EsfuerzoCortoBarb, 0.7412)







#########################################################################################
#########################################################################################
#########################################################################################



	NetSounds.AddAnimSound(per,"Kgt_dth_n00", MuerteKgt1, 0.1100)
	NetSounds.AddAnimSound(per,"Kgt_dth_n00", AndarKgt1, 0.2000)
	NetSounds.AddAnimSound(per,"Kgt_dth_n00", AndarKgt2, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_n00", AndarKgt1, 0.4000)
	NetSounds.AddAnimSound(per,"Kgt_dth_n00", AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_n00", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_n00", AndarKgt2, 0.7500)
	NetSounds.AddAnimSound(per,"Kgt_dth_n00", CaidaKgt1, 0.7000)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", MuerteKgt2, 0.1100)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", AndarKgt1, 0.2200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", AndarKgt2, 0.3200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", AndarKgt1, 0.4200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", AndarKgt1, 0.5200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", AndarKgt2, 0.6200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", AndarKgt1, 0.7500)
	NetSounds.AddAnimSound(per,"Kgt_dth_n01", CaidaKgt1, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", MuerteKgt3, 0.1200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", AndarKgt1, 0.2200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", AndarKgt1, 0.3200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", AndarKgt2, 0.4200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", AndarKgt1, 0.5200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", AndarKgt1, 0.6200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", AndarKgt2, 0.7500)
	NetSounds.AddAnimSound(per,"Kgt_dth_n02", CaidaKgt1, 0.7000)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", MuerteKgt1, 0.1200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", AndarKgt1, 0.2200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", AndarKgt1, 0.3200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", AndarKgt2, 0.4200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", AndarKgt2, 0.5200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", AndarKgt1, 0.6200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", AndarKgt2, 0.7500)
	NetSounds.AddAnimSound(per,"Kgt_dth_n03", CaidaKgt1, 0.6550)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", MuerteKgt4, 0.1100)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", AndarKgt1, 0.2200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", AndarKgt1, 0.3200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", AndarKgt2, 0.4200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", AndarKgt2, 0.5200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", AndarKgt1, 0.6200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", AndarKgt2, 0.7500)
	NetSounds.AddAnimSound(per,"Kgt_dth_n04", CaidaKgt1, 0.7600)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", MuerteKgt4, 0.1100)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", AndarKgt1, 0.2200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", AndarKgt1, 0.3200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", AndarKgt1, 0.5200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", AndarKgt2, 0.4200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", AndarKgt1, 0.6200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", AndarKgt2, 0.7500)
	NetSounds.AddAnimSound(per,"Kgt_dth_n05", CaidaKgt1, 0.7700)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", MuerteKgt2, 0.1200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", AndarKgt2, 0.2200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", AndarKgt2, 0.3200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", AndarKgt2, 0.5200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", AndarKgt1, 0.4200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", AndarKgt2, 0.6200)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", AndarKgt1, 0.7500)
	NetSounds.AddAnimSound(per,"Kgt_dth_n06", CaidaKgt1, 0.6900)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", DesangreKgt2, 0.1250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt1, 0.2250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt1, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt2, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", AndarKgt1, 0.7200)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", CaidaKgt1, 0.7800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c1", DesangreKgt1, 0.2500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", DesangreKgt2, 0.1250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", DesangreKgt1, 0.2500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt1, 0.2250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt2, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", AndarKgt1, 0.7200)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", CaidaKgt1, 0.7720)
	NetSounds.AddAnimSound(per,"Kgt_dth_c2", CaidaKgt2, 0.8720)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", DesangreKgt1, 0.1250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", DesangreKgt2, 0.2500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt1, 0.2250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt2, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", AndarKgt1, 0.7200)
	NetSounds.AddAnimSound(per,"Kgt_dth_c3", CaidaKgt1, 0.7220)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", DesangreKgt1, 0.1250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", DesangreKgt2, 0.2500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", AndarKgt1, 0.2250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", AndarKgt2, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", CaidaKgt1, 0.7000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c4", CaidaKgt2, 0.8720)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", DesangreKgt1, 0.1250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", DesangreKgt2, 0.2500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt1, 0.2250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt2, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", AndarKgt1, 0.7200)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", CaidaKgt1, 0.7720)
	NetSounds.AddAnimSound(per,"Kgt_dth_c5", CaidaKgt2, 0.5500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", DesangreKgt1, 0.1250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", DesangreKgt2, 0.2500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt1, 0.2250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt2, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", AndarKgt1, 0.7200)
	NetSounds.AddAnimSound(per,"Kgt_dth_c6", CaidaKgt1, 0.7700)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", DesangreKgt1, 0.1250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", DesangreKgt2, 0.2500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt1, 0.2250)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt1, 0.6000)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt2, 0.6800)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", AndarKgt1, 0.7200)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", CaidaKgt1, 0.6300)
	NetSounds.AddAnimSound(per,"Kgt_dth_c7", CaidaKgt2, 0.6900)
	NetSounds.AddAnimSound(per,"Kgt_dth0", MuerteKgt2, 0.1100)
	NetSounds.AddAnimSound(per,"Kgt_dth0", CaidaKgt1, 0.5710)
	NetSounds.AddAnimSound(per,"Kgt_dth0", CaidaKgt2, 0.7700)
	NetSounds.AddAnimSound(per,"Kgt_dth0", MuerteKgt1, 0.1100)
	NetSounds.AddAnimSound(per,"Kgt_dth0", AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,"Kgt_dth0", AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,"Kgt_dth0", AndarKgt1, 0.6800)
	
	
	NetSounds.AddAnimSound(per,"Kgt_dth_burn", MuerteQuemado, 0.1100)
	
	NetSounds.AddAnimSound(per,"Dth_Fll2_Kgt", MuerteSaltoVacioKgt2, 0.1900)
	NetSounds.AddAnimSound(per,"Dth_Fll2_Kgt", CaidaKgt1, 0.1100)
	
	NetSounds.AddAnimSound(per,"Dth_Fll_Kgt", MuerteSaltoVacioKgt1, 0.1000)
	
	NetSounds.AddAnimSound(per,"Kgt_dth_rockfront", MuerteAplastamientoKgt1, 0.1000)
	NetSounds.AddAnimSound(per,"Kgt_dth_rockfront", HeridaKgt1, 0.1000)
	
	NetSounds.AddAnimSound(per,"Kgt_dth_rock", HeridaKgt1, 0.1100)
	NetSounds.AddAnimSound(per,"Kgt_dth_rock", MuerteAplastamientoKgt1, 0.1100)





	NetSounds.AddAnimSound(per,'Kgt_clmb_low_1h', EsfuerzosubirKgt, 0.4770)
	NetSounds.AddAnimSound(per,'Kgt_clmb_low_1h', AndarKgt10, 0.4870)
	NetSounds.AddAnimSound(per,'Kgt_clmb_medlow_1h', EsfuerzosubirKgt, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_clmb_medlow_1h', AndarKgt10, 0.2400)
	NetSounds.AddAnimSound(per,'Kgt_clmb_medium_1h', EsfuerzosubirKgt2, 0.1200)
	NetSounds.AddAnimSound(per,'Kgt_clmb_medium_1h', EsfuerzosubirKgt1, 0.6500)
	NetSounds.AddAnimSound(per,'Kgt_clmb_medium_1h', AndarKgt10, 0.1320)
	NetSounds.AddAnimSound(per,'Kgt_clmb_medium_1h', AndarKgt11, 0.5950)
	NetSounds.AddAnimSound(per,'Kgt_clmb_high_1h', EsfuerzosubirKgt2, 0.1200)
	NetSounds.AddAnimSound(per,'Kgt_clmb_high_1h', EsfuerzosubirKgt1, 0.7862)
	NetSounds.AddAnimSound(per,'Kgt_clmb_high_1h', AndarKgt10, 0.3700)
	NetSounds.AddAnimSound(per,'Kgt_clmb_high_1h', AndarKgt11, 0.6550)


	NetSounds.AddAnimSound(per,'Kgt_jmph0_no', EsfuerzosubirKgt, 0.4150)
	NetSounds.AddAnimSound(per,'Kgt_jmp_no', SaltoCortoBarbaro6, 0.0700)
	NetSounds.AddAnimSound(per,'Kgt_jmp_no', SaltoCortoBarbaro5, 0.3800)
	NetSounds.AddAnimSound(per,'Kgt_jmp_1h', SaltoCortoBarbaro, 0.1000)
	#NetSounds.AddAnimSound(per,'Kgt_jmp_1h', SaltoCortoBarbaro2, 0.3800)
	
	
	
	NetSounds.AddAnimSound(per,'Kgt_derrape', SaltoCortoBarbaro4, 0.2500)
	NetSounds.AddAnimSound(per,'Kgt_derrape', AndarKgt2, 0.3800)
	NetSounds.AddAnimSound(per,'Kgt_slip', ResbalaKgt1, 0.1300)


	NetSounds.AddAnimSound(per,'Kgt_g_draw_run', Enfundar, 0.1300)
	NetSounds.AddAnimSound(per,'Kgt_g_draw_run', EsfuerzoGolpeLateralBarb, 0.2200)
	NetSounds.AddAnimSound(per,'Kgt_g_draw_run', SesgadoLargoAgudo, 0.2500)
	
	NetSounds.AddAnimSound(per,'Kgt_g_draw_rlx', Enfundar, 0.1300)
	NetSounds.AddAnimSound(per,'Kgt_g_draw_rlx', EsfuerzoGolpeLateralBarb, 0.1300)
	NetSounds.AddAnimSound(per,'Kgt_g_draw_rlx', SesgadoLargoAgudo, 0.3470)
	
	#NetSounds.AddAnimSound(per,'Kgt_g_01low_new', SesgadoLargoAgudo, 0.1950)
	#NetSounds.AddAnimSound(per,'Kgt_g_01low_new', AndarKgt1, 0.4200)
	#NetSounds.AddAnimSound(per,'Kgt_g_01low_new', SesgadoCortoAgudo, 0.3950)
	#NetSounds.AddAnimSound(per,'Kgt_g_01low_new', EsfuerzoGolpeArribaBarb, 0.1750)
	
	NetSounds.AddAnimSound(per,'Kgt_g_back', SesgadoCortoAgudo, 0.1200)
	NetSounds.AddAnimSound(per,'Kgt_g_back', EsfuerzoCorto1Barb, 0.1200)
	NetSounds.AddAnimSound(per,'Kgt_g_back', AndarKgt2, 0.1500)
	NetSounds.AddAnimSound(per,'Kgt_g_back', EsfuerzoCorto2Barb, 0.3800)
	NetSounds.AddAnimSound(per,'Kgt_g_back', SesgadoLargoAgudo, 0.3800)
	
	NetSounds.AddAnimSound(per,'Kgt_g_s3_new', SesgadoLargoAgudo, 0.2860)
	NetSounds.AddAnimSound(per,'Kgt_g_s3_new', EsfuerzoGolpeArribaBarb, 0.2225)
	NetSounds.AddAnimSound(per,'Kgt_g_s3_new', AndarKgt1, 0.3200)
	
	NetSounds.AddAnimSound(per,'Kgt_g_02_new', SesgadoCorto, 0.2950)
	NetSounds.AddAnimSound(per,'Kgt_g_02_new', EsfuerzoCorto1Barb, 0.1750)
	NetSounds.AddAnimSound(per,'Kgt_g_02_new', AndarKgt1, 0.3600)
	
	NetSounds.AddAnimSound(per,'Kgt_g_19_bs1_new', SesgadoLargoAgudo, 0.2650)
	NetSounds.AddAnimSound(per,'Kgt_g_19_bs1_new', SesgadoCorto, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_g_19_bs1_new', EsfuerzoGolpeArribaBarb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_g_19_bs1_new', EsfuerzoCorto6Barb, 0.4810)
	NetSounds.AddAnimSound(per,'Kgt_g_19_bs1_new', AndarKgt1, 0.5000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_22lowkata_new', SesgadoLargoAgudo, 0.1320)
	NetSounds.AddAnimSound(per,'Kgt_g_22lowkata_new', SesgadoLargo, 0.3570)
	NetSounds.AddAnimSound(per,'Kgt_g_22lowkata_new', EsfuerzoGolpeLateralBarb, 0.1200)
	NetSounds.AddAnimSound(per,'Kgt_g_22lowkata_new', AndarKgt1, 0.4000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_01_7_new', SesgadoLargo, 0.2950)
	NetSounds.AddAnimSound(per,'Kgt_g_01_7_new', SesgadoLargoAgudo, 0.2950)
	NetSounds.AddAnimSound(per,'Kgt_g_01_7_new', EsfuerzoCorto6Barb, 0.2950)
	NetSounds.AddAnimSound(per,'Kgt_g_01_7_new', AndarKgt2, 0.3400)
	
	NetSounds.AddAnimSound(per,'Kgt_g_3s9_6new', SesgadoCorto, 0.2650)
	NetSounds.AddAnimSound(per,'Kgt_g_3s9_6new', EsfuerzoCorto2Barb, 0.2650)
	NetSounds.AddAnimSound(per,'Kgt_g_3s9_6new', SesgadoLargoAgudo, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_g_3s9_6new', AndarKgt2, 0.3400)
	NetSounds.AddAnimSound(per,'Kgt_g_3s9_6new', AndarKgt2, 0.8000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_b06_new', SesgadoLargoAgudo, 0.1650)
	NetSounds.AddAnimSound(per,'Kgt_g_b06_new',EsfuerzoGolpeLateralBarb, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_g_b06_new', SesgadoCortoAgudo, 0.4950)
	NetSounds.AddAnimSound(per,'Kgt_g_b06_new', AndarKgt2, 0.5300)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_28new', SesgadoEspecialLargo2, 0.345)
	NetSounds.AddAnimSound(per,'Kgt_g_28new', EsfuerzoGolpeAtrasBarb, 0.325)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low', SesgadoCortoAgudo, 0.2233)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low', EsfuerzoCorto2Barb, 0.2230)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low', EsfuerzoGolpeLateralDchBarb, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low', SesgadoCortoGrave, 0.6620)
	
	NetSounds.AddAnimSound(per,'Kgt_g_18_11_22_new', SesgadoEspecialCorto2, 0.147)
	NetSounds.AddAnimSound(per,'Kgt_g_18_11_22_new', SesgadoEspecialCorto2, 0.366)
	NetSounds.AddAnimSound(per,'Kgt_g_18_11_22_new', SesgadoEspecialLargo1, 0.630)
	NetSounds.AddAnimSound(per,'Kgt_g_18_11_22_new', EsfuerzoGolpeAtrasBarb, 0.137)
	NetSounds.AddAnimSound(per,'Kgt_g_18_11_22_new', EsfuerzoGolpeAtras1Barb, 0.346)
	NetSounds.AddAnimSound(per,'Kgt_g_18_11_22_new', EsfuerzoBarbMediano, 0.570)
	NetSounds.AddAnimSound(per,'Kgt_g_18_11_22_new', AndarKgt2, 0.600)
	
	NetSounds.AddAnimSound(per,'Kgt_g_29_3new', EsfuerzoGolpeAtrasBarb, 0.390)
	NetSounds.AddAnimSound(per,'Kgt_g_29_3new', SesgadoEspecialLargo1, 0.400)
	NetSounds.AddAnimSound(per,'Kgt_g_29_3new', SesgadoEspecialCorto2, 0.173)
	
	NetSounds.AddAnimSound(per,'Kgt_g_06lowkata_new', SesgadoCorto, 0.2270)
	NetSounds.AddAnimSound(per,'Kgt_g_06lowkata_new', SesgadoCortoAgudo, 0.4750)
	NetSounds.AddAnimSound(per,'Kgt_g_06lowkata_new', SesgadoCorto, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_g_06lowkata_new', EsfuerzoCorto2Barb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_g_06lowkata_new', EsfuerzoCorto2Barb, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_g_06lowkata_new', EsfuerzoCorto3Barb, 0.4750)
	NetSounds.AddAnimSound(per,'Kgt_g_06lowkata_new', AndarKgt2, 0.5000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', EsfuerzoCorto1Barb, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', EsfuerzoCorto2Barb, 0.2000)
	# NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', SesgadoCorto, 0.1000)
	# NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', SesgadoCortoAgudo, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', EsfuerzoGolpeLateralBarb, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', SesgadoEspecialCorto2, 0.1000	# Heavier woosh sound
	NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', SesgadoEspecialCorto1, 0.2000)	# IceSword
	NetSounds.AddAnimSound(per,'Kgt_g_12_7_s1new', SesgadoEspecialLargo2, 0.4900)	#		-LeadHead

	
	NetSounds.AddAnimSound(per,'Kgt_g_21_6_s8new', EsfuerzoGolpeAtras1Barb, 0.170)
	NetSounds.AddAnimSound(per,'Kgt_g_21_6_s8new', EsfuerzoGolpeAtrasBarb, 0.310)
	NetSounds.AddAnimSound(per,'Kgt_g_21_6_s8new', EsfuerzoBarbMediano, 0.550)
	NetSounds.AddAnimSound(per,'Kgt_g_21_6_s8new', SesgadoEspecialCorto2, 0.176)
	NetSounds.AddAnimSound(per,'Kgt_g_21_6_s8new', SesgadoEspecialCorto2, 0.315)
	NetSounds.AddAnimSound(per,'Kgt_g_21_6_s8new', AndarKgt2, 0.530)
	NetSounds.AddAnimSound(per,'Kgt_g_21_6_s8new', SesgadoEspecialLargo1, 0.562)
	
	NetSounds.AddAnimSound(per,'Kgt_g_32_5_3new', EsfuerzoBarbMediano, 0.185)
	NetSounds.AddAnimSound(per,'Kgt_g_32_5_3new', SesgadoEspecialCorto2, 0.186)
	NetSounds.AddAnimSound(per,'Kgt_g_32_5_3new', EsfuerzoGolpeAtrasBarb, 0.274)
	NetSounds.AddAnimSound(per,'Kgt_g_32_5_3new', SesgadoEspecialLargo1, 0.294)
	NetSounds.AddAnimSound(per,'Kgt_g_32_5_3new', AndarKgt2, 0.700)
	NetSounds.AddAnimSound(per,'Kgt_g_32_5_3new', EsfuerzoGolpeAtras1Barb, 0.508)
	NetSounds.AddAnimSound(per,'Kgt_g_32_5_3new', SesgadoEspecialLargo2, 0.518)
	
	#NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', SesgadoLargoAgudo, 0.2640)
	#NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', SesgadoCortoAgudo, 0.5550)
	#NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', EsfuerzoCorto4Barb, 0.2120)
	#NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', AndarKgt1, 0.6000)
	###
	#Firesword special, replaced all with new ones -LeadHead
	###
	NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', SesgadoCortoAgudo, 0.1240)
	NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', SesgadoEspecialLargo1, 0.2850)
	NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', SesgadoEspecialLargo2, 0.5050)
	NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', AndarKgt1, 0.6500)
	NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', EsfuerzoCorto4Barb, 0.1620)
	NetSounds.AddAnimSound(per,'Kgt_g_s28kata_new', EsfuerzoBarbMediano, 0.5780)
	
	
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_01', EsfuerzoCorto6Barb, 0.3117)
	NetSounds.AddAnimSound(per,'Kgt_g_01', AndarKgt1, 0.3500)
	NetSounds.AddAnimSound(per,'Kgt_g_01', SesgadoCorto, 0.3117)
	
	NetSounds.AddAnimSound(per,'Kgt_g_08', EsfuerzoCorto2Barb, 0.4030)
	NetSounds.AddAnimSound(per,'Kgt_g_08', AndarKgt1, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_g_08', SesgadoCortoGrave, 0.4030)
	
	NetSounds.AddAnimSound(per,'Kgt_g_09', EsfuerzoCorto6Barb, 0.3291)
	NetSounds.AddAnimSound(per,'Kgt_g_09', AndarKgt2, 0.3600)
	NetSounds.AddAnimSound(per,'Kgt_g_09', SesgadoCorto, 0.3291)
	
	NetSounds.AddAnimSound(per,'Kgt_g_02', EsfuerzoCorto5Barb, 0.3026)
	NetSounds.AddAnimSound(per,'Kgt_g_02', AndarKgt2, 0.3500)
	NetSounds.AddAnimSound(per,'Kgt_g_02', SesgadoCortoAgudo, 0.3026)
	
	NetSounds.AddAnimSound(per,'Kgt_g_07', EsfuerzoCorto4Barb, 0.3291)
	NetSounds.AddAnimSound(per,'Kgt_g_07', AndarKgt2, 0.3600)
	NetSounds.AddAnimSound(per,'Kgt_g_07', SesgadoCortoAgudo, 0.3291)
	
	NetSounds.AddAnimSound(per,'Kgt_g_06', EsfuerzoCorto3Barb, 0.3500)
	NetSounds.AddAnimSound(per,'Kgt_g_06', AndarKgt2, 0.4700)
	NetSounds.AddAnimSound(per,'Kgt_g_06', SesgadoCorto, 0.4342)
	
	NetSounds.AddAnimSound(per,'Kgt_g_05', EsfuerzoCorto2Barb, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_g_05', AndarKgt1, 0.5500)
	NetSounds.AddAnimSound(per,'Kgt_g_05', SesgadoCortoGrave, 0.5000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_11', EsfuerzoGolpeFrontalBarb, 0.2252)
	NetSounds.AddAnimSound(per,'Kgt_g_11', AndarKgt1, 0.2600)
	NetSounds.AddAnimSound(per,'Kgt_g_11', SesgadoLargo, 0.4685)
	
	NetSounds.AddAnimSound(per,'Kgt_g_12', EsfuerzoGolpeFrontalBarb, 0.5954)
	NetSounds.AddAnimSound(per,'Kgt_g_12', AndarKgt2, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_g_12', SesgadoLargo, 0.5954)
	
	NetSounds.AddAnimSound(per,'Kgt_g_13', EsfuerzoGolpeFrontalBarb, 0.3053)
	NetSounds.AddAnimSound(per,'Kgt_g_13', AndarKgt1, 0.3500)
	NetSounds.AddAnimSound(per,'Kgt_g_13', SesgadoLargoAgudo, 0.3053)
	
	NetSounds.AddAnimSound(per,'Kgt_g_14', EsfuerzoGolpeLateralBarb, 0.3969)
	NetSounds.AddAnimSound(per,'Kgt_g_14', AndarKgt2, 0.4300)
	NetSounds.AddAnimSound(per,'Kgt_g_14', SesgadoLargoGrave, 0.3969)
	
	NetSounds.AddAnimSound(per,'Kgt_g_15', EsfuerzoGolpeLateralBarb, 0.4628)  #no se si se usa
	NetSounds.AddAnimSound(per,'Kgt_g_15', AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_g_15', SesgadoLargo, 0.4628)
	
	NetSounds.AddAnimSound(per,'Kgt_g_16', EsfuerzoGolpeLateralBarb, 0.3200)
	NetSounds.AddAnimSound(per,'Kgt_g_16', AndarKgt1, 0.3400)
	NetSounds.AddAnimSound(per,'Kgt_g_16', SesgadoLargoAgudo, 0.4681)
	
	NetSounds.AddAnimSound(per,'Kgt_g_17', EsfuerzoGolpeLateralBarb, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_g_17', AndarKgt2, 0.4600)
	NetSounds.AddAnimSound(per,'Kgt_g_17', SesgadoLargoAgudo, 0.4427)
	
	NetSounds.AddAnimSound(per,'Kgt_g_18', EsfuerzoGolpeArribaBarb, 0.4224)
	NetSounds.AddAnimSound(per,'Kgt_g_18', AndarKgt1, 0.4600)
	NetSounds.AddAnimSound(per,'Kgt_g_18', SesgadoLargoGrave, 0.4224)
	
	NetSounds.AddAnimSound(per,'Kgt_g_21', EsfuerzoGolpeArribaBarb, 0.2500)
	NetSounds.AddAnimSound(per,'Kgt_g_21', AndarKgt1, 0.4600)
	NetSounds.AddAnimSound(per,'Kgt_g_21', SesgadoLargoGrave, 0.5410)
	
	NetSounds.AddAnimSound(per,'Kgt_g_22', EsfuerzoGolpeAtrasBarb, 0.4698)
	NetSounds.AddAnimSound(per,'Kgt_g_22', SesgadoLargo, 0.4698)
	NetSounds.AddAnimSound(per,'Kgt_g_22', AndarKgt1, 0.2000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_23', EsfuerzoGolpeArribaBarb, 0.2500)
	NetSounds.AddAnimSound(per,'Kgt_g_23', SesgadoLargo, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_g_23', AndarKgt1, 0.3000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_26', EsfuerzoGolpeCabezaBarb, 0.2200)
	NetSounds.AddAnimSound(per,'Kgt_g_26', SesgadoLargoAgudo, 0.4000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_27', EsfuerzoGolpeArribaBarb, 0.3800)
	NetSounds.AddAnimSound(per,'Kgt_g_27', SesgadoLargoAgudo, 0.6210)
	NetSounds.AddAnimSound(per,'Kgt_g_27', SesgadoLargoGrave, 0.8100)
	
	NetSounds.AddAnimSound(per,'Kgt_g_31', EsfuerzoGolpeAtrasBarb, 0.2950)
	NetSounds.AddAnimSound(per,'Kgt_g_31', EsfuerzoCorto6Barb, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_g_31', SesgadoLargo, 0.2950)
	NetSounds.AddAnimSound(per,'Kgt_g_31', SesgadoLargoAgudo, 0.4100)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_punch1', EsfuerzoCorto3Barb, 0.3250)
	NetSounds.AddAnimSound(per,'Kgt_g_punch1', SesgadoCorto, 0.3290)
	NetSounds.AddAnimSound(per,'Kgt_g_punch2', EsfuerzoCorto2Barb, 0.3150)
	NetSounds.AddAnimSound(per,'Kgt_g_punch2', SesgadoCorto, 0.3240)
	NetSounds.AddAnimSound(per,'Kgt_g_punch4', EsfuerzoCorto2Barb, 0.3150)
	NetSounds.AddAnimSound(per,'Kgt_g_punch4', SesgadoCorto, 0.3240)
	
	NetSounds.AddAnimSound(per,'Kgt_g_bad_axe', SesgadoLento, 0.4140)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_axe', EsfuerzoGolpeCabezaBarb, 0.3350)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_axe', AndarKgt2, 0.4300)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_bad_1h', SesgadoLento, 0.3060)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_1h', EsfuerzoPesadoKgt, 0.1100)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_1h', AndarKgt2, 0.4300)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_1h', AndarKgt1, 0.7000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_bad_no', SesgadoCorto, 0.3060)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_no', EsfuerzoPesadoKgt, 0.1100)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_no', AndarKgt2, 0.4300)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_no', AndarKgt1, 0.7000)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_bad_spear2', SesgadoLargo, 0.4520)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_spear2', EsfuerzoGolpeCabezaBarb, 0.3350)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_spear2', AndarKgt2, 0.4700)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_spear', SesgadoLento, 0.2820)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_spear', EsfuerzoGolpeAtrasBarb, 0.2360)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_spear', AndarKgt1, 0.3000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword', SesgadoLento, 0.2900)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword', EsfuerzoPesadoKgt, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword', AndarKgt1, 0.3200)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword2', SesgadoLento, 0.4300)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword2', EsfuerzoPesadoKgt1, 0.2400)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword2', AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword3', SesgadoLento, 0.3970)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword3', EsfuerzoPesadoKgt2, 0.1200)
	NetSounds.AddAnimSound(per,'Kgt_g_bad_sword3', AndarKgt1, 0.4200)
	
	NetSounds.AddAnimSound(per,'Kgt_g_magic', ConcBladeSword1, 0.1300)
	NetSounds.AddAnimSound(per,'Kgt_g_magic', EsfuerzoGolpeLateralDchBarb, 0.3700)
	NetSounds.AddAnimSound(per,'Kgt_g_magic', SesgadoLargoGrave, 0.5530)
	
	NetSounds.AddAnimSound(per,'Kgt_g_magic2', ConcBladeSword2, 0.1000)
	NetSounds.AddAnimSound(per,'Kgt_g_magic2', EsfuerzoBarbMediano, 0.3250)
	NetSounds.AddAnimSound(per,'Kgt_g_magic2', SesgadoLargoGrave, 0.5530)   # 0.5530 -LeadHead
	
	
	# NetSounds.AddAnimSound(per,'Kgt_d_r',EsfuerzoCortoBarb, 0.2100)
	# NetSounds.AddAnimSound(per,'Kgt_d_l',EsfuerzoCorto1Barb, 0.3770)
	# NetSounds.AddAnimSound(per,'Kgt_d_b',EsfuerzoCorto2Barb, 0.2990)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_08_new',SesgadoCorto, 0.2100)
	NetSounds.AddAnimSound(per,'Kgt_g_08_new',EsfuerzoCorto1Barb, 0.2050)
	NetSounds.AddAnimSound(per,'Kgt_g_08_new',AndarKgt1, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_g_08_new',AndarKgt2, 0.8000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_07_new',SesgadoCortoAgudo, 0.2800)
	NetSounds.AddAnimSound(per,'Kgt_g_07_new',EsfuerzoCorto2Barb, 0.2900)
	NetSounds.AddAnimSound(per,'Kgt_g_07_new',AndarKgt1, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_g_07_new',AndarKgt2, 0.8000)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_12_new',SesgadoCortoGrave, 0.3150)
	NetSounds.AddAnimSound(per,'Kgt_g_12_new',EsfuerzoGolpeLateralDchBarb, 0.1100)
	NetSounds.AddAnimSound(per,'Kgt_g_12_new',AndarKgt1, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_g_12_new',AndarKgt2, 0.8000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_sb25_new',SesgadoEspecialLargo2, 0.472)
	NetSounds.AddAnimSound(per,'Kgt_g_sb25_new',EsfuerzoGolpeAtras1Barb, 0.459)
	NetSounds.AddAnimSound(per,'Kgt_g_sb25_new',EsfuerzoCorto2Barb, 0.245)
	NetSounds.AddAnimSound(per,'Kgt_g_sb25_new',AndarKgt1, 0.400)
	
	NetSounds.AddAnimSound(per,'Kgt_g_b32kata_new',SesgadoEspecialCorto2, 0.274)
	NetSounds.AddAnimSound(per,'Kgt_g_b32kata_new',EsfuerzoCorto2Barb, 0.264)
	NetSounds.AddAnimSound(per,'Kgt_g_b32kata_new',EsfuerzoGolpeAtras1Barb, 0.536)
	NetSounds.AddAnimSound(per,'Kgt_g_b32kata_new',SesgadoEspecialLargo1, 0.556)
	NetSounds.AddAnimSound(per,'Kgt_g_b32kata_new',AndarKgt1, 0.400)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_01low_new',SesgadoLargoAgudo, 0.3200)
	NetSounds.AddAnimSound(per,'Kgt_g_01low_new',EsfuerzoCorto2Barb, 0.3150)
	NetSounds.AddAnimSound(per,'Kgt_g_01low_new',AndarKgt1, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_g_01low_new',AndarKgt2, 0.8000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_01_new',SesgadoEspecialLargo1, 0.201)
	NetSounds.AddAnimSound(per,'Kgt_g_01_new',EsfuerzoGolpeAtras1Barb, 0.190)
	NetSounds.AddAnimSound(per,'Kgt_g_01_new',AndarKgt1, 0.4000)
	
	NetSounds.AddAnimSound(per,'Kgt_g_s18_new',SesgadoLargo, 0.3450)
	NetSounds.AddAnimSound(per,'Kgt_g_s18_new',EsfuerzoCorto3Barb, 0.2200)
	NetSounds.AddAnimSound(per,'Kgt_g_s18_new',AndarKgt1, 0.6000)
	
	
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_s22low_new',SesgadoEspecialLargo2, 0.340)
	NetSounds.AddAnimSound(per,'Kgt_g_s22low_new',EsfuerzoBarbMediano, 0.320)
	NetSounds.AddAnimSound(per,'Kgt_g_s22low_new',AndarKgt1, 0.400)
	
	NetSounds.AddAnimSound(per,'Kgt_g_s19_new',SesgadoEspecialLargo1, 0.543)
	NetSounds.AddAnimSound(per,'Kgt_g_s19_new',EsfuerzoGolpeAtras1Barb, 0.523)
	NetSounds.AddAnimSound(per,'Kgt_g_s19_new',AndarKgt1, 0.400)
	
	
	NetSounds.AddAnimSound(per,'Kgt_g_27kata_new',SesgadoEspecialCorto1, 0.110)
	NetSounds.AddAnimSound(per,'Kgt_g_27kata_new',EsfuerzoCorto6Barb, 0.110)
	NetSounds.AddAnimSound(per,'Kgt_g_27kata_new',SesgadoEspecialCorto2, 0.245)
	NetSounds.AddAnimSound(per,'Kgt_g_27kata_new',SesgadoEspecialLargo2, 0.427)
	NetSounds.AddAnimSound(per,'Kgt_g_27kata_new',EsfuerzoBarbMediano, 0.400)
	NetSounds.AddAnimSound(per,'Kgt_g_27kata_new',AndarKgt2, 0.800)
	
	NetSounds.AddAnimSound(per,'Kgt_g_26low_new',SesgadoCortoAgudo, 0.4100)
	NetSounds.AddAnimSound(per,'Kgt_g_26low_new',AndarKgt2, 0.6090)
	NetSounds.AddAnimSound(per,'Kgt_g_26low_new',EsfuerzoGolpeArribaBarb, 0.1300)
	
	NetSounds.AddAnimSound(per,'Kgt_g_22kata_23_new',SesgadoCortoAgudo, 0.258)
	NetSounds.AddAnimSound(per,'Kgt_g_22kata_23_new',SesgadoEspecialLargo2, 0.559)
	NetSounds.AddAnimSound(per,'Kgt_g_22kata_23_new',EsfuerzoCortoBarb, 0.240)
	NetSounds.AddAnimSound(per,'Kgt_g_22kata_23_new',EsfuerzoBarbMediano, 0.500)
	NetSounds.AddAnimSound(per,'Kgt_g_22kata_23_new',AndarKgt1, 0.400)
	
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',SesgadoEspecialCorto1, 0.093)	    # Added -LeadHead
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',SesgadoEspecialCorto2, 0.223)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',SesgadoEspecialLargo1, 0.646)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',EsfuerzoGolpeAtras1Barb, 0.646)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',EsfuerzoCortoBarb, 0.100)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',EsfuerzoGolpeAtrasBarb, 0.213)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',AndarKgt1, 0.300)
	NetSounds.AddAnimSound(per,'Kgt_g_09_07_s6low_new',AndarKgt2, 0.400)
	
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',SesgadoCortoAgudo, 0.1320)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',SesgadoCorto, 0.2610)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',SesgadoCortoGrave, 0.6050)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',EsfuerzoCorto2Barb, 0.1300)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',EsfuerzoCorto3Barb, 0.2200)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',EsfuerzoGolpeCabezaBarb, 0.4580)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',AndarKgt1, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',AndarKgt2, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_g_07_01_19_26low_new',AndarKgt2, 0.7000)
	
	
	NetSounds.AddAnimSound(per,'Kgt_1tw_h_f',AndarKgt2, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_1tw_h_f',EsfuerzoBarbMediano, 0.3000)
	
	NetSounds.AddAnimSound(per,'Kgt_1tw_l_f',AndarKgt2, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_1tw_l_f',EsfuerzoCorto2Barb, 0.3000)
	
	NetSounds.AddAnimSound(per,'Kgt_jog_turn',AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_jog_turn',EsfuerzosubirKgt2, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_wlk_turn',AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_wlk_turn',EsfuerzofinalsubirKgt, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_snk_turn',AndarKgt2, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_rlx_turn',AndarKgt2, 0.4500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_f_s',AndarKgt2, 0.9000)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_s',EsfuerzofinalsubirKgt, 0.8000)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_s',EsfuerzofinalsubirKgt, 0.3800)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_s',AndarKgt1, 0.3600)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_s',AndarKgt2, 0.9000)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_s',EsfuerzofinalsubirKgt, 0.8000)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_s',EsfuerzofinalsubirKgt, 0.3800)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_s',AndarKgt1, 0.3600)
	

	
	NetSounds.AddAnimSound(per,'Snk_b_Kgt',AndarKgt1, 0.0540)
	NetSounds.AddAnimSound(per,'Snk_b_Kgt',AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Snk_1h_Kgt',AndarKgt1, 0.0540)
	NetSounds.AddAnimSound(per,'Snk_1h_Kgt',AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Snk_spear_Kgt',AndarKgt1, 0.0540)
	NetSounds.AddAnimSound(per,'Snk_spear_Kgt',AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Snk_2w_Kgt',AndarKgt1, 0.0540)
	NetSounds.AddAnimSound(per,'Snk_2w_Kgt',AndarKgt2, 0.5000)
	NetSounds.AddAnimSound(per,'Snk_no_Kgt',AndarKgt1, 0.0540)
	NetSounds.AddAnimSound(per,'Snk_no_Kgt',AndarKgt2, 0.5000)
	
	
	NetSounds.AddAnimSound(per,'Kgt_attack_b_spear', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_spear', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_spear', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_spear', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_spear', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_f_spear', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_spear', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_spear', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_spear', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_spear', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_l_spear', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_spear', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_spear', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_spear', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_spear', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_r_spear', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_spear', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_spear', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_spear', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_spear', AndarKgt7, 0.8500)
	
	
	NetSounds.AddAnimSound(per,'Kgt_attack_b_sword', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_sword', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_sword', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_sword', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_b_sword', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_f_sword', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_sword', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_sword', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_sword', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_f_sword', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_l_sword', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_sword', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_sword', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_sword', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_l_sword', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_r_sword', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_sword', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_sword', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_sword', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_r_sword', AndarKgt7, 0.8500)
	
	
	NetSounds.AddAnimSound(per,'Kgt_attack_b', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_b', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_b', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_b', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_b', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_f', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_f', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_f', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_f', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_f', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_l', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_l', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_l', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_l', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_l', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_r', AndarKgt7, 0.0534)
	NetSounds.AddAnimSound(per,'Kgt_attack_r', AndarKgt8, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_attack_r', AndarKgt7, 0.4200)
	NetSounds.AddAnimSound(per,'Kgt_attack_r', AndarKgt8, 0.6200)
	NetSounds.AddAnimSound(per,'Kgt_attack_r', AndarKgt7, 0.8500)
	
	NetSounds.AddAnimSound(per,'Kgt_parryspear', SaltoCortoBarbaro6, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_parryspear', AndarKgt7, 0.6000)
	
	NetSounds.AddAnimSound(per,'Kgt_parry2w', SaltoCortoBarbaro6, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_parry2w', AndarKgt7, 0.5000)
	
	NetSounds.AddAnimSound(per,'Kgt_df_01', SaltoCortoBarbaro6, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_df_01', AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_df_02', SaltoCortoBarbaro6, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_df_02', AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_df_s_broken', SaltoCortoBarbaro6, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_df_s_broken', AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_df_01_spear', SaltoCortoBarbaro6, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_df_01_spear', AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_df_02_spear', SaltoCortoBarbaro6, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_df_02_spear', AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_df_01_2w', SaltoCortoBarbaro6, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_df_01_2w', AndarKgt1, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_df_02_2w', SaltoCortoBarbaro6, 0.4000)
	NetSounds.AddAnimSound(per,'Kgt_df_02_2w', AndarKgt1, 0.5000)
	
	NetSounds.AddAnimSound(per,'Kgt_hurt_jog', HeridaKgt1, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_hurt_neck', HeridaKgt3, 0.3158)
	NetSounds.AddAnimSound(per,'Kgt_hurt_breast', HeridaKgt1, 0.3889)
	NetSounds.AddAnimSound(per,'Kgt_hurt_back', HeridaKgt3, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_hurt_r_arm', HeridaKgt1, 0.4076)
	NetSounds.AddAnimSound(per,'Kgt_hurt_l_arm', HeridaKgt3, 0.5333)
	NetSounds.AddAnimSound(per,'Kgt_hurt_r_leg', HeridaKgt1, 0.4076)
	NetSounds.AddAnimSound(per,'Kgt_hurt_l_leg', HeridaKgt3, 0.4375)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_head', HeridaKgt1, 0.3333)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_neck', HeridaKgt3, 0.3158)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_breast', HeridaKgt1,0.3889)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_back', HeridaKgt3, 0.4211)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_r_arm', HeridaKgt1, 0.2100)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_l_arm', HeridaKgt3, 0.1786)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_r_leg', HeridaKgt1, 0.4076)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_l_leg', HeridaKgt3, 0.4375)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_lite', HeridaKgt1, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_hurt_f_big', HeridaKgt3, 0.3000)
	NetSounds.AddAnimSound(per,'Kgt_hurt_head', HeridaKgt1, 0.6000)
	
	
	NetSounds.AddAnimSound(per,'Kgt_key',RuidoLlaveCerradura, 0.4100)
	NetSounds.AddAnimSound(per,'Kgt_key',RuidoLlave, 0.1300)
	NetSounds.AddAnimSound(per,'Kgt_key',Ruidook, 0.2000)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_00', CogerEspada, 0.2069)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_01', CogerEspada, 0.3103) 
	NetSounds.AddAnimSound(per,'Kgt_tke_r_02', CogerEspada, 0.2759) 
	NetSounds.AddAnimSound(per,'Kgt_tke_r_03', CogerEspada, 0.2754)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_04', CogerEspada, 0.2727) 
	NetSounds.AddAnimSound(per,'Kgt_tke_r_04', CogerEspada, 0.2654)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_05', CogerEspada, 0.2654)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key00',CogerLlave, 0.2069)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key00', CogerArma, 0.5652)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key01',CogerLlave, 0.3103)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key01', CogerArma, 0.6000)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key02',CogerLlave, 0.2759)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key02', CogerArma, 0.6000)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key03',CogerLlave, 0.2754)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key03', CogerArma, 0.6000)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key04',CogerLlave, 0.2727)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key04', CogerArma, 0.6000)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key05',CogerLlave, 0.2654)
	NetSounds.AddAnimSound(per,'Kgt_tke_r_key05', CogerArma, 0.6000)
	NetSounds.AddAnimSound(per,'Kgt_lvr_u',SonidoPalanca, 0.3889)
	NetSounds.AddAnimSound(per,'Kgt_lvr_d',SonidoPalanca, 0.3548)
	
	NetSounds.AddAnimSound(per,'Kgt_chg_l', CambiarEscudo, 0.3652)
	
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r_l', Enfundar, 0.5000)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r_l', AndarKgt1, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r', Enfundar, 0.5)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r', AndarKgt1, 0.4500)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_r', CambiarEscudo, 0.3652)
	NetSounds.AddAnimSound(per,'Kgt_attack_chg_l', CambiarEscudo, 0.3652)
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	