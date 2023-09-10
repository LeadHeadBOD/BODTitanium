##///
##||| TRAIKNIGHTNIMATIONSET.PY TITANIUM
##||| Change list:
##||| * Added steps for dth anims that were missing them.
##\\\ 

import Bladex
import Enm_Def



def LoadTraitorKnightAnimationSet(ct_name):

	#### Relax ####
	#Bladex.AddAnimFlags("Tkn_rlx",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)

	Bladex.LoadSampledAnimation("../../Anm/Tkn_rlx_no.BMV","Rlx_no_Tkn",1)
	Bladex.AddAnmRStep("Rlx_no_Tkn",0.0)
	Bladex.AddAnmLStep("Rlx_no_Tkn",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Tkn_rlx_no.BMV","Rlx_1h_Tkn",1)
	Bladex.AddAnmRStep("Rlx_1h_Tkn",0)
	Bladex.AddAnmLStep("Rlx_1h_Tkn",0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_b.BMV","Rlx_b_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmRStep("Rlx_b_Tkn",0.0)
	Bladex.AddAnmLStep("Rlx_b_Tkn",0.0)




####	TREPAR


	anm_name="Tkn_clmb_low_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_low_1h.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.17)
	Bladex.AddAnmRStep(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.48)
	Bladex.AddAnmLStep(anm_name,0.82)

	anm_name="Tkn_clmb_medlow_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_medlow_1h.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.30)
	Bladex.AddAnmRStep(anm_name,0.79)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.28)
	Bladex.AddAnmLStep(anm_name,0.53)
	Bladex.AddAnmLRelease(anm_name,0.83)
	Bladex.AddAnmLStep(anm_name,0.98)

	anm_name="Tkn_clmb_medium_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_medium_1h.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.13)
	Bladex.AddAnmRStep(anm_name,0.84)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,1)

	anm_name="Tkn_clmb_high_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_high_1h.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.09)
	Bladex.AddAnmRStep(anm_name,0.88)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.09)
	Bladex.AddAnmLStep(anm_name,1.0)






	#### Caidas ####

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_low_no.BMV","FallLow_Tkn",0,"Knight_Traitor")
	Bladex.AddAnmRStep("FallLow_Tkn",0.0)
	Bladex.AddAnmLStep("FallLow_Tkn",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_med_no.BMV","FallMed_Tkn",0,"Knight_Traitor")
	Bladex.AddAnmRStep("FallMed_Tkn",0.0)
	Bladex.AddAnmLStep("FallMed_Tkn",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_high_no.BMV","FallHigh_Tkn",0,"Knight_Traitor")
	Bladex.AddAnmRStep("FallHigh_Tkn",0.0)
	Bladex.AddAnmLStep("FallHigh_Tkn",0.0)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Tkn",0)
	#Bladex.AddAnmRStep("Dth_Fll_Tkn",0.0)
	#Bladex.AddAnmLStep("Dth_Fll_Tkn",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Tkn",0)
	Bladex.AddAnmRStep("Dth_Fll2_Tkn",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Tkn",0.0)



	### CORRER   ####
#	Bladex.LoadSampledAnimation("../../Anm/Tkn_jog_no.BMV","Jog_no_Tkn",1)
#	Bladex.AddAnmRStep("Jog_no_Tkn",0.0)
#	Bladex.AddAnmLStep("Jog_no_Tkn",0.498)
#	Bladex.AddAnmRStep("Jog_no_Tkn",1.0)
#	Bladex.AddAnmRRelease("Jog_no_Tkn",0.329)
#	Bladex.AddAnmLRelease("Jog_no_Tkn",0.862)
#	Bladex.AddStopTests("Jog_no_Tkn")
	#Bladex.AddAnmEvent("Jog_no_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Jog_no_Tkn","StopTest",0.7)

	Bladex.LoadSampledAnimation("../../Anm/Tkn_jog_1h.BMV","Jog_1h_Tkn",1)
	Bladex.AddAnmRStep("Jog_1h_Tkn",0.00)
	Bladex.AddAnmLStep("Jog_1h_Tkn",0.511)
	Bladex.AddAnmRStep("Jog_1h_Tkn",1.00)
	Bladex.AddAnmRRelease("Jog_1h_Tkn",0.308)
	Bladex.AddAnmLRelease("Jog_1h_Tkn",0.794)
	Bladex.AddAnmEvent("Jog_1h_Tkn","StopTest",0.20)
	Bladex.AddAnmEvent("Jog_1h_Tkn","StopTest",0.7)

	Bladex.LoadSampledAnimation("../../Anm/Tkn_jog_2h.BMV","Jog_2h_Tkn",1)
	Bladex.AddAnmRStep("Jog_2h_Tkn",0.00)
	Bladex.AddAnmLStep("Jog_2h_Tkn",0.511)
	Bladex.AddAnmRStep("Jog_2h_Tkn",1.00)
	Bladex.AddAnmRRelease("Jog_2h_Tkn",0.308)
	Bladex.AddAnmLRelease("Jog_2h_Tkn",0.794)
	Bladex.AddAnmEvent("Jog_2h_Tkn","StopTest",0.20)
	Bladex.AddAnmEvent("Jog_2h_Tkn","StopTest",0.7)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_jog_b.BMV","Jog_b_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmRStep("Jog_b_Tkn",0.0)
	Bladex.AddAnmRRelease("Jog_b_Tkn",0.324)
	Bladex.AddAnmRStep("Jog_b_Tkn",1.0)
	Bladex.AddAnmLStep("Jog_b_Tkn",0.334)
	Bladex.AddAnmLRelease("Jog_b_Tkn",0.525)
	Bladex.AddStopTests("Jog_b_Tkn")
	#Bladex.AddAnmEvent("Jog_b_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Jog_b_Tkn","StopTest",0.7)

	### SNEAK   ####
	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_no.BMV","Snk_no_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmRStep("Snk_no_Tkn",0.0)
	Bladex.AddAnmLStep("Snk_no_Tkn",0.485)
	Bladex.AddAnmRStep("Snk_no_Tkn",1.0)
	Bladex.AddAnmRRelease("Snk_no_Tkn",0.543)
	Bladex.AddAnmLRelease("Snk_no_Tkn",0.627)
	Bladex.AddStopTests("Sbk_no_Tkn")
	#Bladex.AddAnmEvent("Snk_no_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Snk_no_Tkn","StopTest",0.7)

	Bladex.LoadSampledAnimation("../../Anm/kgt_snk_1h.BMV","Snk_1h_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmRStep("Snk_1h_Tkn",0.000)
	Bladex.AddAnmLRelease("Snk_1h_Tkn",0.985)
	Bladex.AddAnmRStep("Snk_1h_Tkn",1.000)
	Bladex.AddAnmLStep("Snk_1h_Tkn",0.500)
	Bladex.AddAnmRRelease("Snk_1h_Tkn",0.500)
	Bladex.AddStopTests("Snk_1h_Tkn")
	#Bladex.AddAnmEvent("Snk_1h_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Snk_1h_Tkn","StopTest",0.7)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_b.BMV","Snk_b_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmRStep("Snk_b_Tkn",0.0)
	Bladex.AddAnmLStep("Snk_b_Tkn",0.509)
	Bladex.AddAnmRStep("Snk_b_Tkn",1.0)
	Bladex.AddAnmRRelease("Snk_b_Tkn",0.608)
	Bladex.AddAnmLRelease("Snk_b_Tkn",0.98)
	Bladex.AddStopTests("Snk_b_Tkn")
	#Bladex.AddAnmEvent("Snk_b_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Snk_b_Tkn","StopTest",0.7)


	#### TMP WBK ####
	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_1h.BMV","Wbk_1h_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmLStep("Wbk_1h_Tkn",0.0)
	Bladex.AddAnmRStep("Wbk_1h_Tkn",0.5)
	Bladex.AddAnmLStep("Wbk_1h_Tkn",1.0)
	Bladex.AddAnmLRelease("Wbk_1h_Tkn",0.5)
	Bladex.AddAnmRRelease("Wbk_1h_Tkn",1.0)
	Bladex.AddStopTests("Wbk_1h_Tkn")
	#Bladex.AddAnmEvent("Wbk_1h_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Wbk_1h_Tkn","StopTest",0.70)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_no.BMV","Wbk_no_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmLStep("Wbk_no_Tkn",0.0)
	Bladex.AddAnmRStep("Wbk_no_Tkn",0.5)
	Bladex.AddAnmLStep("Wbk_no_Tkn",1.0)
	Bladex.AddAnmLRelease("Wbk_no_Tkn",0.5)
	Bladex.AddAnmRRelease("Wbk_no_Tkn",1.0)
	Bladex.AddStopTests("Wbk_no_Tkn")
	#Bladex.AddAnmEvent("Wbk_no_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Wbk_no_Tkn","StopTest",0.70)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_b.BMV","Wbk_b_Tkn",1,"Knight_Traitor")
	Bladex.AddAnmRStep("Wbk_b_Tkn",0.0)
	Bladex.AddAnmLStep("Wbk_b_Tkn",0.5)
	Bladex.AddAnmRStep("Wbk_b_Tkn",1.0)
	Bladex.AddAnmRRelease("Wbk_b_Tkn",0.5)
	Bladex.AddAnmLRelease("Wbk_b_Tkn",1.0)
	Bladex.AddStopTests("Wbk_b_Tkn")
	#Bladex.AddAnmEvent("Wbk_b_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Wbk_b_Tkn","StopTest",0.70)





	#
	#### Caminar ####
	#

	Bladex.LoadSampledAnimation("../../Anm/Tkn_wlk_2h.BMV","Wlk_2h_Tkn",1)

	Bladex.AddAnmLStep("Wlk_2h_Tkn",0.0)
	Bladex.AddAnmRStep("Wlk_2h_Tkn",0.5)
	Bladex.AddAnmLStep("Wlk_2h_Tkn",1.0)
	Bladex.AddAnmLRelease("Wlk_2h_Tkn",0.5)
	Bladex.AddAnmRRelease("Wlk_2h_Tkn",1.0)
	Bladex.AddStopTests("Wlk_2h_Tkn")
	Bladex.AddStopTests("Wlk_2h_Tkn")
	#Bladex.AddAnmEvent("Wlk_2h_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Wlk_2h_Tkn","StopTest",0.7)


	Bladex.LoadSampledAnimation("../../Anm/Tkn_wlk_1h.BMV","Wlk_1h_Tkn",1)

	Bladex.AddAnmRStep("Wlk_1h_Tkn",0.0)
	Bladex.AddAnmLStep("Wlk_1h_Tkn",0.0)
	Bladex.AddAnmRRelease("Wlk_1h_Tkn",0.123)
	Bladex.AddAnmRStep("Wlk_1h_Tkn",0.522)
	Bladex.AddAnmLRelease("Wlk_1h_Tkn",0.618)
	Bladex.AddAnmLStep("Wlk_1h_Tkn",1.0)
	Bladex.AddStopTests("Wlk_1h_Tkn")
	#Bladex.AddAnmEvent("Wlk_1h_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Wlk_1h_Tkn","StopTest",0.7)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_no.BMV","Wlk_no_Tkn",1,"Knight_Traitor")

	Bladex.AddAnmRStep("Wlk_no_Tkn",0.0)
	Bladex.AddAnmLStep("Wlk_no_Tkn",0.5)
	Bladex.AddAnmRStep("Wlk_no_Tkn",1.0)
	Bladex.AddAnmRRelease("Wlk_no_Tkn",0.5)
	Bladex.AddAnmLRelease("Wlk_no_Tkn",1.0)
	Bladex.AddStopTests("Wlk_no_Tkn")
	#Bladex.AddAnmEvent("Wlk_no_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Wlk_no_Tkn","StopTest",0.7)


#	anm_name="Tkn_wlk_t"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.11)
#	Bladex.AddAnmLStep(anm_name,0.52)
#	Bladex.AddAnmRRelease(anm_name,0.61)
#	Bladex.AddStopTests(anm_name)
#	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)



	#Andar con arco

	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_b.BMV","Wlk_b_Tkn",1,"Knight_Traitor")

	Bladex.AddAnmRStep("Wlk_b_Tkn",0.0)
	Bladex.AddAnmLStep("Wlk_b_Tkn",0.5)
	Bladex.AddAnmRStep("Wlk_b_Tkn",1.0)
	Bladex.AddAnmRRelease("Wlk_b_Tkn",0.5)
	Bladex.AddAnmLRelease("Wlk_b_Tkn",1.0)
	Bladex.AddStopTests("Wlk_b_Tkn")
	Bladex.AddStopTests("Wlk_b_Tkn")
	#Bladex.AddAnmEvent("Wlk_b_Tkn","StopTest",0.20)
	#Bladex.AddAnmEvent("Wlk_b_Tkn","StopTest",0.7)







	#
	# Ataques
	#
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_08.BMV","Tkn_g_08",0)
	Bladex.AddAnmRStep("Tkn_g_08",0)
	Bladex.AddAnmLStep("Tkn_g_08",0)
	Bladex.AddAnmRRelease("Tkn_g_08",0.29)
	Bladex.AddAnmRStep("Tkn_g_08",0.49)
	Bladex.AddAnmRRelease("Tkn_g_08",0.72)
	Bladex.AddAnmRStep("Tkn_g_08",0.89)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01.BMV","Tkn_g_01",0)
	Bladex.AddAnmRStep("Tkn_g_01",0)
	Bladex.AddAnmLStep("Tkn_g_01",0)
	Bladex.AddAnmRRelease("Tkn_g_01",0.21)
	Bladex.AddAnmRStep("Tkn_g_01",0.36)
	Bladex.AddAnmRRelease("Tkn_g_01",0.64)
	Bladex.AddAnmRStep("Tkn_g_01",0.83)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_02.BMV","Tkn_g_02",0)
	Bladex.AddAnmRStep("Tkn_g_02",0)
	Bladex.AddAnmLStep("Tkn_g_02",0)
	Bladex.AddAnmRRelease("Tkn_g_02",0.15)
	Bladex.AddAnmRStep("Tkn_g_02",0.27)
	Bladex.AddAnmRRelease("Tkn_g_02",0.55)
	Bladex.AddAnmRStep("Tkn_g_02",0.74)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_05.BMV","Tkn_g_05",0)
	Bladex.AddAnmRStep("Tkn_g_05",0)
	Bladex.AddAnmLStep("Tkn_g_05",0)
	Bladex.AddAnmRRelease("Tkn_g_05",0.28)
	Bladex.AddAnmRStep("Tkn_g_05",0.5)
	Bladex.AddAnmRRelease("Tkn_g_05",0.72)
	Bladex.AddAnmRStep("Tkn_g_05",0.9)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_06.BMV","Tkn_g_06",0)
	Bladex.AddAnmRStep("Tkn_g_06",0)
	Bladex.AddAnmLStep("Tkn_g_06",0)
	Bladex.AddAnmRRelease("Tkn_g_06",0.19)
	Bladex.AddAnmRStep("Tkn_g_06",0.37)
	Bladex.AddAnmRRelease("Tkn_g_06",0.67)
	Bladex.AddAnmRStep("Tkn_g_06",0.85)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_07.BMV","Tkn_g_07",0)
	Bladex.AddAnmRStep("Tkn_g_07",0)
	Bladex.AddAnmLStep("Tkn_g_07",0)
	Bladex.AddAnmRRelease("Tkn_g_07",0.15)
	Bladex.AddAnmRStep("Tkn_g_07",0.35)
	Bladex.AddAnmRRelease("Tkn_g_07",0.51)
	Bladex.AddAnmRStep("Tkn_g_07",0.72)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_09.BMV","Tkn_g_09",0)
	Bladex.AddAnmRStep("Tkn_g_09",0)
	Bladex.AddAnmLStep("Tkn_g_09",0)
	Bladex.AddAnmRRelease("Tkn_g_09",0.23)
	Bladex.AddAnmRStep("Tkn_g_09",0.36)
	Bladex.AddAnmRRelease("Tkn_g_09",0.55)
	Bladex.AddAnmRStep("Tkn_g_09",0.71)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_13.BMV","Tkn_g_13",0)
	Bladex.AddAnmRStep("Tkn_g_13",0)
	Bladex.AddAnmLStep("Tkn_g_13",0)
	Bladex.AddAnmRRelease("Tkn_g_13",0.41)
	Bladex.AddAnmRStep("Tkn_g_13",0.57)
	Bladex.AddAnmLRelease("Tkn_g_13",0.76)
	Bladex.AddAnmLStep("Tkn_g_13",0.89)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_18.BMV","Tkn_g_18",0)
	Bladex.AddAnmRStep("Tkn_g_18",0)
	Bladex.AddAnmLStep("Tkn_g_18",0)
	Bladex.AddAnmRRelease("Tkn_g_18",0.37)
	Bladex.AddAnmRStep("Tkn_g_18",0.50)
	Bladex.AddAnmLRelease("Tkn_g_18",0.77)
	Bladex.AddAnmLStep("Tkn_g_18",0.90)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_14.BMV","Tkn_g_14",0)
	Bladex.AddAnmRStep("Tkn_g_14",0)
	Bladex.AddAnmLStep("Tkn_g_14",0)
	Bladex.AddAnmLRelease("Tkn_g_14",0.15)
	Bladex.AddAnmLStep("Tkn_g_14",0.37)
	Bladex.AddAnmRRelease("Tkn_g_14",0.43)
	Bladex.AddAnmRStep("Tkn_g_14",0.56)
	Bladex.AddAnmLRelease("Tkn_g_14",0.73)
	Bladex.AddAnmLStep("Tkn_g_14",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_11.BMV","Tkn_g_11",0)
	Bladex.AddAnmRStep("Tkn_g_11",0)
	Bladex.AddAnmLStep("Tkn_g_11",0)
	Bladex.AddAnmRRelease("Tkn_g_11",0.4)
	Bladex.AddAnmRStep("Tkn_g_11",0.55)
	Bladex.AddAnmLRelease("Tkn_g_11",0.78)
	Bladex.AddAnmLStep("Tkn_g_11",0.93)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_16.BMV","Tkn_g_16",0)
	Bladex.AddAnmRStep("Tkn_g_16",0)
	Bladex.AddAnmLStep("Tkn_g_16",0)
	Bladex.AddAnmRRelease("Tkn_g_16",0.16)
	Bladex.AddAnmRStep("Tkn_g_16",0.275)
	Bladex.AddAnmLRelease("Tkn_g_16",0.54)
	Bladex.AddAnmLStep("Tkn_g_16",0.675)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_12.BMV","Tkn_g_12",0)
	Bladex.AddAnmRStep("Tkn_g_12",0)
	Bladex.AddAnmLStep("Tkn_g_12",0)
	Bladex.AddAnmRRelease("Tkn_g_12",0.4)
	Bladex.AddAnmRStep("Tkn_g_12",0.52)
	Bladex.AddAnmLRelease("Tkn_g_12",0.71)
	Bladex.AddAnmLStep("Tkn_g_12",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_17.BMV","Tkn_g_17",0)
	Bladex.AddAnmRStep("Tkn_g_17",0)
	Bladex.AddAnmLStep("Tkn_g_17",0)
	Bladex.AddAnmRRelease("Tkn_g_17",0.16)
	Bladex.AddAnmRStep("Tkn_g_17",0.27)
	Bladex.AddAnmLRelease("Tkn_g_17",0.53)
	Bladex.AddAnmLStep("Tkn_g_17",0.65)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_15.BMV","Tkn_g_15",0)
	Bladex.AddAnmRStep("Tkn_g_15",0)
	Bladex.AddAnmLStep("Tkn_g_15",0)
	Bladex.AddAnmRRelease("Tkn_g_15",0.17)
	Bladex.AddAnmRStep("Tkn_g_15",0.35)
	Bladex.AddAnmLRelease("Tkn_g_15",0.56)
	Bladex.AddAnmLStep("Tkn_g_15",0.76)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_21.BMV","Tkn_g_21",0)
	Bladex.AddAnmRStep("Tkn_g_21",0)
	Bladex.AddAnmLStep("Tkn_g_21",0)
	Bladex.AddAnmRRelease("Tkn_g_21",0.51)
	Bladex.AddAnmRStep("Tkn_g_21",0.669)
	Bladex.AddAnmLRelease("Tkn_g_21",0.696)
	Bladex.AddAnmLStep("Tkn_g_21",0.834)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_22.BMV","Tkn_g_22",0)
	Bladex.AddAnmRStep("Tkn_g_22",0)
	Bladex.AddAnmLStep("Tkn_g_22",0)
	Bladex.AddAnmRRelease("Tkn_g_22",0.474)
	Bladex.AddAnmRStep("Tkn_g_22",0.544)
	Bladex.AddAnmRRelease("Tkn_g_22",0.605)
	Bladex.AddAnmRStep("Tkn_g_22",0.67)
	Bladex.AddAnmRRelease("Tkn_g_22",0.781)
	Bladex.AddAnmRStep("Tkn_g_22",0.847)
	Bladex.AddAnmLRelease("Tkn_g_22",0.2)
	Bladex.AddAnmLStep("Tkn_g_22",0.433)
	Bladex.AddAnmLRelease("Tkn_g_22",0.549)
	Bladex.AddAnmLStep("Tkn_g_22",0.6)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_23.BMV","Tkn_g_23",0)
	Bladex.AddAnmRStep("Tkn_g_23",0)
	Bladex.AddAnmLStep("Tkn_g_23",0)
	Bladex.AddAnmRRelease("Tkn_g_23",0.529)
	Bladex.AddAnmRStep("Tkn_g_23",0.743)
	Bladex.AddAnmLRelease("Tkn_g_23",0.75)
	Bladex.AddAnmLStep("Tkn_g_23",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_26.BMV","Tkn_g_26",0)
	Bladex.AddAnmRStep("Tkn_g_26",0)
	Bladex.AddAnmLStep("Tkn_g_26",0)
	Bladex.AddAnmRRelease("Tkn_g_26",0.135)
	Bladex.AddAnmRStep("Tkn_g_26",0.236)
	Bladex.AddAnmLRelease("Tkn_g_26",0.48)
	Bladex.AddAnmLStep("Tkn_g_26",0.682)
	Bladex.AddAnmLRelease("Tkn_g_26",0.79)
	Bladex.AddAnmLStep("Tkn_g_26",0.885)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_27.BMV","Tkn_g_27",0)
	Bladex.AddAnmRStep("Tkn_g_27",0)
	Bladex.AddAnmLStep("Tkn_g_27",0)
	Bladex.AddAnmRRelease("Tkn_g_27",0.535)
	Bladex.AddAnmRStep("Tkn_g_27",0.653)
	Bladex.AddAnmRRelease("Tkn_g_27",0.906)
	Bladex.AddAnmRStep("Tkn_g_27",1)
	Bladex.AddAnmLRelease("Tkn_g_27",0.691)
	Bladex.AddAnmLStep("Tkn_g_27",0.873)


	anm_name="Tkn_g_31"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_31.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.283)
	Bladex.AddAnmRStep(anm_name,0.383)
	Bladex.AddAnmRRelease(anm_name,0.544)
	Bladex.AddAnmRStep(anm_name,0.597)
	Bladex.AddAnmLRelease(anm_name,0.010)
	Bladex.AddAnmLStep(anm_name,0.257)
	Bladex.AddAnmLRelease(anm_name,0.51)
	Bladex.AddAnmLStep(anm_name,0.597)

	#
	#
	#
	#
	#
	#

	#
	# Ataques : coje los del caballero normal
	#

	anm_name="Tkn_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.186)
	Bladex.AddAnmRStep(anm_name,0.586)
	Bladex.AddAnmLRelease(anm_name,0.555)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.565)
	Bladex.AddAnmLRelease(anm_name,0.135)
	Bladex.AddAnmLStep(anm_name,0.594)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)


	anm_name="Tkn_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.511)
	Bladex.AddAnmLRelease(anm_name,0.055)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.506)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.684)
	Bladex.AddAnmLRelease(anm_name,0.115)
	Bladex.AddAnmLStep(anm_name,0.575)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)



	#anm_name="Tkn_d_b"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.125)
	#Bladex.AddAnmRStep(anm_name,0.417)
	#Bladex.AddAnmLRelease(anm_name,0.333)
	#Bladex.AddAnmLStep(anm_name,0.583)
	#Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)


	anm_name="Tkn_d_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.173)
	Bladex.AddAnmRStep(anm_name,0.693)
	Bladex.AddAnmLRelease(anm_name,0.560)
	Bladex.AddAnmLStep(anm_name,1)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)


	anm_name="Tkn_d_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.333)
	Bladex.AddAnmRStep(anm_name,0.678)
	Bladex.AddAnmLRelease(anm_name,0.125)
	Bladex.AddAnmLStep(anm_name,0.435)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)


	anm_name="Tkn_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.186)
	Bladex.AddAnmRStep(anm_name,0.586)
	Bladex.AddAnmLRelease(anm_name,0.555)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.565)
	Bladex.AddAnmLRelease(anm_name,0.135)
	Bladex.AddAnmLStep(anm_name,0.594)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.182)
	Bladex.AddAnmRStep(anm_name,0.594)
	Bladex.AddAnmLRelease(anm_name,0.645)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.505)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.101)
	Bladex.AddAnmLStep(anm_name,0.570)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_rlx_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_rlx_f_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

#	anm_name="Tkn_attack_rlx_s"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_rlx_s.BMV",anm_name,1,"Knight_Traitor")
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)



	#####Burlas######
	anm_name="Tkn_laugh"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)

	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)


	anm_name="Tkn_insult"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_insult.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_look_around"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_look_around.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_fury"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	#anm_name="Tkn_scape01"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0.31)
	#Bladex.AddAnmLStep(anm_name,0.44)
	#Bladex.AddAnmRRelease(anm_name,0.56)
	#Bladex.AddAnmLRelease(anm_name,0.62)
	#Bladex.AddAnmRStep(anm_name,0.64)
	#Bladex.AddAnmLStep(anm_name,0.75)
	#Bladex.AddAnmRRelease(anm_name,0.80)
	#Bladex.AddAnmLRelease(anm_name,0.94)
	#Bladex.AddAnmRStep(anm_name,0.97)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)

	anm_name="Tkn_attack_look"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.05)
	Bladex.AddAnmLStep(anm_name,0.1)
	Bladex.AddAnmRRelease(anm_name,0.47)
	Bladex.AddAnmRStep(anm_name,0.62)
	#Bladex.AddBipedAction("Knight",anm_name[4:],anm_name,0.0,1.0,0)


	#
	# Slip
	#
	anm_name="Tkn_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Tkn_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Tkn_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	#
	# Bowing
	#
	anm_name="Tkn_b1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_b1.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Tkn_b2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_b2.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Tkn_b3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_b3.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)



	anm_name="Tkn_sword_reaction"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.238)
	Bladex.AddAnmRStep(anm_name,0.332)
	Bladex.AddAnmRRelease(anm_name,0.529)
	Bladex.AddAnmRStep(anm_name,0.667)
	Bladex.AddAnmLRelease(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.497)
	Bladex.AddAnmLRelease(anm_name,0.537)
	Bladex.AddAnmLStep(anm_name,0.697)



##### CAMBIAR ARMAS

	anm_name="Tkn_attack_chg_r_l"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_chg_r_l.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)

##### BEBER

	anm_name="Tkn_attack_drink"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_drink.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)



####
# Heridas sin movimiento
####


	anm_name="Tkn_hurt_f_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_back.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_f_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_arm.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_f_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_breast.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_f_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_head.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_f_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_leg.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	#anm_name="Kgt_hurt_f_neck"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0.000)
	#Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_f_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_arm.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_f_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_leg.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_head.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	#Bladex.AddAnmRRelease(anm_name,0.140)
	#Bladex.AddAnmRStep(anm_name,0.382)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_l_arm.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_l_leg.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	#anm_name="Kgt_hurt_neck"
	#Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_neck.BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0.000)
	#Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_r_arm.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_r_leg.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	#anm_name="Kgt_hurt0"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0.000)
	#Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_back.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_hurt_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_breast.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)



	anm_name="Tkn_hurt_jog"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_jog.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.21)
	Bladex.AddAnmRRelease(anm_name,0.36)
	Bladex.AddAnmRStep(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.07)
	Bladex.AddAnmLStep(anm_name,0.4)
	Bladex.AddAnmLRelease(anm_name,0.58)
	Bladex.AddAnmLStep(anm_name,0.8)


	anm_name="Tkn_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_big.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.4)
	Bladex.AddAnmRStep(anm_name,0.6)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.27)
	Bladex.AddAnmLStep(anm_name,0.43)


	anm_name="Tkn_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_lite.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.35)
	Bladex.AddAnmRStep(anm_name,0.59)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,1.0)


	anm_name="Tkn_df_01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_01.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)

	anm_name="Tkn_df_02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_02.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.310)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmRStep(anm_name,0.569)
	Bladex.AddAnmLStep(anm_name,0.832)

	anm_name="Tkn_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_s_broken.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.439)
	Bladex.AddAnmRStep(anm_name,595)
	Bladex.AddAnmLRelease(anm_name,0.708)
	Bladex.AddAnmLStep(anm_name,0.867)

	#anm_name="Tkn_sword_broken"
	#Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Knight_Traitor")
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.238)
	#Bladex.AddAnmRStep(anm_name,0.332)
	#Bladex.AddAnmRRelease(anm_name,0.529)
	#Bladex.AddAnmRStep(anm_name,0.667)
	#Bladex.AddAnmLRelease(anm_name,0.333)
	#Bladex.AddAnmLStep(anm_name,0.497)
	#Bladex.AddAnmLRelease(anm_name,0.537)
	#Bladex.AddAnmLStep(anm_name,0.697)



	#################
	#
	# Muertes (me voy a suicidar, como siga esto asi. No hay derecho)
	#
	##################





	anm_name="Tkn_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth0.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.083)   # Added.
	Bladex.AddAnmRStep(anm_name,0.205)      #
	Bladex.AddAnmRRelease(anm_name,0.604)   #
	Bladex.AddAnmRStep(anm_name,0.872)      #
	Bladex.AddAnmLRelease(anm_name,0.178)   #
	Bladex.AddAnmLStep(anm_name,0.508)      #
	Bladex.AddAnmLRelease(anm_name,0.641)   #
	Bladex.AddAnmLStep(anm_name,0.896)      #   -LeadHead

	anm_name="Tkn_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c1.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)
 	Bladex.AddAnmLRelease(anm_name,0.745)  # Added.
	Bladex.AddAnmRRelease(anm_name,0.789)  #
	Bladex.AddAnmLStep(anm_name,0.883)     #
	Bladex.AddAnmRStep(anm_name,0.908)     #    -LeadHead    

	anm_name="Tkn_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c2.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)

	anm_name="Tkn_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c3.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)


	anm_name="Tkn_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c4.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.277)
	Bladex.AddAnmRStep(anm_name,0.407)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.079)
	Bladex.AddAnmLStep(anm_name,0.242)
	Bladex.AddAnmLRelease(anm_name,0.418)
	Bladex.AddAnmLStep(anm_name,0.524)
	Bladex.AddAnmLRelease(anm_name,0.645)
	Bladex.AddAnmLStep(anm_name,0.796)


	anm_name="Tkn_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c5.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.507)
	Bladex.AddAnmRStep(anm_name,0.591)
	Bladex.AddAnmRRelease(anm_name,0.667)
	Bladex.AddAnmRStep(anm_name,0.898)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.521)
	Bladex.AddAnmLStep(anm_name,0.593)
	Bladex.AddAnmLRelease(anm_name,0.659)
	Bladex.AddAnmLStep(anm_name,0.917)


	anm_name="Tkn_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c6.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.086)
	Bladex.AddAnmRStep(anm_name,0.134)
	Bladex.AddAnmRRelease(anm_name,0.249)
	Bladex.AddAnmRStep(anm_name,0.343)
	Bladex.AddAnmRRelease(anm_name,0.484)
	Bladex.AddAnmRStep(anm_name,0.536)
	Bladex.AddAnmRRelease(anm_name,0.729)
	Bladex.AddAnmRStep(anm_name,0.838)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.151)
	Bladex.AddAnmLStep(anm_name,0.234)
	Bladex.AddAnmLRelease(anm_name,0.357)
	Bladex.AddAnmLStep(anm_name,0.441)
	Bladex.AddAnmLRelease(anm_name,0.558)
	Bladex.AddAnmLStep(anm_name,0.607)
	Bladex.AddAnmLRelease(anm_name,0.746)
	Bladex.AddAnmLStep(anm_name,0.845)


	anm_name="Tkn_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)


	anm_name="Tkn_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n00.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)


	anm_name="Tkn_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n01.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.500)
	Bladex.AddAnmRStep(anm_name,0.761)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.081)
	Bladex.AddAnmLStep(anm_name,0.356)
	Bladex.AddAnmLRelease(anm_name,0.428)
	Bladex.AddAnmLStep(anm_name,0.515)
	Bladex.AddAnmLRelease(anm_name,0.617)
	Bladex.AddAnmLStep(anm_name,0.772)


	anm_name="Tkn_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n02.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)


	anm_name="Tkn_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n03.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)


	anm_name="Tkn_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n04.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.154)
	Bladex.AddAnmRStep(anm_name,0.198)
	Bladex.AddAnmRRelease(anm_name,0.290)
	Bladex.AddAnmRStep(anm_name,0.347)
	Bladex.AddAnmRRelease(anm_name,0.557)
	Bladex.AddAnmRStep(anm_name,0.595)
	Bladex.AddAnmRRelease(anm_name,0.743)
	Bladex.AddAnmRStep(anm_name,0.838)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.046)
	Bladex.AddAnmLStep(anm_name,0.069)
	Bladex.AddAnmLRelease(anm_name,0.223)
	Bladex.AddAnmLStep(anm_name,0.295)
	Bladex.AddAnmLRelease(anm_name,0.417)
	Bladex.AddAnmLStep(anm_name,0.479)
	Bladex.AddAnmLRelease(anm_name,0.592)
	Bladex.AddAnmLStep(anm_name,0.728)
	Bladex.AddAnmLRelease(anm_name,0.747)
	Bladex.AddAnmLStep(anm_name,0.886)


	anm_name="Tkn_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n05.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)


	anm_name="Tkn_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.303)
	Bladex.AddAnmRStep(anm_name,0.469)
	Bladex.AddAnmRRelease(anm_name,0.497)
	Bladex.AddAnmRStep(anm_name,0.627)
	Bladex.AddAnmRRelease(anm_name,0.709)
	Bladex.AddAnmRStep(anm_name,0.832)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.100)
	Bladex.AddAnmLStep(anm_name,0.305)
	Bladex.AddAnmLRelease(anm_name,0.347)
	Bladex.AddAnmLStep(anm_name,0.417)
	Bladex.AddAnmLRelease(anm_name,0.474)
	Bladex.AddAnmLStep(anm_name,0.690)

	anm_name="Tkn_dth_burn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_burn.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.089)
	Bladex.AddAnmRStep(anm_name,0.119)
	Bladex.AddAnmRRelease(anm_name,0.203)
	Bladex.AddAnmRStep(anm_name,0.242)
	Bladex.AddAnmRRelease(anm_name,0.284)
	Bladex.AddAnmRStep(anm_name,0.330)
	Bladex.AddAnmRRelease(anm_name,0.378)
	Bladex.AddAnmRStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.467)
	Bladex.AddAnmRStep(anm_name,0.486)
	Bladex.AddAnmRRelease(anm_name,0.539)
	Bladex.AddAnmRStep(anm_name,0.570)
	Bladex.AddAnmRRelease(anm_name,0.671)
	Bladex.AddAnmRStep(anm_name,0.715)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.046)
	Bladex.AddAnmLStep(anm_name,0.075)
	Bladex.AddAnmLRelease(anm_name,0.145)
	Bladex.AddAnmLStep(anm_name,0.185)
	Bladex.AddAnmLRelease(anm_name,0.256)
	Bladex.AddAnmLStep(anm_name,0.278)
	Bladex.AddAnmLRelease(anm_name,0.411)
	Bladex.AddAnmLStep(anm_name,0.463)
	Bladex.AddAnmLRelease(anm_name,0.563)
	Bladex.AddAnmLStep(anm_name,0.599)
	Bladex.AddAnmLRelease(anm_name,0.627)
	Bladex.AddAnmLStep(anm_name,0.667)
	Bladex.AddAnmLRelease(anm_name,0.678)
	Bladex.AddAnmLStep(anm_name,0.713)


	anm_name="Tkn_dth_rock"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rock.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_dth_rockfront"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rockfront.BMV",anm_name,0,"Knight_Traitor")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.348)
	Bladex.AddAnmRStep(anm_name,0.796)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.335)
	Bladex.AddAnmLStep(anm_name,0.792)



#### BURLAS


	anm_name="Tkn_fury"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_fury.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_laugh"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_laugh.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Tkn_alarm02"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_alarm02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	Bladex.LoadSampledAnimation("../../Anm/Tkn_alarm01.BMV","Tkn_alarm01",0)
	Bladex.AddAnmRStep("Tkn_alarm01",0.0)
	Bladex.AddAnmLStep("Tkn_alarm01",0.0)
	Bladex.AddAnmLRelease("Tkn_alarm01",0.265)
	Bladex.AddAnmLStep("Tkn_alarm01",0.420)