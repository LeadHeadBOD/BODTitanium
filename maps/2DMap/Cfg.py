############################################################################################################
#
# 2DMap by wolfson
#
# GotoMapVars.VisitedMaps ---- Maps we already have been in.
# lugares.MapStatus ---------- Maps we can go to.
#  ---- .
#  ---- .
#
#
############################################################################################################
import Bladex
import AuxFuncs
import GotoMapVars
import Language
import LoadBar

LoadBar.ECTSProgressBar(175,"Blade_progress.jpg")

execfile("../../Scripts/sys_init.py")


GotoMapVars.Get2DMapValues()

#GotoMapVars.VisitedMaps[7] = 1 # parrrrrrche
if(	GotoMapVars.VisitedMaps[ 7] or
	GotoMapVars.VisitedMaps[ 8] or
	GotoMapVars.VisitedMaps[ 9] or
	GotoMapVars.VisitedMaps[10] or
	GotoMapVars.VisitedMaps[11] or
	GotoMapVars.VisitedMaps[12] or
	GotoMapVars.VisitedMaps[13] or
	GotoMapVars.VisitedMaps[14]):
	#print("mapagordo")
	Bladex.ReadLevel("mapa.lvl")
else:
	#print("mapequenio")
	Bladex.ReadLevel("ppiomapa.lvl")
	#print "Found 2DMap"

execfile("../../Scripts/BladeInit.py")

#GotoMapVars.VisitedMaps[14] = 1 # parrrrrrche

if not(GotoMapVars.VisitedMaps[14]):
	execfile("lugares.py")
	execfile("Behaviour.py")
	execfile("luces.py") # Where the weapons are # Have to load it conditionally
else:
	execfile("lugaresback.py")# Alternative file
	execfile("Behaviourback.py")# Alternative file
	execfile("lucesback.py")# Where the weapons are # Have to load it conditionally

# Always called
Bladex.AddMusicEventMP3("iniciaragnar",   "../../Sounds/MAPA2.mp3", 0.1, 1.0, 0.40, 10000, 0, -1 )
Bladex.AddScheduledFunc(Bladex.GetTime(),Bladex.ExeMusicEvent,(Bladex.GetMusicEvent("iniciaragnar"),))
execfile("nube.py")

AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)
import ScorerWidgets
import MenuText
Bladex.AddScheduledFunc(Bladex.GetTime(),AuxFuncs.FadeFrom,(4.5, 0.0))
InfoKeysWidget=BUIx.B_TextWidget(Scorer.wFrame,"InfoKeys","",ScorerWidgets.font_server,Language.LetrasMenuBig)
InfoKeysWidget.SetScale(0.5)
InfoKeysWidget.SetAlpha(0)
InfoKeysWidget.SetColor(249,128,0)
InfoKeysWidget.SetText(MenuText.GetMenuText("Press Left and Right to select your next destination. Press Enter to confirm"))
Scorer.wFrame.AddWidget(InfoKeysWidget,0.50,7,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

Bladex.AddScheduledFunc(Bladex.GetTime() + 0.1,InfoKeysWidget.SetAlpha,(.33,))
Bladex.AddScheduledFunc(Bladex.GetTime() + 0.2,InfoKeysWidget.SetAlpha,(.66,))
Bladex.AddScheduledFunc(Bladex.GetTime() + 0.3,InfoKeysWidget.SetAlpha,(1,))

import Scorer
AuxFuncs.SingleFrameFade()
Scorer.SetVisible(0)
