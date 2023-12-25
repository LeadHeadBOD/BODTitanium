##///
##||| MENU.PY TITANIUM
##||| Change list:
##||| * If the level is "Final" should no longer show the option "Return to Game"
##||| * Now uses TranslateInputFromTo() instead of fixed WASD control in case the user has re-bound the keys.
##\\\ 

# Modified 03/Mar/2000 Rod Wolfson
import Blood
import MenuWidget
import WidgetsExtra
import Bladex
import BBLib
import netgame
import Raster
import BIPCx
import Sounds
import GotoMapVars
import acts
import SaveGame
import MemPersistence
import string
import ObjStore
import KeybWidget
if netgame.GetNetState() == 0:
##  import Scorer
##  import TabWidget
  import Credits
else:
  import NetScorer


import Raster
import BInput
import BUIx
import pdb
#import sys

import Reference #Por demo_mode...


import MenuText
import NetMisc
import netwidgets

import Language

import os
import GamepadWidget

#import Bldb

MenuFontSmall=Language.LetrasMenuSmall
MenuFontMed=Language.LetrasMenu
MenuFontBig=Language.LetrasMenuBig

GamepadButtonVSep = -1400
BackOptionVSep = -1000
BackGamepadOptionVSep = -1250

Character = -1

TBUDSoundAble = 1

EscapeFunction = None

# SOUNDS FOR MENU->
SndCorreGema=Bladex.CreateSound("../../Sounds/golpe-2.wav","Risoto1")
SndCorreGema.Volume=0.5
SndCorreGema.MinDistance=1000000.0
SndCorreGema.MaxDistance=2000000

SndNewMenu=Bladex.CreateSound("../../Sounds/golpe-madera-pesada.wav","Risoto2")
SndNewMenu.Volume=1.0
SndNewMenu.MinDistance=1000000.0
SndNewMenu.MaxDistance=2000000

last_ss_quality=-1
sound_cfg_changed=0

def PlaySound(Chound):
	cam = Bladex.GetEntity("Camera")
	Chound.Position = cam.Position
	Chound.Stop()
	Chound.PlaySound(0)

# MUSIC FOR MENU->
#Bladex.AddMusicEventMP3( "MenuMusic",  "../../Sounds/abismo-fin1.MP3",     2.0, 1.0, 1.0, 10001, 1, -1 )
#-----------------------------------------

def BackMenu(option):
	_MainMenu.DeActivateMenuItem()


GamepadButton = {
			"Name"    : "${ignore:Accept}${ignore:\" - " + MenuText.GetMenuText("Accept") + " / }${ignore:Return}${ignore:\" - " + MenuText.GetMenuText("Back") + "\"}",
			"VSep"    : GamepadButtonVSep,
			"Font"    : MenuFontBig,
			"Kind"    : MenuWidget.B_MenuItemTextNoFXNoFocus
			}


BackOption =    {"Name"    : MenuText.GetMenuText("BACK"),
				"VSep"    : BackOptionVSep,
				"Command" : BackMenu,
				"Font"    : MenuFontBig
			 }


BackGamepadOption = {"Name"    : MenuText.GetMenuText("BACK"),
			  "VSep"    : BackGamepadOptionVSep,
			  "Command" : BackMenu,
			  "Font"    : MenuFontBig
			 }

# Map Loading Upong Menu Request---
def Load2DMap(option):
	Bladex.LoadLevel("2DMap")

def LoadPlayerSelect(option):
	global EscapeFunction

	if "Casa" != Bladex.GetCurrentMap():
		MemPersistence.Store("MapAlreadyLoaded","pepepotamo")
		Bladex.LoadLevel("Casa")
	else:
		aux = EscapeFunction
		EscapeFunction = None
		_MainMenu.DeActivateMenuItem()
		_MainMenu.DeActivateMenuItem()
		EscapeFunction = aux
		aux = None
		EscapeFunction(1)

def LoadTutorial(option):
	Bladex.LoadLevel("Tutorial")
#----------------------------------

# Save/Load Game-------------------
def SaveGame1(option):
	Bladex.SetRunString("Bladex.StopTime();import GameState;state=GameState.WorldState();state.GetState();state.SaveState('../../Save/SaveGame1.py');state=None")

def SaveGame2(option):
	Bladex.SetRunString("Bladex.StopTime();import GameState;state=GameState.WorldState();state.GetState();state.SaveState('../../Save/SaveGame2.py');state=None")

def SaveGame3(option):
	Bladex.SetRunString("Bladex.StopTime();import GameState;state=GameState.WorldState();state.GetState();state.SaveState('../../Save/SaveGame3.py');state=None")

def SaveGame4(option):
	Bladex.SetRunString("Bladex.StopTime();import GameState;state=GameState.WorldState();state.GetState();state.SaveState('../../Save/SaveGame4.py');state=None")



def LoadGameAux(name):
	path="../../Save/%s_files"%(name,)
	execfile="execfile('../../Scripts/sys_init.py');execfile('../../Save/%s.py')"%(name,)

	file_data_aux=open("%s/%saux"%(path,"aux"),"rt")
	text=file_data_aux.read()
	print text
##	text="Anulado para hacer pruebas"
	file_data_aux.close()

	Bladex.BeginLoadGame()
	Bladex.CloseLevel(execfile,text)


def LoadGame(option):

	LoadGameAux("SaveGame1")



def LoadGame2(option):

	LoadGameAux("SaveGame2")


def LoadGame3(option):
	LoadGameAux("SaveGame3")

def LoadGame4(option):
	LoadGameAux("SaveGame4")
#----------------------------------

def CmdQuit(menu_class):
  Bladex.Quit()

def CommandPrb(menu_class):
  print "Hola"

def OptionCommandPrb(menu_class,option):
  print "Received",option

def SetOptionCommandPrb():
  return "Off"

## Pantalla completa/ventana
# Traducir
def SetFullScreenMode(option):
  print option
  if option=="Full Screen":
    Raster.SetVideoMode(0)
  else:
    Raster.SetWindowSize(640,480)


def FullScreenModeSettings():
  print "FullScreenModeSettings"
  if Raster.FullScreen():
    return 0
  else:
    return 1



# Auto-Facing
def SetFacing(option):
  if option=="Yes":
    Bladex.SetAutoEngageCombat(1)
  else:
    Bladex.SetAutoEngageCombat(0)
  SaveConfiguration()

# Play Intro settings
def GetPlayIntro():
  return Bladex.GetPlayIntro()

def SetPlayIntro(option):
  Bladex.SetPlayIntro(option=="Yes")

def GetFacing():
  return Bladex.GetAutoEngageCombat()


def FacingSettings():
  if Bladex.GetAutoEngageCombat():
    return 1
  else:
    return 0

GORE_PASSWORD         = ""
NEW_GORE_PASSWORD     = ""
CONFIRM_GORE_PASSWORD = ""

CORRECT_GORE_PASSWORD = ""

def LoadPasswordFile():
	import rotor
	global CORRECT_GORE_PASSWORD

	# read encrypted string
	try:
		passwordfile = open("../../Bin/Password.txt", "r")
	except:
		return
	encrpass = passwordfile.read()
	passwordfile.close()

	# use the enigma to decrypt (thank's Hitler!)
	rt = rotor.newrotor('key',12)
	CORRECT_GORE_PASSWORD = rt.decrypt(encrpass)
	del rt

LoadPasswordFile()


def SavePasswordFile():
	import rotor
	global CORRECT_GORE_PASSWORD

	# use the enigma to decrypt (thank's Hitler!)
	rt       = rotor.newrotor('key',12)
	encrpass = rt.encrypt(CORRECT_GORE_PASSWORD)
	del rt

	# write encrypted string
	passwordfile = open("../../Bin/Password.txt", "w")
	passwordfile.write(encrpass)
	passwordfile.close()


# Mouse Config--------
# Axis Invertion
def GetMouseInvertX():
	MouseData = Bladex.GetMouseState()
	return 1-MouseData[0]
def GetMouseInvertY():
	MouseData = Bladex.GetMouseState()
	return 1-MouseData[1]

def SetMouseInvertX(option):
	MouseData = Bladex.GetMouseState()
	if option == "No":
		Bladex.SetMouseState(0,MouseData[1],MouseData[2],MouseData[3])
	else:
		Bladex.SetMouseState(1,MouseData[1],MouseData[2],MouseData[3])
	KeybWidget.SaveListConfig()

def SetMouseInvertY(option):
	MouseData = Bladex.GetMouseState()
	if option == "No":
		Bladex.SetMouseState(MouseData[0],0,MouseData[2],MouseData[3])
	else:
		Bladex.SetMouseState(MouseData[0],1,MouseData[2],MouseData[3])
	KeybWidget.SaveListConfig()

# X Sens
def GetMouseXSens():
	MouseData = Bladex.GetMouseState()
	return int(MouseData[2])

def SetMouseXSens(v):
	MouseData = Bladex.GetMouseState()
	Bladex.SetMouseState(MouseData[0],MouseData[1],v,MouseData[3])
	KeybWidget.SaveListConfig()

# Y Sens
def GetMouseYSens():
	MouseData = Bladex.GetMouseState()
	return int(MouseData[3])

def SetMouseYSens(v):
	MouseData = Bladex.GetMouseState()
	Bladex.SetMouseState(MouseData[0],MouseData[1],MouseData[2],v)
	KeybWidget.SaveListConfig()

# KeybConfig
def ResetKeyB(option):
	_MainMenu.DeActivateMenuItem()
	acts.ResetDefaultControls()
	if KeybWidget.AdditionalKeysCallBack:
	   KeybWidget.AdditionalKeysCallBack()
	_MainMenu.ActivateMenuItem()
	#Maybe should be overwritting values with default-control-file values



def SetDeFacingValue(v):
	return Bladex.SetAecGap(v)



# Scorer Config
CurrentScorerVar = "Full"

def CurrentScorer():
	global CurrentScorerVar
	if CurrentScorerVar == "Full":
		return 0
	if CurrentScorerVar == "Auto":
		return 1

def SetScorer(option):
	global CurrentScorerVar
	import Scorer
	if option == "Full":
		Scorer.PowDefWidgets.Activate()
		Scorer.wKeysFrame.SetVisible(1)
		Scorer.wKeysRFrame.SetVisible(1)
		Scorer.wSpecialsFrame.SetVisible(1)
		Scorer.wEnemiesFrame.SetVisible(1)
		Scorer.wObjectsFrame.SetVisible(1)
		Scorer.wArrowInfo.SetVisible(1)
	elif option == "Auto":
		Scorer.wLeftHand.SetVisible(0)
		Scorer.wRightHand.SetVisible(0)
		Scorer.PowDefWidgets.Deactivate()
		Scorer.wKeysFrame.SetVisible(0)
		Scorer.wKeysRFrame.SetVisible(0)
		Scorer.wSpecialsFrame.SetVisible(0)
		Scorer.wEnemiesFrame.SetVisible(0)
		Scorer.wObjectsFrame.SetVisible(0)
		Scorer.wArrowInfo.SetVisible(0)
	CurrentScorerVar = option
	SaveConfiguration()


# Gore PassWord Checking
def CheckGorePassWord():
	global GORE_PASSWORD
	global CORRECT_GORE_PASSWORD

	print "Checking Password"
	return (CORRECT_GORE_PASSWORD == GORE_PASSWORD)


def Empty():
	return ""


def SetPass(name):
	global GORE_PASSWORD
	GORE_PASSWORD = name

def SetNewPass(name):
	global NEW_GORE_PASSWORD
	NEW_GORE_PASSWORD = name

def SetConfNewPass(name):
	global CONFIRM_GORE_PASSWORD
	CONFIRM_GORE_PASSWORD = name


def SaveConfiguration():
	cfgfile=open('../../Config/GameCfg.py','w')
	cfgfile.write('\n# Configuration settings... be carefull!\n\n\n')
	cfgfile.write("Bladex.SetBloodLevel("+`Bladex.GetBloodLevel()`+')\n')
	cfgfile.write("Bladex.SetMutilationLevel("+`Bladex.GetMutilationLevel()`+')\n')
	cfgfile.write("Bladex.SetDrawObjectShadows("+`Bladex.GetDrawObjectShadows()`+')\n')
	cfgfile.write("Bladex.SetReworkedCamera("+`Bladex.GetReworkedCamera()`+')\n')
	cfgfile.write("Bladex.SetVibration("+`Bladex.GetVibration()`+')\n')
	cfgfile.write("Bladex.SetAutoEngageCombat("+`Bladex.GetAutoEngageCombat()`+')\n')
	cfgfile.write("Bladex.SetFieldOfView("+`Bladex.GetFieldOfView()`+')\n')
	cfgfile.write("Bladex.SetHideUI("+`Bladex.GetHideUI()`+')\n')
	cfgfile.write("Bladex.SetUIScaleFactor("+`Bladex.GetUIScaleFactor()`+')\n')
	cfgfile.write("Bladex.SetAecGap("+`Bladex.GetAecGap()`+')\n')
	cfgfile.write("Blood.Evaporation = "+`Blood.Evaporation`+'\n')
	cfgfile.write("SetScorer("+`CurrentScorerVar`+")\n")
	cfgfile.write('\n# Achalay my brother!.\n\n\n')
	cfgfile.close()

	print "Game options Saved."

## Sangre
# Traducir
def SetBlood(option):
  if option=="Yes":
    Bladex.SetBloodLevel(1)
  else:
    Bladex.SetBloodLevel(0)
  SaveConfiguration()


def BloodSettings():
  if Bladex.GetBloodLevel():
    return 0
  else:
    return 1



## Mutilaciones
# Traducir
def SetMutilation(option):
  if option=="Yes":
    Bladex.SetMutilationLevel(1)
  else:
    Bladex.SetMutilationLevel(0)
  SaveConfiguration()


def MutilationSettings():
  if Bladex.GetMutilationLevel():
    return 0
  else:
    return 1





## Sombras
# Traducir
def SetShadows(option):
  if option=="Yes":
    Bladex.SetDrawObjectShadows(1)
  else:
    Bladex.SetDrawObjectShadows(0)
  SaveConfiguration()


def ShadowsSettings():
  if Bladex.GetDrawObjectShadows():
    return 0
  else:
    return 1

def SetReworkedCamera(option):
  if option=="Yes":
    Bladex.SetReworkedCamera(1)
  else:
    Bladex.SetReworkedCamera(0)
  SaveConfiguration()

def SetVibration(option):
  if option=="Yes":
    Bladex.SetVibration(1)
  else:
    Bladex.SetVibration(0)
  SaveConfiguration()

def Vibration():
  if Bladex.GetVibration():
    return 0
  else:
    return 1

def ReworkedCamera():
  if Bladex.GetReworkedCamera():
    return 0
  else:
    return 1

## Blood evaporation
# Traducir
def SetBloodEvaporation(option):
	a = Bladex.GetCurrentMap()
	lar = len(a)
	if lar>5:
		a = a[lar-4:lar]
	else:
		a = ""

	if string.upper(a)!="BACK":

		if option=="Active":
			Blood.Evaporation = 1
		else:
			Blood.Evaporation = 0
		SaveConfiguration()


def BloodEvaporationSettings():

  if Blood.Evaporation:
    return 0
  else:
    return 1

##  Screen mode
def SetScreenModeValue(v,target):
  # print "Set Screen mode"
  screenMode = -1
  if(v == "Windowed"):
    screenMode = 0
  elif(v == "Fullscreen"):
    screenMode = 1
  elif(v == "Borderless"):
    screenMode = 2

  if(screenMode != -1):
    Bladex.SetScreenMode(screenMode)
    target.Parent.MenuItems[1].focusable = screenMode==1
    target.Parent.MenuItems[1].SetSelOption(GetActiveMonitor())

def GetScreenMode():
  return Bladex.GetScreenMode()

##  Monitor
def GetNumMonitor():
  monitors = []
  for i in range(0, Bladex.GetNumMonitor()):
    monitors.append(MenuText.GetMenuText(str(i + 1)))
  return monitors

def GetActiveMonitor():
  return Bladex.GetActiveMonitor()

def SetActiveMonitorValue(v):
  Bladex.SetActiveMonitor(int(v) - 1)
  return

## Aspect Ratio
def GetAspectRatio():
  # TODO
  return 0

def SetAspectRatioValue(v):
  # TODO
  return

## Résolution
supported_res = []

def GetResolutionValue():
  i = 0
  global supported_res
  if(len(supported_res) == 0):
    supported_res = Bladex.GetSupportedResolution()
  res = Bladex.GetResolution()

  for r in supported_res:
    if(r == res):
      break
    i = i + 1

  if(i == len(supported_res)):
    i = -1

  return i

def GetSupportedResolution():
  global supported_res
  supported_res = Bladex.GetSupportedResolution()
  res_list = []
  for r in supported_res:
    res_list.append(MenuText.GetMenuText(str(r[0]) + "x" + str(r[1])))
  return res_list

def FocusableWhenFullScreen(target):
  target.focusable = Bladex.GetScreenMode()==1
  return 0

def FocusableWhenWindowed(target):
  target.focusable = not Bladex.GetScreenMode()==1
  return 0

def SetResolutionValue(v):
  str = string.split(v, "x")
  width = str[0]
  height = str[1]
  Bladex.SetResolution(int(width), int(height))

## Vertical Sync
def GetVerticalSync():
  return Bladex.GetVerticalSync()

def SetVerticalSyncValue(option):
  Bladex.SetVerticalSync(option=="Yes")
  return

def GetLimitFps():
  return Bladex.GetLimitFps()

def SetLimitFps(option):
  Bladex.SetLimitFps(option=="Yes")
  return

## Correcci�n Gamma
def GetGammaValue():
  return Raster.GetGammaCorrection()

def SetGammaValue(v):
  Raster.SetGammaCorrection(v)

## Correcci�n Brightness
def GetBrightnessValue():
  return Raster.GetBrightness()

def SetBrightnessValue(v):
  Raster.SetBrightness(v)

def setFXVolume(v):
  Bladex.SetSoundVolume(v * 0.1)
  SndCorreGema.PlayStereo()

def setMusicVolume(v):
  sound_cfg_changed=1
  Bladex.SetMusicVolume(v*0.1)

## Correcci�n Contrast
def GetContrastValue():
  return Raster.GetContrast()

def SetContrastValue(v):
  Raster.SetContrast(v)

def ResetVideo(option):
	_MainMenu.DeActivateMenuItem()
	Raster.SetGammaCorrection(0.5)
	Raster.SetContrast(0.5)
	Raster.SetBrightness(0)
	_MainMenu.ActivateMenuItem()

# OPTIONS/SOUND FUNCTION CALLS----------------
## Volumen de sonido
def GetSoundValue():
  return int(10*Bladex.GetSoundVolume())

def SetSoundValue(v):
  global sound_cfg_changed
  sound_cfg_changed=1

  return Bladex.SetSoundVolume(v*0.1)

## Volumen de la musica
def GetMusicValue():
  return int(10*Bladex.GetMusicVolume())


def SetMusicValue(v):
  global sound_cfg_changed
  sound_cfg_changed=1

  return Bladex.SetMusicVolume(v*0.1)



def GetSoundQuality():
    global last_ss_quality
    last_ss_quality=Bladex.GetSSQuality()
    return Bladex.GetSSQuality()


def SetSoundQuality(option):
    global last_ss_quality
    if option == "High":
        #Bladex.SetSSQuality(2)
        last_ss_quality=2
        return 2
    if option == "Med":
        #Bladex.SetSSQuality(1)
        last_ss_quality=1
        return 1
    if option == "Low":
        #Bladex.SetSSQuality(0)
        last_ss_quality=0
        return 0

def GetSubtitlesEnable():
  return Bladex.GetSubtitlesEnable()

def SetSubtitlesEnable(option):
  global sound_cfg_changed
  sound_cfg_changed=1
  Bladex.SetSubtitlesEnable(option=="Yes")


def GetValidFieldsOfView():
  min = int(90)
  max = int(170)
  return (min, max,int(max-min))

def GetCurrentFieldOfView():
  return Bladex.GetFieldOfView()

def SetCurrentFieldOfView(value):
  Bladex.SetFieldOfView(value)
  SaveConfiguration()

def GetAntialiasing():
  return Bladex.GetAntialiasing()

def SetAntialiasing(option):
  Bladex.SetAntialiasing(option=="Yes")
  return 0

def GetHideUI():
  return Bladex.GetHideUI()

def SetHideUI(value):
  Bladex.SetHideUI(value == "Yes")
  SaveConfiguration()

def GetUIScale():
  return Bladex.GetUIScaleFactor()

def SetUIScale(value):
  if value == "Big":
    Bladex.SetUIScaleFactor(2)
  if value == "Normal":
    Bladex.SetUIScaleFactor(1)
  if value == "Small":
    Bladex.SetUIScaleFactor(0)

  SaveConfiguration()

#---
#def GetEAX():
#	return Bladex.GetEAXOverride()
#
#
#def SetEAX(option):
#	global sound_cfg_changed
#	sound_cfg_changed=1
#
#	if option == "Enabled":
#		Bladex.SetEAXOverride(0)
#		#a = "hacer algo"
#	if option == "Disabled":
#		Bladex.SetEAXOverride(1)
#		#a = "hacer algo"
#---
def GetSpeakerConfig():
    return Bladex.GetSpeakerConfig()


def SetSpeakerConfig(option):
    global sound_cfg_changed
    sound_cfg_changed=1

    if option == "Mono":
        Bladex.SetSpeakerConfig(0)
    if option == "2 Speakers":
        Bladex.SetSpeakerConfig(1)
    if option == "4 Speakers":
        Bladex.SetSpeakerConfig(2)
    if option == "5.1":
        Bladex.SetSpeakerConfig(3)
    if option == "7.1":
        Bladex.SetSpeakerConfig(4)


#---------------------------------------------

#def GetMouseInvert():
#	MouseData = Bladex.GetMouseState()
#	return MouseData[0]

#def SetMouseInvert(option):
#	MouseData = Bladex.GetMouseState()
#	if option == "Yes":
#		Bladex.SetMouseState(0,MouseData[1],MouseData[2])
#	else:
#		Bladex.SetMouseState(1,MouseData[1],MouseData[2])

## De-Facing Values
def GetDeFacingValue():
  return int( Bladex.GetAecGap() )

def SetDeFacingValue(v):
  i = Bladex.SetAecGap(v)
  SaveConfiguration()
  return  i


#Inicio de TravelBook
#def ExecTravelBook(menu_class):
#	if Reference.DEMO_MODE==1:
#		return
#	import Scorer
#	Scorer.HideTBS()
#	hWnd = Bladex.GetWindowId()
#
#	print "Executing Travel Book..."
#	# Status File Setup
#	StatusFile = open("../../TravelBook/status.txt", "w")
#
#	BarbEquipementFile = None
#	AmazonEquipementFile = None
#	DwarfEquipementFile = None
#	KnightEquipementFile = None
#
#	char = Bladex.GetEntity("Player1")
#	Inventory = char.GetInventory()
#
#	# CHARACTER TYPE AND MAIN AVAILABLE LINKS---------
#
#	# Character Characteristics_____
#	if char.Kind == "Barbarian_N":
#		StatusFile.write("Barbarian\n")	# Character Barabarian
#	#	if Bladex.GetCurrentMap != "Barb-M1"  : StatusFile.write("cc\n")			# ! First Map 4 this character
#

#		StatusFile.write("Amazon\n")		# Character Amazon
#	#	if Bladex.GetCurrentMap != "Ruins-M4" : StatusFile.write("cc\n")			# ! First Map 4 this character
#
#	if char.Kind == "Dwarf_N":
#		StatusFile.write("Dwarf\n")			# Character Dwarf
#	#	if Bladex.GetCurrentMap != "Dwarf_M3" : StatusFile.write("cc\n")			# ! First Map 4 this character
#
#	if char.Kind == "Knight_N":
#		StatusFile.write("Knight\n")		# Character Knight
#	#	if Bladex.GetCurrentMap != "Ragnar-M2": StatusFile.write("cc\n")			# ! First Map 4 this character
#
#	StatusFile.write("cc\n")			# Making Character Characteristics available.
#
#	# Creation History Link________
#	if (Inventory.nTablets > 0):
#		StatusFile.write("ch\n")
#
#	if len(GotoMapVars.BaList):
#		StatusFile.write("ba\n")
#
#	StatusFile.close()
#	#-------------------------------------------------
#
#	# SKILL FILE--------------------------------------
#	SkillFile	= open("../../TravelBook/Character Characteristics/Skills/Character Skills.txt", "w")
#	list = Bladex.GetCombos("Player1") # Also 2 be used for Specific Weapon Combos
#	for i in range(len(list)):
#		if list[i][1] == 0:
#			SkillFile.write("New")
#		SkillFile.write(list[i][0])
#		SkillFile.write("\n")
#	SkillFile.close()
#	#-------------------------------------------------
#
#	# EQUIPEMENT FILE---------------------------------
#	BarbEquipementFile		= open("../../TravelBook/Character Characteristics/Equipement/Barb/Carried Equipement.txt", "w")
#	AmazonEquipementFile	= open("../../TravelBook/Character Characteristics/Equipement/Amazon/Carried Equipement.txt", "w")
#	DwarfEquipementFile		= open("../../TravelBook/Character Characteristics/Equipement/Dwarf/Carried Equipement.txt", "w")
#	KnightEquipementFile	= open("../../TravelBook/Character Characteristics/Equipement/Knight/Carried Equipement.txt", "w")
#
#	BarbShieldsFile			= open("../../TravelBook/Character Characteristics/Equipement/Barb/Carried Shields.txt", "w")
#	AmazonShieldsFile		= open("../../TravelBook/Character Characteristics/Equipement/Amazon/Carried Shields.txt", "w")
#	DwarfShieldsFile		= open("../../TravelBook/Character Characteristics/Equipement/Dwarf/Carried Shields.txt", "w")
#	KnightShieldsFile		= open("../../TravelBook/Character Characteristics/Equipement/Knight/Carried Shields.txt", "w")
#
#
#	# Race-Ordered Weapons
#	KnightWeaps = [	"QueenSword","IceSword","FireSword","Gladius","Orksword","Espadaelfica" ,
#					"Espadaromana","Espadacurva","Dagesse","Cimitarra","EgyptSword","Espadafilo" ,
#					"Espada","Maza","Maza2","Maza3"]
#
#	DwarfWeaps = [	"CrushHammer","FireAxe","IceHammer","Hacha","Hacha5","Hacha4","Hacha3",
#					"Hacha6","Hacha2","Garrote","Martillo","Martillo2","Garropin","MazaDoble" ,
#					"Garrote2","Martillo3"]
#
#	AmazonWeaps = [	"TaiSword","SteelFeather","FireBo","LightEdge","Ninjato",
#					"HookSword","Katana" ,"DoubleSword","Bo","Lanza","Naginata","Tridente",
#					"Hachacuchilla","Naginata2","DeathBo","CrushBo"]
#
#	BarbWeaps  = [	"FireBigSword","IceAxe","DalWeapon","Sablazo","Chaosword",
#					"DeathSword","LongSword","Alfanje","BigSword","SawSword","FlatSword",
#					"Eclipse","Guadanya","Hacha2hojas","RhinoClub","Hacharrajada"]
#
#	ShowableItems = []
#
#	InventoryList = []
#
#	for i in range(Inventory.nWeapons):
#		Weapon = Inventory.GetWeapon(i)
#		RootWeapon = Bladex.GetEntity(Weapon)
#		InventoryList.append(RootWeapon.Kind)
#
#	# Fromerly picked Weapons___
#	TakenObjects = char.Data.GetObjectsTaken()
#
#	# ITEMS FILE________________
#	ItemsFile	= open("../../TravelBook/Character Characteristics/Items/Carried Items.txt", "w")
#	for i in range(Inventory.nKindObjects):
#		Object = Inventory.GetObject(i)
#		RootObject = Bladex.GetEntity(Object)
#		ItemsFile.write(RootObject.Kind)
#		ItemsFile.write("\n")
#
#	ItemsFile.close()
#	#---------------------------
#
#	# FORMERLY PICKED WEAPONS___
#	for i in TakenObjects:
#		if not InventoryList.count(i):
#			if (BarbWeaps.count(i)):
#				BarbEquipementFile.write(i)
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				BarbEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					BarbEquipementFile.write(combo[0])
#					BarbEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					BarbEquipementFile.write("none\n")
#
#
#			if (AmazonWeaps.count(i)):
#				AmazonEquipementFile.write(i)
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				AmazonEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					AmazonEquipementFile.write(combo[0])
#					AmazonEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					AmazonEquipementFile.write("none\n")
#
#
#			if (DwarfWeaps.count(i)):
#				DwarfEquipementFile.write(i)
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				DwarfEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					DwarfEquipementFile.write(combo[0])
#					DwarfEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					DwarfEquipementFile.write("none\n")
#
#
#			if (KnightWeaps.count(i)):
#				KnightEquipementFile.write(i)
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				KnightEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					KnightEquipementFile.write(combo[0])
#					KnightEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					KnightEquipementFile.write("none\n")
#
#
#	WrittenWeapons = []
#
#	# CARRIED WEAPONS___________
#	for i in range(Inventory.nWeapons):
#		Weapon = Inventory.GetWeapon(i)
#		RootWeapon = Bladex.GetEntity(Weapon)
#		if not WrittenWeapons.count(RootWeapon.Kind):
#			WrittenWeapons.append(RootWeapon.Kind)
#
#			# Weapon is Barbarian's
#			if(BarbWeaps.count(RootWeapon.Kind)):
#				i = RootWeapon.Kind
#				BarbEquipementFile.write(i)
#				BarbEquipementFile.write("_i")
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				BarbEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					if not BarbEquipementFile.write(combo[1]) == 0:
#						BarbEquipementFile.write("New")
#					BarbEquipementFile.write(combo[0])
#					BarbEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					BarbEquipementFile.write("none\n")
#
#			# Weapon is Amazon's
#			if(AmazonWeaps.count(RootWeapon.Kind)):
#				i = RootWeapon.Kind
#				AmazonEquipementFile.write(i)
#				AmazonEquipementFile.write("_i")
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				AmazonEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					if not AmazonEquipementFile.write(combo[1]) == 0:
#						AmazonEquipementFile.write("New")
#					AmazonEquipementFile.write(combo[0])
#					AmazonEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					AmazonEquipementFile.write("none\n")
#
#			# Weapon is Dwarf's
#			if(DwarfWeaps.count(RootWeapon.Kind)):
#				i = RootWeapon.Kind
#				DwarfEquipementFile.write(i)
#				DwarfEquipementFile.write("_i")
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				DwarfEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					if not DwarfEquipementFile.write(combo[1]) == 0:
#						DwarfEquipementFile.write("New")
#					DwarfEquipementFile.write(combo[0])
#					DwarfEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					DwarfEquipementFile.write("none\n")
#
#			# Weapon is Knight
#			if(KnightWeaps.count(RootWeapon.Kind)):
#				i = RootWeapon.Kind
#				KnightEquipementFile.write(i)
#				KnightEquipementFile.write("_i")
#				WC = Bladex.GetWeaponCombos("Player1",i)
#				KnightEquipementFile.write("\n")
#				c = 0
#				for combo in WC:
#					if not KnightEquipementFile.write(combo[1]) == 0:
#						KnightEquipementFile.write("New")
#					KnightEquipementFile.write(combo[0])
#					KnightEquipementFile.write("\n")
#					c = c+1
#				for counter in range(4 - c):
#					KnightEquipementFile.write("none\n")
#
#	WrittenShields = []
#	# Carried Shiels___________
#	for i in range(Inventory.nShields):
#		Shield = Inventory.GetShield(i)
#		RootShield = Bladex.GetEntity(Shield)
#		if not WrittenShields.count(RootShield.Kind):
#			WrittenShields.append(RootShield.Kind)
#
#			#if RootShield is Barb's
#			BarbShieldsFile.write(RootShield.Kind)
#			BarbShieldsFile.write("_i")
#			BarbShieldsFile.write("\n")
#
#			#if RootShield is Amazon's
#			AmazonShieldsFile.write(RootShield.Kind)
#			AmazonShieldsFile.write("_i")
#			AmazonShieldsFile.write("\n")
#
#			#if RootShield is Dwarf's
#			DwarfShieldsFile.write(RootShield.Kind)
#			DwarfShieldsFile.write("_i")
#			DwarfShieldsFile.write("\n")
#
#			#if RootShield is Knight's
#			KnightShieldsFile.write(RootShield.Kind)
#			KnightShieldsFile.write("_i")
#			KnightShieldsFile.write("\n")
#	# FORMERLY CARRIED SHIELDS___________
#	Shield = [	"Escudo1","Escudo2","Escudo3","Escudo4","Escudo5","Escudo6","Escudo7",
#				"Escudo8","Escudo9","Escudon","VampShield","DalShield","KingShield"]
#
#	for Obj in TakenObjects:
#		if not InventoryList.count(Obj):
#			if Shield.count(Obj):
#				KnightShieldsFile.write(RootShield.Kind)
#				KnightShieldsFile.write("\n")
#				DwarfShieldsFile.write(RootShield.Kind)
#				DwarfShieldsFile.write("\n")
#				BarbShieldsFile.write(RootShield.Kind)
#				BarbShieldsFile.write("\n")
#				AmazonShieldsFile.write(RootShield.Kind)
#				AmazonShieldsFile.write("\n")
#
#	#if it is a shield
#	# if it is not in inventory
#	#write shield
#
#	BarbEquipementFile.close()
#	AmazonEquipementFile.close()
#	DwarfEquipementFile.close()
#	KnightEquipementFile.close()
#
#	BarbShieldsFile.close()
#	AmazonShieldsFile.close()
#	DwarfShieldsFile.close()
#	KnightShieldsFile.close()
#	#-------------------------------------------------
#
#	# DIARY WRITING-----------------------------------
#	# Writting Fuct--------------------
#	count = 1
#	for imapa in range(len(GotoMapVars.MText)):
#		MFile = open("../../TravelBook/Kingdom History/M"+`imapa + 1`+".txt", "w")
#		for texto in GotoMapVars.MText[imapa]:
#			if (texto[0] == "T" and texto[1] == "T"):
#				MFile.write(texto)
#				MFile.write(str(count))
#				count = count + 1
#			else :
#				MFile.write(texto)
#				if char.Kind == "Barbarian_N":
#					MFile.write("Bar")
#				if char.Kind == "Amazon_N":
#					MFile.write("Amz")
#				if char.Kind == "Dwarf_N":
#					MFile.write("Dwf")
#				if char.Kind == "Knight_N":
#					MFile.write("Kgt")
#			MFile.write(".htm")
#			MFile.write("\n")
#		MFile.close()
#	#----------------------------------
#	#-------------------------------------------------
#	# CREATION HISTORY--------------------
#	count = 1
#	MFile = open("../../TravelBook/Creation History/status.txt", "w")
#	for imapa in range(len(GotoMapVars.MText)):
#		for texto in GotoMapVars.MText[imapa]:
#			if (texto[0] == "T" and texto[1] == "T"):
#				MFile.write("CH")
#				MFile.write(str(count))
#				count = count + 1
#				MFile.write("\n")
#	MFile.close()
#	#----------------------------------
#	# BLADE ATHEM--------------------
#	MFile = open("../../TravelBook/The Blade Athem/status.txt", "w")
#	for mapp in GotoMapVars.BaList:
#		MFile.write(mapp)
#		MFile.write("\n")
#	MFile.close()
#	#----------------------------------
#
#	Bladex.SetInputMode("Mouse","UNACQUIRE")
#	Bladex.SetInputMode("Keyboard","UNACQUIRE")
#	BIPCx.CreateNewProcess("../../TravelBook/BladeTBW.exe",hWnd)
#	BIPCx.CreateNewProcess("../../TravelBook/TravelBook.exe",hWnd)
#	print "Waiting..."
#	print BIPCx.WaitCommand()
#	Bladex.SetInputMode("Mouse","ACQUIRE")
#	Bladex.SetInputMode("Keyboard","ACQUIRE")





_MainMenu=None

TB_ACTIVATED=0


def ActivateMenu(caller_id = None):
  if caller_id == None:
    Bladex.TriggerEventInner()
  try:
    AppMode=Bladex.GetAppMode()
  except x:
    print "Error getting AppMode",x

  # Do some python garbage collection
  ObjStore.CheckStore()

  if AppMode=="Game" or AppMode=="Demo":

    if AppMode=="Demo":
        import Demo_Stuff
        if Demo_Stuff.demo_is_active==1:
            #pdb.set_trace()
            print "ERROR - Menu.ActivateMenu()"
            print "Fix with a path but should NOT happen!!!"
            Demo_Stuff.DemoLoop()
            return

    global _MainMenu

    # Stop Music
    # Start Music
    #Bladex.KillMusic()

    _MainMenu=MainMenu("Menu Principal",Desc1)
    NetMisc.SetMainMenu(_MainMenu)

    #print "Reference count _MainMenu.wMenu: (recien creado)",sys.getrefcount(_MainMenu.wMenu)

    _MainMenu.MenuStack.Push(_MainMenu.wMenu)

    InputManager=BInput.GetInputManager()
    oldInputActionsSet=InputManager.GetInputActionsSet()
    InputManager.SetInputActionsSet("Menu")

    # Acciones de los men�s.
    Bladex.AddInputAction("Menu Next",0)
    Bladex.AddInputAction("Menu Prev",0)
    Bladex.AddInputAction("Menu Inc",0)
    Bladex.AddInputAction("Menu Dec",0)
    Bladex.AddInputAction("Menu ActivateItem",0)
    Bladex.AddInputAction("Menu DeActivateItem",0)
    Bladex.AddInputAction("Menu Supr",0)
    Bladex.AddInputAction("Menu Next Strong",0)
    Bladex.AddInputAction("MenuToggleHiRes",0)


    # Teclas de los men�s.
    # Bladex.AssocKey("Menu Next","Keyboard","S")
    Bladex.AssocKey("Menu Next","Keyboard","Down")
    Bladex.AssocKey("Menu Next","Gamepad","JoyDown")
    Bladex.AssocKey("Menu Next","Gamepad","ButtonDown")
    Bladex.AddBoundFunc("Menu Next",_MainMenu.MenuNextItem)
    BInput.TranslateInputFromTo("Backwards","Menu Next")

    
    # Bladex.AssocKey("Menu Prev","Keyboard","W")
    Bladex.AssocKey("Menu Prev","Keyboard","Up")
    Bladex.AssocKey("Menu Prev","Gamepad","JoyUp")
    Bladex.AssocKey("Menu Prev","Gamepad","ButtonUp")
    Bladex.AddBoundFunc("Menu Prev",_MainMenu.MenuPrevItem)
    BInput.TranslateInputFromTo("Forwards","Menu Prev")

    # Bladex.AssocKey("Menu Inc","Keyboard","D")
    Bladex.AssocKey("Menu Inc","Keyboard","Right")
    Bladex.AssocKey("Menu Inc","Gamepad","JoyRight")
    Bladex.AssocKey("Menu Inc","Gamepad","ButtonRight")
    Bladex.AssocKey("Menu Inc","Gamepad","ButtonRightTrigger")
    Bladex.AssocKey("Menu Inc","Gamepad","ButtonRightShoulder")
    Bladex.AddBoundFunc("Menu Inc",_MainMenu.MenuIncItem)
    BInput.TranslateInputFromTo("Turn Right","Menu Inc")

    # Bladex.AssocKey("Menu Dec","Keyboard","A")
    Bladex.AssocKey("Menu Dec","Keyboard","Left")
    Bladex.AssocKey("Menu Dec","Gamepad","JoyLeft")
    Bladex.AssocKey("Menu Dec","Gamepad","ButtonLeft")
    Bladex.AssocKey("Menu Dec","Gamepad","ButtonLeftTrigger")
    Bladex.AssocKey("Menu Dec","Gamepad","ButtonLeftShoulder")
    Bladex.AddBoundFunc("Menu Dec",_MainMenu.MenuDecItem)
    BInput.TranslateInputFromTo("Turn Left","Menu Dec")

    Bladex.AssocKey("Menu Supr","Keyboard","Backspace")
    Bladex.AssocKey("Menu Supr","Gamepad","ButtonNorth")
    Bladex.AddBoundFunc("Menu Supr",_MainMenu.MenuSuprItem)

    Bladex.AssocKey("Menu ActivateItem","Keyboard","Enter")
    Bladex.AssocKey("Menu ActivateItem","Gamepad","ButtonSouth")
    Bladex.AddBoundFunc("Menu ActivateItem",_MainMenu.ActivateMenuItem)


    #Bladex.AssocKey("Menu DeActivateItem","Keyboard","Backspace")
    Bladex.AssocKey("Menu DeActivateItem","Keyboard","Esc")
    Bladex.AssocKey("Menu DeActivateItem","Keyboard","F1")
    Bladex.AssocKey("Menu DeActivateItem","Gamepad","ButtonStart")
    Bladex.AssocKey("Menu DeActivateItem","Gamepad","ButtonBack")
    Bladex.AssocKey("Menu DeActivateItem","Gamepad","ButtonEast")
    Bladex.AddBoundFunc("Menu DeActivateItem",_MainMenu.DeActivateMenuItem)

    Bladex.AssocKey("Menu Next Strong","Keyboard","Tab")
    Bladex.AddBoundFunc("Menu Next Strong",_MainMenu.MenuNextItemStrong)

    InputManager=BInput.GetInputManager()
    InputManager.SetInputActionsSet("Menu")
    if Reference.DEMO_MODE==0:
        if netgame.GetNetState() == 0:
           SaveGame.CreateSaveMenu()

    #print "Reference count _MainMenu.wMenu: (fin de ActivateMenu())",sys.getrefcount(_MainMenu.wMenu)
    #Bladex.SetAppMode("Menu")
  elif AppMode=="Menu":
    # Start Music
    #Bladex.ExeMusicEvent(Bladex.GetMusicEvent("MenuMusic"))
    #print "Reference count _MainMenu.wMenu:",sys.getrefcount(_MainMenu.wMenu)
    #print "Reference count _MainMenu:",sys.getrefcount(_MainMenu)
    Bladex.AddScheduledFunc(Bladex.GetTime(),ClearMenuKeyb,())

    Bladex.SetAppMode("Game")


    if netgame.GetNetState() == 0:
      import Scorer
      Scorer.ActivateScorer()
    else:
      NetScorer.ActivateScorer()

    Raster.SetTextMode(3)

    global TB_ACTIVATED
    global MENU_PREACTIVATED

    if TB_ACTIVATED:
      MENU_PREACTIVATED=0
      TB_ACTIVATED=0
      Raster.SetTextShadow(2, 2)

  else:
    print "Invalid AppMode"

  Raster.RemoveBackgroundImage()
  print "End ActivateMenu()"

MENU_PREACTIVATED = 0
def PreActivateMenu():
	global MENU_PREACTIVATED
	if not MENU_PREACTIVATED:
		ActivateMenu()
		MENU_PREACTIVATED = 1
	else:
		_MainMenu.DeActivateMenuItem() # :NOTE: workaround to be able to get out of the menu
		print "-----------------------------"
		print "   Sorry Gary!                "
		print "   May be next time      "
		print "-----------------------------"

def ClearMenuKeyb():
  InputManager=BInput.GetInputManager()
  InputManager.SetInputActionsSet("Menu")

  global _MainMenu

  #print "Reference count _MainMenu:",sys.getrefcount(_MainMenu)

  Bladex.RemoveInputAction("Menu Next")
  Bladex.RemoveInputAction("Menu Prev")
  Bladex.RemoveInputAction("Menu Inc")
  Bladex.RemoveInputAction("Menu Dec")
  Bladex.RemoveInputAction("Menu ActivateItem")
  Bladex.RemoveInputAction("Menu DeActivateItem")
  Bladex.RemoveInputAction("Menu Supr")
  Bladex.RemoveInputAction("Menu Next Strong")
  Bladex.RemoveInputAction("MenuToggleHiRes")

  #print "Reference count _MainMenu: (Antes ->None)",sys.getrefcount(_MainMenu)
  _MainMenu=None
  #print "Reference count _MainMenu: (Asignacion -> None)",sys.getrefcount(_MainMenu)

  InputManager.SetInputActionsSet("Default")








wNULL_MenuParent=BUIx.CreateNULLWidget()

class MainMenu:
  def __init__(self,Name,MenuDescription):
    #Bldb.set_trace()
    self.Name=Name
    self.MenuDescription=MenuDescription
    #BBLib.ReadMMP("../../Data/NewLogo.mmp")
    self.MenuStack=MenuWidget.MenuStack(ActivateMenu)
    self.wMenu=MenuWidget.B_MenuTree(wNULL_MenuParent,self.MenuDescription,self.MenuStack)
    self.wMenu.SetAutoScale(1)

#Raster.LoadBitmap("Background","../../Data/Menu.bmp")

  def __del__(self):
    self.MenuStack.Reset()
    self.MenuStack=None
    self.wMenu=None


  def ActivateMenuItem(self):
    if Bladex.GetAppMode()=="Menu":
      wActiveMenuElement=self.MenuStack.Top().GetFocus()
      try:
        sw=wActiveMenuElement.GetFocus()
        sw.ActivateItem(1)
      except:
        wActiveMenuElement.ActivateItem(1)
      #print "Act"
      #PlaySound(SndNewMenu)
      SndNewMenu.PlayStereo()


  def DeActivateMenuItem(self):
    global EscapeFunction
    if Bladex.GetAppMode()=="Menu":
      Bladex.SetGamepadChangeFunc()
      if ((self.MenuStack.nItems() == 1) and (EscapeFunction!=None)):
        if(EscapeFunction(0)):
          return

      global MENU_PREACTIVATED
      MENU_PREACTIVATED = 0

      wActiveMenuElement=self.MenuStack.Top().GetFocus()
      try:
        sw=wActiveMenuElement.GetFocus()
        sw.ActivateItem(0)
      except:
        wActiveMenuElement.ActivateItem(0)
      #print "Deact"


      #
      # Do we have to  change the quality of the sound?
      #
      global last_ss_quality
      global sound_cfg_changed
      if last_ss_quality!=-1 and last_ss_quality<>Bladex.GetSSQuality():
        print "Reseting sound quality"
        Bladex.SetSSQuality(last_ss_quality)
      else:
        if sound_cfg_changed==1:
            Bladex.SaveSSConfig()
            sound_cfg_changed=0

      SndNewMenu.PlayStereo()

  def MenuNextItemStrong(self):
    w=self.MenuStack.Top()
    w.NextFocus()

  def MenuNextItem(self):
  	global TBUDSoundAble
	w=self.MenuStack.Top()
	sw=w.GetFocus()
	#PlaySound(SndCorreGema)
	if TBUDSoundAble:
		SndCorreGema.PlayStereo()
	try:
		sw.NextFocus()
	except:
		w.NextFocus()


  def MenuPrevItem(self):
	w=self.MenuStack.Top()
	sw=w.GetFocus()
	#PlaySound(SndCorreGema)
	if TBUDSoundAble:
		SndCorreGema.PlayStereo()
	try:
		sw.PrevFocus()
	except:
		w.PrevFocus()


  def MenuIncItem(self):
    w=self.MenuStack.Top()
    try:
      sw=w.GetFocus()
      #print "Increasing spin value"
      sw.IncMenuItem()
    except AttributeError:
      try:
        w.IncMenuItem()
      except AttributeError:
         pass
      #print "cant increase any more"#Seems not 2 be working this way

  def MenuDecItem(self):
    w=self.MenuStack.Top()
    try:
      sw=w.GetFocus()
      sw.DecMenuItem()
      #print "Decreasing spin value"
    except AttributeError:
      try:
        w.DecMenuItem()
      except AttributeError:
         pass
      #print "cant decrease any more"#Seems not 2 be working this way


  def MenuSuprItem(self):
    print "MenuSuprItem(self)"
    w=self.MenuStack.Top().GetFocus()
    try:
      sw=w.GetFocus()
      sw.SuprMenuItem()
    except AttributeError:
      try:
        w.SuprMenuItem()
      except AttributeError:
         pass


  def CommandPrb(self):
    print "Method CommandPrb"

  def EndMenu(self):
    while len(self.MenuStack.Top())>0:
      self.DeActivateMenuItem()

#class B_MenuItemLogo(BUIx.B_FrameWidget,MenuWidget.B_MenuTreeItem):
#  def __init__(self,Parent,MenuDescr,StackMenu):
#    BUIx.B_FrameWidget.__init__(self,Parent,MenuDescr["Name"],512,128)
#    MenuWidget.B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)

#    self.bm1=BUIx.B_BitmapWidget(Parent,"logobm1",640,480,"Logo1")
#    self.bm1.SetColor(255,255,255)
#    self.bm1.SetAlpha(1.0)


#    self.bm2=BUIx.B_BitmapWidget(Parent,"logobm2",256,128,"Logo2")
#    self.bm2.SetColor(255,255,255)
#    self.bm2.SetAlpha(1.0)

#    self.subbm1=BUIx.B_BitmapWidget(Parent,"sublogobm1",256,128,"LogoSub1")
#    self.subbm1.SetColor(255,255,255)
#    self.subbm1.SetAlpha(1.0)

#    self.subbm2=BUIx.B_BitmapWidget(Parent,"sublogobm2",256,128,"LogoSub2")
#    self.subbm2.SetColor(255,255,255)
#    self.subbm2.SetAlpha(1.0)

#    self.AddWidget(self.bm1,0,0,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

#    self.AddWidget(self.bm2,0,0,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

#    self.AddWidget(self.subbm1,0,0,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
#    self.AddWidget(self.subbm2,0,0,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

#    self.Vid=WidgetsExtra.B_VideoWidget(self,"video logo","../../Data/Sangre.avi") #video\\Main.avi)#
    #self.Vid=WidgetsExtra.B_VideoWidget(self,"video logo","../../Data/vid_hom.avi")
    #print "B_MenuItemLogo.Vid",self.Vid,"with refcount",sys.getrefcount(self.Vid)
#    self.AddWidget(self.Vid,0.5,1,
#                   BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
#                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    #print "B_MenuItemLogo.Vid",self.Vid,"with refcount",sys.getrefcount(self.Vid)
#    self.thisown=1


#  def AcceptsFocus(self):
#    return 0

#  def __del__(self):
#    BUIx.B_FrameWidget.__del__(self)
#    MenuWidget.B_MenuTreeItem.__del__(self)
#    #print "B_MenuItemLogo.Vid",self.Vid,"with refcount",sys.getrefcount(self.Vid)
#    self.Vid.SetDrawFunc(None)  #Parche, si no no se llama a __del__()
#    #print "B_MenuItemLogo.Vid (DrawFunc -> None)",self.Vid,"with refcount",sys.getrefcount(self.Vid)
#    self.Vid=None
#    #print "B_MenuItemLogo.__del__()"











CtrlsPosition=(70, BUIx.B_FrameWidget.B_FR_AbsoluteLeft, BUIx.B_FrameWidget.B_FR_Left)
def AuxCtrlDef(action_menu_name,action_name,kFlags):
    res = {"Name":MenuText.GetMenuText(action_menu_name),
             "Position" :CtrlsPosition,
             "Action"   :action_name,
             "Kind"     :KeybWidget.ControlMenuItem,
             "kFlags"   :kFlags,
             "VSep" : 34,
             "Size" :(200,300)
            }
    if Language.Current == "Chinese":
        res["Font"] = Language.CtrlMenu
    return res
KeybActions=[]
for k in acts.ConfigurableActions:
  KeybActions.append(AuxCtrlDef(k[0],k[1],k[2]))








#LogoItem={"Name":"Logo",
#          "VSep":50,
#          "Kind":B_MenuItemLogo
#         }




#OpenGLOptions=[{"Name":MenuText.GetMenuText("Screen Mode"),
#                "VSep":30,
#                "Kind":MenuWidget.B_MenuItemOption,
#                "Options":[MenuText.GetMenuText("Full Screen"),MenuText.GetMenuText("Windowed")],
#                "Command":SetFullScreenMode,
#                "SelOptionFunc":FullScreenModeSettings
#               },
#               {"Name":MenuText.GetMenuText("OpenGL 2")}
#              ]


def GoTo2d(menu_class):
	import GotoMapVars
	GotoMapVars.EndOfLevel()


vsepexit=120

if Reference.DEMO_MODE:
    QuitMenu  =            {"VSep":-1000,
                            "Size":(640,480),
                            "Name"     :MenuText.GetMenuText("EXIT"),
                            "Font"     :MenuFontBig,
                            "iFocus"   :2,
                            "ListDescr":[ {"Name":MenuText.GetMenuText("Exit: are you sure?"),
                                           "VSep":vsepexit,
                                           "Font":MenuFontBig,
                                           "Kind":MenuWidget.B_MenuItemTextNoFXNoFocus
                                          },
                                          {"Name":MenuText.GetMenuText("Yes"),
                                           "VSep":10,
                                           "Font":MenuFontMed,
                                           "ListDescr":[ {"Name":"Features",
                                                          "Kind":MenuWidget.B_BackFeatures
                                                         },
                                                         {"Name":" "},
                                                       ]
                                          },
                                          {"Name":MenuText.GetMenuText("No"),
                                           "VSep":1,
                                           "Font":MenuFontMed,
                                           "Command":BackMenu
                                          },
                                          {"Name":"Back",
                                           "Kind":MenuWidget.B_BackBlank
                                          }
                                        ]
                           }

else:
    QuitMenu  =            {"VSep":-1000,
                            "Size":(640,480),
                            "Name"     :MenuText.GetMenuText("EXIT"),
                            "Font"     :MenuFontBig,
                            "iFocus"   :2,
                            "ListDescr":[ {"Name":MenuText.GetMenuText("Exit: are you sure?"),
                                           "VSep":vsepexit,
                                           "Font":MenuFontBig,
                                           "Kind":MenuWidget.B_MenuItemTextNoFXNoFocus
                                          },
                                          {"Name":MenuText.GetMenuText("Yes"),
                                           "VSep":10,
                                           "Command":CmdQuit,
                                           "Font":MenuFontMed
                                          },
                                          {"Name":MenuText.GetMenuText("No"),
                                           "VSep":1,
                                           "Font":MenuFontMed,
                                           "Command":BackMenu
                                          },
                                          {"Name":"Back",
                                           "Kind":MenuWidget.B_BackBlank
                                          }
                                        ]
                           }

PlayerConfigMenu=[
                  {"Name":MenuText.GetMenuText("Name:"),
                   "VSep":30,
                   "Kind":netwidgets.B_InputBox,
                   "MaxSize":10,
                   "GetInput":NetMisc.GetPlayerName,
                   "SetInput":NetMisc.SetPlayerName
                  },
                  {"Name":MenuText.GetMenuText("Character:"),
                   "Font":MenuFontMed,
                   "Kind":MenuWidget.B_MenuItemOption,
                   "Options":[MenuText.GetMenuText("Knight"),MenuText.GetMenuText("Barbarian"),MenuText.GetMenuText("Dwarf"),MenuText.GetMenuText("Amazon")],
                   "SelOptionFunc":NetMisc.GetCharType,
                   "Command":NetMisc.SetCharType
                  },
                  {"Name":"Lista de jugadores",
                   "Kind":netwidgets.B_ImageListWidget,
                   "ImageList":NetMisc.CharBitmaps,
                   "GetCharType":NetMisc.GetCharStatus,
                   "VSep":30
                  },
                  {"Name":"< "+MenuText.GetMenuText("Next Skin")+" >",
                   "VSep":30,
                   "Command":NetMisc.NextSkin,
                   "LeftCommand":NetMisc.NextSkin,
                   "RightCommand":NetMisc.PreviousSkin,
                  },
                  {"Name":MenuText.GetMenuText("Level")+":",
                   "Kind":MenuWidget.B_MenuSpin,
                   "SpinValues":(1,4,3),
                   "SpinGetValue":NetMisc.GetHandicap,
                   "SpinSetValueEnd":NetMisc.SetHandicap
                  },
                  {"Name":MenuText.GetMenuText("Save"),
                   "Command":NetMisc.SavePlayerConfiguration
                  },
                  {"Name":"Back",
                   "Kind":MenuWidget.B_BackBlank
                  }
                 ]

def MapLoading(option):
	global Character
	if Character == 0:
		Bladex.LoadLevel("Ruins_M4")
	if Character == 1:
		Bladex.LoadLevel("Barb_M1")
	if Character == 2:
		Bladex.LoadLevel("Ragnar_M2")
	if Character == 3:
		Bladex.LoadLevel("Dwarf_M3")

TutGameChoosing = {"Name":"TopMenu",
         "Size":(640,480),
         "Kind":MenuWidget.B_MenuItemTextNoFX,
         "ListDescr":[ {"Name":MenuText.GetMenuText("ENTER TUTORIAL"),
                        "VSep":100,
                        "Font":MenuFontBig,
                        "Command":LoadTutorial
                       },
                       {"Name":MenuText.GetMenuText("CONTINUE"),
                        "Font":MenuFontBig,
                        "Command":MapLoading
                       },
                       BackOption,
                       GamepadButton,
                       {"Name":"Back",
                        "Kind":MenuWidget.B_BackImageWidget
                       }
                     ]
        }

NormalMenu = 1

def GetPasswordMenu():
	if CORRECT_GORE_PASSWORD == "":
		return ParentalLockOffMenu
	else:
		return ParentalLockOnMenu

def SwitchParentalLock(Option):
	global CONFIRM_GORE_PASSWORD
	global NEW_GORE_PASSWORD
	global GORE_PASSWORD
	global CORRECT_GORE_PASSWORD

	print "Hola!"
	parl = GetMenuItem(["OPTIONS","GORE"])

	if parl["ListDescr"][0] == ParentalLockOffMenu:
		if (NEW_GORE_PASSWORD == CONFIRM_GORE_PASSWORD) and (CONFIRM_GORE_PASSWORD != ""):
			CORRECT_GORE_PASSWORD = NEW_GORE_PASSWORD
			GORE_PASSWORD         = CORRECT_GORE_PASSWORD
			SavePasswordFile()
			_MainMenu.DeActivateMenuItem()
			_MainMenu.DeActivateMenuItem()

			parl["ListDescr"][0] = ParentalLockOnMenu
			GORE_PASSWORD = ""

			Bladex.SetBloodLevel(0)
			Bladex.SetMutilationLevel(0)
			SaveConfiguration()

			_MainMenu.ActivateMenuItem()
	else:
		if (CORRECT_GORE_PASSWORD == GORE_PASSWORD):
			_MainMenu.DeActivateMenuItem()
			_MainMenu.DeActivateMenuItem()

			parl["ListDescr"][0] = ParentalLockOffMenu

			CORRECT_GORE_PASSWORD = ""
			GORE_PASSWORD         = ""
			SavePasswordFile()

			_MainMenu.ActivateMenuItem()

ParentalLockOnMenu = {"Name":MenuText.GetMenuText("Parental Lock ON"),
                      "Size":(640,480),
                      "VSep":100,
                      "Font":MenuFontBig,
                      "ListDescr":[
                                     { "Name"        : MenuText.GetMenuText("Password:"),
                                       "VSep"        : 185,
                                       "Kind"        : netwidgets.B_InputBox,
                                       "MaxSize"     : 8,
                                       "GetInput"    : Empty,
                                       "SetInput"    : SetPass,
                                       "PasswordChar": "#",
                                     },
                                     {"Name":MenuText.GetMenuText("ACCEPT"),
                                      "VSep":50,
                                      "Font":MenuFontBig,
                                      "Command":SwitchParentalLock
                                     },
                                     BackOption,
                                     GamepadButton,
                                     {"Name":"Back",
                                      "Kind":MenuWidget.B_BackImageWidget
                                     }
                                  ]
                     }

ParentalLockOffMenu = {"Name":MenuText.GetMenuText("Parental Lock OFF"),
                      "VSep":100,
                      "Size":(640,480),
                      "Font":MenuFontBig,
                      "ListDescr":[
                                     {"Name"        : MenuText.GetMenuText("New Password:"),
                                      "Kind"        : netwidgets.B_InputBox,
                                      "VSep"        : 185,
                                      "MaxSize"     : 8,
                                      "GetInput"    : Empty,
                                      "SetInput"    : SetNewPass,
                                      "PasswordChar": "#",
                                     },
                                     {"Name"        : MenuText.GetMenuText("Confirm New Password:"),
                                      "Kind"        : netwidgets.B_InputBox,
                                      "MaxSize"     : 8,
                                      "GetInput"    : Empty,
                                      "SetInput"    : SetConfNewPass,
                                      "PasswordChar": "#",
                                     },
                                     {"Name":MenuText.GetMenuText("ACCEPT"),
                                      "VSep":50,
                                      "Font":MenuFontBig,
                                      "Command":SwitchParentalLock
                                     },
                                     BackOption,
                                     GamepadButton,
                                     {"Name":"Back",
                                      "Kind":MenuWidget.B_BackImageWidget
                                     }
                                  ]
                     }

def SwitchCasaByGlobalMenu():
	global Desc1
	global TutGameChoosing

	DescAux = Desc1
	Desc1 = TutGameChoosing
	TutGameChoosing = DescAux
	DescAux = None

def SwitchToCasaMenu():
	global NormalMenu
	if NormalMenu:
		NormalMenu = 0
		SwitchCasaByGlobalMenu()
		# if Reference.DEMO_MODE:
			# GetMenuItem(['ENTER TUTORIAL'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus


def SwitchToGlobalMenu():
	global NormalMenu
	if not NormalMenu:
		NormalMenu = 1
		SwitchCasaByGlobalMenu()
Controler_Menu = {"Name":MenuText.GetMenuText("CONTROLS"),
                          "VSep":8,
                          "Font":MenuFontBig,
                          "Size":(640,480),
                          "ListDescr":[{"Name":MenuText.GetMenuText("LAYOUT"),
                                        "VSep":100,
                                        "Size":(780,480),
                                        "Font":MenuFontBig,
                                        "ListDescr":[{"Name":"Keyboard settings",
                                                      "Kind":KeybWidget.B_KeybListWidget,
                                                      "VSep":100,
                                                      "Size":(750,380),
                                                      "ListDescr":KeybActions
                                                     },
                                                      BackOption,
                                                      GamepadButton,
                                                      {"Name":"Back",
                                                       "Kind":MenuWidget.B_BackImageWidget
                                                      }
#                                                     {"Name":MenuText.GetMenuText("CONFIGURE ACTIONS"),
#                                                      "VSep":180,
#                                                      "Size":(640,480),
#                                                      "Font":MenuFontBig,
#                                                      "ListDescr":[{"Name":"KeybList",
#                                                                        "Kind":KeybWidget.B_KeybListWidget,
#                                                                        "VSep":120,
#                                                                        "Size":(610,200),
#                                                                        "ListDescr":KeybActions
#                                                                       },
#                                                                       BackOption,
#                                                                       {"Name":"Back",
#                                                                        "Kind":MenuWidget.B_BackImageWidget
#                                                                       }
#                                                                     ]
#                                                         },
#                                                         BackOption,
#                                                         {"Name":"Back",
#                                                          "Kind":MenuWidget.B_BackImageWidget
#                                                         }
                                                         ]
                                           },
                                           {"Name":MenuText.GetMenuText("CAMERA"),
                                            "Font":MenuFontBig,
                                            "Size":(640,480),
                                            "ListDescr":[{"Name":MenuText.GetMenuText("Invert") + " X",
                                                          "VSep":100,
                                                          "Font":MenuFontMed,
                                                          "Kind":MenuWidget.B_MenuItemOption,
                                                          "Options":[MenuText.GetMenuText("Yes"),MenuText.GetMenuText("No")],
                                                          "SelOptionFunc":GetMouseInvertX,
                                                          "Command": SetMouseInvertX
                                                          },
                                                          {"Name":MenuText.GetMenuText("Invert") + " Y",
                                                          "Font":MenuFontMed,
                                                          "Kind":MenuWidget.B_MenuItemOption,
                                                          "Options":[MenuText.GetMenuText("Yes"),MenuText.GetMenuText("No")],
                                                          "SelOptionFunc":GetMouseInvertY,
                                                          "Command": SetMouseInvertY
                                                          },
                                                         {"Name":MenuText.GetMenuText("X Speed"),
                                                          "Font":MenuFontMed,
                                                          "Kind":MenuWidget.B_MenuSpin,
                                                          "SpinValues":(int(0),int(10),int(10)),
                                                          "SpinGetValue":GetMouseXSens,
                                                          "SpinSetValueEnd":SetMouseXSens
                                                          },
                                                         {"Name":MenuText.GetMenuText("Y Speed"),
                                                          "Font":MenuFontMed,
                                                          "Kind":MenuWidget.B_MenuSpin,
                                                          "SpinValues":(int(0),int(10),int(10)),
                                                          "SpinGetValue":GetMouseYSens,
                                                          "SpinSetValueEnd":SetMouseYSens
                                                          },
                                                          BackOption,
                                                          GamepadButton,
                                                         {"Name":"Back",
                                                          "Kind":MenuWidget.B_BackImageWidget
                                                         }
                                                         ]
                                           },
                                           {"Name":MenuText.GetMenuText("GAMEPAD"),
                                            "Font":MenuFontBig,
                                            "Size":(640,480),
                                            "ListDescr":[{"Name":"Gamepad settings",
                                                          "Kind":GamepadWidget.B_GamepadWidget
                                                          },
                                                          {"Name":MenuText.GetMenuText("Vibration:"),
                                                           "VSep":370,
                                                           "Font":MenuFontMed,
                                                           "Kind":MenuWidget.B_MenuItemOption,
                                                           "Options":[MenuText.GetMenuText("Yes"),MenuText.GetMenuText("No")],
                                                           "SelOptionFunc":Vibration,
                                                           "Command":SetVibration
                                                           },
                                                          BackGamepadOption,
                                                          GamepadButton,
                                                         {"Name":"Back",
                                                          "Kind":MenuWidget.B_BackImageWidget
                                                         }
                                                         ]
                                           },
                                           {"Name":MenuText.GetMenuText("RESET TO DEFAULTS"),
                                            "Font":MenuFontBig,
                                            "Command": ResetKeyB
                                           },
                                           BackOption,
                                           GamepadButton,
                                           {"Name":"Back",
                                            "Kind":MenuWidget.B_BackImageWidget
                                           }
                                         ]
                             }

Options_Menu = {"Name":MenuText.GetMenuText("OPTIONS"),
                        "VSep":8,
                        "Font":MenuFontBig,
                        "Size":(640,480),
                        "ListDescr":[
                                      {
                                        "Name":MenuText.GetMenuText("DISPLAY"),
                                        "VSep":100,
                                        "Font":MenuFontBig,
                                        "Size":(640, 480),
                                        "ListDescr":[
                                               #  {
                                                  #   "Name":MenuText.GetMenuText("Aspect ratio:"),
                                                  #   "VSep":15,
                                                  #   "Font":MenuFontMed,
                                                  #   "Kind":MenuWidget.B_MenuItemOption,
                                                  #   "Options":[MenuText.GetMenuText("4:3"), MenuText.GetMenuText("16:9"), MenuText.GetMenuText("16:10")],
                                                  #   # "Options":[MenuText.GetMenuText("1 (Default)"), MenuText.GetMenuText("2")],
                                                  #   "SelOptionFunc":GetAspectRatio,
                                                  #   "Command":SetAspectRatioValue,
                                                  #   "PostInitCommand":FocusableWhenWindowed,
                                                  #  },
                                                   {"Name":MenuText.GetMenuText("Anti-Aliasing:"),
                                                    "VSep": 100,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                                    "SelOptionFunc":GetAntialiasing,
                                                    "Command":SetAntialiasing,
                                                   },
                                                   {"Name":MenuText.GetMenuText("Vertical Sync:"),
                                                    "VSep":15,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                                    "SelOptionFunc":GetVerticalSync,
                                                    "Command":SetVerticalSyncValue,
                                                   },
                                                   {"Name":MenuText.GetMenuText("Framerate Limit:"),
                                                    "VSep":15,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                                    "SelOptionFunc":GetLimitFps,
                                                    "Command":SetLimitFps,
                                                   },
                                                    BackOption,
                                                    GamepadButton,
                                                   {"Name":"Back",
                                                    "Kind":MenuWidget.B_BackImageWidget
                                                   }
                                                  ]
                                      },
                                     {"Name":MenuText.GetMenuText("VIDEO"),
                                      "VSep":-5,
                                      "Size":(640,480),
                                      "Font":MenuFontBig,
                                      "ListDescr":[
                                                   {"Name":MenuText.GetMenuText("Gamma:"),
                                                    "VSep":100,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuSpin,
                                                    "SpinValues":(0.0,1.0,20),
                                                    "SpinGetValue":GetGammaValue,
                                                    "SpinOnChange":SetGammaValue,
                                                    "SpinSetValue":SetGammaValue,
                                                    "Size": (430,19)
                                                   },
                                                   {"Name":MenuText.GetMenuText("Contrast:"),
                                                    "VSep":15,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuSpin,
                                                    "SpinValues":(0.0,1.0,20),
                                                    "SpinGetValue":GetContrastValue,
                                                    "SpinOnChange":SetContrastValue,
                                                    "SpinSetValue":SetContrastValue,
                                                    "Size": (430,19),
                                                   },
                                                   {"Name":MenuText.GetMenuText("Brightness:"),
                                                    "VSep":15,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuSpin,
                                                    "SpinValues":(0.0,1.0,20),
                                                    "SpinGetValue":GetBrightnessValue,
                                                    "SpinOnChange":SetBrightnessValue,
                                                    "SpinSetValue":SetBrightnessValue,
                                                    "Size": (430,19)
                                                   },
                                                   {"Name":MenuText.GetMenuText("RESET COLOUR CONTROL"),
                                                    "VSep":15,
                                                    "Font":MenuFontMed,
                                                    "Command": ResetVideo
                                                   },
                                                   {"Name":MenuText.GetMenuText("Character Shadows:"),
                                                    "VSep":15,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("Yes"),MenuText.GetMenuText("No")],
                                                    "SelOptionFunc":ShadowsSettings,
                                                    "Command":SetShadows,
                                                   },
                                                   {"Name":MenuText.GetMenuText("Field Of View:"),
                                                    "VSep": 15,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuSpin,
                                                    "SpinValues":GetValidFieldsOfView(),
                                                    "SpinGetValue":GetCurrentFieldOfView,
                                                    "SpinSetValueEnd":SetCurrentFieldOfView,
                                                    "DefaultValue": 114,
                                                    "Size": (430,19)
                                                   },
                                                   {"Name":MenuText.GetMenuText("Reworked Camera:"),
                                                    "VSep":15,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("Yes"),MenuText.GetMenuText("No")],
                                                    "SelOptionFunc":ReworkedCamera,
                                                    "Command":SetReworkedCamera,
                                                   },
                                                   BackOption,
                                                   GamepadButton,
                                                   {"Name":"Back",
                                                    "Kind":MenuWidget.B_BackImageWidget
                                                   }
                                                  ]
                                      },
                                      {"Name":MenuText.GetMenuText("USER INTERFACE"),
                                      "VSep":-5,
                                      "Size":(640,480),
                                      "Font":MenuFontBig,
                                      "ListDescr":[
                                                   {"Name":MenuText.GetMenuText("Subtitles:"),
                                                    "VSep":100,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                                    "SelOptionFunc":GetSubtitlesEnable,
                                                    "Command":SetSubtitlesEnable
                                                   },
                                                   {"Name":MenuText.GetMenuText("UI Scale:"),
                                                    "VSep":10,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("Small"),MenuText.GetMenuText("Normal"),MenuText.GetMenuText("Big")],
                                                    "SelOptionFunc":GetUIScale,
                                                    "Command":SetUIScale
                                                   },
                                                   {"Name":MenuText.GetMenuText("Hide UI:"),
                                                    "VSep":10,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                                    "SelOptionFunc":GetHideUI,
                                                    "Command":SetHideUI
                                                   },
                                                   BackOption,
                                                   GamepadButton,
                                                   {"Name":"Back",
                                                    "Kind":MenuWidget.B_BackImageWidget
                                                   }
                                                  ]
                                     },
                                      {"Name":MenuText.GetMenuText("SOUND"),
                                       "VSep":-5,
                                       "Font":MenuFontBig,
                                       "Size":(640,480),
                                       "ListDescr":[
                                                   {"Name":MenuText.GetMenuText("FX Volume:"),
                                                    "VSep":100,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuSpin,
                                                    "SpinValues":(int(0),int(10),int(10)),
                                                    "SpinGetValue":GetSoundValue,
                                                    "SpinSetValueEnd":SetSoundValue,
                                                    "SpinOnChange":setFXVolume
                                                   },
                                                   {"Name":MenuText.GetMenuText("Music Volume:"),
                                                    "VSep": 10,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuSpin,
                                                    "SpinValues":(int(0),int(10),int(10)),
                                                    "SpinGetValue":GetMusicValue,
                                                    "SpinSetValueEnd":SetMusicValue,
                                                    "SpinOnChange":setMusicVolume
                                                   },
                                                   {"Name":MenuText.GetMenuText("Sound Quality:"),
                                                    "VSep":10,
                                                    "Font":MenuFontMed,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("Low"),MenuText.GetMenuText("Med"),MenuText.GetMenuText("High")],
                                                    "SelOptionFunc":GetSoundQuality,
                                                    "Command":SetSoundQuality
                                                   },
#                                                   {"Name":MenuText.GetMenuText("EAX:"),
#                                                    "VSep":10,
#                                                    "Font":MenuFontMed,
#                                                    "Options":[MenuText.GetMenuText("Disabled"),MenuText.GetMenuText("Enabled")],
#                                                    "Kind":MenuWidget.B_MenuItemOption,
#                                                    "SelOptionFunc":GetEAX,
#                                                    "Command":SetEAX
#                                                   },
#                                                   {"Name":MenuText.GetMenuText("EAX (FOR IMPROVED ENVIRONMENTAL REALISM)"),
#                                                    "VSep":5,
#                                                    "Font": MenuFontSmall,
#                                                    "Kind": MenuWidget.B_MenuItemTextNoFXNoFocus
#                                                   },
                                                   {"Name":MenuText.GetMenuText("Speaker Configuration:"),
                                                    "VSep":10,
                                                    "Font":MenuFontMed,
                                                    "Options":[MenuText.GetMenuText("Mono"),MenuText.GetMenuText("2 Speakers"),MenuText.GetMenuText("4 Speakers"),MenuText.GetMenuText("5.1"),MenuText.GetMenuText("7.1")],
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "SelOptionFunc":GetSpeakerConfig,
                                                    "Command":SetSpeakerConfig
                                                   },
                                                   BackOption,
                                                   GamepadButton,
                                                   {"Name":"Back",
                                                    "Kind":MenuWidget.B_BackImageWidget
                                                   }
                                                  ]
                                     },
                                     {"Name":MenuText.GetMenuText("GORE"),
                                      "VSep":-5,
                                      "Size":(640,480),
                                      "Font":MenuFontBig,
                                      "ListDescr":[
                                                  GetPasswordMenu(),
                                                   {"VSep":0,
                                                    "Name":MenuText.GetMenuText("Blood:"),
                                                    "Font":MenuFontBig,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("Yes"),MenuText.GetMenuText("No")],
                                                    "Command":SetBlood,
                                                    "SelOptionFunc":BloodSettings,
                                                    "CheckPass" : CheckGorePassWord
                                                    },
                                                    {"Name":MenuText.GetMenuText("Mutilations:"),
                                                     "Font":MenuFontBig,
                                                     "Kind":MenuWidget.B_MenuItemOption,
                                                     "Options":[MenuText.GetMenuText("Yes"),MenuText.GetMenuText("No")],
                                                     "Command":SetMutilation,
                                                     "SelOptionFunc":MutilationSettings,
                                                     "CheckPass" : CheckGorePassWord
                                                    },
                                                    BackOption,
                                                    GamepadButton,
                                                    {"Name":"Back",
                                                     "Kind":MenuWidget.B_BackImageWidget
                                                    }
                                                  ]
                                     },
                                     {"Name":MenuText.GetMenuText("AUTO LOCK ON:"),
                                                    "VSep":30,
                                                    "Font":MenuFontBig,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                                    "Command": SetFacing,
                                                    "SelOptionFunc":GetFacing
                                     },
                                     {"Name":MenuText.GetMenuText("PLAY INTRO:"),
                                                    "VSep":10,
                                                    "Font":MenuFontBig,
                                                    "Kind":MenuWidget.B_MenuItemOption,
                                                    "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                                    "Command": SetPlayIntro,
                                                    "SelOptionFunc":GetPlayIntro

                                     },
                                     # {"Name":MenuText.GetMenuText("PLAY INTRO:"),
                                     #  "VSep":-5,
                                     #  "Font":MenuFontBig,
                                     #  "Kind":MenuWidget.B_MenuItemOption,
                                     #  "Options":[MenuText.GetMenuText("No"),MenuText.GetMenuText("Yes")],
                                      # "Command": SetPlayIntro,
                                      # "SelOptionFunc":GetPlayIntro
                                     # },
                                     #{"Name":MenuText.GetMenuText("GAME OPTIONS"),
                                      #"Size":(640,480),
                                      #"Font":MenuFontBig,
                                      #"ListDescr":[#{"Name":MenuText.GetMenuText("De-Facing Time"),
                                                   # "Kind":MenuWidget.B_MenuSpin,
                                                   # "SpinValues":(int(1),int(30),int(29)),
                                                   # "SpinGetValue":GetDeFacingValue,
                                                   # "SpinSetValueEnd":SetDeFacingValue
                                                   #},
                                         #          {"Name":MenuText.GetMenuText("Blood Evaporation:"),
                                       #             "VSep":15,
                                        #            "Font":MenuFontMed,
                                        #            "Kind":MenuWidget.B_MenuItemOption,
                                        #            "Options":[MenuText.GetMenuText("Active"),MenuText.GetMenuText("Inactive")],
                                        #            "SelOptionFunc":BloodEvaporationSettings,
                                        #            "Command":SetBloodEvaporation
                                        #           },
                                                   #{"Name":MenuText.GetMenuText("On-Screen Info:"),
                                                   #"Font":MenuFontMed,
                                                   #"VSep":15,
                                                   #"Kind":MenuWidget.B_MenuItemOption,
                                                   #"Options":[MenuText.GetMenuText("Full"),MenuText.GetMenuText("Auto")],
                                                   #"SelOptionFunc":CurrentScorer,
                                                   #"Command":SetScorer
                                                   #},
                                                   #{"Name":MenuText.GetMenuText("Detail Level:"),
                                                   #"Font":MenuFontBig,
                                                   #"Kind":MenuWidget.B_MenuItemOption,
                                                   #"Options":[MenuText.GetMenuText("High"),MenuText.GetMenuText("Med"),MenuText.GetMenuText("Low")],
                                                   #"Command":OptionCommandPrb
                                                   #},

                                      #             BackOption,
                                      #             {"Name":"Back",
                                      #              "Kind":MenuWidget.B_BackImageWidget
                                      #             }
                                                   #{"Name":MenuText.GetMenuText("Gamma Correction"),
                                                   # "Font":MenuFontMed,
                                                   # "Kind":MenuWidget.B_MenuSpin,
                                                   # "SpinValues":(-30,70,10),
                                                   # "SpinGetValue":GetGammaValue,
                                                   # "SpinSetValueEnd":SetGammaValue,
                                                   # "Size":(240,19)
                                                   #}
                                      #            ]
                                     #},
                                     BackOption,
                                     GamepadButton,
                                     {"Name":"Back",
                                      "Kind":MenuWidget.B_BackImageWidget
                                     }
                                    ]

                       }

if(Bladex.IsRunningOnHandheldDevice() == 0):
    Options_Menu["ListDescr"][0]["ListDescr"][0]["VSep"] = 15
    Options_Menu["ListDescr"][0]["ListDescr"].insert(0,{"Name":MenuText.GetMenuText("Resolution:"),
                                                        "VSep":15,
                                                        "Font":MenuFontMed,
                                                        "Kind":MenuWidget.B_MenuItemOption,
                                                        "Options":GetSupportedResolution(),
                                                        "SelOptionFunc":GetResolutionValue,
                                                        "Command":SetResolutionValue,
                                                       })

    Options_Menu["ListDescr"][0]["ListDescr"].insert(0,{
                                                        "Name":MenuText.GetMenuText("Monitor:"),
                                                        "VSep":15,
                                                        "Font":MenuFontMed,
                                                        "Kind":MenuWidget.B_MenuItemOption,
                                                        "Options":GetNumMonitor(),
                                                        "SelOptionFunc":GetActiveMonitor,
                                                        "Command":SetActiveMonitorValue,
                                                        "PostInitCommand":FocusableWhenFullScreen,
                                                       })

    Options_Menu["ListDescr"][0]["ListDescr"].insert(0,{"Name":MenuText.GetMenuText("Window Mode:"),
                                                        "VSep":100,
                                                        "Font":MenuFontMed,
                                                        "Kind":MenuWidget.B_MenuItemOption,
                                                        "Options":[MenuText.GetMenuText("Windowed"),MenuText.GetMenuText("Fullscreen"), MenuText.GetMenuText("Borderless")],
                                                        "SelOptionFunc":GetScreenMode,
                                                        "Command2":SetScreenModeValue,
                                                       })

if netgame.GetNetState() != 0:
  PlayerConfigMenu.insert(6,{"Name":MenuText.GetMenuText("This modification will take effect in the next arena"),
                             "VSep":20,
                             "Font":MenuFontSmall,
                             "Kind":MenuWidget.B_MenuItemTextNoFXNoFocus
                             })

  Desc1={"Name":"TopMenu",
         "Kind":MenuWidget.B_MenuItemTextNoFX,
         "ListDescr":[ {"Name":MenuText.GetMenuText("DISCONNECT"),
                        "VSep":130,
                        "Font":MenuFontBig,
                        "Command":NetMisc.Disconnect
                       },
                       Controler_Menu,
                       Options_Menu,
                       {"Name":MenuText.GetMenuText("MODIFY PLAYER"),
                        "Font":MenuFontBig,
                        "VSep":10,
                        "ListDescr":PlayerConfigMenu
                       }
                       ,QuitMenu,
                       GamepadButton,
                       {"Name":"Back",
                        "Kind":MenuWidget.B_BackImageWidget
                       }
                     ]
        }
else:
  Desc1={"Name":"TopMenu",
         "Size":(640,480),
         "Kind":MenuWidget.B_MenuItemTextNoFX,
         "ListDescr":[ {"Name":MenuText.GetMenuText("GAME"),
                        "Font":MenuFontBig,
                        "VSep":100,
                        "Size":(640,480),
                        "ListDescr":[{
                                       "Name":MenuText.GetMenuText("START NEW GAME"),
                                       "Size":(640,480),
                                       "Font":MenuFontBig,
                                       "VSep":100,
                                       "Command":LoadPlayerSelect
                                      },
                                      {"Name":MenuText.GetMenuText("SAVE GAME"),
                                       "Font":MenuFontBig,
                                       "Size":(640,480),
                                       #"Kind":MenuWidget.B_VariableFocusTextMenuItem,
                                       #"Command":SaveGame1
                                       "ListDescr":[ {"Name"     : MenuText.GetMenuText("Savegame Slot 1:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 200,
                                                      "Command":SaveGame1
                                                     },
                                                     {"Name"     : MenuText.GetMenuText("Savegame Slot 2:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 20,
                                                      "Command":SaveGame2
                                                     },
                                                     {"Name"     : MenuText.GetMenuText("Savegame Slot 3:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 20,
                                                      "Command":SaveGame3
                                                     },
                                                     {"Name"     : MenuText.GetMenuText("Savegame Slot 4:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 20,
                                                      "Command":SaveGame4
                                                     },
                                                     {"Name":"Back",
                                                      "Kind":MenuWidget.B_BackImageWidget
                                                     }
                                                   ]
                                      },
                                      {"Name":MenuText.GetMenuText("LOAD GAME"),
                                       "Font":MenuFontBig,
                                       "Size":(640,480),
                                       "ListDescr":[ {"Name"     : MenuText.GetMenuText("Load Game at Slot 1:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 200,
                                                      "Command":LoadGame
                                                     },
                                                     {"Name"     : MenuText.GetMenuText("Load Game at Slot 2:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 20,
                                                      "Command":LoadGame2
                                                     },
                                                     {"Name"     : MenuText.GetMenuText("Load Game at Slot 3:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 20,
                                                      "Command":LoadGame3
                                                     },
                                                     {"Name"     : MenuText.GetMenuText("Load Game at Slot 4:"),
                                                      "Font":MenuFontBig,
                                                      "VSep"     : 20,
                                                      "Command":LoadGame4
                                                     },
                                                     {"Name":"Back",
                                                      "Kind":MenuWidget.B_BackImageWidget
                                                     }
                                                   ]

                                      },
                                      # {"Name":MenuText.GetMenuText("ARENA"),
                                      #  "Font":MenuFontBig,
                                      #  "Size":(640,480),
                                      #  "VSep":20,
                                      #  "ListDescr":[ {"Name":MenuText.GetMenuText("Connection:"),
                                      #                 "Font":MenuFontMed,
                                      #                 "VSep":150,
                                      #                 "Kind":MenuWidget.B_MenuItemOption,
                                      #                 "Options":[MenuText.GetMenuText("IPX"),MenuText.GetMenuText("TCP/IP")],
                                      #                 "SelOptionFunc":NetMisc.GetProtocol,
                                      #                 "Command":NetMisc.SetProtocol
                                      #                },
                                      #                {"Name":MenuText.GetMenuText("NEW ARENA"),
                                      #                 "Size":(640,480),
                                      #                 "Font":MenuFontBig,
                                      #                 "ListDescr":[
                                      #                              {"Name"     : MenuText.GetMenuText("Name:"),
                                      #                               "VSep"     : 20,
                                      #                               "Kind"     : netwidgets.B_InputBox,
                                      #                               "MaxSize"  : 16,
                                      #                               "GetInput" : NetMisc.GetArenaName,
                                      #                               "SetInput" : NetMisc.SetArenaName,
                                      #                              },
                                      #                              {"Name"       : "Lista de mapas",
                                      #                               "Kind"       : netwidgets.B_MapListWidget,
                                      #                               "LeftMap"    : "../../Data/net/MapL.bmp",
                                      #                               "RightMap"   : "../../Data/net/MapR.bmp",
                                      #                               "SelMap"     : "../../Data/net/MapM.bmp",
                                      #                               "MarkMap"    : "../../Data/net/MapS.bmp",
                                      #                               "MapGetValue": NetMisc.GetArenaMaps,
                                      #                               "MapSetValue": NetMisc.SetArenaMaps,
                                      #                               "VSep"       : 15
                                      #                              },
                                      #                              {"Name":MenuText.GetMenuText("The bad place"),
                                      #                               "VSep":1,
                                      #                               "Kind":netwidgets.B_DescriptorLabel
                                      #                               },
                                      #                              {"Name":MenuText.GetMenuText("Max players:"),
                                      #                               "Kind":MenuWidget.B_MenuSpin,
                                      #                               "SpinValues":(2,10,8),
                                      #                               "SpinGetValue":NetMisc.GetMaxPlayers,
                                      #                               "SpinSetValueEnd":NetMisc.SetMaxPlayers,
                                      #                               "VSep"       : 30
                                      #                              },
                                      #                              {"Name":MenuText.GetMenuText("Max level:"),
                                      #                               "Kind":MenuWidget.B_MenuSpin,
                                      #                               "SpinValues":(1,4,3),
                                      #                               "SpinGetValue":NetMisc.GetArenaHandicap,
                                      #                               "SpinSetValueEnd":NetMisc.SetArenaHandicap
                                      #                              },
                                      #                              {"Name":MenuText.GetMenuText("Packets per second:"),
                                      #                               "Font":MenuFontMed,
                                      #                               "Kind":MenuWidget.B_MenuItemOption,
                                      #                               "Options":[
                                      #                                          MenuText.GetMenuText("Variable"),
                                      #                                          "10",
                                      #                                          "20",
                                      #                                          "30",
                                      #                                          "40",
                                      #                                          "50",
                                      #                                          "60"
                                      #                                         ],
                                      #                               "SelOptionFunc":NetMisc.GetPPS,
                                      #                               "Command":NetMisc.SetPPS
                                      #                              },
                                      #                              {"Name":MenuText.GetMenuText("Death limit:"),
                                      #                               "Kind":MenuWidget.B_MenuSpin,
                                      #                               "SpinValues":(1,50,49),
                                      #                               "SpinGetValue":NetMisc.GetFragLimit,
                                      #                               "SpinSetValueEnd":NetMisc.SetFragLimit
                                      #                              },
                                      #                              {"Name":MenuText.GetMenuText("START"),
                                      #                               "Command":NetMisc.StartServer
                                      #                              },
                                      #                              {"Name"    : MenuText.GetMenuText("BACK"),
                                      #                               "VSep"    : 10,
                                      #                               "Command" : BackMenu,
                                      #                              },
                                      #                              {"Name":"Back",
                                      #                               "Kind":MenuWidget.B_BackBlank
                                      #                              }
                                      #                             ]
                                      #                },
                                      #                {"Name":MenuText.GetMenuText("JOIN GAME"),
                                      #                 "Size":(640,480),
                                      #                 "Font":MenuFontBig,
                                      #                 "ListDescr":[
                                      #                              {"Name"     : MenuText.GetMenuText("Address:"),
                                      #                               "Kind"     : netwidgets.B_InputBox,
                                      #                               "MaxSize"  : 32,
                                      #                               "GetInput" : NetMisc.GetIp,
                                      #                               "SetInput" : NetMisc.SetIp,
                                      #                               "Locked"   : NetMisc.IpLooked,
                                      #                               "VSep"     : 120
                                      #                              },
                                      #                              {
                                      #                               "Name"     : MenuText.GetMenuText("Search"),
                                      #                               "Command"  : NetMisc.BrowseServers
                                      #                              },
                                      #                              {"Name"     : MenuText.GetMenuText("Server's list"),
                                      #                               "Kind"     : netwidgets.B_ServerListWidget,
                                      #                               "Size"     : (610,200),
                                      #                               "ListDescr": []
                                      #                              },
                                      #                              {"Name"    : MenuText.GetMenuText("BACK"),
                                      #                               "VSep"    : 10,
                                      #                               "Command" : BackMenu,
                                      #                              },
                                      #                              {"Name":"Back",
                                      #                               "Kind":MenuWidget.B_BackBlank
                                      #                              }
                                      #                             ]
                                      #                },
                                      #                {"Name":MenuText.GetMenuText("PLAYER CONFIGURATION"),
                                      #                 "Font":MenuFontBig,
                                      #                 "ListDescr":PlayerConfigMenu
                                      #                },
                                      #                BackOption,
                                      #                {"Name":"Back",
                                      #                 "Kind":MenuWidget.B_BackImageWidget
                                      #                }
                                      #              ]
                                      # },
                                      BackOption,
                                      GamepadButton,
                                      {"Name":"Back",
                                       "Kind":MenuWidget.B_BackImageWidget
                                      }
                                   ]
                       },
                       Controler_Menu,
                       Options_Menu,
                       {"Name":MenuText.GetMenuText("CREDITS"),
                        "VSep":8,
                        "Size":(640,480),
                        "Font":MenuFontBig,
                        "ListDescr":[ {"Name":"Credits",
                                       "Kind":Credits.B_CreditsImageWidget}
                                    ]

                       },
                       QuitMenu,
                       GamepadButton,
                       {"Name":"Back",
                        "Size":(640,480),
                        "Kind":MenuWidget.B_BackImageWidget
                       }
                     ]
        }
  ########## RODRIGO!! AQUI ESTA COMO SE HACE
  if ("Casa" != Bladex.GetCurrentMap()) and ("Final" != Bladex.GetCurrentMap()):       # Added Final -LeaHead
    Desc1["ListDescr"].insert(1,
                                           {"Name":MenuText.GetMenuText("BACK TO GAME"),
                                            "VSep":8,
                                            "Font":MenuFontBig,
                                            "Command":BackMenu,
                                           })
    ########## ENJOY!


def BackMap():
	Desc1["ListDescr"].insert(len(Desc1["ListDescr"])-1,
	                                     {"Name":MenuText.GetMenuText("Leave Rune Quest"),
	                                      "Font":MenuFontBig,
	                                      "Command":GoTo2d,
	                                      "VSep":20,
	                                     })

# Xample by Dario and co
#    Menu.GetMenuItem(['Game','Save Current'])["Kind"] = MenuWidget.B_MenuItemTextNoFocus
#    Menu.GetMenuItem(['Options','Game Options','Gore','Password:'])
def GetMenuItem(way):
	global Desc1

	idx          = 0
	continueflag = 1
	MenuLevel    = Desc1
	ReturnValue  = 1

	while(continueflag):
		continueflag = 0
		for val in MenuLevel["ListDescr"]:
			if val.has_key("Name"):
				#print "see",val["Name"]

				if MenuText.GetMenuText(way[idx]) == val["Name"]:
					idx = idx + 1
					if len(way)==idx:
						ReturnValue = val

					else:
						if val.has_key("ListDescr"):
							continueflag = 1
							MenuLevel = val
							#print "Searching at",val["Name"]

						else:
							print val["Name"],"is not a list"
					break
	MenuLevel = None
	return ReturnValue



def InitMenuKeys():
    Raster.SetTextMode(3)
    InputManager=BInput.GetInputManager()
    InputManager.AddInputActionsSet("MenuRedefine") #Conjunto para cuando se est�n definiendo los controles
    InputManager.AddInputActionsSet("Menu")

    oldInputActionsSet=InputManager.GetInputActionsSet()

    InputManager.SetInputActionsSet("Menu")
    #Bladex.AddInputAction("Deactivate Menu",0)
    #Bladex.AssocKey("Deactivate Menu","Keyboard","Esc")
    #Bladex.AddBoundFunc("Deactivate Menu",ActivateMenu)

    InputManager.SetInputActionsSet("Default")
    Bladex.AddInputAction("Activate Menu",0)
    Bladex.AddInputAction("InGameToggleHiRes",0)

    Bladex.AssocKey("Activate Menu","Keyboard","Esc")
    Bladex.AssocKey("Activate Menu","Gamepad","ButtonStart")
    Bladex.AddBoundFunc("Activate Menu",PreActivateMenu)

    InputManager.SetInputActionsSet(oldInputActionsSet)
    print "Activadas!"

    if Reference.DEMO_MODE==1:
        #print "Demo mode was 1!"

        #GetMenuItem(['Travel Book'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus

        GetMenuItem(['CREDITS'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
        del GetMenuItem(['CREDITS'])["ListDescr"] #xq tienen submenus

        GetMenuItem(['GAME','SAVE GAME'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
        del GetMenuItem(['GAME','SAVE GAME'])["ListDescr"] #xq tienen submenus

        GetMenuItem(['GAME','LOAD GAME'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
        del GetMenuItem(['GAME','LOAD GAME'])["ListDescr"] #xq tienen submenus

        # GetMenuItem(['GAME','ARENA'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
        # del GetMenuItem(['GAME','ARENA'])["ListDescr"] #xq tienen submenus

        #GetMenuItem(['OPTIONS','CONTROLS','(Gamepad)'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
        #del GetMenuItem(['Options','Controls','(Gamepad)'])["ListDescr"] #xq tienen submenus
    else:
	if netgame.GetNetState()==0:
	        ProtocolList = [netgame.IsValidProtocol(0),netgame.IsValidProtocol(1)]
	        if ProtocolList == [0,0]:
	                GetMenuItem(['GAME','ARENA'])["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
	        elif ProtocolList == [1,0]:
	                GetMenuItem(['GAME','ARENA'])["ListDescr"][0]={ "Name":MenuText.GetMenuText("Connection:")+"  "+MenuText.GetMenuText("IPX (Local network)"),
	                                                                "Font":MenuFontMed,
	                                                                "VSep":150,
	                                                                "Kind":MenuWidget.B_MenuItemTextNoFXNoFocus,
	                                                             }
	                NetMisc.TCP = 0
	        elif ProtocolList == [0,1]:
	                GetMenuItem(['GAME','ARENA'])["ListDescr"][0]={ "Name":MenuText.GetMenuText("Connection:")+"  "+MenuText.GetMenuText("TCP/IP"),
	                                                                "Font":MenuFontMed,
	                                                                "VSep":150,
	                                                                "Kind":MenuWidget.B_MenuItemTextNoFXNoFocus,
	                                                             }
	                NetMisc.TCP = 1



#InitMenuKeys()


try:
  execfile("../../Config/GameCfg.py")
  print "Menu.py -> Executed GameCfg.py"
except:
  print "Menu.py -> No GameCfg.py found"



"""
class Listener(BInput.B_InputListener):
  def __init__(self,name):
    BInput.B_InputListener.__init__(self,name)
    #self.SetPythonFunc(self.Prb)

  def Prb(self,x,y,z):
    print "Listener::Prb()",x,y,z


_Listener=Listener("Python Listener 1")
InputManager=BInput.GetInputManager()
keyb=InputManager.GetAttachedDevice("Keyboard")
keyb.AddListener(_Listener)
"""
