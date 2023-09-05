##///
##||| LchAnimatinoSet.PY TITANIUM
##||| Change list:
##||| * Added step events for anim dth0
##||| * Added step events for hurt anims
##||| * 
##||| * TODO: ensure better synchronization between all anims and step events
##||| * 
##||| * 
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



def LoadLchAnimationSet(ct_name):

	print "Loading the Lch animation sets..."

	Bladex.LoadSampledAnimation("../../Anm/Lch_appears1.BMV","Lch_appears1",0)      # PLAGUE: Missing steps
	Bladex.AddAnmRStep("Lch_appears1",0)
	Bladex.AddAnmLStep("Lch_appears1",0)

#	#### Relax ####
#	#Bladex.AddAnimFlags("Lch_rlx",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
#
#	Bladex.LoadSampledAnimation("../../Anm/Lch_rlx_no.BMV","Rlx_no_Lch",1)
#	Bladex.AddAnmRStep("Rlx_no_Lch",0.0)
#	Bladex.AddAnmLStep("Rlx_no_Lch",0.0)
#
	Bladex.LoadSampledAnimation("../../Anm/Lch_rlx_no.BMV","Rlx_1h_Lch",1)
	Bladex.AddAnmRStep("Rlx_1h_Lch",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Lch",0.0)
#
#	Bladex.LoadSampledAnimation("../../Anm/Lch_rlx_b.BMV","Rlx_b_Lch",1)
#	Bladex.AddAnmRStep("Rlx_b_Lch",0.0)
#	Bladex.AddAnmLStep("Rlx_b_Lch",0.0)
#
#	### CORRER   ####
#	Bladex.CreateFCAnimation("../../Anm/Lch_jog_no.BMV","Jog_no_Lch",4)
#	Bladex.AddAnmRStep("Jog_no_Lch",0.0)
#	Bladex.AddAnmLStep("Jog_no_Lch",0.505)
#	Bladex.AddAnmRStep("Jog_no_Lch",1.0)
#	Bladex.AddAnmRRelease("Jog_no_Lch",0.266)
#	Bladex.AddAnmLRelease("Jog_no_Lch",0.783)
#	Bladex.AddAnmEvent("Jog_no_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Jog_no_Lch","StopTest",0.7)
#
#	Bladex.CreateFCAnimation("../../Anm/Lch_jog_1h.BMV","Jog_1h_Lch",4)
#	Bladex.AddAnmLStep("Jog_1h_Lch",0.0)
#	Bladex.AddAnmLRelease("Jog_1h_Lch",0.209)#
#	Bladex.AddAnmLStep("Jog_1h_Lch",0.516)
#	Bladex.AddAnmLRelease("Jog_1h_Lch",0.724)#
#	Bladex.AddAnmLStep("Jog_1h_Lch",0.1000)
#	Bladex.AddAnmRStep("Jog_1h_Lch",0.266)
#	Bladex.AddAnmRRelease("Jog_1h_Lch",0.455)
#	Bladex.AddAnmRStep("Jog_1h_Lch",0.783)
#	Bladex.AddAnmRRelease("Jog_1h_Lch",0.947)
#	Bladex.AddAnmEvent("Jog_1h_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Jog_1h_Lch","StopTest",0.7)
#
#	Bladex.CreateFCAnimation("../../Anm/Lch_jog_b.BMV","Jog_b_Lch",4)
#	Bladex.AddAnmLStep("Jog_b_Lch",0.055)
#	Bladex.AddAnmLRelease("Jog_b_Lch",0.201)
#	Bladex.AddAnmLStep("Jog_b_Lch",0.535)
#	Bladex.AddAnmLRelease("Jog_b_Lch",0.734)
#	Bladex.AddAnmRStep("Jog_b_Lch",0.0)
#	Bladex.AddAnmRRelease("Jog_b_Lch",0.033)
#	Bladex.AddAnmRStep("Jog_b_Lch",0.346)
#	Bladex.AddAnmRRelease("Jog_b_Lch",0.51)
#	Bladex.AddAnmRStep("Jog_b_Lch",0.83)
#	Bladex.AddAnmEvent("Jog_b_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Jog_b_Lch","StopTest",0.7)
#



#	### SNEAK   ####
#	Bladex.CreateFCAnimation("../../Anm/Lch_snk_no.BMV","Snk_no_Lch",4)
#	Bladex.AddAnmRStep("Snk_no_Lch",0.0)
#	Bladex.AddAnmLStep("Snk_no_Lch",0.485)
#	Bladex.AddAnmRStep("Snk_no_Lch",1.0)
#	Bladex.AddAnmRRelease("Snk_no_Lch",0.543)
#	Bladex.AddAnmLRelease("Snk_no_Lch",0.627)
#	Bladex.AddAnmEvent("Snk_no_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Snk_no_Lch","StopTest",0.7)
#
#	Bladex.CreateFCAnimation("../../Anm/Lch_snk_1h.BMV","Snk_1h_Lch",4)
#	Bladex.AddAnmRStep("Snk_1h_Lch",0.000)
#	Bladex.AddAnmLRelease("Snk_1h_Lch",0.005)
#	Bladex.AddAnmRStep("Snk_1h_Lch",1.000)
#	Bladex.AddAnmLStep("Snk_1h_Lch",0.500)
#	Bladex.AddAnmRRelease("Snk_1h_Lch",0.500)
#	Bladex.AddAnmEvent("Snk_1h_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Snk_1h_Lch","StopTest",0.7)
#
#	Bladex.CreateFCAnimation("../../Anm/Lch_snk_b.BMV","Snk_b_Lch",4)
#	Bladex.AddAnmRStep("Snk_b_Lch",0.0)
#	Bladex.AddAnmLStep("Snk_b_Lch",0.509)
#	Bladex.AddAnmRStep("Snk_b_Lch",1.0)
#	Bladex.AddAnmRRelease("Snk_b_Lch",0.608)
#	Bladex.AddAnmLRelease("Snk_b_Lch",0.052)
#	Bladex.AddAnmEvent("Snk_b_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Snk_b_Lch","StopTest",0.7)


#	####  WBK ####
#	Bladex.CreateFCAnimation("../../Anm/Lch_attack_b.BMV","Wbk_1h_Lch",4)
#	Bladex.AddAnmRStep("Wbk_1h_Lch",0.0)
#	Bladex.AddAnmRRelease("Wbk_1h_Lch",0.153)
#	Bladex.AddAnmRStep("Wbk_1h_Lch",0.270)
#	Bladex.AddAnmRRelease("Wbk_1h_Lch",0.630)
#	Bladex.AddAnmRStep("Wbk_1h_Lch",777)
#	Bladex.AddAnmLStep("Wbk_1h_Lch",0.045)
#	Bladex.AddAnmLRelease("Wbk_1h_Lch",0.4)
#	Bladex.AddAnmLStep("Wbk_1h_Lch",0.52)
#	Bladex.AddAnmLRelease("Wbk_1h_Lch",0.873)
#	Bladex.AddStopTests("Wbk_1h_Lch")


#	Bladex.AddAnmEvent("Wbk_1h_Lch","StopTest",0.2)
#	Bladex.AddAnmEvent("Wbk_1h_Lch","StopTest",0.7)
#
#	Bladex.CreateFCAnimation("../../Anm/Lch_attack_b.BMV","Wbk_no_Lch",4)
#
#	Bladex.AddAnmRStep("Wbk_no_Lch",0.106)
#	Bladex.AddAnmRRelease("Wbk_no_Lch",0.166)
#	Bladex.AddAnmRStep("Wbk_no_Lch",0.621)
#	Bladex.AddAnmRRelease("Wbk_no_Lch",0.7)
#	Bladex.AddAnmRStep("Wbk_no_Lch",1)
#	Bladex.AddAnmLStep("Wbk_no_Lch",0)
#	Bladex.AddAnmLRelease("Wbk_no_Lch",0.046)
#	Bladex.AddAnmLStep("Wbk_no_Lch",0.345)
#	Bladex.AddAnmLRelease("Wbk_no_Lch",0.541)
#	Bladex.AddAnmLStep("Wbk_no_Lch",0.849)
#	Bladex.AddStopTests(anm_name)
#
#
#	Bladex.AddAnmEvent("Wbk_no_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Wbk_no_Lch","StopTest",0.70)






	#
	#### Caminar ####
	#


	Bladex.LoadSampledAnimation("../../Anm/Lch_wlk_1h.BMV","Wlk_1h_Lch",1)

	Bladex.AddAnmRStep("Wlk_1h_Lch",0.0)
	Bladex.AddAnmRRelease("Wlk_1h_Lch",0.10)
	Bladex.AddAnmRStep("Wlk_1h_Lch",0.33)
	Bladex.AddAnmRRelease("Wlk_1h_Lch",0.56)
	Bladex.AddAnmRStep("Wlk_1h_Lch",0.84)
	Bladex.AddAnmLStep("Wlk_1h_Lch",0.0)
	Bladex.AddAnmLRelease("Wlk_1h_Lch",0.32)
	Bladex.AddAnmLStep("Wlk_1h_Lch",0.51)
	Bladex.AddAnmLRelease("Wlk_1h_Lch",0.75)
	Bladex.AddAnmLStep("Wlk_1h_Lch",1.00)

	Bladex.AddStopTests("Wlk_1h_Lch")




	anm_name="Lch_wbk_1h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.319)
	Bladex.AddAnmRStep(anm_name,0.542)
	Bladex.AddAnmRRelease(anm_name,0.833)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.153)
	Bladex.AddAnmLStep(anm_name,0.333)
	Bladex.AddAnmLRelease(anm_name,0.639)
	Bladex.AddAnmLStep(anm_name,0.819)





#	Bladex.CreateFCAnimation("../../Anm/Lch_wlk_b.BMV","Wlk_b_Lch",4)

#	Bladex.AddAnmRStep("Wlk_b_Lch",0.0)
#	Bladex.AddAnmRRelease("Wlk_b_Lch",0.234)
#	Bladex.AddAnmRStep("Wlk_b_Lch",0.541)
#	Bladex.AddAnmRRelease("Wlk_b_Lch",0.881)
#	Bladex.AddAnmRStep("Wlk_b_Lch",1.0)
#	Bladex.AddAnmLStep("Wlk_b_Lch",0.0)
#	Bladex.AddAnmLRelease("Wlk_b_Lch",0.137)
#	Bladex.AddAnmLStep("Wlk_b_Lch",0.273)
#	Bladex.AddAnmLRelease("Wlk_b_Lch",0.628)
#	Bladex.AddAnmLStep("Wlk_b_Lch",0.774)

#	Bladex.AddAnmEvent("Wlk_b_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Wlk_b_Lch","StopTest",0.7)




	#
	# End caminar
	#


	###

#	Bladex.CreateFCAnimation("../../Anm/Lch_wlk_1h.BMV","Wlk_1h_Lch",4)
#
#	Bladex.AddAnmRStep("Wlk_1h_Lch",0.0)
#	Bladex.AddAnmLStep("Wlk_1h_Lch",0.5)
#	Bladex.AddAnmRStep("Wlk_1h_Lch",1.0)
#	Bladex.AddAnmRRelease("Wlk_1h_Lch",0.5)
#	Bladex.AddAnmLRelease("Wlk_1h_Lch",1.0)
#
#	Bladex.AddAnmEvent("Wlk_1h_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("Wlk_1h_Lch","StopTest",0.7)
#



#	Bladex.CreateFCAnimation("../../Anm/Lch_wlk_short_no.BMV","WlkShort_Lch",4)
#
#	Bladex.AddAnmRStep("WlkShort_Lch",0.0)
#	Bladex.AddAnmLStep("WlkShort_Lch",0.5)
#	Bladex.AddAnmRStep("WlkShort_Lch",1.0)
#	Bladex.AddAnmRRelease("WlkShort_Lch",0.5)
#	Bladex.AddAnmLRelease("WlkShort_Lch",1.0)
#
#	Bladex.AddAnmEvent("WlkShort_Lch","StopTest",0.20)
#	Bladex.AddAnmEvent("WlkShort_Lch","StopTest",0.7)
#
#	#### Escalones ####
#
#	#Bladex.LoadSampledAnimation("../../Anm/Lch_wlk_up.BMV","WlkUp_Lch",1)
#
#	Bladex.CreateDFCAnimation("../../Anm/Lch_wlk_up.BMV","../../Anm/Lch_wlk_no.BMV","WlkUp_Lch",4)
#	Bladex.CreateDFCAnimation("../../Anm/Lch_wlk_down.BMV","../../Anm/Lch_wlk_no.BMV","WlkDown_Lch",4)
#
#	Bladex.CreateFCAnimation("../../Anm/Lch_stairs_u_no.BMV","StairsUp_Lch",4)
#	Bladex.CreateDFCAnimation("../../Anm/Lch_stairs_u_no_mas.BMV","../../Anm/Lch_stairs_u_no.BMV","StairsUpP_Lch",4)
#
#	Bladex.CreateFCAnimation("../../Anm/Lch_stairs_d_no.BMV","StairsDown_Lch",4)
#
#	Bladex.AddAnmRStep("StairsUp_Lch",0.0)
#	Bladex.AddAnmLStep("StairsUp_Lch",0.5)
#	Bladex.AddAnmRStep("StairsUp_Lch",1.0)
#	Bladex.AddAnmRRelease("StairsUp_Lch",0.5)
#	Bladex.AddAnmLRelease("StairsUp_Lch",1.0)
#
	#### Caidas ####

#	Bladex.LoadSampledAnimation("../../Anm/Lch_fll_low_1h.BMV","FallMed_Lch",0)
#	Bladex.AddAnmRStep("FallLow_Lch",0.0)
#	Bladex.AddAnmLStep("FallLow_Lch",0.0)

#	Bladex.LoadSampledAnimation("../../Anm/Lch_fll_med_1h.BMV","FallMed_Lch",0)
#	Bladex.AddAnmRStep("FallMed_Lch",0.0)
#	Bladex.AddAnmLStep("FallMed_Lch",0.0)

#	Bladex.LoadSampledAnimation("../../Anm/Lch_fll_high_1h.BMV","FallMed_Lch",0)
#	Bladex.AddAnmRStep("FallHigh_Lch",0.0)
#	Bladex.AddAnmLStep("FallHigh_Lch",0.0)


	#
	# Ataques
#	#


	Bladex.LoadSampledAnimation("../../Anm/Lch_g_spit.BMV","Lch_g_spit",0)
	Bladex.AddAnmRStep("Lch_g_spit",0)
	Bladex.AddAnmLStep("Lch_g_spit",0)
	Bladex.AddAnmRRelease("Lch_g_spit",0.521)
	Bladex.AddAnmRStep("Lch_g_spit",0.586)
	Bladex.AddAnmLRelease("Lch_g_spit",0.464)
	Bladex.AddAnmLStep("Lch_g_spit",0.504)





#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_08.BMV","Lch_g_08",0)
#	Bladex.AddAnmRStep("Lch_g_08",0)
#	Bladex.AddAnmLStep("Lch_g_08",0)
#	Bladex.AddAnmRRelease("Lch_g_08",0.29)
#	Bladex.AddAnmRStep("Lch_g_08",0.49)
#	Bladex.AddAnmRRelease("Lch_g_08",0.72)
#	Bladex.AddAnmRStep("Lch_g_08",0.89)
#

#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_01.BMV","Lch_g_01",0)
#	Bladex.AddAnmRStep("Lch_g_01",0)
#	Bladex.AddAnmLStep("Lch_g_01",0)
#	Bladex.AddAnmRRelease("Lch_g_01",0.087)
#	Bladex.AddAnmRStep("Lch_g_01",0.265)
#	Bladex.AddAnmRRelease("Lch_g_01",0.552)
#	Bladex.AddAnmRStep("Lch_g_01",0.817)


#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_02.BMV","Lch_g_02",0)
#	Bladex.AddAnmRStep("Lch_g_02",0)
#	Bladex.AddAnmLStep("Lch_g_02",0)
#	Bladex.AddAnmRRelease("Lch_g_02",0.034)
#	Bladex.AddAnmRStep("Lch_g_02",0.130)
#	Bladex.AddAnmRRelease("Lch_g_02",0.246)
#	Bladex.AddAnmRStep("Lch_g_02",0.350)
#	Bladex.AddAnmRRelease("Lch_g_02",0.591)
#	Bladex.AddAnmRStep("Lch_g_02",0.806)
#

#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_05.BMV","Lch_g_05",0)
#	Bladex.AddAnmRStep("Lch_g_05",0)
#	Bladex.AddAnmLStep("Lch_g_05",0)
#	Bladex.AddAnmRRelease("Lch_g_05",0.28)
#	Bladex.AddAnmRStep("Lch_g_05",0.5)
#	Bladex.AddAnmRRelease("Lch_g_05",0.72)
#	Bladex.AddAnmRStep("Lch_g_05",0.9)


#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_06.BMV","Lch_g_06",0)
#	Bladex.AddAnmRStep("Lch_g_06",0)
#	Bladex.AddAnmLStep("Lch_g_06",0)
#	Bladex.AddAnmRRelease("Lch_g_06",0.153)
#	Bladex.AddAnmRStep("Lch_g_06",0.372)
#	Bladex.AddAnmRRelease("Lch_g_06",0.554)
#	Bladex.AddAnmRStep("Lch_g_06",0.788)
#

#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_07.BMV","Lch_g_07",0)
#	Bladex.AddAnmRStep("Lch_g_07",0)
#	Bladex.AddAnmLStep("Lch_g_07",0)
#	Bladex.AddAnmRRelease("Lch_g_07",0.073)
#	Bladex.AddAnmRStep("Lch_g_07",0.215)
#	Bladex.AddAnmRRelease("Lch_g_07",0.836)
#	Bladex.AddAnmRStep("Lch_g_07",0.987)


#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_09.BMV","Lch_g_09",0)
#	Bladex.AddAnmRStep("Lch_g_09",0)
#	Bladex.AddAnmLStep("Lch_g_09",0)
#	Bladex.AddAnmRRelease("Lch_g_09",0.105)
#	Bladex.AddAnmRStep("Lch_g_09",0.265)
#	Bladex.AddAnmRRelease("Lch_g_09",0.625)
#	Bladex.AddAnmRStep("Lch_g_09",0.832)


	Bladex.LoadSampledAnimation("../../Anm/Lch_g_13.BMV","Lch_g_13",0)
	Bladex.AddAnmRStep("Lch_g_13",0)
	Bladex.AddAnmLStep("Lch_g_13",0)
	Bladex.AddAnmRRelease("Lch_g_13",0.39)
	Bladex.AddAnmRStep("Lch_g_13",0.43)
	Bladex.AddAnmLRelease("Lch_g_13",0.58)
	Bladex.AddAnmLStep("Lch_g_13",0.63)



	Bladex.LoadSampledAnimation("../../Anm/Lch_g_18.BMV","Lch_g_18",0)
	Bladex.AddAnmRStep("Lch_g_18",0)
	Bladex.AddAnmRRelease("Lch_g_18",0.49)
	Bladex.AddAnmRStep("Lch_g_18",0.56)
	Bladex.AddAnmRRelease("Lch_g_18",0.72)
	Bladex.AddAnmRStep("Lch_g_18",0.78)
	Bladex.AddAnmLStep("Lch_g_18",0)
	Bladex.AddAnmLRelease("Lch_g_18",0.57)
	Bladex.AddAnmLStep("Lch_g_18",0.68)






#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_14.BMV","Lch_g_14",0)
#	Bladex.AddAnmRStep("Lch_g_14",0)
#	Bladex.AddAnmLStep("Lch_g_14",0)
#	Bladex.AddAnmLRelease("Lch_g_14",0.15)
#	Bladex.AddAnmLStep("Lch_g_14",0.37)
#	Bladex.AddAnmRRelease("Lch_g_14",0.43)
#	Bladex.AddAnmRStep("Lch_g_14",0.56)
#	Bladex.AddAnmLRelease("Lch_g_14",0.73)
#	Bladex.AddAnmLStep("Lch_g_14",0.85)
#
#
#	Bladex.LoadSampledAnimation("../../Anm/Lch_g_11.BMV","Lch_g_11",0)
#	Bladex.AddAnmRStep("Lch_g_11",0)
#	Bladex.AddAnmLStep("Lch_g_11",0)
#	Bladex.AddAnmRRelease("Lch_g_11",0.4)
#	Bladex.AddAnmRStep("Lch_g_11",0.55)
#	Bladex.AddAnmLRelease("Lch_g_11",0.78)
#	Bladex.AddAnmLStep("Lch_g_11",0.93)


	Bladex.LoadSampledAnimation("../../Anm/Lch_g_16.BMV","Lch_g_16",0)
	Bladex.AddAnmRStep("Lch_g_16",0)
	Bladex.AddAnmLStep("Lch_g_16",0)
	Bladex.AddAnmRRelease("Lch_g_16",0.475)
	Bladex.AddAnmRStep("Lch_g_16",0.521)
	Bladex.AddAnmLRelease("Lch_g_16",0.53)
	Bladex.AddAnmLStep("Lch_g_16",0.618)



	Bladex.LoadSampledAnimation("../../Anm/Lch_g_12.BMV","Lch_g_12",0)
	Bladex.AddAnmRStep("Lch_g_12",0)
	Bladex.AddAnmLStep("Lch_g_12",0)
	Bladex.AddAnmRRelease("Lch_g_12",0.437)
	Bladex.AddAnmRStep("Lch_g_12",0.543)
	Bladex.AddAnmRRelease("Lch_g_12",0.698)
	Bladex.AddAnmRStep("Lch_g_12",0.763)
	Bladex.AddAnmLRelease("Lch_g_12",0.549)
	Bladex.AddAnmLStep("Lch_g_12",0.709)


	anm_name="Lch_g_claw1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.36)
	Bladex.AddAnmRStep(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.24)
	Bladex.AddAnmLStep(anm_name,0.27)
	Bladex.AddAnmLRelease(anm_name,0.77)
	Bladex.AddAnmLStep(anm_name,0.81)


	anm_name="Lch_g_claw2"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.59)
	Bladex.AddAnmRStep(anm_name,0.64)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.34)
	Bladex.AddAnmLStep(anm_name,0.39)
	Bladex.AddAnmLRelease(anm_name,0.80)
	Bladex.AddAnmLStep(anm_name,0.84)



	anm_name="Lch_g_claw3"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.33)
	Bladex.AddAnmRStep(anm_name,0.39)
	Bladex.AddAnmRRelease(anm_name,0.44)
	Bladex.AddAnmRStep(anm_name,0.54)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.29)
	Bladex.AddAnmLStep(anm_name,0.34)
	Bladex.AddAnmLRelease(anm_name,0.40)
	Bladex.AddAnmLStep(anm_name,0.47)



	#
	# Slip
	#
	anm_name="Lch_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Lch_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Lch_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_fll.BMV","Dth_Fll_Lch",0)
	#Bladex.AddAnmRStep("Dth_Fll_Lch",0.0)
	#Bladex.AddAnmLStep("Dth_Fll_Lch",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_fll2.BMV","Dth_Fll2_Lch",0)
	Bladex.AddAnmRStep("Dth_Fll2_Lch",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Lch",0.0)







############ MUERTES










	anm_name="Lch_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth0.BMV",anm_name,0,"Lich")
	Bladex.AddAnmLStep(anm_name,0.00)       
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.116)       ###
	Bladex.AddAnmLStep(anm_name,0.164)          # 
	Bladex.AddAnmRRelease(anm_name,0.259)       # Added 
	Bladex.AddAnmRStep(anm_name,0.302)          # Previously was entirely missing.
	Bladex.AddAnmLRelease(anm_name,0.386)       #
	Bladex.AddAnmLStep(anm_name,0.418)          #           
	Bladex.AddAnmRRelease(anm_name,0.567)       #
	Bladex.AddAnmRStep(anm_name,0.614)          #           -LeadHead
	Bladex.AddAnmLRelease(anm_name,0.805)       #   
	Bladex.AddAnmRRelease(anm_name,0.810)       #
	Bladex.AddAnmLStep(anm_name,0.965)          #
	Bladex.AddAnmRStep(anm_name,0.970)          ###


	anm_name="Lch_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_c1.BMV",anm_name,0,"Lich")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)

	anm_name="Lch_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_c2.BMV",anm_name,0,"Lich")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)

	anm_name="Lch_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_c3.BMV",anm_name,0,"Lich")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)


	anm_name="Lch_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_c4.BMV",anm_name,0,"Lich")
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


	anm_name="Lch_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_c5.BMV",anm_name,0,"Lich")
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


	anm_name="Lch_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_c6.BMV",anm_name,0,"Lich")
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

	anm_name="Lch_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Lich")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)

	anm_name="Lch_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_n00.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)

	anm_name="Lch_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_n01.BMV",anm_name,0)
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


	anm_name="Lch_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_n02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)

	anm_name="Lch_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_n03.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)

	anm_name="Lch_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_n04.BMV",anm_name,0,"Lich")
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

	anm_name="Lch_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_n05.BMV",anm_name,0,"Lich")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)

	anm_name="Lch_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Lch_dth_n06.BMV",anm_name,0,"Lich")
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





########################################################################
#
#	Hurts
#
########################################################################




	anm_name="Lch_hurt_big"
	Bladex.LoadSampledAnimation("../../Anm/Lch_hurt_big.BMV",anm_name,0) 
	Bladex.AddAnmRStep(anm_name,0.000)          ###
	Bladex.AddAnmLStep(anm_name,0.000)          # 
	Bladex.AddAnmLRelease(anm_name,0.168)       #
	Bladex.AddAnmLStep(anm_name,0.267)          # Added
	Bladex.AddAnmRRelease(anm_name,0.365)       #       -LeadHead
	Bladex.AddAnmRStep(anm_name,0.470)          #
	Bladex.AddAnmLRelease(anm_name,0.548)       #
	Bladex.AddAnmLStep(anm_name,0.689)          #
	Bladex.AddAnmRRelease(anm_name,0.875)       #
	Bladex.AddAnmRStep(anm_name,0.970)          ###
    

	anm_name="Lch_hurt_lite"
	Bladex.LoadSampledAnimation("../../Anm/Lch_hurt_lite.BMV",anm_name,0) 
	Bladex.AddAnmRStep(anm_name,0.000)        ## 
	Bladex.AddAnmLStep(anm_name,0.000)        # 
	Bladex.AddAnmLRelease(anm_name,0.139)     #
	Bladex.AddAnmLStep(anm_name,0.450)        # Added
	Bladex.AddAnmRRelease(anm_name,0.574)     #       -LeadHead
	Bladex.AddAnmRStep(anm_name,0.872)        ###

	anm_name="Lch_hurt_big2"
	Bladex.LoadSampledAnimation("../../Anm/Lch_hurt_big2.BMV",anm_name,0,"Lich") 
	Bladex.AddAnmRStep(anm_name,0.000)      ## 
	Bladex.AddAnmLStep(anm_name,0.000)      # 
	Bladex.AddAnmLRelease(anm_name,0.102)   #
	Bladex.AddAnmRRelease(anm_name,0.106)   # Added
	Bladex.AddAnmRStep(anm_name,0.201)      #         -LeadHead
	Bladex.AddAnmLStep(anm_name,0.222)      ##