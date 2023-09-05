##///
##||| KNIGHTANIMATIONSET.PY TITANIUM
##||| Change list:
##||| * Ajusted sneak walk timings
##||| * Removed steps from _fire type anims where they were not needed.
##||| 
##\\\ 

import Bladex
import Enm_Def






def LoadKnightAnimationSet(ct_name):

	print "Loading the knight animation sets..."

	#### Relax ####

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_no.BMV","Rlx_no_Kgt",1)
	Bladex.AddAnmRStep("Rlx_no_Kgt",0.0)
	Bladex.AddAnmLStep("Rlx_no_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_1h.BMV","Rlx_1h_Kgt",1)
	Bladex.AddAnmRStep("Rlx_1h_Kgt",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_2h.BMV","Rlx_2h_Kgt",1)
	Bladex.AddAnmRStep("Rlx_2h_Kgt",0.0)
	Bladex.AddAnmLStep("Rlx_2h_Kgt",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_s.BMV","Rlx_s_Kgt",1)
	Bladex.AddAnmRStep("Rlx_s_Kgt",0.0)
	Bladex.AddAnmLStep("Rlx_s_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_b.BMV","Rlx_b_Kgt",1)
	Bladex.AddAnmRStep("Rlx_b_Kgt",0.0)
	Bladex.AddAnmLStep("Rlx_b_Kgt",0.0)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_sword.BMV","Rlx_2w_Kgt",1)
	Bladex.AddAnmRStep("Rlx_2w_Kgt",0.0)
	Bladex.AddAnmLStep("Rlx_2w_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_spear.BMV","Rlx_spear_Kgt",1)
	Bladex.AddAnmRStep("Rlx_spear_Kgt",0.0)
	Bladex.AddAnmLStep("Rlx_spear_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_vt.BMV","Kgt_rlx_vt",1)
	Bladex.AddAnmRStep("Kgt_rlx_vt",0.0)
	Bladex.AddAnmLStep("Kgt_rlx_vt",0.0)


	### CORRER   ####
	Bladex.LoadSampledAnimation("../../Anm/Kgt_jog_no.BMV","Jog_no_Kgt",1)
	Bladex.AddAnmRStep("Jog_no_Kgt",0.0)
	Bladex.AddAnmRRelease("Jog_no_Kgt",0.266)
	Bladex.AddAnmRStep("Jog_no_Kgt",1.0)
	Bladex.AddAnmLStep("Jog_no_Kgt",0.505)
	Bladex.AddAnmLRelease("Jog_no_Kgt",0.783)
	Bladex.AddStopTests("Jog_no_Kgt")

	Bladex.LoadSampledAnimation("../../Anm/Kgt_jog_1h.BMV","Jog_1h_Kgt",1)
	Bladex.AddAnmLStep("Jog_1h_Kgt",0.00)
	Bladex.AddAnmLRelease("Jog_1h_Kgt",0.31)
	Bladex.AddAnmLStep("Jog_1h_Kgt",1.0)
	Bladex.AddAnmRStep("Jog_1h_Kgt",0.5)
	Bladex.AddAnmRRelease("Jog_1h_Kgt",0.79)
	Bladex.AddStopTests("Jog_1h_Kgt")

	Bladex.LoadSampledAnimation("../../Anm/Kgt_jog_b.BMV","Jog_b_Kgt",1)
	Bladex.AddAnmLStep("Jog_b_Kgt",0.00)
	Bladex.AddAnmLRelease("Jog_b_Kgt",0.31)
	Bladex.AddAnmRStep("Jog_b_Kgt",0.5)
	Bladex.AddAnmRRelease("Jog_b_Kgt",0.79)
	Bladex.AddAnmLStep("Jog_b_Kgt",1.0)
	Bladex.AddStopTests("Jog_b_Kgt")

	Bladex.LoadSampledAnimation("../../Anm/Kgt_jog_sword.BMV","Jog_2w_Kgt",1)
	Bladex.AddAnmLStep("Jog_2w_Kgt",0.00)
	Bladex.AddAnmLRelease("Jog_2w_Kgt",0.31)
	Bladex.AddAnmRStep("Jog_2w_Kgt",0.5)
	Bladex.AddAnmRRelease("Jog_2w_Kgt",0.79)
	Bladex.AddAnmLStep("Jog_2w_Kgt",1.0)
	Bladex.AddStopTests("Jog_2w_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_jog_spear.BMV","Jog_spear_Kgt",1)
	Bladex.AddAnmLStep("Jog_spear_Kgt",0.00)
	Bladex.AddAnmLRelease("Jog_spear_Kgt",0.31)
	Bladex.AddAnmRStep("Jog_spear_Kgt",0.5)
	Bladex.AddAnmRRelease("Jog_spear_Kgt",0.79)
	Bladex.AddAnmLStep("Jog_spear_Kgt",1.0)
	Bladex.AddStopTests("Jog_spear_Kgt")


	### CORRER ATRAS ###

	anm_name="Kgt_jogb_1h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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


	anm_name="Kgt_jogb_sword"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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

	anm_name="Kgt_jogb_spear"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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



	anm_name="Kgt_jogb_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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

	anm_name="Kgt_jogb_2h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.126)
	Bladex.AddAnmRStep(anm_name,0.340)
	Bladex.AddAnmRRelease(anm_name,0.480)
	Bladex.AddAnmRStep(anm_name,0.676)
	Bladex.AddAnmRRelease(anm_name,0.810)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.035)
	Bladex.AddAnmLStep(anm_name,0.228)
	Bladex.AddAnmLRelease(anm_name,0.343)
	Bladex.AddAnmLStep(anm_name,0.578)
	Bladex.AddAnmLRelease(anm_name,0.695)
	Bladex.AddAnmLStep(anm_name,0.899)
	Bladex.AddStopTests(anm_name)

	anm_name="Kgt_jogb_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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
	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_no.BMV","Snk_no_Kgt",1)
	Bladex.AddAnmRStep("Snk_no_Kgt",0.0)
	Bladex.AddAnmLStep("Snk_no_Kgt",0.0)
	Bladex.AddAnmRStep("Snk_no_Kgt",1.0)
	Bladex.AddAnmRRelease("Snk_no_Kgt",0.628)
	Bladex.AddAnmLRelease("Snk_no_Kgt",0.113)
	Bladex.AddAnmLStep("Snk_no_Kgt",0.452)

	Bladex.AddStopTests("Snk_no_Kgt")

	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_1h.BMV","Snk_1h_Kgt",1)
	Bladex.AddAnmLStep("Snk_1h_Kgt",0.0)                                    # Timings changed for sneak compatibility.
	Bladex.AddAnmRStep("Snk_1h_Kgt",0.0)                                    #
	Bladex.AddAnmLRelease("Snk_1h_Kgt",0.161)                               #
	Bladex.AddAnmLStep("Snk_1h_Kgt",0.477)                                  #
	Bladex.AddAnmRRelease("Snk_1h_Kgt",0.648)                               #
	Bladex.AddAnmRStep("Snk_1h_Kgt",1.0)                                    #           -LeadHead
    
	Bladex.AddStopTests("Snk_1h_Kgt")

	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_spear.BMV","Snk_spear_Kgt",1)
	Bladex.AddAnmLStep("Snk_spear_Kgt",0.0)                                 # Timings changed for sneak compatibility.
	Bladex.AddAnmRStep("Snk_spear_Kgt",0.0)                                 # 
	Bladex.AddAnmLRelease("Snk_spear_Kgt",0.161)                            #
	Bladex.AddAnmLStep("Snk_spear_Kgt",0.477)                               #
	Bladex.AddAnmRRelease("Snk_spear_Kgt",0.648)                            #
	Bladex.AddAnmRStep("Snk_spear_Kgt",1.0)                                 #           -LeadHead

	Bladex.AddStopTests("Snk_spear_Kgt")                                    

	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_sword.BMV","Snk_2w_Kgt",1)
	Bladex.AddAnmLStep("Snk_2w_Kgt",0.0)                                    # Timings changed for sneak compatibility.
	Bladex.AddAnmRStep("Snk_2w_Kgt",0.0)                                    # 
	Bladex.AddAnmLRelease("Snk_2w_Kgt",0.161)                               #
	Bladex.AddAnmLStep("Snk_2w_Kgt",0.477)                                  #
	Bladex.AddAnmRRelease("Snk_2w_Kgt",0.648)                               #
	Bladex.AddAnmRStep("Snk_2w_Kgt",1.0)                                    #           -LeadHead    
    
	Bladex.AddStopTests("Snk_2w_Kgt")




	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_b.BMV","Snk_b_Kgt",1)
	Bladex.AddAnmRStep("Snk_b_Kgt",0.0)
	Bladex.AddAnmRRelease("Snk_b_Kgt",0.608)
	Bladex.AddAnmRStep("Snk_b_Kgt",1.0)
	Bladex.AddAnmLStep("Snk_b_Kgt",0.509)
	Bladex.AddAnmLRelease("Snk_b_Kgt",0.952)
	Bladex.AddStopTests("Snk_b_Kgt")


	#### WBK ####


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_1h.BMV","Wbk_1h_Kgt",1)
	Bladex.AddAnmRStep("Wbk_1h_Kgt",0.543)
	Bladex.AddAnmLStep("Wbk_1h_Kgt",0)
	Bladex.AddAnmRRelease("Wbk_1h_Kgt",1)
	Bladex.AddAnmLRelease("Wbk_1h_Kgt",0.678)
	Bladex.AddAnmLStep("Wbk_1h_Kgt",1)
	Bladex.AddStopTests("Wbk_1h_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_2h.BMV","Wbk_2h_Kgt",1)
	Bladex.AddAnmRStep("Wbk_2h_Kgt",0.0)
	Bladex.AddAnmLStep("Wbk_2h_Kgt",0.0)
	Bladex.AddAnmRRelease("Wbk_2h_Kgt",0.125)
	Bladex.AddAnmRStep("Wbk_2h_Kgt",0.537)
	Bladex.AddAnmLRelease("Wbk_2h_Kgt",0.661)
	Bladex.AddAnmLStep("Wbk_2h_Kgt",1.0)
	Bladex.AddStopTests("Wbk_2h_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_no.BMV","Wbk_no_Kgt",1)
	Bladex.AddAnmRStep("Wbk_no_Kgt",0.543)
	Bladex.AddAnmLStep("Wbk_no_Kgt",0)
	Bladex.AddAnmRRelease("Wbk_no_Kgt",1)
	Bladex.AddAnmLRelease("Wbk_no_Kgt",0.678)
	Bladex.AddAnmLStep("Wbk_no_Kgt",1)
	Bladex.AddStopTests("Wbk_no_Kgt")


#	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_s.BMV","Wbk_s_Kgt",1)
#
#	Bladex.AddAnmRStep("Wbk_s_Kgt",0.0)
#	Bladex.AddAnmLStep("Wbk_s_Kgt",0.0)
#	Bladex.AddAnmRRelease("Wbk_s_Kgt",0.127)
#	Bladex.AddAnmRStep("Wbk_s_Kgt",0.496)
#	Bladex.AddAnmLRelease("Wbk_s_Kgt",0.648)
#	Bladex.AddAnmLStep("Wbk_s_Kgt",1)
#	Bladex.AddStopTests("Wbk_s_Kgt")
#
#
#
	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_b.BMV","Wbk_b_Kgt",1)

	Bladex.AddAnmRStep("Wbk_b_Kgt",0.0)
	Bladex.AddAnmLStep("Wbk_b_Kgt",0.0)
	Bladex.AddAnmRRelease("Wbk_b_Kgt",0.144)
	Bladex.AddAnmRStep("Wbk_b_Kgt",0.537)
	Bladex.AddAnmLRelease("Wbk_b_Kgt",0.640)
	Bladex.AddAnmLStep("Wbk_b_Kgt",1.0)
	Bladex.AddStopTests("Wbk_b_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_spear.BMV","Wbk_spear_Kgt",1)

	Bladex.AddAnmRStep("Wbk_spear_Kgt",0.543)
	Bladex.AddAnmLStep("Wbk_spear_Kgt",0)
	Bladex.AddAnmRRelease("Wbk_spear_Kgt",1)
	Bladex.AddAnmLRelease("Wbk_spear_Kgt",0.678)
	Bladex.AddAnmLStep("Wbk_spear_Kgt",1)
	Bladex.AddStopTests("Wbk_spear_Kgt")

	Bladex.LoadSampledAnimation("../../Anm/Kgt_wbk_sword.BMV","Wbk_2w_Kgt",1)

	Bladex.AddAnmRStep("Wbk_2w_Kgt",0.543)
	Bladex.AddAnmLStep("Wbk_2w_Kgt",0)
	Bladex.AddAnmRRelease("Wbk_2w_Kgt",1)
	Bladex.AddAnmLRelease("Wbk_2w_Kgt",0.678)
	Bladex.AddAnmLStep("Wbk_2w_Kgt",1)
	Bladex.AddStopTests("Wbk_2w_Kgt")

#	Bladex.AddAnmRStep("Wbk_no_Kgt",0.0)
#	Bladex.AddAnmLStep("Wbk_no_Kgt",0.0)
#	Bladex.AddAnmRRelease("Wbk_no_Kgt",0.127)
#	Bladex.AddAnmRStep("Wbk_no_Kgt",0.496)
#	Bladex.AddAnmLRelease("Wbk_no_Kgt",0.648)
#	Bladex.AddAnmLStep("Wbk_no_Kgt",1.0)
#	Bladex.AddStopTests("Wbk_no_Kgt")




	#
	#### Caminar ####
	#



	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_no.BMV","Wlk_no_Kgt",1)

	Bladex.AddAnmRStep("Wlk_no_Kgt",0.0)
	Bladex.AddAnmRRelease("Wlk_no_Kgt",0.5)
	Bladex.AddAnmRStep("Wlk_no_Kgt",1.0)
	Bladex.AddAnmLRelease("Wlk_no_Kgt",1.0)
	Bladex.AddAnmLStep("Wlk_no_Kgt",0.5)
	Bladex.AddStopTests("Wlk_no_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_1h.BMV","Wlk_1h_Kgt",1)

	Bladex.AddAnmRStep("Wlk_1h_Kgt",0.0)
	Bladex.AddAnmRRelease("Wlk_1h_Kgt",0.470)
	Bladex.AddAnmRStep("Wlk_1h_Kgt",1.0)
	Bladex.AddAnmLStep("Wlk_1h_Kgt",0.4)
	Bladex.AddAnmLRelease("Wlk_1h_Kgt",1.0)
	Bladex.AddStopTests("Wlk_1h_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_sword.BMV","Wlk_2w_Kgt",1)
	Bladex.AddAnmRStep("Wlk_2w_Kgt",0.0)
	Bladex.AddAnmLStep("Wlk_2w_Kgt",0.4)
	Bladex.AddAnmRStep("Wlk_2w_Kgt",1.0)
	Bladex.AddAnmRRelease("Wlk_2w_Kgt",0.470)
	Bladex.AddAnmLRelease("Wlk_2w_Kgt",1.0)
	Bladex.AddStopTests("Wlk_2w_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_spear.BMV","Wlk_spear_Kgt",1)

	Bladex.AddAnmRStep("Wlk_spear_Kgt",0.0)
	Bladex.AddAnmLStep("Wlk_spear_Kgt",0.4)
	Bladex.AddAnmRStep("Wlk_spear_Kgt",1)
	Bladex.AddAnmRRelease("Wlk_spear_Kgt",0.470)
	Bladex.AddAnmLRelease("Wlk_spear_Kgt",1.0)
	Bladex.AddStopTests("Wlk_spear_Kgt")




	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_2h.BMV","Wlk_2h_Kgt",1)
	Bladex.AddAnmRStep("Wlk_2h_Kgt",0.000)
	Bladex.AddAnmRStep("Wlk_2h_Kgt",1.000)
	Bladex.AddAnmLStep("Wlk_2h_Kgt",0.500)
	Bladex.AddAnmRRelease("Wlk_2h_Kgt",0.500)
	Bladex.AddAnmLRelease("Wlk_2h_Kgt",1.0)
	Bladex.AddStopTests("Wlk_2h_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_b.BMV","Wlk_b_Kgt",1)
	Bladex.AddAnmRStep("Wlk_b_Kgt",0.0)
	Bladex.AddAnmRRelease("Wlk_b_Kgt",0.608)
	Bladex.AddAnmRStep("Wlk_b_Kgt",1.0)
	Bladex.AddAnmLStep("Wlk_b_Kgt",0.509)
	Bladex.AddAnmLRelease("Wlk_b_Kgt",0.952)
	Bladex.AddStopTests("Wlk_b_Kgt")


	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_s.BMV","Wlk_s_Kgt",1)

	Bladex.AddAnmRStep("Wlk_s_Kgt",0.0)
	Bladex.AddAnmLStep("Wlk_s_Kgt",0.5)
	Bladex.AddAnmRStep("Wlk_s_Kgt",1.0)
	Bladex.AddAnmRRelease("Wlk_s_Kgt",0.5)
	Bladex.AddAnmLRelease("Wlk_s_Kgt",1.0)
	Bladex.AddStopTests("Wlk_s_Kgt")





	#### Caidas ####

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_low_no.BMV","FallLow_Kgt",0)
	Bladex.AddAnmRStep("FallLow_Kgt",0.0)
	Bladex.AddAnmLStep("FallLow_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_med_no.BMV","FallMed_Kgt",0)
	Bladex.AddAnmRStep("FallMed_Kgt",0.0)
	Bladex.AddAnmLStep("FallMed_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_fll_high_no.BMV","FallHigh_Kgt",0)
	Bladex.AddAnmRStep("FallHigh_Kgt",0.0)
	Bladex.AddAnmLStep("FallHigh_Kgt",0.0)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Kgt",1)
	#Bladex.AddAnmRStep("Dth_Fll_Kgt",0.0)
	#Bladex.AddAnmLStep("Dth_Fll_Kgt",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Kgt",0)
	Bladex.AddAnmRStep("Dth_Fll2_Kgt",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Kgt",0.0)




	#
	# Ataques
	#
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_08.BMV","Kgt_g_08",0)
	Bladex.AddAnmRStep("Kgt_g_08",0)
	Bladex.AddAnmLStep("Kgt_g_08",0)
	Bladex.AddAnmRRelease("Kgt_g_08",0.29)
	Bladex.AddAnmRStep("Kgt_g_08",0.49)
	Bladex.AddAnmRRelease("Kgt_g_08",0.72)
	Bladex.AddAnmRStep("Kgt_g_08",0.89)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01.BMV","Kgt_g_01",0)
	Bladex.AddAnmRStep("Kgt_g_01",0)
	Bladex.AddAnmLStep("Kgt_g_01",0)
	Bladex.AddAnmRRelease("Kgt_g_01",0.21)
	Bladex.AddAnmRStep("Kgt_g_01",0.36)
	Bladex.AddAnmRRelease("Kgt_g_01",0.64)
	Bladex.AddAnmRStep("Kgt_g_01",0.83)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_02.BMV","Kgt_g_02",0)
	Bladex.AddAnmRStep("Kgt_g_02",0)
	Bladex.AddAnmLStep("Kgt_g_02",0)
	Bladex.AddAnmRRelease("Kgt_g_02",0.15)
	Bladex.AddAnmRStep("Kgt_g_02",0.27)
	Bladex.AddAnmRRelease("Kgt_g_02",0.55)
	Bladex.AddAnmRStep("Kgt_g_02",0.74)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_05.BMV","Kgt_g_05",0)
	Bladex.AddAnmRStep("Kgt_g_05",0)
	Bladex.AddAnmLStep("Kgt_g_05",0)
	Bladex.AddAnmRRelease("Kgt_g_05",0.28)
	Bladex.AddAnmRStep("Kgt_g_05",0.5)
	Bladex.AddAnmRRelease("Kgt_g_05",0.72)
	Bladex.AddAnmRStep("Kgt_g_05",0.9)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_06.BMV","Kgt_g_06",0)
	Bladex.AddAnmRStep("Kgt_g_06",0)
	Bladex.AddAnmLStep("Kgt_g_06",0)
	Bladex.AddAnmRRelease("Kgt_g_06",0.19)
	Bladex.AddAnmRStep("Kgt_g_06",0.37)
	Bladex.AddAnmRRelease("Kgt_g_06",0.67)
	Bladex.AddAnmRStep("Kgt_g_06",0.85)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_07.BMV","Kgt_g_07",0)
	Bladex.AddAnmRStep("Kgt_g_07",0)
	Bladex.AddAnmLStep("Kgt_g_07",0)
	Bladex.AddAnmRRelease("Kgt_g_07",0.15)
	Bladex.AddAnmRStep("Kgt_g_07",0.35)
	Bladex.AddAnmRRelease("Kgt_g_07",0.51)
	Bladex.AddAnmRStep("Kgt_g_07",0.72)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_09.BMV","Kgt_g_09",0)
	Bladex.AddAnmRStep("Kgt_g_09",0)
	Bladex.AddAnmLStep("Kgt_g_09",0)
	Bladex.AddAnmRRelease("Kgt_g_09",0.23)
	Bladex.AddAnmRStep("Kgt_g_09",0.36)
	Bladex.AddAnmRRelease("Kgt_g_09",0.55)
	Bladex.AddAnmRStep("Kgt_g_09",0.71)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_13.BMV","Kgt_g_13",0)
	Bladex.AddAnmRStep("Kgt_g_13",0)
	Bladex.AddAnmLStep("Kgt_g_13",0)
	Bladex.AddAnmRRelease("Kgt_g_13",0.41)
	Bladex.AddAnmRStep("Kgt_g_13",0.57)
	Bladex.AddAnmLRelease("Kgt_g_13",0.76)
	Bladex.AddAnmLStep("Kgt_g_13",0.89)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_18.BMV","Kgt_g_18",0)
	Bladex.AddAnmRStep("Kgt_g_18",0)
	Bladex.AddAnmLStep("Kgt_g_18",0)
	Bladex.AddAnmRRelease("Kgt_g_18",0.37)
	Bladex.AddAnmRStep("Kgt_g_18",0.50)
	Bladex.AddAnmLRelease("Kgt_g_18",0.77)
	Bladex.AddAnmLStep("Kgt_g_18",0.90)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_14.BMV","Kgt_g_14",0)
	Bladex.AddAnmRStep("Kgt_g_14",0)
	Bladex.AddAnmLStep("Kgt_g_14",0)
	Bladex.AddAnmLRelease("Kgt_g_14",0.15)
	Bladex.AddAnmLStep("Kgt_g_14",0.37)
	Bladex.AddAnmRRelease("Kgt_g_14",0.43)
	Bladex.AddAnmRStep("Kgt_g_14",0.56)
	Bladex.AddAnmLRelease("Kgt_g_14",0.73)
	Bladex.AddAnmLStep("Kgt_g_14",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_11.BMV","Kgt_g_11",0)
	Bladex.AddAnmRStep("Kgt_g_11",0)
	Bladex.AddAnmLStep("Kgt_g_11",0)
	Bladex.AddAnmRRelease("Kgt_g_11",0.4)
	Bladex.AddAnmRStep("Kgt_g_11",0.55)
	Bladex.AddAnmLRelease("Kgt_g_11",0.78)
	Bladex.AddAnmLStep("Kgt_g_11",0.93)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_16.BMV","Kgt_g_16",0)
	Bladex.AddAnmRStep("Kgt_g_16",0)
	Bladex.AddAnmLStep("Kgt_g_16",0)
	Bladex.AddAnmRRelease("Kgt_g_16",0.16)
	Bladex.AddAnmRStep("Kgt_g_16",0.275)
	Bladex.AddAnmLRelease("Kgt_g_16",0.54)
	Bladex.AddAnmLStep("Kgt_g_16",0.675)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_12.BMV","Kgt_g_12",0)
	Bladex.AddAnmRStep("Kgt_g_12",0)
	Bladex.AddAnmLStep("Kgt_g_12",0)
	Bladex.AddAnmRRelease("Kgt_g_12",0.4)
	Bladex.AddAnmRStep("Kgt_g_12",0.52)
	Bladex.AddAnmLRelease("Kgt_g_12",0.71)
	Bladex.AddAnmLStep("Kgt_g_12",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_17.BMV","Kgt_g_17",0)
	Bladex.AddAnmRStep("Kgt_g_17",0)
	Bladex.AddAnmLStep("Kgt_g_17",0)
	Bladex.AddAnmRRelease("Kgt_g_17",0.16)
	Bladex.AddAnmRStep("Kgt_g_17",0.27)
	Bladex.AddAnmLRelease("Kgt_g_17",0.53)
	Bladex.AddAnmLStep("Kgt_g_17",0.65)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_15.BMV","Kgt_g_15",0)
	Bladex.AddAnmRStep("Kgt_g_15",0)
	Bladex.AddAnmLStep("Kgt_g_15",0)
	Bladex.AddAnmRRelease("Kgt_g_15",0.17)
	Bladex.AddAnmRStep("Kgt_g_15",0.35)
	Bladex.AddAnmLRelease("Kgt_g_15",0.56)
	Bladex.AddAnmLStep("Kgt_g_15",0.76)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_21.BMV","Kgt_g_21",0)
	Bladex.AddAnmRStep("Kgt_g_21",0)
	Bladex.AddAnmLStep("Kgt_g_21",0)
	Bladex.AddAnmRRelease("Kgt_g_21",0.51)
	Bladex.AddAnmRStep("Kgt_g_21",0.669)
	Bladex.AddAnmLRelease("Kgt_g_21",0.696)
	Bladex.AddAnmLStep("Kgt_g_21",0.834)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_22.BMV","Kgt_g_22",0)
	Bladex.AddAnmRStep("Kgt_g_22",0)
	Bladex.AddAnmLStep("Kgt_g_22",0)
	Bladex.AddAnmRRelease("Kgt_g_22",0.474)
	Bladex.AddAnmRStep("Kgt_g_22",0.544)
	Bladex.AddAnmRRelease("Kgt_g_22",0.605)
	Bladex.AddAnmRStep("Kgt_g_22",0.67)
	Bladex.AddAnmRRelease("Kgt_g_22",0.781)
	Bladex.AddAnmRStep("Kgt_g_22",0.847)
	Bladex.AddAnmLRelease("Kgt_g_22",0.2)
	Bladex.AddAnmLStep("Kgt_g_22",0.433)
	Bladex.AddAnmLRelease("Kgt_g_22",0.549)
	Bladex.AddAnmLStep("Kgt_g_22",0.6)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_23.BMV","Kgt_g_23",0)
	Bladex.AddAnmRStep("Kgt_g_23",0)
	Bladex.AddAnmLStep("Kgt_g_23",0)
	Bladex.AddAnmRRelease("Kgt_g_23",0.529)
	Bladex.AddAnmRStep("Kgt_g_23",0.743)
	Bladex.AddAnmLRelease("Kgt_g_23",0.75)
	Bladex.AddAnmLStep("Kgt_g_23",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_26.BMV","Kgt_g_26",0)
	Bladex.AddAnmRStep("Kgt_g_26",0)
	Bladex.AddAnmLStep("Kgt_g_26",0)
	Bladex.AddAnmRRelease("Kgt_g_26",0.135)
	Bladex.AddAnmRStep("Kgt_g_26",0.236)
	Bladex.AddAnmLRelease("Kgt_g_26",0.48)
	Bladex.AddAnmLStep("Kgt_g_26",0.682)
	Bladex.AddAnmLRelease("Kgt_g_26",0.79)
	Bladex.AddAnmLStep("Kgt_g_26",0.885)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_27.BMV","Kgt_g_27",0)
	Bladex.AddAnmRStep("Kgt_g_27",0)
	Bladex.AddAnmLStep("Kgt_g_27",0)
	Bladex.AddAnmRRelease("Kgt_g_27",0.535)
	Bladex.AddAnmRStep("Kgt_g_27",0.653)
	Bladex.AddAnmRRelease("Kgt_g_27",0.906)
	Bladex.AddAnmRStep("Kgt_g_27",1)
	Bladex.AddAnmLRelease("Kgt_g_27",0.691)
	Bladex.AddAnmLStep("Kgt_g_27",0.873)


	anm_name="Kgt_g_31"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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


	anm_name="Kgt_g_magic"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_magic.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.105)
	Bladex.AddAnmRRelease(anm_name,0.558)
	Bladex.AddAnmRStep(anm_name,0.762)
	Bladex.AddAnmRRelease(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.465)
	Bladex.AddAnmLStep(anm_name,0.545)
	Bladex.AddAnmEvent("Kgt_g_magic","LaunchTrail",0.595)


	anm_name="Kgt_g_magic2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_magic2.BMV",anm_name,0)
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

	Bladex.AddAnmEvent("Kgt_g_magic2","LaunchTrail",0.377)



	anm_name="Kgt_g_3s9_6new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_3s9_6new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.108)
	Bladex.AddAnmRStep(anm_name,0.197)
	Bladex.AddAnmRRelease(anm_name,0.351)
	Bladex.AddAnmRStep(anm_name,0.580)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.165)
	Bladex.AddAnmLStep(anm_name,0.288)
	Bladex.AddAnmLRelease(anm_name,0.675)
	Bladex.AddAnmLStep(anm_name,0.911)

	#Bladex.SetAnimationFactor("Kgt_g_3s9_6new",2)



	anm_name="Kgt_g_28new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_28new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.144)
	Bladex.AddAnmRStep(anm_name,0.419)
	Bladex.AddAnmLStep(anm_name,0.090)
	Bladex.AddAnmLRelease(anm_name,0.647)
	Bladex.AddAnmLStep(anm_name,0.888)
	Bladex.AddAnmLRelease(anm_name,1.000)



	anm_name="Kgt_g_12_7_s1new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_12_7_s1new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.165)
	Bladex.AddAnmRStep(anm_name,0.329)
	Bladex.AddAnmRRelease(anm_name,0.390)
	Bladex.AddAnmRStep(anm_name,0.517)
	Bladex.AddAnmRRelease(anm_name,0.744)
	Bladex.AddAnmRStep(anm_name,0.861)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.389)
	Bladex.AddAnmLStep(anm_name,0.516)



	anm_name="Kgt_g_21_6_s8new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_21_6_s8new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.108)
	Bladex.AddAnmRStep(anm_name,0.186)
	Bladex.AddAnmRRelease(anm_name,0.369)
	Bladex.AddAnmRStep(anm_name,0.410)
	Bladex.AddAnmRRelease(anm_name,0.453)
	Bladex.AddAnmRStep(anm_name,0.557)
	Bladex.AddAnmRRelease(anm_name,0.731)
	Bladex.AddAnmRStep(anm_name,0.853)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.432)
	Bladex.AddAnmLStep(anm_name,0.532)


	anm_name="Kgt_g_32_5_3new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_32_5_3new.BMV",anm_name,0)
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


	anm_name="Kgt_g_29_3new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_29_3new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.233)
	Bladex.AddAnmRStep(anm_name,0.305)
	Bladex.AddAnmRRelease(anm_name,0.363)
	Bladex.AddAnmRStep(anm_name,0.473)
	Bladex.AddAnmRRelease(anm_name,0.741)
	Bladex.AddAnmRStep(anm_name,0.899)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.116)
	Bladex.AddAnmLStep(anm_name,0.217)
	Bladex.AddAnmLRelease(anm_name,0.295)
	Bladex.AddAnmLStep(anm_name,0.350)



	anm_name="Kgt_g_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_back.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.477)
	Bladex.AddAnmRStep(anm_name,0.767)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.305)
	Bladex.AddAnmLRelease(anm_name,0.829)
	Bladex.AddAnmLStep(anm_name,1.000)




	####### Nuevos Ataques############



	anm_name="Kgt_g_07_01_19_26low_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_07_01_19_26low_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.331)
	Bladex.AddAnmRStep(anm_name,0.459)
	Bladex.AddAnmRRelease(anm_name,0.509)
	Bladex.AddAnmRStep(anm_name,0.562)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.407)
	Bladex.AddAnmLStep(anm_name,0.980)




	anm_name="Kgt_g_19_bs1_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_19_bs1_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.081)
	Bladex.AddAnmRStep(anm_name,0.215)
	Bladex.AddAnmRRelease(anm_name,0.341)
	Bladex.AddAnmRStep(anm_name,0.526)
	Bladex.AddAnmRRelease(anm_name,0.704)
	Bladex.AddAnmRStep(anm_name,0.867)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.274)
	Bladex.AddAnmLStep(anm_name,0.481)




	anm_name="Kgt_g_01_7_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01_7_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.081)
	Bladex.AddAnmRStep(anm_name,0.215)
	Bladex.AddAnmRRelease(anm_name,0.341)
	Bladex.AddAnmRStep(anm_name,0.526)
	Bladex.AddAnmRRelease(anm_name,0.704)
	Bladex.AddAnmRStep(anm_name,0.867)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.274)
	Bladex.AddAnmLStep(anm_name,0.481)




	anm_name="Kgt_g_01_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.156)
	Bladex.AddAnmRStep(anm_name,0.702)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.026)
	Bladex.AddAnmLStep(anm_name,0.232)
	Bladex.AddAnmLRelease(anm_name,0.608)
	Bladex.AddAnmLStep(anm_name,0.862)




	anm_name="Kgt_g_01low_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01low_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.156)
	Bladex.AddAnmRStep(anm_name,0.702)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.026)
	Bladex.AddAnmLStep(anm_name,0.232)
	Bladex.AddAnmLRelease(anm_name,0.608)
	Bladex.AddAnmLStep(anm_name,0.862)




	anm_name="Kgt_g_02_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_02_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.336)
	Bladex.AddAnmRRelease(anm_name,0.610)
	Bladex.AddAnmRStep(anm_name,0.865)
	Bladex.AddAnmLStep(anm_name,0.000)




	anm_name="Kgt_g_06lowkata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_06lowkata_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.041)
	Bladex.AddAnmRStep(anm_name,0.453)
	Bladex.AddAnmRRelease(anm_name,0.692)
	Bladex.AddAnmRStep(anm_name,0.865)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.384)
	Bladex.AddAnmLStep(anm_name,0.680)




	anm_name="Kgt_g_07_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_07_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.091)
	Bladex.AddAnmRStep(anm_name,0.344)
	Bladex.AddAnmRRelease(anm_name,0.553)
	Bladex.AddAnmRStep(anm_name,0.823)
	Bladex.AddAnmLStep(anm_name,0.000)




	anm_name="Kgt_g_08_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_08_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.069)
	Bladex.AddAnmRStep(anm_name,0.367)
	Bladex.AddAnmRRelease(anm_name,0.577)
	Bladex.AddAnmRStep(anm_name,0.954)
	Bladex.AddAnmLStep(anm_name,0.000)




	anm_name="Kgt_g_09_07_s6low_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_09_07_s6low_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.067)
	Bladex.AddAnmRStep(anm_name,0.921)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.414)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.952)
	Bladex.AddAnmLStep(anm_name,1.000)




	anm_name="Kgt_g_12_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_12_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.248)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.021)
	Bladex.AddAnmLStep(anm_name,0.288)
	Bladex.AddAnmLRelease(anm_name,0.776)
	Bladex.AddAnmLStep(anm_name,0.910)
	Bladex.AddAnmLStep(anm_name,1.000)




	anm_name="Kgt_g_18_11_22_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_18_11_22_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.203)
	Bladex.AddAnmRStep(anm_name,0.279)
	Bladex.AddAnmRRelease(anm_name,0.371)
	Bladex.AddAnmRStep(anm_name,0.467)
	Bladex.AddAnmRRelease(anm_name,0.521)
	Bladex.AddAnmRStep(anm_name,0.659)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.041)
	Bladex.AddAnmLStep(anm_name,0.180)
	Bladex.AddAnmLRelease(anm_name,0.258)
	Bladex.AddAnmLStep(anm_name,0.374)
	Bladex.AddAnmLStep(anm_name,0.375)
	Bladex.AddAnmLRelease(anm_name,0.648)
	Bladex.AddAnmLStep(anm_name,0.985)




	anm_name="Kgt_g_22kata_23_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_22kata_23_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.442)
	Bladex.AddAnmRStep(anm_name,0.562)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.726)
	Bladex.AddAnmLStep(anm_name,0.833)




	anm_name="Kgt_g_22lowkata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_22lowkata_new.BMV",anm_name,0.)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.162)
	Bladex.AddAnmRStep(anm_name,0.418)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.264)
	Bladex.AddAnmLStep(anm_name,0.972)




	anm_name="Kgt_g_b06_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_b06_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.155)
	Bladex.AddAnmRStep(anm_name,0.524)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.534)
	Bladex.AddAnmLStep(anm_name,0.951)




	anm_name="Kgt_g_27kata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_27kata_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.155)
	Bladex.AddAnmRStep(anm_name,0.524)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.534)
	Bladex.AddAnmLStep(anm_name,0.951)




	anm_name="Kgt_g_26low_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_26low_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.225)
	Bladex.AddAnmRStep(anm_name,0.458)
	Bladex.AddAnmRRelease(anm_name,0.713)
	Bladex.AddAnmRStep(anm_name,0.909)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.224)
	Bladex.AddAnmLStep(anm_name,0.389)
	Bladex.AddAnmLRelease(anm_name,0.466)
	Bladex.AddAnmLStep(anm_name,0.738)




	anm_name="Kgt_g_b32kata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_b32kata_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.274)
	Bladex.AddAnmRStep(anm_name,0.502)
	Bladex.AddAnmRRelease(anm_name,0.597)
	Bladex.AddAnmRStep(anm_name,0.843)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.134)
	Bladex.AddAnmLStep(anm_name,0.200)
	Bladex.AddAnmLRelease(anm_name,0.368)
	Bladex.AddAnmLStep(anm_name,0.558)
	Bladex.AddAnmLRelease(anm_name,0.814)
	Bladex.AddAnmLStep(anm_name,0.962)




	anm_name="Kgt_g_s18_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_s18_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.263)
	Bladex.AddAnmRStep(anm_name,0.508)
	Bladex.AddAnmRRelease(anm_name,0.674)
	Bladex.AddAnmRStep(anm_name,0.868)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.134)
	Bladex.AddAnmLStep(anm_name,0.426)



	anm_name="Kgt_g_s19_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_s19_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.020)
	Bladex.AddAnmRStep(anm_name,0.497)
	Bladex.AddAnmRRelease(anm_name,0.748)
	Bladex.AddAnmRStep(anm_name,0.913)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.065)
	Bladex.AddAnmLStep(anm_name,0.790)



	anm_name="Kgt_g_s22low_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_s22low_new.BMV",anm_name,0)
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



	anm_name="Kgt_g_s28kata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_s28kata_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.432)
	Bladex.AddAnmRStep(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.427)
	Bladex.AddAnmLStep(anm_name,0.541)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.991)



	anm_name="Kgt_g_s3_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_s3_new.BMV",anm_name,0)
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


	anm_name="Kgt_g_sb25_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_sb25_new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.208)
	Bladex.AddAnmRStep(anm_name,0.499)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.227)
	Bladex.AddAnmLStep(anm_name,0.432)
	Bladex.AddAnmLRelease(anm_name,0.520)
	Bladex.AddAnmLStep(anm_name,0.585)
	Bladex.AddAnmLRelease(anm_name,0.722)
	Bladex.AddAnmLStep(anm_name,0.946)





	anm_name="Kgt_g_draw_rlx"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_draw_rlx.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.817)
	Bladex.AddAnmLStep(anm_name,0.383)


	anm_name="Kgt_g_draw_run"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_draw_run.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.042)
	Bladex.AddAnmLStep(anm_name,0.319)




#	Ataques Torpes


	anm_name="Kgt_g_bad_axe"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_axe.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.099)
	Bladex.AddAnmRStep(anm_name,0.160)
	Bladex.AddAnmRRelease(anm_name,0.400)
	Bladex.AddAnmRStep(anm_name,0.446)
	Bladex.AddAnmRRelease(anm_name,0.738)
	Bladex.AddAnmRStep(anm_name,0.956)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.390)
	Bladex.AddAnmLStep(anm_name,0.445)



	anm_name="Kgt_g_bad_spear"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_spear.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.345)
	Bladex.AddAnmRStep(anm_name,0.428)
	Bladex.AddAnmRRelease(anm_name,0.664)
	Bladex.AddAnmRStep(anm_name,0.803)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.456)
	Bladex.AddAnmLStep(anm_name,0.647)



	anm_name="Kgt_g_bad_spear2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_spear2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.557)
	Bladex.AddAnmRStep(anm_name,0.657)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmLStep(anm_name,0.479)
	Bladex.AddAnmLRelease(anm_name,0.809)
	Bladex.AddAnmLStep(anm_name,0.918)



	anm_name="Kgt_g_bad_sword"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_sword.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)


	anm_name="Kgt_g_bad_no"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_no.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)

	anm_name="Kgt_g_bad_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_1h.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)


	anm_name="Kgt_g_bad_sword2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_sword2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.418)
	Bladex.AddAnmRStep(anm_name,0.522)
	Bladex.AddAnmRRelease(anm_name,0.668)
	Bladex.AddAnmRStep(anm_name,0.855)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.551)
	Bladex.AddAnmLStep(anm_name,0.670)



	anm_name="Kgt_g_bad_sword3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_sword3.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.133)
	Bladex.AddAnmRStep(anm_name,0.550)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.322)
	Bladex.AddAnmLStep(anm_name,0.548)

	Bladex.AddAnmEvent("Kgt_g_bad_sword3","W2hToLeft",0.15)
	Bladex.AddAnmEvent("Kgt_g_bad_sword3","W2hToRight",0.98)




############ GOLPES SIN ARMAS ###############



	anm_name="Kgt_g_punch1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_punch1.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.115)
	Bladex.AddAnmRStep(anm_name,0.344)
	Bladex.AddAnmRRelease(anm_name,0.688)
	Bladex.AddAnmRStep(anm_name,0.990)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.271)
	Bladex.AddAnmLStep(anm_name,0.792)




	anm_name="Kgt_g_punch2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_punch2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.133)
	Bladex.AddAnmRStep(anm_name,0.344)
	Bladex.AddAnmRRelease(anm_name,0.567)
	Bladex.AddAnmRStep(anm_name,0.800)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.167)
	Bladex.AddAnmLStep(anm_name,0.633)

	anm_name="Kgt_g_punch4"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_punch4.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.361)
	Bladex.AddAnmRStep(anm_name,0.528)
	Bladex.AddAnmRRelease(anm_name,0.806)
	Bladex.AddAnmRStep(anm_name,0.972)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.542)
	Bladex.AddAnmLStep(anm_name,0.778)


	anm_name="Kgt_g_kick"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_kick.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.160)
	Bladex.AddAnmRStep(anm_name,0.827)
	Bladex.AddAnmLStep(anm_name,0.000)



	#
	# Movimientos en combate
	#
	anm_name="Kgt_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.074)
	Bladex.AddAnmRStep(anm_name,0.259)
	Bladex.AddAnmRRelease(anm_name,0.407)
	Bladex.AddAnmRStep(anm_name,0.63)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmRStep(anm_name,0.926)
	Bladex.AddAnmLRelease(anm_name,0.148)
	Bladex.AddAnmLStep(anm_name,0.333)
	Bladex.AddAnmLRelease(anm_name,0.481)
	Bladex.AddAnmLStep(anm_name,0.697)
	Bladex.AddAnmLRelease(anm_name,0.815)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)



	anm_name="Kgt_attack_l_sword"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.215)
	Bladex.AddAnmRRelease(anm_name,0.485)
	Bladex.AddAnmRStep(anm_name,0.767)
	Bladex.AddAnmRRelease(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.182)
	Bladex.AddAnmLStep(anm_name,0.424)
	Bladex.AddAnmLRelease(anm_name,0.655)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)


	anm_name="Kgt_attack_l_spear"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.074)
	Bladex.AddAnmRStep(anm_name,0.259)
	Bladex.AddAnmRRelease(anm_name,0.407)
	Bladex.AddAnmRStep(anm_name,0.63)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmRStep(anm_name,0.926)
	Bladex.AddAnmLRelease(anm_name,0.148)
	Bladex.AddAnmLStep(anm_name,0.333)
	Bladex.AddAnmLRelease(anm_name,0.481)
	Bladex.AddAnmLStep(anm_name,0.697)
	Bladex.AddAnmLRelease(anm_name,0.815)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Kgt_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.256)
	Bladex.AddAnmRStep(anm_name,0.519)
	Bladex.AddAnmLRelease(anm_name,0.740)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)



	anm_name="Kgt_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
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

	anm_name="Kgt_attack_r_sword"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
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

	anm_name="Kgt_attack_r_spear"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
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

	anm_name="Kgt_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.270)
	Bladex.AddAnmLRelease(anm_name,0.524)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddAnmRRelease(anm_name,0.994)
	Bladex.AddStopTests(anm_name)



	anm_name="Kgt_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.317)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.457)
	Bladex.AddAnmLRelease(anm_name,0.857)
	Bladex.AddStopTests(anm_name)

	anm_name="Kgt_attack_f_sword"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.317)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.457)
	Bladex.AddAnmLRelease(anm_name,0.857)
	Bladex.AddStopTests(anm_name)


	anm_name="Kgt_attack_f_spear"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.317)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.457)
	Bladex.AddAnmLRelease(anm_name,0.857)
	Bladex.AddStopTests(anm_name)


	anm_name="Kgt_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.108)
	Bladex.AddAnmLStep(anm_name,0.459)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.579)
	Bladex.AddAnmRStep(anm_name,1.00)
	Bladex.AddStopTests(anm_name)



	anm_name="Kgt_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.325)
	Bladex.AddAnmRStep(anm_name,0.408)
	Bladex.AddAnmRRelease(anm_name,0.740)
	Bladex.AddAnmLStep(anm_name,1.0)
	Bladex.AddStopTests(anm_name)


	anm_name="Kgt_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.154)
	Bladex.AddAnmRStep(anm_name,0.474)
	Bladex.AddAnmLRelease(anm_name,0.724)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)




#Esquivas con y sin golpe



	anm_name="Kgt_d_b"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.378)
	Bladex.AddAnmRStep(anm_name,0.833)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.366)
	Bladex.AddAnmLStep(anm_name,0.680)




#	anm_name="Kgt_d_r"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.021)
#	Bladex.AddAnmRStep(anm_name,0.23)
#	Bladex.AddAnmLRelease(anm_name,0.167)
#	Bladex.AddAnmLStep(anm_name,0.333)


	anm_name="Kgt_g_d_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.175)
	Bladex.AddAnmRRelease(anm_name,0.459)
	Bladex.AddAnmRStep(anm_name,0.879)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.233)
	#POR QUE si no , pierde el angulo!!!
	Bladex.AddAnmLStep(anm_name,0.29)
	Bladex.AddAnmLRelease(anm_name,0.295)
	Bladex.AddAnmLStep(anm_name,0.438)




#	anm_name="Kgt_d_l"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0.148)
#	Bladex.AddAnmRRelease(anm_name,0.093)
#	Bladex.AddAnmRStep(anm_name,0.444)
#	Bladex.AddAnmLRelease(anm_name,1)


	anm_name="Kgt_g_d_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.144)

	#porque si no...
	Bladex.AddAnmRStep(anm_name,0.31)
	Bladex.AddAnmRRelease(anm_name,0.315)

	Bladex.AddAnmRStep(anm_name,0.540)
	Bladex.AddAnmRRelease(anm_name,0.736)
	Bladex.AddAnmRStep(anm_name,0.830)
	Bladex.AddAnmLStep(anm_name,0.132)
	Bladex.AddAnmLRelease(anm_name,0.433)
	Bladex.AddAnmLStep(anm_name,0.778)






########     Relax encarado


	anm_name="Kgt_rlx_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Kgt_rlx_f_spear"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	anm_name="Kgt_rlx_f_sword"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
#	anm_name="Kgt_rlx_s"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Kgt_attack_rlx_s"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


	#
	# Saltos
	#
	anm_name="Kgt_jmp_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	Bladex.AddAnmRStep(anm_name,0.340)
	Bladex.AddAnmLStep(anm_name,0.340)
	Bladex.AddAnmRRelease(anm_name,0.360)
	Bladex.AddAnmLRelease(anm_name,0.461)
	Bladex.AddAnmRStep(anm_name,0.499)
	Bladex.AddAnmRRelease(anm_name,0.597)
	Bladex.AddAnmRStep(anm_name,0.696)
	Bladex.AddAnmLStep(anm_name,0.696)



	anm_name="Kgt_jmp_1h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

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




	anm_name="Kgt_jmph0_no"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.324)
	Bladex.AddAnmLRelease(anm_name,0.532)
	Bladex.AddAnmRStep(anm_name,0.618)
	Bladex.AddAnmLStep(anm_name,0.843)


	#
	# Slip
	#
	anm_name="Kgt_slip"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Kgt_derrape"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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
	anm_name="Kgt_b1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Kgt_b2"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Kgt_b3"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




####
# Heridas sin movimiento
####


	anm_name="Kgt_hurt_f_back"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_f_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_f_breast"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_f_head"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_f_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Kgt_hurt_f_neck"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_f_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_f_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_head.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	#Bladex.AddAnmRRelease(anm_name,0.140)
	#Bladex.AddAnmRStep(anm_name,0.382)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_arm.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_leg.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Kgt_hurt_neck"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_neck.BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_arm.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_leg.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Kgt_hurt0"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_back.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Kgt_hurt_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_breast.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)



	anm_name="Kgt_hurt_jog"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.21)
	Bladex.AddAnmRRelease(anm_name,0.36)
	Bladex.AddAnmRStep(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.07)
	Bladex.AddAnmLStep(anm_name,0.4)
	Bladex.AddAnmLRelease(anm_name,0.58)
	Bladex.AddAnmLStep(anm_name,0.8)


	anm_name="Kgt_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.4)
	Bladex.AddAnmRStep(anm_name,0.6)

	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.27)
	Bladex.AddAnmLStep(anm_name,0.43)


	anm_name="Kgt_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.35)
	Bladex.AddAnmRStep(anm_name,0.59)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,1.0)








	anm_name="Kgt_parry2w"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_parry2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.189)
	Bladex.AddAnmRRelease(anm_name,0.631)
	Bladex.AddAnmRStep(anm_name,0.959)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.156)
	Bladex.AddAnmLStep(anm_name,0.313)
	Bladex.AddAnmLRelease(anm_name,0.416)


	anm_name="Kgt_parryspear"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_parryspear.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.093)
	Bladex.AddAnmRStep(anm_name,0.519)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.384)
	Bladex.AddAnmLStep(anm_name,0.669)

	anm_name="Kgt_df_01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_01.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Kgt_df_01_spear"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_01_spear.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.380)
	Bladex.AddAnmRStep(anm_name,0.665)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.240)
	Bladex.AddAnmLStep(anm_name,0.585)

	anm_name="Kgt_df_01_2w"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_01_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.614)
	Bladex.AddAnmRStep(anm_name,0.882)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.526)
	Bladex.AddAnmLStep(anm_name,0.771)

	anm_name="Kgt_df_02_2w"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_02_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.397)
	Bladex.AddAnmRStep(anm_name,0.637)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.214)
	Bladex.AddAnmLStep(anm_name,0.572)

	anm_name="Kgt_df_02_spear"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_02_spear.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.454)
	Bladex.AddAnmRStep(anm_name,0.753)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.221)
	Bladex.AddAnmLStep(anm_name,0.593)


	anm_name="Kgt_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.439)
	Bladex.AddAnmRStep(anm_name,595)
	Bladex.AddAnmLRelease(anm_name,0.708)
	Bladex.AddAnmLStep(anm_name,0.867)

	anm_name="Kgt_sword_broken"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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


	anm_name="Kgt_sword_reaction"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0)
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




	anm_name="Kgt_df_02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.310)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmRStep(anm_name,0.569)
	Bladex.AddAnmLStep(anm_name,0.832)



	#####################################
	#
	# Trepar
	#
	#####################################

	anm_name="Kgt_clmb_medlow_1h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.30)
	Bladex.AddAnmRStep(anm_name,0.79)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.28)
	Bladex.AddAnmLStep(anm_name,0.53)
	Bladex.AddAnmLRelease(anm_name,0.83)
	Bladex.AddAnmLStep(anm_name,0.98)

	anm_name="Kgt_clmb_medium_1h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.13)
	Bladex.AddAnmRStep(anm_name,0.84)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,1)

	anm_name="Kgt_clmb_high_1h"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.09)
	Bladex.AddAnmRStep(anm_name,0.88)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.09)
	Bladex.AddAnmLStep(anm_name,1.0)




############ COGERES / Llaves




	anm_name="Kgt_tke_r_01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.159)
	Bladex.AddAnmLStep(anm_name,0.327)
	Bladex.AddAnmLRelease(anm_name,0.689)
	Bladex.AddAnmLStep(anm_name,0.893)

	anm_name="Kgt_tke_r_02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.183)
	Bladex.AddAnmRStep(anm_name,0.343)
	Bladex.AddAnmRRelease(anm_name,0.585)
	Bladex.AddAnmRStep(anm_name,0.840)

	anm_name="Kgt_tke_r_03"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.191)
	Bladex.AddAnmRStep(anm_name,0.335)
	Bladex.AddAnmRRelease(anm_name,0.502)
	Bladex.AddAnmRStep(anm_name,0.715)

	anm_name="Kgt_tke_r_04"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.216)
	Bladex.AddAnmRStep(anm_name,0.395)
	Bladex.AddAnmRRelease(anm_name,0.716)
	Bladex.AddAnmRStep(anm_name,1)

	anm_name="Kgt_tke_r_05"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.208)
	Bladex.AddAnmRStep(anm_name,0.369)
	Bladex.AddAnmRRelease(anm_name,0.544)
	Bladex.AddAnmRStep(anm_name,0.842)

	anm_name="Kgt_tke_r_key00"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.096)
	Bladex.AddAnmLStep(anm_name,0.159)
	Bladex.AddAnmLRelease(anm_name,0.350)
	Bladex.AddAnmLStep(anm_name,0.443)

	anm_name="Kgt_tke_r_key01"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.121)
	Bladex.AddAnmRStep(anm_name,0.245)
	Bladex.AddAnmRRelease(anm_name,0.420)
	Bladex.AddAnmRStep(anm_name,0.588)


	anm_name="Kgt_tke_r_key02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.160)
	Bladex.AddAnmRStep(anm_name,0.264)
	Bladex.AddAnmRRelease(anm_name,0.408)
	Bladex.AddAnmRStep(anm_name,0.566)

	anm_name="Kgt_tke_r_key03"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.132)
	Bladex.AddAnmRStep(anm_name,0.261)
	Bladex.AddAnmRRelease(anm_name,0.489)
	Bladex.AddAnmRStep(anm_name,0.689)

	anm_name="Kgt_tke_r_key05"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.153)
	Bladex.AddAnmRStep(anm_name,0.270)
	Bladex.AddAnmRRelease(anm_name,0.401)
	Bladex.AddAnmRStep(anm_name,0.601)





	##########################################
	########### GIROS DE 180� ################
	##########################################




	anm_name="Kgt_wlk_turn"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.403)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmLStep(anm_name,0.217)
	Bladex.AddAnmLRelease(anm_name,0.833)


	anm_name="Kgt_snk_turn"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.403)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmLStep(anm_name,0.217)
	Bladex.AddAnmLRelease(anm_name,0.833)



	anm_name="Kgt_jog_turn"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.311)
	Bladex.AddAnmRStep(anm_name,0.714)
	Bladex.AddAnmRRelease(anm_name,0.808)
	Bladex.AddAnmLStep(anm_name,0.284)
	Bladex.AddAnmLRelease(anm_name,0.690)
	Bladex.AddAnmLStep(anm_name,0.971)



	anm_name="Kgt_rlx_turn"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.095)
	Bladex.AddAnmLStep(anm_name,0.875)






############	Change Weapons




	anm_name="Kgt_attack_chg_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Kgt_attack_chg_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Kgt_attack_chg_r_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)



	anm_name="Kgt_drp_r"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Kgt_drp_l"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,1)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)







############	Throw Objects




	anm_name="Kgt_1tw_l_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.25)
	Bladex.AddAnmRStep(anm_name,0.45)
	Bladex.AddAnmRRelease(anm_name,0.64)
	Bladex.AddAnmRStep(anm_name,0.97)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Kgt_1tw_h_f"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)



##########	Drink/ Eat



	anm_name="Kgt_drink"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Kgt_eat00"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Kgt_gulp00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_gulp.BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Kgt_attack_drink"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)



######## USE / ACTIVATE



	anm_name="Kgt_key"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Kgt_lvr_u"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.126)
	Bladex.AddAnmRStep(anm_name,0.294)
	Bladex.AddAnmRRelease(anm_name,0.720)
	Bladex.AddAnmRStep(anm_name,0.875)

	anm_name="Kgt_lvr_d"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.126)
	Bladex.AddAnmRStep(anm_name,0.294)
	Bladex.AddAnmRRelease(anm_name,0.720)
	Bladex.AddAnmRStep(anm_name,0.875)

	anm_name="Kgt_pulsador"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.075)
	Bladex.AddAnmRStep(anm_name,0.233)
	Bladex.AddAnmRRelease(anm_name,0.566)
	Bladex.AddAnmRStep(anm_name,0.856)

	anm_name="Kgt_fire0"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	# Bladex.AddAnmRRelease(anm_name,0.113)     # Commented all of these steps out as the knigt does NOT actually take any during this anm
	# Bladex.AddAnmRStep(anm_name,0.29)         # -LeadHead
	# Bladex.AddAnmRRelease(anm_name,0.751)
	# Bladex.AddAnmRStep(anm_name,0.98)

	anm_name="Kgt_fire1"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.091)
	Bladex.AddAnmRStep(anm_name,0.2)
	Bladex.AddAnmRRelease(anm_name,0.650)
	Bladex.AddAnmRStep(anm_name,0.824)

	anm_name="Kgt_fire2"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.081)
	Bladex.AddAnmRStep(anm_name,0.225)
	Bladex.AddAnmRRelease(anm_name,0.752)
	Bladex.AddAnmRStep(anm_name,0.922)

	anm_name="Kgt_fire3"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	# Bladex.AddAnmRRelease(anm_name,0.104)     # Commented all of these steps out as the knigt does NOT actually take any during this anm
	# Bladex.AddAnmRStep(anm_name,0.239)        # -LeadHead
	# Bladex.AddAnmRRelease(anm_name,0.748)
	# Bladex.AddAnmRStep(anm_name,0.953)

	anm_name="Kgt_fire_g"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.108)
	Bladex.AddAnmRStep(anm_name,0.244)
	Bladex.AddAnmRRelease(anm_name,0.758)
	Bladex.AddAnmRStep(anm_name,0.926)





############ MUERTES









	anm_name="Kgt_dth0"         # PLAGUE: Missing steps
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)



	anm_name="Kgt_dth_c1"       # PLAGUE: Missing steps
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)

	anm_name="Kgt_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)

	anm_name="Kgt_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)

	anm_name="Kgt_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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

	anm_name="Kgt_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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

	anm_name="Kgt_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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

	anm_name="Kgt_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Knight_N")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)



	anm_name="Kgt_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)

	anm_name="Kgt_dth_n01"
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

	anm_name="Kgt_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)

	anm_name="Kgt_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)

	anm_name="Kgt_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
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

	anm_name="Kgt_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)

	anm_name="Kgt_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0)
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

	anm_name="Kgt_dth_rock"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rock.BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Kgt_dth_rockfront"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rockfront.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.348)
	Bladex.AddAnmRStep(anm_name,0.796)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.335)
	Bladex.AddAnmLStep(anm_name,0.792)

	anm_name="Kgt_dth_burn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_burn.BMV",anm_name,0)
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
























#	JOG_ANM
#	#                     Name      WUEA,MOD_Y,SOLF,COPY_ROT,BNG_MOV,HEADF
#	Bladex.AddAnimFlags("Cos_attack_f",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
#
#
#
#
#
#
#	#### Escalones ####
#
#	#Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_up.BMV","WlkUp_Kgt",1)
#
#	Bladex.CreateDFCAnimation("../../Anm/Kgt_wlk_up.BMV","../../Anm/Kgt_wlk_no.BMV","WlkUp_Kgt",4)
#	Bladex.CreateDFCAnimation("../../Anm/Kgt_wlk_down.BMV","../../Anm/Kgt_wlk_no.BMV","WlkDown_Kgt",4)
#
#	Bladex.CreateFCAnimation("../../Anm/Kgt_stairs_u_no.BMV","StairsUp_Kgt",4)
#	Bladex.CreateDFCAnimation("../../Anm/Kgt_stairs_u_no_mas.BMV","../../Anm/Kgt_stairs_u_no.BMV","StairsUpP_Kgt",4)
#
#	Bladex.CreateFCAnimation("../../Anm/Kgt_stairs_d_no.BMV","StairsDown_Kgt",4)
#
#	Bladex.AddAnmRStep("StairsUp_Kgt",0.0)
#	Bladex.AddAnmLStep("StairsUp_Kgt",0.5)
#	Bladex.AddAnmRStep("StairsUp_Kgt",1.0)
#	Bladex.AddAnmRRelease("StairsUp_Kgt",0.5)
#	Bladex.AddAnmLRelease("StairsUp_Kgt",1.0)
#
#
#	Bladex.CreateFCAnimation("../../Anm/Kgt_stairs_back_d_no.BMV","StairsDownBack_Kgt",4)
#
#	Bladex.AddAnmRStep("StairsDownBack_Kgt",0.5)
#	Bladex.AddAnmLStep("StairsDownBack_Kgt",0.0)
#	Bladex.AddAnmRStep("StairsDownBack_Kgt",1.0)
#	Bladex.AddAnmRRelease("StairsDownBack_Kgt",1.0)
#	Bladex.AddAnmLRelease("StairsDownBack_Kgt",0.5)
#
#
#	Bladex.CreateFCAnimation("../../Anm/Kgt_stairs_up_back_no.BMV","StairsUpBack_Kgt",4)
#
#	Bladex.AddAnmRStep("StairsUpBack_Kgt",0.081)
#	Bladex.AddAnmLRelease("StairsUpBack_Kgt",0.086)
#	Bladex.AddAnmLStep("StairsUpBack_Kgt",0.472)
#	Bladex.AddAnmRRelease("StairsUpBack_Kgt",0.527)
#	Bladex.AddAnmLRelease("StairsUpBack_Kgt",1)
#
#
#	Bladex.CreateFCAnimation("../../Anm/Kgt_stairs_back_d_no_mas.BMV","StairsDownBackP_Kgt",4)
#
#	Bladex.AddAnmRStep("StairsDownBackP_Kgt",0.5)
#	Bladex.AddAnmLStep("StairsDownBackP_Kgt",0.0)
#	Bladex.AddAnmRStep("StairsDownBackP_Kgt",1.0)
#	Bladex.AddAnmRRelease("StairsDownBackP_Kgt",1.0)
#	Bladex.AddAnmLRelease("StairsDownBackP_Kgt",0.5)
#
#
#	Bladex.CreateFCAnimation("../../Anm/Kgt_stairs_up_back_no_mas.BMV","StairsUpBackP_Kgt",4)
#
#	Bladex.AddAnmRStep("StairsUpBack_Kgt",0.081)
#	Bladex.AddAnmLRelease("StairsUpBack_Kgt",0.086)
#	Bladex.AddAnmLStep("StairsUpBack_Kgt",0.472)
#	Bladex.AddAnmRRelease("StairsUpBack_Kgt",0.527)
#	Bladex.AddAnmLRelease("StairsUpBack_Kgt",1)



#	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_short_no.BMV","WlkShort_Kgt",1)
#
#	Bladex.AddAnmRStep("WlkShort_Kgt",0.0)
#	Bladex.AddAnmLStep("WlkShort_Kgt",0.5)
#	Bladex.AddAnmRStep("WlkShort_Kgt",1.0)
#	Bladex.AddAnmRRelease("WlkShort_Kgt",0.5)
#	Bladex.AddAnmLRelease("WlkShort_Kgt",1.0)
	#Aqui MANUAL !!!
	#Bladex.AddAnmEvent("WlkShort_Kgt","StopTest",0.01)
	#Bladex.AddAnmEvent("WlkShort_Kgt","StopTest",0.51)
#	Bladex.AddStopTests("WlkShort_Kgt")


#	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_short_sword.BMV","WlkShort_2w_Kgt",1)
#	Bladex.AddAnmRStep("WlkShort_2w_Kgt",0.0)
#	Bladex.AddAnmLStep("WlkShort_2w_Kgt",0.5)
#	Bladex.AddAnmRStep("WlkShort_2w_Kgt",1.0)
#	Bladex.AddAnmRRelease("WlkShort_2w_Kgt",0.5)
#	Bladex.AddAnmLRelease("WlkShort_2w_Kgt",1.0)
#	Bladex.AddStopTests("WlkShort_2w_Kgt")
#
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_wlk_short_spear.BMV","WlkShort_spear_Kgt",1)
#	Bladex.AddAnmRStep("WlkShort_spear_Kgt",0.0)
#	Bladex.AddAnmLStep("WlkShort_spear_Kgt",0.5)
#	Bladex.AddAnmRStep("WlkShort_spear_Kgt",1.0)
#	Bladex.AddAnmRRelease("WlkShort_spear_Kgt",0.5)
#	Bladex.AddAnmLRelease("WlkShort_spear_Kgt",1.0)
#	Bladex.AddStopTests("WlkShort_spear_Kgt")


	#anm_name="Kgt_attack_t_r"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,1)
	#Bladex.AddAnmLStep(anm_name,1)


	#anm_name="Kgt_attack_t_l"
	#Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
	#Bladex.AddAnmRStep(anm_name,0)
	#Bladex.AddAnmRRelease(anm_name,0)
	#Bladex.AddAnmLStep(anm_name,0)
	#Bladex.AddAnmLRelease(anm_name,0)
	#Bladex.AddAnmRStep(anm_name,1)
	#Bladex.AddAnmLStep(anm_name,1)

#	anm_name="Kgt_slip_b"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)


#	anm_name="Kgt_clmb_low_1h"
#	Bladex.LoadSampledAnimation("../../Anm/" + anm_name + ".BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmRRelease(anm_name,0.17)
#	Bladex.AddAnmRStep(anm_name,0.41)
#	Bladex.AddAnmLStep(anm_name,0)
#	Bladex.AddAnmLRelease(anm_name,0.48)
#	Bladex.AddAnmLStep(anm_name,0.82)
