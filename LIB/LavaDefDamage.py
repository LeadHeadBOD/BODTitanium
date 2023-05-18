##///
##||| LAVADEFDAMAGE.PY TITANIUM
##||| Change list:
##||| * Added checks for touchfunc to stop damaging entities when playing offline and game is paused.
##\\\ 


############################################################################
#
#
#	def CreateLava(entity_name,x,y,z,texture="LAVA",zoom=0.1,self_light=1):
#		It creates a lava entity (with entity_name as name) in that given point (x,y,z)
#		If you want , you can change the texture name with the 5th parameter
#		6th: to change the zoom of the texture
#       7th (new!) Change the degree of self ilumination (0-1)
#
#	Please note that the "TextureName" and "Zoom" parameter of the lava entity
#	can be changed in real time. Also , the self_light. Nice for real time effects ;)
#
#	Also note that the default name for the texture used is "LAVA" (in UPPER case!)
#
############################################################################

import Bladex
import Reference
import Damage
import netgame
import GameStateAux
import ObjStore
import Actions
import AbreCam
import AuxFuncs
import CharStats


UNDEDICATED = not netgame.IsDedicated()

def TakeMe2Init(EntityName):
	#print "TakeMe2Init"
	me=Bladex.GetEntity(EntityName)
	me.LaunchAnmType("Rlx")
	pos=me.InitPos
	me.Position=pos[0],pos[1],pos[2]



class LAVA_AREA:
	entity_name=""
	zoom=0.1
	self_light=1.0
	texture_name="LAVA"
	particle_type="LargeFire"
	ObjId=""

	def __init__(self):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self

	#Internal - Relocated particle entity to follow the burning character
	def FuegoInLavaPlayer(self,obj_name, entity_damaged):

		#
		# Particle system
		#
		fuego=Bladex.GetEntity(obj_name)
		if not fuego:
			return
		else:
			if fuego.DeathTime<Bladex.GetTime():
				return


		char=Bladex.GetEntity(entity_damaged)
		l_ent=Bladex.GetEntity(self.entity_name)
		fuego.Position=char.Position[0], l_ent.Position[1], char.Position[2]
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, self.FuegoInLavaPlayer, (obj_name,entity_damaged))

		#
		# Sound effect
		#
		if UNDEDICATED:
			snd_name=self.entity_name+entity_damaged+"_snd"
			sound=Bladex.GetEntity(snd_name)
			if sound:
				sound.Position=fuego.Position
				print "checking if playing"
				if sound.Playing==0:
					sound.PlaySound(0)
			else:
				print "NO SOUND!! ERROR!!!!"

	def LaunchFireInLava(self,entity_name,entity_damaged):
		self.entity_name=entity_name
		char=Bladex.GetEntity(entity_damaged)
		l_ent=Bladex.GetEntity(entity_name)
		pos= char.Position

		fuego_name=entity_name+entity_damaged+"_prtcls"
		pfuego=Bladex.CreateEntity(fuego_name, "Entity Particle System D1", pos[0],l_ent.Position[1], pos[2])
		pfuego.ParticleType=self.particle_type
		pfuego.YGravity=0.0
		pfuego.Friction=0.05
		pfuego.PPS=128
		pfuego.Velocity=0.0, -1500.0, 0.0
		pfuego.RandomVelocity=25.0
		pfuego.Time2Live=16
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, self.FuegoInLavaPlayer, (fuego_name,entity_damaged))

		if UNDEDICATED:
			snd_name=entity_name+entity_damaged+"_snd"
			sound=Bladex.GetEntity(snd_name)
			if not sound:
				sound=Bladex.CreateEntity(snd_name, "Entity Sound", pos[0], pos[1], pos[2] )
				sound.SetSound("../../Sounds/muerte-acida.wav")
			else:
				sound.Position=pos
			sound.PlaySound(0)


	def SetLastCameraPosition(self,counter,cam):
		if counter >= 0:
			cam.Position =    cam.Position[0],cam.Position[1]-10,cam.Position[2]
			cam.TPos     =    cam.TPos[0],cam.TPos[1]-4,cam.TPos[2]
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.025,   self.SetLastCameraPosition,  (counter-0.025,cam))


	def LavaDefTouchFunc(self,entity_name,entity_damaged,factor):
		player=Bladex.GetEntity(entity_damaged)
		prevLife = player.Life
		AppMode=Bladex.GetAppMode()         # -LeadHead
		if player.Life>0:
			if player.Kind in Reference.LavaInmune:
				return
			if factor >= 1.0:
				player.Life=0
				if player.Name == "Player1":
					cam = Bladex.GetEntity("Camera")
					cam.SType    = 0
					cam.TType    = 0
					Lava = Bladex.GetEntity(entity_name)
					if Lava.Position[1] < cam.Position[1]:
						cam.Position = cam.Position[0], Lava.Position[1], cam.Position[2]
					AuxFuncs.FadeFrom(0.15,0.0,255,128,0)
					self.SetLastCameraPosition(5.0,cam)
			else:
				if netgame.GetNetState()==1:                                                                       # If playing online - proceed as usual.
					player.Life=player.Life-(factor+1.0)*0.0025*CharStats.GetCharMaxLife(player.Kind,player.Level) # 
				elif AppMode == "Menu":                                                                            # If not online and we have menu open - do nothing.
					return                                                                                         #
				else:                                                                                              # If not online and playing like a civilized person - hurt me plenty.
					player.Life=player.Life-(factor+1.0)*0.0025*CharStats.GetCharMaxLife(player.Kind,player.Level) #                    -LeadHead
		else:
			return

		if player.Life<=0 and player.AnimName<>"dth_burn":
			Actions.FireDeath(entity_damaged,self.particle_type,16)
			if netgame.GetNetState()==1: # Juego en red -> servidor
				Damage.PlayerHitFunc(player.Name,"Lava", player.Life, prevLife)


		my_fire=Bladex.GetEntity(entity_name+entity_damaged+"_prtcls")
		if not my_fire:
			self.LaunchFireInLava(entity_name,entity_damaged)
			my_fire=Bladex.GetEntity(entity_name+entity_damaged+"_prtcls")

		my_fire.DeathTime=Bladex.GetTime()+0.2



	def CreateLava(self,entity_name,x,y,z,texture="LAVA",zoom=0.1,slight=1,particle_type="LargeFire"):
		self.entity_name=entity_name
		self.texture_name=texture
		self.zoom=zoom
		self.sleft_light=slight
		self.particle_type=particle_type
		tmp_lava=Bladex.CreateEntity(entity_name,"Entity Lava",x,y,z)
		tmp_lava.TextureName=texture
		tmp_lava.Zoom=zoom
		tmp_lava.SelfLight=slight
		tmp_lava.TouchFluidFunc=self.LavaDefTouchFunc

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver c䮯 poder guardar el estado de la clase
		return (1,
				self.ObjId,
				self.entity_name,
				self.zoom,
				self.texture_name,
				self.self_light,
				self.particle_type,
				GameStateAux.SaveNewMembers(self)
				)

	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase

		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.entity_name=parm[2]
			self.zoom=parm[3]
			self.texture_name=parm[4]
			self.self_light=parm[5]
			self.particle_type=parm[6]
			GameStateAux.LoadNewMembers(self,parm[7])

			my_ent=Bladex.GetEntity(self.entity_name)

			if my_ent:
				my_ent.TextureName=self.texture_name
				my_ent.Zoom=self.zoom
				my_ent.SelfLight=self.self_light
				my_ent.TouchFluidFunc=self.LavaDefTouchFunc
##			if self.obj:
##				self.obj.Data=self
##			GameStateAux.LoadedPickledData[self.ObjId]=self
		else:
			print "DinObj.__setstate__() -> Version mismatch"
			# Valores de creaci䮠por si valen para algo.
			self.entity_name=""
			self.zoom=0.1
			self.texture_name="LAVA"
			self.particle_type="LargeFire"
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self
