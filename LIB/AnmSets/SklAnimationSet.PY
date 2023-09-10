###///
###||| SKLANIMATIONSET.PY TITANIUM
###||| Change list:
###||| * Added skl_dth_explo
###||| * Added steps for dth anims that were missing them.
###|||
###||| Because of this, ../AnmPak/Skl.dat might need to be deleted or replaced upon installation
###\\\


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



def LoadSklAnimationSet(ct_name):

	print "Loading the Skl animation sets..."

	Bladex.LoadSampledAnimation("../../Anm/Skl_appears1.BMV","Skl_appears1",0)
	Bladex.AddAnmRStep("Skl_appears1",0)
	Bladex.AddAnmLStep("Skl_appears1",0)

	#### Relax ####
	#Bladex.AddAnimFlags("Skl_rlx",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)

#	Bladex.LoadSampledAnimation("../../Anm/Skl_rlx_no.BMV","Rlx_no_Skl",1)
#	Bladex.AddAnmRStep("Rlx_no_Skl",0.0)
#	Bladex.AddAnmLStep("Rlx_no_Skl",0.0)
#
	Bladex.LoadSampledAnimation("../../Anm/Skl_rlx_1h.BMV","Rlx_1h_Skl",1)
	Bladex.AddAnmRStep("Rlx_1h_Skl",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Skl",0.0)

#	Bladex.LoadSampledAnimation("../../Anm/Skl_rlx_b.BMV","Rlx_b_Skl",1)
#	Bladex.AddAnmRStep("Rlx_b_Skl",0.0)
#	Bladex.AddAnmLStep("Rlx_b_Skl",0.0)
#
#	### CORRER   ####
#	Bladex.CreateFCAnimation("../../Anm/Skl_jog_no.BMV","Jog_no_Skl",4)
#	Bladex.AddAnmRStep("Jog_no_Skl",0.0)
#	Bladex.AddAnmLStep("Jog_no_Skl",0.505)
#	Bladex.AddAnmRStep("Jog_no_Skl",1.0)
#	Bladex.AddAnmRRelease("Jog_no_Skl",0.266)
#	Bladex.AddAnmLRelease("Jog_no_Skl",0.783)
#	Bladex.AddAnmEvent("Jog_no_Skl","StopTest",0.20)
#	Bladex.AddAnmEvent("Jog_no_Skl","StopTest",0.7)

	Bladex.LoadSampledAnimation("../../Anm/Skl_jog_1h.BMV","Jog_1h_Skl",1)
	Bladex.AddAnmLStep("Jog_1h_Skl",0.0)
	Bladex.AddAnmLRelease("Jog_1h_Skl",0.21)
	Bladex.AddAnmLStep("Jog_1h_Skl",0.516)
	Bladex.AddAnmLRelease("Jog_1h_Skl",0.724)
	Bladex.AddAnmLStep("Jog_1h_Skl",1.0)
	Bladex.AddAnmRStep("Jog_1h_Skl",0.266)
	Bladex.AddAnmRRelease("Jog_1h_Skl",0.455)
	Bladex.AddAnmRStep("Jog_1h_Skl",0.783)
	Bladex.AddAnmRRelease("Jog_1h_Skl",0.947)
	Bladex.AddAnmEvent("Jog_1h_Skl","StopTest",0.20)
	Bladex.AddAnmEvent("Jog_1h_Skl","StopTest",0.7)
#
#	Bladex.CreateFCAnimation("../../Anm/Skl_jog_b.BMV","Jog_b_Skl",4)
#	Bladex.AddAnmLStep("Jog_b_Skl",0.055)
#	Bladex.AddAnmLRelease("Jog_b_Skl",0.201)
#	Bladex.AddAnmLStep("Jog_b_Skl",0.535)
#	Bladex.AddAnmLRelease("Jog_b_Skl",0.734)
#	Bladex.AddAnmRStep("Jog_b_Skl",0.0)
#	Bladex.AddAnmRRelease("Jog_b_Skl",0.033)
#	Bladex.AddAnmRStep("Jog_b_Skl",0.346)
#	Bladex.AddAnmRRelease("Jog_b_Skl",0.51)
#	Bladex.AddAnmRStep("Jog_b_Skl",0.83)
#	Bladex.AddAnmEvent("Jog_b_Skl","StopTest",0.20)
#	Bladex.AddAnmEvent("Jog_b_Skl","StopTest",0.7)
#
	### SNEAK   ####
	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_no.BMV","Snk_no_Skl",1,"Skeleton")
	Bladex.AddAnmRStep("Snk_no_Skl",0.0)
	Bladex.AddAnmLStep("Snk_no_Skl",0.485)
	Bladex.AddAnmRStep("Snk_no_Skl",1.0)
	Bladex.AddAnmRRelease("Snk_no_Skl",0.543)
	Bladex.AddAnmLRelease("Snk_no_Skl",0.627)
	Bladex.AddAnmEvent("Snk_no_Skl","StopTest",0.20)
	Bladex.AddAnmEvent("Snk_no_Skl","StopTest",0.7)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_1h.BMV","Snk_1h_Skl",1,"Skeleton")
	Bladex.AddAnmRStep("Snk_1h_Skl",0.000)
	Bladex.AddAnmLRelease("Snk_1h_Skl",0.005)
	Bladex.AddAnmRStep("Snk_1h_Skl",1.000)
	Bladex.AddAnmLStep("Snk_1h_Skl",0.500)
	Bladex.AddAnmRRelease("Snk_1h_Skl",0.500)
	Bladex.AddAnmEvent("Snk_1h_Skl","StopTest",0.20)
	Bladex.AddAnmEvent("Snk_1h_Skl","StopTest",0.7)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_b.BMV","Snk_b_Skl",1,"Skeleton")
	Bladex.AddAnmRStep("Snk_b_Skl",0.0)
	Bladex.AddAnmLStep("Snk_b_Skl",0.509)
	Bladex.AddAnmRStep("Snk_b_Skl",1.0)
	Bladex.AddAnmRRelease("Snk_b_Skl",0.608)
	Bladex.AddAnmLRelease("Snk_b_Skl",0.052)
	Bladex.AddAnmEvent("Snk_b_Skl","StopTest",0.20)
	Bladex.AddAnmEvent("Snk_b_Skl","StopTest",0.7)


	####  WBK ####
#	Bladex.LoadSampledAnimation("../../Anm/Skl_attack_b.BMV","Wbk_1h_Skl",1)
#	Bladex.AddAnmRStep("Wbk_1h_Skl",0.0)
#	Bladex.AddAnmRRelease("Wbk_1h_Skl",0.153)
#	Bladex.AddAnmRStep("Wbk_1h_Skl",0.270)
#	Bladex.AddAnmRRelease("Wbk_1h_Skl",0.630)
#	Bladex.AddAnmRStep("Wbk_1h_Skl",0.765)
#	Bladex.AddAnmLStep("Wbk_1h_Skl",0.00)
#	Bladex.AddAnmLRelease("Wbk_1h_Skl",0.4)
#	Bladex.AddAnmLStep("Wbk_1h_Skl",0.52)
#	Bladex.AddAnmLRelease("Wbk_1h_Skl",0.873)
#	Bladex.AddAnmLStep("Wbk_1h_Skl",1.0)
#	Bladex.AddStopTests("Wbk_1h_Skl")


	Bladex.AddAnmEvent("Wbk_1h_Skl","StopTest",0.2)
	Bladex.AddAnmEvent("Wbk_1h_Skl","StopTest",0.7)
#
#	Bladex.CreateFCAnimation("../../Anm/Skl_attack_b.BMV","Wbk_no_Skl",4)
#
#	Bladex.AddAnmRStep("Wbk_no_Skl",0.106)
#	Bladex.AddAnmRRelease("Wbk_no_Skl",0.166)
#	Bladex.AddAnmRStep("Wbk_no_Skl",0.621)
#	Bladex.AddAnmRRelease("Wbk_no_Skl",0.7)
#	Bladex.AddAnmRStep("Wbk_no_Skl",1)
#	Bladex.AddAnmLStep("Wbk_no_Skl",0)
#	Bladex.AddAnmLRelease("Wbk_no_Skl",0.046)
#	Bladex.AddAnmLStep("Wbk_no_Skl",0.345)
#	Bladex.AddAnmLRelease("Wbk_no_Skl",0.541)
#	Bladex.AddAnmLStep("Wbk_no_Skl",0.849)
#	Bladex.AddStopTests(anm_name)
#
#
#	Bladex.AddAnmEvent("Wbk_no_Skl","StopTest",0.20)
#	Bladex.AddAnmEvent("Wbk_no_Skl","StopTest",0.70)






	#
	#### Caminar ####
	#


	Bladex.LoadSampledAnimation("../../Anm/Skl_wlk_1h.BMV","Wlk_1h_Skl",1)

	Bladex.AddAnmRStep("Wlk_1h_Skl",0.0)
	Bladex.AddAnmRRelease("Wlk_1h_Skl",0.362)
	Bladex.AddAnmRStep("Wlk_1h_Skl",0.510)
	Bladex.AddAnmRRelease("Wlk_1h_Skl",0.843)
	Bladex.AddAnmRStep("Wlk_1h_Skl",1.0)
	Bladex.AddAnmLStep("Wlk_1h_Skl",0.0)
	Bladex.AddAnmLRelease("Wlk_1h_Skl",0.073)
	Bladex.AddAnmLStep("Wlk_1h_Skl",0.263)
	Bladex.AddAnmLRelease("Wlk_1h_Skl",0.616)
	Bladex.AddAnmLStep("Wlk_1h_Skl",0.768)
	Bladex.AddStopTests("Wlk_1h_Skl")



	Bladex.LoadSampledAnimation("../../Anm/Skl_wlk_b.BMV","Wlk_b_Skl",1)

	Bladex.AddAnmRStep("Wlk_b_Skl",0.0)
	Bladex.AddAnmRRelease("Wlk_b_Skl",0.380)
	Bladex.AddAnmRStep("Wlk_b_Skl",0.541)
	Bladex.AddAnmRRelease("Wlk_b_Skl",0.863)
	Bladex.AddAnmRStep("Wlk_b_Skl",1.0)
	Bladex.AddAnmLStep("Wlk_b_Skl",0.0)
	Bladex.AddAnmLRelease("Wlk_b_Skl",0.137)
	Bladex.AddAnmLStep("Wlk_b_Skl",0.273)
	Bladex.AddAnmLRelease("Wlk_b_Skl",0.628)
	Bladex.AddAnmLStep("Wlk_b_Skl",0.774)
	Bladex.AddStopTests("Wlk_b_Skl")





	#
	# End caminar
	#


	###




#	Bladex.CreateFCAnimation("../../Anm/Skl_wlk_short_no.BMV","WlkShort_Skl",4)
#
#	Bladex.AddAnmRStep("WlkShort_Skl",0.0)
#	Bladex.AddAnmLStep("WlkShort_Skl",0.5)
#	Bladex.AddAnmRStep("WlkShort_Skl",1.0)
#	Bladex.AddAnmRRelease("WlkShort_Skl",0.5)
#	Bladex.AddAnmLRelease("WlkShort_Skl",1.0)
#
#	Bladex.AddAnmEvent("WlkShort_Skl","StopTest",0.20)
#	Bladex.AddAnmEvent("WlkShort_Skl","StopTest",0.7)
#
#	#### Escalones ####
#
#	#Bladex.LoadSampledAnimation("../../Anm/Skl_wlk_up.BMV","WlkUp_Skl",1)
#
#	Bladex.CreateDFCAnimation("../../Anm/Skl_wlk_up.BMV","../../Anm/Skl_wlk_no.BMV","WlkUp_Skl",4)
#	Bladex.CreateDFCAnimation("../../Anm/Skl_wlk_down.BMV","../../Anm/Skl_wlk_no.BMV","WlkDown_Skl",4)
#
#	Bladex.CreateFCAnimation("../../Anm/Skl_stairs_u_no.BMV","StairsUp_Skl",4)
#	Bladex.CreateDFCAnimation("../../Anm/Skl_stairs_u_no_mas.BMV","../../Anm/Skl_stairs_u_no.BMV","StairsUpP_Skl",4)
#
#	Bladex.CreateFCAnimation("../../Anm/Skl_stairs_d_no.BMV","StairsDown_Skl",4)
#
#	Bladex.AddAnmRStep("StairsUp_Skl",0.0)
#	Bladex.AddAnmLStep("StairsUp_Skl",0.5)
#	Bladex.AddAnmRStep("StairsUp_Skl",1.0)
#	Bladex.AddAnmRRelease("StairsUp_Skl",0.5)
#	Bladex.AddAnmLRelease("StairsUp_Skl",1.0)
#
	#### Caidas ####

#	Bladex.LoadSampledAnimation("../../Anm/Skl_fll_low_1h.BMV","FallMed_Skl",0)
#	Bladex.AddAnmRStep("FallLow_Skl",0.0)
#	Bladex.AddAnmLStep("FallLow_Skl",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Skl_fll_med.BMV","FallMed_Skl",0)
	Bladex.AddAnmRStep("FallMed_Skl",0.0)
	Bladex.AddAnmLStep("FallMed_Skl",0.0)

#	Bladex.LoadSampledAnimation("../../Anm/Skl_fll_high_1h.BMV","FallMed_Skl",0)
#	Bladex.AddAnmRStep("FallHigh_Skl",0.0)
#	Bladex.AddAnmLStep("FallHigh_Skl",0.0)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Skl",0,"Skeleton")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Skl",0,"Skeleton")
	Bladex.AddAnmRStep("Dth_Fll2_Skl",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Skl",0.0)

	#
	# Ataques
#	#
#	Bladex.LoadSampledAnimation("../../Anm/Skl_g_08.BMV","Skl_g_08",0)
#	Bladex.AddAnmRStep("Skl_g_08",0)
#	Bladex.AddAnmLStep("Skl_g_08",0)
#	Bladex.AddAnmRRelease("Skl_g_08",0.29)
#	Bladex.AddAnmRStep("Skl_g_08",0.49)
#	Bladex.AddAnmRRelease("Skl_g_08",0.72)
#	Bladex.AddAnmRStep("Skl_g_08",0.89)
#

	Bladex.LoadSampledAnimation("../../Anm/Skl_g_01.BMV","Skl_g_01",0)
	Bladex.AddAnmRStep("Skl_g_01",0)
	Bladex.AddAnmLStep("Skl_g_01",0)
	Bladex.AddAnmRRelease("Skl_g_01",0.087)
	Bladex.AddAnmRStep("Skl_g_01",0.265)
	Bladex.AddAnmRRelease("Skl_g_01",0.552)
	Bladex.AddAnmRStep("Skl_g_01",0.817)


	Bladex.LoadSampledAnimation("../../Anm/Skl_g_02.BMV","Skl_g_02",0)
	Bladex.AddAnmRStep("Skl_g_02",0)
	Bladex.AddAnmLStep("Skl_g_02",0)
	Bladex.AddAnmRRelease("Skl_g_02",0.034)
	Bladex.AddAnmRStep("Skl_g_02",0.130)
	Bladex.AddAnmRRelease("Skl_g_02",0.246)
	Bladex.AddAnmRStep("Skl_g_02",0.350)
	Bladex.AddAnmRRelease("Skl_g_02",0.591)
	Bladex.AddAnmRStep("Skl_g_02",0.806)


#	Bladex.LoadSampledAnimation("../../Anm/Skl_g_05.BMV","Skl_g_05",0)
#	Bladex.AddAnmRStep("Skl_g_05",0)
#	Bladex.AddAnmLStep("Skl_g_05",0)
#	Bladex.AddAnmRRelease("Skl_g_05",0.28)
#	Bladex.AddAnmRStep("Skl_g_05",0.5)
#	Bladex.AddAnmRRelease("Skl_g_05",0.72)
#	Bladex.AddAnmRStep("Skl_g_05",0.9)


#	Bladex.LoadSampledAnimation("../../Anm/Skl_g_06.BMV","Skl_g_06",0)
#	Bladex.AddAnmRStep("Skl_g_06",0)
#	Bladex.AddAnmLStep("Skl_g_06",0)
#	Bladex.AddAnmRRelease("Skl_g_06",0.153)
#	Bladex.AddAnmRStep("Skl_g_06",0.372)
#	Bladex.AddAnmRRelease("Skl_g_06",0.554)
#	Bladex.AddAnmRStep("Skl_g_06",0.788)
#

	Bladex.LoadSampledAnimation("../../Anm/Skl_g_07.BMV","Skl_g_07",0)
	Bladex.AddAnmRStep("Skl_g_07",0)
	Bladex.AddAnmLStep("Skl_g_07",0)
	Bladex.AddAnmRRelease("Skl_g_07",0.073)
	Bladex.AddAnmRStep("Skl_g_07",0.215)
	Bladex.AddAnmRRelease("Skl_g_07",0.836)
	Bladex.AddAnmRStep("Skl_g_07",0.987)


	Bladex.LoadSampledAnimation("../../Anm/Skl_g_09.BMV","Skl_g_09",0)
	Bladex.AddAnmRStep("Skl_g_09",0)
	Bladex.AddAnmLStep("Skl_g_09",0)
	Bladex.AddAnmRRelease("Skl_g_09",0.105)
	Bladex.AddAnmRStep("Skl_g_09",0.265)
	Bladex.AddAnmRRelease("Skl_g_09",0.625)
	Bladex.AddAnmRStep("Skl_g_09",0.832)

#
#	Bladex.LoadSampledAnimation("../../Anm/Skl_g_13.BMV","Skl_g_13",0)
#	Bladex.AddAnmRStep("Skl_g_13",0)
#	Bladex.AddAnmLStep("Skl_g_13",0)
#	Bladex.AddAnmRRelease("Skl_g_13",0.41)
#	Bladex.AddAnmRStep("Skl_g_13",0.57)
#	Bladex.AddAnmLRelease("Skl_g_13",0.76)
#	Bladex.AddAnmLStep("Skl_g_13",0.89)
#

	Bladex.LoadSampledAnimation("../../Anm/kgt_g_18.BMV","Skl_g_18",0,"Skeleton")
	Bladex.AddAnmRStep("Skl_g_18",0)
	Bladex.AddAnmRRelease("Skl_g_18",0.211)
	Bladex.AddAnmRStep("Skl_g_18",0.503)
	Bladex.AddAnmRRelease("Skl_g_18",0.730)
	Bladex.AddAnmRStep("Skl_g_18",0.894)
	Bladex.AddAnmLStep("Skl_g_18",0)
	Bladex.AddAnmLRelease("Skl_g_18",0.091)
	Bladex.AddAnmLStep("Skl_g_18",0.207)
	Bladex.AddAnmLRelease("Skl_g_18",0.308)
	Bladex.AddAnmLStep("Skl_g_18",0.48)
	Bladex.AddAnmLRelease("Skl_g_18",0.793)
	Bladex.AddAnmLStep("Skl_g_18",0.841)


#

#	Bladex.LoadSampledAnimation("../../Anm/Skl_g_14.BMV","Skl_g_14",0)
#	Bladex.AddAnmRStep("Skl_g_14",0)
#	Bladex.AddAnmLStep("Skl_g_14",0)
#	Bladex.AddAnmLRelease("Skl_g_14",0.15)
#	Bladex.AddAnmLStep("Skl_g_14",0.37)
#	Bladex.AddAnmRRelease("Skl_g_14",0.43)
#	Bladex.AddAnmRStep("Skl_g_14",0.56)
#	Bladex.AddAnmLRelease("Skl_g_14",0.73)
#	Bladex.AddAnmLStep("Skl_g_14",0.85)
#
#
#	Bladex.LoadSampledAnimation("../../Anm/Skl_g_11.BMV","Skl_g_11",0)
#	Bladex.AddAnmRStep("Skl_g_11",0)
#	Bladex.AddAnmLStep("Skl_g_11",0)
#	Bladex.AddAnmRRelease("Skl_g_11",0.4)
#	Bladex.AddAnmRStep("Skl_g_11",0.55)
#	Bladex.AddAnmLRelease("Skl_g_11",0.78)
#	Bladex.AddAnmLStep("Skl_g_11",0.93)


	Bladex.LoadSampledAnimation("../../Anm/Skl_g_16.BMV","Skl_g_16",0)
	Bladex.AddAnmRStep("Skl_g_16",0)
	Bladex.AddAnmLStep("Skl_g_16",0)
	Bladex.AddAnmRRelease("Skl_g_16",0.066)
	Bladex.AddAnmRStep("Skl_g_16",0.230)
	Bladex.AddAnmLRelease("Skl_g_16",0.257)
	Bladex.AddAnmLStep("Skl_g_16",0.445)


#Bladex.LoadSampledAnimation("../../Anm/Skl_g_12.BMV","Skl_g_12",0)
#Bladex.AddAnmRStep("Skl_g_12",0)
#Bladex.AddAnmLStep("Skl_g_12",0)
#Bladex.AddAnmRRelease("Skl_g_12",0.4)
#Bladex.AddAnmRStep("Skl_g_12",0.52)
#Bladex.AddAnmLRelease("Skl_g_12",0.71)
#Bladex.AddAnmLStep("Skl_g_12",0.85)


#Bladex.LoadSampledAnimation("../../Anm/Skl_g_17.BMV","Skl_g_17",0)
#Bladex.AddAnmRStep("Skl_g_17",0)
#Bladex.AddAnmLStep("Skl_g_17",0)
#Bladex.AddAnmRRelease("Skl_g_17",0.16)
#Bladex.AddAnmRStep("Skl_g_17",0.27)
#Bladex.AddAnmLRelease("Skl_g_17",0.53)
#Bladex.AddAnmLStep("Skl_g_17",0.65)


#
#Bladex.LoadSampledAnimation("../../Anm/Skl_g_15.BMV","Skl_g_15",0)
#Bladex.AddAnmRRelease("Skl_g_15",0.09)
#Bladex.AddAnmRStep("Skl_g_15",0.3)
#Bladex.AddAnmLRelease("Skl_g_15",0.32)
#Bladex.AddAnmRRelease("Skl_g_15",0.364)
#Bladex.AddAnmRStep("Skl_g_15",0.551)
#Bladex.AddAnmLStep("Skl_g_15",0.592)
#

#Bladex.LoadSampledAnimation("../../Anm/Skl_g_21.BMV","Skl_g_21",0)
#Bladex.AddAnmRStep("Skl_g_21",0)
#Bladex.AddAnmLStep("Skl_g_21",0)
#Bladex.AddAnmRRelease("Skl_g_21",0.51)
#Bladex.AddAnmRStep("Skl_g_21",0.669)
#Bladex.AddAnmLRelease("Skl_g_21",0.696)
#Bladex.AddAnmLStep("Skl_g_21",0.834)
#
#
	Bladex.LoadSampledAnimation("../../Anm/Skl_g_22.BMV","Skl_g_22",0)
	Bladex.AddAnmRStep("Skl_g_22",0)
	Bladex.AddAnmLStep("Skl_g_22",0)
	Bladex.AddAnmRRelease("Skl_g_22",0.075)
	Bladex.AddAnmRStep("Skl_g_22",0.143)
	Bladex.AddAnmRRelease("Skl_g_22",0.412)
	Bladex.AddAnmRStep("Skl_g_22",0.494)
	Bladex.AddAnmRRelease("Skl_g_22",0.856)
	Bladex.AddAnmRStep("Skl_g_22",0.959)
	Bladex.AddAnmLRelease("Skl_g_22",0.259)
	Bladex.AddAnmLStep("Skl_g_22",0.317)


#
#
#Bladex.LoadSampledAnimation("../../Anm/Skl_g_23.BMV","Skl_g_23",0)
#Bladex.AddAnmRStep("Skl_g_23",0)
#Bladex.AddAnmLStep("Skl_g_23",0)
#Bladex.AddAnmRRelease("Skl_g_23",0.529)
#Bladex.AddAnmRStep("Skl_g_23",0.743)
#Bladex.AddAnmLRelease("Skl_g_23",0.75)
#Bladex.AddAnmLStep("Skl_g_23",0.85)
#
#
#Bladex.LoadSampledAnimation("../../Anm/Skl_g_26.BMV","Skl_g_26",0)
#Bladex.AddAnmRStep("Skl_g_26",0)
#Bladex.AddAnmLStep("Skl_g_26",0)
#Bladex.AddAnmRRelease("Skl_g_26",0.135)
#Bladex.AddAnmRStep("Skl_g_26",0.236)
#Bladex.AddAnmLRelease("Skl_g_26",0.48)
#Bladex.AddAnmLStep("Skl_g_26",0.682)
#Bladex.AddAnmLRelease("Skl_g_26",0.79)
#Bladex.AddAnmLStep("Skl_g_26",0.885)
#
#
#Bladex.LoadSampledAnimation("../../Anm/Skl_g_27.BMV","Skl_g_27",0)
#Bladex.AddAnmRStep("Skl_g_27",0)
#Bladex.AddAnmLStep("Skl_g_27",0)
#Bladex.AddAnmRRelease("Skl_g_27",0.28)
#Bladex.AddAnmRStep("Skl_g_27",0.5)
#Bladex.AddAnmLRelease("Skl_g_27",0.72)
#Bladex.AddAnmLStep("Skl_g_27",0.74)
#
#
#anm_name="Skl_g_31"
#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#Bladex.AddAnmRStep(anm_name,0)
#Bladex.AddAnmLStep(anm_name,0)
#Bladex.AddAnmRRelease(anm_name,0.283)
#Bladex.AddAnmRStep(anm_name,0.383)
#Bladex.AddAnmRRelease(anm_name,0.544)
#Bladex.AddAnmRStep(anm_name,0.597)
#Bladex.AddAnmLRelease(anm_name,0.010)
#Bladex.AddAnmLStep(anm_name,0.257)
#Bladex.AddAnmLRelease(anm_name,0.51)
#Bladex.AddAnmLStep(anm_name,0.597)


	#
	# Movimientos en combate
	#
	anm_name="Skl_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.072)
	Bladex.AddAnmRStep(anm_name,0.268)
	Bladex.AddAnmRRelease(anm_name,0.568)
	Bladex.AddAnmRStep(anm_name,0.723)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.346)
	Bladex.AddAnmLStep(anm_name,0.467)
	Bladex.AddAnmLRelease(anm_name,0.858)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Skl_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.392)
	Bladex.AddAnmRStep(anm_name,0.521)
	Bladex.AddAnmRRelease(anm_name,0.889)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.183)
	Bladex.AddAnmLStep(anm_name,0.323)
	Bladex.AddAnmLRelease(anm_name,0.638)
	Bladex.AddAnmLStep(anm_name,0.753)
	Bladex.AddStopTests(anm_name)

	anm_name="Skl_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.329)
	Bladex.AddAnmRStep(anm_name,0.506)
	Bladex.AddAnmRRelease(anm_name,0.856)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.105)
	Bladex.AddAnmLStep(anm_name,0.253)
	Bladex.AddAnmLRelease(anm_name,0.487)
	Bladex.AddAnmLStep(anm_name,0.765)
	Bladex.AddStopTests(anm_name)

	anm_name="Skl_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.163)
	Bladex.AddAnmRStep(anm_name,0.282)
	Bladex.AddAnmRRelease(anm_name,0.635)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.388)
	Bladex.AddAnmLStep(anm_name,0.551)
	Bladex.AddAnmLRelease(anm_name,0.876)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

#	anm_name="Skl_d_b"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.296)
#	Bladex.AddAnmRStep(anm_name,0.562)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.416)
#	Bladex.AddAnmLStep(anm_name,0.709)
#
#	anm_name="Skl_d_r"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.166)
#	Bladex.AddAnmRStep(anm_name,0.318)
#	Bladex.AddAnmRRelease(anm_name,0.481)
#	Bladex.AddAnmRStep(anm_name,0.807)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.272)
#	Bladex.AddAnmLStep(anm_name,0.648)
#
#	anm_name="Skl_d_l"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.067)
#	Bladex.AddAnmRStep(anm_name,0.150)
#	Bladex.AddAnmRRelease(anm_name,0.325)
#	Bladex.AddAnmRStep(anm_name,0.678)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.150)
#	Bladex.AddAnmRStep(anm_name,0.370)
#	Bladex.AddAnmLRelease(anm_name,0.566)
#	Bladex.AddAnmLStep(anm_name,0.829)

	anm_name="Skl_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.072)
	Bladex.AddAnmRStep(anm_name,0.268)
	Bladex.AddAnmRRelease(anm_name,0.568)
	Bladex.AddAnmRStep(anm_name,0.723)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.346)
	Bladex.AddAnmLStep(anm_name,0.467)
	Bladex.AddAnmLRelease(anm_name,0.858)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Skl_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.392)
	Bladex.AddAnmRStep(anm_name,0.521)
	Bladex.AddAnmRRelease(anm_name,0.889)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.183)
	Bladex.AddAnmLStep(anm_name,0.323)
	Bladex.AddAnmLRelease(anm_name,0.591)
	Bladex.AddAnmLStep(anm_name,0.753)
	Bladex.AddStopTests(anm_name)

	anm_name="Skl_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.329)
	Bladex.AddAnmRStep(anm_name,0.506)
	Bladex.AddAnmRRelease(anm_name,0.856)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.105)
	Bladex.AddAnmLStep(anm_name,0.253)
	Bladex.AddAnmLRelease(anm_name,0.487)
	Bladex.AddAnmLStep(anm_name,0.765)
	Bladex.AddStopTests(anm_name)

	anm_name="Skl_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.163)
	Bladex.AddAnmRStep(anm_name,0.282)
	Bladex.AddAnmRRelease(anm_name,0.635)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.388)
	Bladex.AddAnmLStep(anm_name,0.551)
	Bladex.AddAnmLRelease(anm_name,0.876)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

#	anm_name="Skl_rlx_f"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#
#	anm_name="Skl_rlx_s"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#
#	anm_name="Skl_attack_rlx_s"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)


#	anm_name="Skl_attack_t_r"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0)
#	Bladex.AddAnmRStep(anm_name,1)
#	Bladex.AddAnmLStep(anm_name,1)
#
#
#	anm_name="Skl_attack_t_r"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0)
#	Bladex.AddAnmRStep(anm_name,1)
#	Bladex.AddAnmLStep(anm_name,1)
#
#	anm_name="Skl_attack_t_r_s"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#
#	anm_name="Skl_attack_t_r_s"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#
#
#
#	#
#	# Saltos
#	#
#	anm_name="Skl_jmp_no"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	"""
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.10)
#	"""
#	Bladex.AddAnmRStep(anm_name,0.3)
#	Bladex.AddAnmLStep(anm_name,0.3)
#	#Bladex.AddAnmRStep(anm_name,0.33)
#	#Bladex.AddAnmLStep(anm_name,0.34)
#	Bladex.AddAnmRRelease(anm_name,0.37)
#	Bladex.AddAnmLRelease(anm_name,0.45)
#	Bladex.AddAnmRStep(anm_name,0.49)
#	Bladex.AddAnmRRelease(anm_name,0.62)
#	Bladex.AddAnmRStep(anm_name,0.70)
#	Bladex.AddAnmLStep(anm_name,0.70)
#
#
#	anm_name="Skl_jmp_1h"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#
#	Bladex.AddAnmRStep(anm_name,0.0)
#	Bladex.AddAnmRRelease(anm_name,0.223)
#	Bladex.AddAnmRStep(anm_name,0.466)
#	Bladex.AddAnmRRelease(anm_name,0.594)
#	Bladex.AddAnmRStep(anm_name,0.681)
#	Bladex.AddAnmLStep(anm_name,0.0)
#	Bladex.AddAnmLRelease(anm_name,0.075)
#	Bladex.AddAnmLStep(anm_name,0.193)
#	Bladex.AddAnmLRelease(anm_name,0.297)
#	Bladex.AddAnmLStep(anm_name,0.528)
#	Bladex.AddAnmLRelease(anm_name,0.688)
#	Bladex.AddAnmLStep(anm_name,0.800)
#
#	anm_name="Skl_jmph0_no"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.324)
#	Bladex.AddAnmLRelease(anm_name,0.532)
#	Bladex.AddAnmRStep(anm_name,0.618)
#	Bladex.AddAnmLStep(anm_name,0.843)
#	Bladex.AddStopTests(anm_name)
#
#	#
#	# Slip
#	#
	anm_name="Skl_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Skl_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Skl_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




	####GIRAR#####
	##############

#    	anm_name="Skl_t_r_1h"
#    	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV","Skl_t_r_1h",0)
#
#    	Bladex.AddAnmRStep("Skl_t_r_1h",0.0)
#    	Bladex.AddAnmLStep("Skl_t_r_1h",0.0)
#    	Bladex.AddAnmLRelease("Skl_t_r_1h",0.380)
#    	Bladex.AddAnmLStep("Skl_t_r_1h",0.627)
#

#   	anm_name="Skl_t_r_1h"
#    	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV","Skl_t_r_1h",0)
#
#    	Bladex.AddAnmRStep("Skl_t_r_1h",0.0)
#    	Bladex.AddAnmLStep("Skl_t_r_1h",0.0)
#    	Bladex.AddAnmLRelease("Skl_t_r_1h",0.317)
#    	Bladex.AddAnmLStep("Skl_t_r_1h",0.472)



	anm_name="Skl_jmp_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_jmp_1h.BMV","Skl_jmp_1h",0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.340)
	Bladex.AddAnmLStep(anm_name,0.340)
	Bladex.AddAnmRRelease(anm_name,0.360)
	Bladex.AddAnmLRelease(anm_name,0.461)
	Bladex.AddAnmRStep(anm_name,0.499)
	Bladex.AddAnmRRelease(anm_name,0.597)
	Bladex.AddAnmRStep(anm_name,0.696)
	Bladex.AddAnmLStep(anm_name,0.696)



	anm_name="Skl_b1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV","Skl_b1",0)
	Bladex.AddAnmLStep("Skl_b1",0)
	Bladex.AddAnmRStep("Skl_b1",0.0)

	anm_name="Skl_b2"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV","Skl_b2",0)
	Bladex.AddAnmLStep("Skl_b2",0)
	Bladex.AddAnmRStep("Skl_b2",0.0)

	anm_name="Skl_b3"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV","Skl_b3",0)
	Bladex.AddAnmLStep("Skl_b3",0)
	Bladex.AddAnmRStep("Skl_b3",0.0)



	anm_name="Skl_clmb_low"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.35)
	Bladex.AddAnmRStep(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.4)
	Bladex.AddAnmLStep(anm_name,0.63)

#	anm_name="Skl_clmb_med"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.0)
#	Bladex.AddAnmRRelease(anm_name,0.11)
#	Bladex.AddAnmRStep(anm_name,0.22)
#	Bladex.AddAnmRRelease(anm_name,0.71)
#	Bladex.AddAnmRStep(anm_name,0.9)
#	Bladex.AddAnmLStep(anm_name,0.0)
#	Bladex.AddAnmLRelease(anm_name,0.4)
#	Bladex.AddAnmLStep(anm_name,0.58)
#	Bladex.AddAnmLRelease(anm_name,0.93)
#	Bladex.AddAnmLStep(anm_name,1.0)

	anm_name="Skl_patrol1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)



	anm_name="Skl_sword_reaction"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Skeleton")
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





###########################
#                         #
#     A�adidos Luismi     #
#                         #
###########################




	anm_name="Skl_attack_chg_r_l"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_chg_r_l.BMV",anm_name,1,"Skeleton")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)




	anm_name="Skl_alarm01"
	Bladex.LoadSampledAnimation("../../Anm/Skl_alarm01.BMV",anm_name,1,"Skeleton")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


#
#	anm_name="Skl_alarm02"
#	Bladex.LoadSampledAnimation("../../Anm/Tkn_alarm02.BMV",anm_name,1,"Skeleton")
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.00)
#
#
#	anm_name="Skl_fury"
#	Bladex.LoadSampledAnimation("../../Anm/Tkn_fury.BMV",anm_name,1,"Skeleton")
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.00)
#




	anm_name="Skl_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_s_broken.BMV",anm_name,1,"Skeleton")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)





	anm_name="Skl_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth0.BMV",anm_name,0,"Skeleton")
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


	anm_name="Skl_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c1.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)
 	Bladex.AddAnmLRelease(anm_name,0.745)  # Added.
	Bladex.AddAnmRRelease(anm_name,0.789)  #
	Bladex.AddAnmLStep(anm_name,0.883)     #
	Bladex.AddAnmRStep(anm_name,0.908)     #    -LeadHead

	anm_name="Skl_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c2.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)

	anm_name="Skl_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c3.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)

	anm_name="Skl_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c4.BMV",anm_name,0,"Skeleton")
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

	anm_name="Skl_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c5.BMV",anm_name,0,"Skeleton")
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

	anm_name="Skl_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c6.BMV",anm_name,0,"Skeleton")
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

	anm_name="Skl_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)



	anm_name="Skl_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n00.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)

	anm_name="Skl_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n01.BMV",anm_name,0,"Skeleton")
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

	anm_name="Skl_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n02.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)

	anm_name="Skl_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n03.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)

	anm_name="Skl_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n04.BMV",anm_name,0,"Skeleton")
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

	anm_name="Skl_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n05.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)

	anm_name="Skl_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0,"Skeleton")
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

	anm_name="Skl_dth_rock"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rock.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Skl_dth_rockfront"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rockfront.BMV",anm_name,0,"Skeleton")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.348)
	Bladex.AddAnmRStep(anm_name,0.796)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.335)
	Bladex.AddAnmLStep(anm_name,0.792)

	anm_name="Skl_dth_burn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_burn.BMV",anm_name,0,"Skeleton")
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

	anm_name="Skl_dth_explo" ### Added -LeadHead
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.065)
	Bladex.AddAnmRRelease(anm_name,0.127)
	Bladex.AddAnmLStep(anm_name,1.0)


###### Heridas


	anm_name="Skl_hurt_f_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_hurt_f_breast"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_hurt_f_head"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_hurt_f_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_hurt_f_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_hurt_f_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_hurt_back"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.4)
	Bladex.AddAnmRStep(anm_name,0.6)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.27)
	Bladex.AddAnmLStep(anm_name,0.43)

	anm_name="Skl_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.35)
	Bladex.AddAnmRStep(anm_name,0.59)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,1.0)


	anm_name="Skl_df_01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Skl_df_02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.310)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmRStep(anm_name,0.569)
	Bladex.AddAnmLStep(anm_name,0.832)