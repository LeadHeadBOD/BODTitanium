##///
##||| BIPED.PY TITANIUM
##||| Change list:
##||| * Added Ice Golem
##||| * Added Gold Ork
##||| 
##\\\ 

import Bladex
import DefAnims

#
# Kind of attack set -> For the combos files
#
ATK_UNIQUE=0
ATK_RANDOM=1
ATK_SEQUENTIAL=2


import Trails
Trails.Init()

import ActionTables
ActionTables.Init()



#
# Caballero
#

def KnightWhenFirst():	
	Bladex.CreateBipedData("Knight","Knight_N")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Knight.dat")
	import KnightAnimationSet
	KnightAnimationSet.LoadKnightAnimationSet("Knight")
	import KgtBAct
	import LinkTables
	LinkTables.LinkMe("Knight")
	import KgtCombos
	import AnmFact
	AnmFact.AnmFactKnight()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Knight.dat","Knight")
	if dir(DefAnims).count("Knight"):
		DefAnims.Knight()
	Bladex.AddFloorCTolerance("slip",10)


#
# Amazon
#
def AmzWhenFirst():
	Bladex.CreateBipedData("Amz","Amazon_N")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Amz.dat")
	import AmzAnimationSet
	AmzAnimationSet.LoadAmzAnimationSet("Amz")
	import AmzBAct
	import LinkTables	
	LinkTables.LinkMe("Amz")
	import AmzCombos
	import AnmFact
	AnmFact.AnmFactAmazon()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Amz.dat","Amz")
	if dir(DefAnims).count("Amz"):
		DefAnims.Amz()
	Bladex.AddFloorCTolerance("slip",10)



#
# Dwarf
#
def DwfWhenFirst():		
	Bladex.CreateBipedData("Dwf","Dwarf_N")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Dwf.dat")
	import DwfAnimationSet
	DwfAnimationSet.LoadDwfAnimationSet("Dwf")
	import DwfBAct
	import LinkTables
	LinkTables.LinkMe("Dwf")
	import DwfCombos
	import AnmFact
	AnmFact.AnmFactDwarf()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Dwf.dat","Dwf")
	if dir(DefAnims).count("Dwf"):
		DefAnims.Dwf()
	Bladex.AddFloorCTolerance("slip",10)




#
# Dwarf 1
#
def Dwf1WhenFirst():	
	Bladex.CreateBipedData("Ena","Enano1")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Ena.dat")
	import DwfAnimationSet
	DwfAnimationSet.LoadDwfAnimationSet("Enano1")
	import Dwf1BAct
	import LinkTables
	LinkTables.LinkMe("Ena")
	import Dwf1Combos
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Ena.dat","Ena")
	if dir(DefAnims).count("Ena"):
		DefAnims.Ena()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "DwarfIcon1")	




#
# Dwarf 2
#
def Dwf2WhenFirst():	
	Bladex.CreateBipedData("Enb","Enano2")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Enb.dat")
	import DwfAnimationSet
	DwfAnimationSet.LoadDwfAnimationSet("Enano2")
	import Dwf2BAct
	import LinkTables
	LinkTables.LinkMe("Enb")
	import Dwf2Combos
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Enb.dat","Enb")
	if dir(DefAnims).count("Enb"):
		DefAnims.Enb()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "DwarfIcon2")	





#
# Barbarian
#
def BarWhenFirst():	
	Bladex.CreateBipedData("Bar","Barbarian_N")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Bar.dat")
	import BarAnimationSet
	BarAnimationSet.LoadBarAnimationSet("Bar")
	import BarBAct
	import LinkTables
	LinkTables.LinkMe("Bar")
	if dir(DefAnims).count("Bar"):
		DefAnims.Bar()
	import BarCombos
	import AnmFact
	AnmFact.AnmFactBarbarian()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Bar.dat","Bar")
	Bladex.AddFloorCTolerance("slip",10)








#
# Traitor Knight
#
def TraitorKnightWhenFirst():
	Bladex.CreateBipedData("Knight_Traitor","Knight_Traitor")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Knight_Traitor.dat")
	import TraiKnightAnimationSet
	TraiKnightAnimationSet.LoadTraitorKnightAnimationSet("Knight_Traitor")
	import TknBAct
	import LinkTables	
	LinkTables.LinkMe("Knight_Traitor")
	import TknCombos
	import AnmFact
	AnmFact.AnmFactTraitorKnight()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Knight_Traitor.dat","Knight_Traitor")
	if dir(DefAnims).count("Knight_Traitor"):
		DefAnims.Knight_Traitor()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "TraitorIcon")	






#
# Ork
#
def OrkWhenFirst():
	Bladex.CreateBipedData("Ork","Ork")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Ork.dat")
	import OrkAnimationSet
	OrkAnimationSet.LoadOrkAnimationSet("Ork")
	import OrkBAct
	import LinkTables
	LinkTables.LinkMe("Ork")
	import OrkCombos
	import AnmFact
	AnmFact.AnmFactOrk()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Ork.dat","Ork")
	if dir(DefAnims).count("Ork"):
		DefAnims.Ork()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "OrcIcon")	



#
# Dark Ork
#
def Dark_OrkWhenFirst():
	Bladex.CreateBipedData("Dok","Dark_Ork")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Dok.dat")
	import OrkAnimationSet
	OrkAnimationSet.LoadOrkAnimationSet("Dok")
	import DokBAct
	import LinkTables
	LinkTables.LinkMe("Dok")
	import DokCombos
	import AnmFact
	AnmFact.AnmFactOrk()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Dok.dat","Dok")
	if dir(DefAnims).count("Dok"):
		DefAnims.Dok()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "OrkDarkIcon")	

#
# Gold ork
#
def Gold_OrkWhenFirst():
	Bladex.CreateBipedData("Org","Gold_Ork")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Org.dat")
	import OrkAnimationSet
	OrkAnimationSet.LoadOrkAnimationSet("Org")
	import OrgBAct
	import LinkTables
	LinkTables.LinkMe("Org")
	import OrgCombos
	import AnmFact
	AnmFact.AnmFactOrk()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Org.dat","Org")
	if dir(DefAnims).count("Org"):
		DefAnims.Org()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "OrkGoldIcon")	


#
# Great Ork
#
def Great_OrkWhenFirst():
	Bladex.CreateBipedData("Gok","Great_Ork")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Gok.dat")
	import GokAnimationSet
	GokAnimationSet.LoadGokAnimationSet("Gok")
	import GokBAct
	import LinkTables
	LinkTables.LinkMe("Gok")
	import GokCombos
	import AnmFact
	AnmFact.AnmFactGreatOrk()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Gok.dat","Gok")
	if dir(DefAnims).count("Gok"):
		DefAnims.Gok()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "GorkIcon")	



#
# Ldm
#
def LittleDemonWhenFirst():
	Bladex.CreateBipedData("Ldm","Little_Demon")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Ldm.dat")
	import LdmAnimationSet
	LdmAnimationSet.LoadLdmAnimationSet("Ldm")
	import LdmBAct
	import LinkTables
	LinkTables.LinkMe("Ldm")
	import LdmCombos
	import AnmFact
	AnmFact.AnmFactLittleDemon()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Ldm.dat","Ldm")
	if dir(DefAnims).count("Ldm"):
		DefAnims.Ldm()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "LDemonIcon")	




#
# Gdm
#
def GreaterDemonWhenFirst():
	Bladex.CreateBipedData("Gdm","Great_Demon")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Gdm.dat")
	import GdmAnimationSet
	GdmAnimationSet.LoadGdmAnimationSet("Gdm")
	import GdmBAct
	import LinkTables
	LinkTables.LinkMe("Gdm")
	import GdmCombos
	import AnmFact
	AnmFact.AnmFactGreatDemon()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Gdm.dat","Gdm")
	if dir(DefAnims).count("Gdm"):
		DefAnims.Gdm()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadBOD('FireRing')
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "GDemonIcon")	





#
# Skeleton
#
def SkeletonWhenFirst():
	Bladex.CreateBipedData("Skl","Skeleton")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Skl.dat")
	import SklAnimationSet
	SklAnimationSet.LoadSklAnimationSet("Skl")
	import SklBAct
	import LinkTables
	LinkTables.LinkMe("Skl")
	import SklCombos
	import AnmFact
	AnmFact.AnmFactSkeleton()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Skl.dat","Skl")
	if dir(DefAnims).count("Skl"):
		DefAnims.Skl()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "SkeletonIcon")	





#
# Cos
#
def CosWhenFirst():
	Bladex.CreateBipedData("Cos","Cos")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Cos.dat")
	import CosAnimationSet
	CosAnimationSet.LoadCosAnimationSet("Cos")
	import CosBAct
	import LinkTables
	LinkTables.LinkMe("Cos")
	import CosCombos
	import AnmFact
	AnmFact.AnmFactCosita()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Cos.dat","Cos")
	if dir(DefAnims).count("Cos"):
		DefAnims.Cos()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "CosIcon")	




#
# Min
#
def MinWhenFirst():
	Bladex.CreateBipedData("Min","Minotaur")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Min.dat")
	import MinAnimationSet
	MinAnimationSet.LoadMinAnimationSet("Min")
	import MinBAct
	import LinkTables
	LinkTables.LinkMe("Min")
	import MinCombos
	import AnmFact
	AnmFact.AnmFactMinotaur()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Min.dat","Min")
	if dir(DefAnims).count("Min"):
		DefAnims.Min()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "MinotaurIcon")	
	




#
# Lich
#
def LichWhenFirst():
	Bladex.CreateBipedData("Lch","Lich")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Lch.dat")
	import LchAnimationSet
	LchAnimationSet.LoadLchAnimationSet("Lch")
	import LchBAct
	import LinkTables
	LinkTables.LinkMe("Lch")
	import LchCombos
	import AnmFact
	AnmFact.AnmFactLich()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Lch.dat","Lch")
	if dir(DefAnims).count("Lch"):
		DefAnims.Lch()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "Lich")	
	





#
# Salamander
#
def SalamanderWhenFirst():	
	Bladex.CreateBipedData("Slm","Salamander")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Slm.dat")
	import SlmAnimationSet
	SlmAnimationSet.LoadSlmAnimationSet("Slm")
	import SlmBAct
	import LinkTables
	LinkTables.LinkMe("Slm")
	import SlmCombos
	import AnmFact
	AnmFact.AnmFactSalamander()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Slm.dat","Slm")
	if dir(DefAnims).count("Slm"):
		DefAnims.Slm()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "SalamanderIcon")	





#
# Chk
#
def ChaosKnightWhenFirst():
	Bladex.CreateBipedData("Chk","ChaosKnight")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Chk.dat")
	import ChkAnimationSet
	ChkAnimationSet.LoadChkAnimationSet("Chk")
	import ChkBAct
	import LinkTables
	LinkTables.LinkMe("Chk")
	import ChkCombos
	import AnmFact
	AnmFact.AnmFactChosKnight()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Chk.dat","Chk")
	if dir(DefAnims).count("Chk"):
		DefAnims.Chk()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadBOD('EsferaNegra')	
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "ChaosIcon")	




#
# Vmp
#
def VampWhenFirst():
	Bladex.CreateBipedData("Vmp","Vamp")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Vmp.dat")
	import VmpAnimationSet
	VmpAnimationSet.LoadVmpAnimationSet("Vmp")
	import VmpBAct
	import LinkTables
	LinkTables.LinkMe("Vmp")
	import VmpCombos
	import AnmFact
	AnmFact.AnmFactVampire()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Vmp.dat","Vmp")
	if dir(DefAnims).count("Vmp"):
		DefAnims.Vmp()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "VampireIcon")	




#
# RAGNAR
#
def RagnarWhenFirst():
	Bladex.CreateBipedData("Rgn","Ragnar")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Rgn.dat")
	import RgnAnimationSet
	RgnAnimationSet.LoadRgnAnimationSet("Rgn")
	import RgnBAct
	import LinkTables
	LinkTables.LinkMe("Rgn")
	import RgnCombos
	import AnmFact
	AnmFact.AnmFactRagnar()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Rgn.dat","Rgn")
	if dir(DefAnims).count("Rgn"):
		DefAnims.Rgn()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "RagnarIcon")	





#
# PRISONER_1
#
def Prs_1WhenFirst():
	Bladex.CreateBipedData("Prs_1","Prisoner_1")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Prs_1.dat")
	import PrsAnimationSet
	PrsAnimationSet.LoadPrsAnimationSet("Prs")
	import PrsBAct
	PrsBAct.BAct("Prs_1")
	import LinkTables
	LinkTables.LinkMe("Prs_1")
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Prs_1.dat","Prs_1")
	if dir(DefAnims).count("Prs_1"):
		DefAnims.Prs_1()
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "PrisonerIcon")	



#
# PRISONER_2
#
def Prs_2WhenFirst():
	Bladex.CreateBipedData("Prs_2","Prisoner_2")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Prs_2.dat")
	import PrsAnimationSet
	PrsAnimationSet.LoadPrsAnimationSet("Prs")	
	import PrsBAct
	PrsBAct.BAct("Prs_2")
	import LinkTables
	LinkTables.LinkMe("Prs_2")
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Prs_2.dat","Prs_2")
	if dir(DefAnims).count("Prs_2"):
		DefAnims.Prs_2()



#
# PRISONER_3
#
def Prs_3WhenFirst():
	Bladex.CreateBipedData("Prs_3","Prisoner_3")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Prs_3.dat")
	import PrsAnimationSet
	PrsAnimationSet.LoadPrsAnimationSet("Prs")
	import PrsBAct
	PrsBAct.BAct("Prs_3")
	import LinkTables
	LinkTables.LinkMe("Prs_3")
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Prs_3.dat","Prs_3")
	if dir(DefAnims).count("Prs_3"):
		DefAnims.Prs_3()



#
# PRISONER_4
#
def Prs_4WhenFirst():
	Bladex.CreateBipedData("Prs_4","Prisoner_4")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Prs_4.dat")
	import PrsAnimationSet
	PrsAnimationSet.LoadPrsAnimationSet("Prs")
	import PrsBAct
	PrsBAct.BAct("Prs_4")
	import LinkTables
	LinkTables.LinkMe("Prs_4")
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Prs_4.dat","Prs_4")
	if dir(DefAnims).count("Prs_4"):
		DefAnims.Prs_4()



#
# PRISONER_5
#
def Prs_5WhenFirst():
	Bladex.CreateBipedData("Prs_5","Prisoner_5")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Prs_5.dat")
	import PrsAnimationSet
	PrsAnimationSet.LoadPrsAnimationSet("Prs")
	import PrsBAct
	PrsBAct.BAct("Prs_5")
	import LinkTables
	LinkTables.LinkMe("Prs_5")
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Prs_5.dat","Prs_5")
	if dir(DefAnims).count("Prs_5"):
		DefAnims.Prs_5()



#
# PRISONER_6
#
def Prs_6WhenFirst():
	Bladex.CreateBipedData("Prs_6","Prisoner_6")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Prs_6.dat")
	import PrsAnimationSet
	PrsAnimationSet.LoadPrsAnimationSet("Prs")
	import PrsBAct
	PrsBAct.BAct("Prs_6")
	import LinkTables
	LinkTables.LinkMe("Prs_6")
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Prs_6.dat","Prs_6")
	if dir(DefAnims).count("Prs_6"):
		DefAnims.Prs_6()






















#                                                       
# Zombie Knight                                         
#                                                       
def Knight_ZombieWhenFirst():                           
	Bladex.CreateBipedData("Zkn","Knight_Zombie")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Zkn.dat")
	import LchAnimationSet
	LchAnimationSet.LoadLchAnimationSet("Zkn")      
	import ZknBAct
	import LinkTables
	LinkTables.LinkMe("Zkn")
	import ZknCombos
	import AnmFact
	AnmFact.AnmFactLich()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Zkn.dat","Zkn")
	if dir(DefAnims).count("Zkn"):
		DefAnims.Zkn()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "KnightzombieIcon")	


     
#                                                            
# Dark Knight                                              
#                                                            

def Dark_KnightWhenFirst():                                
	Bladex.CreateBipedData("Dkn","Dark_Knight")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Dkn.dat")
	import TraiKnightAnimationSet
	TraiKnightAnimationSet.LoadTraitorKnightAnimationSet("Dkn")
	import DknBAct
	import LinkTables
	LinkTables.LinkMe("Dkn")
	import AnmFact
	AnmFact.AnmFactTraitorKnight()
	import DknCombos
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Dkn.dat","Dkn")
	if dir(DefAnims).count("Dkn"):
		DefAnims.Dkn()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "KnightDarkIcon")	

                                                             




#                                                       
# Troll Dark                                         
#                                                       
def Troll_DarkWhenFirst():                           
	Bladex.CreateBipedData("Trl","Troll_Dark")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Trl.dat")
	import TrlAnimationSet
	TrlAnimationSet.LoadTrlAnimationSet("Trl")      
	import TrlBAct
	import LinkTables
	LinkTables.LinkMe("Trl")                        
	import TrlCombos
	import AnmFact
	AnmFact.AnmFactTroll()	
	#...

	race=Bladex.GetCharType("Troll_snow","Trl")
	race.Biped="Trl"
	# race.BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "TrollSnowIcon")
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Trl.dat","Trl")
	if dir(DefAnims).count("Trl"):
		DefAnims.Trl()
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "TrollDarkIcon")	


#
# Troll Snow
#
# def Troll_SnowWhenFirst():                           
	# Bladex.CreateBipedData("Trl_sn","Troll_Snow")
	# exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Trl_sn.dat")
	# import TrlAnimationSet
	# TrlAnimationSet.LoadTrlAnimationSet("Trl_sn")      
	# import Trl_snBAct
	# import LinkTables
	# LinkTables.LinkMe("Trl_sn")                        
	# import Trl_snCombos
	# import AnmFact
	# AnmFact.AnmFactTroll()	
	# if not exitsPak:
		# Bladex.SaveAnmRaceData("../../AnmPak/Trl_sn.dat","Trl_sn")
	# if dir(DefAnims).count("Trl_sn"):
		# DefAnims.Trl_sn()
	# import BBLib
	# BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "TrollSnowIcon")	






#                                                       
# Small Spider                                         
#                                                       
def SpidersmallWhenFirst():                           
	Bladex.CreateBipedData("Spd","Spidersmall")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Spd.dat")
	import SpdAnimationSet
	SpdAnimationSet.LoadSpdAnimationSet("Spd")
	import SpdsmallBAct
	import LinkTables
	LinkTables.LinkMe("Spd")
	import SpdCombos
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Spd.dat","Spd")
	if dir(DefAnims).count("Spd"):
		DefAnims.Spd()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "SpiderIcon")	




#                                   
# DalGurak                                         
#
def DalGurakWhenFirst():
	Bladex.CreateBipedData("Dgk","DalGurak")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Dgk.dat")
	import DgkAnimationSet
	DgkAnimationSet.LoadDgkAnimationSet("Dgk")
	import DgkBAct
	import LinkTables
	LinkTables.LinkMe("Dgk")
	import DgkCombos
	import AnmFact
	AnmFact.AnmFactDalGurak()
	Bladex.AddFloorCTolerance("slip",10)
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Dgk.dat","Dgk")
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "DalGurakIcon")	
	if dir(DefAnims).count("Dgk"):
		DefAnims.Dgk()







#
# An-Ahkard        
#
def AnAhkardWhenFirst():
	Bladex.CreateBipedData("Ank","DarkLord")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Ank.dat")
	import AnkAnimationSet
	AnkAnimationSet.LoadAnkAnimationSet("Ank")
	import AnkBAct
	import LinkTables
	LinkTables.LinkMe("Ank")
	import AnkCombos
	import AnmFact
	AnmFact.AnmFactAnAhkard()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Ank.dat","Ank")
	if dir(DefAnims).count("Ank"):
		DefAnims.Ank()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "DarkLordIcon")	






#
# Golems
#
def Golem_stoneWhenFirst():
	Bladex.CreateBipedData("Glm_st","Golem_stone")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Glm_st.dat")
	import GlmAnimationSet
	GlmAnimationSet.LoadGlmAnimationSet("Glm_st")
	import Glm_stBAct
	import LinkTables
	LinkTables.LinkMe("Glm_st")
	import Glm_stCombos
	import AnmFact
	AnmFact.AnmFactGolem()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Glm_st.dat","Glm_st")
	if dir(DefAnims).count("Glm_st"):
		DefAnims.Glm_st()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadBOD('Piedra_Glm_st')
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "StoneGolemIcon")	



def Golem_clayWhenFirst():
	Bladex.CreateBipedData("Glm_cl","Golem_clay")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Glm_cl.dat")
	import GlmAnimationSet
	GlmAnimationSet.LoadGlmAnimationSet("Glm_cl")
	import Glm_clBAct
	import LinkTables
	LinkTables.LinkMe("Glm_cl")
	import Glm_clCombos
	import AnmFact
	AnmFact.AnmFactGolem()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Glm_cl.dat","Glm_cl")
	if dir(DefAnims).count("Glm_cl"):
		DefAnims.Glm_cl()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadBOD('Piedra_Glm_cl')
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "ClayGolemIcon")	



def Golem_lavaWhenFirst():
	Bladex.CreateBipedData("Glm_lv","Golem_lava")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Glm_lv.dat")
	import GlmAnimationSet
	GlmAnimationSet.LoadGlmAnimationSet("Glm_lv")
	import Glm_lvBAct
	import LinkTables
	LinkTables.LinkMe("Glm_lv")
	import Glm_lvCombos
	import AnmFact
	AnmFact.AnmFactGolem()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Glm_lv.dat","Glm_lv")
	if dir(DefAnims).count("Glm_lv"):
		DefAnims.Glm_lv()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadBOD('Piedra_Glm_lv')
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "LavaGolemIcon")



def Golem_metalWhenFirst():
	Bladex.CreateBipedData("Glm_mt","Golem_metal")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Glm_mt.dat")
	import GlmAnimationSet
	GlmAnimationSet.LoadGlmAnimationSet("Glm_mt")
	import Glm_mtBAct
	import LinkTables
	LinkTables.LinkMe("Glm_mt")
	import Glm_mtCombos
	import AnmFact
	AnmFact.AnmFactGolem()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Glm_mt.dat","Glm_mt")
	if dir(DefAnims).count("Glm_mt"):
		DefAnims.Glm_mt()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadBOD('Piedra_Glm_mt')
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "MetalGolemIcon")	



def Golem_iceWhenFirst():                               ### Added -LeadHead
	Bladex.CreateBipedData("Glm_ic","Golem_ice")
	exitsPak=Bladex.LoadAnmRaceData("../../AnmPak/Glm_ic.dat")
	import GlmAnimationSet
	GlmAnimationSet.LoadGlmAnimationSet("Glm_ic")
	import Glm_icBAct
	import LinkTables
	LinkTables.LinkMe("Glm_ic")
	import Glm_icCombos
	import AnmFact
	AnmFact.AnmFactGolem()
	if not exitsPak:
		Bladex.SaveAnmRaceData("../../AnmPak/Glm_ic.dat","Glm_ic")
	if dir(DefAnims).count("Glm_ic"):
		DefAnims.Glm_ic()
	Bladex.AddFloorCTolerance("slip",10)
	import BBLib
	BBLib.LoadBOD('Piedra_Glm_ic')
	BBLib.LoadResourceToMemory(BBLib.B_CID_BMP, "IceGolemIcon")	




def Init():
	race=Bladex.GetCharType("Knight_N","Kgt_N")
	race.OnFirst=KnightWhenFirst

	race=Bladex.GetCharType("Amazon_N","Amz_N")
	race.OnFirst=AmzWhenFirst

	race=Bladex.GetCharType("Dwarf_N","Dwf_N")
	race.OnFirst=DwfWhenFirst

	race=Bladex.GetCharType("Enano1","Enano1")
	race.OnFirst=Dwf1WhenFirst

	race=Bladex.GetCharType("Enano2","Enano2")
	race.OnFirst=Dwf2WhenFirst

	race=Bladex.GetCharType("Barbarian_N","Bar")
	race.OnFirst=BarWhenFirst

	race=Bladex.GetCharType("Knight_Traitor","Tkn")
	race.OnFirst=TraitorKnightWhenFirst

	race=Bladex.GetCharType("Ork","Ork")
	race.OnFirst=OrkWhenFirst

	race=Bladex.GetCharType("Dark_Ork","Dok")
	race.OnFirst=Dark_OrkWhenFirst

	race=Bladex.GetCharType("Gold_Ork","Org")           #Added -LeadHead
	race.OnFirst=Gold_OrkWhenFirst

	race=Bladex.GetCharType("Great_Ork","Gok")
	race.OnFirst=Great_OrkWhenFirst

	race=Bladex.GetCharType("Little_Demon","Ldm")
	race.OnFirst=LittleDemonWhenFirst

	race=Bladex.GetCharType("Great_Demon","Gdm")
	race.OnFirst=GreaterDemonWhenFirst
	
	race=Bladex.GetCharType("Skeleton","Skl")
	race.OnFirst=SkeletonWhenFirst

	race=Bladex.GetCharType("Cos","Cos")
	race.OnFirst=CosWhenFirst

	race=Bladex.GetCharType("Minotaur","Min")
	race.OnFirst=MinWhenFirst

	race=Bladex.GetCharType("Lich","Lch")
	race.OnFirst=LichWhenFirst

	race=Bladex.GetCharType("Salamander","Slm")
	race.OnFirst=SalamanderWhenFirst

	race=Bladex.GetCharType("ChaosKnight","Chk")
	race.OnFirst=ChaosKnightWhenFirst

	race=Bladex.GetCharType("Vamp","Vmp")
	race.OnFirst=VampWhenFirst

	race=Bladex.GetCharType("Ragnar","Rgn")
	race.OnFirst=RagnarWhenFirst

	race=Bladex.GetCharType("Prisoner_1","Prs_1")
	race.OnFirst=Prs_1WhenFirst

	race=Bladex.GetCharType("Prisoner_2","Prs_2")
	race.OnFirst=Prs_2WhenFirst

	race=Bladex.GetCharType("Prisoner_3","Prs_3")
	race.OnFirst=Prs_3WhenFirst

	race=Bladex.GetCharType("Prisoner_4","Prs_4")
	race.OnFirst=Prs_4WhenFirst

	race=Bladex.GetCharType("Prisoner_5","Prs_5")
	race.OnFirst=Prs_5WhenFirst

	race=Bladex.GetCharType("Prisoner_6","Prs_6")
	race.OnFirst=Prs_6WhenFirst

	race=Bladex.GetCharType("Knight_Zombie","Zkn")
	race.OnFirst=Knight_ZombieWhenFirst

	race=Bladex.GetCharType("Dark_Knight","Dkn")
	race.OnFirst=Dark_KnightWhenFirst

	race=Bladex.GetCharType("Troll_Dark","Trl")
	race.OnFirst=Troll_DarkWhenFirst

	race=Bladex.GetCharType("Troll_snow","Trl")          
	race.OnFirst=Troll_DarkWhenFirst                     #Para que cree bipedo ,para que carge sus animaciones

	race=Bladex.GetCharType("Spidersmall","Spd")
	race.OnFirst=SpidersmallWhenFirst

	race=Bladex.GetCharType("DalGurak","Dgk")
	race.OnFirst=DalGurakWhenFirst

	race=Bladex.GetCharType("DarkLord","Ank")
	race.OnFirst=AnAhkardWhenFirst

	race=Bladex.GetCharType("Golem_stone","Glm")
	race.OnFirst=Golem_stoneWhenFirst

	race=Bladex.GetCharType("Golem_clay","Glm")
	race.OnFirst=Golem_clayWhenFirst

	race=Bladex.GetCharType("Golem_lava","Glm")
	race.OnFirst=Golem_lavaWhenFirst
	
	race=Bladex.GetCharType("Golem_metal","Glm")
	race.OnFirst=Golem_metalWhenFirst	
    
	race=Bladex.GetCharType("Golem_ice","Glm")          #They forgot about you
	race.OnFirst=Golem_iceWhenFirst                     # -LeadHead





#
#
#   VARIOS - Esto siempre al final del fichero!!!
#   Psado al final de TODAS ( o eso deberia ser !) xxxxxxWhenFirst()
#
#Bladex.AddFloorCTolerance("slip",10)

