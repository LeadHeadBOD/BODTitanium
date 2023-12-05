##///
##||| BUTTON.PY TITANIUM
##||| Change list:
##||| * Addressed an engine quirk - 2 sounds with the same internal name cannot be played simaltenously
##|||   as such every button now gets its internal name appended with the buttons objId
##\\\ 

import Bladex
import Actions
import ObjStore
import GameStateAux

class ButtonCombination:

	ObjId=""
	activates = 0
	corrects = 0
	n_buttons = 0
	correct_func = None
	failed_func = None
	order = 0
	state = 0
	combi = 0
	first_button = 0
	last_button = 0
	Cycle       = -1




	def __init__(self,correct_func,failed_func):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		self.correct_func = correct_func
		self.failed_func = failed_func
		ObjStore.ObjectsStore[self.ObjId]=self

	def AddButton(self,button_name,time,dir,dist,order,state,correct_state):
		button = CreateButton(button_name,time,dir,dist,order,state,correct_state,self)

		if (self.first_button):
			last_button = Bladex.GetEntity(self.last_button).Data
			last_button.next_button = button_name
		else:
			self.first_button = button_name

		self.last_button = button_name
		return button

	def Reset(self,type,entity = "Player1"):
		button = Bladex.GetEntity(self.first_button).Data
		char = Bladex.GetEntity(entity)

		#if (self.state <> 0):
		#	self.activates =

		for i in range(self.n_buttons):
			button_e = Bladex.GetEntity(button.entity)
			char.Data.obj_used = button_e

			if (self.state == 0):
				if (type):
					ActivateButton(entity,0)
				else:
					button.state = 0
			else:
				if (type):
					if(button.state <> button.initial_state):
						ActivateButton(enmtity,0)
				else:
					if(button.state <> button.initial_state):
						button.state = button.initial_state

			button = Bladex.GetEntity(button.next_button).Data

		if (self.state == 0):
			self.activates = 0
			self.corrects = 0

	def __setstate__(self,parm):
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self

			self.activates=parm[2]
			self.corrects=parm[3]
			self.n_buttons=parm[4]
			GameStateAux.LoadFunctionAux(parm[5],self,"correct_func")
			GameStateAux.LoadFunctionAux(parm[6],self,"failed_func")
			self.order=parm[7]
			self.state=parm[8]
			self.combi=parm[9]
			self.first_button=parm[10]
			self.last_button=parm[11]
			self.Cycle=parm[12]

		else:
			print "ButtonCombination.__setstate__() -> Version mismatch"
			# Valores por si valen para algo.
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self

	def __getstate__(self):
			return (1,
					self.ObjId,
					self.activates,
					self.corrects,
					self.n_buttons,
					GameStateAux.SaveFunctionAux(self.correct_func),
					GameStateAux.SaveFunctionAux(self.failed_func),
					self.order,
					self.state,
					self.combi,
					self.first_button,
					self.last_button,
					self.Cycle
					)

	def persistent_id(self):
		return self.ObjId


def CreateButtonCombination(type=0,correct_func="",failed_func=""):
	combi = ButtonCombination(correct_func,failed_func)

	if (type == 1):
		combi.order = 1

	if (type == 2):
		combi.state = 1

	return combi


class BUTTON:

	ObjId=""
	time=0
	last_time = 0
	finish_time = 0
	state = 0
	correct_state = 1
	v = [0,0,0]
	dir = [0,0,0]
	order = 0
	position_i = [0,0,0]
	position_f = [0,0,0]
	entity = 0
	sound=None
	combi=None

	def __init__(self):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		self.sound = Bladex.CreateSound('../../Sounds/block-sliding.wav', 'Sound Button'+self.ObjId)
		self.sound.Volume=1.0
		self.sound.MinDistance=7000
		self.sound.MaxDistance=20000
		self.next_button = 0
		self.position_i = [0,0,0]
		self.position_f = [0,0,0]
		self.v = [0,0,0]
		self.dir = [0,0,0]
		self.combi=None


		ObjStore.ObjectsStore[self.ObjId]=self

	def __getstate__(self):
		sound_name = ""
		if self.sound <> None:
			sound_name = self.sound.Name

		# Tiene que devolver c䮯 poder guardar el estado de la clase
		return (1,
				self.ObjId,
				self.last_time,
				self.finish_time,
				self.state,
				self.correct_state,
				self.v,
				self.dir,
				self.order,
				self.position_i,
				self.position_f,
				self.entity,
				sound_name,
				self.next_button,
				self.combi,
				self.time
				)


	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
##			GameStateAux.PersistentObject.__setstate__(self,parm)
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.last_time=parm[2]
			self.finish_time=parm[3]
			self.state=parm[4]
			self.correct_state=parm[5]
			self.v=parm[6]
			self.dir=parm[7]
			self.order=parm[8]
			self.position_i=parm[9]
			self.position_f=parm[10]
			self.entity=parm[11]
			sound_Name=parm[12]
			self.sound=Bladex.GetSound(sound_Name)
			self.next_button=parm[13]
			self.combi=parm[14]
			self.time=parm[15]
		else:
			print "Door.__setstate__() -> Version mismatch"
			# Valores por si valen para algo.
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self
			self.sound = Bladex.CreateSound('../../Sounds/block-sliding.wav', 'Sound Button'+self.ObjId)
			self.sound.Volume=1.0
			self.sound.MinDistance=7000
			self.sound.MaxDistance=20000
			self.next_button = 0
			self.combi=None
			self.time=0


	def persistent_id(self):
		return self.ObjId


def MoveButton(button_name,time):
	button_e = Bladex.GetEntity(button_name)
	button = button_e.Data

	timer = Bladex.GetTime()

	itime = timer - button.last_time

	if (timer < button.finish_time):
		x = button_e.Position[0] + itime * button.v[0]
		y = button_e.Position[1] + itime * button.v[1]
		z = button_e.Position[2] + itime * button.v[2]

		button_e.Position = (x,y,z)
	else:
		if (button.state):
			#button_e.Position = button.position_f
			x = button.position_f[0]
			y = button.position_f[1]
			z = button.position_f[2]

			button_e.Position = (x,y,z)

		else:
			button_e.Position = button.position_i

		button_e.RemoveFromList("TimerButton")
		button.sound.Stop()

	button.last_time = timer

def ActivateButton(entity,event):
	Char = Bladex.GetEntity(entity)

	button_e = Char.Data.obj_used
	button = button_e.Data
	combi = button.combi

	Bladex.CreateTimer("TimerButton",1.0/60.0)
	button_e.SubscribeToList("TimerButton")

	button.sound.Play(button_e.Position[0],button_e.Position[1],button_e.Position[2],combi.Cycle)

	if (button.state):
		button.state = 0
	else:
		button.state = 1

	button.v[0] = button.v[0] * -1
	button.v[1] = button.v[1] * -1
	button.v[2] = button.v[2] * -1

	combi.activates = combi.activates + 1

	print "Buttons Activados ",combi.activates

	if (combi.order and button.order == combi.activates):
		combi.corrects = combi.corrects + 1
	elif (combi.state):
		if (button.correct_state == button.state):
			combi.corrects = combi.corrects + 1
		else:
			combi.corrects = combi.corrects - 1
		combi.activates = combi.corrects

	if (combi.activates == combi.n_buttons):
		if (combi.order or combi.state):
			if (combi.corrects == combi.n_buttons and combi.correct_func):
				apply(combi.correct_func,())
			elif (combi.failed_func):
				apply(combi.failed_func,())
		elif (combi.correct_func):
			apply(combi.correct_func,())

	time = Bladex.GetTime()
	button.last_time = time
	button.finish_time = time + button.time

	Char.DelAnmEventFunc("Activate")
	Char.Data.obj_used = None


def UseButton(button_name,type):
	button_e = Bladex.GetEntity(button_name)
	button = button_e.Data;

	if button.state == 0 or button.combi.state:
		Char = Bladex.GetEntity("Player1")
		Actions.QuickTurnToFaceEntity ("Player1",button_name)
		Char.LaunchAnmType("pulsador")
		#Char.LaunchAnimation("Kgt_pulsador")
		Char.Data.obj_used = button_e
		Char.AddAnmEventFunc("Activate",ActivateButton)

def Turn(name):
	button_e = Bladex.GetEntity(name)
	button = button_e.Data;

	if button.state == 0 or button.combi.state:
		Char = Bladex.GetEntity("Player1")
		Char.Data.obj_used = button_e
		apply(ActivateButton,("Player1","Activate"))

def HitFunc(stick,sticker,x,y,z,xc,yc,zc,wcx,wcy,wcz,wdx,wdy,wdz):
	button_e = Bladex.GetEntity(stick)
	button = button_e.Data;
	if button.state == 0 or button.combi.state:
		Char = Bladex.GetEntity("Player1")
		Char.Data.obj_used = button_e
		apply(ActivateButton,("Player1","Activate"))

def StickArrow(sticker,stick):
	button_e = Bladex.GetEntity(stick)
	button = button_e.Data;
	if button.state == 0 or button.combi.state:
		Char = Bladex.GetEntity("Player1")
		Char.Data.obj_used = button_e
		apply(ActivateButton,("Player1","Activate"))

def CreateButton(button_name,time,dir,dist,order,state,correct_state,combi):
	button = BUTTON()
	button_e = Bladex.GetEntity(button_name)
	button_e.Static = 0
	button_e.Data = button
	button_e.UseFunc = UseButton
	button_e.TimerFunc = MoveButton
	button_e.StickFunc = StickArrow
	button_e.HitFunc = HitFunc
	button.entity = button_name

	button.position_i = button_e.Position
	button.position_f[0] = button_e.Position[0] + dist * dir[0]
	button.position_f[1] = button_e.Position[1] + dist * dir[1]
	button.position_f[2] = button_e.Position[2] + dist * dir[2]

	button.combi = combi

	a = dist / time

	if (combi.state and correct_state == state):
		combi.corrects = combi.corrects + 1
		combi.activates = combi.activates + 1

	if (state):
		button_e.Position = button.position_f
		button.v[0] = a * dir[0]
		button.v[1] = a * dir[1]
		button.v[2] = a * dir[2]
	else:
		button.v[0] = a * dir[0] * -1
		button.v[1] = a * dir[1] * -1
		button.v[2] = a * dir[2] * -1

	button.order = order
	button.time = time
	button.state = state
	button.initial_state = state
	button.correct_state = correct_state

	combi.n_buttons = combi.n_buttons + 1

	return button
