##///
##||| AniSoundLch.PY TITANIUM
##||| Change list:
##||| * Commmented out animations that do not exist
##||| * Added "body hitting floor" (YYEAAAAAAH!) sound for death animations that were missing them.
##||| * Slight improvements in sound sync for death anims.
##||| * !!! All events which called "MuerteLch3" and "MuerteLch4" have been replaced by 1 and 2 respectively!
##|||   !!! This is done due to the fact that there are no unique sounds or parameters for 3 and 4.
##||| * Fixed hurt anims not having any sounds.
##\\\ 

import Bladex
import NetSounds
import netgame

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************

AsignarSonidosLichCalled=0
def AsignarSonidosLich(Personaje):
	from AniSoundLchX import *
	
	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoLch)
	per.AddEventSound('weapon_block', GolpeArmaArmaLch)
	per.AddEventSound('impale', TajoEmpalanteLch)
	per.AddEventSound('slash', TajoCortanteLch)
	per.AddEventSound('mutilate', TajoMutilacionLch)
	per.AddEventSound('crush', GolpeContundenteLch)
	
	
	global AsignarSonidosLichCalled
	if AsignarSonidosLichCalled:
		return
	AsignarSonidosLichCalled=1


	# Sonidos de animaciones

	# Animation Alarm (We want a selection of sounds, so better link a function)
	#per.AddAnimSound('Tkn_alarm01', KnightKeepStill, 0.0532)
	# Animation Sleep
	#per.AddAnimSound('Tkn_sleep', Snore, 0.0532)
	# Animation Speak01
	#per.AddAnimSound('Tkn_speak01', Guard1, 0.5)
	#per.AddAnimSound('Tkn_speak01', KnightKeepStill, 0.5)
	# Animation Speak02
	#per.AddAnimSound('Tkn_speak02', Guard2, 0.5)
	#per.AddAnimSound('Tkn_speak02', KnightKeepStill, 0.5)
	per.AddAnimSound('Lch_chg_r', Enfundar, 0.4)
	per.AddAnimSound('Lch_chg_r_l', Enfundar, 0.3599)
	per.AddAnimSound('Lch_attack_chg_r_l', Enfundar, 0.5)
	per.AddAnimSound('Lch_attack_chg_r', Enfundar, 0.5)
	per.AddAnimSound('Lch_chg_r', Enfundar, 0.4)
	per.AddAnimSound('Lch_chg_r_l', Enfundar, 0.3599)
	per.AddAnimSound('Lch_attack_chg_r_l', Enfundar, 0.5)
	per.AddAnimSound('Lch_attack_chg_r', Enfundar, 0.5)

	# per.AddAnimSound('Lch_g_01', EsfuerzoCorto6Lch, 0.2468)       
	# per.AddAnimSound('Lch_g_02', EsfuerzoCorto5Lch, 0.3026)
	# per.AddAnimSound('Lch_g_05', EsfuerzoCorto2Lch, 0.5300)
	# per.AddAnimSound('Lch_g_06', EsfuerzoCorto3Lch, 0.4211)
	# per.AddAnimSound('Lch_g_07', EsfuerzoCorto4Lch, 0.3291)
	# per.AddAnimSound('Lch_g_08', EsfuerzoCorto2Lch, 0.3881)
	# per.AddAnimSound('Lch_g_09', EsfuerzoCorto6Lch, 0.2895)
	# per.AddAnimSound('Lch_g_01', SesgadoCorto, 0.3377)
	# per.AddAnimSound('Lch_g_01', AndarLch1, 0.5000)
	# per.AddAnimSound('Lch_g_01', AndarLch2, 0.7000)
	# per.AddAnimSound('Lch_g_01', RespiracionLch1, 0.1500)
	# per.AddAnimSound('Lch_g_01', RespiracionLch2, 0.8000)
	# per.AddAnimSound('Lch_g_02', SesgadoCortoAgudo, 0.3158)
	# per.AddAnimSound('Lch_g_02', AndarLch1, 0.5000)
	# per.AddAnimSound('Lch_g_02', AndarLch2, 0.7000)
	# per.AddAnimSound('Lch_g_02', RespiracionLch2, 0.2200)
	# per.AddAnimSound('Lch_g_02', RespiracionLch1, 0.800)
	# per.AddAnimSound('Lch_g_05', SesgadoCortoGrave, 0.5658)       ###
	# per.AddAnimSound('Lch_g_05', AndarLch1, 0.7000)               #
	# per.AddAnimSound('Lch_g_05', AndarLch2, 0.8500)               # None of these animations exist.
	# per.AddAnimSound('Lch_g_05', RespiracionLch1, 0.1500)         # Lich only has 12, 13, 16, 18
	# per.AddAnimSound('Lch_g_05', RespiracionLch2, 0.3000)         # an claw1, claw2, claw3
	# per.AddAnimSound('Lch_g_06', SesgadoCorto, 0.4342)            #
	# per.AddAnimSound('Lch_g_06', AndarLch1, 0.7000)               # Commented out to avoid issues
	# per.AddAnimSound('Lch_g_06', AndarLch2, 0.8500)               #           -LeadHead
	# per.AddAnimSound('Lch_g_06', RespiracionLch2, 0.1200)         ###
	# per.AddAnimSound('Lch_g_06', RespiracionLch1, 0.3000)
	# per.AddAnimSound('Lch_g_06', RespiracionLch2, 0.8000)
	# per.AddAnimSound('Lch_g_06', RespiracionLch1, 0.6000)
	# per.AddAnimSound('Lch_g_07', SesgadoCortoAgudo, 0.3418)
	# per.AddAnimSound('Lch_g_07', AndarLch2, 0.6000)
	# per.AddAnimSound('Lch_g_07', AndarLch1, 0.8000)
	# per.AddAnimSound('Lch_g_07', RespiracionLch1, 0.1700)
	# per.AddAnimSound('Lch_g_07', RespiracionLch2, 0.7000)
	# per.AddAnimSound('Lch_g_07', RespiracionLch2, 0.4000)
	# per.AddAnimSound('Lch_g_08', SesgadoCortoGrave, 0.4030)
	# per.AddAnimSound('Lch_g_08', AndarLch1, 0.4030)
	# per.AddAnimSound('Lch_g_08', AndarLch2, 0.6000)
	# per.AddAnimSound('Lch_g_08', RespiracionLch2, 0.5000)
	# per.AddAnimSound('Lch_g_08', RespiracionLch1, 0.7000)
	# per.AddAnimSound('Lch_g_08', RespiracionLch2, 0.1100)
	# per.AddAnimSound('Lch_g_08', RespiracionLch1, 0.2000)
	# per.AddAnimSound('Lch_g_09', SesgadoCorto, 0.3158)
	# per.AddAnimSound('Lch_g_09', AndarLch1, 0.6000)
	# per.AddAnimSound('Lch_g_09', AndarLch2, 0.8000)
	# per.AddAnimSound('Lch_g_09', RespiracionLch1, 0.5000)
	# per.AddAnimSound('Lch_g_09', RespiracionLch2, 0.7000)
	# per.AddAnimSound('Lch_g_09', RespiracionLch2, 0.1100)
	# per.AddAnimSound('Lch_g_11', EsfuerzoGolpeFrontalLch, 0.4685)
	per.AddAnimSound('Lch_g_12', EsfuerzoGolpeFrontalLch, 0.2290)
	per.AddAnimSound('Lch_g_13', EsfuerzoGolpeFrontalLch, 0.3053)
	# per.AddAnimSound('Lch_g_14', EsfuerzoGolpeLateralLch, 0.2290)         # See comment above -LeadHead
	# per.AddAnimSound('Lch_g_15', EsfuerzoGolpeLateralLch, 0.4628)
	per.AddAnimSound('Lch_g_16', EsfuerzoGolpeLateralLch, 0.4681)
	per.AddAnimSound('Lch_g_17', EsfuerzoGolpeLateralLch, 0.4200)
	per.AddAnimSound('Lch_g_18', EsfuerzoGolpeArribaLch, 0.4224)
	# per.AddAnimSound('Lch_g_11', SesgadoLargo, 0.4775)
	# per.AddAnimSound('Lch_g_11', AndarLch1, 0.7000)
	# per.AddAnimSound('Lch_g_11', AndarLch2, 0.8500)                       # See comment above -LeadHead
	# per.AddAnimSound('Lch_g_11', RespiracionLch1, 0.1200)
	# per.AddAnimSound('Lch_g_11', RespiracionLch2, 0.2500)
	# per.AddAnimSound('Lch_g_11', RespiracionLch1, 0.6000)
	# per.AddAnimSound('Lch_g_11', RespiracionLch2, 0.8000)
	per.AddAnimSound('Lch_g_12', SesgadoLargo, 0.4351)
	per.AddAnimSound('Lch_g_12', AndarLch1, 0.7000)
	per.AddAnimSound('Lch_g_12', AndarLch2, 0.8500)
	per.AddAnimSound('Lch_g_12', RespiracionLch1, 0.5000)
	per.AddAnimSound('Lch_g_12', RespiracionLch2, 0.6000)
	per.AddAnimSound('Lch_g_12', RespiracionLch1, 0.1100)
	per.AddAnimSound('Lch_g_13', SesgadoLargoAgudo, 0.1679)
	per.AddAnimSound('Lch_g_13', AndarLch1, 0.6000)
	per.AddAnimSound('Lch_g_13', AndarLch2, 0.8500)
	per.AddAnimSound('Lch_g_13', RespiracionLch1, 0.4000)
	per.AddAnimSound('Lch_g_13', RespiracionLch2, 0.5000)
	per.AddAnimSound('Lch_g_13', RespiracionLch1, 0.7000)
	# per.AddAnimSound('Lch_g_14', SesgadoLargoGrave, 0.3969)
	# per.AddAnimSound('Lch_g_14', AndarLch1, 0.6000)
	# per.AddAnimSound('Lch_g_14', AndarLch2, 0.8500)
	# per.AddAnimSound('Lch_g_14', RespiracionLch1, 0.1100)
	# per.AddAnimSound('Lch_g_14', RespiracionLch2, 0.5000)
	# per.AddAnimSound('Lch_g_14', RespiracionLch1, 0.7000)
	# per.AddAnimSound('Lch_g_15', SesgadoLargo, 0.4463)
	# per.AddAnimSound('Lch_g_15', AndarLch1, 0.6000)
	# per.AddAnimSound('Lch_g_15', AndarLch2, 0.8000)                   # See comment above -LeadHead
	# per.AddAnimSound('Lch_g_15', RespiracionLch1, 0.1500)
	# per.AddAnimSound('Lch_g_15', RespiracionLch2, 0.3000)
	# per.AddAnimSound('Lch_g_15', RespiracionLch1, 0.6000)
	# per.AddAnimSound('Lch_g_15', RespiracionLch2, 0.7500)
	# per.AddAnimSound('Lch_g_15', RespiracionLch1, 0.9000)
	per.AddAnimSound('Lch_g_16', SesgadoLargoAgudo, 0.4823)
	per.AddAnimSound('Lch_g_16', AndarLch1, 0.6000)
	per.AddAnimSound('Lch_g_16', AndarLch2, 0.8000)
	per.AddAnimSound('Lch_g_16', RespiracionLch1, 0.1500)
	per.AddAnimSound('Lch_g_16', RespiracionLch1, 0.3000)
	per.AddAnimSound('Lch_g_16', RespiracionLch1, 0.7000)
	per.AddAnimSound('Lch_g_16', RespiracionLch1, 0.8500)
	# per.AddAnimSound('Lch_g_17', SesgadoLargoAgudo, 0.4427)
	# per.AddAnimSound('Lch_g_17', AndarLch2, 0.6000)
	# per.AddAnimSound('Lch_g_17', AndarLch1, 0.8000)
	# per.AddAnimSound('Lch_g_17', RespiracionLch1, 0.1200)                 # See comment above -LeadHead
	# per.AddAnimSound('Lch_g_17', RespiracionLch1, 0.5900)
	# per.AddAnimSound('Lch_g_17', RespiracionLch2, 0.7000)
	per.AddAnimSound('Lch_g_18', SesgadoLargoGrave, 0.4483)
	per.AddAnimSound('Lch_g_18', AndarLch1, 0.6000)
	per.AddAnimSound('Lch_g_18', AndarLch2, 0.8000)
	per.AddAnimSound('Lch_g_18', RespiracionLch1, 0.1500)
	per.AddAnimSound('Lch_g_18', RespiracionLch1, 0.3000)
	per.AddAnimSound('Lch_g_18', RespiracionLch1, 0.7000)
	per.AddAnimSound('Lch_g_18', RespiracionLch1, 0.9000)
	# per.AddAnimSound('Lch_g_22', EsfuerzoGolpeAtrasLch, 0.4300)
	# per.AddAnimSound('Lch_g_26', EsfuerzoGolpeCabezaLch, 0.1342)
	# per.AddAnimSound('Lch_g_22', SesgadoLargo, 0.4698)
	# per.AddAnimSound('Lch_g_22', AndarLch1, 0.6000)
	# per.AddAnimSound('Lch_g_22', AndarLch2, 0.8000)
	# per.AddAnimSound('Lch_g_22', RespiracionLch2, 0.3000)
	# per.AddAnimSound('Lch_g_22', RespiracionLch1, 0.1500)
	# per.AddAnimSound('Lch_g_22', RespiracionLch2, 0.7000)
	# per.AddAnimSound('Lch_g_22', RespiracionLch1, 0.9000)
	# per.AddAnimSound('Lch_g_26', SesgadoLargoAgudo, 0.1983)
	# per.AddAnimSound('Lch_g_26', RespiracionLch1, 0.3000)
	# per.AddAnimSound('Lch_g_26', RespiracionLch2, 0.4500)                 # See comment above -LeadHead
	# per.AddAnimSound('Lch_g_26', RespiracionLch1, 0.6500)
	# per.AddAnimSound('Lch_g_26', RespiracionLch2, 0.8500)
	# per.AddAnimSound('Lch_g_31', EsfuerzoGolpeAtrasLch, 0.2950)
	# per.AddAnimSound('Lch_g_31', SesgadoLargo, 0.2950)            
	# per.AddAnimSound('Lch_g_31', AndarLch2, 0.6000)
	# per.AddAnimSound('Lch_g_31', AndarLch1, 0.8000)
	# per.AddAnimSound('Lch_g_31', RespiracionLch1, 0.1500)
	# per.AddAnimSound('Lch_g_31', RespiracionLch2, 0.4000)
	# per.AddAnimSound('Lch_g_31', RespiracionLch1, 0.7000)
	# per.AddAnimSound('Lch_g_31', RespiracionLch2, 0.9000)
	
	per.AddAnimSound('Lch_g_12', SesgadoLargoAgudo, 0.5461)
	per.AddAnimSound('Lch_g_12', EsfuerzoCortoLch, 0.5180)
	per.AddAnimSound('Lch_g_16', SesgadoLargoAgudo, 0.4543)
	per.AddAnimSound('Lch_g_16', EsfuerzoCorto1Lch, 0.4400)
	per.AddAnimSound('Lch_g_13', SesgadoLargoAgudo, 0.3150)
	per.AddAnimSound('Lch_g_13', EsfuerzoCorto2Lch, 0.2900)
	per.AddAnimSound('Lch_g_18', SesgadoLargoAgudo, 0.4894)
	per.AddAnimSound('Lch_g_18', EsfuerzoCorto3Lch, 0.4700)
	
	per.AddAnimSound('Lch_g_claw1', SesgadoLargoGrave, 0.3300)
	per.AddAnimSound('Lch_g_claw1', EsfuerzoCorto4Lch, 0.3690)
	per.AddAnimSound('Lch_g_claw1', AndarLch1, 0.5500)
	per.AddAnimSound('Lch_g_claw1', AndarLch2, 0.7500)
	per.AddAnimSound('Lch_g_claw1', RespiracionLch1, 0.1200)
	per.AddAnimSound('Lch_g_claw1', RespiracionLch2, 0.6500)
	per.AddAnimSound('Lch_g_claw1', RespiracionLch1, 0.8500)
	per.AddAnimSound('Lch_g_claw2', SesgadoLargoGrave, 0.3160)
	per.AddAnimSound('Lch_g_claw2', EsfuerzoLchMediano, 0.2900)
	per.AddAnimSound('Lch_g_claw2', AndarLch1, 0.4500)
	per.AddAnimSound('Lch_g_claw2', AndarLch2, 0.6500)
	per.AddAnimSound('Lch_g_claw2', RespiracionLch1, 0.1200)
	per.AddAnimSound('Lch_g_claw2', RespiracionLch2, 0.2900)
	per.AddAnimSound('Lch_g_claw2', RespiracionLch1, 0.5500)
	per.AddAnimSound('Lch_g_claw2', RespiracionLch2, 0.7500)
	per.AddAnimSound('Lch_g_claw3', SesgadoLargoGrave, 0.3005)
	per.AddAnimSound('Lch_g_claw3', EsfuerzoLchMediano, 0.3005)
	per.AddAnimSound('Lch_g_claw3', AndarLch1, 0.5000)
	per.AddAnimSound('Lch_g_claw3', AndarLch2, 0.7000)
	per.AddAnimSound('Lch_g_claw3', RespiracionLch1, 0.1500)
	per.AddAnimSound('Lch_g_claw3', RespiracionLch2, 0.4250)
	per.AddAnimSound('Lch_g_claw3', RespiracionLch1, 0.6250)
	per.AddAnimSound('Lch_g_claw3', RespiracionLch2, 0.7000)
	
	#per.AddAnimSound('Lch_g_spit', EscupeLch1, 0.4000)
	per.AddAnimSound('Lch_g_spit', EscupeLch1, 0.1000)
	
	per.AddAnimSound('Lch_Rlx_no', SesgadoLargoAgudo, 0.2950)
	per.AddAnimSound('Lch_Wlk_1h', SesgadoLargoAgudo, 0.2950)
	

	per.AddAnimSound('Lch_clmb_medlow_1h', EsfuerzoCorto2Lch, 0.2400)
	per.AddAnimSound('Lch_clmb_medium_1h', EsfuerzoCorto2Lch, 0.1389)
	per.AddAnimSound('Lch_clmb_high_1h', EsfuerzoCorto1Lch, 0.0862)
	per.AddAnimSound('Lch_clmb_medlow_no', EsfuerzoCorto2Lch, 0.4000)
	per.AddAnimSound('Lch_clmb_medium_no', EsfuerzoCorto2Lch, 0.1944)
	per.AddAnimSound('Lch_clmb_high_no', EsfuerzoCorto1Lch, 0.1552)
	per.AddAnimSound('Lch_clmb_medium_1h', EsfuerzoCortoLch, 0.1944)
	per.AddAnimSound('Lch_clmb_high_1h', EsfuerzoLchMediano, 0.1552)
	per.AddAnimSound('Lch_clmb_high_1h', EsfuerzoCortoLch, 0.1552)
	per.AddAnimSound('Lch_clmb_medium_no', EsfuerzoCortoLch, 0.1944)
	per.AddAnimSound('Lch_clmb_high_no', EsfuerzoLchMediano, 0.1552)
	per.AddAnimSound('Lch_clmb_high_no', EsfuerzoCortoLch, 0.1552)

	per.AddAnimSound('Lch_dth0', MuerteLch1, 0.1000)
	per.AddAnimSound('Lch_dth0', CaidaLch1, 0.8820)             # Added 
	per.AddAnimSound('Lch_dth0', CaidaLch2, 0.9540)             # Anim previously had no other sounds than MuerteLch1
	per.AddAnimSound("Lch_dth0", AndarLch1, 0.1400)             #
	per.AddAnimSound("Lch_dth0", AndarLch2, 0.2450)             #       -LeadHead
	per.AddAnimSound("Lch_dth0", AndarLch1, 0.6900)             #
    
	# per.AddAnimSound("Ork_dth_i1", MuerteLch1, 0.1130)        
	# per.AddAnimSound("Ork_dth_i2", MuerteLch4, 0.1130)        # Commented out
	# per.AddAnimSound("Ork_dth_bl1", MuerteLch2, 0.1130)       # These animations do not exist. -LeadHead
	# per.AddAnimSound("Ork_dth_bl2", MuerteLch1, 0.1130)
    
    
	per.AddAnimSound("Ork_dth_rock", MuerteLch1, 0.1130)
	per.AddAnimSound("Lch_dth_n00", MuerteLch1, 0.1100)
	per.AddAnimSound("Lch_dth_n00", AndarLch1, 0.2000)
	per.AddAnimSound("Lch_dth_n00", AndarLch2, 0.4000)
	per.AddAnimSound("Lch_dth_n00", AndarLch1, 0.6000)
	per.AddAnimSound("Lch_dth_n00", AndarLch1, 0.7500)
	per.AddAnimSound("Lch_dth_n00", CaidaLch2, 0.5100)          #Added -LeadHead
	per.AddAnimSound("Lch_dth_n00", CaidaLch1, 0.7080)          #Changed (was 0.8)
    

	per.AddAnimSound("Lch_dth_n01", MuerteLch2, 0.1100)
	per.AddAnimSound("Lch_dth_n01", AndarLch1, 0.2200)
	per.AddAnimSound("Lch_dth_n01", AndarLch2, 0.4200)
	per.AddAnimSound("Lch_dth_n01", AndarLch1, 0.6200)
	per.AddAnimSound("Lch_dth_n01", AndarLch2, 0.7500)
	per.AddAnimSound("Lch_dth_n01", CaidaLch1, 0.6100)         # Changed (was 0.78)
	per.AddAnimSound("Lch_dth_n01", CaidaLch2, 0.7900)         # Added
	per.AddAnimSound("Lch_dth_n02", MuerteLch1, 0.1200)
	per.AddAnimSound("Lch_dth_n02", AndarLch1, 0.2200)
	per.AddAnimSound("Lch_dth_n02", AndarLch2, 0.4200)
	per.AddAnimSound("Lch_dth_n02", AndarLch1, 0.6200)
	per.AddAnimSound("Lch_dth_n02", AndarLch2, 0.7500)
	per.AddAnimSound("Lch_dth_n02", CaidaLch1, 0.7300)          #Changed (was 0.8)
	per.AddAnimSound("Lch_dth_n02", CaidaLch2, 0.6150)          # Added
	per.AddAnimSound("Lch_dth_n03", MuerteLch2, 0.1200)
	per.AddAnimSound("Lch_dth_n03", AndarLch1, 0.2200)
	per.AddAnimSound("Lch_dth_n03", AndarLch2, 0.4200)
	per.AddAnimSound("Lch_dth_n03", AndarLch1, 0.6200)
	per.AddAnimSound("Lch_dth_n03", AndarLch2, 0.7500)
	per.AddAnimSound("Lch_dth_n03", CaidaLch1, 0.5850)          #Changed (was 0.755)
	per.AddAnimSound("Lch_dth_n04", MuerteLch2, 0.1100)
	per.AddAnimSound("Lch_dth_n04", AndarLch1, 0.2200)
	per.AddAnimSound("Lch_dth_n04", AndarLch2, 0.4200)
	per.AddAnimSound("Lch_dth_n04", AndarLch1, 0.6200)
	per.AddAnimSound("Lch_dth_n04", AndarLch2, 0.7500)
	per.AddAnimSound("Lch_dth_n04", CaidaLch1, 0.7600)
	per.AddAnimSound("Lch_dth_n05", MuerteLch2, 0.1100)
	per.AddAnimSound("Lch_dth_n05", AndarLch1, 0.2200)
	per.AddAnimSound("Lch_dth_n05", AndarLch2, 0.4200)
	per.AddAnimSound("Lch_dth_n05", AndarLch1, 0.6200)
	per.AddAnimSound("Lch_dth_n05", AndarLch2, 0.7500)
	per.AddAnimSound("Lch_dth_n05", CaidaLch1, 0.8000)          #Changed (was 0.770)
	per.AddAnimSound("Lch_dth_n06", MuerteLch2, 0.1200)
	per.AddAnimSound("Lch_dth_n06", AndarLch2, 0.2200)
	per.AddAnimSound("Lch_dth_n06", AndarLch1, 0.4200)
	per.AddAnimSound("Lch_dth_n06", AndarLch2, 0.6200)
	per.AddAnimSound("Lch_dth_n06", AndarLch1, 0.7500)
	per.AddAnimSound("Lch_dth_n06", CaidaLch1, 0.5340)          #Changed (was 0.790)
	per.AddAnimSound("Lch_dth_n06", CaidaLch1, 0.7180)
	per.AddAnimSound("Lch_dth_c1", DesangreLch1, 0.1250)
	per.AddAnimSound("Lch_dth_c1", AndarLch1, 0.2250)
	per.AddAnimSound("Lch_dth_c1", AndarLch1, 0.3000)
	per.AddAnimSound("Lch_dth_c1", AndarLch2, 0.3800)
	per.AddAnimSound("Lch_dth_c1", AndarLch1, 0.4500)
	per.AddAnimSound("Lch_dth_c1", AndarLch1, 0.5000)
	per.AddAnimSound("Lch_dth_c1", AndarLch1, 0.6000)
	per.AddAnimSound("Lch_dth_c1", AndarLch2, 0.6800)
	per.AddAnimSound("Lch_dth_c1", AndarLch1, 0.7200)
	per.AddAnimSound("Lch_dth_c1", CaidaLch2, 0.6860)           # Changed, was CaidaLch1, 0.7800
	per.AddAnimSound("Lch_dth_c1", CaidaLch1, 0.7970)           # Added -LeadHead
	per.AddAnimSound("Lch_dth_c1", DesangreLch1, 0.2500)
	per.AddAnimSound("Lch_dth_c2", DesangreLch1, 0.1250)
	per.AddAnimSound("Lch_dth_c2", DesangreLch1, 0.2500)
	per.AddAnimSound("Lch_dth_c2", AndarLch1, 0.2250)
	per.AddAnimSound("Lch_dth_c2", AndarLch1, 0.3000)
	per.AddAnimSound("Lch_dth_c2", AndarLch2, 0.3800)
	per.AddAnimSound("Lch_dth_c2", AndarLch2, 0.4500)
	per.AddAnimSound("Lch_dth_c2", AndarLch1, 0.5000)
	per.AddAnimSound("Lch_dth_c2", AndarLch1, 0.6000)
	per.AddAnimSound("Lch_dth_c2", AndarLch2, 0.6800)
	per.AddAnimSound("Lch_dth_c2", AndarLch1, 0.7200)
	per.AddAnimSound("Lch_dth_c2", CaidaLch1, 0.7720)
	per.AddAnimSound("Lch_dth_c2", CaidaLch2, 0.8720)
	per.AddAnimSound("Lch_dth_c3", DesangreLch1, 0.1250)
	per.AddAnimSound("Lch_dth_c3", DesangreLch1, 0.2500)
	per.AddAnimSound("Lch_dth_c3", AndarLch1, 0.2250)
	per.AddAnimSound("Lch_dth_c3", AndarLch1, 0.3000)
	per.AddAnimSound("Lch_dth_c3", AndarLch2, 0.3800)
	per.AddAnimSound("Lch_dth_c3", AndarLch2, 0.4500)
	per.AddAnimSound("Lch_dth_c3", AndarLch1, 0.5000)
	per.AddAnimSound("Lch_dth_c3", AndarLch1, 0.6000)
	per.AddAnimSound("Lch_dth_c3", AndarLch2, 0.6800)
	per.AddAnimSound("Lch_dth_c3", AndarLch1, 0.7200)
	per.AddAnimSound("Lch_dth_c3", CaidaLch1, 0.7220)
	per.AddAnimSound("Lch_dth_c4", DesangreLch1, 0.1250)
	per.AddAnimSound("Lch_dth_c4", DesangreLch1, 0.2500)
	per.AddAnimSound("Lch_dth_c4", AndarLch1, 0.2250)
	per.AddAnimSound("Lch_dth_c4", AndarLch1, 0.3000)
	per.AddAnimSound("Lch_dth_c4", AndarLch2, 0.3800)
	per.AddAnimSound("Lch_dth_c4", AndarLch2, 0.4500)
	per.AddAnimSound("Lch_dth_c4", AndarLch1, 0.5000)
	per.AddAnimSound("Lch_dth_c4", AndarLch1, 0.6000)
	per.AddAnimSound("Lch_dth_c4", AndarLch2, 0.6800)
	per.AddAnimSound("Lch_dth_c4", CaidaLch1, 0.7000)
	per.AddAnimSound("Lch_dth_c4", CaidaLch2, 0.8720)
	per.AddAnimSound("Lch_dth_c5", DesangreLch1, 0.1250)
	per.AddAnimSound("Lch_dth_c5", DesangreLch1, 0.2500)
	per.AddAnimSound("Lch_dth_c5", AndarLch1, 0.2250)
	per.AddAnimSound("Lch_dth_c5", AndarLch1, 0.3000)
	per.AddAnimSound("Lch_dth_c5", AndarLch2, 0.3800)
	per.AddAnimSound("Lch_dth_c5", AndarLch2, 0.4500)
	per.AddAnimSound("Lch_dth_c5", AndarLch1, 0.5000)
	per.AddAnimSound("Lch_dth_c5", AndarLch1, 0.6000)
	per.AddAnimSound("Lch_dth_c5", AndarLch2, 0.6800)
	per.AddAnimSound("Lch_dth_c5", AndarLch1, 0.7200)
	per.AddAnimSound("Lch_dth_c5", CaidaLch1, 0.7500) # Changed, was 0.772
	per.AddAnimSound("Lch_dth_c5", CaidaLch2, 0.5190) # Changed, was 0.55 -LeadHead
	per.AddAnimSound("Lch_dth_c6", DesangreLch1, 0.1250)
	per.AddAnimSound("Lch_dth_c6", DesangreLch1, 0.2500)
	per.AddAnimSound("Lch_dth_c6", AndarLch1, 0.2250)
	per.AddAnimSound("Lch_dth_c6", AndarLch1, 0.3000)
	per.AddAnimSound("Lch_dth_c6", AndarLch2, 0.3800)
	per.AddAnimSound("Lch_dth_c6", AndarLch2, 0.4500)
	per.AddAnimSound("Lch_dth_c6", AndarLch1, 0.5000)
	per.AddAnimSound("Lch_dth_c6", AndarLch1, 0.6000)
	per.AddAnimSound("Lch_dth_c6", AndarLch2, 0.6800)
	per.AddAnimSound("Lch_dth_c6", AndarLch1, 0.7200)
	per.AddAnimSound("Lch_dth_c6", CaidaLch1, 0.7610) # Changed, was 0.77
	per.AddAnimSound("Lch_dth_c6", CaidaLch2, 0.7150) # Added -LeadHead

	# per.AddAnimSound('Lch_hurt_jog', HeridaLch2, 0.3000)         ####
	# per.AddAnimSound('Lch_hurt_neck', HeridaLch2, 0.1000)        # Commented out.
	# per.AddAnimSound('Lch_hurt_breast', HeridaLch2, 0.1667)      # 
	# per.AddAnimSound('Lch_hurt_back', HeridaLch2, 0.2632)        # These are BipedAction or AnmType names.
	# per.AddAnimSound('Lch_hurt_r_arm', HeridaLch2, 0.1500)       # 
	# per.AddAnimSound('Lch_hurt_l_arm', HeridaLch2, 0.2000)       # Function "AddAnimSound" does not care about either.
	# per.AddAnimSound('Lch_hurt_r_leg', HeridaLch2, 0.1765)       # AniSound references only animation names.
	# per.AddAnimSound('Lch_hurt_l_leg', HeridaLch2, 0.2143)       # Liches do not have any animations with these names.
	# per.AddAnimSound('Lch_hurt_f_head', HeridaLch2, 0.3000)      # 
	# per.AddAnimSound('Lch_hurt_f_breast', HeridaLch2,0.2727)     # Only valid animations by default are:
	# per.AddAnimSound('Lch_hurt_f_back', HeridaLch2, 0.1818)      #    * "Lch_hurt_big"
	# per.AddAnimSound('Lch_hurt_f_r_arm', HeridaLch2, 0.2727)     #    * "Lch_hurt_lite"
	# per.AddAnimSound('Lch_hurt_f_l_arm', HeridaLch2, 0.2727)     #    * "Lch_hurt_big2"
	# per.AddAnimSound('Lch_hurt_f_r_leg', HeridaLch2, 0.2727)     # 
	# per.AddAnimSound('Lch_hurt_f_l_leg', HeridaLch2, 0.2727)     # "_f_big" and "_f_lite" in theory exist, but are identical to normal ones and never actually called in the code.
	# per.AddAnimSound('Lch_hurt_f_lite', HeridaLch2, 0.1333)      # Additionally, they all use HeridaLch2, HeridaLch1 would be unused.
	# per.AddAnimSound('Lch_hurt_f_big', HeridaLch2, 0.1304)       # 
	# per.AddAnimSound('Lch_hurt_f_big', HeridaLch2, 0.1304)       #                                            -LeadHead
	# per.AddAnimSound('Lch_hurt_head', HeridaLch2, 0.1579)        ####
    
	per.AddAnimSound('Lch_hurt_big2', HeridaLch2, 0.1110)    ###
	per.AddAnimSound('Lch_hurt_big2', CaidaLch2, 0.1610)     ### Added
	per.AddAnimSound('Lch_hurt_big2', AndarLch2, 0.4310)     ### previously had no sound at all
	per.AddAnimSound('Lch_hurt_big2', AndarLch1, 0.5840)     ###
	per.AddAnimSound('Lch_hurt_big2', AndarLch2, 0.6910)     ###        -LeadHead
    
	per.AddAnimSound('Lch_hurt_lite', AndarLch2, 0.3770)     ### Added
    
	per.AddAnimSound('Lch_hurt_big', AndarLch2, 0.169)       ###
	per.AddAnimSound('Lch_hurt_big', AndarLch1, 0.328)       ### Added
	per.AddAnimSound('Lch_hurt_big', AndarLch2, 0.618)       ### 
	
	per.AddAnimSound('Rlx_no_Lch', RespiracionLch1, 0.1500)
	per.AddAnimSound('Rlx_no_Lch', AndarLch1, 0.2250)
	per.AddAnimSound('Rlx_no_Lch', RespiracionLch2, 0.3000)
	per.AddAnimSound('Rlx_no_Lch', AndarLch2, 0.3750)
	per.AddAnimSound('Rlx_no_Lch', RespiracionLch1, 0.4500)
	per.AddAnimSound('Rlx_no_Lch', AndarLch1, 0.5250)
	per.AddAnimSound('Rlx_no_Lch', RespiracionLch2, 0.6000)
	per.AddAnimSound('Rlx_no_Lch', AndarLch2, 0.6750)
	per.AddAnimSound('Rlx_no_Lch', RespiracionLch2, 0.7500)
	per.AddAnimSound('Rlx_no_Lch', AndarLch1, 0.8250)
	per.AddAnimSound('Rlx_no_Lch', RespiracionLch2, 0.9000)
	per.AddAnimSound('Rlx_1h_Lch', AndarLch2, 0.1500)
	per.AddAnimSound('Rlx_1h_Lch', RespiracionLch1, 0.1500)
	per.AddAnimSound('Rlx_1h_Lch', AndarLch1, 0.2250)
	per.AddAnimSound('Rlx_1h_Lch', RespiracionLch2, 0.3000)
	per.AddAnimSound('Rlx_1h_Lch', AndarLch2, 0.3750)
	per.AddAnimSound('Rlx_1h_Lch', RespiracionLch1, 0.4500)
	per.AddAnimSound('Rlx_1h_Lch', AndarLch1, 0.5250)
	per.AddAnimSound('Rlx_1h_Lch', RespiracionLch2, 0.6000)
	per.AddAnimSound('Rlx_1h_Lch', AndarLch2, 0.6750)
	per.AddAnimSound('Rlx_1h_Lch', RespiracionLch2, 0.7500)
	per.AddAnimSound('Rlx_1h_Lch', AndarLch1, 0.8250)
	per.AddAnimSound('Rlx_1h_Lch', RespiracionLch2, 0.9000)
	per.AddAnimSound('Rlx_1h2_Lch', RespiracionLch1, 0.1500)
	per.AddAnimSound('Rlx_1h2_Lch', AndarLch1, 0.2250)
	per.AddAnimSound('Rlx_1h2_Lch', RespiracionLch2, 0.3000)
	per.AddAnimSound('Rlx_1h2_Lch', AndarLch2, 0.3750)
	per.AddAnimSound('Rlx_1h2_Lch', RespiracionLch1, 0.4500)
	per.AddAnimSound('Rlx_1h2_Lch', AndarLch1, 0.5250)
	per.AddAnimSound('Rlx_1h2_Lch', RespiracionLch2, 0.6000)
	per.AddAnimSound('Rlx_1h2_Lch', AndarLch2, 0.6750)
	per.AddAnimSound('Rlx_1h2_Lch', RespiracionLch2, 0.7500)
	per.AddAnimSound('Rlx_1h2_Lch', AndarLch1, 0.8250)
	per.AddAnimSound('Rlx_1h2_Lch', RespiracionLch2, 0.9000)
	
	#per.AddAnimSound('Wlk_1h_Lch', RespiracionLch2, 0.1500)
	per.AddAnimSound('Wlk_1h_Lch', AndarLch1, 0.2250)
	#per.AddAnimSound('Wlk_1h_Lch', RespiracionLch2, 0.3000)
	per.AddAnimSound('Wlk_1h_Lch', AndarLch2, 0.3750)
	#per.AddAnimSound('Wlk_1h_Lch', RespiracionLch2, 0.4500)
	per.AddAnimSound('Wlk_1h_Lch', AndarLch1, 0.6250)
	#per.AddAnimSound('Wlk_1h_Lch', RespiracionLch2, 0.6000)
	per.AddAnimSound('Wlk_1h_Lch', AndarLch2, 0.6750)
	#per.AddAnimSound('Wlk_1h_Lch', RespiracionLch2, 0.7500)
	per.AddAnimSound('Wlk_1h_Lch', AndarLch1, 0.8250)
	#per.AddAnimSound('Wlk_1h_Lch', RespiracionLch2, 0.9000)
	
	per.AddAnimSound('Lch_appears1', GeneradorLch1, 0.1000)
	per.AddAnimSound('Lch_appears2', GeneradorLch2, 0.1000)
	
	
	
	
	
	