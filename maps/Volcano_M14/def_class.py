##///
##||| VOLCANO_M14/def_class.PY TITANIUM
##||| Change list:
##||| * Gem animation is now 60fps rather than.
##\\\ 

import Bladex
import math
import B3DLib
import Actions
import AuxFuncs
import Scorer
import GotoMapVars


class Arania:
	
	def __init__(self,x,y,z,LlaveN):
		self.Pos = x,y,z
		self.LlaveNegra=LlaveN

	def MuevePata(self,e_name, time):
		for i in range(len(self.Patas)):
			self.DataPata[i][2] = self.DataPata[i][2]+self.DataPata[i][3]
			if   self.DataPata[i][2]> 10:
				self.DataPata[i][3] = -1
			elif self.DataPata[i][2]<-10:
				self.DataPata[i][3] = +1
			
			#################################################
			
			delta = self.DataPata[i][0]
			dy    = self.DataPata[i][1] + self.DataPata[i][2]*50
			
			p1=self.ppos
			p2=self.Pos
			x = p2[0]-p1[0]
			z = p2[2]-p1[2]
			angle = B3DLib.GetXZAngle(x,0,z)
				
			dx = math.sin(angle)*delta
			dz = math.cos(angle)*delta
	
			pata = self.Patas[i]
			pata.Velocity= dx*2,dy*2,dz*2
			pata.Position = self.Pos[0]-dx, self.Pos[1]-dy, self.Pos[2]-dz
	
	def CreatePata(self,delta,dy):
		
		p1=self.ppos
		p2=self.Pos
		x = p2[0]-p1[0]
		z = p2[2]-p1[2]
		angle = B3DLib.GetXZAngle(x,0,z)
			
		dx = math.sin(angle)*delta
		dz = math.cos(angle)*delta
		
	
		
		pata=Bladex.CreateEntity("Roja1", "Entity Particle System D1", self.Pos[0]-dx, self.Pos[1]-dy, self.Pos[2]-dz)
		pata.Time2Live=16
		pata.ParticleType="Roja1"
		pata.PPS=64
		pata.YGravity=0
		pata.Friction=0
		pata.Velocity= dx*2,dy*2,dz*2
		pata.RandomVelocity=0
	
		return pata

	def CreateLinea(self,Posi):
		
		self.Cuerpo=Bladex.CreateEntity("Cuerpo", "Entity Particle System D1", self.Pos[0], self.Pos[1], self.Pos[2])
		self.Cuerpo.Time2Live=32
		self.Cuerpo.ParticleType="Roja2"
		self.Cuerpo.PPS=64
		self.Cuerpo.YGravity=0
		self.Cuerpo.Friction=0
		self.Cuerpo.Velocity=0,0,0
		self.Cuerpo.RandomVelocity=-20
		self.Cuerpo.DeathTime=Bladex.GetTime()+1.5
		
		self.Cuerpo.Position = self.Pos
		self.Cuerpo.Velocity = ((self.Pos[0]-Posi[0]),
				        (self.Pos[1]-Posi[1]),
				        (self.Pos[2]-Posi[2]))
		
	def Crea(self,Posi):
		self.ppos = Bladex.GetEntity("Player1").Position
		
		self.CreateLinea(Posi)
		
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.5, self.Lanza, ())
		     
			
	def Lanza(self):
		self.Cuerpo=Bladex.CreateEntity("Cuerpo", "Entity Particle System D1", self.Pos[0], self.Pos[1], self.Pos[2])
		self.Cuerpo.Time2Live=32
		self.Cuerpo.ParticleType="Roja2"
		self.Cuerpo.PPS=64
		self.Cuerpo.YGravity=0
		self.Cuerpo.Friction=0
		self.Cuerpo.Velocity=0,0,0
		self.Cuerpo.RandomVelocity=-20
		
		self.Cabeza=Bladex.CreateEntity("Cuerpo", "Entity Particle System D1", self.Pos[0], self.Pos[1]-700, self.Pos[2])
		self.Cabeza.Time2Live=16
		self.Cabeza.ParticleType="Roja1"
		self.Cabeza.PPS=64
		self.Cabeza.YGravity=0
		self.Cabeza.Friction=0
		self.Cabeza.Velocity=0,0,0
		self.Cabeza.RandomVelocity=-15
		
		self.DataPata = ([-1800, -500,  0, 1],
			         [-1800,  500,-19,-1],
			         [ 1800, -500, 10, 1],
			         [ 1800,  500,-16, 1],
			         [-1300,-1200, -8,-1],
			         [-1300, 1200, 16, 1],
			         [ 1300,-1200, 12, 1],
			         [ 1300, 1200,  4,-1])
				 
		self.Patas = (self.CreatePata(-1800, -500),
			      self.CreatePata(-1800,  500),
			      self.CreatePata( 1800, -500),
			      self.CreatePata( 1800,  500),
			      self.CreatePata(-1300,-1200),
			      self.CreatePata(-1300, 1200),
			      self.CreatePata( 1300,-1200),
			      self.CreatePata( 1300, 1200))

		self.LlaveNegra.TimerFunc     = self.MuevePata
		self.LlaveNegra.SubscribeToList("Timer60")
	
	
	def LlaveTimer(self,e_name, time):
		self.Counter         = self.Counter + 1
		self.LlaveNegra.Rotate(1, 0, 0,0.06532)
		if self.Counter == 160:
			self.CreaLlaveFX(self.LlaveNegra)
		if self.Counter > 160:
			self.LlaveNegra.Position = self.LlaveNegra.Position[0]+self.Delta[0], self.LlaveNegra.Position[1]+self.Delta[1],self.LlaveNegra.Position[2]+self.Delta[2]
			if self.Counter >= 320:
				self.LlaveNegra.RemoveFromList("Timer60")
				Actions.TakeObject("Player1", self.LlaveNegra.Name)
				AuxFuncs.FadeTo(5.0, 50.0)
				Scorer.SetVisible(0)
				Bladex.DeactivateInput()
				
					
				Bladex.ExeMusicEvent(Bladex.GetMusicEvent("araniavolcan"))
				Bladex.AddScheduledFunc(Bladex.GetTime()+5.5,GotoMapVars.EndOfLevel,())
		else:
			self.LlaveNegra.Alpha = self.Counter/160.0
		
	def Borra(self):
		self.Cuerpo.DeathTime=Bladex.GetTime()+0.7
		self.ppos = Bladex.GetEntity("Player1").Position
		self.Cabeza.DeathTime=Bladex.GetTime()+0.7
		self.LlaveNegra.Position = self.Pos
		self.LlaveNegra.Orientation   = -0.7,0,  0, -0.7
		self.LlaveNegra.TimerFunc     = self.LlaveTimer
		self.Counter = 0
		char = Bladex.GetEntity("Player1")
		self.Delta = (char.Position[0]-self.Pos[0])/160,(char.Position[1]-self.Pos[1])/160,(char.Position[2]-self.Pos[2])/160
		self.SoundLlaveInn.Position = char.Position		
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,self.SoundLlaveInn.PlaySound,(0,))
		
		
		for i in self.Patas:
			i.DeathTime=Bladex.GetTime()
