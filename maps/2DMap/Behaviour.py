##///
##||| 2DMAP/BEHAVIOUR.PY TITANIUM
##||| Change list:
##||| * Shield rotation animation now plays at 60fps rather than 20fps
##\\\ 


import Bladex
import Scorer
import ScorerWidgets
import MenuText
import math
import Raster
import BUIx
import Gems
import GameText
import GotoMapVars
import lugares
import Language

CoolFlag = 1
thispos = 0,0,0
animFPS = 60      #Added -LeadHead

Gems.SetGemColor(Gems.RED_GEM)

Gems.MaximunAlpha =0.99

def EfectoCool():
	global thispos
	global CoolFlag
	Gems.EfectoConcentracion(	thispos,
								"achalay",
								80,#frames
								50.0,#scale
								60.0)

	if CoolFlag:
		Bladex.AddScheduledFunc(Bladex.GetTime() + 0.5,  EfectoCool,())

EfectoCool()

Frame = 0

font_server_behaviour=BUIx.B_FontServer()
font_behaviour=font_server_behaviour.CreateBFont(Language.LetrasMenuBig)


#------- LABEL SHOWING-------------
def LabelEntity(entity,text,dx,dy):
	if entity:
		Zcreen=Raster.GetSize()
		text_wh=(font_behaviour.GetTextWidth(text),font_behaviour.GetHeight("H"))
		# FIXME: Due to some reason this is not working, re-enalbel next line later.
		Raster.SetFont(font_behaviour.GetPointer())
		text_pos=Bladex.GetScreenXY(entity.Rel2AbsPoint(0.0,0.0,0.0))
		text_x=(text_pos[0] * Zcreen[0]) + (Zcreen[0]/2) - (text_wh[0] / 2.0 + dx)
		text_y=(text_pos[1] * Zcreen[0]) + (Zcreen[1]/2) - (text_wh[1] / 2.0 + dy)
		#Raster.SetTextColor(200,180,180) #Por poner uno cualquiera
		Raster.SetPosition(text_x,text_y)
		Raster.WriteText(text)

def ShowLabelEntity(Ent):
	Raster.SetTextAlpha(0.3)
	Raster.SetTextColor(255,255,255)
	LabelEntity(Ent, Ent.Name, 0, 0)

def ShowLabelEntity2(Ent):
	Raster.SetTextColor(255, 254, 125)
	Raster.SetTextAlpha(1)
	LabelEntity(Ent, Ent.Name, 0, 0)

vused = 0

def ContRot(Ent):                                                                      # Old rotation speed was 2 radians per second
	Ent.RotateRel(0,0,0,  0,0,1,  2.0/animFPS)                                         # at a framerate of 20FPS
	Bladex.AddScheduledFunc(Bladex.GetTime() + 1.0/animFPS,  ContRot,(Ent,))           # Rotation speed (almost) unchanged, but made it 60FPS -LeadHead

def SetShields():
	global GoodShield
	global BadShield
	global Cartelitos

	ca = 0
	for ThisGP in Cartelitos:
		if lugares.MapStatus[ca]:
			Bladex.GetEntity(BadShield[ca]).PutToWorld()
			ContRot(Bladex.GetEntity(BadShield[ca]))
		# Visible Good shields and Complete Blade Sword
		if GotoMapVars.VisitedMaps[ca]:
			Bladex.GetEntity(GoodShield[ca]).PutToWorld()
		ca = ca + 1

def NameWrittingFuct(time):

	global thispos
	global Cartelitos
	global Frame
	global CurrentSelected
	global GoodShield
	global BadShield
	global Tablillas
	global vused

	if not vused:
		SetShields()
		vused = 1

	a = 0
	for ThisGP in Cartelitos:
		if (lugares.MapStatus[a] or GotoMapVars.VisitedMaps[a]):
			# Visible Bad shields and Simple Blade Sword
			if (a == CurrentSelected):
				thispos = Bladex.GetEntity(ThisGP).Position
				ShowLabelEntity2(Bladex.GetEntity(Cartelitas[a]))
			else:
				ShowLabelEntity(Bladex.GetEntity(ThisGP))
		a = a + 1

	cam = Bladex.GetEntity("Camera")
	cam.ETarget = "Player1"
	cam.TType = 0
	cam.SType = 0

	if GotoMapVars.VisitedMaps[7]:
		# GRAND MAP-------------
		cam.TPos = (-23400,1,-5000)
		cam.Position = -23400,-116000,-5001
		#-----------------------
	else :
		# PPIO------------------
		cam.TPos = (-56100,1,-19500)
		cam.Position = -56100,-71455, -19501
		#-----------------------

Bladex.SetAfterFrameFunc("2dMap",NameWrittingFuct)
Bladex.GetEntity("Player1").SetOnFloor()

Scorer.SetVisible(0)

cam = Bladex.GetEntity("Camera")