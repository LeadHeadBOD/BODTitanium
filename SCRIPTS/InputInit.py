##///
##||| POCIMAC.PY TITANIUM
##||| Change list:
##||| * Added necessary "AddInputAction" for potion hotkeys
##||| * 
##||| * 
##||| * 
##\\\ 

import DefaultSelectionData



import BInput

InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")  # Me aseguro de definir las acciones en el grupo correcto

import Reference



Bladex.AddInputAction("Forwards",1)
Bladex.AddInputAction("Backwards",1)
Bladex.AddInputAction("Turn Left",1)
Bladex.AddInputAction("Turn Right",1)
Bladex.AddInputAction("Jump",1)
Bladex.AddInputAction("Attack",1)
Bladex.AddInputAction("Attack Release",0)
Bladex.AddInputAction("Block",1)
Bladex.AddInputAction("Sneak",1)
Bladex.AddInputAction("Run",1)
Bladex.AddInputAction("Block Release",0)
Bladex.AddInputAction("Throw Right",0)
Bladex.AddInputAction("Throw Left",0)
Bladex.AddInputAction("Throw",0)
Bladex.AddInputAction("Throw Release",0)
Bladex.AddInputAction("Use",0)
Bladex.AddInputAction("Select Enemy",0)
Bladex.AddInputAction("UnSelectEnemy",0)
Bladex.AddInputAction("Screen Shot",0)
Bladex.AddInputAction("Toggle Weapons",0)

Bladex.AddInputAction("SelectObj",0)
Bladex.AddInputAction("UnSelectObj",0)

Bladex.AddInputAction("Look Up",1)
Bladex.AddInputAction("Look Down",1)

Bladex.AddInputAction("Swim Up",1)
Bladex.AddInputAction("Swim Down",1)

if Reference.DEMO_MODE==0:
    Bladex.AddInputAction("ToggleStats",0)
    Bladex.AddInputAction("ToggleSampling",0)
    Bladex.AddInputAction("Camera Left",1)
    Bladex.AddInputAction("Camera Right",1)
    Bladex.AddInputAction("Toggle Sound",0)
    Bladex.AddInputAction("Bigger FOV",0)
    Bladex.AddInputAction("Smaller FOV",0)
    Bladex.AddInputAction("Change Mov",0)
    Bladex.AddInputAction("Toggle BB",0)
    Bladex.AddInputAction("ToggleInvincibility",0)

Bladex.AddInputAction("Change Camera",0)
Bladex.AddInputAction("Fixed Camera",0)
Bladex.AddInputAction("Camera Dist",0)

Bladex.AddInputAction("Cycle Weapons",0)
Bladex.AddInputAction("Cycle Shields",0)
Bladex.AddInputAction("Cycle Objects",0)
Bladex.AddInputAction("Free Look",1)
Bladex.AddInputAction("Next View",0)
Bladex.AddInputAction("Last View",0)

Bladex.AddInputAction("RotateX",0)
Bladex.AddInputAction("RotateY",0)

Bladex.AddInputAction("FrwdDown",0)
Bladex.AddInputAction("FrwdUp",0)
Bladex.AddInputAction("BrwdDown",0)
Bladex.AddInputAction("BrwdUp",0)



Bladex.AddInputAction("Show Scorer",0)
Bladex.AddInputAction("Send Message",0)


Bladex.AddInputAction("TurnInRelax",0)

Bladex.AddInputAction("ToggleProfiling",0)

Bladex.AddInputAction("LaunchTravel",0)

#####################################
# Titanium stuff   -LeadHead
#####################################
"""Hotkeys"""
Bladex.AddInputAction("PowerPotKey",0)
Bladex.AddInputAction("FullPotKey",0)
Bladex.AddInputAction("200PotKey",0)
Bladex.AddInputAction("100PotKey",0)
Bladex.AddInputAction("BraceletKey",0)
Bladex.AddInputAction("CrownKey",0)
Bladex.AddInputAction("AmuletKey",0)

"""Titanium Scorer"""
#Bladex.AddInputAction("ShowTitaniumStats",0)


#####################################
# Specials Gamepad Tricks
#####################################

Bladex.AddInputAction("Turn Around",0)
# Bladex.AddInputAction("PressLeftRight",0)
# Bladex.AddInputAction("SpecialThrow",0)
# Bladex.AddInputAction("SpecialThrow Release",0)
Bladex.AddInputAction("UseAndLeftRight",0)
Bladex.AddInputAction("JumpAndSelectObj",0)
Bladex.AddInputAction("SneakOrSelectPreviousEnemy",0)
Bladex.AddInputAction("SneakOrSelectPreviousEnemyRelease",0)

Bladex.AssocKey("RotateX","Gamepad","X_LAxis")
Bladex.AssocKey("RotateY","Gamepad","Y_LAxis")

def PressUpDown():
	me=Bladex.GetEntity("Player1")

	if me.InAttack == 1:
		Bladex.FakeInputAction("JoyDown", 1)
		Bladex.FakeInputAction("JoyUp", 1)
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.30, Bladex.FakeInputAction, ("JoyUp", 0))
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.30, Bladex.FakeInputAction, ("JoyDown", 0))
	else:
		Bladex.TurnAround()

Bladex.AddBoundFunc("Turn Around", PressUpDown)

def PressLeftRight():
	Bladex.FakeInputAction("JoyLeft", 1)
	Bladex.FakeInputAction("JoyRight", 1)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.1, Bladex.FakeInputAction, ("JoyRight", 0))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.1, Bladex.FakeInputAction, ("JoyLeft", 0))

def UseAndLeftRight():
	Bladex.FakeInputAction("Use", 1)
	PressLeftRight()

Bladex.AddBoundFunc("UseAndLeftRight", UseAndLeftRight)

def JumpAndSelectObj():
	Bladex.FakeInputAction("Jump", 1)
	Bladex.FakeInputAction("SelectObj", 1)
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.01, Bladex.FakeInputAction, ("Jump", 0))
	Bladex.AddScheduledFunc(Bladex.GetTime() + 0.01, Bladex.FakeInputAction, ("SelectObj", 0))

Bladex.AddBoundFunc("JumpAndSelectObj", JumpAndSelectObj)

def SneakOrSelectPreviousEnemy():
	Bladex.FakeInputAction("Sneak", 1)
	DefaultSelectionData.SelectPreviousEnemy()

def SneakOrSelectPreviousEnemyRelease():
	Bladex.FakeInputAction("Sneak", 0)

Bladex.AddBoundFunc("SneakOrSelectPreviousEnemy", SneakOrSelectPreviousEnemy)
Bladex.AddBoundFunc("SneakOrSelectPreviousEnemyRelease", SneakOrSelectPreviousEnemyRelease)


# def SpecialThrow():
# 	Bladex.FakeInputAction("Throw", 1)

# def SpecialThrowRelease():
# 	Bladex.FakeInputAction("Throw Release", 0)

# Bladex.AddBoundFunc("SpecialThrow", SpecialThrow)
# Bladex.AddBoundFunc("SpecialThrow Release", SpecialThrowRelease)

execfile("../../Scripts/DefControlGamepad.py")

