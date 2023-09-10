###///
###||| AMZANIMATIONSET.PY TITANIUM
###||| Change list:
###||| * Added missing steps in death animm.
###||| * Added steps for torch anims that were missing them.
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



def LoadAmzAnimationSet(ct_name):

	print "Loading the aMaZoN animation sets..."

	#### Relax ####

	Bladex.LoadSampledAnimation("../../Anm/Amz_rlx_no.BMV","Rlx_no_Amz",1)
	Bladex.AddAnmRStep("Rlx_no_Amz",0.0)
	Bladex.AddAnmLStep("Rlx_no_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Amz_rlx_2w.BMV","Rlx_2w_Amz",1)
	Bladex.AddAnmRStep("Rlx_2w_Amz",0.0)
	Bladex.AddAnmLStep("Rlx_2w_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Amz_rlx_2h.BMV","Rlx_2h_Amz",1)
	Bladex.AddAnmRStep("Rlx_2h_Amz",0.0)
	Bladex.AddAnmLStep("Rlx_2h_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Amz_rlx_1h.BMV","Rlx_1h_Amz",1)
	Bladex.AddAnmRStep("Rlx_1h_Amz",0.0)
	Bladex.AddAnmLStep("Rlx_1h_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Amz_rlx_spear.BMV","Rlx_spear_Amz",1)
	Bladex.AddAnmRStep("Rlx_spear_Amz",0.0)
	Bladex.AddAnmLStep("Rlx_spear_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Amz_rlx_b.BMV","Rlx_b_Amz",1)
	Bladex.AddAnmRStep("Rlx_b_Amz",0.0)
	Bladex.AddAnmLStep("Rlx_b_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_vt.BMV","Amz_rlx_vt",1,"Amazon_L")
	Bladex.AddAnmRStep("Amz_rlx_vt",0.0)
	Bladex.AddAnmLStep("Amz_rlx_vt",0.0)

######## Arrojares

	Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_l_f.BMV","Amz_1tw_l_f",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_1tw_l_f",0.0)
	Bladex.AddAnmLStep("Amz_1tw_l_f",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_h_f.BMV","Amz_1tw_h_f",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_1tw_h_f",0.0)
	Bladex.AddAnmLStep("Amz_1tw_h_f",0.0)

#	Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_l_f.BMV","Amz_1tw_l",1,"Amazon_L")
#	Bladex.AddAnmRStep("Amz_1tw_l",0.0)
#	Bladex.AddAnmLStep("Amz_1tw_l",0.0)

#	Bladex.LoadSampledAnimation("../../Anm/Kgt_1tw_l_f.BMV","Amz_1tw_h",1,"Amazon_L")
#	Bladex.AddAnmRStep("Amz_1tw_h",0.0)
#	Bladex.AddAnmLStep("Amz_1tw_h",0.0)

	### CORRER   ####


	anm_name="Jog_no_Amz"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_no.BMV","Jog_no_Amz",1)
	Bladex.AddAnmRStep(anm_name,0.475)
	Bladex.AddAnmRRelease(anm_name,0.693)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.190)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)


	anm_name="Jog_s_Amz"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_s.BMV","Jog_s_Amz",1)
	Bladex.AddAnmRStep(anm_name,0.533)
	Bladex.AddAnmRRelease(anm_name,0.733)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.233)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)


	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_2w.BMV","Jog_2w_Amz",1)
	Bladex.AddAnmLStep("Jog_2w_Amz",0.00)
	Bladex.AddAnmLRelease("Jog_2w_Amz",0.31)
	Bladex.AddAnmRStep("Jog_2w_Amz",0.5)
	Bladex.AddAnmRRelease("Jog_2w_Amz",0.79)
	Bladex.AddAnmLStep("Jog_2w_Amz",1.0)
	Bladex.AddStopTests("Jog_2w_Amz")


	anm_name="Jog_spear_Amz"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_spear.BMV","Jog_spear_Amz",1)
	Bladex.AddAnmRStep(anm_name,0.533)
	Bladex.AddAnmRRelease(anm_name,0.733)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.233)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)
#   antigua animaci�n de correr con lanza borrar si queda esta como definitiva
#	Bladex.AddAnmRStep("Jog_spear_Amz",0.528)
#	Bladex.AddAnmRRelease("Jog_spear_Amz",0.833)
#	Bladex.AddAnmLStep("Jog_spear_Amz",0.000)
#	Bladex.AddAnmLRelease("Jog_spear_Amz",0.250)
#	Bladex.AddAnmLStep("Jog_spear_z",.000)
#	Bladex.AddStopTests("Jog_spear_Amz")

	anm_name="Jog_axe_Amz"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_axe.BMV","Jog_axe_Amz",1)
	Bladex.AddAnmRStep(anm_name,0.512)
	Bladex.AddAnmRRelease(anm_name,0.805)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.284)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)


	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_2h.BMV","Jog_2h_Amz",1)
	Bladex.AddAnmRStep("Jog_2h_Amz",0.460)
	Bladex.AddAnmRRelease("Jog_2h_Amz",0.711)
	Bladex.AddAnmLStep("Jog_2h_Amz",0.000)
	Bladex.AddAnmLRelease("Jog_2h_Amz",0.221)
	Bladex.AddAnmLStep("Jog_2h_Amz",1.000)
	Bladex.AddStopTests("Jog_2h_Amz")

	anm_name="Jog_b_Amz"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_b.BMV","Jog_b_Amz",1)
	Bladex.AddAnmRStep(anm_name,0.475)
	Bladex.AddAnmRRelease(anm_name,0.693)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.190)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)



	### CORRER ATRAS ###

	anm_name="Amz_jogb_b"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jogb_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.330)
	Bladex.AddAnmRRelease(anm_name,0.695)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.525)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_jogb_no"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jogb_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.281)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.563)
	Bladex.AddAnmLRelease(anm_name,0.875)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_jogb_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jogb_spear.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.281)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.563)
	Bladex.AddAnmLRelease(anm_name,0.875)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_jogb_axe"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jogb_axe.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.293)
	Bladex.AddAnmRStep(anm_name,1)
	Bladex.AddAnmLStep(anm_name,0.443)
	Bladex.AddAnmLRelease(anm_name,0.792)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_jogb_2w"
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
	Bladex.LoadSampledAnimation("../../Anm/Amz_snk_no.BMV","Snk_no_Amz",1)
	Bladex.AddAnmRStep("Snk_no_Amz",0.000)
	Bladex.AddAnmRRelease("Snk_no_Amz",0.600)
	Bladex.AddAnmRStep("Snk_no_Amz",1.000)
	Bladex.AddAnmLStep("Snk_no_Amz",0.441)
	Bladex.AddAnmLRelease("Snk_no_Amz",1.000)
	Bladex.AddStopTests("Snk_no_Amz")

	Bladex.LoadSampledAnimation("../../Anm/Amz_snk_1h.BMV","Snk_1h_Amz",1)
	Bladex.AddAnmRStep("Snk_1h_Amz",0.000)
	Bladex.AddAnmRRelease("Snk_1h_Amz",0.173)
	Bladex.AddAnmRStep("Snk_1h_Amz",0.538)
	Bladex.AddAnmLStep("Snk_1h_Amz",0.000)
	Bladex.AddAnmLRelease("Snk_1h_Amz",0.586)
	Bladex.AddAnmLStep("Snk_1h_Amz",1.000)
	Bladex.AddStopTests("Snk_1h_Amz")

	Bladex.LoadSampledAnimation("../../Anm/Amz_snk_2h.BMV","Snk_2h_Amz",1)
	Bladex.AddAnmRStep("Snk_2h_Amz",0.000)
	Bladex.AddAnmRRelease("Snk_2h_Amz",0.173)
	Bladex.AddAnmRStep("Snk_2h_Amz",0.538)
	Bladex.AddAnmLStep("Snk_2h_Amz",0.000)
	Bladex.AddAnmLRelease("Snk_2h_Amz",0.586)
	Bladex.AddAnmLStep("Snk_2h_Amz",1.000)
	Bladex.AddStopTests("Snk_1h_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_snk_2w.BMV","Snk_2w_Amz",1)
	Bladex.AddAnmRStep("Snk_2w_Amz",0.000)
	Bladex.AddAnmRRelease("Snk_2w_Amz",0.173)
	Bladex.AddAnmRStep("Snk_2w_Amz",0.538)
	Bladex.AddAnmLStep("Snk_2w_Amz",0.000)
	Bladex.AddAnmLRelease("Snk_2w_Amz",0.586)
	Bladex.AddAnmLStep("Snk_2w_Amz",1.000)
	Bladex.AddStopTests("Snk_2w_Amz")

	Bladex.LoadSampledAnimation("../../Anm/Amz_snk_spear.BMV","Snk_spear_Amz",1)
	Bladex.AddAnmRStep("Snk_spear_Amz",0.000)
	Bladex.AddAnmRRelease("Snk_spear_Amz",0.173)
	Bladex.AddAnmRStep("Snk_spear_Amz",0.538)
	Bladex.AddAnmLStep("Snk_spear_Amz",0.000)
	Bladex.AddAnmLRelease("Snk_spear_Amz",0.586)
	Bladex.AddAnmLStep("Snk_spear_Amz",1.000)
	Bladex.AddStopTests("Snk_spear_Amz")

	Bladex.LoadSampledAnimation("../../Anm/Amz_snk_axe.BMV","Snk_axe_Amz",1)
	Bladex.AddAnmRStep("Snk_axe_Amz",0.000)
	Bladex.AddAnmRRelease("Snk_axe_Amz",0.173)
	Bladex.AddAnmRStep("Snk_axe_Amz",0.538)
	Bladex.AddAnmLStep("Snk_axe_Amz",0.000)
	Bladex.AddAnmLRelease("Snk_axe_Amz",0.586)
	Bladex.AddAnmLStep("Snk_axe_Amz",1.000)
	Bladex.AddStopTests("Snk_axe_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_snk_b.BMV","Snk_b_Amz",1)
	Bladex.AddAnmRStep("Snk_b_Amz",0.000)
	Bladex.AddAnmRRelease("Snk_b_Amz",0.184)
	Bladex.AddAnmRStep("Snk_b_Amz",0.499)
	Bladex.AddAnmLStep("Snk_b_Amz",0.000)
	Bladex.AddAnmLRelease("Snk_b_Amz",0.613)
	Bladex.AddAnmLStep("Snk_b_Amz",1.000)
	Bladex.AddStopTests("Snk_b_Amz")


	#### WBK ####
	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_1h.BMV","Wbk_1h_Amz",1)
	Bladex.AddAnmRStep("Wbk_1h_Amz",0.000)
	Bladex.AddAnmRRelease("Wbk_1h_Amz",0.552)
	Bladex.AddAnmRStep("Wbk_1h_Amz",1.000)
	Bladex.AddAnmLStep("Wbk_1h_Amz",0.395)
	Bladex.AddAnmLRelease("Wbk_1h_Amz",1.000)
	Bladex.AddStopTests("Wbk_1h_Amz")


	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_2h.BMV","Wbk_2h_Amz",1)
	Bladex.AddAnmRStep("Wbk_2h_Amz",0.000)
	Bladex.AddAnmRRelease("Wbk_2h_Amz",0.552)
	Bladex.AddAnmRStep("Wbk_2h_Amz",1.000)
	Bladex.AddAnmLStep("Wbk_2h_Amz",0.395)
	Bladex.AddAnmLRelease("Wbk_2h_Amz",1.000)
	Bladex.AddStopTests("Wbk_2h_Amz")


	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_no.BMV","Wbk_no_Amz",1)
	Bladex.AddAnmRStep("Wbk_no_Amz",0.000)
	Bladex.AddAnmRRelease("Wbk_no_Amz",0.531)
	Bladex.AddAnmRStep("Wbk_no_Amz",1.000)
	Bladex.AddAnmLStep("Wbk_no_Amz",0.519)
	Bladex.AddAnmLRelease("Wbk_no_Amz",1.000)
	Bladex.AddStopTests("Wbk_no_Amz")


#	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_s.BMV","Wbk_s_Amz",1)
#	Bladex.AddAnmRStep("Wbk_s_Amz",0.000)
#	Bladex.AddAnmRRelease("Wbk_s_Amz",0.575)
#	Bladex.AddAnmRStep("Wbk_s_Amz",1.000)
#	Bladex.AddAnmLStep("Wbk_s_Amz",0.513)
#	Bladex.AddAnmLRelease("Wbk_s_Amz",1.000)
#	Bladex.AddStopTests("Wbk_s_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_b.BMV","Wbk_b_Amz",1)
	Bladex.AddAnmRStep("Wbk_b_Amz",0.373)
	Bladex.AddAnmRRelease("Wbk_b_Amz",1.000)
	Bladex.AddAnmLStep("Wbk_b_Amz",0.000)
	Bladex.AddAnmLRelease("Wbk_b_Amz",0.490)
	Bladex.AddAnmLStep("Wbk_b_Amz",1.000)
	Bladex.AddStopTests("Wbk_b_Amz")


	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_spear.BMV","Wbk_spear_Amz",1)
	Bladex.AddAnmRStep("Wbk_spear_Amz",0.000)
	Bladex.AddAnmRRelease("Wbk_spear_Amz",0.575)
	Bladex.AddAnmRStep("Wbk_spear_Amz",1.000)
	Bladex.AddAnmLStep("Wbk_spear_Amz",0.513)
	Bladex.AddAnmLRelease("Wbk_spear_Amz",1.000)
	Bladex.AddStopTests("Wbk_spear_Amz")

	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_axe.BMV","Wbk_axe_Amz",1)
	Bladex.AddAnmRStep("Wbk_axe_Amz",0.439)
	Bladex.AddAnmRRelease("Wbk_axe_Amz",1.000)
	Bladex.AddAnmLStep("Wbk_axe_Amz",0.000)
	Bladex.AddAnmLRelease("Wbk_axe_Amz",0.511)
	Bladex.AddAnmLStep("Wbk_axe_Amz",1.000)
	Bladex.AddStopTests("Wbk_axe_Amz")




	Bladex.LoadSampledAnimation("../../Anm/Amz_wbk_2w.BMV","Wbk_2w_Amz",1)
	Bladex.AddAnmRStep("Wbk_2w_Amz",0.000)
	Bladex.AddAnmRRelease("Wbk_2w_Amz",0.527)
	Bladex.AddAnmRStep("Wbk_2w_Amz",1.000)
	Bladex.AddAnmLStep("Wbk_2w_Amz",0.433)
	Bladex.AddAnmLRelease("Wbk_2w_Amz",1.000)
	Bladex.AddStopTests("Wbk_2w_Amz")


	#
	#### Caminar ####
	#



	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_no.BMV","Wlk_no_Amz",1)
	Bladex.AddAnmRStep("Wlk_no_Amz",0.000)
	Bladex.AddAnmRRelease("Wlk_no_Amz",0.502)
	Bladex.AddAnmRStep("Wlk_no_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_no_Amz",0.48)
	Bladex.AddAnmLRelease("Wlk_no_Amz",1.000)
	Bladex.AddStopTests("Wlk_no_Amz")


	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_1h.BMV","Wlk_1h_Amz",1)
	Bladex.AddAnmRStep("Wlk_1h_Amz",0.000)
	Bladex.AddAnmRStep("Wlk_1h_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_1h_Amz",0.500)
	Bladex.AddAnmRRelease("Wlk_1h_Amz",0.500)
	Bladex.AddAnmLRelease("Wlk_1h_Amz",1.0)
	Bladex.AddStopTests("Wlk_1h_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_2h.BMV","Wlk_2h_Amz",1)
	Bladex.AddAnmRStep("Wlk_2h_Amz",0.000)
	Bladex.AddAnmRStep("Wlk_2h_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_2h_Amz",0.500)
	Bladex.AddAnmRRelease("Wlk_2h_Amz",0.500)
	Bladex.AddAnmLRelease("Wlk_2h_Amz",1.0)
	Bladex.AddStopTests("Wlk_2h_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_b.BMV","Wlk_b_Amz",1)
	Bladex.AddAnmRStep("Wlk_b_Amz",0.000)
	Bladex.AddAnmRRelease("Wlk_b_Amz",0.627)
	Bladex.AddAnmRStep("Wlk_b_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_b_Amz",0.000)
	Bladex.AddAnmLRelease("Wlk_b_Amz",0.112)
	Bladex.AddAnmLStep("Wlk_b_Amz",0.502)
	Bladex.AddStopTests("Wlk_b_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_2w.BMV","Wlk_2w_Amz",1)
	Bladex.AddAnmRStep("Wlk_2w_Amz",0.000)
	Bladex.AddAnmRRelease("Wlk_2w_Amz",0.540)
	Bladex.AddAnmRStep("Wlk_2w_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_2w_Amz",0.484)
	Bladex.AddAnmLRelease("Wlk_2w_Amz",1.000)
	Bladex.AddStopTests("Wlk_2w_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_spear.BMV","Wlk_spear_Amz",1)
	Bladex.AddAnmRStep("Wlk_spear_Amz",0.000)
	Bladex.AddAnmRRelease("Wlk_spear_Amz",0.540)
	Bladex.AddAnmRStep("Wlk_spear_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_spear_Amz",0.484)
	Bladex.AddAnmLRelease("Wlk_spear_Amz",1.000)
	Bladex.AddStopTests("Wlk_spear_Amz")


	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_axe.BMV","Wlk_axe_Amz",1)
	Bladex.AddAnmRStep("Wlk_axe_Amz",0.000)
	Bladex.AddAnmRRelease("Wlk_axe_Amz",0.540)
	Bladex.AddAnmRStep("Wlk_axe_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_axe_Amz",0.484)
	Bladex.AddAnmLRelease("Wlk_axe_Amz",1.000)
	Bladex.AddStopTests("Wlk_axe_Amz")



	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_s.BMV","Wlk_s_Amz",1)
	Bladex.AddAnmRStep("Wlk_s_Amz",0.000)
	Bladex.AddAnmRStep("Wlk_s_Amz",1.000)
	Bladex.AddAnmLStep("Wlk_s_Amz",0.500)
	Bladex.AddAnmRRelease("Wlk_s_Amz",0.500)
	Bladex.AddAnmLRelease("Wlk_s_Amz",1.0)
	Bladex.AddStopTests("Wlk_s_Amz")






	#### Caidas ####

	Bladex.LoadSampledAnimation("../../Anm/Amz_fll_low.BMV","FallLow_Amz",0)
	Bladex.AddAnmRStep("FallLow_Amz",0.0)
	Bladex.AddAnmLStep("FallLow_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Amz_fll_medlow.BMV","FallMed_Amz",0)
	Bladex.AddAnmRStep("FallMed_Amz",0.0)
	Bladex.AddAnmLStep("FallMed_Amz",0.0)

	Bladex.LoadSampledAnimation("../../Anm/Amz_fll_med.BMV","FallHigh_Amz",0)
	Bladex.AddAnmRStep("FallHigh_Amz",0.0)
	Bladex.AddAnmLStep("FallHigh_Amz",0.0)

	#Caida enorme
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll.BMV","Dth_Fll_Amz",0,"Amazon_L")
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_fll2.BMV","Dth_Fll2_Amz",0,"Amazon_L")
	Bladex.AddAnmRStep("Dth_Fll2_Amz",0.0)
	Bladex.AddAnmLStep("Dth_Fll2_Amz",0.0)

	#
	# Ataques
	#


	anm_name="Amz_g_magic"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_magic.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.105)
	Bladex.AddAnmRRelease(anm_name,0.558)
	Bladex.AddAnmRStep(anm_name,0.762)
	Bladex.AddAnmRRelease(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.465)
	Bladex.AddAnmLStep(anm_name,0.545)
	Bladex.AddAnmEvent("Amz_g_magic","LaunchTrail",0.593)

	anm_name="Amz_g_magic2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_magic2.BMV",anm_name,0)
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
	Bladex.AddAnmEvent("Amz_g_magic2","LaunchTrail",0.377)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_08.BMV","Amz_g_08",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_08",0)
	Bladex.AddAnmLStep("Amz_g_08",0)
	Bladex.AddAnmRRelease("Amz_g_08",0.29)
	Bladex.AddAnmRStep("Amz_g_08",0.49)
	Bladex.AddAnmRRelease("Amz_g_08",0.72)
	Bladex.AddAnmRStep("Amz_g_08",0.89)


	anm_name="Amz_g_back"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_back.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.477)
	Bladex.AddAnmRStep(anm_name,0.767)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.305)
	Bladex.AddAnmLRelease(anm_name,0.829)
	Bladex.AddAnmLStep(anm_name,1.000)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_01.BMV","Amz_g_01",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_01",0)
	Bladex.AddAnmLStep("Amz_g_01",0)
	Bladex.AddAnmRRelease("Amz_g_01",0.21)
	Bladex.AddAnmRStep("Amz_g_01",0.36)
	Bladex.AddAnmRRelease("Amz_g_01",0.64)
	Bladex.AddAnmRStep("Amz_g_01",0.83)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_02.BMV","Amz_g_02",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_02",0)
	Bladex.AddAnmLStep("Amz_g_02",0)
	Bladex.AddAnmRRelease("Amz_g_02",0.15)
	Bladex.AddAnmRStep("Amz_g_02",0.27)
	Bladex.AddAnmRRelease("Amz_g_02",0.55)
	Bladex.AddAnmRStep("Amz_g_02",0.74)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_05.BMV","Amz_g_05",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_05",0)
	Bladex.AddAnmLStep("Amz_g_05",0)
	Bladex.AddAnmRRelease("Amz_g_05",0.28)
	Bladex.AddAnmRStep("Amz_g_05",0.5)
	Bladex.AddAnmRRelease("Amz_g_05",0.72)
	Bladex.AddAnmRStep("Amz_g_05",0.9)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_06.BMV","Amz_g_06",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_06",0)
	Bladex.AddAnmLStep("Amz_g_06",0)
	Bladex.AddAnmRRelease("Amz_g_06",0.19)
	Bladex.AddAnmRStep("Amz_g_06",0.37)
	Bladex.AddAnmRRelease("Amz_g_06",0.67)
	Bladex.AddAnmRStep("Amz_g_06",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_07.BMV","Amz_g_07",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_07",0)
	Bladex.AddAnmLStep("Amz_g_07",0)
	Bladex.AddAnmRRelease("Amz_g_07",0.15)
	Bladex.AddAnmRStep("Amz_g_07",0.35)
	Bladex.AddAnmRRelease("Amz_g_07",0.51)
	Bladex.AddAnmRStep("Amz_g_07",0.72)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_09.BMV","Amz_g_09",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_09",0)
	Bladex.AddAnmLStep("Amz_g_09",0)
	Bladex.AddAnmRRelease("Amz_g_09",0.23)
	Bladex.AddAnmRStep("Amz_g_09",0.36)
	Bladex.AddAnmRRelease("Amz_g_09",0.55)
	Bladex.AddAnmRStep("Amz_g_09",0.71)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_13.BMV","Amz_g_13",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_13",0)
	Bladex.AddAnmLStep("Amz_g_13",0)
	Bladex.AddAnmRRelease("Amz_g_13",0.41)
	Bladex.AddAnmRStep("Amz_g_13",0.57)
	Bladex.AddAnmLRelease("Amz_g_13",0.76)
	Bladex.AddAnmLStep("Amz_g_13",0.89)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_18.BMV","Amz_g_18",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_18",0)
	Bladex.AddAnmLStep("Amz_g_18",0)
	Bladex.AddAnmRRelease("Amz_g_18",0.37)
	Bladex.AddAnmRStep("Amz_g_18",0.50)
	Bladex.AddAnmLRelease("Amz_g_18",0.77)
	Bladex.AddAnmLStep("Amz_g_18",0.90)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_14.BMV","Amz_g_14",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_14",0)
	Bladex.AddAnmLStep("Amz_g_14",0)
	Bladex.AddAnmLRelease("Amz_g_14",0.15)
	Bladex.AddAnmLStep("Amz_g_14",0.37)
	Bladex.AddAnmRRelease("Amz_g_14",0.43)
	Bladex.AddAnmRStep("Amz_g_14",0.56)
	Bladex.AddAnmLRelease("Amz_g_14",0.73)
	Bladex.AddAnmLStep("Amz_g_14",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_11.BMV","Amz_g_11",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_11",0)
	Bladex.AddAnmLStep("Amz_g_11",0)
	Bladex.AddAnmRRelease("Amz_g_11",0.4)
	Bladex.AddAnmRStep("Amz_g_11",0.55)
	Bladex.AddAnmLRelease("Amz_g_11",0.78)
	Bladex.AddAnmLStep("Amz_g_11",0.93)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_16.BMV","Amz_g_16",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_16",0)
	Bladex.AddAnmLStep("Amz_g_16",0)
	Bladex.AddAnmRRelease("Amz_g_16",0.16)
	Bladex.AddAnmRStep("Amz_g_16",0.275)
	Bladex.AddAnmLRelease("Amz_g_16",0.54)
	Bladex.AddAnmLStep("Amz_g_16",0.675)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_12.BMV","Amz_g_12",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_12",0)
	Bladex.AddAnmLStep("Amz_g_12",0)
	Bladex.AddAnmRRelease("Amz_g_12",0.4)
	Bladex.AddAnmRStep("Amz_g_12",0.52)
	Bladex.AddAnmLRelease("Amz_g_12",0.71)
	Bladex.AddAnmLStep("Amz_g_12",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_17.BMV","Amz_g_17",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_17",0)
	Bladex.AddAnmLStep("Amz_g_17",0)
	Bladex.AddAnmRRelease("Amz_g_17",0.16)
	Bladex.AddAnmRStep("Amz_g_17",0.27)
	Bladex.AddAnmLRelease("Amz_g_17",0.53)
	Bladex.AddAnmLStep("Amz_g_17",0.65)



	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_15.BMV","Amz_g_15",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_15",0)
	Bladex.AddAnmLStep("Amz_g_15",0)
	Bladex.AddAnmRRelease("Amz_g_15",0.17)
	Bladex.AddAnmRStep("Amz_g_15",0.35)
	Bladex.AddAnmLRelease("Amz_g_15",0.56)
	Bladex.AddAnmLStep("Amz_g_15",0.76)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_21.BMV","Amz_g_21",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_21",0)
	Bladex.AddAnmLStep("Amz_g_21",0)
	Bladex.AddAnmRRelease("Amz_g_21",0.51)
	Bladex.AddAnmRStep("Amz_g_21",0.669)
	Bladex.AddAnmLRelease("Amz_g_21",0.696)
	Bladex.AddAnmLStep("Amz_g_21",0.834)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_22.BMV","Amz_g_22",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_22",0)
	Bladex.AddAnmLStep("Amz_g_22",0)
	Bladex.AddAnmRRelease("Amz_g_22",0.474)
	Bladex.AddAnmRStep("Amz_g_22",0.544)
	Bladex.AddAnmRRelease("Amz_g_22",0.605)
	Bladex.AddAnmRStep("Amz_g_22",0.67)
	Bladex.AddAnmRRelease("Amz_g_22",0.781)
	Bladex.AddAnmRStep("Amz_g_22",0.847)
	Bladex.AddAnmLRelease("Amz_g_22",0.2)
	Bladex.AddAnmLStep("Amz_g_22",0.433)
	Bladex.AddAnmLRelease("Amz_g_22",0.549)
	Bladex.AddAnmLStep("Amz_g_22",0.6)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_23.BMV","Amz_g_23",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_23",0)
	Bladex.AddAnmLStep("Amz_g_23",0)
	Bladex.AddAnmRRelease("Amz_g_23",0.529)
	Bladex.AddAnmRStep("Amz_g_23",0.743)
	Bladex.AddAnmLRelease("Amz_g_23",0.75)
	Bladex.AddAnmLStep("Amz_g_23",0.85)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_26.BMV","Amz_g_26",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_26",0)
	Bladex.AddAnmLStep("Amz_g_26",0)
	Bladex.AddAnmRRelease("Amz_g_26",0.135)
	Bladex.AddAnmRStep("Amz_g_26",0.236)
	Bladex.AddAnmLRelease("Amz_g_26",0.48)
	Bladex.AddAnmLStep("Amz_g_26",0.682)
	Bladex.AddAnmLRelease("Amz_g_26",0.79)
	Bladex.AddAnmLStep("Amz_g_26",0.885)


	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_27.BMV","Amz_g_27",0,"Amazon_L")
	Bladex.AddAnmRStep("Amz_g_27",0)
	Bladex.AddAnmLStep("Amz_g_27",0)
	Bladex.AddAnmRRelease("Amz_g_27",0.28)
	Bladex.AddAnmRStep("Amz_g_27",0.5)
	Bladex.AddAnmLRelease("Amz_g_27",0.72)
	Bladex.AddAnmLStep("Amz_g_27",0.74)


	anm_name="Amz_g_31"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_31.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_g_3s9_6new"
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


	anm_name="Amz_g_12_7_s1new"
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


	anm_name="Amz_g_28new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_28new.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.144)
	Bladex.AddAnmRStep(anm_name,0.419)
	Bladex.AddAnmLStep(anm_name,0.090)
	Bladex.AddAnmLRelease(anm_name,0.647)
	Bladex.AddAnmLStep(anm_name,0.888)
	Bladex.AddAnmLRelease(anm_name,1.000)


	anm_name="Amz_g_27kata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_27kata_new.BMV",anm_name,0,"Amazon_N")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.155)
	Bladex.AddAnmRStep(anm_name,0.524)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.534)
	Bladex.AddAnmLStep(anm_name,0.951)






####
#  Golpes lanza a dos manos
####

	anm_name="Amz_g_spear19"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear19.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.313)
	Bladex.AddAnmRStep(anm_name,0.790)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.017)
	Bladex.AddAnmLStep(anm_name,0.360)
	Bladex.AddAnmEvent("Amz_g_spear19","W2hToLeft",0.03)
	Bladex.AddAnmEvent("Amz_g_spear19","W2hToRight",0.93)


	anm_name="Amz_g_spear_b29"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_b29.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.138)
	Bladex.AddAnmRStep(anm_name,0.322)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.644)
	Bladex.AddAnmLStep(anm_name,0.874)



	anm_name="Amz_g_spear_2katab6low"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_2katab6low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.274)
	Bladex.AddAnmRStep(anm_name,0.448)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.214)
	Bladex.AddAnmLStep(anm_name,0.285)
	Bladex.AddAnmLRelease(anm_name,0.695)
	Bladex.AddAnmLStep(anm_name,0.875)


	anm_name="Amz_g_spear02"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear02.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.119)
	Bladex.AddAnmRStep(anm_name,0.296)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.838)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Amz_g_spear02","W2hToLeft",0.15)
	Bladex.AddAnmEvent("Amz_g_spear02","W2hToRight",0.93)


	anm_name="Amz_g_spear02low"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear02low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.104)
	Bladex.AddAnmRStep(anm_name,0.293)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.841)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Amz_g_spear02low","W2hToLeft",0.227)
	Bladex.AddAnmEvent("Amz_g_spear02low","W2hToRight",0.93)


	anm_name="Amz_g_spear08"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear08.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.129)
	Bladex.AddAnmRStep(anm_name,0.373)
	Bladex.AddAnmRRelease(anm_name,0.560)
	Bladex.AddAnmRStep(anm_name,0.829)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmEvent("Amz_g_spear08","W2hToLeft",0.2)
	Bladex.AddAnmEvent("Amz_g_spear08","W2hToRight",0.93)


	anm_name="Amz_g_spear09"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear09.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.444)
	Bladex.AddAnmLStep(anm_name,0.518)
	Bladex.AddAnmLRelease(anm_name,0.765)
	Bladex.AddAnmLStep(anm_name,0.869)
	Bladex.AddAnmEvent("Amz_g_spear09","W2hToLeft",0.11)
	Bladex.AddAnmEvent("Amz_g_spear09","W2hToRight",0.93)


	anm_name="Amz_g_spear12"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear12.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.269)
	Bladex.AddAnmRStep(anm_name,0.671)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.159)
	Bladex.AddAnmLStep(anm_name,0.359)
	Bladex.AddAnmEvent("Amz_g_spear12","W2hToLeft",0.212)
	Bladex.AddAnmEvent("Amz_g_spear12","W2hToRight",0.93)


	anm_name="Amz_g_spear16low"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear16low.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.398)
	Bladex.AddAnmRStep(anm_name,0.491)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.320)
	Bladex.AddAnmLStep(anm_name,0.410)
	Bladex.AddAnmLRelease(anm_name,0.814)
	Bladex.AddAnmLStep(anm_name,0.884)


	anm_name="Amz_g_spear22"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear22.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.223)
	Bladex.AddAnmRStep(anm_name,0.388)
	Bladex.AddAnmRRelease(anm_name,0.812)
	Bladex.AddAnmRStep(anm_name,0.937)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.546)
	Bladex.AddAnmLStep(anm_name,0.783)

	anm_name="Amz_g_spear26kata"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear26kata.BMV",anm_name,0)
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


	anm_name="Amz_g_spear2katab2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear2katab2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.250)
	Bladex.AddAnmRStep(anm_name,0.413)
	Bladex.AddAnmRRelease(anm_name,0.496)
	Bladex.AddAnmRStep(anm_name,0.684)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.496)
	Bladex.AddAnmLStep(anm_name,0.635)
	Bladex.AddAnmLRelease(anm_name,0.684)
	Bladex.AddAnmLStep(anm_name,0.738)


	anm_name="Amz_g_spear32kata_b2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear32kata_b2.BMV",anm_name,0)
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


	anm_name="Amz_g_spear3s2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear3s2.BMV",anm_name,0)
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

	anm_name="Amz_g_spearb2kata"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spearb2kata.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.133)
	Bladex.AddAnmRStep(anm_name,0.266)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.352)
	Bladex.AddAnmLStep(anm_name,0.540)


	anm_name="Amz_g_spears1"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spears1.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.259)
	Bladex.AddAnmRStep(anm_name,0.401)
	Bladex.AddAnmRRelease(anm_name,0.644)
	Bladex.AddAnmRStep(anm_name,0.757)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.187)
	Bladex.AddAnmLStep(anm_name,0.374)
	Bladex.AddAnmEvent("Amz_g_spears1","W2hToLeft",0.258)
	Bladex.AddAnmEvent("Amz_g_spears1","W2hToRight",0.93)


	anm_name="Amz_g_spears6"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spears6.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.149)
	Bladex.AddAnmRStep(anm_name,0.289)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.195)
	Bladex.AddAnmLStep(anm_name,0.305)
	Bladex.AddAnmLRelease(anm_name,0.780)
	Bladex.AddAnmLStep(anm_name,0.900)
	Bladex.AddAnmEvent("Amz_g_spears6","W2hToLeft",0.11)
	Bladex.AddAnmEvent("Amz_g_spears6","W2hToRight",0.93)


	anm_name="Amz_g_spears8"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spears8.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.274)
	Bladex.AddAnmRStep(anm_name,0.466)
	Bladex.AddAnmRRelease(anm_name,0.680)
	Bladex.AddAnmRStep(anm_name,0.822)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.275)
	Bladex.AddAnmLStep(anm_name,0.473)
	Bladex.AddAnmLRelease(anm_name,0.628)
	Bladex.AddAnmLStep(anm_name,0.828)
	Bladex.AddAnmEvent("Amz_g_spears8","W2hToLeft",0.272)
	Bladex.AddAnmEvent("Amz_g_spears8","W2hToRight",0.93)


	anm_name="Amz_g_spear_back"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_back.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.363)
	Bladex.AddAnmLStep(anm_name,0.695)


	anm_name="Amz_g_spear_sb11"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_sb11.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.123)
	Bladex.AddAnmRStep(anm_name,0.245)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.458)
	Bladex.AddAnmRRelease(anm_name,0.507)
	Bladex.AddAnmRStep(anm_name,0.637)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.221)
	Bladex.AddAnmLStep(anm_name,0.401)
	Bladex.AddAnmLRelease(anm_name,0.448)
	Bladex.AddAnmLStep(anm_name,0.617)
	Bladex.AddAnmLRelease(anm_name,0.839)
	Bladex.AddAnmLStep(anm_name,0.948)
	Bladex.AddAnmEvent("Amz_g_spear_sb11","W2hToLeft",0.12)
	Bladex.AddAnmEvent("Amz_g_spear_sb11","W2hToRight",0.99)


	anm_name="Amz_g_spear17"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear17.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.41)
	Bladex.AddAnmRStep(anm_name,0.57)
	Bladex.AddAnmLRelease(anm_name,0.76)
	Bladex.AddAnmLStep(anm_name,0.89)


	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear16.BMV","Amz_g_spear16",0)
	Bladex.AddAnmRStep("Amz_g_spear16",0)
	Bladex.AddAnmLStep("Amz_g_spear16",0)
	Bladex.AddAnmRRelease("Amz_g_spear16",0.16)
	Bladex.AddAnmRStep("Amz_g_spear16",0.275)
	Bladex.AddAnmLRelease("Amz_g_spear16",0.54)
	Bladex.AddAnmLStep("Amz_g_spear16",0.675)


	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_b6_26.BMV","Amz_g_spear_b6_26",0)
	Bladex.AddAnmRStep("Amz_g_spear_b6_26",0)
	Bladex.AddAnmLStep("Amz_g_spear_b6_26",0)
	Bladex.AddAnmRRelease("Amz_g_spear_b6_26",0.474)
	Bladex.AddAnmRStep("Amz_g_spear_b6_26",0.544)
	Bladex.AddAnmRRelease("Amz_g_spear_b6_26",0.605)
	Bladex.AddAnmRStep("Amz_g_spear_b6_26",0.67)
	Bladex.AddAnmRRelease("Amz_g_spear_b6_26",0.781)
	Bladex.AddAnmRStep("Amz_g_spear_b6_26",0.847)
	Bladex.AddAnmLRelease("Amz_g_spear_b6_26",0.2)
	Bladex.AddAnmLStep("Amz_g_spear_b6_26",0.433)
	Bladex.AddAnmLRelease("Amz_g_spear_b6_26",0.549)
	Bladex.AddAnmLStep("Amz_g_spear_b6_26",0.6)


	anm_name="Amz_g_spear19_13"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear19_13.BMV",anm_name,0)
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


	anm_name="Amz_g_spear_b06"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_b06.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.155)
	Bladex.AddAnmRStep(anm_name,0.524)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.534)
	Bladex.AddAnmLStep(anm_name,0.951)


	anm_name="Amz_g_spear_bs21"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_bs21.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.141)
	Bladex.AddAnmRStep(anm_name,0.400)
	Bladex.AddAnmRRelease(anm_name,0.446)
	Bladex.AddAnmRStep(anm_name,0.564)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.073)
	Bladex.AddAnmLStep(anm_name,0.145)
	Bladex.AddAnmLRelease(anm_name,0.261)
	Bladex.AddAnmLStep(anm_name,0.434)
	Bladex.AddAnmLRelease(anm_name,0.726)
	Bladex.AddAnmLStep(anm_name,0.857)


	anm_name="Amz_g_spear111"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear111.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.239)
	Bladex.AddAnmRStep(anm_name,0.812)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.066)
	Bladex.AddAnmLStep(anm_name,0.272)


	anm_name="Amz_g_spear_21"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_21.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.222)
	Bladex.AddAnmRStep(anm_name,0.392)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.236)
	Bladex.AddAnmLStep(anm_name,0.346)
	Bladex.AddAnmLRelease(anm_name,0.603)
	Bladex.AddAnmLStep(anm_name,0.776)
	Bladex.AddAnmEvent("Amz_g_spear_21","W2hToLeft",0.2)
	Bladex.AddAnmEvent("Amz_g_spear_21","W2hToRight",0.93)


	anm_name="Amz_g_spear13"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear13.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.172)
	Bladex.AddAnmRStep(anm_name,0.266)
	Bladex.AddAnmRRelease(anm_name,0.359)
	Bladex.AddAnmRStep(anm_name,0.641)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.172)
	Bladex.AddAnmLStep(anm_name,0.297)
	Bladex.AddAnmEvent("Amz_g_spear13","W2hToLeft",0.2)
	Bladex.AddAnmEvent("Amz_g_spear13","W2hToRight",0.93)


	anm_name="Amz_g_spear_kata23"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear_kata23.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.122)
	Bladex.AddAnmRStep(anm_name,0.518)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.488)
	Bladex.AddAnmLStep(anm_name,0.865)

	anm_name="Amz_g_spear33"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear33.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.216)
	Bladex.AddAnmRStep(anm_name,0.313)
	Bladex.AddAnmRRelease(anm_name,0.463)
	Bladex.AddAnmRStep(anm_name,0.752)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.244)
	Bladex.AddAnmLStep(anm_name,0.375)
	Bladex.AddAnmEvent("Amz_g_spear33","W2hToLeft",0.11)
	Bladex.AddAnmEvent("Amz_g_spear33","W2hToRight",0.93)


	anm_name="Amz_g_spear19_bs1"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_spear19_bs1.BMV",anm_name,0)
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












	anm_name="Amz_g_06lowkata_new"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_06lowkata_new.BMV",anm_name,0,"Amazon_N")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.041)
	Bladex.AddAnmRStep(anm_name,0.453)
	Bladex.AddAnmRRelease(anm_name,0.692)
	Bladex.AddAnmRStep(anm_name,0.865)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.384)
	Bladex.AddAnmLStep(anm_name,0.680)




######### GOLPES SIN ARMAS ##############


	anm_name="Amz_g_kick1"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_kick1.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.160)
	Bladex.AddAnmRStep(anm_name,0.508)
	Bladex.AddAnmRRelease(anm_name,0.676)
	Bladex.AddAnmRStep(anm_name,0.872)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.093)
	Bladex.AddAnmLStep(anm_name,0.148)

#	anm_name="Amz_g_kick1"
#	Bladex.LoadSampledAnimation("../../Anm/Amz_g_kick1.BMV",anm_name,0)
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmRRelease(anm_name,0.128)
#	Bladex.AddAnmRStep(anm_name,1.000)
#	Bladex.AddAnmLStep(anm_name,0.531)
#	Bladex.SetAnimationFactor("Amz_g_kick1",3.0)


	anm_name="Amz_g_kick2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_kick2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.233)
	Bladex.AddAnmRStep(anm_name,0.970)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Amz_g_kick4"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_kick4.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.132)
	Bladex.AddAnmRRelease(anm_name,0.198)
	Bladex.AddAnmRStep(anm_name,0.582)
	Bladex.AddAnmRStep(anm_name,0.582)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.066)
	Bladex.AddAnmLStep(anm_name,0.462)
	Bladex.AddAnmLRelease(anm_name,0.725)
	Bladex.AddAnmLStep(anm_name,0.967)

	anm_name="Amz_g_kick5"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_kick5.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.048)
	Bladex.AddAnmRStep(anm_name,0.390)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.162)
	Bladex.AddAnmLStep(anm_name,0.968)

	anm_name="Amz_g_punch2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_punch2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.100)
	Bladex.AddAnmRStep(anm_name,0.448)
	Bladex.AddAnmRRelease(anm_name,0.790)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Amz_g_punch1"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_punch1.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.105)
	Bladex.AddAnmRStep(anm_name,0.368)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.132)
	Bladex.AddAnmLStep(anm_name,0.289)
	Bladex.AddAnmLRelease(anm_name,0.421)
	Bladex.AddAnmLStep(anm_name,0.947)



#	Ataques Torpes


	anm_name="Amz_g_bad_axe"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_bad_axe.BMV",anm_name,0)
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

	anm_name="Amz_g_bad_no"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_no.BMV",anm_name,0,"Amazon_N")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)

	anm_name="Amz_g_bad_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_bad_1h.BMV",anm_name,0,"Amazon_N")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.306)
	Bladex.AddAnmRStep(anm_name,0.433)
	Bladex.AddAnmRRelease(anm_name,0.624)
	Bladex.AddAnmRStep(anm_name,0.760)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.438)
	Bladex.AddAnmLStep(anm_name,0.554)


	anm_name="Amz_g_bad_sword"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_bad_sword.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.341)
	Bladex.AddAnmRStep(anm_name,0.440)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.481)
	Bladex.AddAnmLStep(anm_name,0.575)


	anm_name="Amz_g_bad_sword2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_bad_sword2.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.777)
	Bladex.AddAnmRStep(anm_name,0.872)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Amz_g_bad_sword3"
	Bladex.LoadSampledAnimation("../../Anm/Amz_g_bad_sword3.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.133)
	Bladex.AddAnmRStep(anm_name,0.550)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.322)
	Bladex.AddAnmLStep(anm_name,0.548)
	Bladex.AddAnmEvent("Amz_g_bad_sword3","W2hToLeft",0.15)
	Bladex.AddAnmEvent("Amz_g_bad_sword3","W2hToRight",0.98)






	anm_name="Amz_g_draw_rlx"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_draw_rlx.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.817)
	Bladex.AddAnmLStep(anm_name,0.383)


	anm_name="Amz_g_draw_run"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_g_draw_run.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.042)
	Bladex.AddAnmLStep(anm_name,0.319)






	#
	# Movimientos en combate
	#
	anm_name="Amz_attack_l"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_l.BMV",anm_name,1)
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
	Bladex.AddAnmLStep(anm_name,0.597)
	Bladex.AddAnmLRelease(anm_name,0.815)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_attack_r_no"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_r_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.174)
	Bladex.AddAnmRStep(anm_name,0.348)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,0.652)
	Bladex.AddAnmRRelease(anm_name,0.782)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.011)
	Bladex.AddAnmLStep(anm_name,0.215)
	Bladex.AddAnmLRelease(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.586)
	Bladex.AddAnmLRelease(anm_name,0.717)
	Bladex.AddAnmLStep(anm_name,0.891)

	Bladex.AddStopTests(anm_name)


	anm_name="Amz_attack_l_no"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_l_no.BMV",anm_name,1)
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
	Bladex.AddAnmLStep(anm_name,0.597)
	Bladex.AddAnmLRelease(anm_name,0.815)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_attack_r"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_r.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.174)
	Bladex.AddAnmRStep(anm_name,0.348)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,0.652)
	Bladex.AddAnmRRelease(anm_name,0.782)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.011)
	Bladex.AddAnmLStep(anm_name,0.215)
	Bladex.AddAnmLRelease(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.586)
	Bladex.AddAnmLRelease(anm_name,0.717)
	Bladex.AddAnmLStep(anm_name,0.891)

	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_f"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_f.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.353)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.441)
	Bladex.AddAnmLRelease(anm_name,0.794)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_f_no"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_f_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.353)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.441)
	Bladex.AddAnmLRelease(anm_name,0.794)
	Bladex.AddStopTests(anm_name)
#	anm_name="Amz_attack_b"
#	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_b.BMV",anm_name,1)
#	Bladex.AddAnmRStep(anm_name,0.286)
#	Bladex.AddAnmRRelease(anm_name,0.643)
#	Bladex.AddAnmLStep(anm_name,0.000)
#	Bladex.AddAnmLRelease(anm_name,0.393)
#	Bladex.AddAnmLStep(anm_name,1.000)
#	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_b"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_b.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.167)
	Bladex.AddAnmRStep(anm_name,0.500)
	Bladex.AddAnmRRelease(anm_name,0.667)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.106)
	Bladex.AddAnmLStep(anm_name,0.333)
	Bladex.AddAnmLRelease(anm_name,0.561)
	Bladex.AddAnmLStep(anm_name,0.864)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_b_no"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_b_no.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.286)
	Bladex.AddAnmRRelease(anm_name,0.643)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.393)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_d_b"
	Bladex.LoadSampledAnimation("../../Anm/Amz_d_b.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.235)
	Bladex.AddAnmRStep(anm_name,0.797)
	Bladex.AddAnmRRelease(anm_name,0.866)
	Bladex.AddAnmRStep(anm_name,0.962)
	Bladex.AddAnmLStep(anm_name,0.254)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmLStep(anm_name,0.606)



	anm_name="Amz_d_r"
	Bladex.LoadSampledAnimation("../../Anm/Amz_d_r.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.474)
	Bladex.AddAnmRRelease(anm_name,0.628)
	Bladex.AddAnmRStep(anm_name,0.919)
	Bladex.AddAnmRRelease(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.147)
	Bladex.AddAnmLStep(anm_name,0.511)
	Bladex.AddAnmLRelease(anm_name,0.793)
	Bladex.AddAnmLStep(anm_name,0.924)


	anm_name="Amz_d_l"
	Bladex.LoadSampledAnimation("../../Anm/Amz_d_l.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.244)
	Bladex.AddAnmRStep(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.249)
	Bladex.AddAnmLRelease(anm_name,0.350)
	Bladex.AddAnmLStep(anm_name,0.593)
	Bladex.AddAnmLRelease(anm_name,0.876)
	Bladex.AddAnmLStep(anm_name,0.965)


	anm_name="Amz_attack_l_s"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_l_s.BMV",anm_name,1)
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
	Bladex.AddAnmLStep(anm_name,0.597)
	Bladex.AddAnmLRelease(anm_name,0.815)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_r_s"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_r_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.174)
	Bladex.AddAnmRStep(anm_name,0.348)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,0.652)
	Bladex.AddAnmRRelease(anm_name,0.782)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.011)
	Bladex.AddAnmLStep(anm_name,0.215)
	Bladex.AddAnmLRelease(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.586)
	Bladex.AddAnmLRelease(anm_name,0.717)
	Bladex.AddAnmLStep(anm_name,0.891)

	Bladex.AddStopTests(anm_name)



	anm_name="Amz_attack_f_s"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_f_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.353)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.441)
	Bladex.AddAnmLRelease(anm_name,0.794)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_b_s"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_b_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.286)
	Bladex.AddAnmRRelease(anm_name,0.643)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.393)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_rlx_f"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_rlx.BMV",anm_name,1,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)



	anm_name="Amz_rlx_f_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_rlx_2w.BMV",anm_name,1,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Amz_rlx_f_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_rlx_spear.BMV",anm_name,1,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)


#	anm_name="Amz_rlx_s"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_s.BMV",anm_name,1,"Amazon_L")
#	Bladex.AddAnmRStep(anm_name,0)
#	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Amz_attack_rlx_s"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_rlx_s.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




#########Encaramiento con espada 2manos############

	anm_name="Amz_attack_l_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_l_2w.BMV",anm_name,1)
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
	Bladex.AddAnmLStep(anm_name,0.597)
	Bladex.AddAnmLRelease(anm_name,0.815)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_attack_r_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_r_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.174)
	Bladex.AddAnmRStep(anm_name,0.348)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,0.652)
	Bladex.AddAnmRRelease(anm_name,0.782)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.011)
	Bladex.AddAnmLStep(anm_name,0.215)
	Bladex.AddAnmLRelease(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.586)
	Bladex.AddAnmLRelease(anm_name,0.717)
	Bladex.AddAnmLStep(anm_name,0.891)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_f_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_f_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.353)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.441)
	Bladex.AddAnmLRelease(anm_name,0.794)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_b_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_b_2w.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.286)
	Bladex.AddAnmRRelease(anm_name,0.643)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.393)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)


#########Encaramiento con lanza############

	anm_name="Amz_attack_l_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_l_spear.BMV",anm_name,1)
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
	Bladex.AddAnmLStep(anm_name,0.597)
	Bladex.AddAnmLRelease(anm_name,0.815)
	Bladex.AddAnmLStep(anm_name,1)
	Bladex.AddStopTests(anm_name)


	anm_name="Amz_attack_r_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_r_spear.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.174)
	Bladex.AddAnmRStep(anm_name,0.348)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,0.652)
	Bladex.AddAnmRRelease(anm_name,0.782)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.011)
	Bladex.AddAnmLStep(anm_name,0.215)
	Bladex.AddAnmLRelease(anm_name,0.333)
	Bladex.AddAnmLStep(anm_name,0.586)
	Bladex.AddAnmLRelease(anm_name,0.717)
	Bladex.AddAnmLStep(anm_name,0.891)
	Bladex.AddStopTests(anm_name)

	anm_name="Amz_attack_f_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_f_spear.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.353)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.441)
	Bladex.AddAnmLRelease(anm_name,0.794)
	Bladex.AddStopTests(anm_name)
	anm_name="Amz_attack_b_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_attack_b_spear.BMV",anm_name,1)
	Bladex.AddAnmRStep(anm_name,0.286)
	Bladex.AddAnmRRelease(anm_name,0.643)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.393)
	Bladex.AddAnmLStep(anm_name,1.000)
	Bladex.AddStopTests(anm_name)





	#
	# Saltos
	#
	anm_name="Amz_jmp_no"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_jmp_no.BMV",anm_name,0,"Amazon_L")
	"""
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.10)
	"""
	Bladex.AddAnmRStep(anm_name,0.3)
	Bladex.AddAnmLStep(anm_name,0.3)
	#Bladex.AddAnmRStep(anm_name,0.33)
	#Bladex.AddAnmLStep(anm_name,0.34)
	Bladex.AddAnmRRelease(anm_name,0.37)
	Bladex.AddAnmLRelease(anm_name,0.45)
	Bladex.AddAnmRStep(anm_name,0.49)
	Bladex.AddAnmRRelease(anm_name,0.62)
	Bladex.AddAnmRStep(anm_name,0.70)
	Bladex.AddAnmLStep(anm_name,0.70)


	anm_name="Amz_jmp_1h"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jmp_1h.BMV",anm_name,0)
	"""
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.10)
	"""
	Bladex.AddAnmRStep(anm_name,0.3)
	Bladex.AddAnmLStep(anm_name,0.3)
	#Bladex.AddAnmRStep(anm_name,0.33)
	#Bladex.AddAnmLStep(anm_name,0.34)
	Bladex.AddAnmRRelease(anm_name,0.37)
	Bladex.AddAnmLRelease(anm_name,0.45)
	Bladex.AddAnmRStep(anm_name,0.49)
	Bladex.AddAnmRRelease(anm_name,0.62)
	Bladex.AddAnmRStep(anm_name,0.70)
	Bladex.AddAnmLStep(anm_name,0.70)
	#eventos de pasos = kgt_jmp_1h


	anm_name="Amz_jmph0_no"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_jmph0_no.BMV",anm_name,0,"Amazon_L")

	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.324)
	Bladex.AddAnmLRelease(anm_name,0.532)
	Bladex.AddAnmRStep(anm_name,0.618)
	Bladex.AddAnmLStep(anm_name,0.843)

	#
	# Slip
	#
	anm_name="Amz_slip"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip.BMV",anm_name,1,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Amz_slip_b"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_slip_b.BMV",anm_name,1,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Amz_derrape"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_derrape.BMV",anm_name,0,"Amazon_L")
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
	anm_name="Amz_b1"
	Bladex.LoadSampledAnimation("../../Anm/Amz_b1.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Amz_b2"
	Bladex.LoadSampledAnimation("../../Anm/Amz_b2.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)

	anm_name="Amz_b3"
	Bladex.LoadSampledAnimation("../../Anm/Amz_b3.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)




####
# Heridas sin movimiento
####


	anm_name="Amz_hurt_f_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_back.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_f_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_arm.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_f_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_breast.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_f_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_head.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_f_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_leg.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Amz_hurt_f_neck"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_neck.BMV",anm_name,0,"Amazon_L")
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_f_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_arm.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_f_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_leg.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Amz_hurt0"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt0.BMV",anm_name,0,"Amazon_L")
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

#	anm_name="Amz_hurt_neck"
#	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_neck.BMV",anm_name,0,"Amazon_L")
#	Bladex.AddAnmRStep(anm_name,0.000)
#	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_jog"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_jog.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_head"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_head.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_l_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_arm.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_l_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_l_leg.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_r_arm"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_arm.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_r_leg"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_r_leg.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_back"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_back.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)

	anm_name="Amz_hurt_breast"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_breast.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)




	###############
	#
	#Hurt
	#
	###############

	anm_name="Amz_hurt_jog"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_jog.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.21)
	Bladex.AddAnmRRelease(anm_name,0.36)
	Bladex.AddAnmRStep(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.07)
	Bladex.AddAnmLStep(anm_name,0.4)
	Bladex.AddAnmLRelease(anm_name,0.58)
	Bladex.AddAnmLStep(anm_name,0.8)


	anm_name="Amz_hurt_f_big"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_big.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.4)
	Bladex.AddAnmRStep(anm_name,0.6)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.27)
	Bladex.AddAnmLStep(anm_name,0.43)



	anm_name="Amz_hurt_f_lite"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_hurt_f_lite.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.0)
	Bladex.AddAnmRRelease(anm_name,0.35)
	Bladex.AddAnmRStep(anm_name,0.59)
	Bladex.AddAnmLStep(anm_name,0.0)
	Bladex.AddAnmLRelease(anm_name,0.55)
	Bladex.AddAnmLStep(anm_name,1.0)

	anm_name="Amz_parry_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_parry_spear.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.023)
	Bladex.AddAnmRStep(anm_name,0.459)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.349)
	Bladex.AddAnmLStep(anm_name,0.750)



	anm_name="Amz_df_01_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_df_01_spear.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.380)
	Bladex.AddAnmRStep(anm_name,0.665)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.240)
	Bladex.AddAnmLStep(anm_name,0.585)


	anm_name="Amz_df_02_spear"
	Bladex.LoadSampledAnimation("../../Anm/Amz_df_02_spear.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.454)
	Bladex.AddAnmRStep(anm_name,0.753)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.221)
	Bladex.AddAnmLStep(anm_name,0.593)


	anm_name="Amz_parry_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_parry_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.008)
	Bladex.AddAnmRStep(anm_name,0.203)
	Bladex.AddAnmRRelease(anm_name,0.669)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.136)
	Bladex.AddAnmLStep(anm_name,0.295)
	Bladex.AddAnmLRelease(anm_name,0.435)
	Bladex.AddAnmLStep(anm_name,0.697)



	anm_name="Amz_df_01_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_df_01_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.380)
	Bladex.AddAnmRStep(anm_name,0.665)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.240)
	Bladex.AddAnmLStep(anm_name,0.585)


	anm_name="Amz_df_02_2w"
	Bladex.LoadSampledAnimation("../../Anm/Amz_df_02_2w.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.400)
	Bladex.AddAnmRStep(anm_name,0.695)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.194)
	Bladex.AddAnmLStep(anm_name,0.701)

	anm_name="Amz_sword_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_sword_reaction"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Amazon_L")
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









	#############	########      #########
	#
	# Trepar      ###################
	#
	##################


	anm_name="Amz_clmb_low_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_low_1h.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.17)
	Bladex.AddAnmRStep(anm_name,0.41)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.48)
	Bladex.AddAnmLStep(anm_name,0.82)

	anm_name="Amz_clmb_medlow_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_medlow_1h.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.30)
	Bladex.AddAnmRStep(anm_name,0.79)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.28)
	Bladex.AddAnmLStep(anm_name,0.53)
	Bladex.AddAnmLRelease(anm_name,0.83)
	Bladex.AddAnmLStep(anm_name,0.98)

	anm_name="Amz_clmb_medium_1h"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_clmb_medium_1h.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.13)
	Bladex.AddAnmRStep(anm_name,0.84)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.13)
	Bladex.AddAnmLStep(anm_name,0.100)

	anm_name="Amz_clmb_high_1h"
	Bladex.LoadSampledAnimation("../../Anm/Amz_clmb_high.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.07)
	Bladex.AddAnmRStep(anm_name,0.9)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.07)
	Bladex.AddAnmLStep(anm_name,0.83)





	##########################################
	########### GIROS DE 180� ################
	##########################################




	anm_name="Amz_wlk_turn"
	Bladex.LoadSampledAnimation("../../Anm/Amz_wlk_turn.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.209)
	Bladex.AddAnmRStep(anm_name,0.722)
	Bladex.AddAnmLStep(anm_name,0.178)
	Bladex.AddAnmLRelease(anm_name,0.813)

	anm_name="Amz_snk_turn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_snk_turn.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.403)
	Bladex.AddAnmRStep(anm_name,0.821)
	Bladex.AddAnmLStep(anm_name,0.217)
	Bladex.AddAnmLRelease(anm_name,0.833)


	anm_name="Amz_jog_turn"
	Bladex.LoadSampledAnimation("../../Anm/Amz_jog_turn.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.376)
	Bladex.AddAnmRStep(anm_name,0.714)
	Bladex.AddAnmRRelease(anm_name,0.762)
	Bladex.AddAnmLStep(anm_name,0.284)
	Bladex.AddAnmLRelease(anm_name,0.690)
	Bladex.AddAnmLStep(anm_name,0.952)

	anm_name="Amz_rlx_turn"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_rlx_turn.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.095)
	Bladex.AddAnmLStep(anm_name,0.875)






##################################
#				 #
#	A�adidos de Luismi       #
#				 #
##################################





	anm_name="Amz_tke_r_key00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_key00.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.096)
	Bladex.AddAnmLStep(anm_name,0.159)
	Bladex.AddAnmLRelease(anm_name,0.350)
	Bladex.AddAnmLStep(anm_name,0.443)


	anm_name="Amz_tke_r_key01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_key01.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.121)
	Bladex.AddAnmRStep(anm_name,0.245)
	Bladex.AddAnmRRelease(anm_name,0.420)
	Bladex.AddAnmRStep(anm_name,0.588)


	anm_name="Amz_tke_r_key02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_key02.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.160)
	Bladex.AddAnmRStep(anm_name,0.264)
	Bladex.AddAnmRRelease(anm_name,0.408)
	Bladex.AddAnmRStep(anm_name,0.566)

	anm_name="Amz_tke_r_key03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_key03.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.132)
	Bladex.AddAnmRStep(anm_name,0.261)
	Bladex.AddAnmRRelease(anm_name,0.489)
	Bladex.AddAnmRStep(anm_name,0.689)

	anm_name="Amz_tke_r_key04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_key05.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.153)
	Bladex.AddAnmRStep(anm_name,0.270)
	Bladex.AddAnmRRelease(anm_name,0.401)
	Bladex.AddAnmRStep(anm_name,0.601)




	anm_name="Amz_tke_r_01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_01.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.159)
	Bladex.AddAnmLStep(anm_name,0.327)
	Bladex.AddAnmLRelease(anm_name,0.689)
	Bladex.AddAnmLStep(anm_name,0.893)

	anm_name="Amz_tke_r_02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_02.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.183)
	Bladex.AddAnmRStep(anm_name,0.343)
	Bladex.AddAnmRRelease(anm_name,0.585)
	Bladex.AddAnmRStep(anm_name,0.840)

	anm_name="Amz_tke_r_03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_03.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.191)
	Bladex.AddAnmRStep(anm_name,0.335)
	Bladex.AddAnmRRelease(anm_name,0.502)
	Bladex.AddAnmRStep(anm_name,0.715)

	anm_name="Amz_tke_r_04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_04.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.216)
	Bladex.AddAnmRStep(anm_name,0.395)
	Bladex.AddAnmRRelease(anm_name,0.716)
	Bladex.AddAnmRStep(anm_name,1)

	anm_name="Amz_tke_r_05"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_tke_r_05.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.208)
	Bladex.AddAnmRStep(anm_name,0.369)
	Bladex.AddAnmRRelease(anm_name,0.544)
	Bladex.AddAnmRStep(anm_name,0.842)


	anm_name="Amz_drp_r"
	Bladex.LoadSampledAnimation("../../Anm/Amz_drp_r.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Amz_drp_l"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_drp_l.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)





	anm_name="Amz_attack_chg_r"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_chg_r.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Amz_attack_chg_l"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_chg_l.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Amz_attack_chg_r_l"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_chg_r_l.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)



	anm_name="Amz_drink"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_drink.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Amz_eat00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_eat00.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Amz_gulp00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_gulp.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Amz_attack_drink"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_attack_drink.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)





	anm_name="Amz_key"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_key.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Amz_lvr_u"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_lvr_u.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Amz_lvr_d"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_lvr_d.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)

	anm_name="Amz_pulsador"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_pulsador.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)




	anm_name="Amz_fire0"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_fire0.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Amz_fire1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_fire1.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.091)   # Was missing.
	Bladex.AddAnmRStep(anm_name,0.2)        #
	Bladex.AddAnmRRelease(anm_name,0.650)   #
	Bladex.AddAnmRStep(anm_name,0.824)      #       -LeadHead
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Amz_fire2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_fire2.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.081)     # Was missing.
	Bladex.AddAnmRStep(anm_name,0.225)        #
	Bladex.AddAnmRRelease(anm_name,0.752)     #
	Bladex.AddAnmRStep(anm_name,0.922)        #       -LeadHead
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Amz_fire3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_fire3.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)


	anm_name="Amz_fire_g"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_fire_g.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmRRelease(anm_name,0.108)      # Was missing.
	Bladex.AddAnmRStep(anm_name,0.244)         #
	Bladex.AddAnmRRelease(anm_name,0.758)      #
	Bladex.AddAnmRStep(anm_name,0.926)         #       -LeadHead

	#Bladex.SetAnimationFactor("Kgt_attack_chg_r",1.5)








	anm_name="Amz_df_01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_01.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmLStep(anm_name,0.000)


	anm_name="Amz_df_s_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_s_broken.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmLRelease(anm_name,0.131)
	Bladex.AddAnmLStep(anm_name,0.414)
	Bladex.AddAnmRRelease(anm_name,0.439)
	Bladex.AddAnmRStep(anm_name,595)
	Bladex.AddAnmLRelease(anm_name,0.708)
	Bladex.AddAnmLStep(anm_name,0.867)

	anm_name="Amz_sword_broken"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_sword_reaction"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_sword_broken.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_df_02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_df_02.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0)
	Bladex.AddAnmRRelease(anm_name,0.310)
	Bladex.AddAnmLRelease(anm_name,0.310)
	Bladex.AddAnmRStep(anm_name,0.569)
	Bladex.AddAnmLStep(anm_name,0.832)


############ MUERTES



	anm_name="Amz_dth0"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth0.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_dth_c1"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c1.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmLStep(anm_name,0.00)
	Bladex.AddAnmRStep(anm_name,0.00)
	Bladex.AddAnmLRelease(anm_name,0.040)
	Bladex.AddAnmLStep(anm_name,0.081)
 	Bladex.AddAnmLRelease(anm_name,0.745)  # Added.
	Bladex.AddAnmRRelease(anm_name,0.789)  #
	Bladex.AddAnmLStep(anm_name,0.883)     #
	Bladex.AddAnmRStep(anm_name,0.908)     #    -LeadHead


	anm_name="Amz_dth_c2"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c2.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.037)
	Bladex.AddAnmRStep(anm_name,0.083)
	Bladex.AddAnmRRelease(anm_name,0.166)
	Bladex.AddAnmRStep(anm_name,0.306)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.083)
	Bladex.AddAnmLStep(anm_name,0.126)


	anm_name="Amz_dth_c3"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c3.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.583)
	Bladex.AddAnmRStep(anm_name,0.758)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.597)
	Bladex.AddAnmLStep(anm_name,0.886)


	anm_name="Amz_dth_c4"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c4.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_dth_c5"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c5.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_dth_c6"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_c6.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_dth_c7"
	Bladex.LoadSampledAnimation("../../Anm/Ork_dth_c1.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.282)
	Bladex.AddAnmRStep(anm_name,0.384)
	Bladex.AddAnmRRelease(anm_name,0.659)
	Bladex.AddAnmRStep(anm_name,0.887)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.579)
	Bladex.AddAnmLStep(anm_name,0.890)


	anm_name="Amz_dth_n00"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n00.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.641)
	Bladex.AddAnmRStep(anm_name,0.878)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.192)
	Bladex.AddAnmLStep(anm_name,0.411)
	Bladex.AddAnmLRelease(anm_name,0.626)
	Bladex.AddAnmLStep(anm_name,0.873)


	anm_name="Amz_dth_n01"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n01.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_dth_n02"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n02.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.681)
	Bladex.AddAnmRStep(anm_name,0.859)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.315)
	Bladex.AddAnmLStep(anm_name,0.611)
	Bladex.AddAnmLRelease(anm_name,0.703)
	Bladex.AddAnmLStep(anm_name,0.921)


	anm_name="Amz_dth_n03"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n03.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.101)
	Bladex.AddAnmRStep(anm_name,0.271)
	Bladex.AddAnmRRelease(anm_name,0.478)
	Bladex.AddAnmRStep(anm_name,1.000)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.530)
	Bladex.AddAnmLStep(anm_name,0.692)


	anm_name="Amz_dth_n04"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n04.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_dth_n05"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n05.BMV",anm_name,0,"Amazon_L")
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.825)
	Bladex.AddAnmRStep(anm_name,0.979)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.050)
	Bladex.AddAnmLStep(anm_name,0.138)
	Bladex.AddAnmLRelease(anm_name,0.816)
	Bladex.AddAnmLStep(anm_name,0.950)


	anm_name="Amz_dth_n06"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_n06.BMV",anm_name,0,"Amazon_L")
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


	anm_name="Amz_dth_rock"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rock.BMV",anm_name,0)
	Bladex.AddAnmLStep(anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.00)

	anm_name="Amz_dth_rockfront"
	Bladex.LoadSampledAnimation("../../Anm/Kgt_dth_rockfront.BMV",anm_name,0)
	Bladex.AddAnmRStep(anm_name,0.000)
	Bladex.AddAnmRRelease(anm_name,0.348)
	Bladex.AddAnmRStep(anm_name,0.796)
	Bladex.AddAnmLStep(anm_name,0.000)
	Bladex.AddAnmLRelease(anm_name,0.335)
	Bladex.AddAnmLStep(anm_name,0.792)

	anm_name="Amz_dth_burn"
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
