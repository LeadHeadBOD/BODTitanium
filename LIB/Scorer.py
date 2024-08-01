##///
##||| SCORER.PY TITANIUM
##||| Change list:
##||| * Added TrueEnergyBar
##||| * Will no longer show "Press F1" on Tutorial level, which is confusing.
##||| 
##\\\ 


import BUIx
import Bladex
#import Bldb
import ScorerWidgets
import WidgetsExtra
import ScorerActions
import PowDefWidgets
import Raster
import B3DLib
import math
import CharStats
import MenuText
import Language
from Reference import ENERGY_LOW_LEVEL
from Reference import DEMO_MODE




CURRENT_LEVEL_R=0
CURRENT_LEVEL_G=128
CURRENT_LEVEL_B=255

CURRENT_STRENGTH_R=251
CURRENT_STRENGTH_G=241
CURRENT_STRENGTH_B=2


E_ICON_DISTANCE = 37
E_CENTRAL_DISTANCE = 20
E_EDGAL_DISTANCE = 4
E_ARROW_DISTANCE = 40



def ReorderEnemies(me,enemies,FacedName):
	Left   = 0
	Right  = 0
	Result = [(-1,10.0), (-1,10.0),
	          (-1,10.0),
	          (-1,-10.0), (-1,-10.0)]
	if FacedName:
		CentralAngle = B3DLib.GetEntity2EntityAngle(me.Name,FacedName)
	else:
		CentralAngle = me.Angle

	for ename in range(len(enemies)):

		angle = ((B3DLib.GetEntity2EntityAngle(me.Name,enemies[ename][0]) - CentralAngle) % (3.1415*2))
		if angle > 3.1415:
			angle = angle-3.1415*2

		if math.fabs(angle) < math.fabs(Result[2][1]):
			Result[2] = (ename,angle)
		""" # PLAGUE: HD update uses the following "try". Why? Should I do it as well? What does it even do?
		try:
			if math.fabs(angle) < math.fabs(Result[2][1]):
				Result[2] = (ename,angle)
		except:
			pass
		"""

	for ename in range(len(enemies)):

		angle = ((B3DLib.GetEntity2EntityAngle(me.Name,enemies[ename][0]) - CentralAngle) % (3.1415*2))
		if angle > 3.1415:
			angle = angle-3.1415*2

		if ename==Result[2][0]:
			continue
		if angle > 0:
			if   angle < Result[1][1]:
				if Result[1][0] != -1:
					if Result[0][0] != -1:
						Left = Left+1
					Result[0] = Result[1]
				Result[1] = (ename,angle)
			elif angle < Result[0][1]:
				if Result[0][0] != -1:
					Left = Left+1
				Result[0] = (ename,angle)
			else:
				Left = Left+1
		else:
			if   angle > Result[3][1]:
				if Result[3][0] != -1:
					if Result[4][0] != -1:
						Right = Right+1
					Result[4] = Result[3]
				Result[3] = (ename,angle)
			elif angle > Result[4][1]:
				if Result[4][0] != -1:
					Right = Right+1
				Result[4] = (ename,angle)
			else:
				Right = Right+1

	return (Left,Right),Result




def SetEnemiesData(pj):
  enemies= pj.Data.visible_enemies
  arrows,ienemies=ReorderEnemies(pj,enemies,pj.ActiveEnemy)
  wEnemyBorderSelector.SetBorder(pj.ActiveEnemy!="")
  wEnemyMark.SetVisible(pj.ActiveEnemy!="")
  rw,rh=Raster.GetSize()
  if wants_auto_scale:
    if pj.ActiveEnemy:
      wEnemies[2].SetSize(35*rw/640,35*rh/480)
      wEnemiesVenoms[2].SetSize(35*rw/640,35*rh/480)
    else:
      wEnemies[2].SetSize(28*rw/640,28*rh/480)
      wEnemiesVenoms[2].SetSize(28*rw/640,28*rh/480)
  else:
    if pj.ActiveEnemy:
      wEnemies[2].SetSize(35,35)
      wEnemiesVenoms[2].SetSize(35,35)
    else:
      wEnemies[2].SetSize(28,28)
      wEnemiesVenoms[2].SetSize(28,28)

  wEnemyLeft.SetVisible(arrows[1]!=0)
  wEnemyRight.SetVisible(arrows[0]!=0)

  for x in range(5):

    idx = ienemies[4-x][0]
    if idx == -1:
    	wEnemies[x].SetVisible(0)
    	continue

    wEnemies[x].SetVisible(1)
    try:
    	wEnemies[x].SetBitmap(enemies[idx][1][0])
    except TypeError:
    	print "Bitmap not set for enemy "+enemies[idx][0]


    chartype = Bladex.GetCharType(pj.CharType,pj.CharTypeExt)
    if((x == 2) and (pj.ActiveEnemy != "")):
      wEnemies[x].SetAlpha(1.0)
    else:
      Alpha = (chartype.MaxCombatDist-B3DLib.GetXZDistance(pj.Name,enemies[idx][0]))/chartype.MaxCombatDist
      wEnemies[x].SetAlpha(Alpha)

    ent=Bladex.GetEntity(enemies[idx][0])
    if not ent:
    	print "The character called "+enemies[idx][0]+" has been destroyed"
    	continue
    #apply(wEnemies[x].SetColor, ent.Data.CurrentHealthColor)
    if ent.Data:
    	if ent.Data.Poisoned:
    		wEnemiesVenoms[x].SetVisible(1)
    	else:
    		wEnemiesVenoms[x].SetVisible(0)
    else:
    	wEnemiesVenoms[x].SetVisible(0)

    wEnemiesLifeLabels[x].SetText(`int(ent.Life)`)
    percentil  = ent.Life/CharStats.GetCharMaxLife(ent.Kind,ent.Level)
    if percentil>1.0:
    	percentil = 1
    wEnemyBarrLabels[x].SetPositionPercentage(percentil)
    wEnemyBarrLabels[x].SetBackgroundAlpha(wEnemies[x].GetAlpha())
    wEnemiesLevelLabels[x].SetText(`ent.Level+1`)
    inv = ent.GetInventory()
    key_found= inv.GetSpecialKey(0)
    if not key_found and inv.nKeys:
      key_found= inv.GetKey(0)
    if key_found:
      object= Bladex.GetEntity(key_found)
      if wEnemiesKeyLabels[x].GetBOD()!=object.Kind:
        wEnemiesKeyLabels[x].SetBOD(object.Kind)
      wEnemiesKeyLabels[x].SetVisible(1)
      if inv.nObjects:
        object= Bladex.GetEntity(inv.GetObject(0))
        if wEnemiesObjLabels[x].GetBOD()!=object.Kind:
          wEnemiesObjLabels[x].SetBOD(object.Kind)
        wEnemiesObjLabels[x].SetVisible(1)
      else:
        wEnemiesObjLabels[x].SetVisible(0)
    else:
      # If there's an object, put it in the key slot
      if inv.nObjects:
        object= Bladex.GetEntity(inv.GetObject(0))
        if wEnemiesKeyLabels[x].GetBOD()!=object.Kind:
          wEnemiesKeyLabels[x].SetBOD(object.Kind)
        wEnemiesKeyLabels[x].SetVisible(1)
      else:
        wEnemiesKeyLabels[x].SetVisible(0)
      wEnemiesObjLabels[x].SetVisible(0)
    wEnemies[x].RecalcLabelLayout(BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter)
    wEnemies[x].RecalcLabelLayout(BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom)

  wEnemiesFrame.RecalcLayout()


__wNULL=BUIx.CreateNULLWidget()
char=Bladex.GetEntity("Player1")









# Si esta a 1 hace que se escale el HUD, si esta a 0 entonces solo se ajustan las posiciones
# (y ademas queda mejor), pero como es una opcion no soportada no esta terminada del todo.
#
wants_auto_scale=0


# Frames ---------------------------------------------------------------------------------------------------
wFrame=BUIx.B_FrameWidget(__wNULL,"MainFrame",640,480)
wMessageFrame=BUIx.B_FrameWidget(__wNULL,"MessageFrame",640,480)
Bladex.SetMessageWidget( wMessageFrame.GetPointer() )
wLeftFrame=BUIx.B_FrameWidget(wFrame,"BarsFrame",195,65)
wEnemiesFrame=BUIx.B_FrameWidget(wFrame,"EnemiesFrame",E_ICON_DISTANCE*5+E_CENTRAL_DISTANCE*2+E_ARROW_DISTANCE*2,65)
wObjectsFrame=ScorerWidgets.B_ObjectsFrame(wFrame,"ObjectsFrame",125,65,char)
wLogFrame=BUIx.B_FrameWidget(wFrame,"LogFrame",125,65)
#wKeysFrame=BUIx.B_FrameWidget(wFrame,"KeysFrame",50,65)
wKeysRFrame=BUIx.B_FrameWidget(wFrame,"KeysRFrame",50,65)
wSpecialsFrame=BUIx.B_FrameWidget(wFrame,"SpecialsFrame",180,32)



# Texto  ----------------------------------------------------------------------------------------------------
wGameText=BUIx.B_TextWidget(wFrame,"GameTextWidget","\n\n\n\n\n",ScorerWidgets.font_server,Language.LetrasMenuBig)
#wGameText=ScorerWidgets.B_GameTextWidget(wFrame,"GameTextWidget")
wGameText.SetScale(0.5)
wGameText.SetAlpha(1)
wGameText.SetColor(255,255,255)



# Travel Book Warning--------------------------------------------------------------------------------------------
Widget = BUIx.B_TextWidget(wFrame, "pressF1","",ScorerWidgets.font_server,Language.MapaDeLetrasHi)
Widget.SetText(MenuText.GetMenuText("PRESS") + "${\" F1\":LaunchTravel}")
Widget.SetScale(0.28)
Widget.SetAlpha(1)
Widget.SetColor(240,51,2)
Widget.SetVisible(1)

wFramePress=BUIx.B_FrameWidget(wFrame,"PressFrame",80,18)
wFramePress.SetVisible(0)
wFramePress.AddWidget(Widget,0,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

wFrame.AddWidget(wFramePress,0,0,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

TBookSword=BUIx.B_BitmapWidget(wFrame,"TBookSword",126,22,"PRESSF1","../../Data/mmps/PRESSF1_hi_empty.png")
TBookSword.SetColor(255,255,255)
TBookSword.SetAlpha(1.0)
TBookSword.SetVisible(0)
wFrame.AddWidget(TBookSword,0,0,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)

TBS=Bladex.CreateSound("../../Sounds/M-DESENFUNDA-PIEDRA.wav","TBWarning")
TBS.Volume=1.0
TBS.MinDistance=1000000.0
TBS.MaxDistance=2000000

def SlideTBS(dir,time = 0):
	if Bladex.GetCurrentMap() == "Tutorial":    # Stolen from HD update
		return                                  #       -LeadHead
	TBS.PlayStereo()
	SlideTBS2(dir,time)

def SlideTBS2(dir,time = 0):

	global TBookSword
	MarcoAnchoTex = 201
	if time < 0.25:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.015,SlideTBS2,(dir,time + 0.02))
	else:
		time = 0.25

	if dir:
		XPos = -MarcoAnchoTex * time * 4
	else:
		TBookSword.SetVisible(1)
		wFramePress.SetVisible(1)
		XPos = -MarcoAnchoTex + (MarcoAnchoTex * time * 4)

		wFrame.MoveWidgetTo("TBookSword",XPos,0)
		wFrame.MoveWidgetTo("Widget",XPos,0)

	Bladex.AddScheduledFunc(Bladex.GetTime() + 10,HideTBS,())

def HideTBS():
	global TBookSword
	TBookSword.SetVisible(0)
	wFramePress.SetVisible(0)



# Barras de vida --------------------------------------------------------------------------------------------
BAR_DELTA = 26
Bladex.ReadBitMap("../../Data/Vida.bmp","Vida")
Bladex.ReadBitMap("../../Data/Vida enemigo 8.bmp","BitmapBarraEnemigo")



wLifeBar=WidgetsExtra.B_FlashBarWidget(wLeftFrame,"LifeBar",116+BAR_DELTA,10)
wLifeBar.SetColor(255,0,0)
wLifeBar.SetFlashColor(53, 141, 36)
wLifeBar.SetFlash(0)
wLifeBar.Continuous= 1
wLifeBar.SetBackgroundAlpha(0.0)
wLifeBar.SetAlpha(1.0)
wLifeBar.SetBitmap("Vida")


##def wLifeBarSizeChanged(x,y):
##  print "wLifeBarSizeChanged",x,y
##
##wLifeBar.SetSizeChangedFunc(wLifeBarSizeChanged)

wLifeLabel=BUIx.B_TextWidget(wLifeBar,"LifeLabel","100/100",ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wLifeLabel.SetColor(255,0,0)
wLifeLabel.SetAlpha(1.0)
wLifeLabel.SetScale(0.25)
wOffset = -2
if Language.Current == "Russian":
    wOffset = 0
wLifeBar.AddLabel(wLifeLabel,4-BAR_DELTA,wOffset,
                  BUIx.B_Widget.B_LAB_Right,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_AbsoluteLeft,BUIx.B_Widget.B_FR_Left,
                  BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                  )


wPoisonLabel=BUIx.B_TextWidget(wLifeBar,"PoisonLabel",MenuText.GetMenuText("POISONED"),ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wPoisonLabel.SetColor(85,105,60)
wPoisonLabel.SetAlpha(1.0)
wPoisonLabel.SetScale(0.25)
wLifeBar.AddLabel(wPoisonLabel,0.4,0.5,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )
wPoisonLabel.SetVisible(0)




# Barra de nivel -------------------------------------------------------------------------------------------
wLifeMarker = BUIx.B_BitmapWidget(wLeftFrame,"ObjNameBg",205,51,"MARCADORVIDAYXP","../../Data/marcadorvidayxp.mmp");
wLifeMarker.SetColor(255,255,255)
wLifeMarker.SetAlpha(1.0)



wLevelBar=ScorerWidgets.B_SmoothBarWidget(wLeftFrame,"LevelBar",116+BAR_DELTA,5)
#wLevelBar=BUIx.B_BarWidget(wLeftFrame,"LevelBar",180,8)
wLevelBar.SetColor(CURRENT_LEVEL_R,CURRENT_LEVEL_G,CURRENT_LEVEL_B)
wLevelBar.SetAlpha(1.0)
wLevelBar.SetBackgroundAlpha(0.0)
wLevelBar.SetBackgroundColor(0,80,110)


#wLevelUpLabel=BUIx.B_TextWidget(wLevelBar,"LevelUpLabel",MenuText.GetMenuText("LEVEL UP"),ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wLevelUpLabel=WidgetsExtra.B_FlashTextWidget(wLevelBar,"LevelUpLabel",MenuText.GetMenuText("LEVEL UP"),ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wLevelUpLabel.SetColor(170,170,170)
wLevelUpLabel.SetAlpha(1.0)
wLevelUpLabel.SetVisible(0)
wLevelUpLabel.SetScale(0.25)
wLevelBar.AddLabel(wLevelUpLabel,0,2,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_Bottom,
                  BUIx.B_Widget.B_FR_AbsoluteRight,BUIx.B_Widget.B_FR_Right,
                  BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                  )


wCurrentLevelLabel=BUIx.B_TextWidget(wLevelBar,"CurrentLevelLabel","Level 5",ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wCurrentLevelLabel.SetColor(0,159,220)
wCurrentLevelLabel.SetAlpha(1.0)
wCurrentLevelLabel.SetScale(0.25)
wOffset = -4
if Language.Current == "Russian":
    wOffset = -2
wLevelBar.AddLabel(wCurrentLevelLabel,6-BAR_DELTA,wOffset,
                  BUIx.B_Widget.B_LAB_Right,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_AbsoluteLeft,BUIx.B_Widget.B_FR_Left,
                  BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                  )
wLevelBar.SetBitmap("Vida")

# Barra de un bar    -------------------------------------------------------------------------------------------
wLowBarFrame=BUIx.B_FrameWidget(wFrame,"LowBarFrame",176, 22)
wLowBarFrame.SetVisible(1)


wEnergyBmp=BUIx.B_BitmapWidget(wLowBarFrame,"EnergyBmp",176, 22,"MARCADORLANZAMAGOTAM","../../Data/marcadorlanzamagotam.mmp")
wEnergyBmp.SetColor(255,255,255)
wEnergyBmp.SetAlpha(1.0)
wEnergyBmp.SetVisible(1)

# Barra de strength  -------------------------------------------------------------------------------------------
wStrengthBar=ScorerWidgets.B_SmoothBarWidget(wLowBarFrame,"StrengthBar",112*(8.0/6.5),8)
wStrengthBar.SetColor(CURRENT_STRENGTH_R,CURRENT_STRENGTH_G,CURRENT_STRENGTH_B)
wStrengthBar.SetAlpha(0.75)
wStrengthBar.SetBackgroundAlpha(0.0)
wStrengthBar.SetBackgroundColor(CURRENT_STRENGTH_R,CURRENT_STRENGTH_G,CURRENT_STRENGTH_B)
wStrengthBar.SetVisible(0)
wStrengthBar.SetBitmap("Vida")

wMaxPowerLabel=WidgetsExtra.B_FlashTextWidget(wStrengthBar,"MaxPowerLabel",MenuText.GetMenuText("Maximun power"),ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wMaxPowerLabel.SetColor(255,255,255)
wMaxPowerLabel.SetAlpha(1.0)
wMaxPowerLabel.SetVisible(0)
wMaxPowerLabel.SetScale(0.25)
wStrengthBar.AddLabel(wMaxPowerLabel,0.4,0.32,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )

wStrengthLabel=WidgetsExtra.B_FlashTextWidget(wStrengthBar,"StrengthLabel",MenuText.GetMenuText("Launch"),ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wStrengthLabel.SetColor(251,210,99)
wStrengthLabel.SetAlpha(1.0)
wStrengthLabel.SetFlash(0.0)
wStrengthLabel.SetScale(0.25)
wStrengthBar.AddLabel(wStrengthLabel,9,0.32,
                  BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_AbsoluteRight,BUIx.B_Widget.B_FR_Right,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )

#wStrengthBar.SetBitmap("BitmapBarra")

# Barra de energy  -------------------------------------------------------------------------------------------
## Original energy bar
wEnergyBar=ScorerWidgets.B_SmoothBarWidget(wLowBarFrame,"EnergyBar",112*(8.0/6.5),8)
wEnergyBar.SetColor(0,255,128)
wEnergyBar.SetAlpha(0.25) # was 0.75, overriden back to this value every frame if using original energy config -LeadHead
wEnergyBar.SetBackgroundAlpha(0.0)
wEnergyBar.SetBackgroundColor(64,64,64)
wEnergyBar.SetVisible(0)
wEnergyBar.SetBitmap("Vida")

## "TRUE" energy bar    -LeadHead
wTrueEnergyBar=ScorerWidgets.B_SmoothBarWidget(wLowBarFrame,"TrueEnergyBar",112*(8.0/6.5),8)
wTrueEnergyBar.SetColor(0,255,128)
wTrueEnergyBar.SetAlpha(0.75)
wTrueEnergyBar.SetBackgroundAlpha(0.0)
wTrueEnergyBar.SetBackgroundColor(64,64,64)
wTrueEnergyBar.SetVisible(0)
wTrueEnergyBar.SetBitmap("Vida")

wDangerLabel=WidgetsExtra.B_FlashTextWidget(wEnergyBar,"DangerLabel",MenuText.GetMenuText("Low energy"),ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wDangerLabel.SetColor(238,191,0)
wDangerLabel.SetAlpha(1.0)
wDangerLabel.SetVisible(0)
wDangerLabel.SetScale(0.25)
wEnergyBar.AddLabel(wDangerLabel,0.4,0.5,
                  BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_HRelative, BUIx.B_Widget.B_FR_HCenter,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )

wEnergyMaxLabel=WidgetsExtra.B_FlashTextWidget(wEnergyBar,"EnergyMaxLabel","100",ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wEnergyMaxLabel.SetColor(0,255,128)
wEnergyMaxLabel.SetAlpha(1)
wEnergyMaxLabel.SetVisible(1)
wEnergyMaxLabel.SetScale(0.25)
wEnergyBar.AddLabel(wEnergyMaxLabel,7,0.5,
                  BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter,
                  BUIx.B_Widget.B_FR_AbsoluteRight, BUIx.B_Widget.B_FR_Right,
                  BUIx.B_Widget.B_FR_VRelative, BUIx.B_Widget.B_FR_VCenter
                  )


wLowBarFrame.AddWidget(wStrengthBar,56,6)

wLowBarFrame.AddWidget(wTrueEnergyBar,56,6) # Added

wLowBarFrame.AddWidget(wEnergyBar,56,6)

wLowBarFrame.AddWidget(wEnergyBmp,0,0)


# Llaves ---------------------------------------------------------------------------------------------------
wKey1=ScorerWidgets.B_InvKey3DWidget(wObjectsFrame,"Key1",32,32,"Llave",char)
#wKey2=ScorerWidgets.B_InvKeyRing3DWidget(wKeysFrame,"Key2",32,32,"Llavero",char)

# Nuevo Objeto ---------------------------------------------------------------------------------------------------
wNewObject=ScorerWidgets.B_Obj3DWidget (wLogFrame,"NewObject",32,32,"Llave")
wNewObject.Scale=0
wNewObject.SetAlpha(1.0)
wLogFrame.AddWidget(wNewObject,0.5,3,
                        BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                        BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

wNewObjectText=WidgetsExtra.B_FlashTextWidget(wLogFrame,"DangerLabel","el comoe'",ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wNewObjectText.SetColor(255,255,255)
wNewObjectText.SetAlpha(1.0)
wNewObjectText.SetFlash(10)
wNewObjectText.SetScale(0.25)

wLogFrame.AddWidget(wNewObjectText,0.5,40,
                        BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                        BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)



# Especials ---------------------------------------------------------------------------------------------------
wSpecialKey1=ScorerWidgets.B_InvSpecialKeyWidget(wSpecialsFrame,"BEETLE",22,22,char)
wSpecialKey2=ScorerWidgets.B_InvSpecialKeyWidget(wSpecialsFrame,"SPIDER",22,22,char)
wSpecialKey3=ScorerWidgets.B_InvSpecialKeyWidget(wSpecialsFrame,"SHELL",22,22,char)
wSpecialKey4=ScorerWidgets.B_InvSpecialKeyWidget(wSpecialsFrame,"STAR",22,22,char)

wTablet1=ScorerWidgets.B_InvTabletWidget(wSpecialsFrame,"Tablilla1","!", char,0)
wTablet2=ScorerWidgets.B_InvTabletWidget(wSpecialsFrame,"Tablilla2","\"",char,1)
wTablet3=ScorerWidgets.B_InvTabletWidget(wSpecialsFrame,"Tablilla3","#", char,2)
wTablet4=ScorerWidgets.B_InvTabletWidget(wSpecialsFrame,"Tablilla4","$$", char,3)
wTablet5=ScorerWidgets.B_InvTabletWidget(wSpecialsFrame,"Tablilla5","%", char,4)
wTablet6=ScorerWidgets.B_InvTabletWidget(wSpecialsFrame,"Tablilla6","&", char,5)


"""
# Objetos --------------------------------------------------------------------------------------------------
wSelObjectText=BUIx.B_TextWidget(wObjectsFrame,"SelObjectText","RED GEM  +10% EXP",
                 ScorerWidgets.font_server,Language.MapaDeLetrasHi)
wSelObjectText.SetColor(170,170,170)
wSelObjectText.SetAlpha(0.5)
"""



# Enemigos -------------------------------------------------------------------------------------------------
wEnemy1,wEnemyVenom1,wEnemy1LifeLabel,wEnemy1LevelLabel,wEnemy1KeyLabel,wEnemy1ObjLabel,wEnemy1BarrLabel=ScorerWidgets.CreateEnemyWidget("wEnemy1",wEnemiesFrame,wants_auto_scale)
wEnemy1.SetAlpha(0.25)

wEnemy2,wEnemyVenom2,wEnemy2LifeLabel,wEnemy2LevelLabel,wEnemy2KeyLabel,wEnemy2ObjLabel,wEnemy2BarrLabel=ScorerWidgets.CreateEnemyWidget("wEnemy2",wEnemiesFrame,wants_auto_scale)
wEnemy2.SetAlpha(1.0)

wEnemy3,wEnemyVenom3,wEnemy3LifeLabel,wEnemy3LevelLabel,wEnemy3KeyLabel,wEnemy3ObjLabel,wEnemy3BarrLabel=ScorerWidgets.CreateEnemyWidget("wEnemy3",wEnemiesFrame,wants_auto_scale,35)
wEnemy3.SetAlpha(0.25)

wEnemy4,wEnemyVenom4,wEnemy4LifeLabel,wEnemy4LevelLabel,wEnemy4KeyLabel,wEnemy4ObjLabel,wEnemy4BarrLabel=ScorerWidgets.CreateEnemyWidget("wEnemy4",wEnemiesFrame,wants_auto_scale)
wEnemy4.SetAlpha(0.25)

wEnemy5,wEnemyVenom5,wEnemy5LifeLabel,wEnemy5LevelLabel,wEnemy5KeyLabel,wEnemy5ObjLabel,wEnemy5BarrLabel=ScorerWidgets.CreateEnemyWidget("wEnemy5",wEnemiesFrame,wants_auto_scale)
wEnemy5.SetAlpha(0.25)



wEnemies=[wEnemy1,wEnemy2,wEnemy3,wEnemy4,wEnemy5]
wEnemiesVenoms=[wEnemyVenom1,wEnemyVenom2,wEnemyVenom3,
                   wEnemyVenom4,wEnemyVenom5]
wEnemiesLifeLabels=[wEnemy1LifeLabel,wEnemy2LifeLabel,wEnemy3LifeLabel,
                   wEnemy4LifeLabel,wEnemy5LifeLabel]
wEnemiesLevelLabels=[wEnemy1LevelLabel,wEnemy2LevelLabel,wEnemy3LevelLabel,
                   wEnemy4LevelLabel,wEnemy5LevelLabel]
wEnemiesKeyLabels=[wEnemy1KeyLabel,wEnemy2KeyLabel,wEnemy3KeyLabel,
                   wEnemy4KeyLabel,wEnemy5KeyLabel]
wEnemiesObjLabels=[wEnemy1ObjLabel,wEnemy2ObjLabel,wEnemy3ObjLabel,
                   wEnemy4ObjLabel,wEnemy5ObjLabel]
wEnemyBarrLabels =[wEnemy1BarrLabel,wEnemy2BarrLabel,wEnemy3BarrLabel,
                   wEnemy4BarrLabel,wEnemy5BarrLabel]


wLeftFrame.AddWidget(wLifeBar,14,6)
wLeftFrame.AddWidget(wLevelBar,14,24)
wLeftFrame.AddWidget(wLifeMarker,1,1)

wObjectsFrame.AddWidget(wKey1,0,72)

#wKeysRFrame.AddWidget(wKey2,0,6)

wLeftFrame.AddWidget(wSpecialsFrame,15,38)
#wRightFrame.AddWidget(wKeysFrame,8,95)

wSpecialsFrame.AddWidget(wSpecialKey1,0,0)
wSpecialsFrame.AddWidget(wSpecialKey2,21,0)
wSpecialsFrame.AddWidget(wSpecialKey3,43,0)
wSpecialsFrame.AddWidget(wSpecialKey4,65,0)

dlt = 0
wSpecialsFrame.AddWidget(wTablet1, 96-dlt,0)
wSpecialsFrame.AddWidget(wTablet2,110-dlt,0)
wSpecialsFrame.AddWidget(wTablet3,124-dlt,0)
wSpecialsFrame.AddWidget(wTablet4,138-dlt,0)
wSpecialsFrame.AddWidget(wTablet5,152-dlt,0)
wSpecialsFrame.AddWidget(wTablet6,166-dlt,0)


"""
wObjectsFrame.AddWidget(wSelObjectText,0.5,53,
                        BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                        BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
"""


wEnemyLeft=BUIx.B_BitmapWidget(wEnemiesFrame,"FlechaIzquierda",40,40,"FLECHAENEMIGODERECHA","../../Data/flechaenemigoderecha.mmp")
wEnemiesFrame.AddWidget(wEnemyLeft,0,E_EDGAL_DISTANCE,
                              BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
wEnemyLeft.SetAlpha(1.0)
wEnemyLeft.SetColor(255,255,255)


i = 0
c = 0
wEnemiesFrame.AddWidget(wEnemies[i],E_ICON_DISTANCE*i+c*E_CENTRAL_DISTANCE+E_ARROW_DISTANCE,E_EDGAL_DISTANCE,
                              BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
i = 1
c = 0
wEnemiesFrame.AddWidget(wEnemies[i],E_ICON_DISTANCE*i+c*E_CENTRAL_DISTANCE+E_ARROW_DISTANCE,E_EDGAL_DISTANCE,
                              BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)


# Marcador centraL
wEnemyMark=BUIx.B_BitmapWidget(wEnemiesFrame,"SelectorEnemigo",80,80,"SELECTORENEMIGO","../../Data/selectorenemigo.mmp");
wEnemiesFrame.AddWidget(wEnemyMark,0.56,-10,
                           BUIx.B_FrameWidget.B_FR_HRelative,  BUIx.B_FrameWidget.B_FR_HCenter,
                           BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
wEnemyMark.SetAlpha(1.0)
wEnemyMark.SetColor(255,255,255)


i = 2
c = 1
# Cuadrado rojo
wEnemyBorderSelector=BUIx.B_RectWidget(wEnemies[i],"CentralBitmapBorder",35,35)
wEnemyBorderSelector.SetBorderColor(255,0,0)
wEnemies[i].AddLabel(wEnemyBorderSelector,0,0,
                    BUIx.B_Widget.B_LAB_HCenter,BUIx.B_Widget.B_LAB_VCenter,
                    BUIx.B_Widget.B_FR_Left,BUIx.B_Widget.B_FR_Left,
                    BUIx.B_Widget.B_FR_AbsoluteTop,BUIx.B_Widget.B_FR_Top
                    )
# Enemigo del centro
wEnemiesFrame.AddWidget(wEnemies[i],E_ICON_DISTANCE*i+c*E_CENTRAL_DISTANCE+E_ARROW_DISTANCE,E_EDGAL_DISTANCE,
                              BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)




i = 3
c = 2
wEnemiesFrame.AddWidget(wEnemies[i],E_ICON_DISTANCE*i+c*E_CENTRAL_DISTANCE+E_ARROW_DISTANCE,E_EDGAL_DISTANCE,
                              BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

i = 4
c = 2
wEnemiesFrame.AddWidget(wEnemies[i],E_ICON_DISTANCE*i+c*E_CENTRAL_DISTANCE+E_ARROW_DISTANCE,E_EDGAL_DISTANCE,
                              BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)


wEnemyRight=BUIx.B_BitmapWidget(wEnemiesFrame,"FlechaDerecha",40,40,"FLECHAENEMIGOIZQUIERDA","../../Data/flechaenemigoizquierda.mmp");
wEnemiesFrame.AddWidget(wEnemyRight,E_ICON_DISTANCE*5+2*E_CENTRAL_DISTANCE+E_ARROW_DISTANCE,E_EDGAL_DISTANCE,
                              BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
wEnemyRight.SetAlpha(1.0)
wEnemyRight.SetColor(255,255,255)


RInitAlpha=[1.0,0.3,0.2,0.1,0.05]
RInitPositions=[(5,10),(35,20),(75,30),(110,40),(140,50)]
wRightHand=ScorerWidgets.B_HandWidget(wFrame,"RightHand",150,150,"Right",
                                      RInitAlpha,RInitPositions)
LInitAlpha=[1.0,0.3,0.2,0.1]
LInitPositions=[(5,10),(35,20),(75,30),(110,40)]
wLeftHand=ScorerWidgets.B_HandWidget(wFrame,"LefttHand",150,150,"Left",
                                      LInitAlpha,LInitPositions)

wArrowInfo=ScorerWidgets.InvArrowsControl(wFrame,"ArrowInfo",150,150,char,wants_auto_scale)

#wQuiverHand=ScorerWidgets.B_HandWidget(wFrame,"LefttHand",150,150,"Left",
#                                      InitAlpha,InitPositions)




wFrame.AddWidget(wLeftFrame,4,4)
#wFrame.AddWidget(wKeysRFrame,196,0)
wFrame.AddWidget(wObjectsFrame,12,0,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                              BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

wFrame.AddWidget(wLogFrame,12,0,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                              BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)


wFrame.AddWidget(wEnemiesFrame,0.5,0,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                              BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
wFrame.AddWidget(wRightHand,6,20,BUIx.B_FrameWidget.B_FR_AbsoluteRight,BUIx.B_FrameWidget.B_FR_Right,
                              BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
wFrame.AddWidget(wLeftHand,6,20,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                              BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
wFrame.AddWidget(wArrowInfo,6,20,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                              BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


wFrame.AddWidget(wGameText,0.5,27,
                           BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                           BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


wFrame.AddWidget(wLowBarFrame,0.5,2,
                           BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,
                           BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)


#wFrame.SetFocus("LeftFrame")
#wFrame.SetClipDraw(1)

ShieldsControl=ScorerWidgets.InvShieldControl("Shields",wLeftHand,char,
                                              view_period=1.4,cycle_period=0.3,fadein_period=0.3,
                                              fadeout_period=0.3,
                                              end_cycle_callback=ScorerActions.CB_ShieldOut,
                                              Wants_auto_scale=wants_auto_scale)
WeaponsControl=ScorerWidgets.InvWeaponsControl("Weapons",wRightHand,char,ShieldsControl,
                                              view_period=1.4,cycle_period=0.3,fadein_period=0.3,
                                              fadeout_period=0.3,
                                              end_cycle_callback=ScorerActions.CB_WeaponOut,
                                              Wants_auto_scale=wants_auto_scale)
ObjectsControl=ScorerWidgets.InvObjectsControl("Objects",wObjectsFrame,char,
                                              view_period=1.4,cycle_period=0.2,fadein_period=0.3,
                                              fadeout_period=0.3,
                                              end_cycle_callback=ScorerActions.IncCallBack,
                                              Wants_auto_scale=wants_auto_scale)



PowDefWidgets.CreateWidgest()
PowDefWidgets.Activate()


wFrame.SetAutoScale(1)
wMessageFrame.SetAutoScale(1)

if wants_auto_scale:
  wLeftFrame.SetAutoScale(1)
  wEnemiesFrame.SetAutoScale(1)
  wLowBarFrame.SetAutoScale(1)
  wObjectsFrame.SetAutoScale(1)
  #wKeysFrame.SetAutoScale(1)
  #wKeysRFrame.SetAutoScale(1)
  wSpecialsFrame.SetAutoScale(1)

  wGameText.SetAutoScale(1)
  wLifeBar.SetAutoScale(1)
  wLifeLabel.SetAutoScale(1)
  wPoisonLabel.SetAutoScale(1)
  wLevelBar.SetAutoScale(1)
  wLevelUpLabel.SetAutoScale(1)
  wLevelBar.SetAutoScale(1)
  wCurrentLevelLabel.SetAutoScale(1)
  wStrengthBar.SetAutoScale(1)
  wMaxPowerLabel.SetAutoScale(1)
  wStrengthLabel.SetAutoScale(1)
  wTrueEnergyBar.SetAutoScale(1)    # Added
  wEnergyBar.SetAutoScale(1)
  wDangerLabel.SetAutoScale(1)
  wEnergyMaxLabel.SetAutoScale(1)
  TBookSword.SetAutoScale(1)
  Widget.SetAutoScale(1)
  wLifeMarker.SetAutoScale(1)
  wEnergyBmp.SetAutoScale(1)

  wKey1.SetAutoScale(1)
  #wKey2.SetAutoScale(1)

  wSpecialKey1.SetAutoScale(1)
  wSpecialKey2.SetAutoScale(1)
  wSpecialKey3.SetAutoScale(1)
  wSpecialKey4.SetAutoScale(1)

  wTablet1.SetAutoScale(1)
  wTablet2.SetAutoScale(1)
  wTablet3.SetAutoScale(1)
  wTablet4.SetAutoScale(1)
  wTablet5.SetAutoScale(1)
  wTablet6.SetAutoScale(1)

  wEnemyBorderSelector.SetAutoScale(1)
  wEnemyLeft.SetAutoScale(1)
  wEnemyRight.SetAutoScale(1)
  wEnemyMark.SetAutoScale(1)
  for x in range(5):
    wEnemies[x].SetAutoScale(1)
    wEnemiesVenoms[x].SetAutoScale(1)
    wEnemiesLifeLabels[x].SetAutoScale(1)
    wEnemiesLevelLabels[x].SetAutoScale(1)
    wEnemiesKeyLabels[x].SetAutoScale(1)
    wEnemiesObjLabels[x].SetAutoScale(1)
    wEnemyBarrLabels[x].SetAutoScale(1)


  wEnemyBorderSelector.SetAutoScale(1)
  wEnemyLeft.SetAutoScale(1)
  wEnemyRight.SetAutoScale(1)
  wEnemyMark.SetAutoScale(1)
  for x in range(5):
    wEnemies[x].SetAutoScale(1)
    wEnemiesVenoms[x].SetAutoScale(1)
    wEnemiesLifeLabels[x].SetAutoScale(1)
    wEnemiesLevelLabels[x].SetAutoScale(1)
    wEnemiesKeyLabels[x].SetAutoScale(1)
    wEnemiesObjLabels[x].SetAutoScale(1)
    wEnemyBarrLabels[x].SetAutoScale(1)


  PowDefWidgets.DefTextWidget.SetAutoScale(1)
  PowDefWidgets.PowTextWidget.SetAutoScale(1)
  PowDefWidgets.DefBmpWidget.SetAutoScale(1)
  PowDefWidgets.PowBmpWidget.SetAutoScale(1)
  PowDefWidgets.wDefFrame.SetAutoScale(1)
  PowDefWidgets.wPowFrame.SetAutoScale(1)

  wLogFrame.SetAutoScale(1)
  wNewObjectText.SetAutoScale(1)
  wNewObject.SetAutoScale(1)




ObjectsControl.view_period = 3.0  # Modify it to change the time of the inventory.

def ActivateScorer():
    wLeftHand.SetVisible(0)
    wRightHand.SetVisible(0)
    wLogFrame.SetVisible(0)
    wObjectsFrame.SetVisible(0)
    #wKeysFrame.SetVisible(1)
    #wKeysRFrame.SetVisible(1)
    wSpecialsFrame.SetVisible(1)
    Bladex.SetRootWidget(wFrame.GetPointer())

def ViewScorer(v):
  wFrame.SetVisible(v)


def ViewEnemies(v):
  wEnemiesFrame.SetVisible(v)


def ViewBars(v):
  wLeftFrame.SetVisible(v)




def ViewObjects(v):
  wObjectsFrame.SetVisible(v)
  wLogFrame.SetVisible(0)



def AddLifeValue(v):
  wLifeBar.AddValue(v)
  #print str(v)
  #wLifeLabel.SetText(str(v))


last_poisoned      = 0
last_lifeValue     = -100
last_MaxLifeValue  = -100
last_levelValue    = -100

def SetLifeValue(v,maxvalue,poisoned):
  global last_poisoned
  global last_lifeValue
  global last_MaxLifeValue

  doit = 0

  #Bldb.set_trace()
  if (last_lifeValue!=v) or (last_MaxLifeValue!=maxvalue):
    doit = 1
    wLifeBar.SetPositionPercentage(v/maxvalue*(6.5/8.0))
    wLifeLabel.SetText(str(int(v))+"/"+str(maxvalue))
    last_lifeValue = v
    last_MaxLifeValue = maxvalue

  if poisoned!=last_poisoned:
    doit = 1
    wPoisonLabel.SetVisible(poisoned)
    last_poisoned=poisoned
    if poisoned:
      wLifeBar.SetColor(0,66,19)
      wLifeBar.SetFlash(3)
      #wLifeBar2.SetColor(0,83,24)
    else:
      wLifeBar.SetColor(255,0,0)
      wLifeBar.SetFlash(0)
      #wLifeBar2.SetColor(163,28,0)

  if doit:
     wLeftFrame.RecalcLayout()


def SetLevelValue(v):
  global last_levelValue

  if last_levelValue!=v:
     wCurrentLevelLabel.SetText(MenuText.GetMenuText("Level")+" "+str(v+1))
     last_levelValue=v
     wLeftFrame.RecalcLayout()



def SetLevelBarValue(v):
  wLevelBar.SetPosition(v*(6.5/8.0))



def SetLevelLimits(inf,sup):
  wLevelBar.SetLimits(inf,sup)




def __level_up_aux():
  wLevelUpLabel.SetFlash(0)
  wLevelUpLabel.SetVisible(0)


def LevelUp():
  wLevelUpLabel.SetFlash(15)
  wLevelUpLabel.SetVisible(1)
  now=Bladex.GetTime()
  Bladex.AddScheduledFunc(now+2.0,__level_up_aux,())

VISIBLE=1

def SetStrengthBarValue(v):
  wTrueEnergyBar.SetVisible(0)  # Added
  wEnergyBar.SetVisible(0)
  if VISIBLE:
  	wStrengthBar.SetVisible(1)

  old_pos= wStrengthBar.GetPositionPercentage()
  wStrengthBar.SetPositionPercentage(v*(6.5/8.0))

  if v>=1.0:
    if old_pos<1.0:
        wMaxPowerLabel.SetFlash(14)
        wStrengthLabel.SetFlash(14)
        wMaxPowerLabel.SetVisible(1)
  else:
  	wMaxPowerLabel.SetVisible(0)
  	wStrengthLabel.SetFlash(0.0)

def SetEnergyBarValue(v, max_v):
  wTrueEnergyBar.SetVisible(0)  # Added
  wEnergyBar.SetAlpha(0.75)     # Resets EnergyBar back to original settings.   -LeadHead
  wStrengthBar.SetVisible(0)
  if VISIBLE:
  	wEnergyBar.SetVisible(1)
  pos= min(max(v/max_v, 0),1.0)
  wEnergyBar.SetPositionPercentage(pos*(6.5/8.0))
  wEnergyMaxLabel.SetText(`max_v`)
  wEnergyBar.RecalcLabelLayout(BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter)
  if pos<=ENERGY_LOW_LEVEL:
  	wDangerLabel.SetFlash(14)
  	wDangerLabel.SetVisible(1)
  else:
  	wDangerLabel.SetVisible(0)
  	
  	
## New Energy Bar -LeadHead
def SetTrueEnergyBarValue(v, max_v, v_to_lose):
  wEnergyBar.SetAlpha(0.25)
  wStrengthBar.SetVisible(0)
  if VISIBLE:
  	wEnergyBar.SetVisible(1)
  	wTrueEnergyBar.SetVisible(1)
  pos= min(max(v/max_v, 0),1.0)
  wEnergyBar.SetPositionPercentage(pos*(6.5/8.0))
  wEnergyMaxLabel.SetText(`max_v`)
  wEnergyMaxLabel.SetAlpha(1)
  wEnergyBar.RecalcLabelLayout(BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter)
  v_true = (v - v_to_lose)
  pos_true= min(max((v_true/max_v),0),1.0)
  wTrueEnergyBar.SetPositionPercentage(pos_true*(6.5/8.0))
  wTrueEnergyBar.RecalcLabelLayout(BUIx.B_Widget.B_LAB_Left,BUIx.B_Widget.B_LAB_VCenter)
  if (v_true/max_v) <= ENERGY_LOW_LEVEL:
  	wDangerLabel.SetFlash(14)
  	wDangerLabel.SetVisible(1)
  else:
  	wDangerLabel.SetVisible(0)

def SetVisible(vis):
  global VISIBLE
  VISIBLE=vis
  if vis==0:
    HideTBS()
    wLeftHand.SetVisible(vis)
    wRightHand.SetVisible(0)
    PowDefWidgets.Deactivate()
  else:
    PowDefWidgets.Activate()
  #wKeysFrame.SetVisible(vis)
  #wKeysRFrame.SetVisible(vis)
  wSpecialsFrame.SetVisible(vis)
  wEnemiesFrame.SetVisible(vis)
  wLeftFrame.SetVisible(vis)
  wArrowInfo.SetVisible(vis)

  wTrueEnergyBar.SetVisible(0)    # Added
  wEnergyBar.SetVisible(0)
  wStrengthBar.SetVisible(0)
  wStrengthBar.SetVisible(0)
  wLowBarFrame.SetVisible(0)
  wObjectsFrame.SetVisible(0)
  wLogFrame.SetVisible(0)


def LevelUpFlash():
	global wLifeBar


	if not wLifeBar.GetFlash():
		wLifeBar.SetFlash(22)
		Bladex.AddScheduledFunc (Bladex.GetTime() + 2.0,wLifeBar.SetFlash,(0,))

	PowDefWidgets.FlashWidgest()

def NewObjectAtInventory(objName):
	import Select

	wLogFrame.SetVisible(1)
	wObjectsFrame.SetVisible(0)
	Bladex.AddScheduledFunc (Bladex.GetTime() + 15.0, wLogFrame.SetVisible, (0,))

	wNewObjectText.SetText(Select.GetSelectionData(objName)[2])
	wNewObject.SetBOD(Bladex.GetEntity(objName).Kind)
	wLogFrame.RecalcLayout()

def CycleElements():
	wLogFrame.SetVisible(0)
	ObjectsControl.CycleElements()
