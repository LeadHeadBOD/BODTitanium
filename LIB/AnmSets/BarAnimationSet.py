##///
##||| BARANIMATIONSET.PY TITANIUM
##||| Change list:
##||| * Removed steps from _fire type anims where they were not needed.
##||| * Added steps for dth anims that were missing them.
##||| * Removed duplicate "W2H" AnmEvents
##\\\ 

import Bladex
import Enm_Def



def LoadBarAnimationSet(ct_name):

	print "Loading the Barbarian animation sets..."

	#### Relax ####

	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_no.BMV","Rlx_no_Bar",1)
	Bladex.AddAnmRStep("Rlx_no_Bar",0.0)
	Bladex.AddAnmLStep("Rlx_no_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_2h.BMV","Rlx_2h_Bar",1)
	Bladex.AddAnmRStep("Rlx_2h_Bar",0.0)
	Bladex.AddAnmLStep("Rlx_2h_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_1h.BMV","Rlx_1h_Bar",1)
	Bladex.AddAnmRStep("Rlx_1h_Bar",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_b.BMV","Rlx_b_Bar",1)
	Bladex.AddAnmRStep("Rlx_b_Bar",0.0)
	Bladex.AddAnmLStep("Rlx_b_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_2w.BMV","Rlx_2w_Bar",1)
	Bladex.AddAnmRStep("Rlx_2w_Bar",0.0)
	Bladex.AddAnmLStep("Rlx_2w_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_axe.BMV","Rlx_axe_Bar",1)
	Bladex.AddAnmRStep("Rlx_axe_Bar",0.0)
	Bladex.AddAnmLStep("Rlx_axe_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_vt.BMV","Bar_rlx_vt",1)
	Bladex.AddAnmRStep("Bar_rlx_vt",0.0)
	Bladex.AddAnmLStep("Bar_rlx_vt",0.0)


################# ARROJARES ##################




	Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_l_f.BMV","Bar_1tw_l_f",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_1tw_l_f",0.0)
	Bladex.AddAnmLStep("Bar_1tw_l_f",0.0)
	Bladex.AddAnmEvent("Bar_1tw_l_f","ThrowLightFacingEvent",0.3846)

	Bladex.LoadSampledAnimation("../../Anm/Bar_1tw_h_f.BMV","Bar_1tw_h_f",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_1tw_h_f",0.0)
	Bladex.AddAnmLStep("Bar_1tw_h_f",0.0)
	Bladex.AddAnmEvent("Bar_1tw_h_f","ThrowHeavyFacingEvent",0.416)



	### CORRER   ####
	Bladex.LoadSampledAnimation("../../Anm/Bar_jog_no.BMV","Jog_no_Bar",1)
	Bladex.AddAnmRStep("Jog_no_Bar",0.268)
	Bladex.AddAnmRRelease("Jog_no_Bar",0.420)
	Bladex.AddAnmRStep("Jog_no_Bar",0.770)
	Bladex.AddAnmRRelease("Jog_no_Bar",0.914)
	Bladex.AddAnmLStep("Jog_no_Bar",0.000)
	Bladex.AddAnmLRelease("Jog_no_Bar",0.168)
	Bladex.AddAnmLStep("Jog_no_Bar",0.498)
	Bladex.AddAnmLRelease("Jog_no_Bar",0.664)
	Bladex.AddAnmLStep("Jog_no_Bar",1.000)
	Bladex.AddStopTests("Jog_no_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_jog_axe.BMV","Jog_axe_Bar",1)
	Bladex.AddAnmLStep("Jog_axe_Bar",0.00)
	Bladex.AddAnmLRelease("Jog_axe_Bar",0.31)
	Bladex.AddAnmLStep("Jog_axe_Bar",1.0)
	Bladex.AddAnmRStep("Jog_axe_Bar",0.5)
	Bladex.AddAnmRRelease("Jog_axe_Bar",0.79)
	Bladex.AddStopTests("Jog_axe_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_jog_2w.BMV","Jog_2w_Bar",1)
	Bladex.AddAnmLStep("Jog_2w_Bar",0.00)
	Bladex.AddAnmLRelease("Jog_2w_Bar",0.31)
	Bladex.AddAnmLStep("Jog_2w_Bar",1.0)
	Bladex.AddAnmRStep("Jog_2w_Bar",0.5)
	Bladex.AddAnmRRelease("Jog_2w_Bar",0.79)
	Bladex.AddStopTests("Jog_2w_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_jog_1h.BMV","Jog_1h_Bar",1)
	Bladex.AddAnmLStep("Jog_1h_Bar",0.00)
	Bladex.AddAnmLRelease("Jog_1h_Bar",0.31)
	Bladex.AddAnmLStep("Jog_1h_Bar",1.0)
	Bladex.AddAnmRStep("Jog_1h_Bar",0.5)
	Bladex.AddAnmRRelease("Jog_1h_Bar",0.79)
	Bladex.AddStopTests("Jog_1h_Bar")
	Bladex.AddStopTests("Jog_1h_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_jog_2h.BMV","Jog_2h_Bar",1)
	Bladex.AddAnmLStep("Jog_2h_Bar",0.00)
	Bladex.AddAnmLRelease("Jog_2h_Bar",0.31)
	Bladex.AddAnmLStep("Jog_2h_Bar",1.0)
	Bladex.AddAnmRStep("Jog_2h_Bar",0.5)
	Bladex.AddAnmRRelease("Jog_2h_Bar",0.79)
	Bladex.AddStopTests("Jog_2h_Bar")
	Bladex.AddStopTests("Jog_2h_Bar")


	Bladex.LoadSampledAnimation("../../Anm/Bar_jog_b.BMV","Jog_b_Bar",1)
	Bladex.AddAnmLStep("Jog_b_Bar",0.00)
	Bladex.AddAnmLRelease("Jog_b_Bar",0.31)
	Bladex.AddAnmRStep("Jog_b_Bar",0.5)
	Bladex.AddAnmRRelease("Jog_b_Bar",0.79)
	Bladex.AddAnmLStep("Jog_b_Bar",1.0)
	Bladex.AddStopTests("Jog_b_Bar")

	### CORRER ATRAS ###


	anm_name="Bar_jogb_no"
	Bladex.LoadSampledAnimation("../../Anm/Bar_jogb_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.024)
	Bladex.AddAnmRRelease(anm_name,0.122)
	Bladex.AddAnmLStep(anm_name,0.201)
	Bladex.AddAnmRStep(anm_name,0.318)
	Bladex.AddAnmLRelease(anm_name,0.341)
	Bladex.AddAnmRRelease(anm_name,0.427)
	Bladex.AddAnmLStep(anm_name,0.518)
	Bladex.AddAnmRStep(anm_name,0.667)
	Bladex.AddAnmLRelease(anm_name,0.690)
	Bladex.AddAnmRRelease(anm_name,0.748)
	Bladex.AddAnmLStep(anm_name,0.868)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_jogb_b"
	Bladex.LoadSampledAnimation("../../Anm/Bar_jogb_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.135)
	Bladex.AddAnmRStep(anm_name,0.323)
	Bladex.AddAnmRRelease(anm_name,0.473)
	Bladex.AddAnmRStep(anm_name,0.668)
	Bladex.AddAnmRRelease(anm_name,0.802)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.191)
	Bladex.AddAnmLRelease(anm_name,0.353)
	Bladex.AddAnmLStep(anm_name,0.518)
	Bladex.AddAnmLRelease(anm_name,0.697)
	Bladex.AddAnmLStep(anm_name,0.862)
	Bladex.AddAnmLRelease(anm_name,1.000)
	Bladex.AddStopTests(anm_name)


	anm_name="Bar_jogb_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_jogb_axe.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.458)
	Bladex.AddAnmRRelease(anm_name,0.750)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.271)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_jogb_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_jogb_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.024)
	Bladex.AddAnmRRelease(anm_name,0.122)
	Bladex.AddAnmLStep(anm_name,0.201)
	Bladex.AddAnmRStep(anm_name,0.318)
	Bladex.AddAnmLRelease(anm_name,0.341)
	Bladex.AddAnmRRelease(anm_name,0.427)
	Bladex.AddAnmLStep(anm_name,0.518)
	Bladex.AddAnmRStep(anm_name,0.667)
	Bladex.AddAnmLRelease(anm_name,0.690)
	Bladex.AddAnmRRelease(anm_name,0.748)
	Bladex.AddAnmLStep(anm_name,0.868)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)





	### SNEAK   ####

	Bladex.LoadSampledAnimation("../../Anm/Bar_snk_1h.BMV","Snk_1h_Bar",1)  # PLAGUE: If the user has a weapon in hand, and ONLY if the user has a weapon,
	Bladex.AddAnmRStep("Snk_1h_Bar",0.0)                                    # The animation on end (if locked-on) Will still trigger the default step sound
	Bladex.AddAnmLStep("Snk_1h_Bar",0.485)                                  # Most of barb's "_no" states use "_1h" anims, so I don't understand this discrepancy.
	Bladex.AddAnmRStep("Snk_1h_Bar",1.0)                                    # 
	Bladex.AddAnmRRelease("Snk_1h_Bar",0.543)                               # I dont know why, I don't know how
	Bladex.AddAnmLRelease("Snk_1h_Bar",0.952)                               # All I know is that adjusting the timings does nothing
	Bladex.AddStopTests("Snk_1h_Bar")                                       # and I am out of ideas how to fix this crap

	Bladex.LoadSampledAnimation("../../Anm/Bar_snk_b.BMV","Snk_b_Bar",1)
	Bladex.AddAnmRStep("Snk_b_Bar",0.0)
	Bladex.AddAnmLStep("Snk_b_Bar",0.509)
	Bladex.AddAnmRStep("Snk_b_Bar",1.0)
	Bladex.AddAnmRRelease("Snk_b_Bar",0.608)
	Bladex.AddAnmLRelease("Snk_b_Bar",0.952)
	Bladex.AddStopTests("Snk_b_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_snk_2w.BMV","Snk_2w_Bar",1)
	Bladex.AddAnmRStep("Snk_2w_Bar",0.0)
	Bladex.AddAnmLStep("Snk_2w_Bar",0.485)
	Bladex.AddAnmRStep("Snk_2w_Bar",1.0)
	Bladex.AddAnmRRelease("Snk_2w_Bar",0.543)
	Bladex.AddAnmLRelease("Snk_2w_Bar",0.952)
	Bladex.AddStopTests("Snk_2w_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_snk_axe.BMV","Snk_axe_Bar",1)
	Bladex.AddAnmRStep("Snk_axe_Bar",0.0)
	Bladex.AddAnmLStep("Snk_axe_Bar",0.485)
	Bladex.AddAnmRStep("Snk_axe_Bar",1.0)
	Bladex.AddAnmRRelease("Snk_axe_Bar",0.543)
	Bladex.AddAnmLRelease("Snk_axe_Bar",0.952)
	Bladex.AddStopTests("Snk_axe_Bar")


	#### WBK ####

	Bladex.LoadSampledAnimation("../../Anm/Bar_wbk_1h.BMV","Wbk_1h_Bar",1)
	Bladex.AddAnmRStep("Wbk_1h_Bar",0.385)
	Bladex.AddAnmRRelease("Wbk_1h_Bar",1.000)
	Bladex.AddAnmLStep("Wbk_1h_Bar",0.000)
	Bladex.AddAnmLRelease("Wbk_1h_Bar",0.555)
	Bladex.AddAnmLStep("Wbk_1h_Bar",1.000)
	Bladex.AddStopTests("Wbk_1h_Bar")


	anm_name="Wbk_no_Bar"
	Bladex.LoadSampledAnimation("../../Anm/Bar_wbk_no.BMV","Wbk_no_Bar",1)

	Bladex.AddAnmLStep("Wbk_no_Bar",0.0)
	Bladex.AddAnmRStep("Wbk_no_Bar",0.5)
	Bladex.AddAnmLStep("Wbk_no_Bar",1.0)
	Bladex.AddAnmLRelease("Wbk_no_Bar",0.5)
	Bladex.AddAnmRRelease("Wbk_no_Bar",1.0)
	Bladex.AddStopTests("Wbk_no_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_wbk_b.BMV","Wbk_b_Bar",1)
	Bladex.AddAnmLStep("Wbk_b_Bar",0.0)
	Bladex.AddAnmRStep("Wbk_b_Bar",0.5)
	Bladex.AddAnmLStep("Wbk_b_Bar",1.0)
	Bladex.AddAnmLRelease("Wbk_b_Bar",0.5)
	Bladex.AddAnmRRelease("Wbk_b_Bar",1.0)
	Bladex.AddStopTests("Wbk_b_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_wbk_axe.BMV","Wbk_axe_Bar",1)
	Bladex.AddAnmLStep("Wbk_axe_Bar",0.0)
	Bladex.AddAnmRStep("Wbk_axe_Bar",0.5)
	Bladex.AddAnmLStep("Wbk_axe_Bar",1.0)
	Bladex.AddAnmLRelease("Wbk_axe_Bar",0.5)
	Bladex.AddAnmRRelease("Wbk_axe_Bar",1.0)
	Bladex.AddStopTests("Wbk_axe_Bar")

	Bladex.LoadSampledAnimation("../../Anm/Bar_wbk_2w.BMV","Wbk_2w_Bar",1)
	Bladex.AddAnmRStep("Wbk_2w_Bar",0.480)
	Bladex.AddAnmRRelease("Wbk_2w_Bar",1.000)
	Bladex.AddAnmLStep("Wbk_2w_Bar",0.000)
	Bladex.AddAnmLRelease("Wbk_2w_Bar",0.538)
	Bladex.AddAnmLStep("Wbk_2w_Bar",1.000)
	Bladex.AddStopTests("Wbk_2w_Bar")




	#
	#### Caminar ####
	#



	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_no.BMV","Wlk_no_Bar",1)

	Bladex.AddAnmRStep("Wlk_no_Bar",0.0)
	Bladex.AddAnmLStep("Wlk_no_Bar",0.5)
	Bladex.AddAnmRStep("Wlk_no_Bar",1.0)
	Bladex.AddAnmRRelease("Wlk_no_Bar",0.5)
	Bladex.AddAnmLRelease("Wlk_no_Bar",1.0)
	Bladex.AddStopTests("Wlk_no_Bar")



	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_1h.BMV","Wlk_1h_Bar",1)

	Bladex.AddAnmRStep("Wlk_1h_Bar",0.0)
	Bladex.AddAnmLStep("Wlk_1h_Bar",0.5)
	Bladex.AddAnmRStep("Wlk_1h_Bar",1.0)
	Bladex.AddAnmRRelease("Wlk_1h_Bar",0.5)
	Bladex.AddAnmLRelease("Wlk_1h_Bar",1.0)
	Bladex.AddStopTests("Wlk_1h_Bar")



	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_2h.BMV","Wlk_2h_Bar",1)

	Bladex.AddAnmRStep("Wlk_2h_Bar",0.000)
	Bladex.AddAnmRStep("Wlk_2h_Bar",1.000)
	Bladex.AddAnmLStep("Wlk_2h_Bar",0.500)
	Bladex.AddAnmRRelease("Wlk_2h_Bar",0.500)
	Bladex.AddAnmLRelease("Wlk_2h_Bar",1.0)
	Bladex.AddStopTests("Wlk_2h_Bar")




	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_s.BMV","Wlk_s_Bar",1)

	Bladex.AddAnmRStep("Wlk_s_Bar",0.0)
	Bladex.AddAnmLStep("Wlk_s_Bar",0.5)
	Bladex.AddAnmRStep("Wlk_s_Bar",1.0)
	Bladex.AddAnmRRelease("Wlk_s_Bar",0.5)
	Bladex.AddAnmLRelease("Wlk_s_Bar",1.0)
	Bladex.AddStopTests("Wlk_s_Bar")





	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_b.BMV","Wlk_b_Bar",1)

	Bladex.AddAnmRStep("Wlk_b_Bar",0.0)
	Bladex.AddAnmLStep("Wlk_b_Bar",0.5)
	Bladex.AddAnmRStep("Wlk_b_Bar",1.0)
	Bladex.AddAnmRRelease("Wlk_b_Bar",0.5)
	Bladex.AddAnmLRelease("Wlk_b_Bar",1.0)
	Bladex.AddStopTests("Wlk_b_Bar")



	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_2w.BMV","Wlk_2w_Bar",1)

	Bladex.AddAnmRStep("Wlk_2w_Bar",0.0)
	Bladex.AddAnmLStep("Wlk_2w_Bar",0.5)
	Bladex.AddAnmRStep("Wlk_2w_Bar",1.0)
	Bladex.AddAnmRRelease("Wlk_2w_Bar",0.5)
	Bladex.AddAnmLRelease("Wlk_2w_Bar",1.0)
	Bladex.AddStopTests("Wlk_2w_Bar")



	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_axe.BMV","Wlk_axe_Bar",1)

	Bladex.AddAnmRStep("Wlk_axe_Bar",0.0)
	Bladex.AddAnmLStep("Wlk_axe_Bar",0.5)
	Bladex.AddAnmRStep("Wlk_axe_Bar",1.0)
	Bladex.AddAnmRRelease("Wlk_axe_Bar",0.5)
	Bladex.AddAnmLRelease("Wlk_axe_Bar",1.0)
	Bladex.AddStopTests("Wlk_axe_Bar")



	#### Caidas ####

	Bladex.LoadSampledAnimation("../../Anm/Bar_fll_low.BMV","FallLow_Bar",0)
	Bladex.AddAnmRStep("FallLow_Bar",0.0)
	Bladex.AddAnmLStep("FallLow_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_fll_med.BMV","FallMed_Bar",0)
	Bladex.AddAnmRStep("FallMed_Bar",0.0)
	Bladex.AddAnmLStep("FallMed_Bar",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Bar_fll_high.BMV","FallHigh_Bar",0)
	Bladex.AddAnmRStep("FallHigh_Bar",0.0)
	Bladex.AddAnmLStep("FallHigh_Bar",0.0)

	#### Grandes Caidas ####
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Bar",0,"Barbarian")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Bar",0,"Barbarian")
	Bladex.AddAnmRStep("Dth_Fll2_Bar",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Bar",0.0)


	#
	# Ataques
	#


	anm_name="Bar_g_magic"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_magic.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.105)
	Bladex.AddAnmRRelease(anm_name,0.558)
	Bladex.AddAnmRStep(anm_name,0.762)
	Bladex.AddAnmRRelease(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.465)
	Bladex.AddAnmLStep(anm_name,0.545)
	Bladex.AddAnmEvent("Bar_g_magic","LaunchTrail",0.595)

	anm_name="Bar_g_magic2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_magic2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.161)
	Bladex.AddAnmRStep(anm_name,0.361)
	Bladex.AddAnmRRelease(anm_name,0.742)
	Bladex.AddAnmRStep(anm_name,0.913)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.188)
	Bladex.AddAnmLStep(anm_name,0.357)
	Bladex.AddAnmLRelease(anm_name,0.735)
	Bladex.AddAnmLStep(anm_name,0.921)
	Bladex.AddAnmEvent("Bar_g_magic2","LaunchTrail",0.377)

	anm_name="Bar_g_back"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_back.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.477)
	Bladex.AddAnmRStep(anm_name,0.767)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.305)
	Bladex.AddAnmLRelease(anm_name,0.829)
	Bladex.AddAnmLStep(anm_name,1.000)



	Bladex.LoadSampledAnimation("../../Anm/Bar_g_08.BMV","Bar_g_08",0)
	Bladex.AddAnmRStep("Bar_g_08",0)
	Bladex.AddAnmLStep("Bar_g_08",0)
	Bladex.AddAnmRRelease("Bar_g_08",0.29)
	Bladex.AddAnmRStep("Bar_g_08",0.49)
	Bladex.AddAnmRRelease("Bar_g_08",0.72)
	Bladex.AddAnmRStep("Bar_g_08",0.89)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01.BMV","Bar_g_01",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_01",0)
	Bladex.AddAnmLStep("Bar_g_01",0)
	Bladex.AddAnmRRelease("Bar_g_01",0.21)
	Bladex.AddAnmRStep("Bar_g_01",0.36)
	Bladex.AddAnmRRelease("Bar_g_01",0.64)
	Bladex.AddAnmRStep("Bar_g_01",0.83)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_02.BMV","Bar_g_02",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_02",0)
	Bladex.AddAnmLStep("Bar_g_02",0)
	Bladex.AddAnmRRelease("Bar_g_02",0.15)
	Bladex.AddAnmRStep("Bar_g_02",0.27)
	Bladex.AddAnmRRelease("Bar_g_02",0.55)
	Bladex.AddAnmRStep("Bar_g_02",0.74)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_05.BMV","Bar_g_05",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_05",0)
	Bladex.AddAnmLStep("Bar_g_05",0)
	Bladex.AddAnmRRelease("Bar_g_05",0.28)
	Bladex.AddAnmRStep("Bar_g_05",0.5)
	Bladex.AddAnmRRelease("Bar_g_05",0.72)
	Bladex.AddAnmRStep("Bar_g_05",0.9)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_06.BMV","Bar_g_06",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_06",0)
	Bladex.AddAnmLStep("Bar_g_06",0)
	Bladex.AddAnmRRelease("Bar_g_06",0.19)
	Bladex.AddAnmRStep("Bar_g_06",0.37)
	Bladex.AddAnmRRelease("Bar_g_06",0.67)
	Bladex.AddAnmRStep("Bar_g_06",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_07.BMV","Bar_g_07",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_07",0)
	Bladex.AddAnmLStep("Bar_g_07",0)
	Bladex.AddAnmRRelease("Bar_g_07",0.15)
	Bladex.AddAnmRStep("Bar_g_07",0.35)
	Bladex.AddAnmRRelease("Bar_g_07",0.51)
	Bladex.AddAnmRStep("Bar_g_07",0.72)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_09.BMV","Bar_g_09",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_09",0)
	Bladex.AddAnmLStep("Bar_g_09",0)
	Bladex.AddAnmRRelease("Bar_g_09",0.23)
	Bladex.AddAnmRStep("Bar_g_09",0.36)
	Bladex.AddAnmRRelease("Bar_g_09",0.55)
	Bladex.AddAnmRStep("Bar_g_09",0.71)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_13.BMV","Bar_g_13",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_13",0)
	Bladex.AddAnmLStep("Bar_g_13",0)
	Bladex.AddAnmRRelease("Bar_g_13",0.41)
	Bladex.AddAnmRStep("Bar_g_13",0.57)
	Bladex.AddAnmLRelease("Bar_g_13",0.76)
	Bladex.AddAnmLStep("Bar_g_13",0.89)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_18.BMV","Bar_g_18",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_18",0)
	Bladex.AddAnmLStep("Bar_g_18",0)
	Bladex.AddAnmRRelease("Bar_g_18",0.37)
	Bladex.AddAnmRStep("Bar_g_18",0.50)
	Bladex.AddAnmLRelease("Bar_g_18",0.77)
	Bladex.AddAnmLStep("Bar_g_18",0.90)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_18.BMV","Bar_g_14",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_14",0)
	Bladex.AddAnmLStep("Bar_g_14",0)
	Bladex.AddAnmLRelease("Bar_g_14",0.15)
	Bladex.AddAnmLStep("Bar_g_14",0.37)
	Bladex.AddAnmRRelease("Bar_g_14",0.43)
	Bladex.AddAnmRStep("Bar_g_14",0.56)
	Bladex.AddAnmLRelease("Bar_g_14",0.73)
	Bladex.AddAnmLStep("Bar_g_14",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_11.BMV","Bar_g_11",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_11",0)
	Bladex.AddAnmLStep("Bar_g_11",0)
	Bladex.AddAnmRRelease("Bar_g_11",0.4)
	Bladex.AddAnmRStep("Bar_g_11",0.55)
	Bladex.AddAnmLRelease("Bar_g_11",0.78)
	Bladex.AddAnmLStep("Bar_g_11",0.93)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_16.BMV","Bar_g_16",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_16",0)
	Bladex.AddAnmLStep("Bar_g_16",0)
	Bladex.AddAnmRRelease("Bar_g_16",0.16)
	Bladex.AddAnmRStep("Bar_g_16",0.275)
	Bladex.AddAnmLRelease("Bar_g_16",0.54)
	Bladex.AddAnmLStep("Bar_g_16",0.675)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_12.BMV","Bar_g_12",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_12",0)
	Bladex.AddAnmLStep("Bar_g_12",0)
	Bladex.AddAnmRRelease("Bar_g_12",0.4)
	Bladex.AddAnmRStep("Bar_g_12",0.52)
	Bladex.AddAnmLRelease("Bar_g_12",0.71)
	Bladex.AddAnmLStep("Bar_g_12",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_17.BMV","Bar_g_17",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_17",0)
	Bladex.AddAnmLStep("Bar_g_17",0)
	Bladex.AddAnmRRelease("Bar_g_17",0.16)
	Bladex.AddAnmRStep("Bar_g_17",0.27)
	Bladex.AddAnmLRelease("Bar_g_17",0.53)
	Bladex.AddAnmLStep("Bar_g_17",0.65)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_15.BMV","Bar_g_15",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_15",0)
	Bladex.AddAnmLStep("Bar_g_15",0)
	Bladex.AddAnmRRelease("Bar_g_15",0.17)
	Bladex.AddAnmRStep("Bar_g_15",0.35)
	Bladex.AddAnmLRelease("Bar_g_15",0.56)
	Bladex.AddAnmLStep("Bar_g_15",0.76)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_21.BMV","Bar_g_21",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_21",0)
	Bladex.AddAnmLStep("Bar_g_21",0)
	Bladex.AddAnmRRelease("Bar_g_21",0.51)
	Bladex.AddAnmRStep("Bar_g_21",0.669)
	Bladex.AddAnmLRelease("Bar_g_21",0.696)
	Bladex.AddAnmLStep("Bar_g_21",0.834)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_22.BMV","Bar_g_22",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_22",0)
	Bladex.AddAnmLStep("Bar_g_22",0)
	Bladex.AddAnmRRelease("Bar_g_22",0.474)
	Bladex.AddAnmRStep("Bar_g_22",0.544)
	Bladex.AddAnmRRelease("Bar_g_22",0.605)
	Bladex.AddAnmRStep("Bar_g_22",0.67)
	Bladex.AddAnmRRelease("Bar_g_22",0.781)
	Bladex.AddAnmRStep("Bar_g_22",0.847)
	Bladex.AddAnmLRelease("Bar_g_22",0.2)
	Bladex.AddAnmLStep("Bar_g_22",0.433)
	Bladex.AddAnmLRelease("Bar_g_22",0.549)
	Bladex.AddAnmLStep("Bar_g_22",0.6)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_23.BMV","Bar_g_23",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_23",0)
	Bladex.AddAnmLStep("Bar_g_23",0)
	Bladex.AddAnmRRelease("Bar_g_23",0.529)
	Bladex.AddAnmRStep("Bar_g_23",0.743)
	Bladex.AddAnmLRelease("Bar_g_23",0.75)
	Bladex.AddAnmLStep("Bar_g_23",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_26.BMV","Bar_g_26",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_26",0)
	Bladex.AddAnmLStep("Bar_g_26",0)
	Bladex.AddAnmRRelease("Bar_g_26",0.135)
	Bladex.AddAnmRStep("Bar_g_26",0.236)
	Bladex.AddAnmLRelease("Bar_g_26",0.48)
	Bladex.AddAnmLStep("Bar_g_26",0.682)
	Bladex.AddAnmLRelease("Bar_g_26",0.79)
	Bladex.AddAnmLStep("Bar_g_26",0.885)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_27.BMV","Bar_g_27",0,"Barbarian")
	Bladex.AddAnmRStep("Bar_g_27",0)
	Bladex.AddAnmLStep("Bar_g_27",0)
	Bladex.AddAnmRRelease("Bar_g_27",0.28)
	Bladex.AddAnmRStep("Bar_g_27",0.5)
	Bladex.AddAnmLRelease("Bar_g_27",0.72)
	Bladex.AddAnmLStep("Bar_g_27",0.74)


	anm_name="Bar_g_31"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_31.BMV",anm_name,0,"Barbarian")
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







	anm_name="Bar_g_06lowkata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_06lowkata_new.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.041)
	Bladex.AddAnmRStep(anm_name,0.453)
	Bladex.AddAnmRRelease(anm_name,0.692)
	Bladex.AddAnmRStep(anm_name,0.865)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.384)
	Bladex.AddAnmLStep(anm_name,0.680)



	############################################
	#######GOLPES ESPADA A DOS MANOS############


	anm_name="Bar_g2h_21_7"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_21_7.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.462)
	Bladex.AddAnmRStep(anm_name,0.673)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.327)
	Bladex.AddAnmLStep(anm_name,0.404)
	Bladex.AddAnmLRelease(anm_name,0.673)
	Bladex.AddAnmLStep(anm_name,0.808)


	anm_name="Bar_g2h_02kata"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_02kata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.325)
	Bladex.AddAnmRStep(anm_name,0.450)
	Bladex.AddAnmLStep(anm_name,-0.004)


	anm_name="Bar_g2h_21_2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_21_2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.125)
	Bladex.AddAnmRStep(anm_name,0.281)
	Bladex.AddAnmRRelease(anm_name,0.422)
	Bladex.AddAnmRStep(anm_name,0.484)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.750)
	Bladex.AddAnmLStep(anm_name,0.906)




	anm_name="Bar_g2h_21_6kata"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_21_6kata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.290)
	Bladex.AddAnmRStep(anm_name,0.418)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.200)
	Bladex.AddAnmLStep(anm_name,0.277)
	Bladex.AddAnmLRelease(anm_name,0.555)
	Bladex.AddAnmLStep(anm_name,0.684)

	anm_name="Bar_g2h_b7"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_b7.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.143)
	Bladex.AddAnmRStep(anm_name,0.304)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.054)
	Bladex.AddAnmLStep(anm_name,0.196)
	Bladex.AddAnmLRelease(anm_name,0.321)
	Bladex.AddAnmLStep(anm_name,0.393)
	Bladex.AddAnmLRelease(anm_name,0.518)
	Bladex.AddAnmLStep(anm_name,0.696)
	Bladex.AddAnmEvent("Bar_g2h_b7","W2hToLeft",0.325)
	Bladex.AddAnmEvent("Bar_g2h_b7","W2hToRight",0.821)

	anm_name="Bar_g2h_b29"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_b29.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.138)
	Bladex.AddAnmRStep(anm_name,0.322)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.644)
	Bladex.AddAnmLStep(anm_name,0.874)
	Bladex.AddAnmEvent("Bar_g2h_b29","W2hToLeft",0.03)


	anm_name="Bar_g2h_12low"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_12low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.467)
	Bladex.AddAnmRStep(anm_name,0.851)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.181)
	Bladex.AddAnmLStep(anm_name,0.429)
	Bladex.AddAnmLRelease(anm_name,0.866)
	Bladex.AddAnmLStep(anm_name,1.000)


	anm_name="Bar_g2h_19"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_19.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.313)
	Bladex.AddAnmRStep(anm_name,0.790)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.017)
	Bladex.AddAnmLStep(anm_name,0.360)
	Bladex.AddAnmEvent("Bar_g2h_19","W2hToLeft",0.03)
	Bladex.AddAnmEvent("Bar_g2h_19","W2hToRight",0.93)


	anm_name="Bar_g2h_26_b6"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_26_b6.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.176)
	Bladex.AddAnmRStep(anm_name,0.300)
	Bladex.AddAnmRRelease(anm_name,0.442)
	Bladex.AddAnmRStep(anm_name,0.590)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.153)
	Bladex.AddAnmLRelease(anm_name,0.349)
	Bladex.AddAnmLRelease(anm_name,0.349)
	Bladex.AddAnmLStep(anm_name,0.521)
	Bladex.AddAnmLStep(anm_name,0.521)
	Bladex.AddAnmLRelease(anm_name,0.608)
	Bladex.AddAnmLStep(anm_name,0.972)


	anm_name="Bar_g2h_26"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_26.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.139)
	Bladex.AddAnmRStep(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.361)
	Bladex.AddAnmLStep(anm_name,0.806)


	anm_name="Bar_g2h_28"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_28.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.194)
	Bladex.AddAnmRStep(anm_name,0.417)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.556)
	Bladex.AddAnmLStep(anm_name,0.694)
	Bladex.AddAnmEvent("Bar_g2h_28","W2hToLeft",0.4)
	Bladex.AddAnmEvent("Bar_g2h_28","W2hToRight",0.9)


	anm_name="Bar_g2h_31_2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_31_2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.208)
	Bladex.AddAnmRStep(anm_name,0.583)
	Bladex.AddAnmRRelease(anm_name,0.625)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.063)
	Bladex.AddAnmLStep(anm_name,0.167)
	Bladex.AddAnmLRelease(anm_name,0.625)
	Bladex.AddAnmLStep(anm_name,0.833)


	anm_name="Bar_g2h_b6"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_b6.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.173)
	Bladex.AddAnmRStep(anm_name,0.365)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.019)
	Bladex.AddAnmLStep(anm_name,0.154)
	Bladex.AddAnmLRelease(anm_name,0.365)
	Bladex.AddAnmLStep(anm_name,0.462)
	Bladex.AddAnmLRelease(anm_name,0.615)
	Bladex.AddAnmLStep(anm_name,0.827)


	anm_name="Bar_g2h_b6kata"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_b6kata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.337)
	Bladex.AddAnmRStep(anm_name,0.481)
	Bladex.AddAnmRRelease(anm_name,0.742)
	Bladex.AddAnmRStep(anm_name,0.824)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.253)
	Bladex.AddAnmLStep(anm_name,0.326)
	Bladex.AddAnmLRelease(anm_name,0.355)
	Bladex.AddAnmLStep(anm_name,0.418)
	Bladex.AddAnmLRelease(anm_name,0.504)
	Bladex.AddAnmLStep(anm_name,0.841)


	anm_name="Bar_g2h_b6low"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_b6low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRStep(anm_name,0.073)
	Bladex.AddAnmRRelease(anm_name,0.171)
	Bladex.AddAnmRStep(anm_name,0.341)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.098)
	Bladex.AddAnmLStep(anm_name,0.293)
	Bladex.AddAnmLRelease(anm_name,0.415)
	Bladex.AddAnmLStep(anm_name,0.854)


	anm_name="Bar_g2h_b6lowkata"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_b6lowkata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.231)
	Bladex.AddAnmRStep(anm_name,0.269)
	Bladex.AddAnmRRelease(anm_name,0.346)
	Bladex.AddAnmRStep(anm_name,0.481)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.288)
	Bladex.AddAnmLStep(anm_name,0.442)
	Bladex.AddAnmLRelease(anm_name,0.538)
	Bladex.AddAnmLStep(anm_name,0.885)


	anm_name="Bar_g2h_earthpow"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_earthpow.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.662)
	Bladex.AddAnmRStep(anm_name,0.824)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Bar_g2h_s7"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_s7.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.186)
	Bladex.AddAnmRStep(anm_name,0.353)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.213)
	Bladex.AddAnmLStep(anm_name,0.520)


	anm_name="Bar_g2h_01"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_01.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.117)
	Bladex.AddAnmRStep(anm_name,0.331)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.835)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Bar_g2h_01","W2hToLeft",0.1)
	Bladex.AddAnmEvent("Bar_g2h_01","W2hToRight",1)



	anm_name="Bar_g2h_02"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.134)
	Bladex.AddAnmRStep(anm_name,0.305)
	Bladex.AddAnmRRelease(anm_name,0.634)
	Bladex.AddAnmRStep(anm_name,0.827)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Bar_g2h_02","W2hToLeft",0.11)
	Bladex.AddAnmEvent("Bar_g2h_02","W2hToRight",1)

	anm_name="Bar_g2h_02low"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_02low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.254)
	Bladex.AddAnmLRelease(anm_name,0.784)
	Bladex.AddAnmLStep(anm_name,0.896)
	Bladex.AddAnmLRelease(anm_name,1.000)
	Bladex.AddAnmEvent("Bar_g2h_02low","W2hToLeft",0.12)
	Bladex.AddAnmEvent("Bar_g2h_02low","W2hToRight",1)

	anm_name="Bar_g2h_07"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_07.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.223)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.802)
	Bladex.AddAnmEvent("Bar_g2h_07","W2hToLeft",0)
	Bladex.AddAnmEvent("Bar_g2h_07","W2hToRight",1)

	anm_name="Bar_g2h_08"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_08.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.173)
	Bladex.AddAnmRStep(anm_name,0.351)
	Bladex.AddAnmRRelease(anm_name,0.549)
	Bladex.AddAnmRStep(anm_name,0.743)
	Bladex.AddAnmLStep(anm_name,0.130)
	Bladex.AddAnmLRelease(anm_name,1.000)
	Bladex.AddAnmEvent("Bar_g2h_08","W2hToLeft",0.2)
	Bladex.AddAnmEvent("Bar_g2h_08","W2hToRight",1)


	anm_name="Bar_g2h_11"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_11.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.258)
	Bladex.AddAnmRStep(anm_name,0.393)
	Bladex.AddAnmLStep(anm_name,0.228)
	Bladex.AddAnmLRelease(anm_name,1.000)



	anm_name="Bar_g2h_12"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_12.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.305)
	Bladex.AddAnmRStep(anm_name,0.634)
	Bladex.AddAnmLStep(anm_name,0.220)
	Bladex.AddAnmLRelease(anm_name,1.000)
	Bladex.AddAnmEvent("Bar_g2h_12","W2hToLeft",0.2)
	Bladex.AddAnmEvent("Bar_g2h_12","W2hToRight",1)

	anm_name="Bar_g2h_13"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_13.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.179)
	Bladex.AddAnmRStep(anm_name,0.275)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.238)
	Bladex.AddAnmLStep(anm_name,0.357)
	Bladex.AddAnmEvent("Bar_g2h_13","W2hToLeft",0.11)
	Bladex.AddAnmEvent("Bar_g2h_13","W2hToRight",1)


	anm_name="Bar_g2h_17"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_17.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRStep(anm_name,0.219)
	Bladex.AddAnmRRelease(anm_name,0.360)
	Bladex.AddAnmRStep(anm_name,0.658)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.118)
	Bladex.AddAnmLStep(anm_name,0.259)
	# Bladex.AddAnmEvent("Bar_g2h_17","W2hToLeft",0)
	# Bladex.AddAnmEvent("Bar_g2h_17","W2hToRight",1)
	Bladex.AddAnmEvent("Bar_g2h_17","W2hToLeft",0.23)      # Unused anim, but now has correct timings
	Bladex.AddAnmEvent("Bar_g2h_17","W2hToRight",0.93)     # Will re-introduce at some later point -LeadHead


	anm_name="Bar_g2h_22kata_6"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_22kata_6.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.261)
	Bladex.AddAnmRStep(anm_name,0.363)
	Bladex.AddAnmRRelease(anm_name,0.635)
	Bladex.AddAnmRStep(anm_name,0.794)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.171)
	Bladex.AddAnmLStep(anm_name,0.238)
	Bladex.AddAnmLRelease(anm_name,0.522)
	Bladex.AddAnmLStep(anm_name,0.613)


	anm_name="Bar_g2h_26low_b6"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_26low_b6.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.171)
	Bladex.AddAnmRStep(anm_name,0.304)
	Bladex.AddAnmRRelease(anm_name,0.450)
	Bladex.AddAnmRStep(anm_name,0.586)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.381)
	Bladex.AddAnmLStep(anm_name,0.508)
	Bladex.AddAnmLRelease(anm_name,0.831)
	Bladex.AddAnmLStep(anm_name,0.967)


	anm_name="Bar_g2h_26low"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_26low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.112)
	Bladex.AddAnmRStep(anm_name,0.309)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.581)
	Bladex.AddAnmLStep(anm_name,0.790)

	anm_name="Bar_g2h_back"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_back.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.213)
	Bladex.AddAnmRRelease(anm_name,0.701)
	Bladex.AddAnmRStep(anm_name,0.928)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.346)
	Bladex.AddAnmLStep(anm_name,0.705)
	Bladex.AddAnmEvent("Bar_g2h_back","W2hToLeft",0)
	Bladex.AddAnmEvent("Bar_g2h_back","W2hToRight",1)




	anm_name="Bar_g2h_s1"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_s1.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.149)
	Bladex.AddAnmRStep(anm_name,0.261)
	Bladex.AddAnmRRelease(anm_name,0.423)
	Bladex.AddAnmRStep(anm_name,0.700)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.191)
	Bladex.AddAnmLStep(anm_name,0.318)
	# Bladex.AddAnmEvent("Bar_g2h_s1","W2hToLeft",0)
	# Bladex.AddAnmEvent("Bar_g2h_s1","W2hToRight",1)
	Bladex.AddAnmEvent("Bar_g2h_s1","W2hToLeft",0.43)      # Unused anim, but now has correct timings
	Bladex.AddAnmEvent("Bar_g2h_s1","W2hToRight",0.73)     # Will re-introduce at some later point -LeadHead
	
	

	anm_name="Bar_g2h_s8"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_s8.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.403)
	Bladex.AddAnmRRelease(anm_name,0.581)
	Bladex.AddAnmRStep(anm_name,0.724)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.207)
	Bladex.AddAnmLStep(anm_name,0.410)
	Bladex.AddAnmLRelease(anm_name,0.746)
	Bladex.AddAnmLStep(anm_name,0.823)
	Bladex.AddAnmEvent("Bar_g2h_s8","W2hToLeft",0.11)
	Bladex.AddAnmEvent("Bar_g2h_s8","W2hToRight",1)

	anm_name="Bar_g2h_s8kata"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_s8kata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.218)
	Bladex.AddAnmRStep(anm_name,0.321)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.252)
	Bladex.AddAnmLStep(anm_name,0.342)
	Bladex.AddAnmEvent("Bar_g2h_s8kata","W2hToLeft",0)
	Bladex.AddAnmEvent("Bar_g2h_s8kata","W2hToRight",1)


	anm_name="Bar_g2h_d_l"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_d_l.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.143)
	Bladex.AddAnmRStep(anm_name,0.321)
	Bladex.AddAnmRRelease(anm_name,0.639)
	Bladex.AddAnmRStep(anm_name,0.788)
	Bladex.AddAnmLStep(anm_name,0.152)
	Bladex.AddAnmLRelease(anm_name,0.368)
	Bladex.AddAnmLStep(anm_name,0.601)
	Bladex.AddAnmLRelease(anm_name,0.833)
	Bladex.AddAnmLStep(anm_name,0.918)
	#Bladex.AddAnmEvent("Bar_g2h_d_l","W2hToLeft",0.8)
	#Bladex.AddAnmEvent("Bar_g2h_d_l","W2hToRight",1)

	anm_name="Bar_g2h_d_r"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_d_r.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.089)
	Bladex.AddAnmRStep(anm_name,0.240)
	Bladex.AddAnmRRelease(anm_name,0.480)
	Bladex.AddAnmRStep(anm_name,0.676)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.228)
	Bladex.AddAnmLStep(anm_name,0.404)
	Bladex.AddAnmEvent("Bar_g2h_d_r","W2hToLeft",0.8)
	Bladex.AddAnmEvent("Bar_g2h_d_r","W2hToRight",1)



	############################################
	#######GOLPES  HACHA A DOS MANOS############


	anm_name="Bar_g_axe01"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe01.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.111)
	Bladex.AddAnmRStep(anm_name,0.278)
	Bladex.AddAnmRRelease(anm_name,0.694)
	Bladex.AddAnmRStep(anm_name,0.917)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Bar_g_axe01","W2hToLeft",0.22)
	Bladex.AddAnmEvent("Bar_g_axe01","W2hToRight",0.93)


	anm_name="Bar_g_axe02"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.125)
	Bladex.AddAnmRStep(anm_name,0.281)
	Bladex.AddAnmRRelease(anm_name,0.578)
	Bladex.AddAnmRStep(anm_name,0.766)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Bar_g_axe02","W2hToLeft",0.225)
	Bladex.AddAnmEvent("Bar_g_axe02","W2hToRight",0.93)


	anm_name="Bar_g_axe08"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe08.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.160)
	Bladex.AddAnmRStep(anm_name,0.360)
	Bladex.AddAnmRRelease(anm_name,0.586)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Bar_g_axe08","W2hToLeft",0.2)
	Bladex.AddAnmEvent("Bar_g_axe08","W2hToRight",0.93)


	anm_name="Bar_g_axe111"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe111.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.122)
	Bladex.AddAnmRStep(anm_name,0.189)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.135)
	Bladex.AddAnmLStep(anm_name,0.230)
	Bladex.AddAnmLRelease(anm_name,0.649)
	Bladex.AddAnmLStep(anm_name,0.770)
	Bladex.AddAnmEvent("Bar_g_axe111","W2hToLeft",0.247)
	Bladex.AddAnmEvent("Bar_g_axe111","W2hToRight",0.93)


	anm_name="Bar_g_axe12"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe12.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.086)
	Bladex.AddAnmRStep(anm_name,0.190)
	Bladex.AddAnmRRelease(anm_name,0.310)
	Bladex.AddAnmRStep(anm_name,0.759)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.052)
	Bladex.AddAnmLStep(anm_name,0.224)
	Bladex.AddAnmLRelease(anm_name,0.862)
	Bladex.AddAnmLStep(anm_name,0.983)
	Bladex.AddAnmEvent("Bar_g_axe12","W2hToLeft",0.27)
	Bladex.AddAnmEvent("Bar_g_axe12","W2hToRight",0.93)


	anm_name="Bar_g_axe13"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe13.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.172)
	Bladex.AddAnmRStep(anm_name,0.266)
	Bladex.AddAnmRRelease(anm_name,0.359)
	Bladex.AddAnmRStep(anm_name,0.641)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.172)
	Bladex.AddAnmLStep(anm_name,0.297)
	Bladex.AddAnmEvent("Bar_g_axe13","W2hToLeft",0.29)
	Bladex.AddAnmEvent("Bar_g_axe13","W2hToRight",0.93)


	anm_name="Bar_g_axe18"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe18.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.325)
	Bladex.AddAnmRStep(anm_name,0.453)
	Bladex.AddAnmRRelease(anm_name,0.529)
	Bladex.AddAnmRStep(anm_name,0.591)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.054)
	Bladex.AddAnmLStep(anm_name,0.402)
	Bladex.AddAnmLRelease(anm_name,0.663)
	Bladex.AddAnmLStep(anm_name,0.736)
	Bladex.AddAnmEvent("Bar_g_axe18","W2hToLeft",0.25)
	Bladex.AddAnmEvent("Bar_g_axe18","W2hToRight",0.93)


	anm_name="Bar_g_axe21"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe21.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.222)
	Bladex.AddAnmRStep(anm_name,0.392)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.236)
	Bladex.AddAnmLStep(anm_name,0.346)
	Bladex.AddAnmLRelease(anm_name,0.603)
	Bladex.AddAnmLStep(anm_name,0.776)
	Bladex.AddAnmEvent("Bar_g_axe21","W2hToLeft",0.375)
	Bladex.AddAnmEvent("Bar_g_axe21","W2hToRight",0.93)


	anm_name="Bar_g_axe211"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe211.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.130)
	Bladex.AddAnmRStep(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.537)
	Bladex.AddAnmLStep(anm_name,0.815)
	Bladex.AddAnmEvent("Bar_g_axe211","W2hToLeft",0.352)
	Bladex.AddAnmEvent("Bar_g_axe211","W2hToRight",0.93)


	anm_name="Bar_g_axe28"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe28.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.179)
	Bladex.AddAnmRStep(anm_name,0.411)
	Bladex.AddAnmRRelease(anm_name,0.743)
	Bladex.AddAnmRStep(anm_name,0.862)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.217)
	Bladex.AddAnmLStep(anm_name,0.461)
	Bladex.AddAnmLRelease(anm_name,0.601)
	Bladex.AddAnmLStep(anm_name,0.794)
	Bladex.AddAnmEvent("Bar_g_axe28","W2hToLeft",0.393)
	Bladex.AddAnmEvent("Bar_g_axe28","W2hToRight",0.93)


	anm_name="Bar_g_axe30"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe30.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.233)
	Bladex.AddAnmRStep(anm_name,0.385)
	Bladex.AddAnmRRelease(anm_name,0.472)
	Bladex.AddAnmRStep(anm_name,0.572)
	Bladex.AddAnmRRelease(anm_name,0.797)
	Bladex.AddAnmRStep(anm_name,0.842)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.415)
	Bladex.AddAnmLStep(anm_name,0.456)
	Bladex.AddAnmLRelease(anm_name,0.516)
	Bladex.AddAnmLStep(anm_name,0.599)


	anm_name="Bar_g_axe31"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe31.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.128)
	Bladex.AddAnmRStep(anm_name,0.248)
	Bladex.AddAnmRRelease(anm_name,0.397)
	Bladex.AddAnmRStep(anm_name,0.476)
	Bladex.AddAnmRRelease(anm_name,0.609)
	Bladex.AddAnmRStep(anm_name,0.720)
	Bladex.AddAnmRRelease(anm_name,0.793)
	Bladex.AddAnmRStep(anm_name,0.823)
	Bladex.AddAnmLStep(anm_name,0.101)
	Bladex.AddAnmLStep(anm_name,0.101)
	Bladex.AddAnmLRelease(anm_name,0.250)
	Bladex.AddAnmLStep(anm_name,0.271)
	Bladex.AddAnmLRelease(anm_name,0.325)
	Bladex.AddAnmLStep(anm_name,0.362)
	Bladex.AddAnmLRelease(anm_name,0.615)
	Bladex.AddAnmLStep(anm_name,0.723)
	Bladex.AddAnmLRelease(anm_name,0.790)
	Bladex.AddAnmLStep(anm_name,0.825)
	Bladex.AddAnmLRelease(anm_name,1.000)
	Bladex.AddAnmEvent("Bar_g_axe31","W2hToLeft",0.12)
	Bladex.AddAnmEvent("Bar_g_axe31","W2hToRight",0.93)



	anm_name="Bar_g_axe32"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe32.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.146)
	Bladex.AddAnmRStep(anm_name,0.228)
	Bladex.AddAnmRRelease(anm_name,0.317)
	Bladex.AddAnmRStep(anm_name,0.398)
	Bladex.AddAnmRRelease(anm_name,0.483)
	Bladex.AddAnmRStep(anm_name,0.779)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.076)
	Bladex.AddAnmLStep(anm_name,0.264)
	Bladex.AddAnmLRelease(anm_name,0.384)
	Bladex.AddAnmLStep(anm_name,0.423)
	Bladex.AddAnmEvent("Bar_g_axe32","W2hToLeft",0.04)
	Bladex.AddAnmEvent("Bar_g_axe32","W2hToRight",0.93)

	anm_name="Bar_g_axe33"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe33.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.163)
	Bladex.AddAnmRStep(anm_name,0.258)
	Bladex.AddAnmRRelease(anm_name,0.362)
	Bladex.AddAnmRStep(anm_name,0.413)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.077)
	Bladex.AddAnmLStep(anm_name,0.306)
	Bladex.AddAnmEvent("Bar_g_axe33","W2hToLeft",0.1875)
	Bladex.AddAnmEvent("Bar_g_axe33","W2hToRight",0.93)

	anm_name="Bar_g_axe34"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe34.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.099)
	Bladex.AddAnmRStep(anm_name,0.210)
	Bladex.AddAnmRRelease(anm_name,0.277)
	Bladex.AddAnmRStep(anm_name,0.356)
	Bladex.AddAnmRRelease(anm_name,0.456)
	Bladex.AddAnmRStep(anm_name,0.508)
	Bladex.AddAnmRRelease(anm_name,0.706)
	Bladex.AddAnmRStep(anm_name,0.779)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.060)
	Bladex.AddAnmLStep(anm_name,0.236)
	Bladex.AddAnmLRelease(anm_name,0.289)
	Bladex.AddAnmLStep(anm_name,0.394)
	Bladex.AddAnmEvent("Bar_g_axe34","W2hToLeft",0.253)
	Bladex.AddAnmEvent("Bar_g_axe34","W2hToRight",0.93)

	anm_name="Bar_g_axe_b2kata"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe_b2kata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.133)
	Bladex.AddAnmRStep(anm_name,0.266)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.352)
	Bladex.AddAnmLStep(anm_name,0.540)
#	eventos de pies heredados de la animaci�n con lanza de la amz

	anm_name="Bar_g_axe08strong"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe08strong.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.292)
	Bladex.AddAnmRStep(anm_name,0.406)
	Bladex.AddAnmRRelease(anm_name,0.639)
	Bladex.AddAnmRStep(anm_name,0.893)
	Bladex.AddAnmLStep(anm_name,0.000)
	# Bladex.AddAnmEvent("Bar_g_axe34","W2hToLeft",0.22)        ## PLAGUE: Wrong animation name, which prints errors in console
	# Bladex.AddAnmEvent("Bar_g_axe34","W2hToRight",0.93)       ## every time double edge special is
	Bladex.AddAnmEvent(anm_name,"W2hToLeft",0.22)               # old commented out,
	Bladex.AddAnmEvent(anm_name,"W2hToRight",0.93)              # Added -LeadHead

	anm_name="Bar_g_axe_3s2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe_3s2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.324)
	Bladex.AddAnmRStep(anm_name,0.538)
	Bladex.AddAnmRRelease(anm_name,0.691)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.388)
	Bladex.AddAnmLStep(anm_name,0.662)
	Bladex.AddAnmLRelease(anm_name,0.881)
	Bladex.AddAnmLStep(anm_name,0.944)
	# Bladex.AddAnmEvent("Bar_g_axe34","W2hToLeft",0.1)          ## PLAGUE: Wrong animation name, which prints errors in console
	# Bladex.AddAnmEvent("Bar_g_axe34","W2hToRight",0.93)        ## every time double edge special is used 
	Bladex.AddAnmEvent(anm_name,"W2hToLeft",0.1)                 # old commented out,
	Bladex.AddAnmEvent(anm_name,"W2hToRight",0.93)               # Added -LeadHead
#	eventos de pies heredados de la animaci�n con lanza de la amz


	anm_name="Bar_g_axe_32kata_b2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe_32kata_b2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.323)
	Bladex.AddAnmRStep(anm_name,0.534)
	Bladex.AddAnmRRelease(anm_name,0.759)
	Bladex.AddAnmRStep(anm_name,0.870)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.252)
	Bladex.AddAnmLStep(anm_name,0.318)
	Bladex.AddAnmLRelease(anm_name,0.410)
	Bladex.AddAnmLStep(anm_name,0.551)
	Bladex.AddAnmLRelease(anm_name,0.826)
	Bladex.AddAnmLStep(anm_name,0.906)
#	eventos de pies heredados de la animaci�n con lanza de la amz


	anm_name="Bar_g_axe_26kata"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe_26kata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.089)
	Bladex.AddAnmRStep(anm_name,0.200)
	Bladex.AddAnmRRelease(anm_name,0.468)
	Bladex.AddAnmRStep(anm_name,0.618)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.372)
	Bladex.AddAnmLStep(anm_name,0.472)
	Bladex.AddAnmLRelease(anm_name,0.828)
	Bladex.AddAnmLStep(anm_name,0.875)
#	eventos de pies heredados de la animaci�n con lanza de la amz


	anm_name="Bar_g_axe_2katab6low"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_axe_2katab6low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.274)
	Bladex.AddAnmRStep(anm_name,0.448)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.214)
	Bladex.AddAnmLStep(anm_name,0.285)
	Bladex.AddAnmLRelease(anm_name,0.695)
	Bladex.AddAnmLStep(anm_name,0.875)
#	eventos de pies heredados de la animaci�n con lanza de la amz�


	#golpes torpes con lanza



	anm_name="Bar_g_bad_no"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_no.BMV",anm_name,0,"Barbarian_N")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)

	anm_name="Bar_g_bad_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_1h.BMV",anm_name,0,"Barbarian_N")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)

	anm_name="Bar_g_bad_sword"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_bad_sword.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)
	Bladex.AddAnmEvent("Bar_g_bad_sword","W2hToLeft",0.21)
	Bladex.AddAnmEvent("Bar_g_bad_sword","W2hToRight",0.93)






#	anm_name="Bar_g_bad_spear"
#	Bladex.LoadSampledAnimation("../../Anm/Bar_g_bad_spear.BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmRRelease(anm_name,0.345)
#	Bladex.AddAnmRStep(anm_name,0.428)
#	Bladex.AddAnmRRelease(anm_name,0.664)
#	Bladex.AddAnmRStep(anm_name,0.803)
#	Bladex.AddAnmLStep(anm_name,0.000)
#	Bladex.AddAnmLRelease(anm_name,0.456)
#	Bladex.AddAnmLStep(anm_name,0.647)
#	eventos de pies heredados de la animaci�n delKgt


	anm_name="Bar_g_bad_spear2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_bad_spear2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.557)
	Bladex.AddAnmRStep(anm_name,0.657)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmLStep(anm_name,0.479)
	Bladex.AddAnmLRelease(anm_name,0.809)
	Bladex.AddAnmLStep(anm_name,0.918)
#	eventos de pies heredados de la animaci�n delKgt





	anm_name="Bar_g_draw_rlx"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_draw_rlx.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.817)
	Bladex.AddAnmLStep(anm_name,0.383)


	anm_name="Bar_g_draw_run"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_draw_run.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.042)
	Bladex.AddAnmLStep(anm_name,0.319)













############ GOLPES SIN ARMAS ###############



	anm_name="Bar_g_punch1"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_punch1.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.255)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.028)
	Bladex.AddAnmLStep(anm_name,0.327)
	Bladex.AddAnmLRelease(anm_name,0.806)
	Bladex.AddAnmLStep(anm_name,0.998)



	anm_name="Bar_g_punch2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_punch2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.054)
	Bladex.AddAnmRStep(anm_name,0.967)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.025)
	Bladex.AddAnmLStep(anm_name,0.195)
	Bladex.AddAnmLStep(anm_name,1.000)



	anm_name="Bar_g_punch3"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_punch3.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.237)
	Bladex.AddAnmRStep(anm_name,0.421)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.412)
	Bladex.AddAnmLStep(anm_name,0.991)


	anm_name="Bar_g_punch4"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_punch4.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.361)
	Bladex.AddAnmRStep(anm_name,0.528)
	Bladex.AddAnmRRelease(anm_name,0.806)
	Bladex.AddAnmRStep(anm_name,0.972)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.542)
	Bladex.AddAnmLStep(anm_name,0.778)



#	anm_name="Bar_g_kick"
#	Bladex.LoadSampledAnimation("../../Anm/Bar_g_kick.BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmRRelease(anm_name,0.151)
#	Bladex.AddAnmRStep(anm_name,0.778)
#	Bladex.AddAnmLStep(anm_name,0.000)
#	Bladex.SetAnimationFactor("Bar_g_kick",3.7)




	#
	# Movimientos en combate
	#


	anm_name="Bar_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_l.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.074)
	Bladex.AddAnmRStep(anm_name,0.259)
	Bladex.AddAnmRRelease(anm_name,0.407)
	Bladex.AddAnmRStep(anm_name,0.63)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmRStep(anm_name,0.926)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,0.333)
	Bladex.AddAnmLRelease(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0.66)
	Bladex.AddAnmLRelease(anm_name,0.76)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_r.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.167)
	Bladex.AddAnmRStep(anm_name,0.611)
	Bladex.AddAnmRRelease(anm_name,0.722)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,0.167)
	Bladex.AddAnmLStep(anm_name,0.444)
	Bladex.AddAnmLRelease(anm_name,0.667)
	Bladex.AddAnmLStep(anm_name,0.944)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_f.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.404)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.462)
	Bladex.AddAnmLRelease(anm_name,0.904)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.024)
	Bladex.AddAnmRRelease(anm_name,0.122)
	Bladex.AddAnmLStep(anm_name,0.201)
	Bladex.AddAnmRStep(anm_name,0.318)
	Bladex.AddAnmLRelease(anm_name,0.341)
	Bladex.AddAnmRRelease(anm_name,0.427)
	Bladex.AddAnmLStep(anm_name,0.518)
	Bladex.AddAnmRStep(anm_name,0.667)
	Bladex.AddAnmLRelease(anm_name,0.690)
	Bladex.AddAnmRRelease(anm_name,0.748)
	Bladex.AddAnmLStep(anm_name,0.868)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddStopTests(anm_name)
	#eventos de pisada del Kgt_attack_b#


	#anm_name="Bar_d_b"
	#Bladex.LoadSampledAnimation("../../Anm/Bar_d_b.BMV",anm_name,0,"Barbarian")
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.125)
	#Bladex.AddAnmRStep(anm_name,0.417)
	#Bladex.AddAnmLRelease(anm_name,0.52)
	#Bladex.AddAnmLStep(anm_name,0.911)
	#Bladex.SetAnimationFactor("Bar_d_b",3.6)


	#anm_name="Bar_d_r"
	#Bladex.LoadSampledAnimation("../../Anm/Bar_d_b.BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.021)
	#Bladex.AddAnmRStep(anm_name,0.23)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0.167)
	#Bladex.AddAnmLStep(anm_name,0.333)



	anm_name="Bar_d_b_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_d_b_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.3)
	Bladex.AddAnmRStep(anm_name,0.531)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.195)
	Bladex.AddAnmLStep(anm_name,0.5)



	anm_name="Bar_g2h_d_l"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g2h_d_l.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.167)
	Bladex.AddAnmRStep(anm_name,0.431)
	Bladex.AddAnmRRelease(anm_name,0.809)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.078)
	Bladex.AddAnmLStep(anm_name,0.228)
	Bladex.AddAnmLRelease(anm_name,0.474)
	Bladex.AddAnmLStep(anm_name,0.801)

	#anm_name="Bar_d_r"
	#Bladex.LoadSampledAnimation("../../Anm/Kgt_d_r.BMV",anm_name,0,"Barbarian")
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0.021)
	#Bladex.AddAnmRStep(anm_name,0.23)
	#Bladex.AddAnmLRelease(anm_name,0.167)
	#Bladex.AddAnmLStep(anm_name,0.333)


	#anm_name="Bar_d_l"
	#Bladex.LoadSampledAnimation("../../Anm/Kgt_d_l.BMV",anm_name,0,"Barbarian")
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0.94)
	#Bladex.AddAnmRRelease(anm_name,0.432)
	#Bladex.AddAnmLRelease(anm_name,0.012)
	#Bladex.AddAnmLStep(anm_name,0.103)

	anm_name="Bar_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_l_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.256)
	Bladex.AddAnmRStep(anm_name,0.519)
	Bladex.AddAnmLRelease(anm_name,0.740)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_r_s.BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.270)
	Bladex.AddAnmLRelease(anm_name,0.524)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddAnmRRelease(anm_name,0.944)
	Bladex.AddStopTests(anm_name)




	anm_name="Bar_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_f_s.BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.108)
	Bladex.AddAnmLStep(anm_name,0.459)
	Bladex.AddAnmRRelease(anm_name,0.579)
	Bladex.AddAnmRStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_b_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.154)
	Bladex.AddAnmRStep(anm_name,0.474)
	Bladex.AddAnmLRelease(anm_name,0.724)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_rlx_f"
	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_f.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)


	anm_name="Bar_attack_rlx_s"
	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_f_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)


	#anm_name="Bar_attack_t_r"
	#Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_t_r.BMV",anm_name,1,"Barbarian")
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,1)
	#Bladex.AddAnmLStep(anm_name,1)


	#anm_name="Bar_attack_t_l"
	#Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_t_l.BMV",anm_name,1,"Barbarian")
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,1)
	#Bladex.AddAnmLStep(anm_name,1)

#	anm_name="Bar_attack_t_r_s"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_t_r_s.BMV",anm_name,1,"Barbarian")
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#
#	anm_name="Bar_attack_t_l_s"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_t_l_s.BMV",anm_name,1,"Barbarian")
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)




####encaramiento arma a dos manos


	anm_name="Bar_attack_l_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_l_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.074)
	Bladex.AddAnmRStep(anm_name,0.259)
	Bladex.AddAnmRRelease(anm_name,0.407)
	Bladex.AddAnmRStep(anm_name,0.63)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmRStep(anm_name,0.926)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,0.333)
	Bladex.AddAnmLRelease(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0.66)
	Bladex.AddAnmLRelease(anm_name,0.76)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_r_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_r_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.167)
	Bladex.AddAnmRStep(anm_name,0.611)
	Bladex.AddAnmRRelease(anm_name,0.722)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,0.167)
	Bladex.AddAnmLStep(anm_name,0.444)
	Bladex.AddAnmLRelease(anm_name,0.667)
	Bladex.AddAnmLStep(anm_name,0.944)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_f_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_f_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.125)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.438)
	Bladex.AddAnmLRelease(anm_name,0.688)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_b_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_b_2w.BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.325)
	Bladex.AddAnmRStep(anm_name,0.408)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)
	#eventos de pisada del Kgt_attack_b#


	anm_name="Bar_rlx_f_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_f_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




####encaramiento hacha


	anm_name="Bar_attack_l_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_l_axe.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.074)
	Bladex.AddAnmRStep(anm_name,0.259)
	Bladex.AddAnmRRelease(anm_name,0.407)
	Bladex.AddAnmRStep(anm_name,0.63)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmRStep(anm_name,0.926)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,0.333)
	Bladex.AddAnmLRelease(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0.66)
	Bladex.AddAnmLRelease(anm_name,0.76)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_r_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_r_axe.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.167)
	Bladex.AddAnmRStep(anm_name,0.611)
	Bladex.AddAnmRRelease(anm_name,0.722)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLRelease(anm_name,0.167)
	Bladex.AddAnmLStep(anm_name,0.444)
	Bladex.AddAnmLRelease(anm_name,0.667)
	Bladex.AddAnmLStep(anm_name,0.944)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_f_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_f_axe.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.125)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.438)
	Bladex.AddAnmLRelease(anm_name,0.688)
	Bladex.AddStopTests(anm_name)

	anm_name="Bar_attack_b_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_attack_b_axe.BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.325)
	Bladex.AddAnmRStep(anm_name,0.408)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)
	#eventos de pisada del Kgt_attack_b#

	anm_name="Bar_rlx_f_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_f_axe.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)



	#
	# Saltos
	#
	anm_name="Bar_jmp_no"
	Bladex.LoadSampledAnimation("../../Anm/Bar_jmpl_no.BMV",anm_name,0)

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.505)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.0)
	Bladex.AddAnmRStep(anm_name,0.505)


	anm_name="Bar_jmp_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_jmp_1h.BMV",anm_name,0,"Barbarian")

	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.11)
	Bladex.AddAnmLRelease(anm_name,0.05)
	Bladex.AddAnmRStep(anm_name,0.340)
	Bladex.AddAnmLStep(anm_name,0.340)
	Bladex.AddAnmRRelease(anm_name,0.360)
	Bladex.AddAnmLRelease(anm_name,0.461)
	Bladex.AddAnmRStep(anm_name,0.499)
	Bladex.AddAnmRRelease(anm_name,0.597)
	Bladex.AddAnmRStep(anm_name,0.696)
	Bladex.AddAnmLStep(anm_name,0.696)




	anm_name="Bar_jmph0_no"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_jmph0_no.BMV",anm_name,0,"Barbarian")

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.324)
	Bladex.AddAnmLRelease(anm_name,0.532)
	Bladex.AddAnmRStep(anm_name,0.618)
	Bladex.AddAnmLStep(anm_name,0.843)


#	anm_name="Bar_jmp_1h"
#	Bladex.LoadSampledAnimation("../../Anm/Bar_jmpl_1h.BMV",anm_name,0)
#
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.03)
#	Bladex.AddAnmLStep(anm_name,0.5)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.03)
#	Bladex.AddAnmRStep(anm_name,0.5)
#	Bladex.SetAnimationFactor("Bar_jmp_1h",1.25)
#
#
#
#	anm_name="Bar_jmph0_no"
#	Bladex.LoadSampledAnimation("../../Anm/Bar_jmph0_no.BMV",anm_name,0)
#
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.324)
#	Bladex.AddAnmLRelease(anm_name,0.532)
#	Bladex.AddAnmRStep(anm_name,0.618)
#	Bladex.AddAnmLStep(anm_name,0.843)
#	Bladex.SetAnimationFactor("Bar_jmph0_no",1.25)

	#
	# Slip
	#
	anm_name="Bar_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Bar_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Bar_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.099)
	Bladex.AddAnmRStep(anm_name,0.562)
	Bladex.AddAnmRRelease(anm_name,0.802)
	Bladex.AddAnmRStep(anm_name,0.916)
	Bladex.AddAnmLStep(anm_name,0.105)
	Bladex.AddAnmLRelease(anm_name,0.606)
	Bladex.AddAnmLStep(anm_name,0.794)

	#
	# Bowing
	#
	anm_name="Bar_b1"
	Bladex.LoadSampledAnimation("../../Anm/Bar_b1.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Bar_b2"
	Bladex.LoadSampledAnimation("../../Anm/Bar_b2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Bar_b3"
	Bladex.LoadSampledAnimation("../../Anm/Bar_b3.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




############ MUERTES










	anm_name="Bar_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth0.BMV",anm_name,0,"Barbarian")
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


	anm_name="Bar_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c1.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)
 	Bladex.AddAnmLRelease(anm_name,0.745)  # Added.
	Bladex.AddAnmRRelease(anm_name,0.789)  #
	Bladex.AddAnmLStep(anm_name,0.883)     #
	Bladex.AddAnmRStep(anm_name,0.908)     #    -LeadHead

	anm_name="Bar_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c2.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)

	anm_name="Bar_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c3.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)


	anm_name="Bar_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c4.BMV",anm_name,0,"Barbarian")
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


	anm_name="Bar_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c5.BMV",anm_name,0,"Barbarian")
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


	anm_name="Bar_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c6.BMV",anm_name,0,"Barbarian")
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

	anm_name="Bar_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)

	anm_name="Bar_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n00.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)

	anm_name="Bar_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n01.BMV",anm_name,0)
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


	anm_name="Bar_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)

	anm_name="Bar_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n03.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)

	anm_name="Bar_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n04.BMV",anm_name,0,"Barbarian")
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

	anm_name="Bar_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n05.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)

	anm_name="Bar_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0,"Barbarian")
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

	anm_name="Bar_dth_burn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_burn.BMV",anm_name,0,"Barbarian")
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


	anm_name="Bar_dth_rock"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rock.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_dth_rockfront"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rockfront.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.348)
	Bladex.AddAnmRStep(anm_name,0.796)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.335)
	Bladex.AddAnmLStep(anm_name,0.792)






	###############
	#
	#Hurt
	#
	###############





	anm_name="Bar_hurt_f_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_back.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_f_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_arm.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_f_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_breast.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_f_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_head.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_f_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_leg.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Bar_hurt_f_neck"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_neck.BMV",anm_name,0,"Barbarian")
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_f_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_arm.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_f_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_leg.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_head.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_arm.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_leg.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Bar_hurt_neck"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_neck.BMV",anm_name,0,"Barbarian")
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_arm.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_leg.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Bar_hurt0"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt0.BMV",anm_name,0,"Barbarian")
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_back.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_breast.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Bar_hurt_jog"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_jog.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.21)
	Bladex.AddAnmRRelease(anm_name,0.36)
	Bladex.AddAnmRStep(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.07)
	Bladex.AddAnmLStep(anm_name,0.4)
	Bladex.AddAnmLRelease(anm_name,0.58)
	Bladex.AddAnmLStep(anm_name,0.8)


	anm_name="Bar_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_big.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.4)
	Bladex.AddAnmRStep(anm_name,0.6)

	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.27)
	Bladex.AddAnmLStep(anm_name,0.43)



	anm_name="Bar_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_lite.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.35)
	Bladex.AddAnmRStep(anm_name,0.59)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,1.0)

	anm_name="Bar_parry_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_parry_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.189)
	Bladex.AddAnmRRelease(anm_name,0.631)
	Bladex.AddAnmRStep(anm_name,0.959)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.156)
	Bladex.AddAnmLStep(anm_name,0.313)
	Bladex.AddAnmLRelease(anm_name,0.416)
	Bladex.AddAnmLStep(anm_name,0.745)

	anm_name="Bar_df_01"
	Bladex.LoadSampledAnimation("../../Anm/Bar_df_01.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Bar_df_02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_02.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.326)
	Bladex.AddAnmRStep(anm_name,0.502)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.549)
	Bladex.AddAnmLStep(anm_name,0.771)

	anm_name="Bar_df_01_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_df_01_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.614)
	Bladex.AddAnmRStep(anm_name,0.882)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.526)
	Bladex.AddAnmLStep(anm_name,0.771)


	anm_name="Bar_df_02_2w"
	Bladex.LoadSampledAnimation("../../Anm/Bar_df_02_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.397)
	Bladex.AddAnmRStep(anm_name,0.637)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.214)
	Bladex.AddAnmLStep(anm_name,0.572)

	anm_name="Bar_parry_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_parry_axe.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.093)
	Bladex.AddAnmRStep(anm_name,0.519)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Bar_df_01_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_df_01_axe.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.380)
	Bladex.AddAnmRStep(anm_name,0.665)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.240)
	Bladex.AddAnmLStep(anm_name,0.585)


	anm_name="Bar_df_02_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_df_02_axe.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.454)
	Bladex.AddAnmRStep(anm_name,0.753)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.221)
	Bladex.AddAnmLStep(anm_name,0.593)

	anm_name="Bar_sword_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Barbarian")
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


	anm_name="Bar_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_s_broken.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.439)
	Bladex.AddAnmRStep(anm_name,595)
	Bladex.AddAnmLRelease(anm_name,0.708)
	Bladex.AddAnmLStep(anm_name,0.867)


	anm_name="Bar_sword_reaction"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Barbarian")
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




	############	Change Weapons




	anm_name="Bar_attack_chg_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Bar_attack_chg_r",1.5)

	anm_name="Bar_attack_chg_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Bar_attack_chg_l",1.5)

	anm_name="Bar_attack_chg_r_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)



	anm_name="Bar_drp_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Bar_drp_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)








############	Throw Objects




	anm_name="Bar_1tw_l_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.25)
	Bladex.AddAnmRStep(anm_name,0.45)
	Bladex.AddAnmRRelease(anm_name,0.64)
	Bladex.AddAnmRStep(anm_name,0.97)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Bar_1tw_h_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)





##########	Drink/ Eat



	anm_name="Bar_drink"
	Bladex.LoadSampledAnimation("../../Anm/Bar_drink.BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Bar_eat00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_eat00.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Bar_gulp00"
	Bladex.LoadSampledAnimation("../../Anm/Bar_gulp00.BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Bar_attack_drink"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_drink.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)












############ COGERES / Llaves




	anm_name="Bar_tke_r_01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.159)
	Bladex.AddAnmLStep(anm_name,0.327)
	Bladex.AddAnmLRelease(anm_name,0.689)
	Bladex.AddAnmLStep(anm_name,0.893)

	anm_name="Bar_tke_r_02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.183)
	Bladex.AddAnmRStep(anm_name,0.343)
	Bladex.AddAnmRRelease(anm_name,0.585)
	Bladex.AddAnmRStep(anm_name,0.840)

	anm_name="Bar_tke_r_03"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.191)
	Bladex.AddAnmRStep(anm_name,0.335)
	Bladex.AddAnmRRelease(anm_name,0.502)
	Bladex.AddAnmRStep(anm_name,0.715)

	anm_name="Bar_tke_r_04"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.216)
	Bladex.AddAnmRStep(anm_name,0.395)
	Bladex.AddAnmRRelease(anm_name,0.716)
	Bladex.AddAnmRStep(anm_name,1)

	anm_name="Bar_tke_r_05"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.208)
	Bladex.AddAnmRStep(anm_name,0.369)
	Bladex.AddAnmRRelease(anm_name,0.544)
	Bladex.AddAnmRStep(anm_name,0.842)

	anm_name="Bar_tke_r_key00"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.096)
	Bladex.AddAnmLStep(anm_name,0.159)
	Bladex.AddAnmLRelease(anm_name,0.350)
	Bladex.AddAnmLStep(anm_name,0.443)

	anm_name="Bar_tke_r_key01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.121)
	Bladex.AddAnmRStep(anm_name,0.245)
	Bladex.AddAnmRRelease(anm_name,0.420)
	Bladex.AddAnmRStep(anm_name,0.588)


	anm_name="Bar_tke_r_key02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.160)
	Bladex.AddAnmRStep(anm_name,0.264)
	Bladex.AddAnmRRelease(anm_name,0.408)
	Bladex.AddAnmRStep(anm_name,0.566)

	anm_name="Bar_tke_r_key03"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.132)
	Bladex.AddAnmRStep(anm_name,0.261)
	Bladex.AddAnmRRelease(anm_name,0.489)
	Bladex.AddAnmRStep(anm_name,0.689)

	anm_name="Bar_tke_r_key05"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.153)
	Bladex.AddAnmRStep(anm_name,0.270)
	Bladex.AddAnmRRelease(anm_name,0.401)
	Bladex.AddAnmRStep(anm_name,0.601)







	##############################
	#
	# Trepar
	#
	##############################


	anm_name="Bar_clmb_low_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_low_1h.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.17)
	Bladex.AddAnmRStep(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.48)
	Bladex.AddAnmLStep(anm_name,0.82)

	anm_name="Bar_clmb_medlow_1h"
	Bladex.LoadSampledAnimation("../../Anm/Bar_clmb_medlow_1h.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.30)
	Bladex.AddAnmRStep(anm_name,0.79)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.28)
	Bladex.AddAnmLStep(anm_name,0.53)
	Bladex.AddAnmLRelease(anm_name,0.83)
	Bladex.AddAnmLStep(anm_name,0.98)

	anm_name="Bar_clmb_medium_1h"
	Bladex.LoadSampledAnimation("../../Anm/Bar_clmb_medium_1h.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.13)
	Bladex.AddAnmRStep(anm_name,0.84)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,0.100)

	anm_name="Bar_clmb_high_1h"
	Bladex.LoadSampledAnimation("../../Anm/Bar_clmb_high.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.10)
	Bladex.AddAnmRStep(anm_name,0.88)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.10)
	Bladex.AddAnmLStep(anm_name,1.0)






######## USE / ACTIVATE



	anm_name="Bar_key"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Bar_lvr_u"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.126)
	Bladex.AddAnmRStep(anm_name,0.294)
	Bladex.AddAnmRRelease(anm_name,0.720)
	Bladex.AddAnmRStep(anm_name,0.875)

	anm_name="Bar_lvr_d"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.126)
	Bladex.AddAnmRStep(anm_name,0.294)
	Bladex.AddAnmRRelease(anm_name,0.720)
	Bladex.AddAnmRStep(anm_name,0.875)

	anm_name="Bar_pulsador"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_pulsador.BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.075)
	Bladex.AddAnmRStep(anm_name,0.233)
	Bladex.AddAnmRRelease(anm_name,0.566)
	Bladex.AddAnmRStep(anm_name,0.856)

	anm_name="Bar_fire0"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	# Bladex.AddAnmRRelease(anm_name,0.113)     # commented out
	# Bladex.AddAnmRStep(anm_name,0.29)         # no actual steps during this anim
	# Bladex.AddAnmRRelease(anm_name,0.751)     #
	# Bladex.AddAnmRStep(anm_name,0.98)         #           -LeadHead

	anm_name="Bar_fire1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	# Bladex.AddAnmRRelease(anm_name,0.091)    # commented out
	# Bladex.AddAnmRStep(anm_name,0.2)         # no actual steps during this anim
	# Bladex.AddAnmRRelease(anm_name,0.650)    #
	# Bladex.AddAnmRStep(anm_name,0.824)       #           -LeadHead

	anm_name="Bar_fire2"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.081)
	Bladex.AddAnmRStep(anm_name,0.225)
	Bladex.AddAnmRRelease(anm_name,0.752)
	Bladex.AddAnmRStep(anm_name,0.922)

	anm_name="Bar_fire3"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.104)
	Bladex.AddAnmRStep(anm_name,0.239)
	Bladex.AddAnmRRelease(anm_name,0.748)
	Bladex.AddAnmRStep(anm_name,0.953)

	anm_name="Bar_fire_g"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	# Bladex.AddAnmRRelease(anm_name,0.108)   # commented out
	# Bladex.AddAnmRStep(anm_name,0.244)      # no actual steps during this anim
	# Bladex.AddAnmRRelease(anm_name,0.758)   #
	# Bladex.AddAnmRStep(anm_name,0.926)      #           -LeadHead






	##########################################
	########### GIROS DE 180� ################
	##########################################




	anm_name="Bar_wlk_turn"
	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_turn.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.403)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmLStep(anm_name,0.217)
	Bladex.AddAnmLRelease(anm_name,0.833)
	#Antes estaba usando la del caballero, a lo mejor esta da problemas. En ese caso cambio por kgt

	anm_name="Bar_snk_turn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_turn.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.403)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmLStep(anm_name,0.217)
	Bladex.AddAnmLRelease(anm_name,0.833)


	anm_name="Bar_jog_turn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_jog_turn.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.376)
	Bladex.AddAnmRStep(anm_name,0.714)
	Bladex.AddAnmLStep(anm_name,0.284)
	Bladex.AddAnmLRelease(anm_name,0.690)
	Bladex.AddAnmLStep(anm_name,0.971)


	anm_name="Bar_rlx_turn"
	Bladex.LoadSampledAnimation("../../Anm/Bar_rlx_turn.BMV",anm_name,0,"Barbarian")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.095)
	Bladex.AddAnmLStep(anm_name,0.875)







#	Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_h_f.BMV","Bar_1tw_h",0,"Barbarian")
#	Bladex.AddAnmRStep("Bar_1tw_h",0.0)
#	Bladex.AddAnmLStep("Bar_1tw_h",0.0)
#	#Bladex.SetAnimationFactor("Bar_1tw_h",3)
#	Bladex.AddAnmEvent("Bar_1tw_h","ThrowHeavyEvnt",0.4722)
#
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_l_f.BMV","Bar_1tw_l",0,"Barbarian")
#	Bladex.AddAnmRStep("Bar_1tw_l",0.0)
#	Bladex.AddAnmLStep("Bar_1tw_l",0.0)
#	#Bladex.SetAnimationFactor("Bar_1tw_l",3)
#	Bladex.AddAnmEvent("Bar_1tw_l","ThrowLightEvent",0.4839)











#	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_short.BMV","WlkShort_Bar",1)
#
#	Bladex.AddAnmRStep("WlkShort_Bar",0.0)
#	Bladex.AddAnmLStep("WlkShort_Bar",0.5)
#	Bladex.AddAnmRStep("WlkShort_Bar",1.0)
#	Bladex.AddAnmRRelease("WlkShort_Bar",0.5)
#	Bladex.AddAnmLRelease("WlkShort_Bar",1.0)
#	Bladex.AddStopTests("WlkShort_Bar")
#
#	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_short_2w.BMV","WlkShort_2w_Bar",1)
#	Bladex.AddAnmRStep("WlkShort_2w_Bar",0.0)
#	Bladex.AddAnmLStep("WlkShort_2w_Bar",0.5)
#	Bladex.AddAnmRStep("WlkShort_2w_Bar",1.0)
#	Bladex.AddAnmRRelease("WlkShort_2w_Bar",0.5)
#	Bladex.AddAnmLRelease("WlkShort_2w_Bar",1.0)
#	Bladex.AddStopTests("WlkShort_2w_Bar")
#
#	Bladex.LoadSampledAnimation("../../Anm/Bar_wlk_short_axe.BMV","WlkShort_axe_Bar",1)
#	Bladex.AddAnmRStep("WlkShort_axe_Bar",0.0)
#	Bladex.AddAnmLStep("WlkShort_axe_Bar",0.5)
#	Bladex.AddAnmRStep("WlkShort_axe_Bar",1.0)
#	Bladex.AddAnmRRelease("WlkShort_axe_Bar",0.5)
#	Bladex.AddAnmLRelease("WlkShort_axe_Bar",1.0)
#	Bladex.AddStopTests("WlkShort_axe_Bar")


    # PLAGUE: Let's see if the game even supports multiple backdodge anims.
	# anm_name="Bar_d_b_axe"
	# Bladex.LoadSampledAnimation("../../Anm/Bar_d_b_axe.BMV",anm_name,0)
	# Bladex.AddAnmRStep(anm_name,0.000)
	# Bladex.AddAnmRRelease(anm_name,0.202)
	# Bladex.AddAnmRStep(anm_name,0.423)
	# Bladex.AddAnmLStep(anm_name,0.000)
	# Bladex.AddAnmLRelease(anm_name,0.117)
	# Bladex.AddAnmLStep(anm_name,0.412)

	anm_name="Bar_g_d_l_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_d_l_axe.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.431)
	Bladex.AddAnmRRelease(anm_name,0.811)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.078)
	Bladex.AddAnmLStep(anm_name,0.172)
	Bladex.AddAnmLRelease(anm_name,0.474)
	Bladex.AddAnmLStep(anm_name,0.801)

	anm_name="Bar_g_d_r_axe"
	Bladex.LoadSampledAnimation("../../Anm/Bar_g_d_r_axe.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.125)
	Bladex.AddAnmRStep(anm_name,0.281)
	Bladex.AddAnmRRelease(anm_name,0.578)
	Bladex.AddAnmRStep(anm_name,0.766)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Bar_g_d_r_axe","W2hToLeft",0.23)
	Bladex.AddAnmEvent("Bar_g_d_r_axe","W2hToRight",0.95)