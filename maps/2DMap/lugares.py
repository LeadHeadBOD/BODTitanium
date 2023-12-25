##///
##||| 2DMAP/LUGARES.PY TITANIUM
##||| Change list:
##||| * Can now be navigated with movement keys
##\\\ 

import Sounds
import Bladex
import Reference
import GotoMapVars
import GameText
import AuxFuncs
import Language

language = Language.CheckFallback()

MapList = {}
execfile ("../../data/text/"+Language.Current+"/map2D.py")

sound1=Bladex.CreateSound('../../Sounds/golpe-madera-pesada.wav', 'Sound1')
sound1.Volume=0.5
sound1.MinDistance=10000
sound1.MaxDistance=20000

def PlaySound():
	cam = Bladex.GetEntity("Camera")
	sound1.Stop()
	sound1.PlayStereo()


#17 maps
MapStatus	= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Resulting Available Map/s
EntitiesName= {}



import pickle
DataString = Bladex.GetStringValue("HistoricalData")

Cartelitos		= []
Cartelitas		= []

YellowTorch		= (240,126,0)
WhiteTorch		= (200,200,200)
BlueTorch		= (40,60,250)
#---------------------------------


# EVALUATE INPUT DATA----------
# First Choice******
if (1):#VisitedMaps[0] or VisitedMaps[1] or VisitedMaps[2] or VisitedMaps[3]):
	other = 0
	for i in range(11):
		if GotoMapVars.VisitedMaps[6 + i]:
			other = 1
	if not other:
		if not GotoMapVars.VisitedMaps[4]:
			MapStatus[4] = 1
		if not GotoMapVars.VisitedMaps[5]:
			MapStatus[5] = 1
# ******************
# Map 6
if GotoMapVars.VisitedMaps[4] and GotoMapVars.VisitedMaps[5]:
	other = 0
	for i in range(11):# Check from this point on looking for "last used" map.
		if GotoMapVars.VisitedMaps[6 + i]:
			other = 1
		if not other:
				MapStatus[6] = 1 # If neither this map nor the following have been visited, this is the one
# Map 7
if GotoMapVars.VisitedMaps[6]:
	other = 0
	for i in range(10):# Check from this point on looking for "last used" map.
		if GotoMapVars.VisitedMaps[7 + i]:
			other = 1
		if not other:
			MapStatus[7] = 1 # If neither this map nor the following have been visited, this is the one
#------------------------------

if GotoMapVars.VisitedMaps[7]:

	if not GotoMapVars.VisitedMaps[8]  and not GotoMapVars.VisitedMaps[11]:
		MapStatus[ 8] = 1
		MapStatus[11] = 1

	if GotoMapVars.VisitedMaps[9] and GotoMapVars.VisitedMaps[10] and GotoMapVars.VisitedMaps[12] and GotoMapVars.VisitedMaps[13]:
		MapStatus[14] = 1
	else:

		lvm = Bladex.GetStringValue("LastVisitedMap")

		if lvm=="M_9" or lvm=="M_10" or lvm=="M_11":
			if not GotoMapVars.VisitedMaps[9]:
				MapStatus[ 9] = 1
			if not GotoMapVars.VisitedMaps[10]:
				MapStatus[10] = 1
			if GotoMapVars.VisitedMaps[9] and GotoMapVars.VisitedMaps[10]:
				MapStatus[11] = 1

		if lvm=="M_12" or lvm=="M_13" or lvm=="M_14":
			if not GotoMapVars.VisitedMaps[12]:
				MapStatus[12] = 1
			if not GotoMapVars.VisitedMaps[13]:
				MapStatus[13] = 1
			if GotoMapVars.VisitedMaps[12] and GotoMapVars.VisitedMaps[13]:
				MapStatus[ 8] = 1


## Ghost Pointers Creation------------
gpmar = Bladex.CreateEntity(Monolith,"GhostPointer",-57636.530000,13900,-19374.975000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name)

gpmar = Bladex.CreateEntity(Tabriz,"GhostPointer",-79169.079000,13900,4672.719000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name)

gpmar = Bladex.CreateEntity(Khazel,"GhostPointer",-103963.620000,13900,-1505.120000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name)

gpmar = Bladex.CreateEntity(Marakamda,"GhostPointer",-50083.984000,13900,-6576.963000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #4

gpmar = Bladex.CreateEntity(Mine,"GhostPointer",-90134.749000,13900,1985.339000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #5

gpmar=Bladex.CreateEntity(TellHa,"GhostPointer",-70379.699000,13900,-1797.824000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #6

gpmar = Bladex.CreateEntity(QueensT,"GhostPointer",-68459.210000,14000,12682.204000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #7

gpmar=Bladex.CreateEntity(Karum,"GhostPointer",-58187.154000,13900,20706.704000)
gpmar.Static=0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #8

gpmar = Bladex.CreateEntity(Shalatuwar,"GhostPointer",-39236.556000,13900,24243.602000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #9

gpmar = Bladex.CreateEntity(Orlok,"GhostPointer",-13828.658000,13900,23751.465000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #10

gpmar = Bladex.CreateEntity(Nemrut,"GhostPointer",-30310.393000,13900,3890.441000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #11

gpmar = Bladex.CreateEntity(Nejev,"GhostPointer",-41234.284000,13900,39172.076000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #12

gpmar = Bladex.CreateEntity(Alfarum,"GhostPointer",-29326.827000,13900,45394.131000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #13

gpmar = Bladex.CreateEntity(Xathra,"GhostPointer",-43869.492000,13900,56313.163000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #14

gpmar = Bladex.CreateEntity(Ianna,"GhostPointer",28275.839000,13900,37737.520000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #15

gpmar = Bladex.CreateEntity(DalGurak,"GhostPointer",48858.410000,13900,33152.115000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #16
#____________________________________
if Language.Current == "Chinese":
	Cartelitas = Cartelitos
else:
	gpmar = Bladex.CreateEntity(MONOLITH,"GhostPointer",-57636.530000,13900,-19374.975000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name)

	gpmar = Bladex.CreateEntity(TABRIZ,"GhostPointer",-79169.079000,13900,4672.719000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name)

	gpmar = Bladex.CreateEntity(KHAZEL,"GhostPointer",-103963.620000,13900,-1505.120000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name)

	gpmar = Bladex.CreateEntity(MARAKAMDA,"GhostPointer",-50083.984000,13900,-6576.963000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #4

	gpmar = Bladex.CreateEntity(MINE,"GhostPointer",-90134.749000,13900,1985.339000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #5

	gpmar=Bladex.CreateEntity(TELLHA,"GhostPointer",-70379.699000,13900,-1797.824000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #6

	gpmar = Bladex.CreateEntity(QUEENST,"GhostPointer",-68459.210000,14000,12682.204000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #7

	gpmar=Bladex.CreateEntity(KARUM,"GhostPointer",-58187.154000,13900,20706.704000)
	gpmar.Static=0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #8

	gpmar = Bladex.CreateEntity(SHALATUWAR,"GhostPointer",-39236.556000,13900,24243.602000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #9

	gpmar = Bladex.CreateEntity(ORLOK,"GhostPointer",-13828.658000,13900,23751.465000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #10

	gpmar = Bladex.CreateEntity(NEMRUT,"GhostPointer",-30310.393000,13900,3890.441000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #11

	gpmar = Bladex.CreateEntity(NEJEV,"GhostPointer",-41234.284000,13900,39172.076000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #12

	gpmar = Bladex.CreateEntity(ALFARUM,"GhostPointer",-29326.827000,13900,45394.131000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #13

	gpmar = Bladex.CreateEntity(XATHRA,"GhostPointer",-43869.492000,13900,56313.163000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #14

	gpmar = Bladex.CreateEntity(IANNA,"GhostPointer",28275.839000,13900,37737.520000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #15

	gpmar = Bladex.CreateEntity(DALGURAK,"GhostPointer",48858.410000,13900,33152.115000)
	gpmar.Static = 0
	gpmar.UseFunc = None
	Cartelitas.append(gpmar.Name) #16
#_________________________________________________________________
# Default Value
LastMap = 0


TextYPos=5
if Bladex.GetStringValue("LastVisitedMap") == "M_1":
	LastMap = 0
	GameText.WriteText("M1T3",TextYPos)

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/kashgar-balance.wav', 'SoundM1')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())

if Bladex.GetStringValue("LastVisitedMap") == "M_2":
	LastMap = 1
	GameText.WriteText("M2T5",TextYPos)

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/ragnar-txtbalance.wav', 'SoundM2')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())

if Bladex.GetStringValue("LastVisitedMap") == "M_3":
	LastMap = 2
	GameText.WriteText("M3T4",TextYPos)

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/balance-enano.wav', 'SoundM3')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())

if Bladex.GetStringValue("LastVisitedMap") == "M_4":
	LastMap = 3
	GameText.WriteText("M4T4",TextYPos)

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/locruinatxtbalance.wav', 'SoundM4')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())

if Bladex.GetStringValue("LastVisitedMap") == "M_5":
	GameText.WriteText("M5T4",TextYPos)
	LastMap = 4

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/minabalance.wav', 'SoundM5')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())

if Bladex.GetStringValue("LastVisitedMap") == "M_6":
	GameText.WriteText("M6T5",TextYPos)
	LastMap = 5

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/laberintobalance.wav', 'SoundM6')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_7":
	GameText.WriteText("M7T6",TextYPos)
	LastMap = 6

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/tumba-balance.wav', 'SoundM7')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_8":
	GameText.WriteText("M8T6",TextYPos)
	LastMap = 7

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/isla-balance.wav', 'SoundM8')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_9":
	GameText.WriteText("M9T4",TextYPos)
	LastMap = 8

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/orcobalance.wav', 'SoundM9')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_10":
	GameText.WriteText("M10T3",TextYPos)
	LastMap = 9

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/balance-orlok.wav', 'SoundM10')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_11":
	GameText.WriteText("M11T4",TextYPos)
	LastMap = 10

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/nubesbalance.wav', 'SoundM11')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_12":
	GameText.WriteText("M12T4",TextYPos)
	LastMap = 11

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/btomb-balance1.wav', 'SoundM12')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_13":
	GameText.WriteText("M13T8",TextYPos)
	LastMap = 12

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/desierto-balance.wav', 'SoundM13')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_14":
	GameText.WriteText("M14T3",TextYPos)
	LastMap = 13

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/volcanbalance.wav', 'SoundM14')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())


if Bladex.GetStringValue("LastVisitedMap") == "M_15":
	GameText.WriteText("M15T8",TextYPos)
	LastMap = 14

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/palacebalance.wav', 'SoundM15')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())





# Next line is for testing different Texts ;-)
#GameText.WriteText("M1T2")

CurrentSelected = LastMap

def NextPlace():
	global CurrentSelected
	a = CurrentSelected
	bExit = 0
	while (not bExit):
		a = a + 1
		if (a >= 16):
			a = 0
		if ((MapStatus[a] != 0) or (CurrentSelected == a)):
			CurrentSelected = a
			bExit = 1
	PlaySound()

def PrevPlace():
	global CurrentSelected
	a = CurrentSelected
	bExit = 0
	while (not bExit):
		a = a - 1
		if (a < 0):
			a = 15
		if ((MapStatus[a] != 0) or (CurrentSelected == a)):
			CurrentSelected = a
			bExit = 1
	PlaySound()

def FadeInfoKeyWidget(alpha = 1.0):
	try:
		if alpha > 0.009:
			alpha = alpha - 0.008
			InfoKeysWidget.SetAlpha(alpha)
			Bladex.AddScheduledFunc(Bladex.GetTime() + 0.03,FadeInfoKeyWidget,(alpha,))
		else:
			InfoKeysWidget.SetAlpha(0)
	except NameError:
		# InfoKeysWidget probably destroyed already
		pass

def FadeAndLoad():
	global CurrentSelected
	global LastMap
	if (LastMap != CurrentSelected):
		Bladex.RemoveScheduledFunc("NextText")
		GameText.FADE_TIME = 4.5
		GameText.FadeText(1,0)
		FadeInfoKeyWidget()
		Bladex.AddScheduledFunc(Bladex.GetTime(),AuxFuncs.FadeTo,(4.5, 0.0))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 4.5,  SelectPlace,())
		Bladex.DeactivateInput()

def SelectPlace():
	global CurrentSelected
	global LastMap

	Bladex.ActivateInput()
	if (LastMap != CurrentSelected):
		if (CurrentSelected == 0):
			Bladex.LoadLevel("Barb_M1")
		if (CurrentSelected == 3):
			Bladex.LoadLevel("Ruins_M4")
		if (CurrentSelected == 2):
			Bladex.LoadLevel("Dwarf_M3")
		if (CurrentSelected == 1):
			Bladex.LoadLevel("Ragnar_M2")
		if (CurrentSelected == 5):
			Bladex.LoadLevel("Labyrinth_M6")
		if (CurrentSelected == 4):
			Bladex.LoadLevel("Mine_M5")
		if (CurrentSelected == 6):
			Bladex.LoadLevel("Tomb_M7")
		if (CurrentSelected == 7):
			Bladex.LoadLevel("Island_M8")
		if (CurrentSelected == 8):
			Bladex.LoadLevel("Orc_M9")
		if (CurrentSelected == 10):
			Bladex.LoadLevel("Ice_M11")
		if (CurrentSelected == 9):
			Bladex.LoadLevel("Orlok_M10")
		if (CurrentSelected == 11):
			Bladex.LoadLevel("Btomb_M12")
		if (CurrentSelected == 12):
			Bladex.LoadLevel("Desert_M13")
		if (CurrentSelected == 13):
			Bladex.LoadLevel("Volcano_M14")
		if (CurrentSelected == 14):
			Bladex.LoadLevel("Palace_M15")
		if (CurrentSelected == 15):
			Bladex.LoadLevel("Tower_M16")


import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")

Bladex.AddInputAction("Next"  ,0)
Bladex.AddInputAction("Prev"  ,0)
Bladex.AddInputAction("Select",0)

def RedefineKeys():
	import BInput

	InputManager=BInput.GetInputManager()
	LastOne = InputManager.GetInputActionsSet()
	InputManager.SetInputActionsSet("Default")

	Bladex.AssocKey("Next"	,"Keyboard","Right")
	Bladex.AssocKey("Prev"	,"Keyboard","Left")
	Bladex.AssocKey("Select","Keyboard","Enter")
	BInput.TranslateInputFromTo("Turn Right", "Next")   # Added. Now can use movement keys (whatever they happen to be bound to) 
	BInput.TranslateInputFromTo("Turn Left", "Prev")    # to navigate the map screen.  - LeadHead
	
	Bladex.AssocKey("Next"	,"Gamepad","JoyRight")
	Bladex.AssocKey("Prev"	,"Gamepad","JoyLeft")
	Bladex.AssocKey("Select","Gamepad","ButtonSouth")

	InputManager.SetInputActionsSet(LastOne)

import KeybWidget
KeybWidget.AdditionalKeysCallBack = RedefineKeys
RedefineKeys()

Bladex.AddBoundFunc("Next"	,NextPlace  )
Bladex.AddBoundFunc("Prev"	,PrevPlace  )
Bladex.AddBoundFunc("Select",FadeAndLoad)
