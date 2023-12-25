##///
##||| LUGARESBACK.PY TITANIUM
##||| Change list:
##||| * Restored missing narration after clearing Temple of Ianna
##||| * Can now be navigated with movement keys
##||| * Gamepad should work now properly
##\\\ 

import Sounds
import Bladex
import Reference
import GotoMapVars
import GameText
import AuxFuncs
import Language

language = Language.CheckFallback()  ### - Kinda not needed I guess? Leaving it here for consistency with rest of RAS and Fire Falcom code -LeadHead

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
MapStatus	= [0,0,0,0,0,0] # Resulting Available Map/s
EntitiesName= {}


import pickle
DataString = Bladex.GetStringValue("HistoricalData")

Cartelitos		= []
Cartelitas		= []

YellowTorch		= (240,126,0)
WhiteTorch		= (200,200,200)
BlueTorch		= (40,60,250)
#---------------------------------


## Ghost Pointers Creation------------
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

gpmar = Bladex.CreateEntity(Nejev,"GhostPointer",-41234.284000,13900,39172.076000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #12

gpmar = Bladex.CreateEntity(Nemrut,"GhostPointer",-30310.393000,13900,3890.441000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #11

gpmar = Bladex.CreateEntity(Alfarum,"GhostPointer",-29326.827000,13900,45394.131000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #13

gpmar = Bladex.CreateEntity(Ianna,"GhostPointer",28275.839000,13900,37737.520000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #15

gpmar = Bladex.CreateEntity(DalGurak,"GhostPointer",48858.410000,13900,33152.115000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitos.append(gpmar.Name) #16
#____________________________________
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

gpmar = Bladex.CreateEntity(NEJEV,"GhostPointer",-41234.284000,13900,39172.076000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitas.append(gpmar.Name) #12

gpmar = Bladex.CreateEntity(NEMRUT,"GhostPointer",-30310.393000,13900,3890.441000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitas.append(gpmar.Name) #11

gpmar = Bladex.CreateEntity(ALFARUM,"GhostPointer",-29326.827000,13900,45394.131000)
gpmar.Static = 0
gpmar.UseFunc = None
Cartelitas.append(gpmar.Name) #13

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

if Bladex.GetStringValue("LastVisitedMap") == "M_2":
	LastMap = 1

if Bladex.GetStringValue("LastVisitedMap") == "M_3":
	LastMap = 2

if Bladex.GetStringValue("LastVisitedMap") == "M_4":
	LastMap = 4

if Bladex.GetStringValue("LastVisitedMap") == "M_5":
	LastMap = 3

if Bladex.GetStringValue("LastVisitedMap") == "M_6":
	LastMap = 5

if Bladex.GetStringValue("LastVisitedMap") == "M_7":        # Missing narration and text fix. -LeadHead
	GameText.WriteText("M15T8",TextYPos)
	LastMap = 6

	sound2=Bladex.CreateSound('../../Sounds/'+language+'/palacebalance.wav', 'SoundM15')
	sound2.Volume=0.5
	sound2.MinDistance=100000
	sound2.MaxDistance=200000
	Bladex.AddScheduledFunc(Bladex.GetTime(), sound2.PlayStereo, ())

# Next line is for testing different Texts ;-)
#GameText.WriteText("M1T2")

CurrentSelected = LastMap
CarriedTablets = GotoMapVars.GetCarriedTablets()

def NextPlace():
	global CarriedTablets
	global CurrentSelected
	a = CurrentSelected
	bExit = 0
	while (not bExit):
		a = a + 1
		if (a > 7):
			a = 0
		if (a < 6):
			if ((GotoMapVars.PlacedTablets[a] == 0) and (CarriedTablets[a] != 1)):
				CurrentSelected = a
				bExit = 1
		if (a == 6):
			if (CarriedTablets.count(1)):
				CurrentSelected = a
				bExit = 1
		if (a == 7):
			CurrentSelected = a
			bExit = 1
		if(CurrentSelected == a):
			bExit = 1
	PlaySound()

def PrevPlace():
	global CurrentSelected
	a = CurrentSelected
	bExit = 0
	while (not bExit):
		a = a - 1
		if (a < 0):
			a = 7
		if (a < 6):
			if ((GotoMapVars.PlacedTablets[a] == 0) and (CarriedTablets[a] != 1)):
				CurrentSelected = a
				bExit = 1
		if (a == 6):
			if (CarriedTablets.count(1)):
				CurrentSelected = a
				bExit = 1
		if (a == 7):
			CurrentSelected = a
			bExit = 1
		if(CurrentSelected == a):
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
	if (CurrentSelected < 6):
		if ((GotoMapVars.PlacedTablets[CurrentSelected] != 1) and (CarriedTablets[CurrentSelected] != 1)):
			Bladex.AddScheduledFunc(Bladex.GetTime(),AuxFuncs.FadeTo,(4.5, 0.0))
			Bladex.AddScheduledFunc(Bladex.GetTime() + 4.5,  SelectPlace,())
			Bladex.RemoveScheduledFunc("NextText")
			GameText.FADE_TIME = 4.5
			GameText.FadeText(1,0)
			FadeInfoKeyWidget()
			Bladex.DeactivateInput()

	if (CurrentSelected == 6):
		if (CarriedTablets.count(1)):
			Bladex.AddScheduledFunc(Bladex.GetTime(),AuxFuncs.FadeTo,(4.5, 0.0))
			Bladex.AddScheduledFunc(Bladex.GetTime() + 4.5,  SelectPlace,())
			Bladex.RemoveScheduledFunc("NextText")
			GameText.FADE_TIME = 4.5
			GameText.FadeText(1,0)
			FadeInfoKeyWidget()
			Bladex.DeactivateInput()

	if (CurrentSelected == 7):
		Bladex.AddScheduledFunc(Bladex.GetTime(),AuxFuncs.FadeTo,(4.5, 0.0))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 4.5,  SelectPlace,())
		Bladex.RemoveScheduledFunc("NextText")
		GameText.FADE_TIME = 4.5
		GameText.FadeText(1,0)
		FadeInfoKeyWidget()
		Bladex.DeactivateInput()


def SelectPlace():
	global CurrentSelected
	global LastMap

	Bladex.ActivateInput()
	if (LastMap != 6) and (CurrentSelected == 6):
			Bladex.LoadLevel("Palace_Back")
			return

	if (CurrentSelected == 7):
		Bladex.LoadLevel("Tower_M16")
		return

	if not CarriedTablets[CurrentSelected]:
		if (CurrentSelected == 0):
			Bladex.LoadLevel("Mine_Back")
		if (CurrentSelected == 1):
			Bladex.LoadLevel("Labyrinth_Back")
		if (CurrentSelected == 2):
			Bladex.LoadLevel("Tomb_Back")
		if (CurrentSelected == 3):
			Bladex.LoadLevel("Btomb_Back")
		if (CurrentSelected == 4):
			Bladex.LoadLevel("Ice_Back")
		if (CurrentSelected == 5):
			Bladex.LoadLevel("Desert_Back")


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
	
	Bladex.AssocKey("Next"	,"Gamepad","JoyRight")          # SNEG, you muppets, you forgot to add this here!
	Bladex.AssocKey("Prev"	,"Gamepad","JoyLeft")           # Where is your QA department?!
	Bladex.AssocKey("Select","Gamepad","ButtonSouth")       #           -LeadHead

	InputManager.SetInputActionsSet(LastOne)

import KeybWidget
KeybWidget.AdditionalKeysCallBack = RedefineKeys
RedefineKeys()


Bladex.AddBoundFunc("Next"	,NextPlace  )
Bladex.AddBoundFunc("Prev"	,PrevPlace  )
Bladex.AddBoundFunc("Select",FadeAndLoad)
