##///
##||| ChkAnimationSet.PY TITANIUM
##||| Change list:
##||| * Added unused rlx_no anim
##||| * Pre-loads strafe anims
##\\\ 

import Bladex
import Enm_Def

def LoadChkAnimationSet(ct_name):

	print "Loading the ChaosKnight animation sets..."


######  RELAX

	Bladex.LoadSampledAnimation("../../Anm/Chk_rlx_1h.BMV","Rlx_1h_Chk",1)
	Bladex.AddAnmRStep("Rlx_1h_Chk",0)
	Bladex.AddAnmLStep("Rlx_1h_Chk",0)
	#Bladex.AddStopTests("Rlx_1h_Chk")


	Bladex.LoadSampledAnimation("../../Anm/Chk_rlx_f_s.BMV","Rlx_f_s_Chk",1)
	Bladex.AddAnmRStep("Rlx_f_s_Chk",0)
	Bladex.AddAnmLStep("Rlx_f_s_Chk",0)
	#Bladex.AddStopTests("Rlx_f_s_Chk")


	Bladex.LoadSampledAnimation("../../Anm/Chk_rlx_f.BMV","Rlx_f_Chk",1)
	Bladex.AddAnmRStep("Rlx_f_Chk",0)
	Bladex.AddAnmLStep("Rlx_f_Chk",0)
	#Bladex.AddStopTests("Rlx_f_Chk")

	Bladex.LoadSampledAnimation("../../Anm/Chk_rlx_no.BMV","Rlx_no_Chk",1)		# Added
	Bladex.AddAnmRStep("Rlx_no_Chk",0)
	Bladex.AddAnmLStep("Rlx_no_Chk",0)
	#Bladex.AddStopTests("Rlx_no_Chk")

	Bladex.LoadSampledAnimation("../../Anm/Chk_appears.BMV","Chk_appears",0)
	Bladex.AddAnmRStep("Chk_appears",0)
	Bladex.AddAnmLStep("Chk_appears",0)


###### MOVIMIENTOS

	Bladex.LoadSampledAnimation("../../Anm/Chk_attack_b.BMV","Wbk_1h_Chk",1)
	Bladex.AddAnmRStep("Wbk_1h_Chk",0)
	Bladex.AddAnmLStep("Wbk_1h_Chk",0)
	Bladex.AddAnmRRelease("Wbk_1h_Chk",0.302)
	Bladex.AddAnmRStep("Wbk_1h_Chk",0.486)
	Bladex.AddAnmLRelease("Wbk_1h_Chk",0.829)
	Bladex.AddAnmLStep("Wbk_1h_Chk",1)
	Bladex.AddStopTests("Wbk_1h_Chk")

	anm_name="Wlk_1h_Chk"
	Bladex.LoadSampledAnimation("../../Anm/Chk_wlk_1h.BMV","Wlk_1h_Chk",1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.538)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.085)
	Bladex.AddAnmLStep(anm_name,0.511)
	Bladex.AddStopTests("Wlk_1h_Chk")

###############ENCARADO


	anm_name="Attack_f_s_Chk"
	Bladex.LoadSampledAnimation("../../Anm/Chk_attack_f_s.BMV","Attack_f_s_Chk",1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.538)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.085)
	Bladex.AddAnmLStep(anm_name,0.511)


	Bladex.LoadSampledAnimation("../../Anm/Chk_attack_b.BMV","Attack_b_Chk",1)
	Bladex.AddAnmRStep("Attack_b_Chk",0)
	Bladex.AddAnmLStep("Attack_b_Chk",0)
	Bladex.AddAnmRRelease("Attack_b_Chk",0.302)
	Bladex.AddAnmRStep("Attack_b_Chk",0.486)
	Bladex.AddAnmLRelease("Attack_b_Chk",0.829)
	Bladex.AddAnmLStep("Attack_b_Chk",1)
	Bladex.AddStopTests("Attack_b_Chk")



	Bladex.LoadSampledAnimation("../../Anm/Chk_attack_b_s.BMV","Attack_b_s_Chk",1)
	Bladex.AddAnmRStep("Attack_b_s_Chk",0)
	Bladex.AddAnmLStep("Attack_b_s_Chk",0)
	Bladex.AddAnmRRelease("Attack_b_s_Chk",0.286)
	Bladex.AddAnmRStep("Attack_b_s_Chk",0.497)
	Bladex.AddAnmLRelease("Attack_b_s_Chk",0.792)
	Bladex.AddAnmLStep("Attack_b_s_Chk",1)
	Bladex.AddStopTests("Attack_b_s_Chk")


############### Strafe anims added (TO DO: refine step timing)		-LeadHead

	anm_name="Chk_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.286)
	Bladex.AddAnmRStep(anm_name,0.497)
	Bladex.AddAnmLRelease(anm_name,0.792)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	
	anm_name="Chk_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.286)
	Bladex.AddAnmRStep(anm_name,0.497)
	Bladex.AddAnmLRelease(anm_name,0.792)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	
	anm_name="Chk_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.286)
	Bladex.AddAnmRStep(anm_name,0.497)
	Bladex.AddAnmLRelease(anm_name,0.792)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Chk_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.286)
	Bladex.AddAnmRStep(anm_name,0.497)
	Bladex.AddAnmLRelease(anm_name,0.792)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

###### HERIDAS y MUERTE

	Bladex.LoadSampledAnimation("../../Anm/Chk_hurt01.BMV","Chk_hurt01",0)
	Bladex.AddAnmRStep("Chk_hurt01",0)
	Bladex.AddAnmLStep("Chk_hurt01",0)
	Bladex.AddAnmLRelease("Chk_hurt01",0.071)
	Bladex.AddAnmLStep("Chk_hurt01",0.195)
	Bladex.AddAnmLRelease("Chk_hurt01",0.813)
	Bladex.AddAnmLStep("Chk_hurt01",0.945)


	Bladex.LoadSampledAnimation("../../Anm/Chk_hurt_hip.BMV","Chk_hurt_hip",0)
	Bladex.AddAnmRStep("Chk_hurt_hip",0)
	Bladex.AddAnmLStep("Chk_hurt_hip",0)


	Bladex.LoadSampledAnimation("../../Anm/Chk_dth0.BMV","Chk_dth0",0)
	Bladex.AddAnmRStep("Chk_dth0",0)
	Bladex.AddAnmLStep("Chk_dth0",0)


	Bladex.LoadSampledAnimation("../../Anm/Chk_disappear.BMV","Chk_disappear",0)
	Bladex.AddAnmRStep("Chk_disappear",0)
	Bladex.AddAnmLStep("Chk_disappear",0)




###### ATAQUES


	Bladex.LoadSampledAnimation("../../Anm/Chk_g_01.BMV","Chk_g_01",0)
	Bladex.AddAnmRStep("Chk_g_01",0)
	Bladex.AddAnmLStep("Chk_g_01",0)


	Bladex.LoadSampledAnimation("../../Anm/Chk_g_02.BMV","Chk_g_02",0)
	Bladex.AddAnmRStep("Chk_g_02",0)
	Bladex.AddAnmLStep("Chk_g_02",0)


	Bladex.LoadSampledAnimation("../../Anm/Chk_g_07.BMV","Chk_g_07",0)
	Bladex.AddAnmRStep("Chk_g_07",0)
	Bladex.AddAnmLStep("Chk_g_07",0)



	Bladex.LoadSampledAnimation("../../Anm/Chk_g_08.BMV","Chk_g_08",0)
	#Bladex.AddAnmRStep("Chk_g_08",0)
	Bladex.AddAnmLStep("Chk_g_08",0)
	#Bladex.AddAnmRRelease("Chk_g_08",0.143)
	#Bladex.AddAnmRStep("Chk_g_08",0.350)
	#Bladex.AddAnmRRelease("Chk_g_08",0.588)
	#Bladex.AddAnmRStep("Chk_g_08",0.874)


	Bladex.LoadSampledAnimation("../../Anm/Chk_g_12.BMV","Chk_g_12",0)
	#Bladex.AddAnmRStep("Chk_g_12",0)
	Bladex.AddAnmLStep("Chk_g_12",0)
	#Bladex.AddAnmRRelease("Chk_g_12",0.113)
	#Bladex.AddAnmRStep("Chk_g_12",0.265)
	#Bladex.AddAnmRRelease("Chk_g_12",0.691)
	#Bladex.AddAnmRStep("Chk_g_12",0.843)


	Bladex.LoadSampledAnimation("../../Anm/Chk_g_18.BMV","Chk_g_18",0)
	#Bladex.AddAnmRStep("Chk_g_18",0)
	Bladex.AddAnmLStep("Chk_g_18",0)
	#Bladex.AddAnmRRelease("Chk_g_18",0.115)
	#Bladex.AddAnmRStep("Chk_g_18",0.313)
	#Bladex.AddAnmRRelease("Chk_g_18",0.658)
	#Bladex.AddAnmRStep("Chk_g_18",0.802)


	Bladex.LoadSampledAnimation("../../Anm/Chk_g_31.BMV","Chk_g_31",0)
	Bladex.AddAnmRStep("Chk_g_31",0)
	Bladex.AddAnmLStep("Chk_g_31",0)
	Bladex.AddAnmRRelease("Chk_g_31",0.421)
	Bladex.AddAnmRStep("Chk_g_31",0.502)
	Bladex.AddAnmRRelease("Chk_g_31",0.745)
	Bladex.AddAnmRStep("Chk_g_31",0.872)


	Bladex.LoadSampledAnimation("../../Anm/Chk_g_magic.BMV","Chk_g_magic",0)
	Bladex.AddAnmRStep("Chk_g_magic",0)
	Bladex.AddAnmLStep("Chk_g_magic",0)
	Bladex.AddAnmRRelease("Chk_g_magic",0.376)
	Bladex.AddAnmRStep("Chk_g_magic",0.430)
	Bladex.AddAnmRRelease("Chk_g_magic",0.626)
	Bladex.AddAnmRStep("Chk_g_magic",0.697)


######  VARIOS


	Bladex.LoadSampledAnimation("../../Anm/Chk_powerup.BMV","Chk_powerup",0)
	Bladex.AddAnmRStep("Chk_powerup",0)
	Bladex.AddAnmLStep("Chk_powerup",0)
	Bladex.AddAnmLRelease("Chk_powerup",0.072)
	Bladex.AddAnmLStep("Chk_powerup",0.145)
	Bladex.AddAnmLRelease("Chk_powerup",0.821)
	Bladex.AddAnmLStep("Chk_powerup",0.890)








	#
	# Slip
	#
	anm_name="Chk_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Chk_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Chk_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


#
#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Chk_dth_fll.BMV","Dth_Fll_Chk",0)
	#Bladex.AddAnmRStep("Dth_Fll_Chk",0.0)
	#Bladex.AddAnmLStep("Dth_Fll_Chk",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Chk_dth_fll2.BMV","Dth_Fll2_Chk",0)
	Bladex.AddAnmRStep("Dth_Fll2_Chk",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Chk",0.0)
