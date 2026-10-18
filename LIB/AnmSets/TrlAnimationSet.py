##///
##||| TrlAnimationSet.PY TITANIUM
##||| Change list:
##||| * Restored missing head hit reaction
##\\\ 

import Bladex
import Enm_Def

#	JOG_ANM
#	#                     Name      WUEA,MOD_Y,SOLF,COPY_ROT,BNG_MOV,HEADF
#	Bladex.AddAnimFlags("Cos_attack_f",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
#
#
#
#
#



def LoadTrlAnimationSet(ct_name):

	print "Loading the Trl animation sets..."



	#### Relax ####


	Bladex.LoadSampledAnimation("../../Anm/Trl_rlx_1h.BMV","Trl_rlx_1h",1)
	Bladex.AddAnmRStep("Trl_rlx_1h",0.0)
	Bladex.AddAnmLStep("Trl_rlx_1h",0.0)






	####Ataques####


	Bladex.LoadSampledAnimation("../../Anm/Trl_g_01.BMV","Trl_g_01",0)

	Bladex.AddAnmRStep("Trl_g_01",0.0)
	Bladex.AddAnmLStep("Trl_g_01",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Trl_g_02.BMV","Trl_g_02",0)

	Bladex.AddAnmRStep("Trl_g_02",0.0)
	Bladex.AddAnmLStep("Trl_g_02",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Trl_g_04.BMV","Trl_g_04",0)

	Bladex.AddAnmRStep("Trl_g_04",0.0)
	Bladex.AddAnmLStep("Trl_g_04",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Trl_g_06.BMV","Trl_g_06",0)

	Bladex.AddAnmRStep("Trl_g_06",0.0)
	Bladex.AddAnmLStep("Trl_g_06",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Trl_g_12.BMV","Trl_g_12",0)

	Bladex.AddAnmLStep("Trl_g_12",0.0)
	Bladex.AddAnmLRelease("Trl_g_12",0.28)
	Bladex.AddAnmLStep("Trl_g_12",0.34)

	Bladex.AddAnmRStep("Trl_g_12",0.0)
	Bladex.AddAnmRRelease("Trl_g_12",0.35)
	Bladex.AddAnmRStep("Trl_g_12",0.47)


	Bladex.LoadSampledAnimation("../../Anm/Trl_g_18.BMV","Trl_g_18",0)

	Bladex.AddAnmLStep("Trl_g_18",0.0)
	Bladex.AddAnmLRelease("Trl_g_18",0.1)
	Bladex.AddAnmLStep("Trl_g_18",0.3)
	Bladex.AddAnmLRelease("Trl_g_18",0.6)
	Bladex.AddAnmLStep("Trl_g_18",0.74)

	Bladex.AddAnmRStep("Trl_g_18",0.0)
	Bladex.AddAnmRRelease("Trl_g_18",0.3)
	Bladex.AddAnmRStep("Trl_g_18",0.56)


	Bladex.LoadSampledAnimation("../../Anm/Trl_g_19.BMV","Trl_g_19",0)

	Bladex.AddAnmLStep("Trl_g_19",0.0)
	Bladex.AddAnmLRelease("Trl_g_19",0.16)
	Bladex.AddAnmLStep("Trl_g_19",0.53)

	Bladex.AddAnmRStep("Trl_g_19",0.0)
	Bladex.AddAnmRRelease("Trl_g_19",0.5)
	Bladex.AddAnmRStep("Trl_g_19",0.6)


	Bladex.LoadSampledAnimation("../../Anm/Trl_g_31.BMV","Trl_g_31",0)

	Bladex.AddAnmRStep("Trl_g_31",0.0)
	Bladex.AddAnmRRelease("Trl_g_31",0.4)
	Bladex.AddAnmRStep("Trl_g_31",0.53)
	Bladex.AddAnmRRelease("Trl_g_31",0.75)
	Bladex.AddAnmRStep("Trl_g_31",0.82)

	Bladex.AddAnmLStep("Trl_g_31",0.0)
	Bladex.AddAnmLRelease("Trl_g_31",0.3)
	Bladex.AddAnmLStep("Trl_g_31",0.38)
	Bladex.AddAnmLRelease("Trl_g_31",0.57)
	Bladex.AddAnmLStep("Trl_g_31",0.69)



	Bladex.LoadSampledAnimation("../../Anm/Trl_g_run.BMV","Trl_g_run",0)

	Bladex.AddAnmRStep("Trl_g_run",0.36)

	Bladex.AddAnmLStep("Trl_g_run",0.0)
	Bladex.AddAnmLRelease("Trl_g_run",0.076)
	Bladex.AddAnmLStep("Trl_g_run",0.36)


	####Andares y pasos####


	Bladex.LoadSampledAnimation("../../Anm/Trl_wbk_1h.BMV","Trl_wbk_no",1)

	Bladex.AddAnmRStep("Trl_wbk_no",0.0)
	Bladex.AddAnmRRelease("Trl_wbk_no",0.24)
	Bladex.AddAnmRStep("Trl_wbk_no",1.0)

	Bladex.AddAnmLStep("Trl_wbk_no",0.58)
	Bladex.AddAnmLRelease("Trl_wbk_no",0.71)

	Bladex.AddStopTests("Trl_wbk_no")



#	Bladex.LoadSampledAnimation("../../Anm/Trl_wbk_1h.BMV","Trl_wbk_1h",1)
#
#	Bladex.AddAnmRStep("Trl_wbk_1h",0.0)
#	Bladex.AddAnmRRelease("Trl_wbk_1h",0.24)
#	Bladex.AddAnmRStep("Trl_wbk_1h",1.0)
#
#	Bladex.AddAnmLStep("Trl_wbk_1h",0.58)
#	Bladex.AddAnmLRelease("Trl_wbk_1h",0.71)
#
#	Bladex.AddStopTests("Trl_wbk_1h")


	anm_name="Trl_wlk_no"
	Bladex.LoadSampledAnimation("../../Anm/Trl_wlk_no.BMV","Trl_wlk_no",1)

	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.271)
	Bladex.AddAnmRStep(anm_name,0.479)
	Bladex.AddAnmRRelease(anm_name,0.771)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.063)
	Bladex.AddAnmLStep(anm_name,0.271)
	Bladex.AddAnmLRelease(anm_name,0.542)
	Bladex.AddAnmLStep(anm_name,0.750)

	Bladex.AddStopTests("Trl_wlk_no")



	anm_name="Trl_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/Trl_attack_f.BMV","Trl_attack_f",1)

	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.271)
	Bladex.AddAnmRStep(anm_name,0.479)
	Bladex.AddAnmRRelease(anm_name,0.771)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.063)
	Bladex.AddAnmLStep(anm_name,0.271)
	Bladex.AddAnmLRelease(anm_name,0.542)
	Bladex.AddAnmLStep(anm_name,0.750)

	Bladex.AddStopTests("Trl_attack_f")




#	Bladex.LoadSampledAnimation("../../Anm/Trl_wlk_1h.BMV","Trl_wlk_1h",1)
#
#	Bladex.AddAnmRStep("Trl_wlk_1h",0.0)
#	Bladex.AddAnmRRelease("Trl_wlk_1h",0.5)
#	Bladex.AddAnmRStep("Trl_wlk_1h",1.0)
#
#	Bladex.AddAnmLStep("Trl_wlk_1h",0.5)
#	Bladex.AddAnmLRelease("Trl_wlk_1h",1.0)
#
#	Bladex.AddStopTests("Trl_wlk_1h")



	Bladex.LoadSampledAnimation("../../Anm/Trl_jog_1h.BMV","Trl_jog_1h",1)

	Bladex.AddAnmRStep("Trl_jog_1h",0.406)
	Bladex.AddAnmRRelease("Trl_jog_1h",0.738)
	Bladex.AddAnmLStep("Trl_jog_1h",0.000)
	Bladex.AddAnmLRelease("Trl_jog_1h",0.197)
	Bladex.AddAnmLStep("Trl_jog_1h",1.000)

	Bladex.AddStopTests("Trl_jog_1h")




	####Trepares####

	Bladex.LoadSampledAnimation("../../Anm/Trl_clmb_low_1h.BMV","Trl_clmb_low_1h",0)

	Bladex.AddAnmRStep("Trl_clmb_low_1h",0.0)
	Bladex.AddAnmRRelease("Trl_clmb_low_1h",0.055)
	Bladex.AddAnmRStep("Trl_clmb_low_1h",0.14)
	Bladex.AddAnmRRelease("Trl_clmb_low_1h",0.52)
	Bladex.AddAnmRStep("Trl_clmb_low_1h",0.66)

	Bladex.AddAnmLStep("Trl_clmb_low_1h",0.0)
	Bladex.AddAnmLRelease("Trl_clmb_low_1h",0.29)
	Bladex.AddAnmLStep("Trl_clmb_low_1h",0.44)




	####Caeres###


	Bladex.LoadSampledAnimation("../../Anm/Trl_fll_low_1h.BMV","Trl_fll_low_1h",0)

	Bladex.AddAnmRStep("Trl_fll_low_1h",0.0)
	Bladex.AddAnmRRelease("Trl_fll_low_1h",0.15)
	Bladex.AddAnmRStep("Trl_fll_low_1h",0.38)

	Bladex.AddAnmLStep("Trl_fll_low_1h",0.0)
	Bladex.AddAnmLRelease("Trl_fll_low_1h",0.21)
	Bladex.AddAnmLStep("Trl_fll_low_1h",0.38)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth_fll.BMV","Dth_Fll_Trl",0)
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth_fll2.BMV","Dth_Fll2_Trl",0)
	Bladex.AddAnmRStep("Dth_Fll2_Trl",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Trl",0.0)


	####Heridas####





	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_big.BMV","Trl_hurt_big",0)

	Bladex.AddAnmRStep("Trl_hurt_big",0.0)
	Bladex.AddAnmRRelease("Trl_hurt_big",0.34)
	Bladex.AddAnmRStep("Trl_hurt_big",0.54)

	Bladex.AddAnmLStep("Trl_hurt_big",0.0)
	Bladex.AddAnmLRelease("Trl_hurt_big",0.12)
	Bladex.AddAnmLStep("Trl_hurt_big",0.30)
	Bladex.AddAnmLRelease("Trl_hurt_big",0.65)
	Bladex.AddAnmLStep("Trl_hurt_big",0.93)



	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_jog.BMV","Trl_hurt_jog",0)

	Bladex.AddAnmRStep("Trl_hurt_jog",0.26)
	Bladex.AddAnmRRelease("Trl_hurt_jog",0.46)
	Bladex.AddAnmRStep("Trl_hurt_jog",0.72)

	Bladex.AddAnmLStep("Trl_hurt_jog",0.0)
	Bladex.AddAnmLRelease("Trl_hurt_jog",0.1)
	Bladex.AddAnmLStep("Trl_hurt_jog",0.5)
	Bladex.AddAnmLRelease("Trl_hurt_jog",0.79)
	Bladex.AddAnmLStep("Trl_hurt_jog",1.0)








###################
#                 #
# A�adidos Luismi #
#                 #
###################





	#### Muertes ####



	anm_name="Trl_dth_burned"
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth_burned.BMV","Trl_dth_burned",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.088)
	Bladex.AddAnmRStep(anm_name,0.120)
	Bladex.AddAnmRRelease(anm_name,0.168)
	Bladex.AddAnmRStep(anm_name,0.199)
	Bladex.AddAnmRRelease(anm_name,0.258)
	Bladex.AddAnmRStep(anm_name,0.284)
	Bladex.AddAnmRRelease(anm_name,0.316)
	Bladex.AddAnmRStep(anm_name,0.339)
	Bladex.AddAnmRRelease(anm_name,0.375)
	Bladex.AddAnmRStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.461)
	Bladex.AddAnmRStep(anm_name,0.481)
	Bladex.AddAnmRRelease(anm_name,0.541)
	Bladex.AddAnmRStep(anm_name,0.572)
	Bladex.AddAnmRRelease(anm_name,0.652)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.065)
	Bladex.AddAnmLStep(anm_name,0.083)
	Bladex.AddAnmLRelease(anm_name,0.133)
	Bladex.AddAnmLStep(anm_name,0.155)
	Bladex.AddAnmLRelease(anm_name,0.201)
	Bladex.AddAnmLStep(anm_name,0.240)
	Bladex.AddAnmLRelease(anm_name,0.281)
	Bladex.AddAnmLStep(anm_name,0.315)
	Bladex.AddAnmLRelease(anm_name,0.416)
	Bladex.AddAnmLStep(anm_name,0.457)
	Bladex.AddAnmLRelease(anm_name,0.497)
	Bladex.AddAnmLStep(anm_name,0.535)
	Bladex.AddAnmLRelease(anm_name,0.691)


	anm_name="Trl_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth_c1.BMV","Trl_dth_c1",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.503)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.496)


	anm_name="Trl_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth_c2.BMV","Trl_dth_c2",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.631)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.640)


	anm_name="Trl_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth_n00.BMV","Trl_dth_n00",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.256)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.131)


	anm_name="Trl_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth_n01.BMV","Trl_dth_n01",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.111)
	Bladex.AddAnmRStep(anm_name,0.250)
	Bladex.AddAnmRRelease(anm_name,0.289)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.132)
	Bladex.AddAnmLStep(anm_name,0.347)
	Bladex.AddAnmLRelease(anm_name,0.513)


	anm_name="Trl_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Trl_dth0.BMV","Trl_dth0",0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.211)
	Bladex.AddAnmRStep(anm_name,0.287)
	Bladex.AddAnmRRelease(anm_name,0.460)
	Bladex.AddAnmRStep(anm_name,0.519)
	Bladex.AddAnmRRelease(anm_name,0.777)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.188)
	Bladex.AddAnmLRelease(anm_name,0.340)
	Bladex.AddAnmLStep(anm_name,0.421)
	Bladex.AddAnmLRelease(anm_name,0.779)




	#### Mas Heridas ####


	anm_name="Trl_hurt_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_l_arm.BMV","Trl_hurt_l_arm",0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)


	anm_name="Trl_hurt_breast"
	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_breast.BMV","Trl_hurt_breast",0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)


	anm_name="Trl_hurt_back"
	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_back.BMV","Trl_hurt_back",0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)


	anm_name="Trl_hurt_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_r_arm.BMV","Trl_hurt_r_arm",0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)


	anm_name="Trl_hurt_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_r_leg.BMV","Trl_hurt_r_leg",0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)


	anm_name="Trl_hurt_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_l_leg.BMV","Trl_hurt_l_leg",0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	
	# Added 	-LeadHead
	anm_name="Trl_hurt_head"
	Bladex.LoadSampledAnimation("../../Anm/Trl_hurt_head.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)