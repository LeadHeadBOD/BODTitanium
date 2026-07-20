##///
##||| REFERENCE.PY TITANIUM
##||| Change list:
##||| * Wooden shields/2h weapons now makes wooden hit sound
##||| * Rhino Club now makes wooden hit sound
##||| * Added IceGolem attack data
##||| * Added Zombie Knight attack data 
##||| * Added Pivote2 and PivoteEnvenenado
##\\\ 

import Bladex
import math
import netgame
import os

PI = math.pi
TWOPI = PI*2.0
#
# Dictionaries Module
#

######################################
#
# Demo
#

DEMO_MODE=0
if not os.path.exists("../../maps/Mine_M5"):
	DEMO_MODE=1
DEMO_PLAYERS=("AM", "BR", "KN", "DW")


######################################
#
# To show debugging info or not
#
DEBUG_INFO   = 0
PYTHON_DEBUG = 0

def debugprint(Msg):
	if DEBUG_INFO==0:
		return
	try:
		print Msg
	except TypeError:
		pass
######################################


####################################
#Damage Stuff
#

#Damage flags
BODY_UNCLASSIFIED=-1
BODY_FRONT=1
BODY_BACK=2
BODY_HEAD=3
BODY_RARM=6
BODY_LARM=4
BODY_RHAND=7
BODY_LHAND=5
BODY_RLEG=10
BODY_LLEG=8
BODY_RFOOT=11
BODY_LFOOT=9

# Particles values
B_PARTICLE_GTYPE_COPY=0
B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2
B_PARTICLE_GTYPE_MUL=3

#
# Animation state flag
#
WUEA_NONE=0    #It does not have to wait (relax , jog or similars)
WUEA_WAIT=1    #It has to wait , and is waiting to end it
WUEA_ENDED=2   #It has to wait , and it has just ended

# Messages (copied from EntityMessages.hpp)
MESSAGE_PARENT_MOVE=             0x00000001
MESSAGE_PARENT_LINK=             0x00000002
MESSAGE_PARENT_UNLINK=           0x00000003
MESSAGE_CHILD_UNLINK=            0x00000004
MESSAGE_IMPALE=                  0x00000005
MESSAGE_SLASH=                   0x00000006
MESSAGE_START_WEAPON=            0x00000007
MESSAGE_STOP_WEAPON=             0x00000008
MESSAGE_STICK_WEAPON=            0x00000009
MESSAGE_PARENT_NODE_LINK=        0x0000000A
MESSAGE_ELECTRIC_DISCHARGE=      0x0000000B
MESSAGE_PERSONMOV=               0x0000000C
MESSAGE_SETSTATICWEPONMODE=      0x0000000D
MESSAGE_START_TRAIL=             0x0000000E
MESSAGE_STOP_TRAIL=              0x0000000F

# Weapon Modes
UNACTIVE_WEAPON_MODE=    0
START_WEAPON_MODE=       1
ACTIVE_WEAPON_MODE=      2

# Exclusion Flags
B_SOLID_MASK_PERSON          =1

# Targetting Data
TARGET_ANGLE_MIN                 = (1.0*PI/180.0)
TARGET_ANGLE_MAX                 = (4.0*PI/180.0)

ENERGY_LOW_LEVEL=0.25

MaterialOnHitInfo ={}

######################################
# Sound Tables (Please complete these lists, these are just examples)
# Please check that any sounds in the list call the SendNotify=1 in AniSound.py

# Sound Flags
SND_UNCLASSIFIED=-1
SND_ARROW=0		# Sonidas Flechas (Arrow sounds)
SND_HIT=1		# Objeto Arrojado o golpeado (thrown objects or hitting sounds)
SND_NPC=2		# Sonido de enemigo.  Por grito o herida (Other NPCs shouting, or injured)
SND_NOISYPC=3	# Sonido de personaje cuando no esta en modo siglo (pisadas) (PC sounds when they're not in silent mode -- footsteps)
SND_PC=4		# Gritas de ataco o herida (Battle cries or injuries of the PC)

SoundTypes={}

# Sonidas Flechas (Arrow sounds)
#SoundTypes['']=[SND_ARROW]        ???

# Objeto Arrojado o golpeado (thrown objects or hitting sounds)
##SoundTypes['SesgadoCorto']=[SND_HIT]
#SoundTypes['SesgadoLargo']=[SND_HIT]
#SoundTypes['SesgadoCortoGrave']=[SND_HIT]
#SoundTypes['SesgadoLargoGrave']=[SND_HIT]
#SoundTypes['SesgadoCortoAgudo']=[SND_HIT]
#SoundTypes['SesgadoLargoAgudo']=[SND_HIT]
#SoundTypes['GolpeArmaEscudo']=[SND_HIT]
#SoundTypes['GolpeArmaArma']=[SND_HIT]
#SoundTypes['TajoEmpalante']=[SND_HIT]
#SoundTypes['TajoCortante']=[SND_HIT]
#SoundTypes['TajoMutilacion']=[SND_HIT]
SoundTypes['GolpeMaderaLigera']=[SND_HIT]
SoundTypes['GolpeMaderaMediana']=[SND_HIT]
SoundTypes['GolpeMaderaPesada']=[SND_HIT]
SoundTypes['GolpeMetalLigero']=[SND_HIT]
SoundTypes['GolpeMetalMediano']=[SND_HIT]
SoundTypes['GolpeMetalPesado']=[SND_HIT]
SoundTypes['GolpePiedraLigera']=[SND_HIT]
SoundTypes['GolpePiedraMediana']=[SND_HIT]
SoundTypes['GolpePiedraPesada']=[SND_HIT]
SoundTypes['GolpeGenerico2']=[SND_HIT]
SoundTypes['GolpeCristal']=[SND_HIT]
SoundTypes['GolpeCeramicaLigera']=[SND_HIT]
SoundTypes['GolpeCeramicaMediana']=[SND_HIT]
SoundTypes['GolpeCeramicaPesada']=[SND_HIT]
SoundTypes['GolpeCarne']=[SND_HIT]

# Sonido de enemigo.  Por grito o herida (Other NPCs shouting, or injured)

#SoundTypes['EsfuerzoCorto1Orco']=[SND_NPC]
#SoundTypes['EsfuerzoCorto2Orco']=[SND_NPC]
#SoundTypes['EsfuerzoCorto5Orco']=[SND_NPC]
#SoundTypes['EsfuerzoCorto6Orco']=[SND_NPC]
#SoundTypes['EsfuerzoGolpeArribaOrco']=[SND_NPC]
#SoundTypes['EsfuerzoGolpeFrontalOrco']=[SND_NPC]
#SoundTypes['EsfuerzoGolpeCabezaOrco']=[SND_NPC]
#SoundTypes['EsfuerzoGolpeLateralOrco']=[SND_NPC]
#SoundTypes['MuerteOrco1']=[SND_NPC]
#SoundTypes['MuerteOrco2']=[SND_NPC]
#SoundTypes['MuerteOrco3']=[SND_NPC]
#SoundTypes['MuerteOrco4']=[SND_NPC]
#SoundTypes['HeridaOrco1']=[SND_NPC]
#SoundTypes['HeridaOrco2']=[SND_NPC]
#SoundTypes['HeridaOrco3']=[SND_NPC]



# Battlecries?

# Sonido de personaje cuando no esta en modo siglo (pisadas) (PC sounds when they're not in silent mode -- footsteps)

SoundTypes['BeberBarb']=[SND_NOISYPC]
SoundTypes['PasoAgua1']=[SND_NOISYPC]
SoundTypes['PasoAgua2']=[SND_NOISYPC]
SoundTypes['PasoAgua3']=[SND_NOISYPC]
SoundTypes['PasoAgua4']=[SND_NOISYPC]
SoundTypes['PasoArena1']=[SND_NOISYPC]
SoundTypes['PasoArena2']=[SND_NOISYPC]
SoundTypes['PasoArena3']=[SND_NOISYPC]
SoundTypes['PasoArena4']=[SND_NOISYPC]
SoundTypes['PasoBarro1']=[SND_NOISYPC]
SoundTypes['PasoBarro2']=[SND_NOISYPC]
SoundTypes['PasoBarro3']=[SND_NOISYPC]
SoundTypes['PasoBarro4']=[SND_NOISYPC]
SoundTypes['PasoHierba4']=[SND_NOISYPC]
SoundTypes['PasoHierba3']=[SND_NOISYPC]
SoundTypes['PasoHierba2']=[SND_NOISYPC]
SoundTypes['PasoHierba1']=[SND_NOISYPC]
SoundTypes['PasoGrava1']=[SND_NOISYPC]
SoundTypes['PasoGrava2']=[SND_NOISYPC]
SoundTypes['PasoGrava3']=[SND_NOISYPC]
SoundTypes['PasoGrava4']=[SND_NOISYPC]
SoundTypes['PasoGrava5']=[SND_NOISYPC]
SoundTypes['PasoGrava6']=[SND_NOISYPC]
SoundTypes['PasoMaderaTablas1']=[SND_NOISYPC]
SoundTypes['PasoMaderaTablas2']=[SND_NOISYPC]
SoundTypes['PasoMaderaTablas3']=[SND_NOISYPC]
SoundTypes['PasoMaderaPodrida1']=[SND_NOISYPC]
SoundTypes['PasoMaderaPodrida2']=[SND_NOISYPC]
SoundTypes['PasoMaderaPodrida3']=[SND_NOISYPC]
SoundTypes['PasoMadera1']=[SND_NOISYPC]
SoundTypes['PasoMadera2']=[SND_NOISYPC]
SoundTypes['PasoMadera3']=[SND_NOISYPC]
SoundTypes['PasoMetal1']=[SND_NOISYPC]
SoundTypes['PasoMetal2']=[SND_NOISYPC]
SoundTypes['PasoMetal3']=[SND_NOISYPC]
SoundTypes['PasoMetal4']=[SND_NOISYPC]
SoundTypes['PasoNieve1']=[SND_NOISYPC]
SoundTypes['PasoNieve2']=[SND_NOISYPC]
SoundTypes['PasoNieve3']=[SND_NOISYPC]
SoundTypes['PasoNieve4']=[SND_NOISYPC]
SoundTypes['PasoPiedra1']=[SND_NOISYPC]
SoundTypes['PasoPiedra2']=[SND_NOISYPC]
SoundTypes['PasoPiedra3']=[SND_NOISYPC]
SoundTypes['PasoTierra1']=[SND_NOISYPC]
SoundTypes['PasoTierra2']=[SND_NOISYPC]
SoundTypes['PasoTierra3']=[SND_NOISYPC]
SoundTypes['PasoTierra4']=[SND_NOISYPC]
SoundTypes['SaltoInicioBarbaro']=[SND_NOISYPC]
SoundTypes['SaltoFinBarbaro']=[SND_NOISYPC]

# Gritos de ataque o herida (Battlecries or injuries of the PC)
SoundTypes['Caida1']=[SND_PC]
SoundTypes['Caida2']=[SND_PC]
SoundTypes['Caida3']=[SND_PC]
SoundTypes['Caida4']=[SND_PC]
SoundTypes['CambiarEscudo']=[SND_PC]
SoundTypes['EsfuerzoCortoAmz']=[SND_PC]
SoundTypes['EsfuerzoCorto1Amz']=[SND_PC]
SoundTypes['EsfuerzoCorto6Amz']=[SND_PC]
SoundTypes['EsfuerzoCorto3Amz']=[SND_PC]
SoundTypes['EsfuerzoCorto4Amz']=[SND_PC]
SoundTypes['EsfuerzoCorto5Amz']=[SND_PC]
SoundTypes['EsfuerzoGolpeFrontalAmz']=[SND_PC]
SoundTypes['EsfuerzoGolpeLateralAmz']=[SND_PC]
SoundTypes['EsfuerzoGolpeCabezaAmz']=[SND_PC]
SoundTypes['EsfuerzoGolpeAtrasAmz']=[SND_PC]
SoundTypes['EsfuerzoAmzMediano']=[SND_PC]
SoundTypes['EsfuerzoGolpeArribaAmz']=[SND_PC]
SoundTypes['EsfuerzoLargoBarbaro']=[SND_PC]
SoundTypes['EsfuerzoCorto1Barbaro']=[SND_PC]
SoundTypes['EsfuerzoCorto2Barbaro']=[SND_PC]
SoundTypes['EsfuerzoCorto3Barbaro']=[SND_PC]
SoundTypes['EsfuerzoCorto4Barbaro']=[SND_PC]
SoundTypes['EsfuerzoCorto5Barbaro']=[SND_PC]
SoundTypes['EsfuerzoCorto6Barbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeArribaBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeAtrasBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeFrontalBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeCabezaBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeLateralBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeLateralDchBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeAtrasBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeAtras1Barbaro']=[SND_PC]
SoundTypes['EsfuerzoBarbaroMediano']=[SND_PC]
SoundTypes['EsfuerzoBarbaroLargo']=[SND_PC]
SoundTypes['SaltoCortoBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeAtrasBarbaro']=[SND_PC]
SoundTypes['EsfuerzoGolpeAtrasBarbaro']=[SND_PC]
SoundTypes['EsfuerzoCortoDwf']=[SND_PC]
SoundTypes['EsfuerzoCorto1Dwf']=[SND_PC]
SoundTypes['EsfuerzoCorto2Dwf']=[SND_PC]
SoundTypes['EsfuerzoCorto3Dwf']=[SND_PC]
SoundTypes['EsfuerzoCorto4Dwf']=[SND_PC]
SoundTypes['EsfuerzoCorto5Dwf']=[SND_PC]
SoundTypes['EsfuerzoCorto6Dwf']=[SND_PC]
SoundTypes['EsfuerzoGolpeFrontalDwf']=[SND_PC]
SoundTypes['EsfuerzoGolpeLateralDwf']=[SND_PC]
SoundTypes['EsfuerzoGolpeCabezaDwf']=[SND_PC]
SoundTypes['EsfuerzoGolpeAtrasDwf']=[SND_PC]
SoundTypes['EsfuerzoDwfMediano']=[SND_PC]
SoundTypes['EsfuerzoGolpeArribaDwf']=[SND_PC]
SoundTypes['SaltoCortoDwf']=[SND_PC]

SoundTypes['Enfundar']=[SND_PC]
SoundTypes['EnfundarAmz']=[SND_PC]
#SoundTypes['MuerteBarbaro1']=[SND_PC]
#SoundTypes['MuerteBarbaro2']=[SND_PC]
#SoundTypes['MuerteBarbaro3']=[SND_PC]
#SoundTypes['MuerteBarbaro4']=[SND_PC]
#SoundTypes['HeridaBarbaro1']=[SND_PC]
#SoundTypes['HeridaBarbaro2']=[SND_PC]
#SoundTypes['HeridaBarbaro3']=[SND_PC]


# Battlecries?

######################################
# Take Tables (Please complete these lists, these are just examples)

# Take object Flags
OBJ_NONE =-1		#no item
OBJ_ITEM =0			#items
OBJ_SHIELD =1		#shields
OBJ_WEAPON =2		#weapons
OBJ_QUIVER =3		#carcaj
OBJ_STANDARD =4
OBJ_KEY =5
OBJ_SPECIALKEY =6
OBJ_USEME =7		#automatics
OBJ_BOW =8
OBJ_ARROW =9
OBJ_TABLET =10
OBJ_ARMOUR =11


#King of weapon (1handed , 2handed swords , 2handed axe....)
W_FLAG_1H=0     #One handed _whatever_ weapon
W_FLAG_2W=1	   #Two handed sword
W_FLAG_AXE=2	#Two handed axw
W_FLAG_SP=3		#Two handed spear



# Throw Type flags
THR_SPINNING=0
THR_STRAIGHT=1

EntitiesObjectData={}

# Default Object Table                   (Type        DamF  DefF)
DefaultObjectData={}                     #########################

#items
DefaultObjectData['Fetiche']=            [OBJ_ITEM]
DefaultObjectData['Orbe']=               [OBJ_ITEM]

DefaultObjectData['Pocima100']=          [OBJ_ITEM]
DefaultObjectData['Pocima200']=          [OBJ_ITEM]
DefaultObjectData['PocimaTodo']=         [OBJ_ITEM]
DefaultObjectData['BotellaSagrada'] =    [OBJ_ITEM]
DefaultObjectData['PowerPotion']=        [OBJ_ITEM]

DefaultObjectData['Pocima25']=           [OBJ_USEME]
DefaultObjectData['Pocima50']=           [OBJ_USEME]

DefaultObjectData['Llavero']=            [OBJ_ITEM]
DefaultObjectData['Brazalete']=          [OBJ_ITEM]
DefaultObjectData['Amuleto']=            [OBJ_ITEM]
DefaultObjectData['Corona']=             [OBJ_ITEM]
DefaultObjectData['Amuletoserpiente']=   [OBJ_ITEM]
DefaultObjectData['Medallion']=          [OBJ_ITEM]
DefaultObjectData['Amuletofantasma']=    [OBJ_ITEM]
DefaultObjectData['Gemaroja']=           [OBJ_ITEM]
DefaultObjectData['Gemaazul']=           [OBJ_ITEM]
DefaultObjectData['Gemapurpura']=        [OBJ_ITEM]
DefaultObjectData['Gema']=               [OBJ_ITEM]
DefaultObjectData['Pergamino2']=         [OBJ_ITEM]

#shields   

GolpeArmaEscudoMetal=Bladex.CreateSound('../../Sounds/golpe-arma-escudo.wav', 'GolpeArmaEscudoMetal')
GolpeArmaEscudoMetal.SendNotify=1
GolpeArmaEscudoMadera=Bladex.CreateSound('../../Sounds/WoodShield-impact.wav', 'GolpeArmaEscudoMadera')
GolpeArmaEscudoMadera.SendNotify=1

# Use unique sounds for weapon parries?
GolpeArmaArmaMetal=Bladex.CreateSound('../../Sounds/golpe-arma-arma.wav', 'GolpeArmaArmaMetal')
GolpeArmaArmaMetal.SendNotify=1
# GolpeArmaArmaMadera=Bladex.CreateSound('../../Sounds/golpe-arma-arma.wav', 'GolpeArmaArmaMadera')
# GolpeArmaArmaMadera.SendNotify=1

###
#      - - - Titanium specific stuff - - - 
# Some of these flags are kept here so that they can be referenced in other modules as a single point of contact
# and don't need to manually change all other modules
###

PlayerKinds              = ["Barbarian_N", "Knight_N", "Amazon_N", "Dwarf_N" ]

blood_SparkEntities      = ["Golem_metal","ChaosKnight"]
blood_DustDeathEntities  = ["Skeleton","Lich","Golem_stone","Golem_clay","Golem_lava","Golem_ice","Knight_Zombie"]+blood_SparkEntities
blood_GreenBleedEntities = ["Spidersmall"]
blood_GreyBleedEntities  = ["Lich"]

### Weapon kinds specific to characters moved here
UniWeaps = [    "QueenSword" ]

KgtWeaps = [	"IceSword","FireSword","Gladius","Espadaelfica",
							"Espadaromana","Espadacurva","Dagesse","Cimitarra","Espadafilo",
							"Espada","Maza","Maza2","Maza3","HookSword","DoubleSword"]

DwfWeaps = [	"CrushHammer","FireAxe","IceHammer","Hacha","Hacha5","Hacha4","Hacha3",
							"Hacha6","Hacha2","Garrote","Martillo","Martillo2","Garropin","MazaDoble",
							"Garrote2","Martillo3"]

AmzWeaps = [	"SteelFeather","FireBo","IceWand","LanzaAncha","Bichero",
							"Bo","Lanza","Naginata","Tridente","Arpon","Axpear","Crosspear",
							"Hachacuchilla","Naginata2","DeathBo","CrushBo"]

BarWeaps  = [	"FireBigSword","IceAxe","Chaosword",
							"DeathSword","LongSword","Alfanje","BigSword","SawSword","FlatSword",
							"Eclipse","Guadanya","Hacha2hojas","RhinoClub","Hacharrajada"]


##########################################################################################################
#
#	(2b completed)
#
#	0 - OBJ_SHIELD
#	1 - ATTACK
#	2 - DEFENSE
#	3 - Sound used
#	4 - angle of circumference covered (cone)
#       5 - Height
#       6 - Radius
#	7 - Max damage it can stand b4 being break
# 8 - Friendly name
#
#-----------------------------------------------------
#
#
#	0 - OBJ_WEAPON
#	1 - ?
#	2 - ?
#	3 - ?
#	4 - ?
#	5 - (5a,5b,5c,5d,5e)
#		5a ->W_FLAG_1H/W_FLAG_2W/W_FLAG_AXE/W_FLAG_SP
#		5b ->Cone for shield ( not needed in .._1H)
#		5c ->Height
#		5d ->Radius
#		5e ->Defence ( like [5] in OBJ_SHIELD)
#		5f ->Max standing damage (like [7] in OBJ_SHIELD)
#		5g ->Sound when hit
#
#	7 - Max damaga it can stand b4 being break
#
#
#
#   0 - OBJ_ARMOUR
#   1 - Tipo personaje(mirar ejemplos...)
#   2 - Level. VAlores:
#       1-> Arm Ligera
#       2-> Arm media
#       3-> Arm pesada
#
#	3- Factor to be added to the CharDefenseData
#
#
#
##########################################################################################################
"""
Escudo vampiro	42.33º
kingshield	56.68º
Escudo dalgurak	62.84
Escudo 9	64.5
Escudo 8	69.63
Escudo 7	47.16
Escudo 6	37.03
Escudo 5	30.73
Escudo 4	46.2
Escudo 3	38.1
Escudo 2	50.86
Escudo 1	40.26
"""
DEG2RADS= TWOPI/360.0



DefaultObjectData['ArmaduraAmazonaLigera']=     [OBJ_ARMOUR,  "Amz", 1 , 25]
DefaultObjectData['ArmaduraBarbaroLigera']=     [OBJ_ARMOUR,  "Bar", 1 , 25]
DefaultObjectData['ArmaduraCaballeroLigera']=   [OBJ_ARMOUR,  "Kgt", 1 , 10]
DefaultObjectData['ArmaduraCaballeroMedia']=    [OBJ_ARMOUR,  "Kgt", 2 , 40]
DefaultObjectData['ArmaduraCaballeroCompleta']= [OBJ_ARMOUR,  "Kgt", 3 , 80]
DefaultObjectData['ArmaduraEnanoLigera']=       [OBJ_ARMOUR,  "Dwf", 1 , 15]
DefaultObjectData['ArmaduraEnanoMedia']=        [OBJ_ARMOUR,  "Dwf", 2 , 35]

#                 #bod                    #type      #POW #RES  #Sound              #cone             #height #rad #Brk
DefaultObjectData['Escudo1']=            [OBJ_SHIELD,   0, 300, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  6]
DefaultObjectData['Escudo2']=            [OBJ_SHIELD,   0,  80, GolpeArmaEscudoMadera,180.0*DEG2RADS,   2000,  750,  3]
DefaultObjectData['Escudo3']=            [OBJ_SHIELD,-1.2,4000, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  7]
DefaultObjectData['Escudo4']=            [OBJ_SHIELD,   0,2500, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  5]
DefaultObjectData['Escudo5']=            [OBJ_SHIELD,   0,  20, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  5]
DefaultObjectData['Escudo6']=            [OBJ_SHIELD,-1.5,8000, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  5]
DefaultObjectData['Escudo7']=            [OBJ_SHIELD,-0.5,5000, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  5]
DefaultObjectData['Escudo8']=            [OBJ_SHIELD,-0.5,3000, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750, 10]
DefaultObjectData['Escudo9']=            [OBJ_SHIELD,  -1,2000, GolpeArmaEscudoMadera,180.0*DEG2RADS,   2000,  750, 10]     # Was GolpeArmaEscudoMetal  -LeadHead
DefaultObjectData['Escudon']=            [OBJ_SHIELD,-0.5,  30, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   3000, 1250, 10]     # PLAGUE: because it's just 30RES, the shield breaks immediately
DefaultObjectData['VampShield']=         [OBJ_SHIELD,-0.5,1500, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750, 10]
DefaultObjectData['DalShield']=          [OBJ_SHIELD,-1.5,5000, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  0]
DefaultObjectData['KingShield']=         [OBJ_SHIELD,   1,1000, GolpeArmaEscudoMetal, 180.0*DEG2RADS,   2000,  750,  6]
DefaultObjectData['MagicShield']=        [OBJ_SHIELD,-0.5,6000, GolpeArmaEscudoMetal, 360.0*DEG2RADS,   2000, 1500,6000]

#                                                             THROWING
#weapons          name                    type        dam,def, bonus, type

# Naturally attacking races
DefaultObjectData['Cos']=                [OBJ_WEAPON,   3,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Lich']=               [OBJ_WEAPON,   4,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Knight_Zombie']=      [OBJ_WEAPON,   4,  0, 1.0,  THR_SPINNING, []]  # Added -LeadHead
DefaultObjectData['Spidersmall']=        [OBJ_WEAPON,   2,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Little_Demon']=       [OBJ_WEAPON,   8,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Salamander']=         [OBJ_WEAPON,  55,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Great_Demon']=        [OBJ_WEAPON,1000,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['DarkLord']=           [OBJ_WEAPON,  40,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Golem_stone']=        [OBJ_WEAPON,  55,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Golem_clay']=         [OBJ_WEAPON,  55,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Golem_lava']=         [OBJ_WEAPON,  55,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Golem_metal']=        [OBJ_WEAPON,  55,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Golem_ice']=          [OBJ_WEAPON,  55,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Knight_N']=           [OBJ_WEAPON,   0,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Barbarian_N']=        [OBJ_WEAPON,   0,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Amazon_N']=           [OBJ_WEAPON,   0,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['Dwarf_N']=            [OBJ_WEAPON,   0,  0, 1.0,  THR_SPINNING, []]

#
#specials
#
DefaultObjectData['Entity ElectricBolt']=[OBJ_WEAPON,    0,  0, 1.0,  THR_STRAIGHT, [], ['Electric', +50.0]]
DefaultObjectData['Meteorito']=          [OBJ_WEAPON, 1000,  0, 1.0,  THR_STRAIGHT, [], ['Fire', +500.0]]
DefaultObjectData['EsferaNegraAhk']=     [OBJ_WEAPON,  500,  0, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['BolaRayos']=          [OBJ_WEAPON, 2000,  0, 1.0,  THR_STRAIGHT, []]

DefaultObjectData['EsferaNegra']=        [OBJ_WEAPON,  100,  0, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['BolaDalGurak']=       [OBJ_WEAPON,  500,  0, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['EsferaOrbital']=      [OBJ_WEAPON,  500,  0, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['HalfmoonTrail']=      [OBJ_WEAPON, 5000,  0, 1.0,  THR_SPINNING, []]
DefaultObjectData['FireRing']=           [OBJ_WEAPON,    0,  0, 1.0,  THR_SPINNING, [], ['Fire', +500.0]]



#######  ARMAS  #######




# ARMAS DEL BARBARO
#                 #bod                    #type      #POW #RES #throw_mult #throw_type #flag #cone#hght#rad#def#Brk#Sound
DefaultObjectData['FireBigSword']=       [OBJ_WEAPON, 50, -15, 1.5,  THR_SPINNING, [W_FLAG_2W,PI,2000,750,20000,20000,GolpeArmaEscudoMetal], ["Fire", +10.0]]
DefaultObjectData['IceAxe']=             [OBJ_WEAPON, 30, -10, 2.0,  THR_SPINNING, [W_FLAG_AXE,PI,2000,750,4000,4000,GolpeArmaEscudoMetal], ["Ice", +10.0]]
DefaultObjectData['DalWeapon']=          [OBJ_WEAPON,140,   0, 1.0,  THR_SPINNING, [W_FLAG_1H,],["Venom",+6.0]]
DefaultObjectData['DalBlade']=           [OBJ_WEAPON,800,   0, 2.0,  THR_SPINNING, [W_FLAG_1H,]]

DefaultObjectData['Sablazo']=            [OBJ_WEAPON, 20,   0, 2.0,  THR_SPINNING, [W_FLAG_1H,]]

DefaultObjectData['Chaosword']=          [OBJ_WEAPON,  5,   0, 2.0,  THR_STRAIGHT, [W_FLAG_2W,PI,2000,750,100,100,GolpeArmaEscudoMetal]]
DefaultObjectData['DeathSword']=         [OBJ_WEAPON, 40, -10, 2.5,  THR_SPINNING, [W_FLAG_2W,PI,2000,750,500,1000,GolpeArmaEscudoMetal]]
DefaultObjectData['LongSword']=          [OBJ_WEAPON, 80, -15, 2.0,  THR_SPINNING, [W_FLAG_2W,PI,2000,750,1000,4000,GolpeArmaEscudoMetal]]
DefaultObjectData['Alfanje']=            [OBJ_WEAPON,100, -40, 2.8,  THR_SPINNING, [W_FLAG_2W,PI,2000,750,3000,6000,GolpeArmaEscudoMetal]]
DefaultObjectData['BigSword']=           [OBJ_WEAPON,220, -70, 2.5,  THR_SPINNING, [W_FLAG_2W,PI,2000,750,10000,10000,GolpeArmaEscudoMetal]]
DefaultObjectData['SawSword']=           [OBJ_WEAPON,800, -100, 1.0,  THR_SPINNING, [W_FLAG_2W,PI,2000,750,16000,16000,GolpeArmaEscudoMetal]]
DefaultObjectData['FlatSword']=          [OBJ_WEAPON,180, -50, 1.0,  THR_SPINNING, [W_FLAG_2W,PI,2000,750,9000,9000,GolpeArmaEscudoMetal]]

DefaultObjectData['Eclipse']=            [OBJ_WEAPON, 20, -5, 3.0,  THR_SPINNING, [W_FLAG_AXE,PI,2000,750,400,400,GolpeArmaEscudoMetal]]
DefaultObjectData['Guadanya']=           [OBJ_WEAPON, 60, -20, 1.3,  THR_SPINNING, [W_FLAG_AXE,PI,2000,750,2000,2000,GolpeArmaEscudoMetal]]
DefaultObjectData['Hacha2hojas']=        [OBJ_WEAPON,140, -60, 4.0,  THR_SPINNING, [W_FLAG_AXE,PI,2000,750,8000,8000,GolpeArmaEscudoMetal]]
DefaultObjectData['RhinoClub']=          [OBJ_WEAPON,300, -80, 4.0,  THR_SPINNING, [W_FLAG_AXE,PI,2000,750,12000,12000,GolpeArmaEscudoMadera]]  # Was GolpeArmaEscudoMetal
DefaultObjectData['Hacharrajada']=       [OBJ_WEAPON,500, -120, 4.0,  THR_SPINNING, [W_FLAG_AXE,PI,2000,750,14000,14000,GolpeArmaEscudoMetal]]


# ARMAS DEL ENANO

DefaultObjectData['CrushHammer']=   	 [OBJ_WEAPON, 50,  -90, 2.8,  THR_SPINNING, [W_FLAG_1H,],["Venom",+1.0]]
DefaultObjectData['FireAxe']=            [OBJ_WEAPON, 40, -100, 3.5,  THR_SPINNING, [W_FLAG_1H,], ["Fire", +10.0]]
DefaultObjectData['IceHammer']=          [OBJ_WEAPON, 25,  -50, 3.0,  THR_SPINNING, [W_FLAG_1H,], ["Ice", +10.0]]

DefaultObjectData['Hacha']=              [OBJ_WEAPON,  4,   0, 2.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Hacha5']=             [OBJ_WEAPON, 18, -10, 2.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Hacha4']=             [OBJ_WEAPON, 55, -40, 2.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Hacha3']=             [OBJ_WEAPON, 75, -45, 2.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Hacha6']=             [OBJ_WEAPON,290, -50, 2.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Hacha2']=             [OBJ_WEAPON,480, -85, 2.5,  THR_SPINNING, [W_FLAG_1H,]]

DefaultObjectData['Garrote']=            [OBJ_WEAPON,  2,   0, 2.3,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Martillo']=           [OBJ_WEAPON, 95, -30, 2.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Martillo2']=          [OBJ_WEAPON,135, -35, 2.8,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Garropin']=           [OBJ_WEAPON, 45, -30, 2.8,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['MazaDoble']=          [OBJ_WEAPON,200, -60, 2.8,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Garrote2']=           [OBJ_WEAPON,175, -50, 2.8,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Martillo3']=          [OBJ_WEAPON,790, -160, 3.0,  THR_SPINNING, [W_FLAG_1H,]]


# ARMAS DEL CABALLERO

DefaultObjectData['QueenSword']=         [OBJ_WEAPON, 85, -35, 2.4,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['IceSword']=           [OBJ_WEAPON, 45, -15, 4.0,  THR_SPINNING, [W_FLAG_1H,], ["Ice", +10.0]]
DefaultObjectData['FireSword']=          [OBJ_WEAPON, 35, -25, 3.3,  THR_SPINNING, [W_FLAG_1H,], ["Fire", +10.0]]

DefaultObjectData['Gladius']=            [OBJ_WEAPON,  3,   0, 2.2,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Orksword']=           [OBJ_WEAPON, 30,   0, 2.3,  THR_SPINNING, [W_FLAG_1H,],["Venom",+1.0]]
DefaultObjectData['Espadaelfica']=       [OBJ_WEAPON, 50, -25, 2.4,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Espadaromana']=       [OBJ_WEAPON, 35, -20, 2.4,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Espadacurva']=        [OBJ_WEAPON,120, -25, 2.2,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Dagesse']=            [OBJ_WEAPON,150, -30, 2.4,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Cimitarra']=          [OBJ_WEAPON,210, -45, 2.3,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['EgyptSword']=         [OBJ_WEAPON,100,   0, 2.3,  THR_SPINNING, [W_FLAG_1H,],["Venom",+4.0]]
DefaultObjectData['Espadafilo']=         [OBJ_WEAPON,470, -50, 2.3,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Espada']=             [OBJ_WEAPON,780, -80, 2.5,  THR_SPINNING, [W_FLAG_1H,]]

DefaultObjectData['Maza']=               [OBJ_WEAPON, 15,  -5, 2.2,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Maza2']=              [OBJ_WEAPON, 70, -30, 2.3,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Maza3']=              [OBJ_WEAPON,290, -55, 2.4,  THR_SPINNING, [W_FLAG_1H,]]


# ARMAS DE LA AMAZONA

DefaultObjectData['IceWand']=            [OBJ_WEAPON, 30, -20, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,3500,3500,GolpeArmaEscudoMetal], ["Ice", +10.0]]
DefaultObjectData['SteelFeather']=       [OBJ_WEAPON, 60, -50, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,5500,5500,GolpeArmaEscudoMetal],["Venom",+1.0]]
DefaultObjectData['FireBo']=             [OBJ_WEAPON, 50, -30, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,4500,4500,GolpeArmaEscudoMetal],["Fire", +10.0]]


DefaultObjectData['Bo']=                 [OBJ_WEAPON,  3,   0, 2.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,100,100,GolpeArmaEscudoMadera]]  # Was GolpeArmaEscudoMetal
DefaultObjectData['Lanza']=              [OBJ_WEAPON, 35, -10, 2.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,600,600,GolpeArmaEscudoMetal]]
DefaultObjectData['Naginata']=           [OBJ_WEAPON, 50, -20, 2.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,2000,2000,GolpeArmaEscudoMetal]]
DefaultObjectData['Tridente']=           [OBJ_WEAPON, 75, -30, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,4000,4000,GolpeArmaEscudoMetal]]
DefaultObjectData['Hachacuchilla']=      [OBJ_WEAPON,215, -50, 2.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,9000,9000,GolpeArmaEscudoMetal]]
DefaultObjectData['Naginata2']=          [OBJ_WEAPON,490, -80, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,14000,14000,GolpeArmaEscudoMetal]]
DefaultObjectData['DeathBo']=            [OBJ_WEAPON,130, -35, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,7000,7000,GolpeArmaEscudoMetal]]
DefaultObjectData['CrushBo']=            [OBJ_WEAPON,300, -60, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,10000,10000,GolpeArmaEscudoMetal]]
DefaultObjectData['LanzaAncha']=         [OBJ_WEAPON,760, -90, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,16000,16000,GolpeArmaEscudoMetal]]
DefaultObjectData['Axpear']=             [OBJ_WEAPON, 95, -40, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,6000,6000,GolpeArmaEscudoMetal]]
DefaultObjectData['Arpon']=              [OBJ_WEAPON,390, -70, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,12000,12000,GolpeArmaEscudoMetal]]
DefaultObjectData['Bichero']=            [OBJ_WEAPON, 16,  -5, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,400,400,GolpeArmaEscudoMadera]]  # Was GolpeArmaEscudoMetal
DefaultObjectData['Crosspear']=          [OBJ_WEAPON,160, -45, 3.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,8000,8000,GolpeArmaEscudoMetal]]


######## Armas descartadas de la Amazona

DefaultObjectData['DeathKatar']=         [OBJ_WEAPON, 25, -10, 1.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Chakram']=            [OBJ_WEAPON,200,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Katarmoon']=          [OBJ_WEAPON, 30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Chakram2']=           [OBJ_WEAPON,200,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Katar']=              [OBJ_WEAPON, 30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['KatarDoble']=         [OBJ_WEAPON, 30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['TaiSword']=           [OBJ_WEAPON,500,   0, 3.0,  THR_SPINNING, [W_FLAG_1H,], ["Ice", +10.0]]
DefaultObjectData['LightEdge']=          [OBJ_WEAPON, 90,  -2, 1.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Ninjato']=            [OBJ_WEAPON, 50,   0, 1.5,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['HookSword']=          [OBJ_WEAPON, 90, -25, 2.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Katana']=             [OBJ_WEAPON,240,  -1, 2.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['DoubleSword']=        [OBJ_WEAPON,380, -60, 1.5,  THR_SPINNING, [W_FLAG_1H,]]



######### ARMAS MAGICAS

DefaultObjectData['Varita7']=            [OBJ_STANDARD,  30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Varita6']=            [OBJ_STANDARD,  30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Varita5']=            [OBJ_STANDARD,  30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Varita2']=            [OBJ_STANDARD,  30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Varita1']=            [OBJ_STANDARD,  30,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['EspadaMagica1']=      [OBJ_STANDARD,  40, -15, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['EspadaMagica2']=      [OBJ_STANDARD,  45, -20, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['EspadaMagica3']=      [OBJ_STANDARD,  50, -25, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['VampWeapon']=         [OBJ_STANDARD,  90,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,], ['Drain']]
DefaultObjectData['Baston3']=            [OBJ_STANDARD, 100,  -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]



######### ARMAS DE ATAQUE A DISTANCIA


DefaultObjectData['Arco']=               [OBJ_BOW,        5, -5, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['Arco3']=              [OBJ_BOW,       10, -5, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['Arco2']=              [OBJ_BOW,       20, -5, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['Arco_Amz_seleccion']= [OBJ_BOW,       20, -5, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['Flecha']=             [OBJ_ARROW,    100, -5, 1.0,  THR_STRAIGHT, []]
DefaultObjectData['FlechaEnvenenada']=   [OBJ_ARROW,    100, -5, 1.0,  THR_STRAIGHT, [], ["Venom",+5.0]]
DefaultObjectData['FlechaFuego']=        [OBJ_ARROW,    100, -5, 1.0,  THR_STRAIGHT, [], ["Fire", +200.0]]
DefaultObjectData['Suriken']=            [OBJ_STANDARD,  20,  0, 2.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Dagarrojar']=         [OBJ_STANDARD,  30,  0, 2.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Canica']=             [OBJ_STANDARD,  30,  0, 2.0,  THR_SPINNING, [W_FLAG_1H,]]



######### ARMAS COMUNES DE MAL USO


DefaultObjectData['Daga']=               [OBJ_STANDARD,   6,  0, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Cuchillo']=           [OBJ_STANDARD,   5,  0, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Alabarda']=           [OBJ_STANDARD,   8,-25, 1.0,  THR_SPINNING, [W_FLAG_1H,]]



######### ARMAS SAGRADAS


DefaultObjectData['BladeSword']=          [OBJ_WEAPON, 300, -5, 1.0,  THR_STRAIGHT, [W_FLAG_1H,]]
DefaultObjectData['BladeSword2']=         [OBJ_WEAPON, 300, -5, 1.0,  THR_STRAIGHT, [W_FLAG_1H,], ["Light", +300.0]]
DefaultObjectData['BladeSwordBarbarian'] =[OBJ_WEAPON, 300, -5, 1.0,  THR_STRAIGHT, [W_FLAG_2W,PI,2000,750,50000,0,GolpeArmaEscudoMetal]]
DefaultObjectData['BladeSword2Barbarian']=[OBJ_WEAPON, 300, -5, 1.0,  THR_STRAIGHT, [W_FLAG_2W,PI,2000,750,50000,0,GolpeArmaEscudoMetal], ["Light", +300.0]]

DefaultObjectData['Phurbhu']=             [OBJ_STANDARD, 85, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]



######### ARMAS INUTILIZABLES


DefaultObjectData['KingSword']=          [OBJ_WEAPON, 100, 0, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Espadon']=            [OBJ_WEAPON,  60, 0, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Mazapiedra']=         [OBJ_WEAPON, 500, 0, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Hachacarnicero']=     [OBJ_WEAPON, 150, 0, 1.0,  THR_SPINNING, [W_FLAG_1H,]]









# Objetos hirientes


DefaultObjectData['CuchillaFernando']=   [OBJ_WEAPON,9000, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Pendulo']=            [OBJ_WEAPON,9000, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['PinchoManuel']=       [OBJ_WEAPON,9000, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['PinchoMiguel']=       [OBJ_WEAPON,9000, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Pivote']=             [OBJ_WEAPON,  20, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]
DefaultObjectData['Pivote2']=            [OBJ_WEAPON,  60, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]                        # Added
DefaultObjectData['PivoteEnvenenado']=   [OBJ_WEAPON,  60, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,], ["Venom",+20.0]]       #   -LeadHead
DefaultObjectData['Roca1Aurelio']=       [OBJ_WEAPON,  35, -5, 1.0,  THR_SPINNING, [W_FLAG_1H,]]


#Quiver
#weapons          name                    type        #   type
DefaultObjectData['Carcaj']=             [OBJ_QUIVER, 10, "Flecha"]
DefaultObjectData['CarcajFuego']=        [OBJ_QUIVER, 10, "FlechaFuego"]
DefaultObjectData['CarcajEnvenenado']=   [OBJ_QUIVER, 10, "FlechaEnvenenada"]

# Quiver variations
DefaultObjectData['Carcaj_E']=           DefaultObjectData['Carcaj']
DefaultObjectData['Carcaj1']=            DefaultObjectData['Carcaj']
DefaultObjectData['Carcaj2']=            DefaultObjectData['Carcaj']
DefaultObjectData['CarcajFuego_E']=      DefaultObjectData['CarcajFuego']
DefaultObjectData['CarcajFuego1']=       DefaultObjectData['CarcajFuego']
DefaultObjectData['CarcajFuego2']=       DefaultObjectData['CarcajFuego']
DefaultObjectData['CarcajEnvenenado_E']= DefaultObjectData['CarcajEnvenenado']
DefaultObjectData['CarcajEnvenenado1'] = DefaultObjectData['CarcajEnvenenado']
DefaultObjectData['CarcajEnvenenado2']=  DefaultObjectData['CarcajEnvenenado']


# Non inventoriable weapons (classified as standard objects)

DefaultObjectData['Cincel']=             [OBJ_STANDARD,  2, 0, 2.0,  THR_STRAIGHT, []]
DefaultObjectData['Estaca']=             [OBJ_STANDARD,  4, 0, 2.0,  THR_STRAIGHT, []]
DefaultObjectData['MartilloForja']=      [OBJ_STANDARD,  5, 0, 2.0,  THR_STRAIGHT, []]
DefaultObjectData['Pala']=               [OBJ_STANDARD, 10, 0, 2.0,  THR_STRAIGHT, []]
DefaultObjectData['Pico']=               [OBJ_STANDARD, 20, 0, 2.0,  THR_STRAIGHT, []]



# standard objects
DefaultObjectData['Antorcha']=           [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['AntorchaFuego']=      [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, [], ["Fire", +5.0]]
DefaultObjectData['Bandeja']=            [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Bloodbol']=           [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Botella']=            [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['BotellaVerde']=       [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Caliz']=              [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Candelpeque']=        [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Candil']=             [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Cantimplora']=        [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Cazo']=               [OBJ_STANDARD,   4, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Cojin']=              [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Costilla']=           [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Cracorn1']=           [OBJ_STANDARD,   5, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Cracorn2']=           [OBJ_STANDARD,   5, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['CraneoCornudo3']=     [OBJ_STANDARD,   5, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['CraneoCornudo4']=     [OBJ_STANDARD,   5, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Cubo']=               [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Farol']=              [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Farol2']=             [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Femur']=              [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Jarra']=              [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Jarrita']=            [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Libro']=              [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Libro2']=             [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Libro3']=             [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Libroabierto']=       [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Mortero']=            [OBJ_STANDARD,   3, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Palangana']=          [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Pergamino']=          [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Silla']=              [OBJ_STANDARD,   5, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Skull']=              [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Tabla_xl']=           [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Tabla_l']=            [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Tabla_rota']=         [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Taburete']=           [OBJ_STANDARD,   3, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Tacita']=             [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Tintero']=            [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Tronco']=             [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['TroncoNevado']=       [OBJ_STANDARD,   2, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Velon']=              [OBJ_STANDARD,   1, 0, 2.0,  THR_SPINNING, []]
DefaultObjectData['Limb']=               [OBJ_STANDARD,   3, 0, 2.0,  THR_SPINNING, []]

# Golem stones
DefaultObjectData['Piedra_Glm_st']=      [OBJ_STANDARD,  300, -5, 1.0,  THR_SPINNING, []]
DefaultObjectData['Piedra_Glm_mt']=      [OBJ_STANDARD,  400, -5, 1.0,  THR_SPINNING, []]
DefaultObjectData['Piedra_Glm_lv']=      [OBJ_STANDARD,  500, -5, 1.0,  THR_SPINNING, []]
DefaultObjectData['Piedra_Glm_cl']=      [OBJ_STANDARD,  200, -5, 1.0,  THR_SPINNING, []]
DefaultObjectData['Piedra_Glm_ic']=      [OBJ_STANDARD,  300, -5, 1.0,  THR_SPINNING, []]


#keys
DefaultObjectData['Llave']=              [OBJ_KEY]
DefaultObjectData['Llavecobox']=         [OBJ_KEY]
DefaultObjectData['Llavecutre']=         [OBJ_KEY]
DefaultObjectData['Llavemaz']=           [OBJ_KEY]
DefaultObjectData['Llavecob']   =        [OBJ_KEY]
DefaultObjectData['Llavedor']   =        [OBJ_KEY]
DefaultObjectData['Llavepla']   =        [OBJ_KEY]

#Specialkeys
DefaultObjectData['LlaveBlanca']=        [OBJ_SPECIALKEY]
DefaultObjectData['LlaveAzul']  =        [OBJ_SPECIALKEY]
DefaultObjectData['LlaveAmarilla']  =    [OBJ_SPECIALKEY]
DefaultObjectData['LlaveNegra']     =    [OBJ_SPECIALKEY]

#Automatics
DefaultObjectData['Casco3']=             [OBJ_USEME]
DefaultObjectData['Casco4']=             [OBJ_USEME]
DefaultObjectData['Casco5']=             [OBJ_USEME]
DefaultObjectData['CascoBlade']=         [OBJ_USEME]
DefaultObjectData['Coraza1']=            [OBJ_USEME]
DefaultObjectData['Coraza2']=            [OBJ_USEME]
DefaultObjectData['Coraza3']=            [OBJ_USEME]
DefaultObjectData['CorazaBlade']=        [OBJ_USEME]
DefaultObjectData['Hogaza']=             [OBJ_USEME]
DefaultObjectData['Manzana']=            [OBJ_USEME]
DefaultObjectData['Paletilla']=          [OBJ_USEME]
DefaultObjectData['Queso']=              [OBJ_USEME]
DefaultObjectData['Seta']=               [OBJ_USEME]
DefaultObjectData['Setas']=              [OBJ_USEME]
DefaultObjectData['Rabano']=             [OBJ_USEME]
DefaultObjectData['Saquito']=            [OBJ_USEME]
DefaultObjectData['Raiz']=               [OBJ_USEME]

#Tablets
DefaultObjectData['Tablilla1']=          [OBJ_TABLET]
DefaultObjectData['Tablilla2']=          [OBJ_TABLET]
DefaultObjectData['Tablilla3']=          [OBJ_TABLET]
DefaultObjectData['Tablilla4']=          [OBJ_TABLET]
DefaultObjectData['Tablilla5']=          [OBJ_TABLET]
DefaultObjectData['Tablilla6']=          [OBJ_TABLET]

DefaultSelectionData={}
EntitiesSelectionData={}

EnemiesScorerData={}
EnemiesDefaultScorerData={}
######################################

def GetObjectFriendlyName(obj_name):
	try:
		return DefaultSelectionData[obj_name][2]
	except:
		return "No Name"


######################################
# Throw Tables

# Throw Times (how long you can hold a key in seconds)
THROW_TIME_MIN = 0.4
THROW_TIME_MAX = 1.0

# Mass Categories
LightMassMax = 2.9
ImpaleMassMax = 2.65

MaxStrikeDict={	'Chaosword'				: [],
				'Gladius'				: [],
				'Cimitarra'				: [],
				'Espadacurva'			: [],
				'Espada'				: [],
				'Espadaelfica'			: [],
				'Espadafilo'			: [],
				'Espadaromana'			: [],
				'EspadaMagica1'			: [],
				'EspadaMagica2'			: [],
				'Ninjato'				: [],
				'Katana'				: [],
				'EspadaMagica3'			: [],
				'Hacha'					: [],
				'Hacha2'				: [],
				'Hacha3'				: [],
				'Hacha4'				: [],
				'Hacha5'				: [],
				'Hacha6'				: [],
				'Hachacuchilla'			: [],
				'Garrote'				: [],
				'Maza'					: [],
				'Maza2'					: [],
				'Maza3'					: [],
				'Martillo'				: [],
				'Martillo2'				: []}


MedStrikeDict={ 'Garropin'				: [],
				'Garrote2'				: []}


# Please check (and add stone to end, I don't know which stones)
MinStrikeDict={ 'Alabarda'				: [],
				'Baston3'				: [],
				'Lanza'					: [],
				'Naginata'				: [],
				'Tridente'				: [],
				'Varilla'				: [],
				'Varita1'				: [],
				'Varita2'				: [],
				'Varita2'				: [],
				'Varita5'				: [],
				'Varita6'				: [],
				'Varita7'				: [],
				'Mortero'				: [],
				'Skull'					: [],
				'Palangana'				: [],
				'BotellaVerde'			: [],
				'Taburete'				: [],
				'Cubo'					: [],
				'Farol'					: [],
				'Candil'				: [],
				'Libro'					: [],
				'Mortero'				: [],
				'Cuchillo'				: [],
				'Daga'					: [],
				'Tintero'				: [],
				'Velon'					: [],
				'Bloodbol'				: [],
				'Candelpeque'			: [],
				'Tronco'				: [],
				'Cracorn1'				: [],
				'Cracorn2'				: [],
				'Cazo'					: [],
				'Caliz'					: [],
				'Libro2'				: [],
				'Pico'					: [],
				'Pala'					: [],
				'Femur'					: [],
				'Costilla'				: [],
				'Farol2'				: [],
				'MartilloForja'			: [],
				'Cincel'				: [],
				'Pergamino2'			: [],
				'Pergamino'				: [],
				'Saquito'				: [],
				'Libro3'				: [],
				'Libroabierto'			: [],
				'TroncoNevado'			: [],
				'CraneoCornudo3'		: [],
				'CraneoCornudo4'		: [],
				'Silla'					: [],
				'Jarra'					: [],
				'Estaca'				: [],
				'Jarrita'				: [],
				'Bandeja'				: [],
				'Tacita'				: [],
				'Cojin'					: []}

# Please check (especially the stones)
TwoHandedDict={	'Fuelle'				: [],
				'Tinaja'				: [],
				'Perola'				: [],
				'Barril'				: [],
				'Cajon'					: [],
				'Cajon2'				: [],
				'Cajama'				: [],
				'Carretilla'			: [],
				'Cofrepeque'			: [],
				'Mesita'				: []}

# Some items can be stacked into an slot of the inventory.

#                              Kind of object      Max number of objects at inventory
StackObjects  = {
                                'Pocima100'    :    4,
                                'Pocima200'    :    2,
                }
#
# Some items can be carried in the long travels arround the whole world.
#
TravelObjects = [ 'Pocima100','Pocima200', 'PowerPotion', 'PocimaTodo' ]

#
# enemies that can walk inside the lava
#
LavaInmune   = ['Golem_lava','Salamander','Great_Demon','Little_Demon','Spidersmall']

#
#  Health Increase
#                         Object         Life  Cure  Kind
POCIMAC_FOOD   = 0
POCIMAC_POTION = 1
HealthIncrease = {
                         "Manzana"    : (   5,    0, POCIMAC_FOOD)
                        ,"Hogaza"     : (  10,    0, POCIMAC_FOOD)
                        ,"Paletilla"  : (  75,    0, POCIMAC_FOOD)
                        ,"Queso"      : (  40,    0, POCIMAC_FOOD)
                        ,"Seta"       : (  30,    0, POCIMAC_FOOD)
                        ,"Setas"      : (  30,    0, POCIMAC_FOOD)
                        ,"Raiz"       : (  20,    1, POCIMAC_FOOD)
                        ,"Rabano"     : (  20,    1, POCIMAC_FOOD)
                        ,"Saquito"    : ( 100,    1, POCIMAC_FOOD)

                        ,"Pocima25"   : (  50,    1, POCIMAC_POTION)
                        ,"Pocima50"   : ( 150,    1, POCIMAC_POTION)
                        ,"Pocima100"  : ( 500,    1, POCIMAC_POTION)
                        ,"Pocima200"  : (1000,    1, POCIMAC_POTION)
                        ,"PocimaTodo" : (  -1,    1, POCIMAC_POTION)
                  }

######################################
ObjStatic = [
             "Altar",
             "AntorchaAtlante",
             "Antorcha2",
             "Antorchapared",
             "BlasonAurelio",
             "Blason1",
             "Blason2",
             "Blason3",
             "Blason4",
             "Blason5",
             "Blason6",
             "CandilAurelio",
             "Cebolla",
             "ColaSerpiente",
             "Elefante",
             "GanchoAurelio",
             "Gancho",
             "Garfio",
             "Garfio2",
             "Garfio3",
             "GargolaFernando",
             "Gargola",
             "Gargola02",
             "GargolaNevada",
             "Gozne",
             "Halcon",
             "Halcon2",
             "ElefantePartido",
             "LamparaKongo",
             "Lampared",
             "Gancholamp",
             "LamparaMiguel",
             "Lapida",
             "Obelisco",
             "Lapida3",
             "LapidaAmazona",
             "LapidaBarbaro",
             "LapidaCaballero",
             "LapidaManuel",
             "LeonBronce",
             "MandibulaSerpiente",
             "Menhir1",
             "Menhir2",
             "Menhir3",
             "Monjecaliz",
             "Monjema",
             "Monjescudo",
             "Monjespada",
             "ObeliscoGrande",
             "ObeliscoNevado",
             "Peanapiedra",
             "Pelele",
             "PeleleNevado",
             "Pendon1",
             "Pendon2",
             "Pendon3",
             "Pendon4",
             "PiedraInformativa",
             "PiedraNevadaCortada",
             "Polea",
             "PuenteAdolfoDerecho",
             "PuenteAdolfoIzquierdo",
             "ReinaAurelio",
             "Reja",
             "Reyaurelio",
             "Semipuxero",
             "Tapiz",
             "Tapiz2",
             "Tapiz3",
             "Tapiz4",
             "Tapiz5",
             "Tapiz6",
             "TapizAurelio",
             "TapizEscorpion",
             "Tapizkemado1",
             "Tapizkemado2",
             "TelaranyaCuadrada",
             "TelaranyaCuadrada2",
             "TelaranyaEsquina",
             "TelaranyaTriangular",
             "Tronoliso",
             "TronoEscarabeu",
             "Vagoneta",

            ]

ObjWeapon = [
             "Antorcha",
             "Bloodbol",
             "Botella",
             "BotellaVerde",
             "Caliz",
             "Candil",
             "Cazo",
             "Costilla",
             "Cracorn1",
             "Cracorn2",
             "CraneoCornudo3",
             "CraneoCornudo4",
             "Cuchillo",
             "Daga",
             "EsqueletoPieza2",
             "EsqueletoPieza4",
             "EsqueletoPieza6",
             "EsqueletoPieza7",
             "EsqueletoPieza8",
             "EsqueletoPieza9",
             "EsqueletoPieza10",
             "Estaca",
             "Femur",
             "Jarra",
             "Jarrita",
             "Libro",
             "Libro2",
             "Libro3",
             "Mortero",
             "Pala",
             "Pico",
             "Skull",
             "Taburete",

            ]

def ObjType(ObjKind):
	if   ObjKind in ObjWeapon:
		return "Weapon"
	elif ObjKind in ObjStatic:
		return ""
	else:
		return "Physic"

######################################
def GiveObjectPowDefResResMaxData(ObjectName):
	if ObjectName:
		object=Bladex.GetEntity(ObjectName)
		if object:
			# Get object type
			object_data= None
			def_object_data= None
			if DefaultObjectData.has_key(object.Kind):
				def_object_data= DefaultObjectData[object.Kind]
			if EntitiesObjectData.has_key(ObjectName):
				object_data= EntitiesObjectData[ObjectName]
			else:
				object_data=def_object_data

			if object_data:
				if object_data[0]==OBJ_STANDARD or object_data[0]==OBJ_WEAPON or object_data[0]==OBJ_BOW or object_data[0]==OBJ_ARROW:
					sub_object_data=object_data[5]
					if len(sub_object_data)==0 or sub_object_data[0]==W_FLAG_1H:
						return object_data[1], object_data[2], None, None
					else:
						if def_object_data:
							return object_data[1], object_data[2], sub_object_data[4], def_object_data[5][4]
						else:
							return object_data[1], object_data[2], sub_object_data[4], sub_object_data[4]

				elif object_data[0]==OBJ_SHIELD:
					if def_object_data:
						return object_data[1], None, object_data[2], def_object_data[2]
					else:
						return object_data[1], None, object_data[2], object_data[2]
	return None,None,None,None

def GiveObjectFlag(ObjectName):
	if ObjectName:
		object=Bladex.GetEntity(ObjectName)
		if object:
			# Get object type
			if EntitiesObjectData.has_key(ObjectName):
				object_data = EntitiesObjectData[ObjectName]
			elif DefaultObjectData.has_key(object.Kind):
				object_data = DefaultObjectData[object.Kind]
			else:
				return OBJ_NONE
			object_flag = object_data[0]
			return object_flag
	return OBJ_NONE

def GiveWeaponFlag(ObjectName):
	object=Bladex.GetEntity(ObjectName)
	# Get object type
	if EntitiesObjectData.has_key(ObjectName):
		object_data = EntitiesObjectData[ObjectName]
	else:
		object_data = DefaultObjectData[object.Kind]
	object_flag = object_data[0]

	if object_flag!=OBJ_WEAPON:
		return -1

	if len(object_data)<6:
		print "Weapon " + ObjectName + " has not been properly clasified as 1h , 2h ..."
		#pdb.set_trace()
		return W_FLAG_1H
	else:
		if len(object_data[5])<1:
			return W_FLAG_1H
		return object_data[5][0]

def GiveQuiverType(arrow_type):
	for kind in DefaultObjectData.keys():
		if len(kind)<2 or kind[len(kind)-2:]!='_E':
			if len(kind)>0 and kind[len(kind)-1:]!='1':
				if len(kind)>0 and kind[len(kind)-1:]!='2':
					object_data= DefaultObjectData[kind]
					if object_data[0]==OBJ_QUIVER and object_data[2]==arrow_type:
						return kind
	return None

def IsParryingType(Kind):
	if DefaultObjectData.has_key(Kind):
		object_data= DefaultObjectData[Kind]
		if object_data[0]==OBJ_ITEM or object_data[0]==OBJ_USEME:
			return 0
		elif object_data[0]==OBJ_SHIELD:
			return 1
		elif (object_data[0]==OBJ_WEAPON or object_data[1]==OBJ_STANDARD) and len(object_data)>5 and len(object_data[5])>0 and object_data[5][0]!=W_FLAG_1H:
			return 1
	return 0

def IsWeaponType(Kind):
	if DefaultObjectData.has_key(Kind):
		object_data= DefaultObjectData[Kind]
		if object_data[0]==OBJ_WEAPON:
			return 1
	return 0

def CheckWeapons():
	WeaponErrorList=[]
	nents= Bladex.nEntities()
	for i in range(nents):
		ent= Bladex.GetEntity(i)
		if (not ent.Person) and (not ent.Weapon) and ent.Physic:
			object_flag= GiveObjectFlag(ent.Name)
			if object_flag==OBJ_STANDARD or object_flag==OBJ_WEAPON:
				print ent.Kind+"("+ent.Name+") was not created as a weapon"

TimesSaved = 0

def SaveData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"wt")
  p=cPickle.Pickler(funcfile)
  p.persistent_id=GameStateAux.persistent_id
  d=(EntitiesSelectionData,TimesSaved,EntitiesObjectData)
  p.dump(d)
  funcfile.close()


def LoadData(filename):
  import cPickle
  import GameStateAux

  funcfile=open(filename,"rt")
  p=cPickle.Unpickler(funcfile)
  p.persistent_load=GameStateAux.persistent_load
  d=p.load()
  funcfile.close()

  global EntitiesSelectionData
  global TimesSaved
  global EntitiesObjectData

  EntitiesSelectionData = d[0]
  TimesSaved            = d[1]
  EntitiesObjectData    = d[2]

import GameState
GameState.ModulesToBeSaved.append(__import__(__name__))

if netgame.GetNetState() == 1:
	DefaultObjectData['Chaosword']=          [OBJ_WEAPON, 12 , 0, 2.0,  THR_STRAIGHT, [W_FLAG_2W,PI,2000,750,100,100,GolpeArmaEscudoMetal]]
	DefaultObjectData['Hacha']=              [OBJ_WEAPON, 11 , 0, 2.5,  THR_SPINNING, [W_FLAG_1H,]]
	DefaultObjectData['Gladius']=            [OBJ_WEAPON, 10,  0, 2.2,  THR_SPINNING, [W_FLAG_1H,]]
	DefaultObjectData['Bo']=                 [OBJ_WEAPON, 10,  0, 2.0,  THR_SPINNING, [W_FLAG_SP,PI,2000,750,100,100,GolpeArmaEscudoMadera]]  # Was GolpeArmaEscudoMetal
    
    

