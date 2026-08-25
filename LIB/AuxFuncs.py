##///
##||| AuxFuncs.PY TITANIUM
##||| Change list:
##||| * Add func GetDynamicFires()
##||| * Add func FadeAndScaleV2 - allows parallel funcs and runs at 60fps
##||| * 
##\\\ 


import Bladex
import BInput
import Raster
import math
import InitDataField
import B3DLib
import whrandom
import ScriptSkip
import darfuncs
import os
import Language
import BBLib
import time

FadeActive = 0

def Normalize(vector):
	return B3DLib.Normalize(vector)

def Scale(vector, scalar):	
	return B3DLib.Scale(vector,scalar)

def Module(vector):	
	return B3DLib.Modulo(vector[0], vector[1], vector[2])

def Pos2PosXZAngle(p1, p2):
	return B3DLib.Pos2PosXZAngle(p1[0], p1[1], p1[2], p2[0], p2[1], p2[2])

###############

def GetSpot(obj):
	n_child=obj.GetNChildren()
	for n in range(n_child):
		child=Bladex.GetEntity(obj.GetChild(n))
		if child.Kind=="Entity Spot":
			return child
#	print "El objeto "+obj.Name+" no tiene Spot"

def GetFire(obj):
	n_child=obj.GetNChildren()
	for n in range(n_child):
		child=Bladex.GetEntity(obj.GetChild(n))
		if child.Kind=="Entity Fire":
			return child
#	print "El objeto "+obj.Name+" no tiene Fire"

def GetDynamicFires(obj):
	fires = []
	n_child=obj.GetNChildren()
	for n in range(n_child):
		child=Bladex.GetEntity(obj.GetChild(n))
		if child.Kind=="Entity Dynamic Fire":
			fires.append(child)
	return fires

def SpotIntensityVariationGrad(light_name, time):
	light=Bladex.GetEntity(light_name)
	light.Intensity=light.Intensity+light.Data.AuxFuncsData.IntensityVar
	if light.Data.AuxFuncsData.SizeVar:
		light.SizeFactor=light.SizeFactor+light.Data.AuxFuncsData.SizeVar
	if ((light.Data.AuxFuncsData.IntensityVar>=0.0 and light.Intensity>=light.Data.AuxFuncsData.EndIntensity) or (light.Data.AuxFuncsData.IntensityVar<0.0 and light.Intensity<=light.Data.AuxFuncsData.EndIntensity)):
		if light.Data.AuxFuncsData.SizeVar:
			light.SizeFactor=light.Data.AuxFuncsData.EndSize
		light.Intensity=light.Data.AuxFuncsData.EndIntensity
		light.RemoveFromList(light.Data.AuxFuncsData.Timer)
		light.TimerFunc=""
		if light.Data.AuxFuncsData.DestroyOnEnd:
			light.SubscribeToList("Pin")

def SpotIntensityVariation(light_name, init_int, end_int, var_time, destroy=0, init_size=0.0, end_size=0.0, timer="Timer60", timespersec=60):
	light=Bladex.GetEntity(light_name)
	light.Intensity=init_int
	InitDataField.Initialise(light)
	light.Data.AuxFuncsData= ObjectAuxFuncsData()
	light.Data.AuxFuncsData.EndIntensity=end_int
	light.Data.AuxFuncsData.IntensityVar=(end_int-init_int)/(timespersec*var_time)
	light.Data.AuxFuncsData.DestroyOnEnd=destroy
	light.Data.AuxFuncsData.SizeVar=(end_size-init_size)/(timespersec*var_time)
	light.Data.AuxFuncsData.EndSize=end_size
	light.Data.AuxFuncsData.Timer=timer
	if (init_size or end_size):
		light.SizeFactor=init_size
	light.TimerFunc=SpotIntensityVariationGrad
	light.SubscribeToList(timer)



###############

def DeactivateKeyboard():
	#Flush current actions
	#Bladex.SetCallCheck(1)
	Bladex.DeactivateInput()
	Bladex.ActivateInput()
	InputManager=BInput.GetInputManager()
	InputManager.AddInputActionsSet("EmptySet")
	InputManager.SetInputActionsSet("EmptySet")

	Bladex.AddInputAction("Abort"  ,0)
	
	Bladex.AssocKey("Abort","Keyboard","Enter")
	Bladex.AssocKey("Abort","Keyboard","Esc")
	Bladex.AssocKey("Abort","Gamepad","ButtonStart")
	
	Bladex.AddBoundFunc("Abort"	,ScriptSkip.SkipCalled)

#	print "Desactivando teclado..."

def ActivateKeyboard():
	IManager = BInput.GetInputManager()
	IManager.SetInputActionsSet("EmptySet")
	IActions=IManager.GetInputActions()
	IAction = IActions.Find("Abort")
	if IAction.Name()!="NULL":
		IAction.RemoveAllEvents()
		print "Removed 'Abort'"
	
	InputManager=BInput.GetInputManager()
	InputManager.SetInputActionsSet("Default")
	
#	print "Activando teclado..."


###############

def StopCamTravelling(entity_name, camera_element, node):
	global EndFunc
	cam=Bladex.GetEntity("Camera")
	if node==1:
		cam.SType=0
		cam.TType=0
		cam.CameraClearPath(0)
		cam.CameraClearPath(1)
		if EndFunc:
			EndFunc()

def MoveCamFromTo(ox1, oy1, oz1, ox2, oy2, oz2, tx1, ty1, tz1, tx2, ty2, tz2, time, endfunc=""):
	global EndFunc
	EndFunc=endfunc
	cam=Bladex.GetEntity("Camera")
	#Path objetivo
	cam.AddCameraNode(0, time, ox1, oy1, oz1)
	cam.AddCameraNode(0, time/2.0, ox2, oy2, oz2)
	cam.AddCameraNode(0, time/2.0, (ox1+ox2)/2.0, (oy1+oy2)/2.0, (oz1+oz2)/2.0)
	#Path target
	cam.AddCameraNode(1, time, tx1, ty1, tz1)
	cam.AddCameraNode(1, time/2.0, tx2, ty2, tz2)
	cam.AddCameraNode(1, time/2.0, (tx1+tx2)/2.0, (ty1+ty2)/2.0, (tz1+tz2)/2.0)
	cam.SType=1
	cam.TType=1
	cam.CameraStartPath(0)
	cam.CameraStartPath(1)
	cam.ChangeNodeFunc=StopCamTravelling

def ResetScene(cut=1, persndsrc=1, actinput=1):
	cam=Bladex.GetEntity("Camera")
	cam.SetPersonView("Player1")
	if cut:
		cam.Cut()
	if persndsrc:
		Bladex.SetListenerPosition(1)
	if actinput:
		Bladex.ActivateInput()


##################


class ScreenFadeEffect:

	def __init__(self):
		self.FadeTime=1.0
		self.InitFadeTime=1.0
		self.EndFadeTime=1.0
		self.TotalFadeTime=2.0
		self.RColor=0
		self.GColor=0
		self.BColor=0
		self.InitAlpha=1.0
		self.EndAlpha=0.0
		self.AlphaVar=-1.0
		self.InitTime=Bladex.GetTime()
		self.ScreenSize=Raster.GetSize()

def Fade(time):
	global fade_effect
	global FadeActive
	if Bladex.GetAppMode()=="Menu":
		return

	pass_time=time-fade_effect.InitTime
	if pass_time<fade_effect.InitFadeTime:
		alpha=fade_effect.InitAlpha
	elif fade_effect.AlphaVar>0:
		alpha=min(fade_effect.EndAlpha, fade_effect.InitAlpha+(pass_time-fade_effect.InitFadeTime)*fade_effect.AlphaVar/fade_effect.FadeTime)
	else:
		alpha=max(fade_effect.EndAlpha, fade_effect.InitAlpha+(pass_time-fade_effect.InitFadeTime)*fade_effect.AlphaVar/fade_effect.FadeTime)
	Raster.SetFillColor(fade_effect.RColor, fade_effect.GColor, fade_effect.BColor)
	Raster.SetAlpha(alpha)
	Raster.SolidRectangle(0, 0, fade_effect.ScreenSize[0], fade_effect.ScreenSize[1])
	if pass_time>=fade_effect.TotalFadeTime:
		Bladex.RemoveAfterFrameFunc("Fade")
		FadeActive = 0

def FadeTo(fade_time=1.0, end_fade_time=1.0, rcolor=0, gcolor=0, bcolor=0):
	global fade_effect
	global FadeActive
	
	fade_effect=ScreenFadeEffect()
	fade_effect.FadeTime=fade_time
	fade_effect.InitFadeTime=0.0
	fade_effect.EndFadeTime=end_fade_time
	fade_effect.TotalFadeTime=fade_time+end_fade_time
	fade_effect.RColor=rcolor
	fade_effect.GColor=gcolor
	fade_effect.BColor=bcolor
	fade_effect.InitAlpha=0.0
	fade_effect.EndAlpha=1.0
	fade_effect.AlphaVar=1.0
	Bladex.SetAfterFrameFunc("Fade", Fade)
	FadeActive = 1

def FadeFrom(fade_time=1.0, init_fade_time=1.0, rcolor=0, gcolor=0, bcolor=0):
	global fade_effect
	global FadeActive

	fade_effect=ScreenFadeEffect()
	fade_effect.FadeTime=fade_time
	fade_effect.InitFadeTime=init_fade_time
	fade_effect.EndFadeTime=0.0
	fade_effect.TotalFadeTime=fade_time+init_fade_time
	fade_effect.RColor=rcolor
	fade_effect.GColor=gcolor
	fade_effect.BColor=bcolor
	fade_effect.InitAlpha=1.0
	fade_effect.EndAlpha=0.0
	fade_effect.AlphaVar=-1.0
	Bladex.SetAfterFrameFunc("Fade", Fade)
	FadeActive = 1

def FadeFromTo(init_alpha, end_alpha, fade_time=1.0, init_fade_time=1.0, end_fade_time=1.0, rcolor=0, gcolor=0, bcolor=0):
	global fade_effect
	global FadeActive

	fade_effect=ScreenFadeEffect()
	fade_effect.FadeTime=fade_time
	fade_effect.InitFadeTime=init_fade_time
	fade_effect.EndFadeTime=end_fade_time
	fade_effect.TotalFadeTime=fade_time+init_fade_time+end_fade_time
	fade_effect.RColor=rcolor
	fade_effect.GColor=gcolor
	fade_effect.BColor=bcolor
	fade_effect.InitAlpha=float(init_alpha)
	fade_effect.EndAlpha=float(end_alpha)
	fade_effect.AlphaVar=fade_effect.EndAlpha-fade_effect.InitAlpha
	Bladex.SetAfterFrameFunc("Fade", Fade)
	FadeActive = 1

class SingleFrameScreenFadeEffect:

	def __init__(self):
		self.RColor=0
		self.GColor=0
		self.BColor=0
		self.ScreenSize=Raster.GetSize()

def SingleFrameFadeFunc(time):
	global single_frame_fade_effect
	if Bladex.GetAppMode()=="Menu":
		return	
	Raster.SetFillColor(single_frame_fade_effect.RColor, single_frame_fade_effect.GColor, single_frame_fade_effect.BColor)
	Raster.SetAlpha(1.0)
	Raster.SolidRectangle(0, 0, single_frame_fade_effect.ScreenSize[0], single_frame_fade_effect.ScreenSize[1])
	Bladex.RemoveAfterFrameFunc("SingleFrameFadeFunc")

def SingleFrameFade(rcolor=0, gcolor=0, bcolor=0):
	global single_frame_fade_effect
	single_frame_fade_effect=SingleFrameScreenFadeEffect()
	single_frame_fade_effect.RColor=rcolor
	single_frame_fade_effect.GColor=gcolor
	single_frame_fade_effect.BColor=bcolor
	Bladex.SetAfterFrameFunc("SingleFrameFadeFunc", SingleFrameFadeFunc)


#####################

# Destroy Methods
DESTROY_METHOD_BIN= 1
DESTROY_METHOD_REMOVE= 2

class ObjectAuxFuncsData:
	InitAlpha= 0.0
	EndAlpha= 0.0
	AlphaVar= 0.0
	AlphaInitVel= 0.0
	AlphaAcc= 0.0
	CurrentAlpha= 1.0
	RVar= 0
	GVar= 0
	BVar= 0
	EndColor=(0,0,0)
	InitScale=1.0
	ScaleVar= 0.0
	EndScale= 1.0
	ScaleAcc=0.0
	ScaleInitVel= 0.0
	WhileSclFunc= None
	WhileSclArgs=()
	EndSclFunc= None
	EndSclArgs=()
	AngleVar= 0
	Axis= (0, 0, 1)
	SizeVar= 1.0
	EndSize= 1.0
	CurrentSize= 1.0
	IntensityVar= 0.0
	EndIntensity= 0.0
	Timer= "Timer30"
	InitTime= 0
	TotalTime= 0.0
	OnEndFunc= None
	OnEndArgs= ()
	DestroyOnEnd= 0


def FadeObjectGrad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	obj.Alpha=obj.Alpha+obj.Data.AuxFuncsData.AlphaVar
	if obj.Data.AuxFuncsData.AlphaVar>=0.0:
		if obj.Alpha>=obj.Data.AuxFuncsData.EndAlpha:
			obj.Alpha=obj.Data.AuxFuncsData.EndAlpha
			obj.RemoveFromList("Timer60")
			obj.TimerFunc=""
	else:
		if obj.Alpha<=obj.Data.AuxFuncsData.EndAlpha:
			obj.Alpha=obj.Data.AuxFuncsData.EndAlpha
			obj.RemoveFromList("Timer60")
			obj.TimerFunc=""
			if obj.Data.AuxFuncsData.DestroyOnEnd:
				if obj.Data.AuxFuncsData.DestroyOnEnd == DESTROY_METHOD_REMOVE:
					obj.RemoveFromWorld()
				if obj.Data.AuxFuncsData.DestroyOnEnd == DESTROY_METHOD_BIN:
					obj.SubscribeToList("Pin")

def FadeObject(obj_name, init_alpha, end_alpha, fade_time, destroy=0):
	obj=Bladex.GetEntity(obj_name)
	obj.Alpha=init_alpha
	InitDataField.Initialise(obj)
	obj.Data.AuxFuncsData= ObjectAuxFuncsData()
	obj.Data.AuxFuncsData.EndAlpha=end_alpha
	obj.Data.AuxFuncsData.AlphaVar=(end_alpha-init_alpha)/(60.0*fade_time)
	obj.Data.AuxFuncsData.DestroyOnEnd=destroy
	obj.TimerFunc=FadeObjectGrad
	obj.SubscribeToList("Timer60")

def ColorObjectGrad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	r,g,b= (obj.Color[0]+obj.Data.AuxFuncsData.RVar, obj.Color[1]+obj.Data.AuxFuncsData.GVar, obj.Color[2]+obj.Data.AuxFuncsData.BVar)
	if obj.Data.AuxFuncsData.RVar>=0.0:
		r= min(r,obj.Data.AuxFuncsData.EndColor[0])
	else:
		r= max(r,obj.Data.AuxFuncsData.EndColor[0])
	if obj.Data.AuxFuncsData.GVar>=0.0:
		g= min(g,obj.Data.AuxFuncsData.EndColor[1])
	else:
		g= max(g,obj.Data.AuxFuncsData.EndColor[1])
	if obj.Data.AuxFuncsData.BVar>=0.0:
		b= min(b,obj.Data.AuxFuncsData.EndColor[2])
	else:
		b= max(b,obj.Data.AuxFuncsData.EndColor[2])

	obj.Color= (r,g,b)
	if r==obj.Data.AuxFuncsData.EndColor[0] and g==obj.Data.AuxFuncsData.EndColor[1] and b==obj.Data.AuxFuncsData.EndColor[2]:
		obj.RemoveFromList("Timer60")
		obj.TimerFunc=""
		if obj.Data.AuxFuncsData.DestroyOnEnd:
			if obj.Data.AuxFuncsData.DestroyOnEnd & DESTROY_METHOD_REMOVE:
				obj.RemoveFromWorld()
			if obj.Data.AuxFuncsData.DestroyOnEnd & DESTROY_METHOD_BIN:				
				obj.SubscribeToList("Pin")


def ColorObject(obj_name, init_color, end_color, fade_time, destroy=0):
	obj=Bladex.GetEntity(obj_name)
	init_r= min(max(init_color[0],0),255) 
	init_g= min(max(init_color[1],0),255) 
	init_b= min(max(init_color[2],0),255)
	end_r= min(max(end_color[0],0),255) 
	end_g= min(max(end_color[1],0),255) 
	end_b= min(max(end_color[2],0),255)
	obj.Color= (init_r, init_g, init_b)
	InitDataField.Initialise(obj)
	obj.Data.AuxFuncsData= ObjectAuxFuncsData()
	obj.Data.AuxFuncsData.EndColor= (end_r, end_g, end_b)
	obj.Data.AuxFuncsData.RVar=(end_color[0]-init_color[0])/(60.0*fade_time)
	obj.Data.AuxFuncsData.GVar=(end_color[1]-init_color[1])/(60.0*fade_time)
	obj.Data.AuxFuncsData.BVar=(end_color[2]-init_color[2])/(60.0*fade_time)
	obj.Data.AuxFuncsData.DestroyOnEnd=destroy
	obj.TimerFunc=ColorObjectGrad
	obj.SubscribeToList("Timer60")


def ScaleObjectGrad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	obj.Scale=obj.Scale+obj.Data.AuxFuncsData.ScaleVar
	if obj.Data.AuxFuncsData.ScaleVar>=0.0:
		if obj.Scale>=obj.Data.AuxFuncsData.EndScale:
			obj.Scale=obj.Data.AuxFuncsData.EndScale
			obj.RemoveFromList("Timer60")
			obj.TimerFunc=""
	else:
		if obj.Scale<=obj.Data.AuxFuncsData.EndScale:
			obj.Scale=obj.Data.AuxFuncsData.EndScale
			obj.RemoveFromList("Timer60")
			obj.TimerFunc=""

def ScaleObject(obj_name, init_scale, end_scale, scale_time):
	obj=Bladex.GetEntity(obj_name)
	obj.Scale=init_scale
	InitDataField.Initialise(obj)
	obj.Data.AuxFuncsData= ObjectAuxFuncsData()
	obj.Data.AuxFuncsData.EndScale=end_scale
	obj.Data.AuxFuncsData.ScaleVar=(end_scale-init_scale)/(60.0*scale_time)
	obj.TimerFunc=ScaleObjectGrad
	obj.SubscribeToList("Timer60")


def GlowSizeVariationGrad(light_name, time):
	light=Bladex.GetEntity(light_name)
	light.SizeFactor=light.SizeFactor+light.Data.AuxFuncsData.SizeVar
	if ((light.Data.AuxFuncsData.SizeVar>=0.0) and (light.SizeFactor>=light.Data.AuxFuncsData.EndSize)) or ((light.Data.AuxFuncsData.SizeVar<0.0) and (light.SizeFactor<=light.Data.AuxFuncsData.EndSize)):
		light.SizeFactor=light.Data.AuxFuncsData.EndSize
		light.RemoveFromList("Timer30")
		light.TimerFunc=""
		if light.Data.AuxFuncsData.DestroyOnEnd:
			light.SubscribeToList("Pin")

def GlowSizeVariation(light_name, init_size, end_size, var_time, destroy=0):
	light=Bladex.GetEntity(light_name)
	light.SizeFactor=init_size
	InitDataField.Initialise(light)
	light.Data.AuxFuncsData= ObjectAuxFuncsData()
	light.Data.AuxFuncsData.EndSize=end_size
	light.Data.AuxFuncsData.SizeVar=(end_size-init_size)/(30.0*var_time)
	light.Data.AuxFuncsData.DestroyOnEnd=destroy
	light.TimerFunc=GlowSizeVariationGrad
	light.SubscribeToList("Timer30")


def FadeAndScaleAuraGrad(ent_name, time):
	aura=Bladex.GetEntity(ent_name)
	aura.Data.AuxFuncsData.CurrentSize=aura.Data.AuxFuncsData.CurrentSize+aura.Data.AuxFuncsData.SizeVar
	aura.Data.AuxFuncsData.CurrentAlpha=aura.Data.AuxFuncsData.CurrentAlpha+aura.Data.AuxFuncsData.AlphaVar
	if aura.Data.AuxFuncsData.CurrentAlpha<0.0:
		aura.Data.AuxFuncsData.CurrentAlpha=0.0
	elif aura.Data.AuxFuncsData.CurrentAlpha>1.0:
		aura.Data.AuxFuncsData.CurrentAlpha=1.0
	aura.SetAuraParams(aura.Data.AuxFuncsData.CurrentSize, aura.Data.AuxFuncsData.CurrentAlpha, 1, 0, 0, 1)
	if ((aura.Data.AuxFuncsData.SizeVar>0 and aura.Data.AuxFuncsData.CurrentSize>=aura.Data.AuxFuncsData.EndSize) or (aura.Data.AuxFuncsData.SizeVar<0 and aura.Data.AuxFuncsData.CurrentSize<=aura.Data.AuxFuncsData.EndSize)):
		aura.RemoveFromList(aura.Data.AuxFuncsData.Timer)
		aura.TimerFunc=""
		if aura.Data.AuxFuncsData.DestroyOnEnd:
			aura.SubscribeToList("Pin")
		else:
			aura.SetAuraParams(aura.Data.AuxFuncsData.EndSize, aura.Data.AuxFuncsData.EndAlpha, 1, 0, 0, 1)
		if aura.Data.AuxFuncsData.OnEndFunc:
			apply(aura.Data.AuxFuncsData.OnEndFunc, aura.Data.AuxFuncsData.OnEndArgs)

def FadeAndScaleAura(aura_name, init_size, end_size, init_alpha, end_alpha, time, destroy=0, OnEndFunc="", OnEndArgs=(), timer="Timer30", timespersec=30):
	aura=Bladex.GetEntity(aura_name)
	InitDataField.Initialise(aura)
	aura.Data.AuxFuncsData= ObjectAuxFuncsData()
	aura.Data.AuxFuncsData.CurrentSize=init_size
	aura.Data.AuxFuncsData.EndSize=end_size
	aura.Data.AuxFuncsData.SizeVar=(end_size-init_size)/(time*timespersec)
	aura.Data.AuxFuncsData.CurrentAlpha=init_alpha
	aura.Data.AuxFuncsData.EndAlpha=end_alpha
	aura.Data.AuxFuncsData.AlphaVar=(end_alpha-init_alpha)/(time*timespersec)
	aura.Data.AuxFuncsData.DestroyOnEnd=destroy
	aura.Data.AuxFuncsData.OnEndFunc=OnEndFunc
	aura.Data.AuxFuncsData.OnEndArgs=OnEndArgs
	aura.Data.AuxFuncsData.Timer=timer
	aura.TimerFunc=FadeAndScaleAuraGrad
	aura.SubscribeToList(timer)


def FadeAndScaleGrad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	curr_time=Bladex.GetTime()-obj.Data.AuxFuncsData.InitTime
	obj.Alpha=obj.Data.AuxFuncsData.InitAlpha+obj.Data.AuxFuncsData.AlphaInitVel*curr_time+0.5*obj.Data.AuxFuncsData.AlphaAcc*curr_time**2
	obj.Scale=obj.Data.AuxFuncsData.InitScale+obj.Data.AuxFuncsData.ScaleInitVel*curr_time+0.5*obj.Data.AuxFuncsData.ScaleAcc*curr_time**2
	if obj.Data.AuxFuncsData.AngleVar:
		x, y, z=obj.Data.AuxFuncsData.Axis
		ang=whrandom.uniform(-obj.Data.AuxFuncsData.AngleVar, obj.Data.AuxFuncsData.AngleVar)
		obj.RotateRel(0, 0, 0, x, y, z, ang)
	if curr_time>=obj.Data.AuxFuncsData.TotalTime:
		obj.Alpha=obj.Data.AuxFuncsData.EndAlpha
		obj.Scale=obj.Data.AuxFuncsData.EndScale
		obj.RemoveFromList("Timer30")
		obj.TimerFunc=""
		if obj.Data.AuxFuncsData.DestroyOnEnd==DESTROY_METHOD_BIN:
			obj.SubscribeToList("Pin")
		elif obj.Data.AuxFuncsData.DestroyOnEnd==DESTROY_METHOD_REMOVE:
			obj.RemoveFromWorld()

def FadeAndScale(obj_name, pos, init_alpha, end_alpha, alpha_acc, init_scl, end_scl, scl_acc, time, ang_var=0, destroy=0, axis=(0, 0, 1)):
	print "~~~WARNING~~~ starting old FadeAndScale"
	obj=Bladex.GetEntity(obj_name)
	obj.Alpha=init_alpha
	obj.Scale=init_scl
	obj.Position=pos
	InitDataField.Initialise(obj)
	obj.Data.AuxFuncsData= ObjectAuxFuncsData()
	obj.Data.AuxFuncsData.InitAlpha=init_alpha
	obj.Data.AuxFuncsData.EndAlpha=end_alpha
	obj.Data.AuxFuncsData.AlphaAcc=alpha_acc*2.0*(end_alpha-init_alpha)/time**2
	obj.Data.AuxFuncsData.AlphaInitVel=(end_alpha-init_alpha-alpha_acc*(end_alpha-init_alpha))/time
	obj.Data.AuxFuncsData.InitScale=init_scl
	obj.Data.AuxFuncsData.EndScale=end_scl
	obj.Data.AuxFuncsData.ScaleAcc=scl_acc*2.0*(end_scl-init_scl)/time**2
	obj.Data.AuxFuncsData.ScaleInitVel=(end_scl-init_scl-scl_acc*(end_scl-init_scl))/time
	obj.Data.AuxFuncsData.AngleVar=ang_var
	obj.Data.AuxFuncsData.Axis=axis
	obj.Data.AuxFuncsData.DestroyOnEnd=destroy
	obj.Data.AuxFuncsData.InitTime=Bladex.GetTime()
	obj.Data.AuxFuncsData.TotalTime=time
	obj.TimerFunc=FadeAndScaleGrad
	obj.SubscribeToList("Timer30")


### Titanium func - supports parallel funcs and runs at 60fps ###
def FadeAndScaleV2(obj_name, pos, init_alpha, end_alpha, alpha_acc, init_scl, end_scl, scl_acc, time, ang_var=0, destroy=0, axis=(0, 0, 1), WhileSclFunc="", WhileSclArgs=(), EndSclFunc="", EndSclArgs=()):
	print "starting FadeAndScale V2"
	obj=Bladex.GetEntity(obj_name)
	obj.Alpha=init_alpha
	obj.Scale=init_scl
	obj.Position=pos
	InitDataField.Initialise(obj)
	obj.Data.AuxFuncsData= ObjectAuxFuncsData()
	obj.Data.AuxFuncsData.InitAlpha=init_alpha
	obj.Data.AuxFuncsData.EndAlpha=end_alpha
	obj.Data.AuxFuncsData.AlphaAcc=alpha_acc*2.0*(end_alpha-init_alpha)/time**2
	obj.Data.AuxFuncsData.AlphaInitVel=(end_alpha-init_alpha-alpha_acc*(end_alpha-init_alpha))/time
	obj.Data.AuxFuncsData.InitScale=init_scl
	obj.Data.AuxFuncsData.EndScale=end_scl
	obj.Data.AuxFuncsData.ScaleAcc=scl_acc*2.0*(end_scl-init_scl)/time**2
	obj.Data.AuxFuncsData.ScaleInitVel=(end_scl-init_scl-scl_acc*(end_scl-init_scl))/time
	obj.Data.AuxFuncsData.AngleVar=ang_var
	obj.Data.AuxFuncsData.Axis=axis
	obj.Data.AuxFuncsData.WhileSclFunc=WhileSclFunc
	obj.Data.AuxFuncsData.WhileSclArgs=WhileSclArgs
	obj.Data.AuxFuncsData.EndSclFunc=EndSclFunc
	obj.Data.AuxFuncsData.EndSclArgs=EndSclArgs
	obj.Data.AuxFuncsData.DestroyOnEnd=destroy
	obj.Data.AuxFuncsData.InitTime=Bladex.GetTime()
	obj.Data.AuxFuncsData.TotalTime=time
	obj.TimerFunc=FadeAndScaleGradV2
	obj.SubscribeToList("Timer60")


def FadeAndScaleGradV2(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	curr_time=Bladex.GetTime()-obj.Data.AuxFuncsData.InitTime
	obj.Alpha=obj.Data.AuxFuncsData.InitAlpha+obj.Data.AuxFuncsData.AlphaInitVel*curr_time+0.5*obj.Data.AuxFuncsData.AlphaAcc*curr_time**2
	obj.Scale=obj.Data.AuxFuncsData.InitScale+obj.Data.AuxFuncsData.ScaleInitVel*curr_time+0.5*obj.Data.AuxFuncsData.ScaleAcc*curr_time**2
	if obj.Data.AuxFuncsData.WhileSclFunc:
		apply(obj.Data.AuxFuncsData.WhileSclFunc, obj.Data.AuxFuncsData.WhileSclArgs)
	if obj.Data.AuxFuncsData.AngleVar:
		x, y, z=obj.Data.AuxFuncsData.Axis
		ang=whrandom.uniform(-obj.Data.AuxFuncsData.AngleVar, obj.Data.AuxFuncsData.AngleVar)
		obj.RotateRel(0, 0, 0, x, y, z, ang)
	if curr_time>=obj.Data.AuxFuncsData.TotalTime:
		obj.Alpha=obj.Data.AuxFuncsData.EndAlpha
		obj.Scale=obj.Data.AuxFuncsData.EndScale
		obj.RemoveFromList("Timer60")
		obj.TimerFunc=""
		if obj.Data.AuxFuncsData.EndSclFunc:
			apply(obj.Data.AuxFuncsData.EndSclFunc, obj.Data.AuxFuncsData.EndSclArgs)
		if obj.Data.AuxFuncsData.DestroyOnEnd==DESTROY_METHOD_BIN:
			obj.SubscribeToList("Pin")
		elif obj.Data.AuxFuncsData.DestroyOnEnd==DESTROY_METHOD_REMOVE:
			obj.RemoveFromWorld()
### TiFunc end ###

def ScaleObjectV2Grad(obj_name, time):
	obj=Bladex.GetEntity(obj_name)
	curr_time=Bladex.GetTime()-obj.Data.AuxFuncsData.InitTime
	obj.Scale=obj.Data.AuxFuncsData.InitScale+obj.Data.AuxFuncsData.ScaleInitVel*curr_time+0.5*obj.Data.AuxFuncsData.ScaleAcc*curr_time**2
	if obj.Data.AuxFuncsData.WhileSclFunc:
		apply(obj.Data.AuxFuncsData.WhileSclFunc, obj.Data.AuxFuncsData.WhileSclArgs)
	if curr_time>=obj.Data.AuxFuncsData.TotalTime:
		obj.Scale=obj.Data.AuxFuncsData.EndScale
		obj.RemoveFromList("Timer30")
		obj.TimerFunc=""
		if obj.Data.AuxFuncsData.EndSclFunc:
			apply(obj.Data.AuxFuncsData.EndSclFunc, obj.Data.AuxFuncsData.EndSclArgs)
		if obj.Data.AuxFuncsData.DestroyOnEnd==DESTROY_METHOD_BIN:
			obj.SubscribeToList("Pin")
		elif obj.Data.AuxFuncsData.DestroyOnEnd==DESTROY_METHOD_REMOVE:
			obj.RemoveFromWorld()

def ScaleObjectV2(obj_name, init_scl, end_scl, scl_acc, time, WhileSclFunc="", WhileSclArgs=(), EndSclFunc="", EndSclArgs=(), destroy=0):
	obj=Bladex.GetEntity(obj_name)
	obj.Scale=init_scl
	InitDataField.Initialise(obj)
	obj.Data.AuxFuncsData= ObjectAuxFuncsData()
	obj.Data.AuxFuncsData.InitScale=init_scl
	obj.Data.AuxFuncsData.EndScale=end_scl
	obj.Data.AuxFuncsData.ScaleAcc=scl_acc*2.0*(end_scl-init_scl)/time**2
	obj.Data.AuxFuncsData.ScaleInitVel=(end_scl-init_scl-scl_acc*(end_scl-init_scl))/time
	obj.Data.AuxFuncsData.WhileSclFunc=WhileSclFunc
	obj.Data.AuxFuncsData.WhileSclArgs=WhileSclArgs
	obj.Data.AuxFuncsData.EndSclFunc=EndSclFunc
	obj.Data.AuxFuncsData.EndSclArgs=EndSclArgs
	obj.Data.AuxFuncsData.DestroyOnEnd=destroy
	obj.Data.AuxFuncsData.InitTime=Bladex.GetTime()
	obj.Data.AuxFuncsData.TotalTime=time
	obj.TimerFunc=ScaleObjectV2Grad
	obj.SubscribeToList("Timer30")





#########################################
###     Objetos estaticos que queman
#########################################


def SetRadialFireDamageObject(object_name, radius=500.0, floor_displ=1000.0, roof_displ=2000.0):
	x, y, z = Bladex.GetEntity(object_name).Position
	dx=radius/2.0
	dz=radius*((math.sqrt(3.0))/2.0)
	trsector_name=object_name+"_TrSectorFire"
	Bladex.AddTriggerSector(trsector_name, "SectoresTriggerFuego", y+floor_displ, y-roof_displ, [(x+dx, z+dz), (x-dx, z+dz), (x-radius, z), (x-dx, z-dz), (x+dx, z-dz), (x+radius, z)])
	darfuncs.FireOnGS(trsector_name)

#########################################


def setDemoBg(offsetTime):
	path = "../../Data/Demo/"+ Language.Current + "/"
	if not os.path.exists(path + "DEMO-SCREEN.jpg"):
		path = "../../Data/Demo/EnglishUS/"
	Bladex.AddScheduledFunc(Bladex.GetTime()+offsetTime,setBackgroundImage,(path + "DEMO-SCREEN.jpg",))
	Bladex.AddScheduledFunc(Bladex.GetTime()+offsetTime,Bladex.LoadLevel,("Casa",))

	

def setBackgroundImage(path):
	bitmap = BBLib.B_BitMap24()
	bitmap.ReadFromFile(path)
	data = bitmap.GetData()
	w,h = bitmap.GetDimension()
	Raster.SetBackgroundImage(w,h,"RGB","Normal","Stretch",data)
	Raster.Cls(0,0,0)
	Raster.SwapBuffers()
	Raster.SwapBuffers()

	time.sleep(7)
