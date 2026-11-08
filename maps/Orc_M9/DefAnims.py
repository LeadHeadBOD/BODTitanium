import Bladex

def qLoadAnims(Kind,Animation,AnimationFile,person):
	Bladex.LoadSampledAnimation("../../Anm/"+AnimationFile+".BMV",Kind+"_"+Animation,0,person)
	Bladex.AddBipedAction(Kind,Animation,Kind+"_"+Animation,0.0,1.0,0)

def Min():
	qLoadAnims("Min","sp","Min_sp","Minotaur")

def Tkn():
	# Bladex.LoadSampledAnimation("../../Anm/Tkn_prisionero_rlx.bmv","Tkn_prisionero_rlx",1,"Knight_Traitor",1)	# Commented out, anim doesn't exist
	pass

def Gok():
	qLoadAnims("Gok","order_orks","Gok_order_orks","")
	qLoadAnims("Gok","order_minotaur","Gok_order_minotaur","")
	qLoadAnims("Gok","mira","Gok_mira","")

def Knight():
	qLoadAnims("Kgt","anda_hacia_orco","Kgt_anda_hacia_orco","Knight_N")
	qLoadAnims("Kgt","prisionero","Kgt_prisionero","Knight_N")
	qLoadAnims("Kgt","start_orks","Kgt_start_orks","Knight_N")

def Dwf():
	qLoadAnims("Dwf","anda_hacia_orco","Dwf_anda_hacia_orco","Dwarf_N")
	qLoadAnims("Dwf","prisionero","Dwf_prisionero","Dwarf_N")
	qLoadAnims("Dwf","mural_orcos","Kgt_mural_orcos","Dwarf_N")
	qLoadAnims("Dwf","start_orks","Dwf_start_orks","Dwarf_N")

def Amz():
	qLoadAnims("Amz","anda_hacia_orco","Kgt_anda_hacia_orco","Amazon_N")
	qLoadAnims("Amz","prisionero","Kgt_prisionero","Amazon_N")
	qLoadAnims("Amz","mural_orcos","Kgt_mural_orcos","Amazon_N")
	qLoadAnims("Amz","start_orks","Amz_start_orks","Amazon_N")

def Bar():
	qLoadAnims("Bar","anda_hacia_orco","Kgt_anda_hacia_orco","Barbarian_N")
	qLoadAnims("Bar","prisionero","Kgt_prisionero","Barbarian_N")
	qLoadAnims("Bar","mural_orcos","Kgt_mural_orcos","Barbarian_N")
	qLoadAnims("Bar","start_orks","Bar_start_orks","Barbarian_N")