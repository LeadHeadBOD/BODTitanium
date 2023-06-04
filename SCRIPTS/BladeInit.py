##///
##||| BLADEINIT.PY TITANIUM
##||| Change list:
##||| * Execution of AnmCameras has been moved to the very bottom to ensure 
##\\\ 


#####################################################
#
#
#
#	         B L A D E I N I T . P Y
#
#
#
#
#####################################################


import Bladex
Bladex.SetTime(0)
import string
import Reference
import Language

from bladeinit0 import *
#
# Different kind of enemies. Should be called b4 creating ANY PersonEntity!
#
Bladex.OpenProfileSection(3,"BladeInit.Enemies")
import Enemies
Enemies.Init()
Bladex.CloseProfileSection(3)



#
# New animation system (biped)
#
Bladex.OpenProfileSection(4,"BladeInit.Biped")
import Biped
Biped.Init()
Bladex.CloseProfileSection(4)

#
# The sharing of whole sets of animations
#
Bladex.OpenProfileSection(5,"BladeInit.anm_conv")
import anm_conv
anm_conv.Init()
Bladex.CloseProfileSection(5)


#
# To modify flags of animations
#
import Anm_Mdf
Anm_Mdf.Init()






#
# Particle Systems init
#
# CUIDADO! Valores definidos tambien en InitParticleSystems.py.
B_PARTICLE_GTYPE_COPY=0
B_PARTICLE_GTYPE_BLEND=1
B_PARTICLE_GTYPE_ADD=2
B_PARTICLE_GTYPE_MUL=3

#
# Procedural textures
#
execfile("../../Scripts/AutoGenTextures.py")






#
# PJ Init
#
import GotoMapVars
if string.lower(Bladex.GetCurrentMap()) in ['tutorial','2dmap','casa','barb_m1','ragnar_m2','dwarf_m3','ruins_m4']: # Caso especial
  execfile("pj.py")
  print "Found 2DMap"
elif not GotoMapVars.BeginLevel():
  execfile("pj.py")
#
# Scorer Data init
#
import Scorer
Scorer.ActivateScorer()

import CharStats


import GameText
GameText.SetLanguage(Language.Current)

import DefaultScorerData
DefaultScorerData.Init()

# Inicio del personaje y sus marcadores
char=Bladex.GetEntity("Player1")  #Por si acaso
Scorer.SetLevelLimits(0,CharStats.GetCharExperienceCost(char.CharType,char.Level))
Scorer.SetLevelBarValue(char.PartialLevel)
Scorer.SetLevelValue(char.Level)




#
# Timers
#
Bladex.CreateTimer("Timer60",1.0/60.0)
Bladex.CreateTimer("Timer30",1.0/30.0)
Bladex.CreateTimer("Timer15",1.0/15.0)

#import pywin.debugger
#pywin.debugger.set_trace()


#
# Controls ( keyboard,mouse...) stuff
#
execfile("../../Scripts/InputInit.py")

import acts
acts.InitBindings("Player1")
acts.SetNoConfigurableActions()

try:
  execfile("../../Config/Control.py")
  print "BladeInit -> Executed Control.py"
except:
  execfile("../../Scripts/DefControl.py")
  print "BladeInit -> Executed DefControl.py"


#
# Demo Mode
#
import  Demo_Stuff
Demo_Stuff.Init()


#
# Menu
#
import Menu
Menu.InitMenuKeys()


execfile("../../Scripts/Globals.py")



Bladex.SetListenerPosition(1)
#
# FOR RELEASE VERSIONS, SET TO 0
#
#

if Reference.PYTHON_DEBUG >= 1:
	############### DEBUG LEVEL ONE ###############
	execfile("../../Scripts/DebugControl.py")

	if Reference.PYTHON_DEBUG >= 2:
		############### DEBUG LEVEL TWO ###############
		Bladex.SetCallCheck(3)
else:
	Bladex.SetCallCheck(0)

import ItemTypes
import math

import MenuWidget
Bladex.SetGamepadDisconnectFunc(0.0,MenuWidget.SetGamepadDisconnectFunc)

###
# This has been moved to the very bottom so that pj is defined and we can change the AnmCameras depending on current active character -LeadHead
# This still does present a problem if at any point during gameplay the player character's Kind changes
# But nobody would be that insane to do something like that, right?
###
# To modify the movements of the camera
#
import AnmCameras
AnmCameras.Init()
