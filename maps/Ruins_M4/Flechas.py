##///
##||| Ruins_M4/Flechas.PY TITANIUM
##||| Change list:
##||| * Arrows replaced by bolts
##\\\ 

import InitDataField
import Bladex
import Reference
import ItemTypes

class FlechaController(ItemTypes.PersistantItemType):
	Nombre="Unnamed"
	init_ori=(0.0,0.0,0.0,0.0)
	init_pos=(0.0,0.0,0.0)
	escala=1.0
	Pivote=None
	nflecha=0
	sonidopiv=None
	
	def __init__ (self, pivote, _sonidopiv):
		ItemTypes.PersistantItemType.__init__(self, pivote)
		self.Nombre= pivote.Name
		self.Pivote= pivote
		self.init_ori= self.Pivote.Orientation
		self.init_pos= self.Pivote.Position
		self.escala= self.Pivote.Scale
		self.nflecha= 0
		self.Pivote.StickFunc= self.NewPivote
		self.sonidopiv= _sonidopiv
	
	def NewPivote(self, hitting_ent=None, hit_ent=None):
		self.nflecha= self.nflecha+1
		self.Pivote= Bladex.CreateEntity(self.Nombre+`self.nflecha`, "Pivote", self.init_pos[0], self.init_pos[1], self.init_pos[2], "Arrow")
		#print "NewPivote: "+self.Pivote.Name
		self.Pivote.Orientation=self.init_ori
		self.Pivote.Scale=self.escala
		self.Pivote.SendSectorMsgs=0
		InitDataField.Initialise(self.Pivote)
		self.Pivote.Data.NoFXOnHit=1
		self.Pivote.StickFunc=self.NewPivote
	
	def __getstate__(self):
		state= ItemTypes.PersistantItemType.__getstate__(self)
		state[1]["FlechaController"]=(self.Nombre,
									self.init_ori,
									self.init_pos,
									self.escala,
									self.nflecha,
									self.sonidopiv,
									self.Pivote.Name
									)
		
		return state
	
	def __setstate__(self,parm):
		# Toma como parámetro lo que devuelve __getstate__() y debe recrear la clase
		ItemTypes.PersistantItemType.__setstate__(self,parm)
		if parm[0]==1:
			parms=parm[1]["FlechaController"]
			self.Nombre= parms[0]
			self.init_ori= parms[1]
			self.init_pos= parms[2]
			self.escala= parms[3]
			self.nflecha= parms[4]
			self.sonidopiv= parms[5]
			pivote_name= parms[6]
			self.Pivote= Bladex.GetEntity(pivote_name)
			
		else:
			self.Nombre= "Unnamed FlechaController"
			self.init_ori=(0.0,0.0,0.0,0.0)
			self.init_pos=(0.0,0.0,0.0)
			self.escala = 1.0
			self.Pivote= None
			self.nflecha= 0
			self.sonidopiv= None
		
		if self.Pivote:
			InitDataField.Initialise(self.Pivote)
			self.Pivote.Data.NoFXOnHit=1
			self.Pivote.StickFunc=self.NewPivote
		else:
			print "No Pivote found!!!!"
			self.NewPivote()
	
	def StopArrow (self, orientation, position):
		#Debug
		if self.Pivote.Parent:
			print "Sending arrow with parent"
			parent= Bladex.GetEntity(self.Pivote.Parent)
			if parent: parent.Unlink(self.Pivote)
		# End Debug
		
		self.Pivote.Stop()
		self.Pivote.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)
		self.Pivote.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)
		self.Pivote.Orientation= orientation[0], orientation[1], orientation[2], orientation[3]
		self.Pivote.Position= position[0], position[1], position[2]
	
	def StartArrow(self, position, velocity):
		self.Pivote.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)
		self.Pivote.MessageEvent(Reference.MESSAGE_START_TRAIL,0,0)
		self.Pivote.Fly(velocity[0], velocity[1], velocity[2])
		if self.sonidopiv:
			self.sonidopiv.Play(position[0], position[1], position[2], 0)
	
	def RestartArrow (self, orientation, position, velocity):
		self.StopArrow (orientation, position)
		self.StartArrow (position, velocity)
