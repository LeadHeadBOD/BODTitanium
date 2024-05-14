##///
##||| DEFAULTSELECTIONDATA.PY TITANIUM
##||| Change list:
##||| * Adjusted SelectionAfterFrameFunc() to have TrueEnergy
##||| 
##\\\ 

import Bladex
import Select
import Raster
import Actions
import Reference
import CharStats
import math
import netgame
import BUIx
import Language

Label_Opacity=1.0
Label_r=128
Label_g=128
Label_b=128

if netgame.GetNetState() != 2:
	Select.TurnOnAutoSelect("Player1")
	font_server_behaviour=BUIx.B_FontServer()
	font_behaviour=font_server_behaviour.CreateBFont(Language.LetrasMenuBig)
######ARMAS

execfile("../../Data/ObjIds/"+Language.Current+".py")



stime=-2.0

def SelectObject():
	global stime
	time=Bladex.GetTime()
	if(time-stime>0.2):
		pj=Bladex.GetEntity("Player1")
		if(pj.Data.selection_locked and time-stime<2.0):
			Select.SelectNext(pj)
		else:
			Select.AutoSelect(pj)
			if(pj.Data.selected_entity):
				pj.Data.selection_locked=1
		stime=time

def UnSelectObject():
	global stime
	stime=-2.0
	pj=Bladex.GetEntity("Player1")
	pj.Data.selection_locked=0



stime2=-2.0

def IntermediateSelect(EntityName):
	SelectEnemy()


def SelectEnemy(backward=0):
	global stime2
	time=Bladex.GetTime()
	if(time-stime2>0.1):
		pj=Bladex.GetEntity("Player1")
		if pj.InvRight=="" and pj.InvRightBack<>"" and Reference.GiveObjectFlag(pj.InvRightBack)<>Reference.OBJ_QUIVER:
			if pj.AnmEndedFunc==IntermediateSelect:
				pj.AnmEndedFunc= None
			Actions.StdToggleWeapons("Player1")
			pj.AnmEndedFunc=IntermediateSelect
			return
		if(pj.Data.enemy_locked):
			Select.SelectNextEnemy(pj, backward)
		else:
			Select.GetVisibleEnemies(pj)
			if(pj.Data.selected_enemy):
				pj.Data.enemy_locked=1
		stime2=time
		if pj.Data.selected_enemy:
			ene=Bladex.GetEntity(pj.Data.selected_enemy[0])
			if ene and ene.Person:
				pj.SetActiveEnemy(ene)

def SelectPreviousEnemy():
	pj=Bladex.GetEntity("Player1")
	if(pj.Data.enemy_locked): # :TRICKY: Forbid SelectPrevious if the player is not already locking on enemies.
		SelectEnemy(1)

def LabelEntity(entity_name,text,dx,dy):
	entity=Bladex.GetEntity(entity_name)
	if entity:
		screen=Bladex.GetScreenRect()
		text_wh=Bladex.GetTextWH(text)
		text_pos=Bladex.GetScreenXY(entity.Rel2AbsPoint(0.0,0.0,0.0))
		text_x=text_pos[0]-text_wh[0]/2.0+dx
		text_y=text_pos[1]-text_wh[1]/2.0+dy
		if(text_x<screen[0]):
			text_x=screen[0]
		if(text_x+text_wh[0]>screen[2]):
			text_x=screen[2]-text_wh[0]
		if(text_y<screen[1]):
			text_y=screen[1]
		if(text_y+text_wh[1]>screen[3]):
			text_y=screen[3]-text_wh[1]
		Raster.SetFont(font_behaviour.GetPointer())
		Bladex.WriteText(text_x,text_y,text)






def ShowLabelEntity(pj,time):
	global stime

	itime=time-stime
	if(itime<=0.5):
		Raster.SetTextColor(0,0,0)
		Raster.SetTextAlpha(Label_Opacity*2.0*itime)
		LabelEntity(pj.Data.selected_entity[0],pj.Data.selected_entity[1][2],1.0/640.0,1.0/640.0)
		Raster.SetTextColor(Label_r,Label_g,Label_b)
		LabelEntity(pj.Data.selected_entity[0],pj.Data.selected_entity[1][2],0,0)
	elif(itime<=1.0):
		Raster.SetTextColor(0,0,0)
		Raster.SetTextAlpha(Label_Opacity)
		LabelEntity(pj.Data.selected_entity[0],pj.Data.selected_entity[1][2],1.0/640.0,1.0/640.0)
		Raster.SetTextColor(Label_r,Label_g,Label_b)
		LabelEntity(pj.Data.selected_entity[0],pj.Data.selected_entity[1][2],0,0)
	elif(itime<2.0):
		Raster.SetTextColor(0,0,0)
		Raster.SetTextAlpha(Label_Opacity*(2.0-itime))
		LabelEntity(pj.Data.selected_entity[0],pj.Data.selected_entity[1][2],1.0/640.0,1.0/640.0)
		Raster.SetTextColor(Label_r,Label_g,Label_b)
		LabelEntity(pj.Data.selected_entity[0],pj.Data.selected_entity[1][2],0,0)

UseNewEnergyBar = 1

def SelectionAfterFrameFunc(time):
	import Scorer
	import PowDefWidgets

	if not Scorer.VISIBLE:
		return
	pj=Bladex.GetEntity("Player1")
	if pj is None:
		return

	if(pj.Data is not None):
		if (pj.Data.selected_entity and pj.Data.selection_locked):
			ShowLabelEntity(pj,time)
		Scorer.SetLifeValue(pj.Life,CharStats.GetCharMaxLife(pj.CharType,pj.Level),pj.Data.Poisoned)

	Scorer.SetLevelValue(pj.Level)
	Scorer.SetEnemiesData(pj)
	PowDefWidgets.Draw()

	throw_pressed = Bladex.GetTimeActionHeld ("Throw")
	if throw_pressed:
		Scorer.SetStrengthBarValue(Actions.ThrowTime2ThrowForce(throw_pressed))
		Scorer.wLowBarFrame.SetVisible(1)
	else:
		max_energy= CharStats.GetCharMaxEnergy(pj.Kind, pj.Level)
		if pj.Energy < max_energy:
			if UseNewEnergyBar:                                                             # Use new energy bar if option selected.
				Scorer.SetTrueEnergyBarValue(pj.Energy, max_energy, pj.Data.Energy2Lose)    #
			else:                                                                           #
				Scorer.SetEnergyBarValue(pj.Energy, max_energy)                             #           -LeadHead
			Scorer.wLowBarFrame.SetVisible(1)
		else:
			Scorer.wLowBarFrame.SetVisible(0)

if netgame.GetNetState() == 0:
	Bladex.SetAfterFrameFunc("DefaultSelectionData",SelectionAfterFrameFunc)

# The RestoreEnergyFunc is not here!
# See at Basic_Funcs.py

