###///
###||| DWFANIMATIONSET.PY TITANIUM
###||| Change list:
###||| * Included Borer's animation fix for smoother camera
###|||
###||| Because of this, ../AnmPak/Dwf.dat, Enb.dat and Ena.dat MUST be deleted or replaced upon installation
###\\\

import Bladex
import Enm_Def


DwfAnimationSetLoaded=0

def LoadDwfAnimationSet(ct_name):
	global DwfAnimationSetLoaded
	if not DwfAnimationSetLoaded:
		DwfAnimationSetLoaded = 1
		print "Loading the DwArF animation sets..."

		#### Relax ####

		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_1h.BMV","Rlx_1h_Dwf",1)
		Bladex.AddAnmRStep("Rlx_1h_Dwf",0.0)
		Bladex.AddAnmLStep("Rlx_1h_Dwf",0.0)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_sword.BMV","Rlx_2w_Dwf",1)
		Bladex.AddAnmRStep("Rlx_2w_Dwf",0.0)
		Bladex.AddAnmLStep("Rlx_2w_Dwf",0.0)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_spear.BMV","Rlx_spear_Dwf",1)
		Bladex.AddAnmRStep("Rlx_spear_Dwf",0.0)
		Bladex.AddAnmLStep("Rlx_spear_Dwf",0.0)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_b.BMV","Rlx_b_Dwf",1)
		Bladex.AddAnmRStep("Rlx_b_Dwf",0.0)
		Bladex.AddAnmLStep("Rlx_b_Dwf",0.0)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_vt.BMV","Dwf_rlx_vt",1)
		Bladex.AddAnmRStep("Dwf_rlx_vt",0.0)
		Bladex.AddAnmLStep("Dwf_rlx_vt",0.0)




################# ARROJARES ##################




		Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_l_f.BMV","Dwf_1tw_l_f",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_1tw_l_f",0.0)
		Bladex.AddAnmLStep("Dwf_1tw_l_f",0.0)
		Bladex.AddAnmEvent("Dwf_1tw_l_f","ThrowLightFacingEvent",0.3846)

		Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_h_f.BMV","Dwf_1tw_h_f",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_1tw_h_f",0.0)
		Bladex.AddAnmLStep("Dwf_1tw_h_f",0.0)
		Bladex.AddAnmEvent("Dwf_1tw_h_f","ThrowHeavyFacingEvent",0.416)



		### CORRER   ####
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jog_no.BMV","Jog_no_Dwf",1)
		Bladex.AddAnmRStep("Jog_no_Dwf",0.0)
		Bladex.AddAnmRRelease("Jog_no_Dwf",0.166)
		Bladex.AddAnmLStep("Jog_no_Dwf",0.389)
		Bladex.AddAnmLRelease("Jog_no_Dwf",0.624)
		Bladex.AddAnmRStep("Jog_no_Dwf",1.0)
		Bladex.AddStopTests("Jog_no_Dwf")

		Bladex.LoadSampledAnimation("../../Anm/Dwf_jog_b.BMV","Jog_b_Dwf",1)
		Bladex.AddAnmRStep("Jog_b_Dwf",0.0)
		Bladex.AddAnmRRelease("Jog_b_Dwf",0.31)
		Bladex.AddAnmLStep("Jog_b_Dwf",0.52)
		Bladex.AddAnmLRelease("Jog_b_Dwf",0.82)
		Bladex.AddAnmRStep("Jog_b_Dwf",1.0)
		Bladex.AddStopTests("Jog_b_Dwf")

		Bladex.LoadSampledAnimation("../../Anm/Dwf_jog_1h.BMV","Jog_1h_Dwf",1)
		Bladex.AddAnmLStep("Jog_1h_Dwf",0.00)
		Bladex.AddAnmLRelease("Jog_1h_Dwf",0.31)
		Bladex.AddAnmRStep("Jog_1h_Dwf",0.5)
		Bladex.AddAnmRRelease("Jog_1h_Dwf",0.79)
		Bladex.AddAnmLStep("Jog_1h_Dwf",1.0)
		Bladex.AddStopTests("Jog_1h_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_jog_sword.BMV","Jog_2w_Dwf",1)
		Bladex.AddAnmLStep("Jog_2w_Dwf",0.00)
		Bladex.AddAnmLRelease("Jog_2w_Dwf",0.31)
		Bladex.AddAnmRStep("Jog_2w_Dwf",0.5)
		Bladex.AddAnmRRelease("Jog_2w_Dwf",0.79)
		Bladex.AddAnmLStep("Jog_2w_Dwf",1.0)
		Bladex.AddStopTests("Jog_2w_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_jog_axe.BMV","Jog_axe_Dwf",1)
		Bladex.AddAnmLStep("Jog_axe_Dwf",0.00)
		Bladex.AddAnmLRelease("Jog_axe_Dwf",0.31)
		Bladex.AddAnmRStep("Jog_axe_Dwf",0.5)
		Bladex.AddAnmRRelease("Jog_axe_Dwf",0.79)
		Bladex.AddAnmLStep("Jog_axe_Dwf",1.0)
		Bladex.AddStopTests("Jog_axe_Dwf")

		### CORRER ATRAS ###

		anm_name="Dwf_jogb_1h"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jogb_1h.BMV",anm_name,1)
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


		anm_name="Dwf_jogb_no"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jogb_no.BMV",anm_name,1)
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

		anm_name="Dwf_jogb_2w"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jogb_sword.BMV",anm_name,1)
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

		anm_name="Dwf_jogb_spear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jogb_spear.BMV",anm_name,1)
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
		Bladex.LoadSampledAnimation("../../Anm/Dwf_snk_no.BMV","Snk_no_Dwf",1)
		Bladex.AddAnmRStep("Snk_no_Dwf",0)
		Bladex.AddAnmRRelease("Snk_no_Dwf",0.617)
		Bladex.AddAnmRStep("Snk_no_Dwf",1)
		Bladex.AddAnmLStep("Snk_no_Dwf",0)
		Bladex.AddAnmLRelease("Snk_no_Dwf",0.121)
		Bladex.AddAnmLStep("Snk_no_Dwf",0.497)
		Bladex.AddStopTests("Snk_no_Dwf")

		Bladex.LoadSampledAnimation("../../Anm/Dwf_snk_1h.BMV","Snk_1h_Dwf",1)
		Bladex.AddAnmRStep("Snk_1h_Dwf",0)
		Bladex.AddAnmRRelease("Snk_1h_Dwf",0.617)
		Bladex.AddAnmRStep("Snk_1h_Dwf",1)
		Bladex.AddAnmLStep("Snk_1h_Dwf",0)
		Bladex.AddAnmLRelease("Snk_1h_Dwf",0.121)
		Bladex.AddAnmLStep("Snk_1h_Dwf",0.497)
		Bladex.AddStopTests("Snk_1h_Dwf")

		Bladex.LoadSampledAnimation("../../Anm/Dwf_snk_b.BMV","Snk_b_Dwf",1)
		Bladex.AddAnmRStep("Snk_b_Dwf",0.0)
		Bladex.AddAnmLStep("Snk_b_Dwf",0.0)
		Bladex.AddAnmLRelease("Snk_b_Dwf",0.124)
		Bladex.AddAnmLStep("Snk_b_Dwf",0.484)
		Bladex.AddAnmRRelease("Snk_b_Dwf",0.648)
		Bladex.AddAnmRStep("Snk_b_Dwf",1.0)
		Bladex.AddStopTests("Snk_b_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_snk_spear.BMV","Snk_spear_Dwf",1)
		Bladex.AddAnmRStep("Snk_spear_Dwf",0.0)
		Bladex.AddAnmLStep("Snk_spear_Dwf",0.0)
		Bladex.AddAnmLRelease("Snk_spear_Dwf",0.124)
		Bladex.AddAnmLStep("Snk_spear_Dwf",0.484)
		Bladex.AddAnmRRelease("Snk_spear_Dwf",0.648)
		Bladex.AddAnmRStep("Snk_spear_Dwf",1.0)
		Bladex.AddStopTests("Snk_spear_Dwf")

		Bladex.LoadSampledAnimation("../../Anm/Dwf_snk_sword.BMV","Snk_2w_Dwf",1)
		Bladex.AddAnmRStep("Snk_2w_Dwf",0.0)
		Bladex.AddAnmLStep("Snk_2w_Dwf",0.0)
		Bladex.AddAnmLRelease("Snk_2w_Dwf",0.124)
		Bladex.AddAnmLStep("Snk_2w_Dwf",0.484)
		Bladex.AddAnmRRelease("Snk_2w_Dwf",0.648)
		Bladex.AddAnmRStep("Snk_2w_Dwf",1.0)
		Bladex.AddStopTests("Snk_2w_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_wbk_no.BMV","Wbk_no_Dwf",1)

		Bladex.AddAnmLStep("Wbk_no_Dwf",0.0)
		Bladex.AddAnmRStep("Wbk_no_Dwf",0.388)
		Bladex.AddAnmLRelease("Wbk_no_Dwf",0.478)
		Bladex.AddAnmLStep("Wbk_no_Dwf",1.0)
		Bladex.AddAnmRRelease("Wbk_no_Dwf",1)
		Bladex.AddStopTests("Wbk_no_Dwf")



		Bladex.LoadSampledAnimation("../../Anm/Dwf_wbk_b.BMV","Wbk_b_Dwf",1)

		Bladex.AddAnmLStep("Wbk_b_Dwf",0.0)
		Bladex.AddAnmRStep("Wbk_b_Dwf",0.410)
		Bladex.AddAnmLRelease("Wbk_b_Dwf",0.518)
		Bladex.AddAnmLStep("Wbk_b_Dwf",1.0)
		Bladex.AddAnmRRelease("Wbk_b_Dwf",1.0)
		Bladex.AddStopTests("Wbk_b_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_wbk_spear.BMV","Wbk_spear_Dwf",1)

		Bladex.AddAnmRStep("Wbk_spear_Dwf",0.384)
		Bladex.AddAnmRRelease("Wbk_spear_Dwf",1.000)
		Bladex.AddAnmLStep("Wbk_spear_Dwf",0.000)
		Bladex.AddAnmLRelease("Wbk_spear_Dwf",0.471)
		Bladex.AddAnmLStep("Wbk_spear_Dwf",1.0)
		Bladex.AddStopTests("Wbk_spear_Dwf")

		Bladex.LoadSampledAnimation("../../Anm/Dwf_wbk_sword.BMV","Wbk_2w_Dwf",1)

		Bladex.AddAnmRStep("Wbk_2w_Dwf",0.384)
		Bladex.AddAnmRRelease("Wbk_2w_Dwf",1.000)
		Bladex.AddAnmLStep("Wbk_2w_Dwf",0.000)
		Bladex.AddAnmLRelease("Wbk_2w_Dwf",0.471)
		Bladex.AddAnmLStep("Wbk_2w_Dwf",1.0)
		Bladex.AddStopTests("Wbk_2w_Dwf")


		#
		#### Caminar ####
		#



		Bladex.LoadSampledAnimation("../../Anm/Dwf_wlk_no.BMV","Wlk_no_Dwf",1)

		Bladex.AddAnmRStep("Wlk_no_Dwf",0)
		Bladex.AddAnmLStep("Wlk_no_Dwf",0.512)
		Bladex.AddAnmRRelease("Wlk_no_Dwf",0.629)
		Bladex.AddAnmRStep("Wlk_no_Dwf",1)
		Bladex.AddAnmLRelease("Wlk_no_Dwf",1)
		Bladex.AddStopTests("Wlk_no_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_wlk_no.BMV","Wlk_1h_Dwf",1)

		Bladex.AddAnmRStep("Wlk_1h_Dwf",0)
		Bladex.AddAnmLStep("Wlk_1h_Dwf",0.512)
		Bladex.AddAnmRRelease("Wlk_1h_Dwf",0.629)
		Bladex.AddAnmRStep("Wlk_1h_Dwf",1)
		Bladex.AddAnmLRelease("Wlk_1h_Dwf",1)
		Bladex.AddStopTests("Wlk_1h_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_wlk_sword.BMV","Wlk_2w_Dwf",1)

		Bladex.AddAnmRStep("Wlk_2w_Dwf",0)
		Bladex.AddAnmLStep("Wlk_2w_Dwf",0.512)
		Bladex.AddAnmRRelease("Wlk_2w_Dwf",0.629)
		Bladex.AddAnmRStep("Wlk_2w_Dwf",1)
		Bladex.AddAnmLRelease("Wlk_2w_Dwf",1)
		Bladex.AddStopTests("Wlk_2w_Dwf")


		Bladex.LoadSampledAnimation("../../Anm/Dwf_wlk_spear.BMV","Wlk_spear_Dwf",1)

		Bladex.AddAnmRStep("Wlk_spear_Dwf",0)
		Bladex.AddAnmLStep("Wlk_spear_Dwf",0.512)
		Bladex.AddAnmRRelease("Wlk_spear_Dwf",0.629)
		Bladex.AddAnmRStep("Wlk_spear_Dwf",1)
		Bladex.AddAnmLRelease("Wlk_spear_Dwf",1)
		Bladex.AddStopTests("Wlk_spear_Dwf")







		Bladex.LoadSampledAnimation("../../Anm/Dwf_wlk_b.BMV","Wlk_b_Dwf",4)

		Bladex.AddAnmRStep("Wlk_b_Dwf",0.0)
		Bladex.AddAnmLStep("Wlk_b_Dwf",0.0)
		Bladex.AddAnmLRelease("Wlk_b_Dwf",0.106)
		Bladex.AddAnmLStep("Wlk_b_Dwf",0.489)
		Bladex.AddAnmRRelease("Wlk_b_Dwf",0.576)
		Bladex.AddAnmRStep("Wlk_b_Dwf",1.0)
		Bladex.AddStopTests("Wlk_b_Dwf")










		#### Caidas ####

		Bladex.LoadSampledAnimation("../../Anm/Dwf_fll_low_no.BMV","FallLow_Dwf",0)
		Bladex.AddAnmRStep("FallLow_Dwf",0.0)
		Bladex.AddAnmLStep("FallLow_Dwf",0.0)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_fll_med_no.BMV","FallMed_Dwf",0)
		Bladex.AddAnmRStep("FallMed_Dwf",0.0)
		Bladex.AddAnmLStep("FallMed_Dwf",0.0)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_fll_high_no.BMV","FallHigh_Dwf",0)
		Bladex.AddAnmRStep("FallHigh_Dwf",0.0)
		Bladex.AddAnmLStep("FallHigh_Dwf",0.0)

		#Caida enorme
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Dwf",0,"Dwarf_N")
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Dwf",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dth_Fll2_Dwf",0.0)
		Bladex.AddAnmLStep("Dth_Fll2_Dwf",0.0)





		###########
		# Ataques Torpes
		###########

		anm_name="Dwf_g_magic"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_magic.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.105)
		Bladex.AddAnmRRelease(anm_name,0.558)
		Bladex.AddAnmRStep(anm_name,0.762)
		Bladex.AddAnmRRelease(anm_name,1.000)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.465)
		Bladex.AddAnmLStep(anm_name,0.545)
		Bladex.AddAnmEvent("Dwf_g_magic","LaunchTrail",0.595)

		anm_name="Dwf_g_magic2"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_magic2.BMV",anm_name,0)
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
		Bladex.AddAnmEvent("Dwf_g_magic2","LaunchTrail",0.377)


		anm_name="Dwf_g_back"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_back.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.477)
		Bladex.AddAnmRStep(anm_name,0.767)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.131)
		Bladex.AddAnmLStep(anm_name,0.305)
		Bladex.AddAnmLRelease(anm_name,0.829)
		Bladex.AddAnmLStep(anm_name,1.000)



		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_bad_axe.BMV","Dwf_g_bad_axe",0)
		Bladex.AddAnmRStep("Dwf_g_bad_axe",0.000)
		Bladex.AddAnmRRelease("Dwf_g_bad_axe",0.099)
		Bladex.AddAnmRStep("Dwf_g_bad_axe",0.160)
		Bladex.AddAnmRRelease("Dwf_g_bad_axe",0.400)
		Bladex.AddAnmRStep("Dwf_g_bad_axe",0.446)
		Bladex.AddAnmRRelease("Dwf_g_bad_axe",0.738)
		Bladex.AddAnmRStep("Dwf_g_bad_axe",0.956)
		Bladex.AddAnmLStep("Dwf_g_bad_axe",0.000)
		Bladex.AddAnmLRelease("Dwf_g_bad_axe",0.390)
		Bladex.AddAnmLStep("Dwf_g_bad_axe",0.445)
		Bladex.AddAnmEvent("Dwf_g_bad_axe","W2hToLeft",0.1)
		Bladex.AddAnmEvent("Dwf_g_bad_axe","W2hToRight",0.93)



		anm_name="Dwf_g_bad_spear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_bad_spear.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.345)
		Bladex.AddAnmRStep(anm_name,0.428)
		Bladex.AddAnmRRelease(anm_name,0.664)
		Bladex.AddAnmRStep(anm_name,0.803)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.456)
		Bladex.AddAnmLStep(anm_name,0.647)
		Bladex.AddAnmEvent("Dwf_g_bad_spear","W2hToLeft",0.1)
		Bladex.AddAnmEvent("Dwf_g_bad_spear","W2hToRight",0.93)

		anm_name="Dwf_g_bad_no"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_no.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.306)
		Bladex.AddAnmRStep(anm_name,0.433)
		Bladex.AddAnmRRelease(anm_name,0.624)
		Bladex.AddAnmRStep(anm_name,0.760)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.438)
		Bladex.AddAnmLStep(anm_name,0.554)

		anm_name="Dwf_g_bad_1h"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_1h.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.306)
		Bladex.AddAnmRStep(anm_name,0.433)
		Bladex.AddAnmRRelease(anm_name,0.624)
		Bladex.AddAnmRStep(anm_name,0.760)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.438)
		Bladex.AddAnmLStep(anm_name,0.554)


		anm_name="Dwf_g_bad_spear2"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_bad_spear2.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.557)
		Bladex.AddAnmRStep(anm_name,0.657)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.310)
		Bladex.AddAnmLStep(anm_name,0.479)
		Bladex.AddAnmLRelease(anm_name,0.809)
		Bladex.AddAnmLStep(anm_name,0.918)


		anm_name="Dwf_g_bad_sword1"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_bad_sword1.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.306)
		Bladex.AddAnmRStep(anm_name,0.433)
		Bladex.AddAnmRRelease(anm_name,0.624)
		Bladex.AddAnmRStep(anm_name,0.760)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.438)
		Bladex.AddAnmLStep(anm_name,0.554)
		Bladex.AddAnmEvent("Dwf_g_bad_sword1","W2hToLeft",0.15)
		Bladex.AddAnmEvent("Dwf_g_bad_sword1","W2hToRight",0.98)


		anm_name="Dwf_g_bad_sword2"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_bad_sword2.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.418)
		Bladex.AddAnmRStep(anm_name,0.522)
		Bladex.AddAnmRRelease(anm_name,0.668)
		Bladex.AddAnmRStep(anm_name,0.855)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.551)
		Bladex.AddAnmLStep(anm_name,0.670)
		Bladex.AddAnmEvent("Dwf_g_bad_sword2","W2hToLeft",0.15)
		Bladex.AddAnmEvent("Dwf_g_bad_sword2","W2hToRight",0.98)


		anm_name="Dwf_g_bad_sword3"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_bad_sword3.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.133)
		Bladex.AddAnmRStep(anm_name,0.550)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.322)
		Bladex.AddAnmLStep(anm_name,0.548)
		Bladex.AddAnmEvent("Dwf_g_bad_sword3","W2hToLeft",0.15)
		Bladex.AddAnmEvent("Dwf_g_bad_sword3","W2hToRight",0.98)




		#
		# Ataques
		#





		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_01.BMV","Dwf_g_01",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_01",0)
		Bladex.AddAnmLStep("Dwf_g_01",0)
		Bladex.AddAnmRRelease("Dwf_g_01",0.21)
		Bladex.AddAnmRStep("Dwf_g_01",0.36)
		Bladex.AddAnmRRelease("Dwf_g_01",0.64)
		Bladex.AddAnmRStep("Dwf_g_01",0.83)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_01a.BMV","Dwf_g_01a",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_01a",0)
		Bladex.AddAnmLStep("Dwf_g_01a",0)
		Bladex.AddAnmRRelease("Dwf_g_01a",0.21)
		Bladex.AddAnmRStep("Dwf_g_01a",0.36)
		Bladex.AddAnmRRelease("Dwf_g_01a",0.64)
		Bladex.AddAnmRStep("Dwf_g_01a",0.83)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_02.BMV","Dwf_g_02",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_02",0)
		Bladex.AddAnmLStep("Dwf_g_02",0)
		Bladex.AddAnmRRelease("Dwf_g_02",0.15)
		Bladex.AddAnmRStep("Dwf_g_02",0.27)
		Bladex.AddAnmRRelease("Dwf_g_02",0.55)
		Bladex.AddAnmRStep("Dwf_g_02",0.74)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_02a.BMV","Dwf_g_02a",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_02a",0)
		Bladex.AddAnmLStep("Dwf_g_02a",0)
		Bladex.AddAnmRRelease("Dwf_g_02a",0.15)
		Bladex.AddAnmRStep("Dwf_g_02a",0.27)
		Bladex.AddAnmRRelease("Dwf_g_02a",0.55)
		Bladex.AddAnmRStep("Dwf_g_02a",0.74)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_05.BMV","Dwf_g_05",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_05",0)
		Bladex.AddAnmLStep("Dwf_g_05",0)
		Bladex.AddAnmRRelease("Dwf_g_05",0.28)
		Bladex.AddAnmRStep("Dwf_g_05",0.5)
		Bladex.AddAnmRRelease("Dwf_g_05",0.72)
		Bladex.AddAnmRStep("Dwf_g_05",0.9)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_05a.BMV","Dwf_g_05a",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_05a",0)
		Bladex.AddAnmLStep("Dwf_g_05a",0)
		Bladex.AddAnmRRelease("Dwf_g_05a",0.28)
		Bladex.AddAnmRStep("Dwf_g_05a",0.5)
		Bladex.AddAnmRRelease("Dwf_g_05a",0.72)
		Bladex.AddAnmRStep("Dwf_g_05a",0.9)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_06.BMV","Dwf_g_06",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_06",0)
		Bladex.AddAnmLStep("Dwf_g_06",0)
		Bladex.AddAnmRRelease("Dwf_g_06",0.19)
		Bladex.AddAnmRStep("Dwf_g_06",0.37)
		Bladex.AddAnmRRelease("Dwf_g_06",0.67)
		Bladex.AddAnmRStep("Dwf_g_06",0.85)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_06a.BMV","Dwf_g_06a",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_06a",0)
		Bladex.AddAnmLStep("Dwf_g_06a",0)
		Bladex.AddAnmRRelease("Dwf_g_06a",0.19)
		Bladex.AddAnmRStep("Dwf_g_06a",0.37)
		Bladex.AddAnmRRelease("Dwf_g_06a",0.67)
		Bladex.AddAnmRStep("Dwf_g_06a",0.85)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_07.BMV","Dwf_g_07",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_07",0)
		Bladex.AddAnmLStep("Dwf_g_07",0)
		Bladex.AddAnmRRelease("Dwf_g_07",0.15)
		Bladex.AddAnmRStep("Dwf_g_07",0.35)
		Bladex.AddAnmRRelease("Dwf_g_07",0.51)
		Bladex.AddAnmRStep("Dwf_g_07",0.72)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_07a.BMV","Dwf_g_07a",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_07a",0)
		Bladex.AddAnmLStep("Dwf_g_07a",0)
		Bladex.AddAnmRRelease("Dwf_g_07a",0.15)
		Bladex.AddAnmRStep("Dwf_g_07a",0.35)
		Bladex.AddAnmRRelease("Dwf_g_07a",0.51)
		Bladex.AddAnmRStep("Dwf_g_07a",0.72)



		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_08.BMV","Dwf_g_08",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_08",0)
		Bladex.AddAnmLStep("Dwf_g_08",0)
		Bladex.AddAnmRRelease("Dwf_g_08",0.29)
		Bladex.AddAnmRStep("Dwf_g_08",0.49)
		Bladex.AddAnmRRelease("Dwf_g_08",0.72)
		Bladex.AddAnmRStep("Dwf_g_08",0.89)


		Bladex.LoadSampledAnimation("../../Anm/Kgt_g_09.BMV","Dwf_g_09",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_09",0)
		Bladex.AddAnmLStep("Dwf_g_09",0)
		Bladex.AddAnmRRelease("Dwf_g_09",0.23)
		Bladex.AddAnmRStep("Dwf_g_09",0.36)
		Bladex.AddAnmRRelease("Dwf_g_09",0.55)
		Bladex.AddAnmRStep("Dwf_g_09",0.71)

		Bladex.LoadSampledAnimation("../../Anm/Kgt_g_09a.BMV","Dwf_g_09a",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_09a",0)
		Bladex.AddAnmLStep("Dwf_g_09a",0)
		Bladex.AddAnmRRelease("Dwf_g_09a",0.23)
		Bladex.AddAnmRStep("Dwf_g_09a",0.36)
		Bladex.AddAnmRRelease("Dwf_g_09a",0.55)
		Bladex.AddAnmRStep("Dwf_g_09a",0.71)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_11.BMV","Dwf_g_11",0)
		Bladex.AddAnmRStep("Dwf_g_11",0)
		Bladex.AddAnmLStep("Dwf_g_11",0)
		Bladex.AddAnmRRelease("Dwf_g_11",0.4)
		Bladex.AddAnmRStep("Dwf_g_11",0.55)
		Bladex.AddAnmLRelease("Dwf_g_11",0.78)
		Bladex.AddAnmLStep("Dwf_g_11",0.93)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_12.BMV","Dwf_g_12",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_12",0)
		Bladex.AddAnmLStep("Dwf_g_12",0)
		Bladex.AddAnmRRelease("Dwf_g_12",0.4)
		Bladex.AddAnmRStep("Dwf_g_12",0.52)
		Bladex.AddAnmLRelease("Dwf_g_12",0.71)
		Bladex.AddAnmLStep("Dwf_g_12",0.85)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_13.BMV","Dwf_g_13",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_13",0)
		Bladex.AddAnmLStep("Dwf_g_13",0)
		Bladex.AddAnmRRelease("Dwf_g_13",0.41)
		Bladex.AddAnmRStep("Dwf_g_13",0.57)
		Bladex.AddAnmLRelease("Dwf_g_13",0.76)
		Bladex.AddAnmLStep("Dwf_g_13",0.89)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_14.BMV","Dwf_g_14",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_14",0)
		Bladex.AddAnmLStep("Dwf_g_14",0)
		Bladex.AddAnmLRelease("Dwf_g_14",0.15)
		Bladex.AddAnmLStep("Dwf_g_14",0.37)
		Bladex.AddAnmRRelease("Dwf_g_14",0.43)
		Bladex.AddAnmRStep("Dwf_g_14",0.56)
		Bladex.AddAnmLRelease("Dwf_g_14",0.73)
		Bladex.AddAnmLStep("Dwf_g_14",0.85)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_15.BMV","Dwf_g_15",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_15",0)
		Bladex.AddAnmLStep("Dwf_g_15",0)
		Bladex.AddAnmRRelease("Dwf_g_15",0.17)
		Bladex.AddAnmRStep("Dwf_g_15",0.35)
		Bladex.AddAnmLRelease("Dwf_g_15",0.56)
		Bladex.AddAnmLStep("Dwf_g_15",0.76)



		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_16.BMV","Dwf_g_16",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_16",0)
		Bladex.AddAnmLStep("Dwf_g_16",0)
		Bladex.AddAnmRRelease("Dwf_g_16",0.16)
		Bladex.AddAnmRStep("Dwf_g_16",0.275)
		Bladex.AddAnmLRelease("Dwf_g_16",0.54)
		Bladex.AddAnmLStep("Dwf_g_16",0.675)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_17.BMV","Dwf_g_17",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_17",0)
		Bladex.AddAnmLStep("Dwf_g_17",0)
		Bladex.AddAnmRRelease("Dwf_g_17",0.16)
		Bladex.AddAnmRStep("Dwf_g_17",0.27)
		Bladex.AddAnmLRelease("Dwf_g_17",0.53)
		Bladex.AddAnmLStep("Dwf_g_17",0.65)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_18.BMV","Dwf_g_18",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_18",0)
		Bladex.AddAnmLStep("Dwf_g_18",0)
		Bladex.AddAnmRRelease("Dwf_g_18",0.37)
		Bladex.AddAnmRStep("Dwf_g_18",0.50)
		Bladex.AddAnmLRelease("Dwf_g_18",0.77)
		Bladex.AddAnmLStep("Dwf_g_18",0.90)

		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_21.BMV","Dwf_g_21",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_21",0)
		Bladex.AddAnmLStep("Dwf_g_21",0)
		Bladex.AddAnmRRelease("Dwf_g_21",0.51)
		Bladex.AddAnmRStep("Dwf_g_21",0.669)
		Bladex.AddAnmLRelease("Dwf_g_21",0.696)
		Bladex.AddAnmLStep("Dwf_g_21",0.834)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_22.BMV","Dwf_g_22",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_22",0)
		Bladex.AddAnmLStep("Dwf_g_22",0)
		Bladex.AddAnmRRelease("Dwf_g_22",0.474)
		Bladex.AddAnmRStep("Dwf_g_22",0.544)
		Bladex.AddAnmRRelease("Dwf_g_22",0.605)
		Bladex.AddAnmRStep("Dwf_g_22",0.67)
		Bladex.AddAnmRRelease("Dwf_g_22",0.781)
		Bladex.AddAnmRStep("Dwf_g_22",0.847)
		Bladex.AddAnmLRelease("Dwf_g_22",0.2)
		Bladex.AddAnmLStep("Dwf_g_22",0.433)
		Bladex.AddAnmLRelease("Dwf_g_22",0.549)
		Bladex.AddAnmLStep("Dwf_g_22",0.6)


		Bladex.LoadSampledAnimation("../../Anm/Kgt_g_23.BMV","Dwf_g_23",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_23",0)
		Bladex.AddAnmLStep("Dwf_g_23",0)
		Bladex.AddAnmRRelease("Dwf_g_23",0.529)
		Bladex.AddAnmRStep("Dwf_g_23",0.743)
		Bladex.AddAnmLRelease("Dwf_g_23",0.75)
		Bladex.AddAnmLStep("Dwf_g_23",0.85)


		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_26.BMV","Dwf_g_26",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_26",0)
		Bladex.AddAnmLStep("Dwf_g_26",0)
		Bladex.AddAnmRRelease("Dwf_g_26",0.135)
		Bladex.AddAnmRStep("Dwf_g_26",0.236)
		Bladex.AddAnmLRelease("Dwf_g_26",0.48)
		Bladex.AddAnmLStep("Dwf_g_26",0.682)
		Bladex.AddAnmLRelease("Dwf_g_26",0.79)
		Bladex.AddAnmLStep("Dwf_g_26",0.885)


		Bladex.LoadSampledAnimation("../../Anm/Kgt_g_27.BMV","Dwf_g_27",0,"Dwarf_N")
		Bladex.AddAnmRStep("Dwf_g_27",0)
		Bladex.AddAnmLStep("Dwf_g_27",0)
		Bladex.AddAnmRRelease("Dwf_g_27",0.28)
		Bladex.AddAnmRStep("Dwf_g_27",0.5)
		Bladex.AddAnmLRelease("Dwf_g_27",0.72)
		Bladex.AddAnmLStep("Dwf_g_27",0.74)


		anm_name="Dwf_g_31"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_31.BMV",anm_name,0,"Dwarf_N")
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


		anm_name="Dwf_g_s22low_new"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_s22low_new.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.139)
		Bladex.AddAnmRStep(anm_name,0.296)
		Bladex.AddAnmRRelease(anm_name,0.336)
		Bladex.AddAnmRStep(anm_name,0.809)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.031)
		Bladex.AddAnmLStep(anm_name,0.331)
		Bladex.AddAnmLRelease(anm_name,0.695)
		Bladex.AddAnmLStep(anm_name,0.819)


		anm_name="Dwf_g_01low_new"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_01low_new.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.156)
		Bladex.AddAnmRStep(anm_name,0.702)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.026)
		Bladex.AddAnmLStep(anm_name,0.232)
		Bladex.AddAnmLRelease(anm_name,0.608)
		Bladex.AddAnmLStep(anm_name,0.862)



		anm_name="Dwf_g_s3_new"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_s3_new.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.129)
		Bladex.AddAnmRStep(anm_name,0.288)
		Bladex.AddAnmRRelease(anm_name,0.343)
		Bladex.AddAnmRStep(anm_name,0.861)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.037)
		Bladex.AddAnmLStep(anm_name,0.325)
		Bladex.AddAnmLRelease(anm_name,0.799)
		Bladex.AddAnmLStep(anm_name,0.985)




		anm_name="Dwf_g_s18"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_s18.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.020)
		Bladex.AddAnmRStep(anm_name,0.108)
		Bladex.AddAnmRRelease(anm_name,0.324)
		Bladex.AddAnmRStep(anm_name,0.618)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.324)
		Bladex.AddAnmLStep(anm_name,0.618)
		Bladex.AddAnmLRelease(anm_name,0.863)
		Bladex.AddAnmLStep(anm_name,0.961)



		anm_name="Dwf_g_s18_2h"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_s18_2h.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.020)
		Bladex.AddAnmRStep(anm_name,0.108)
		Bladex.AddAnmRRelease(anm_name,0.324)
		Bladex.AddAnmRStep(anm_name,0.618)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.324)
		Bladex.AddAnmLStep(anm_name,0.618)
		Bladex.AddAnmLRelease(anm_name,0.863)
		Bladex.AddAnmLStep(anm_name,0.961)


		anm_name="Dwf_g_12low"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_12low.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.283)
		Bladex.AddAnmRStep(anm_name,0.717)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.110)
		Bladex.AddAnmLStep(anm_name,0.241)


		anm_name="Dwf_g_s11"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_s11.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.215)
		Bladex.AddAnmRStep(anm_name,0.864)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.107)
		Bladex.AddAnmLStep(anm_name,0.277)
		Bladex.AddAnmLRelease(anm_name,0.798)
		Bladex.AddAnmLStep(anm_name,1.000)


		anm_name="Dwf_g_32_5_3new"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_32_5_3new.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.100)
		Bladex.AddAnmRStep(anm_name,0.177)
		Bladex.AddAnmRRelease(anm_name,0.531)
		Bladex.AddAnmRStep(anm_name,0.660)
		Bladex.AddAnmRRelease(anm_name,0.788)
		Bladex.AddAnmRStep(anm_name,0.913)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.338)
		Bladex.AddAnmLStep(anm_name,0.492)


		anm_name="Dwf_g_27kata"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_27kata.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.155)
		Bladex.AddAnmRStep(anm_name,0.524)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.534)
		Bladex.AddAnmLStep(anm_name,0.951)




		anm_name="Dwf_g_06lowkata_new"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_06lowkata_new.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.041)
		Bladex.AddAnmRStep(anm_name,0.453)
		Bladex.AddAnmRRelease(anm_name,0.692)
		Bladex.AddAnmRStep(anm_name,0.865)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.384)
		Bladex.AddAnmLStep(anm_name,0.680)





	############ GOLPES SIN ARMAS ###############



		anm_name="Dwf_g_punch1"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_punch1.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.059)
		Bladex.AddAnmLStep(anm_name,0.500)
		Bladex.AddAnmLRelease(anm_name,0.745)
		Bladex.AddAnmLStep(anm_name,0.922)



		anm_name="Dwf_g_punch2"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_punch2.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.020)
		Bladex.AddAnmRStep(anm_name,0.108)
		Bladex.AddAnmRRelease(anm_name,0.324)
		Bladex.AddAnmRStep(anm_name,0.618)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.324)
		Bladex.AddAnmLStep(anm_name,0.618)
		Bladex.AddAnmLRelease(anm_name,0.863)
		Bladex.AddAnmLStep(anm_name,0.961)



		anm_name="Dwf_g_kick"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_kick.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.056)
		Bladex.AddAnmRStep(anm_name,0.993)
		Bladex.AddAnmRRelease(anm_name,1.542)
		Bladex.AddAnmLStep(anm_name,0.000)





		anm_name="Dwf_g_draw_rlx"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_draw_rlx.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.817)
		Bladex.AddAnmLStep(anm_name,0.383)


		anm_name="Dwf_g_draw_run"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_draw_run.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.042)
		Bladex.AddAnmLStep(anm_name,0.319)







		#
		# Movimientos en combate
		#
		anm_name="Dwf_attack_l"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_l.BMV",anm_name,1)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.119)
		Bladex.AddAnmLStep(anm_name,0.291)
		Bladex.AddAnmLRelease(anm_name,0.458)
		Bladex.AddAnmLStep(anm_name,0.667)
		Bladex.AddAnmLRelease(anm_name,0.786)
		Bladex.AddAnmLStep(anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.0)
		Bladex.AddAnmRRelease(anm_name,0.02)
		Bladex.AddAnmRStep(anm_name,0.17)
		Bladex.AddAnmRRelease(anm_name,0.32)
		Bladex.AddAnmRStep(anm_name,0.516)
		Bladex.AddAnmRRelease(anm_name,0.675)
		Bladex.AddAnmRStep(anm_name,0.910)
		Bladex.AddStopTests(anm_name)


		anm_name="Dwf_attack_l_spear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_l_spear.BMV",anm_name,1)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.119)
		Bladex.AddAnmLStep(anm_name,0.291)
		Bladex.AddAnmLRelease(anm_name,0.458)
		Bladex.AddAnmLStep(anm_name,0.667)
		Bladex.AddAnmLRelease(anm_name,0.786)
		Bladex.AddAnmLStep(anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.0)
		Bladex.AddAnmRRelease(anm_name,0.02)
		Bladex.AddAnmRStep(anm_name,0.17)
		Bladex.AddAnmRRelease(anm_name,0.32)
		Bladex.AddAnmRStep(anm_name,0.516)
		Bladex.AddAnmRRelease(anm_name,0.675)
		Bladex.AddAnmRStep(anm_name,0.910)
		Bladex.AddStopTests(anm_name)




		anm_name="Dwf_attack_l_2w"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_l_sword.BMV",anm_name,1)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.119)
		Bladex.AddAnmLStep(anm_name,0.291)
		Bladex.AddAnmLRelease(anm_name,0.458)
		Bladex.AddAnmLStep(anm_name,0.667)
		Bladex.AddAnmLRelease(anm_name,0.786)
		Bladex.AddAnmLStep(anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.0)
		Bladex.AddAnmRRelease(anm_name,0.02)
		Bladex.AddAnmRStep(anm_name,0.17)
		Bladex.AddAnmRRelease(anm_name,0.32)
		Bladex.AddAnmRStep(anm_name,0.516)
		Bladex.AddAnmRRelease(anm_name,0.675)
		Bladex.AddAnmRStep(anm_name,0.910)
		Bladex.AddStopTests(anm_name)



		anm_name="Dwf_attack_r" ### Borer's anm fix has been applied
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_r.BMV",anm_name,1)
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
        

		anm_name="Dwf_attack_r_spear" ### Borer's anm fix has been applied
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_r_spear.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)     
		Bladex.AddAnmRRelease(anm_name,0.167) 
		Bladex.AddAnmRStep(anm_name,0.611)    
		Bladex.AddAnmRRelease(anm_name,0.722) 
		Bladex.AddAnmRStep(anm_name,1)    
		Bladex.AddAnmLRelease(anm_name,0.167) 
		Bladex.AddAnmLStep(anm_name,0.444)        
		Bladex.AddAnmLRelease(anm_name,0.667) 
		Bladex.AddAnmLStep(anm_name,1.0)
		Bladex.AddStopTests(anm_name)           


		anm_name="Dwf_attack_r_2w" ### Borer's anm fix has been applied
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_r_sword.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)     
		Bladex.AddAnmRRelease(anm_name,0.167) 
		Bladex.AddAnmRStep(anm_name,0.611)    
		Bladex.AddAnmRRelease(anm_name,0.722) 
		Bladex.AddAnmRStep(anm_name,1)    
		Bladex.AddAnmLRelease(anm_name,0.167) 
		Bladex.AddAnmLStep(anm_name,0.444)        
		Bladex.AddAnmLRelease(anm_name,0.667) 
		Bladex.AddAnmLStep(anm_name,1.0)

		anm_name="Dwf_attack_f"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_f.BMV",anm_name,1)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmLRelease(anm_name,0.31)
		Bladex.AddAnmRStep(anm_name,0.5)
		Bladex.AddAnmRRelease(anm_name,0.79)
		Bladex.AddAnmLStep(anm_name,1.0)
		Bladex.AddStopTests(anm_name)

		anm_name="Dwf_attack_b"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_b.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.503)
		Bladex.AddAnmRStep(anm_name,1.000)
		Bladex.AddAnmLStep(anm_name,0.492)
		Bladex.AddAnmLRelease(anm_name,1.000)
		Bladex.AddStopTests(anm_name)

		anm_name="Dwf_attack_b_spear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_b_spear.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.493)
		Bladex.AddAnmRStep(anm_name,1.000)
		Bladex.AddAnmLStep(anm_name,0.482)
		Bladex.AddAnmLRelease(anm_name,1.000)
		Bladex.AddStopTests(anm_name)


		anm_name="Dwf_g_d_l"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_d_l.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.159)
		Bladex.AddAnmRStep(anm_name,0.324)
		Bladex.AddAnmRRelease(anm_name,0.648)
		Bladex.AddAnmRStep(anm_name,0.870)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.064)
		Bladex.AddAnmLStep(anm_name,0.190)
		Bladex.AddAnmLRelease(anm_name,0.392)
		Bladex.AddAnmLStep(anm_name,0.477)
		#este es el de captura


		anm_name="Dwf_g_d_r"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_d_r.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.093)
		Bladex.AddAnmRStep(anm_name,0.222)
		Bladex.AddAnmRStep(anm_name,0.222)
		Bladex.AddAnmRRelease(anm_name,0.407)
		Bladex.AddAnmRStep(anm_name,0.704)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.190)
		Bladex.AddAnmLStep(anm_name,0.318)





		anm_name="Dwf_d_b"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_d_b.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.125)
		Bladex.AddAnmRStep(anm_name,0.417)
		Bladex.AddAnmLRelease(anm_name,0.333)
		Bladex.AddAnmLStep(anm_name,0.583)


		#anm_name="Dwf_d_r"
		#Bladex.LoadSampledAnimation("../../Anm/Dwf_d_r.BMV",anm_name,0,"Dwarf_N")
		#Bladex.AddAnmRStep(anm_name,0)
		#Bladex.AddAnmLStep(anm_name,0)
		#Bladex.AddAnmRRelease(anm_name,0.021)
		#Bladex.AddAnmRStep(anm_name,0.23)
		#Bladex.AddAnmLRelease(anm_name,0.167)
		#Bladex.AddAnmLStep(anm_name,0.333)


#		anm_name="Dwf_g_d_l"
#		Bladex.LoadSampledAnimation("../../Anm/Dwf_g_d_l.BMV",anm_name,0)
#		Bladex.AddAnmRStep(anm_name,0.000)
#		Bladex.AddAnmRRelease(anm_name,0.039)
#		Bladex.AddAnmRStep(anm_name,0.326)
#		Bladex.AddAnmRRelease(anm_name,0.655)
#		Bladex.AddAnmRStep(anm_name,1.000)
#		Bladex.AddAnmLStep(anm_name,0.000)
#		Bladex.AddAnmLRelease(anm_name,0.004)
#		Bladex.AddAnmLStep(anm_name,0.232)
#		Bladex.AddAnmLRelease(anm_name,0.595)
#		Bladex.AddAnmLStep(anm_name,0.690)
#		#este es a mano

		anm_name="Dwf_attack_l_s"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_l_s.BMV",anm_name,1,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.119)
		Bladex.AddAnmLStep(anm_name,0.291)
		Bladex.AddAnmLRelease(anm_name,0.458)
		Bladex.AddAnmLStep(anm_name,0.667)
		Bladex.AddAnmLRelease(anm_name,0.786)
		Bladex.AddAnmLStep(anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.0)
		Bladex.AddAnmRRelease(anm_name,0.02)
		Bladex.AddAnmRStep(anm_name,0.17)
		Bladex.AddAnmRRelease(anm_name,0.32)
		Bladex.AddAnmRStep(anm_name,0.516)
		Bladex.AddAnmRRelease(anm_name,0.675)
		Bladex.AddAnmRStep(anm_name,0.910)
		Bladex.AddStopTests(anm_name)

		anm_name="Dwf_attack_r_s"  ### Borer's anm fix has been applied
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_r_s.BMV",anm_name,1,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)     
		Bladex.AddAnmRStep(anm_name,0.270)    
		Bladex.AddAnmLRelease(anm_name,0.524) 
		Bladex.AddAnmLStep(anm_name,1.0)     
		Bladex.AddAnmRRelease(anm_name,0.994) 
		Bladex.AddStopTests(anm_name)



		anm_name="Dwf_attack_f_s"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_f_s.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.0)
		Bladex.AddAnmRRelease(anm_name,0.33)
		Bladex.AddAnmRStep(anm_name,1.0)
		Bladex.AddAnmLStep(anm_name,0.36)
		Bladex.AddAnmLRelease(anm_name,0.81)
		Bladex.AddStopTests(anm_name)

		anm_name="Dwf_attack_b_s"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_b_s.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.503)
		Bladex.AddAnmRStep(anm_name,1.000)
		Bladex.AddAnmLStep(anm_name,0.492)
		Bladex.AddAnmLRelease(anm_name,1.000)
		Bladex.AddStopTests(anm_name)

		anm_name="Dwf_rlx_f"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_f.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)


		anm_name="Dwf_rlx_f_spear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_f_spear.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)

		anm_name="Dwf_rlx_f_sword"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_f_sword.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)

#		anm_name="Dwf_rlx_s"
#		Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_s.BMV",anm_name,1,"Dwarf_N")
#		Bladex.AddAnmRStep(anm_name,0)
#		Bladex.AddAnmLStep(anm_name,0)
#
		anm_name="Dwf_attack_rlx_s"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_rlx_s.BMV",anm_name,1)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)



		#
		# Saltos
		#
		anm_name="Dwf_jmp_no"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jmp_no.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.188)
		Bladex.AddAnmRStep(anm_name,0.596)
		Bladex.AddAnmRRelease(anm_name,0.761)
		Bladex.AddAnmRStep(anm_name,0.845)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.188)
		Bladex.AddAnmLStep(anm_name,0.596)


		anm_name="Dwf_jmp_1h"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jmp_1h.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.188)
		Bladex.AddAnmRStep(anm_name,0.596)
		Bladex.AddAnmRRelease(anm_name,0.761)
		Bladex.AddAnmRStep(anm_name,0.845)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.188)
		Bladex.AddAnmLStep(anm_name,0.596)




		anm_name="Dwf_jmph0_no"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jmph0_no.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.419)
		Bladex.AddAnmRStep(anm_name,0.681)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.419)
		Bladex.AddAnmLStep(anm_name,0.7)


		#
		# Slip
		#
		anm_name="Dwf_slip"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)

		anm_name="Dwf_slip_b"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)

		anm_name="Dwf_derrape"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0,"Dwarf_N")
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
		anm_name="Dwf_b1"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_b1.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)

		anm_name="Dwf_b2"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_b2.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)

		anm_name="Dwf_b3"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_b3.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)




	####
	# Heridas sin movimiento
	####


		anm_name="Dwf_hurt_f_back"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_f_l_arm"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_f_breast"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_f_head"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_f_l_leg"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_f_r_arm"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_f_r_leg"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_head"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_head.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_l_arm"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_l_arm.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_l_leg"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_l_leg.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_r_arm"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_r_arm.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_r_leg"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_r_leg.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_back"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_back.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_hurt_breast"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_breast.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)



		###############
		#
		#Hurt
		#
		###############

		anm_name="Dwf_hurt_jog"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_jog.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.21)
		Bladex.AddAnmRRelease(anm_name,0.36)
		Bladex.AddAnmRStep(anm_name,0.55)
		Bladex.AddAnmLStep(anm_name,0.0)
		Bladex.AddAnmLRelease(anm_name,0.07)
		Bladex.AddAnmLStep(anm_name,0.4)
		Bladex.AddAnmLRelease(anm_name,0.58)
		Bladex.AddAnmLStep(anm_name,0.8)


		anm_name="Dwf_hurt_f_big"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_big.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.0)
		Bladex.AddAnmRRelease(anm_name,0.4)
		Bladex.AddAnmRStep(anm_name,0.6)

		Bladex.AddAnmLStep(anm_name,0.0)
		Bladex.AddAnmLRelease(anm_name,0.27)
		Bladex.AddAnmLStep(anm_name,0.43)



		anm_name="Dwf_hurt_f_lite"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_hurt_f_lite.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.0)
		Bladex.AddAnmRRelease(anm_name,0.35)
		Bladex.AddAnmRStep(anm_name,0.59)
		Bladex.AddAnmLStep(anm_name,0.0)
		Bladex.AddAnmLRelease(anm_name,0.55)
		Bladex.AddAnmLStep(anm_name,1.0)


		anm_name="Dwf_parry2w"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_parry2w.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.189)
		Bladex.AddAnmRRelease(anm_name,0.631)
		Bladex.AddAnmRStep(anm_name,0.959)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.156)
		Bladex.AddAnmLStep(anm_name,0.313)
		Bladex.AddAnmLRelease(anm_name,0.416)


		anm_name="Dwf_parryspear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_parryspear.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.093)
		Bladex.AddAnmRStep(anm_name,0.519)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.384)
		Bladex.AddAnmLStep(anm_name,0.669)


		anm_name="Dwf_df_01_spear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_df_01_spear.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.380)
		Bladex.AddAnmRStep(anm_name,0.665)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.240)
		Bladex.AddAnmLStep(anm_name,0.585)

		anm_name="Dwf_df_01_2w"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_df_01_2w.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.614)
		Bladex.AddAnmRStep(anm_name,0.882)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.526)
		Bladex.AddAnmLStep(anm_name,0.771)

		anm_name="Dwf_df_02_2w"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_df_02_2w.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.397)
		Bladex.AddAnmRStep(anm_name,0.637)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.214)
		Bladex.AddAnmLStep(anm_name,0.572)

		anm_name="Dwf_df_02_spear"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_df_02_spear.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.454)
		Bladex.AddAnmRStep(anm_name,0.753)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.221)
		Bladex.AddAnmLStep(anm_name,0.593)






		#############	########      #########
		#
		# Trepar      ###################
		#
		##################


		anm_name="Dwf_clmb_low_1h"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_clmb_low_1h.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.17)
		Bladex.AddAnmRStep(anm_name,0.41)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.48)
		Bladex.AddAnmLStep(anm_name,0.82)

		anm_name="Dwf_clmb_medlow_1h"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_clmb_medlow_1h.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.30)
		Bladex.AddAnmRStep(anm_name,0.79)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.28)
		Bladex.AddAnmLStep(anm_name,0.53)
		Bladex.AddAnmLRelease(anm_name,0.83)
		Bladex.AddAnmLStep(anm_name,0.98)

		anm_name="Dwf_clmb_medium_1h"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_clmb_medium_1h.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.13)
		Bladex.AddAnmRStep(anm_name,0.84)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.13)
		Bladex.AddAnmLStep(anm_name,0.100)

		anm_name="Dwf_clmb_high_1h"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_clmb_high_1h.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.11)
		Bladex.AddAnmRStep(anm_name,0.88)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.11)
		Bladex.AddAnmLStep(anm_name,1.0)


		#################
		#
		# Coger
		#
		##################


		anm_name="Dwf_tke_r_04"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_04.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.202)
		Bladex.AddAnmRStep(anm_name,0.420)
		Bladex.AddAnmRRelease(anm_name,0.750)
		Bladex.AddAnmRStep(anm_name,1.0)

		anm_name="Dwf_tke_r_key03"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_key03.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.153)
		Bladex.AddAnmRStep(anm_name,0.316)
		Bladex.AddAnmRRelease(anm_name,0.600)
		Bladex.AddAnmRStep(anm_name,0.833)

		anm_name="Dwf_tke_r_02"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_02.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.200)
		Bladex.AddAnmRStep(anm_name,0.348)
		Bladex.AddAnmRRelease(anm_name,0.582)
		Bladex.AddAnmRStep(anm_name,0.865)

		anm_name="Dwf_tke_r_key01"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_key01.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.175)
		Bladex.AddAnmRRelease(anm_name,0.382)
		Bladex.AddAnmRStep(anm_name,0.594)
		Bladex.AddAnmRRelease(anm_name,1.0)

		anm_name="Dwf_tke_r_05"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_05.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.205)
		Bladex.AddAnmRStep(anm_name,0.401)
		Bladex.AddAnmRRelease(anm_name,0.576)
		Bladex.AddAnmRStep(anm_name,0.827)

		anm_name="Dwf_tke_r_key05"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_key05.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.103)
		Bladex.AddAnmRStep(anm_name,0.230)
		Bladex.AddAnmRRelease(anm_name,0.392)
		Bladex.AddAnmRStep(anm_name,0.639)

		anm_name="Dwf_tke_r_03"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_03.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.137)
		Bladex.AddAnmRStep(anm_name,0.351)
		Bladex.AddAnmRRelease(anm_name,0.532)
		Bladex.AddAnmRStep(anm_name,0.762)

		anm_name="Dwf_tke_r_key02"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_key02.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.100)
		Bladex.AddAnmRStep(anm_name,0.232)
		Bladex.AddAnmRRelease(anm_name,0.389)
		Bladex.AddAnmRStep(anm_name,0.588)

		anm_name="Dwf_tke_r_01"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_01.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.242)
		Bladex.AddAnmLStep(anm_name,0.455)
		Bladex.AddAnmLRelease(anm_name,0.712)
		Bladex.AddAnmLStep(anm_name,0.884)

		anm_name="Dwf_tke_r_key00"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_tke_r_key00.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.156)
		Bladex.AddAnmRRelease(anm_name,0.329)
		Bladex.AddAnmRStep(anm_name,0.421)
		Bladex.AddAnmRRelease(anm_name,1.0)

		#anm_name="Dwf_wbk_t"
		#Bladex.LoadSampledAnimation("../../Anm/Dwf_wbk_t.BMV",anm_name,0,"Dwarf_N")
		#Bladex.AddAnmLStep(anm_name,0)
		#Bladex.AddAnmRStep(anm_name,0)
		#Bladex.AddAnmRRelease(anm_name,0.135)
		#Bladex.AddAnmRStep(anm_name,0.525)
		#Bladex.AddAnmLRelease(anm_name,0.670)
		#Bladex.AddAnmLStep(anm_name,1)
		#Bladex.AddStopTests(anm_name)

		anm_name="Dwf_df_s_broken"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_df_s_broken.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmLRelease(anm_name,0.131)
		Bladex.AddAnmLStep(anm_name,0.414)
		Bladex.AddAnmRRelease(anm_name,0.439)
		Bladex.AddAnmRStep(anm_name,0.595)
		Bladex.AddAnmLRelease(anm_name,0.708)
		Bladex.AddAnmLStep(anm_name,0.867)

		anm_name="Dwf_sword_broken"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_sword_broken.BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.103)
		Bladex.AddAnmRStep(anm_name,0.332)
		Bladex.AddAnmLRelease(anm_name,0.333)
		Bladex.AddAnmLStep(anm_name,0.497)

		anm_name="Dwf_sword_reaction"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_sword_broken.BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.103)
		Bladex.AddAnmRStep(anm_name,0.332)
		Bladex.AddAnmLRelease(anm_name,0.333)
		Bladex.AddAnmLStep(anm_name,0.497)

		anm_name="Dwf_df_02"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_df_02.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)
		Bladex.AddAnmRRelease(anm_name,0.310)
		Bladex.AddAnmLRelease(anm_name,0.310)
		Bladex.AddAnmRStep(anm_name,0.569)
		Bladex.AddAnmLStep(anm_name,0.832)

		anm_name="Dwf_df_01"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_df_01.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)


		##########################################
		########### GIROS DE 180� ################
		##########################################




		anm_name="Dwf_wlk_turn"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_wlk_turn.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.189)
		Bladex.AddAnmRStep(anm_name,0.499)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.669)
		Bladex.AddAnmLStep(anm_name,1.000)


		anm_name="Dwf_snk_turn"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_snk_turn.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.403)
		Bladex.AddAnmRStep(anm_name,0.821)
		Bladex.AddAnmLStep(anm_name,0.217)
		Bladex.AddAnmLRelease(anm_name,0.833)


		anm_name="Dwf_jog_turn"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_jog_turn.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.155)
		Bladex.AddAnmRRelease(anm_name,0.848)
		Bladex.AddAnmLStep(anm_name,0.326)
		Bladex.AddAnmLRelease(anm_name,1.000)


		anm_name="Dwf_rlx_turn"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_rlx_turn.BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.375)
		Bladex.AddAnmRStep(anm_name,0.635)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.150)
		Bladex.AddAnmLStep(anm_name,0.669)

		#################
		#
		# Soltar y cambiar Armas
		#
		##################

		anm_name="Dwf_drp_r"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_drp_r.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)

		anm_name="Dwf_drp_l"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_drp_l.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)

		anm_name="Dwf_attack_chg_r_l"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_chg_r_l.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)

		anm_name="Dwf_attack_chg_r"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_chg_r.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)

		anm_name="Dwf_attack_chg_l"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_attack_chg_l.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0)



		#################
		#
		# Soltar y cambiar Armas
		#
		##################



		anm_name="Dwf_drink"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)

		anm_name="Dwf_eat00"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)

		anm_name="Dwf_gulp00"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_gulp00.BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)

		anm_name="Dwf_attack_drink"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_drink.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.00)


		#################
		#
		# Fuegos y activar puertas
		#
		##################



		anm_name="Dwf_key"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.00)

		anm_name="Dwf_lvr_u"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.126)
		Bladex.AddAnmRStep(anm_name,0.294)
		Bladex.AddAnmRRelease(anm_name,0.720)
		Bladex.AddAnmRStep(anm_name,0.875)

		anm_name="Dwf_lvr_d"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.126)
		Bladex.AddAnmRStep(anm_name,0.294)
		Bladex.AddAnmRRelease(anm_name,0.720)
		Bladex.AddAnmRStep(anm_name,0.875)

		anm_name="Dwf_pulsador"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.075)
		Bladex.AddAnmRStep(anm_name,0.233)
		Bladex.AddAnmRRelease(anm_name,0.566)
		Bladex.AddAnmRStep(anm_name,0.856)

		anm_name="Dwf_fire0"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.113)
		Bladex.AddAnmRStep(anm_name,0.29)
		Bladex.AddAnmRRelease(anm_name,0.751)
		Bladex.AddAnmRStep(anm_name,0.98)

		anm_name="Dwf_fire1"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.091)
		Bladex.AddAnmRStep(anm_name,0.2)
		Bladex.AddAnmRRelease(anm_name,0.650)
		Bladex.AddAnmRStep(anm_name,0.824)

		anm_name="Dwf_fire2"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.081)
		Bladex.AddAnmRStep(anm_name,0.225)
		Bladex.AddAnmRRelease(anm_name,0.752)
		Bladex.AddAnmRStep(anm_name,0.922)

		anm_name="Dwf_fire3"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.104)
		Bladex.AddAnmRStep(anm_name,0.239)
		Bladex.AddAnmRRelease(anm_name,0.748)
		Bladex.AddAnmRStep(anm_name,0.953)

		anm_name="Dwf_fire_g"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmRRelease(anm_name,0.108)
		Bladex.AddAnmRStep(anm_name,0.244)
		Bladex.AddAnmRRelease(anm_name,0.758)
		Bladex.AddAnmRStep(anm_name,0.926)




		#################
		#
		# Muertes (me mueeeeeroooo!!!!!). Que asco!!!
		#
		##################





		anm_name="Dwf_dth0"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth0.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)


		anm_name="Dwf_dth_c1"
		Bladex.LoadSampledAnimation("../../Anm/Dwf_dth_c1.BMV",anm_name,0)
		Bladex.AddAnmLStep(anm_name,0.00)
		Bladex.AddAnmRStep(anm_name,0.00)
		Bladex.AddAnmLRelease(anm_name,0.040)
		Bladex.AddAnmLStep(anm_name,0.081)

		anm_name="Dwf_dth_c2"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c2.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.037)
		Bladex.AddAnmRStep(anm_name,0.083)
		Bladex.AddAnmRRelease(anm_name,0.166)
		Bladex.AddAnmRStep(anm_name,0.306)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.083)
		Bladex.AddAnmLStep(anm_name,0.126)

		anm_name="Dwf_dth_c3"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c3.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.583)
		Bladex.AddAnmRStep(anm_name,0.758)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.597)
		Bladex.AddAnmLStep(anm_name,0.886)


		anm_name="Dwf_dth_c4"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c4.BMV",anm_name,0,"Dwarf_N")
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


		anm_name="Dwf_dth_c5"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c5.BMV",anm_name,0,"Dwarf_N")
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


		anm_name="Dwf_dth_c6"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c6.BMV",anm_name,0,"Dwarf_N")
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

		anm_name="Dwf_dth_c7"
		Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.282)
		Bladex.AddAnmRStep(anm_name,0.384)
		Bladex.AddAnmRRelease(anm_name,0.659)
		Bladex.AddAnmRStep(anm_name,0.887)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.579)
		Bladex.AddAnmLStep(anm_name,0.890)

		anm_name="Dwf_dth_n00"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.641)
		Bladex.AddAnmRStep(anm_name,0.878)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.192)
		Bladex.AddAnmLStep(anm_name,0.411)
		Bladex.AddAnmLRelease(anm_name,0.626)
		Bladex.AddAnmLStep(anm_name,0.873)

		anm_name="Dwf_dth_n01"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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


		anm_name="Dwf_dth_n02"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.681)
		Bladex.AddAnmRStep(anm_name,0.859)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.315)
		Bladex.AddAnmLStep(anm_name,0.611)
		Bladex.AddAnmLRelease(anm_name,0.703)
		Bladex.AddAnmLStep(anm_name,0.921)

		anm_name="Dwf_dth_n03"
		Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.101)
		Bladex.AddAnmRStep(anm_name,0.271)
		Bladex.AddAnmRRelease(anm_name,0.478)
		Bladex.AddAnmRStep(anm_name,1.000)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.530)
		Bladex.AddAnmLStep(anm_name,0.692)

		anm_name="Dwf_dth_n04"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n04.BMV",anm_name,0,"Dwarf_N")
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

		anm_name="Dwf_dth_n05"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n05.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.825)
		Bladex.AddAnmRStep(anm_name,0.979)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.050)
		Bladex.AddAnmLStep(anm_name,0.138)
		Bladex.AddAnmLRelease(anm_name,0.816)
		Bladex.AddAnmLStep(anm_name,0.950)

		anm_name="Dwf_dth_n06"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0,"Dwarf_N")
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

		anm_name="Dwf_dth_burn"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_burn.BMV",anm_name,0,"Dwarf_N")
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


		anm_name="Dwf_dth_rock"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rock.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmLStep(anm_name,0.000)

		anm_name="Dwf_dth_rockfront"
		Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rockfront.BMV",anm_name,0,"Dwarf_N")
		Bladex.AddAnmRStep(anm_name,0.000)
		Bladex.AddAnmRRelease(anm_name,0.348)
		Bladex.AddAnmRStep(anm_name,0.796)
		Bladex.AddAnmLStep(anm_name,0.000)
		Bladex.AddAnmLRelease(anm_name,0.335)
		Bladex.AddAnmLStep(anm_name,0.792)
