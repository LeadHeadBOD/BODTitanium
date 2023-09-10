##///
##||| RGNANIMATIONSET.PY TITANIUM
##||| Change list:
##||| * Added steps for dth anims that were missing them.
##\\\ 

import Bladex
import Enm_Def



def LoadRgnAnimationSet(ct_name):

	print "Loading Ragnar's animation sets..."

	#### Relax ####
	#Bladex.AddAnimFlags("Rgn_rlx",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)

	#Bladex.LoadSampledAnimation("../../Anm/Rgn_rlx_1h.BMV","Rlx_no_Rgn",1)
	#Bladex.AddAnmRStep("Rlx_no_Rgn",0.0)
	#Bladex.AddAnmLStep("Rlx_no_Rgn",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Rgn_rlx_1h.BMV","Rlx_1h_Rgn",1)
	Bladex.AddAnmRStep("Rlx_1h_Rgn",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Rgn",0.0)

	#Bladex.LoadSampledAnimation("../../Anm/Rgn_rlx_b.BMV","Rlx_b_Rgn",1)
	#Bladex.AddAnmRStep("Rlx_b_Rgn",0.0)
	#Bladex.AddAnmLStep("Rlx_b_Rgn",0.0)

	### CORRER   ####


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_jog_no.BMV","Jog_no_Rgn",1)
	#Bladex.AddAnmRStep("Jog_no_Rgn",0.0)
	#Bladex.AddAnmLStep("Jog_no_Rgn",0.42)
	#Bladex.AddAnmRRelease("Jog_no_Rgn",0.32)
	#Bladex.AddAnmRStep("Jog_no_Rgn",0.93)
	#Bladex.AddAnmLRelease("Jog_no_Rgn",0.81)
	#Bladex.AddStopTests("Jog_no_Rgn")

	Bladex.LoadSampledAnimation("../../Anm/Tkn_jog_1h.BMV","Jog_1h_Rgn",1)
	Bladex.AddAnmRStep("Jog_1h_Rgn",0.00)
	Bladex.AddAnmLStep("Jog_1h_Rgn",0.511)
	Bladex.AddAnmRStep("Jog_1h_Rgn",1.00)
	Bladex.AddAnmRRelease("Jog_1h_Rgn",0.308)
	Bladex.AddAnmLRelease("Jog_1h_Rgn",0.794)
	Bladex.AddAnmEvent("Jog_1h_Rgn","StopTest",0.20)
	Bladex.AddAnmEvent("Jog_1h_Rgn","StopTest",0.7)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_jog_1h.BMV","Jog_1h_Rgn",4)
	#Bladex.AddAnmLStep("Jog_1h_Rgn",0.0)
	#Bladex.AddAnmLRelease("Jog_1h_Rgn",0.228)
	#Bladex.AddAnmLStep("Jog_1h_Rgn",0.765)
	#Bladex.AddAnmRStep("Jog_1h_Rgn",0.309)
	#Bladex.AddAnmRRelease("Jog_1h_Rgn",0.784)
	#Bladex.AddStopTests("Jog_1h_Rgn")

	#Bladex.CreateFCAnimation("../../Anm/Rgn_jog_b.BMV","Jog_b_Rgn",4)
	#Bladex.AddAnmLStep("Jog_b_Rgn",0.055)
	#Bladex.AddAnmLRelease("Jog_b_Rgn",0.201)
	#Bladex.AddAnmLStep("Jog_b_Rgn",0.535)
	#Bladex.AddAnmLRelease("Jog_b_Rgn",0.734)
	#Bladex.AddAnmRStep("Jog_b_Rgn",0.0)
	#Bladex.AddAnmRRelease("Jog_b_Rgn",0.033)
	#Bladex.AddAnmRStep("Jog_b_Rgn",0.346)
	#Bladex.AddAnmRRelease("Jog_b_Rgn",0.51)
	#Bladex.AddAnmRStep("Jog_b_Rgn",0.83)
	#Bladex.AddStopTests("Jog_b_Rgn")

	### SNEAK   ####
	#Bladex.CreateFCAnimation("../../Anm/Rgn_snk_no.BMV","Snk_no_Rgn",4)
	#Bladex.AddAnmRStep("Snk_no_Rgn",0.0)
	#Bladex.AddAnmLStep("Snk_no_Rgn",0.485)
	#Bladex.AddAnmRStep("Snk_no_Rgn",1.0)
	#Bladex.AddAnmRRelease("Snk_no_Rgn",0.543)
	#Bladex.AddAnmLRelease("Snk_no_Rgn",0.627)
	#Bladex.AddAnmEvent("Snk_no_Rgn","StopTest",0.20)
	#Bladex.AddAnmEvent("Snk_no_Rgn","StopTest",0.7)

	#Bladex.CreateFCAnimation("../../Anm/Rgn_snk_1h.BMV","Snk_1h_Rgn",4)
	#Bladex.AddAnmRStep("Snk_1h_Rgn",0.000)
	#Bladex.AddAnmLRelease("Snk_1h_Rgn",0.005)
	#Bladex.AddAnmRStep("Snk_1h_Rgn",1.000)
	#Bladex.AddAnmLStep("Snk_1h_Rgn",0.500)
	#Bladex.AddAnmRRelease("Snk_1h_Rgn",0.500)
	#Bladex.AddAnmEvent("Snk_1h_Rgn","StopTest",0.20)
	#Bladex.AddAnmEvent("Snk_1h_Rgn","StopTest",0.7)

	#Bladex.CreateFCAnimation("../../Anm/Rgn_snk_b.BMV","Snk_b_Rgn",4)
	#Bladex.AddAnmRStep("Snk_b_Rgn",0.0)
	#Bladex.AddAnmLStep("Snk_b_Rgn",0.509)
	#Bladex.AddAnmRStep("Snk_b_Rgn",1.0)
	#Bladex.AddAnmRRelease("Snk_b_Rgn",0.608)
	#Bladex.AddAnmLRelease("Snk_b_Rgn",0.052)
	#Bladex.AddAnmEvent("Snk_b_Rgn","StopTest",0.20)
	#Bladex.AddAnmEvent("Snk_b_Rgn","StopTest",0.7)


	####  WBK ####
	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_1h.BMV","Wbk_1h_Rgn",1,"Ragnar")
	Bladex.AddAnmLStep("Wbk_1h_Rgn",0.0)
	Bladex.AddAnmRStep("Wbk_1h_Rgn",0.5)
	Bladex.AddAnmLStep("Wbk_1h_Rgn",1.0)
	Bladex.AddAnmLRelease("Wbk_1h_Rgn",0.5)
	Bladex.AddAnmRRelease("Wbk_1h_Rgn",1.0)
	Bladex.AddStopTests("Wbk_1h_Rgn")



	#
	#### Caminar ####
	#


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_Wlk_no.BMV","Wlk_no_Rgn",1)

	#Bladex.AddAnmRStep("Wlk_no_Rgn",0.1)
	#Bladex.AddAnmLStep("Wlk_no_Rgn",0.0)
	#Bladex.AddAnmRRelease("Wlk_no_Rgn",0.67)
	#Bladex.AddAnmLRelease("Wlk_no_Rgn",0.21)
	#Bladex.AddAnmLStep("Wlk_no_Rgn",0.52)
	#Bladex.AddStopTests("Wlk_no_Rgn")




	Bladex.LoadSampledAnimation("../../Anm/Rgn_wlk_1h.BMV","Wlk_1h_Rgn",1)

	Bladex.AddAnmRStep("Wlk_1h_Rgn",0.1)
	Bladex.AddAnmRRelease("Wlk_1h_Rgn",0.6)
	Bladex.AddAnmLStep("Wlk_1h_Rgn",0.0)
	Bladex.AddAnmLRelease("Wlk_1h_Rgn",0.14)
	Bladex.AddAnmLStep("Wlk_1h_Rgn",0.55)
	Bladex.AddAnmEvent("Wlk_1h_Rgn","StopTest",0.20)
	Bladex.AddAnmEvent("Wlk_1h_Rgn","StopTest",0.7)



	#
	# End caminar
	#


	#Bladex.CreateFCAnimation("../../Anm/Rgn_wlk_short_no.BMV","WlkShort_Rgn",4)

	#Bladex.AddAnmRStep("WlkShort_Rgn",0.0)
	#Bladex.AddAnmLStep("WlkShort_Rgn",0.5)
	#Bladex.AddAnmRStep("WlkShort_Rgn",1.0)
	#Bladex.AddAnmRRelease("WlkShort_Rgn",0.5)
	#Bladex.AddAnmLRelease("WlkShort_Rgn",1.0)

	#Bladex.AddAnmEvent("WlkShort_Rgn","StopTest",0.20)
	#Bladex.AddAnmEvent("WlkShort_Rgn","StopTest",0.7)

	#### Escalones ####

	#Bladex.LoadSampledAnimation("../../Anm/Rgn_wlk_up.BMV","WlkUp_Rgn",1)

	#Bladex.CreateDFCAnimation("../../Anm/Rgn_wlk_up.BMV","../../Anm/Rgn_wlk_no.BMV","WlkUp_Rgn",4)
	#Bladex.CreateDFCAnimation("../../Anm/Rgn_wlk_down.BMV","../../Anm/Rgn_wlk_no.BMV","WlkDown_Rgn",4)

	#Bladex.CreateFCAnimation("../../Anm/Rgn_stairs_u_no.BMV","StairsUp_Rgn",4)
	#Bladex.CreateDFCAnimation("../../Anm/Rgn_stairs_u_no_mas.BMV","../../Anm/Rgn_stairs_u_no.BMV","StairsUpP_Rgn",4)

	#Bladex.CreateFCAnimation("../../Anm/Rgn_stairs_d_no.BMV","StairsDown_Rgn",4)

	#Bladex.AddAnmRStep("StairsUp_Rgn",0.0)
	#Bladex.AddAnmLStep("StairsUp_Rgn",0.5)
	#Bladex.AddAnmRStep("StairsUp_Rgn",1.0)
	#Bladex.AddAnmRRelease("StairsUp_Rgn",0.5)
	#Bladex.AddAnmLRelease("StairsUp_Rgn",1.0)

	#### Caidas ####


	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_med_no.BMV","FallMed_Rgn",0,"Ragnar")
	Bladex.AddAnmRStep("FallMed_Rgn",0.0)
	Bladex.AddAnmLStep("FallMed_Rgn",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_low_no.BMV","FallLow_Rgn",0,"Ragnar")
	Bladex.AddAnmRStep("FallLow_Rgn",0.0)
	Bladex.AddAnmLStep("FallLow_Rgn",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_high_no.BMV","FallHigh_Rgn",0)
	Bladex.AddAnmRStep("FallHigh_Rgn",0.0)
	Bladex.AddAnmLStep("FallHigh_Rgn",0.0)

#	#Caida enorme
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Rgn",0,"Ragnar")
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Rgn",0,"Ragnar")
	#
	# Ataques
	#


	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_01.BMV","Rgn_g_01",0)
	Bladex.AddAnmRStep("Rgn_g_01",0)
	Bladex.AddAnmLStep("Rgn_g_01",0)
	Bladex.AddAnmRRelease("Rgn_g_01",0.11)
	Bladex.AddAnmRStep("Rgn_g_01",0.33)
	Bladex.AddAnmRRelease("Rgn_g_01",0.62)
	Bladex.AddAnmRStep("Rgn_g_01",0.81)



	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_02.BMV","Rgn_g_02",0)
	Bladex.AddAnmRStep("Rgn_g_02",0)
	Bladex.AddAnmLStep("Rgn_g_02",0)
	Bladex.AddAnmRRelease("Rgn_g_02",0.12)
	Bladex.AddAnmRStep("Rgn_g_02",0.33)
	Bladex.AddAnmRRelease("Rgn_g_02",0.62)
	Bladex.AddAnmRStep("Rgn_g_02",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_03.BMV","Rgn_g_03",0)
	Bladex.AddAnmRStep("Rgn_g_03",0)
	Bladex.AddAnmLStep("Rgn_g_03",0)
	Bladex.AddAnmRRelease("Rgn_g_03",0.10)
	Bladex.AddAnmRStep("Rgn_g_03",0.28)
	Bladex.AddAnmRRelease("Rgn_g_03",0.60)
	Bladex.AddAnmRStep("Rgn_g_03",0.84)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_06.BMV","Rgn_g_06",0)
	#Bladex.AddAnmRStep("Rgn_g_06",0)
	#Bladex.AddAnmLStep("Rgn_g_06",0)
	#Bladex.AddAnmRRelease("Rgn_g_06",0.153)
	#Bladex.AddAnmRStep("Rgn_g_06",0.372)
	#Bladex.AddAnmRRelease("Rgn_g_06",0.554)
	#Bladex.AddAnmRStep("Rgn_g_06",0.788)


	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_07.BMV","Rgn_g_07",0)
	Bladex.AddAnmRStep("Rgn_g_07",0)
	Bladex.AddAnmLStep("Rgn_g_07",0)
	Bladex.AddAnmRRelease("Rgn_g_07",0.10)
	Bladex.AddAnmRStep("Rgn_g_07",0.28)
	Bladex.AddAnmRRelease("Rgn_g_07",0.60)
	Bladex.AddAnmRStep("Rgn_g_07",0.76)

	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_08.BMV","Rgn_g_08",0)
	#Bladex.AddAnmRStep("Rgn_g_08",0)
	#Bladex.AddAnmLStep("Rgn_g_08",0)
	#Bladex.AddAnmRRelease("Rgn_g_08",0.062)
	#Bladex.AddAnmRStep("Rgn_g_08",0.259)
	#Bladex.AddAnmRRelease("Rgn_g_08",0.478)
	#Bladex.AddAnmRStep("Rgn_g_08",0.589)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_09.BMV","Rgn_g_09",0)
	#Bladex.AddAnmRStep("Rgn_g_09",0)
	#Bladex.AddAnmLStep("Rgn_g_09",0)
	#Bladex.AddAnmRRelease("Rgn_g_09",0.23)
	#Bladex.AddAnmRStep("Rgn_g_09",0.36)
	#Bladex.AddAnmRRelease("Rgn_g_09",0.55)
	#Bladex.AddAnmRStep("Rgn_g_09",0.71)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_12.BMV","Rgn_g_12",0)
	#Bladex.AddAnmRStep("Rgn_g_13",0)
	#Bladex.AddAnmLStep("Rgn_g_13",0)
	#Bladex.AddAnmRRelease("Rgn_g_13",0.28)
	#Bladex.AddAnmRStep("Rgn_g_13",0.41)
	#Bladex.AddAnmLRelease("Rgn_g_13",0.46)
	#Bladex.AddAnmLStep("Rgn_g_13",0.65)
	#Bladex.AddAnmRRelease("Rgn_g_13",0.72)
	#Bladex.AddAnmRStep("Rgn_g_13",0.87)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_18.BMV","Rgn_g_18",0)
	#Bladex.AddAnmRStep("Rgn_g_18",0)
	#Bladex.AddAnmRRelease("Rgn_g_18",0.211)
	#Bladex.AddAnmRStep("Rgn_g_18",0.503)
	#Bladex.AddAnmRRelease("Rgn_g_18",0.730)
	#Bladex.AddAnmRStep("Rgn_g_18",0.894)
	#Bladex.AddAnmLStep("Rgn_g_18",0)
	#Bladex.AddAnmLRelease("Rgn_g_18",0.091)
	#Bladex.AddAnmLStep("Rgn_g_18",0.207)
	#Bladex.AddAnmLRelease("Rgn_g_18",0.308)
	#Bladex.AddAnmLStep("Rgn_g_18",0.48)
	#Bladex.AddAnmLRelease("Rgn_g_18",0.793)
	#Bladex.AddAnmLStep("Rgn_g_18",0.841)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_14.BMV","Rgn_g_14",0)
	#Bladex.AddAnmRStep("Rgn_g_14",0)
	#Bladex.AddAnmLStep("Rgn_g_14",0)
	#Bladex.AddAnmLRelease("Rgn_g_14",0.15)
	#Bladex.AddAnmLStep("Rgn_g_14",0.37)
	#Bladex.AddAnmRRelease("Rgn_g_14",0.43)
	#Bladex.AddAnmRStep("Rgn_g_14",0.56)
	#Bladex.AddAnmLRelease("Rgn_g_14",0.73)
	#Bladex.AddAnmLStep("Rgn_g_14",0.85)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_11.BMV","Rgn_g_11",0)
	#Bladex.AddAnmRStep("Rgn_g_11",0)
	#Bladex.AddAnmLStep("Rgn_g_11",0)
	#Bladex.AddAnmRRelease("Rgn_g_11",0.4)
	#Bladex.AddAnmRStep("Rgn_g_11",0.55)
	#Bladex.AddAnmLRelease("Rgn_g_11",0.78)
	#Bladex.AddAnmLStep("Rgn_g_11",0.93)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_16.BMV","Rgn_g_16",0)
	#Bladex.AddAnmRStep("Rgn_g_16",0)
	#Bladex.AddAnmLStep("Rgn_g_16",0)
	#Bladex.AddAnmRRelease("Rgn_g_16",0.16)
	#Bladex.AddAnmRStep("Rgn_g_16",0.275)
	#Bladex.AddAnmLRelease("Rgn_g_16",0.54)
	#Bladex.AddAnmLStep("Rgn_g_16",0.675)



	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_17.BMV","Rgn_g_17",0)
	Bladex.AddAnmRStep("Rgn_g_17",0)
	Bladex.AddAnmLStep("Rgn_g_17",0)
	Bladex.AddAnmRRelease("Rgn_g_17",0.10)
	Bladex.AddAnmRStep("Rgn_g_17",0.27)
	Bladex.AddAnmRRelease("Rgn_g_17",0.65)
	Bladex.AddAnmRStep("Rgn_g_17",0.85)
	Bladex.AddAnmLRelease("Rgn_g_17",0.69)
	Bladex.AddAnmLStep("Rgn_g_17",0.81)



	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_15.BMV","Rgn_g_15",0)
	#Bladex.AddAnmRRelease("Rgn_g_15",0.09)
	#Bladex.AddAnmRStep("Rgn_g_15",0.3)
	#Bladex.AddAnmLRelease("Rgn_g_15",0.32)
	#Bladex.AddAnmRRelease("Rgn_g_15",0.364)
	#Bladex.AddAnmRStep("Rgn_g_15",0.551)
	#Bladex.AddAnmLStep("Rgn_g_15",0.592)


	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_21.BMV","Rgn_g_21",0)
	Bladex.AddAnmRStep("Rgn_g_21",0)
	Bladex.AddAnmLStep("Rgn_g_21",0)
	Bladex.AddAnmRRelease("Rgn_g_21",0.11)
	Bladex.AddAnmRStep("Rgn_g_21",0.28)
	Bladex.AddAnmRRelease("Rgn_g_21",0.65)
	Bladex.AddAnmRStep("Rgn_g_21",0.78)
	Bladex.AddAnmLRelease("Rgn_g_21",0.71)
	Bladex.AddAnmLStep("Rgn_g_21",0.79)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_22.BMV","Rgn_g_22",0)
	#Bladex.AddAnmRStep("Rgn_g_22",0)
	#Bladex.AddAnmLStep("Rgn_g_22",0)
	#Bladex.AddAnmRRelease("Rgn_g_22",0.474)
	#Bladex.AddAnmRStep("Rgn_g_22",0.544)
	#Bladex.AddAnmRRelease("Rgn_g_22",0.605)
	#Bladex.AddAnmRStep("Rgn_g_22",0.67)
	#Bladex.AddAnmRRelease("Rgn_g_22",0.781)
	#Bladex.AddAnmRStep("Rgn_g_22",0.847)
	#Bladex.AddAnmLRelease("Rgn_g_22",0.2)
	#Bladex.AddAnmLStep("Rgn_g_22",0.433)
	#Bladex.AddAnmLRelease("Rgn_g_22",0.549)
	#Bladex.AddAnmLStep("Rgn_g_22",0.6)


	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_d_l.BMV","Rgn_g_d_l",0)
	Bladex.AddAnmRStep("Rgn_g_d_l",0)
	Bladex.AddAnmLStep("Rgn_g_d_l",0)
	Bladex.AddAnmRRelease("Rgn_g_d_l",0.21)
	Bladex.AddAnmRStep("Rgn_g_d_l",0.53)
	Bladex.AddAnmRRelease("Rgn_g_d_l",0.86)
	Bladex.AddAnmRStep("Rgn_g_d_l",0.99)
	Bladex.AddAnmLRelease("Rgn_g_d_l",0.12)
	Bladex.AddAnmLStep("Rgn_g_d_l",0.29)

	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_d_r.BMV","Rgn_g_d_r",0)
	Bladex.AddAnmRStep("Rgn_g_d_r",0)
	Bladex.AddAnmLStep("Rgn_g_d_r",0)
	Bladex.AddAnmRRelease("Rgn_g_d_r",0.11)
	Bladex.AddAnmRStep("Rgn_g_d_r",0.36)
	Bladex.AddAnmRRelease("Rgn_g_d_r",0.50)
	Bladex.AddAnmRStep("Rgn_g_d_r",0.65)
	Bladex.AddAnmRRelease("Rgn_g_d_r",0.91)
	Bladex.AddAnmRStep("Rgn_g_d_r",0.99)
	Bladex.AddAnmLRelease("Rgn_g_d_r",0.25)
	Bladex.AddAnmLStep("Rgn_g_d_r",0.46)

	Bladex.LoadSampledAnimation("../../Anm/Rgn_g_escape.BMV","Rgn_g_escape",0)
	Bladex.AddAnmRStep("Rgn_g_d_l",0)
	Bladex.AddAnmLStep("Rgn_g_d_l",0)
	Bladex.AddAnmRRelease("Rgn_g_d_l",0.28)
	Bladex.AddAnmRStep("Rgn_g_d_l",0.45)
	Bladex.AddAnmLRelease("Rgn_g_d_l",0.17)
	Bladex.AddAnmLStep("Rgn_g_d_l",0.48)

	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_26.BMV","Rgn_g_26",0)
	#Bladex.AddAnmRStep("Rgn_g_26",0)
	#Bladex.AddAnmLStep("Rgn_g_26",0)
	#Bladex.AddAnmRRelease("Rgn_g_26",0.135)
	#Bladex.AddAnmRStep("Rgn_g_26",0.236)
	#Bladex.AddAnmLRelease("Rgn_g_26",0.48)
	#Bladex.AddAnmLStep("Rgn_g_26",0.682)
	#Bladex.AddAnmLRelease("Rgn_g_26",0.79)
	#Bladex.AddAnmLStep("Rgn_g_26",0.885)


	#Bladex.LoadSampledAnimation("../../Anm/Rgn_g_27.BMV","Rgn_g_27",0)
	#Bladex.AddAnmRStep("Rgn_g_27",0)
	#Bladex.AddAnmLStep("Rgn_g_27",0)
	#Bladex.AddAnmRRelease("Rgn_g_27",0.28)
	#Bladex.AddAnmRStep("Rgn_g_27",0.5)
	#Bladex.AddAnmLRelease("Rgn_g_27",0.72)
	#Bladex.AddAnmLStep("Rgn_g_27",0.74)

	#anm_name="Rgn_g_31"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.07)
	#Bladex.AddAnmRStep(anm_name,0.27)
	#Bladex.AddAnmRRelease(anm_name,0.41)
	#Bladex.AddAnmRStep(anm_name,0.53)
	#Bladex.AddAnmLRelease(anm_name,0.29)
	#Bladex.AddAnmLStep(anm_name,0.42)
	#Bladex.AddAnmLRelease(anm_name,0.61)
	#Bladex.AddAnmLStep(anm_name,0.72)


	#
	# Movimientos en combate
	#
	anm_name="Rgn_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.25)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.52)
	Bladex.AddAnmRRelease(anm_name,0.78)
	Bladex.AddStopTests(anm_name)

	anm_name="Rgn_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.41)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.56)
	Bladex.AddAnmLRelease(anm_name,0.96)
	Bladex.AddStopTests(anm_name)

	anm_name="Rgn_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.34)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.66)
	Bladex.AddAnmLRelease(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Rgn_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.28)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.5)
	Bladex.AddAnmLRelease(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Rgn_d_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.59)
	Bladex.AddAnmRStep(anm_name,0.99)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,0.79)

	anm_name="Rgn_d_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.28)
	Bladex.AddAnmRStep(anm_name,0.67)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.44)
	Bladex.AddAnmLStep(anm_name,0.89)

	anm_name="Rgn_d_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.42)
	Bladex.AddAnmRStep(anm_name,0.80)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.65)
	Bladex.AddAnmLStep(anm_name,1.0)

	anm_name="Rgn_rlx_f_s"
	Bladex.LoadSampledAnimation("../../Anm/Tkn_rlx_f_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Rgn_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.52)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.11)
	Bladex.AddAnmLStep(anm_name,0.51)
	Bladex.AddStopTests(anm_name)

	anm_name="Rgn_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.13)
	Bladex.AddAnmRRelease(anm_name,0.52)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.12)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Rgn_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.34)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.66)
	Bladex.AddAnmLRelease(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Rgn_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.56)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.41)
	Bladex.AddAnmLRelease(anm_name,0.84)
	Bladex.AddStopTests(anm_name)

	#anm_name="Rgn_attack_rlx"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)

	#anm_name="Rgn_rlx_s"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)

	#anm_name="Rgn_attack_rlx_s"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)


	#anm_name="Rgn_attack_t_r"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,1)
	#Bladex.AddAnmLStep(anm_name,1)


	#anm_name="Rgn_attack_t_l"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,1)
	#Bladex.AddAnmLStep(anm_name,1)

	#anm_name="Rgn_attack_t_r_s"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)

	#anm_name="Rgn_attack_t_l_s"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)



	#
	# Saltos
	#

	#anm_name="Rgn_jmp_no"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0.10)

	#Bladex.AddAnmRStep(anm_name,0.3)
	#Bladex.AddAnmLStep(anm_name,0.3)
	##Bladex.AddAnmRStep(anm_name,0.33)
	##Bladex.AddAnmLStep(anm_name,0.34)
	#Bladex.AddAnmRRelease(anm_name,0.37)
	#Bladex.AddAnmLRelease(anm_name,0.45)
	#Bladex.AddAnmRStep(anm_name,0.49)
	#Bladex.AddAnmRRelease(anm_name,0.62)
	#Bladex.AddAnmRStep(anm_name,0.70)
	#Bladex.AddAnmLStep(anm_name,0.70)


	#anm_name="Rgn_jmp_no"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0.0)
	#Bladex.AddAnmRRelease(anm_name,0.36)
	#Bladex.AddAnmRStep(anm_name,0.55)
	#Bladex.AddAnmLStep(anm_name,0.0)
	#Bladex.AddAnmLRelease(anm_name,0.39)
	#Bladex.AddAnmLStep(anm_name,0.57)


	#anm_name="Rgn_jmp_1h"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV","Rgn_jmp_1h",0)

	#Bladex.AddAnmRStep("Rgn_jmp_1h",0.0)
	#Bladex.AddAnmRRelease("Rgn_jmp_1h",0.223)
	#Bladex.AddAnmRStep("Rgn_jmp_1h",0.466)
	#Bladex.AddAnmRRelease("Rgn_jmp_1h",0.594)
	#Bladex.AddAnmRStep("Rgn_jmp_1h",0.681)
	#Bladex.AddAnmLStep("Rgn_jmp_1h",0.0)
	#Bladex.AddAnmLRelease("Rgn_jmp_1h",0.075)
	#Bladex.AddAnmLStep("Rgn_jmp_1h",0.193)
	#Bladex.AddAnmLRelease("Rgn_jmp_1h",0.297)
	#Bladex.AddAnmLStep("Rgn_jmp_1h",0.528)
	#Bladex.AddAnmLRelease("Rgn_jmp_1h",0.688)
	#Bladex.AddAnmLStep("Rgn_jmp_1h",0.800)



	#anm_name="Rgn_jmph0_no"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.324)
	#Bladex.AddAnmLRelease(anm_name,0.532)
	#Bladex.AddAnmRStep(anm_name,0.618)
	#Bladex.AddAnmLStep(anm_name,0.843)
	#Bladex.AddStopTests(anm_name)

	#
	# Slip
	#

	anm_name="Rgn_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Rgn_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Rgn_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)



	##### Escalares


	anm_name="Rgn_clmb_low_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_low_1h.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.17)
	Bladex.AddAnmRStep(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.48)
	Bladex.AddAnmLStep(anm_name,0.82)


	anm_name="Rgn_clmb_medlow_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_medlow_1h.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.30)
	Bladex.AddAnmRStep(anm_name,0.79)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.28)
	Bladex.AddAnmLStep(anm_name,0.53)
	Bladex.AddAnmLRelease(anm_name,0.83)
	Bladex.AddAnmLStep(anm_name,0.98)


	anm_name="Rgn_clmb_medium_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_medium_1h.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.13)
	Bladex.AddAnmRStep(anm_name,0.84)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,1)


	anm_name="Rgn_clmb_high_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_high_1h.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.09)
	Bladex.AddAnmRStep(anm_name,0.88)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.09)
	Bladex.AddAnmLStep(anm_name,1.0)


	#### CAMBIAR ARMAS

	anm_name="Rgn_attack_chg_r_l"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_chg_r_l.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLStep(anm_name,0.00)


	anm_name="Rgn_attack_drink"
	Bladex.LoadSampledAnimation("../../Anm/Rgn_attack_drink.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLStep(anm_name,0.00)


	####
	# HERIDAS ya de muerte casi
	####


	anm_name="Rgn_hurt_f_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_back.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_f_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_arm.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_f_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_breast.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_f_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_head.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_f_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_leg.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_f_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_arm.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_f_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_leg.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_head.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	#Bladex.AddAnmRRelease(anm_name,0.140)
	#Bladex.AddAnmRStep(anm_name,0.382)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_l_arm.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_l_leg.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_r_arm.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_r_leg.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_back.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_breast.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_hurt_jog"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_jog.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.21)
	Bladex.AddAnmRRelease(anm_name,0.36)
	Bladex.AddAnmRStep(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.07)
	Bladex.AddAnmLStep(anm_name,0.4)
	Bladex.AddAnmLRelease(anm_name,0.58)
	Bladex.AddAnmLStep(anm_name,0.8)

	anm_name="Rgn_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_big.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.4)
	Bladex.AddAnmRStep(anm_name,0.6)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.27)
	Bladex.AddAnmLStep(anm_name,0.43)

	anm_name="Rgn_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_lite.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.35)
	Bladex.AddAnmRStep(anm_name,0.59)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,1.0)

	anm_name="Rgn_df_01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_01.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)

	anm_name="Rgn_df_02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_02.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.310)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmRStep(anm_name,0.569)
	Bladex.AddAnmLStep(anm_name,0.832)

	anm_name="Rgn_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_s_broken.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.439)
	Bladex.AddAnmRStep(anm_name,595)
	Bladex.AddAnmLRelease(anm_name,0.708)
	Bladex.AddAnmLStep(anm_name,0.867)


	anm_name="Rgn_sword_reaction"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Ragnar")
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
	Bladex.SetAnimationFactor("Tkn_sword_reaction",0.7)





	#################
	#
	# Muertes (me voy a suicidar, como siga esto asi. No hay derecho)
	#
	##################





	anm_name="Rgn_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth0.BMV",anm_name,0,"Ragnar")
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

	anm_name="Rgn_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c1.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)
 	Bladex.AddAnmLRelease(anm_name,0.745)  # Added.
	Bladex.AddAnmRRelease(anm_name,0.789)  #
	Bladex.AddAnmLStep(anm_name,0.883)     #
	Bladex.AddAnmRStep(anm_name,0.908)     #    -LeadHead

	anm_name="Rgn_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c2.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)

	anm_name="Rgn_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c3.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)


	anm_name="Rgn_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c4.BMV",anm_name,0,"Ragnar")
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


	anm_name="Rgn_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c5.BMV",anm_name,0,"Ragnar")
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


	anm_name="Rgn_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c6.BMV",anm_name,0,"Ragnar")
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


	anm_name="Rgn_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)


	anm_name="Rgn_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n00.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)


	anm_name="Rgn_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n01.BMV",anm_name,0,"Ragnar")
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


	anm_name="Rgn_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n02.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)


	anm_name="Rgn_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n03.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)


	anm_name="Rgn_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n04.BMV",anm_name,0,"Ragnar")
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


	anm_name="Rgn_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n05.BMV",anm_name,0,"Ragnar")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)


	anm_name="Rgn_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0,"Ragnar")
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

	anm_name="Rgn_dth_burn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_burn.BMV",anm_name,0,"Ragnar")
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


	#### BURLAS

	anm_name="Rgn_insult"
	Bladex.LoadSampledAnimation("../../Anm/Rgn_insult.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_laugh"
	Bladex.LoadSampledAnimation("../../Anm/Rgn_laugh.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_escape"
	Bladex.LoadSampledAnimation("../../Anm/Rgn_escape.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_escape2"
	Bladex.LoadSampledAnimation("../../Anm/Rgn_escape2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Rgn_end_ragnar_ragnar"
	Bladex.LoadSampledAnimation("../../Anm/Rgn_end_ragnar.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
