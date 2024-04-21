##///
##||| RAGNAR_M2/DEF_CLASS.PY TITANIUM
##||| Change list:
##||| * Pendulum trap should now be at 60fps
##\\\ 

import Bladex
import EnemyTypes
import Enm_Def
import Reference
import AniSound
import Sounds
import Combat
import copy
import Actions
import GameStateAux
import Language



TRUE = 1
FALSE = 0

MESSAGE_START_WEAPON = 7
MESSAGE_STOP_WEAPON = 8

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para DrunkWarder.py     **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class DrunkWarder(Enm_Def.NPCPerson):

	Durmiendo=0
	Murmurando=0
	Molestado=0
	Muerto=0
	ronquidos=None
	habladormido=None
	molestia=None
	muerte=None

	def __init__(self, person):
		Enm_Def.NPCPerson.__init__(self, person)
		self.Durmiendo=0
		self.Murmurando=0
		self.Molestado=0
		self.Muerto=0
		person.SetTmpAnmFlags(1, 1, 0, 0, 1, 1, 0)
		person.LaunchAnimation("Tkn_sleep2")
		person.SetOnFloor()

		self.ronquidos=Bladex.CreateSound("../../Sounds/snore-loop.wav", "Ronquidos")
		self.ronquidos.Volume=1
		self.ronquidos.Scale=1.0
		self.ronquidos.MinDistance= 5000
		self.ronquidos.MaxDistance=15000

		self.habladormido=Bladex.CreateSound("../../Sounds/drunk-loop.wav", "HablaDormido")
		self.habladormido.Volume=1
		self.habladormido.Scale=1.0
		self.habladormido.MinDistance= 5000
		self.habladormido.MaxDistance=50000

		self.molestia=Bladex.CreateSound("../../Sounds/drunk-loop-short.wav", "Molestia")
		self.molestia.Volume=1
		self.molestia.Scale=1.0
		self.molestia.MinDistance= 5000
		self.molestia.MaxDistance=25000

		self.muerte=Bladex.CreateSound("../../Sounds/knight-die.wav", "Muerte")
		self.muerte.Volume=1
		self.muerte.Scale=1.0
		self.muerte.MinDistance= 5000
		self.muerte.MaxDistance=15000

	def Murmura(self, entity_name):
#		print "Murmura..."
		self.Murmurando=1
		if self.Durmiendo:
			self.Durmiendo=0
			self.ronquidos.Stop()
		if self.Molestado:
			self.Molestado=0
			self.molestia.Stop()
		person=Bladex.GetEntity(entity_name)
		person.Wuea=Reference.WUEA_ENDED
		person.LaunchAnimation("Tkn_sleep")
		person.SetOnFloor()
		self.habladormido.Play(person.Position[0], person.Position[1], person.Position[2], 0)
		person.AnmEndedFunc=self.Duerme

	def Duerme(self, entity_name):
#		print "Duerme..."
		if self.Muerto:
			return
		self.Durmiendo=1
		if self.Murmurando:
			self.Murmurando=0
		if self.Molestado:
			self.Molestado=0
		person=Bladex.GetEntity(entity_name)
		person.Wuea=Reference.WUEA_ENDED
		person.SetTmpAnmFlags(1, 1, 0, 0, 1, 1, 0)
		person.LaunchAnimation("Tkn_sleep2")
		person.SetOnFloor()
		self.ronquidos.Play(person.Position[0], person.Position[1], person.Position[2], -1)

	def Molestia(self, entity_name):
#		print "Se molesta..."
		self.Molestado=1
		if self.Durmiendo:
			self.Durmiendo=0
			self.ronquidos.Stop()
		if self.Murmurando:
			self.Murmurando=0
			self.habladormido.Stop()
		person=Bladex.GetEntity(entity_name)
		person.Wuea=Reference.WUEA_ENDED
		person.LaunchAnimation("Tkn_sleep_hit")
		person.SetOnFloor()
		self.molestia.Play(person.Position[0], person.Position[1], person.Position[2], 0)
		person.AnmEndedFunc=self.Duerme

	def Muere(self, entity_name):
		#print "Muere..."
		#Bldb.set_trace()
		if self.Durmiendo:
			self.Durmiendo=0
			self.ronquidos.Stop()
		if self.Murmurando:
			self.Murmurando=0
			self.habladormido.Stop()
		if self.Molestado:
			self.Molestado=0
			self.molestia.Stop()
		person=Bladex.GetEntity(entity_name)
		person.Wuea=Reference.WUEA_ENDED
		person.LaunchAnimation("Tkn_dth_sleep")
		person.SetOnFloor()
		self.muerte.Play(person.Position[0], person.Position[1], person.Position[2], 0)
		self.Muerto=1

	# Functions for loading and saving state
	def __getstate__(self):
		#print "DrunkWarder.__getstate__"
		NPCPerson_state=Enm_Def.NPCPerson.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			#print "ERROR: DrunkWarder.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["DrunkWarder"]=(self.ronquidos.Name,self.habladormido.Name,
										   self.molestia.Name,self.muerte.Name,
										   self.Durmiendo,self.Murmurando,self.Molestado,self.Muerto
										  )
		return NPCPerson_state

	def __setstate__(self,parm):
		#print "DrunkWarder.__setstate__"
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		Enm_Def.NPCPerson.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["DrunkWarder"]
			self.ronquidos=Bladex.GetSound(parms[0])
			self.habladormido=Bladex.GetSound(parms[1])
			self.molestia=Bladex.GetSound(parms[2])
			self.muerte=Bladex.GetSound(parms[3])
			self.Durmiendo=parms[4]
			self.Murmurando=parms[5]
			self.Molestado=parms[6]
			self.Muerto=parms[7]


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para BurningKnights.py **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class BurningKnight (EnemyTypes.Knight_Traitor):
	def __init__(self, me):
		#Enm_Def.NPCPerson.__init__(self, me)
		EnemyTypes.Knight_Traitor.__init__(self,me)
		AniSound.AsignarSonidosCaballeroTraidor(me.Name)
		me.Blind=1
		me.Deaf=1


	def SetOnFire (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		try:
			UserName = me.Data.UsedBy
			user = Bladex.GetEntity(UserName)
			user_pos = user.Position
		except:
			user_pos = (0.0, 0.0, 0.0)
		me.CatchOnFire (user_pos[0],user_pos[1], user_pos[2])

	def StartRunning (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		Reference.debugprint (EntityName + ": Im starting to run")
		me.ImHurtFunc=self.RunningImHurt
		me.ImDeadFunc=self.RunningImDead
		# Set me alight
		# We need to make this animation interruptable
		#me.SetTmpAnmFlags(0,1,0,0,1,1)
		me.LaunchAnimation ("Tkn_burn")
		me.AnmEndedFunc=self.StartFalling

	def StartFalling (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		# We need to make this animation noninterruptable
		Reference.debugprint (EntityName + ": Im starting to fall")
		me.ImHurtFunc=self.FallingImHurt
		me.ImDeadFunc=self.FallingImDead
		me.SetTmpAnmFlags(1,1,1,0,1,1)
		me.LaunchAnimation ("Tkn_dth_burn")
		me.Life=-20
		me.AnmEndedFunc=self.Die

	def Die (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		Reference.debugprint (EntityName + ": Dieing")

	def RunningImHurt(self,EntityName):
		me.Wuea=Reference.WUEA_ENDED
		me.LaunchAnmType ("dth0")
		me.Life=-20

	def RunningImDead(self,EntityName):
		pass	# Do nothing

	def FallingImHurt(self,EntityName):
		pass	# Do nothing

	def FallingImDead(self,EntityName):
		pass	# Do nothing

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Pendulos.py        **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************


class PENDULO:
	Piv = [0,0,4900]
	Axi = [1,0,0]
	Pendulo = 0
	Angulo = 0
	Vel = 0.01
	fAc = -0.004
	sound1 = 0
	sound2 = 0
	Dir = 1

	def Stop(self):
		self.Pendulo.RemoveFromList("Timer60")                  #Was Timer30 -LeadHead
		self.Pendulo.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
		self.sound1.StopSound()
		self.sound2.StopSound()

	def Play(self):
		self.Pendulo.SubscribeToList("Timer60")                  #Was Timer30 -LeadHead
		self.Pendulo.MessageEvent(MESSAGE_START_WEAPON,0,0)
		self.sound1.Position = self.Pendulo.Position[0],12000,self.Pendulo.Position[2]
		self.sound2.Position = self.Pendulo.Position[0],12000,self.Pendulo.Position[2]
		self.sound1.PlaySound(-1)
		self.sound2.PlaySound(-1)

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Prisioners.py      **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class Prisoner(Enm_Def.StupidNPCPerson):

  agonia1prs=None
  agonia2prs=None
  muerteprs=None
  Agonizando=0
  Muerto=0
  Desmayado=1


  def __init__(self, person):
    Enm_Def.StupidNPCPerson.__init__(self, person)

    self.agonia1prs=Bladex.CreateSound("../../Sounds/moan2.wav", "Agonia1Prs")
    self.agonia1prs.Volume=1
    self.agonia1prs.Scale=1.112
    self.agonia1prs.MinDistance= 5000
    self.agonia1prs.MaxDistance=25000

    self.agonia2prs=Bladex.CreateSound("../../Sounds/moan2.wav", "Agonia2Prs")
    self.agonia2prs.Volume=1
    self.agonia2prs.Scale=1.112
    self.agonia2prs.MinDistance= 5000
    self.agonia2prs.MaxDistance=25000

    self.muerteprs=Bladex.CreateSound("../../Sounds/knight-die.wav", "MuertePrs")
    self.muerteprs.Volume=1
    self.muerteprs.Scale=1.112
    self.muerteprs.MinDistance= 5000
    self.muerteprs.MaxDistance=25000

    self.Agonizando=0
    self.Muerto=0
    self.Desmayado=1
    self.Desmaya(self.Name)

  def Agoniza(self, entity_name):
    #print "Agoniza..."+entity_name
    if self.Muerto:
      return
    if self.Desmayado:
      self.Desmayado=0
    person=Bladex.GetEntity(entity_name)
    if entity_name=="PrisioneroVivo1":
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_agony01")
      person.SetOnFloor()
      self.agonia1prs.Play(person.Position[0], person.Position[1], person.Position[2], 0)
      self.Agonizando=1
    else:
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_agony02")
      person.SetOnFloor()
      self.agonia2prs.Play(person.Position[0], person.Position[1], person.Position[2], 0)
      self.Agonizando=2
    person.AnmEndedFunc=self.Desmaya

  def Desmaya(self, entity_name):
    #print "Desmayado..."+entity_name
    if self.Muerto:
      return
    self.Desmayado=1
    if self.Agonizando:
      self.Agonizando=0
    person=Bladex.GetEntity(entity_name)
    person.SetTmpAnmFlags(1, 1, 0, 0, 1, 1)
    if entity_name=="PrisioneroVivo1":
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_rlx_01")
      person.SetOnFloor()
    else:
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_rlx_02")
      person.SetOnFloor()

  def Muere(self, entity_name):
    #print "Muere..."+entity_name
    if self.Desmayado:
      self.Desmayado=0
    if self.Agonizando:
      if self.Agonizando==1:
        self.agonia1prs.Stop()
      else:
        self.agonia2prs.Stop()
      self.Agonizando=0
    person=Bladex.GetEntity(entity_name)
    person.Wuea=Reference.WUEA_ENDED
    person.LaunchAnimation("Prs_dth")
    person.SetOnFloor()
    self.muerteprs.Play(person.Position[0], person.Position[1], person.Position[2], 0)
    self.Muerto=1


  # Functions for loading and saving state
  def __getstate__(self):
    #print "Prisoner.__getstate__"
    NPCPerson_state=Enm_Def.StupidNPCPerson.__getstate__(self)
    if(NPCPerson_state[0]!=1):
      #print "ERROR: Prisoner.__getstate__(): Base class version differs."
      return NPCPerson_state

    NPCPerson_state[1]["Prisoner"]=(self.agonia1prs.Name,
                          self.agonia2prs.Name,
                          self.muerteprs.Name,
                          self.Agonizando,
                          self.Muerto,
                          self.Desmayado
                         )
    return NPCPerson_state

  def __setstate__(self,parm):
    #print "Prisoner.__setstate__"
    # Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
    Enm_Def.StupidNPCPerson.__setstate__(self,parm)
    version=parm[0]
    if version==1:
      parms=parm[1]["Prisoner"]
      self.agonia1prs=Bladex.GetSound(parms[0])
      self.agonia2prs=Bladex.GetSound(parms[1])
      self.muerteprs=Bladex.GetSound(parms[2])
      self.Agonizando=parms[3]
      self.Muerto=parms[4]
      self.Desmayado=parms[5]





#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampa_flechas.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class FLECHA:
	def __init__(self):
		self.Nombre = ""
		self.Lanzar = ""
		self.Flechas_Clavadas = 0
		self.Estado = 0
		self.Avance = 0
		self.Orientation = [0,0,0,0]
		self.Position = [0,0,0]
		self.Scale = 0
		self.Tiempo_Lanzamiento = 2
		self.Tiempo_Parada	   = 0.9
		self.Sound = 0
		self.NoFXOnHit=1

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Talking_Knights.py **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class TalkingKnight (EnemyTypes.Knight_Traitor):

	Guard1=None
	Guard2=None

	def __init__(self, me):
		EnemyTypes.Knight_Traitor.__init__(self, me)
		language = Language.CheckFallback()
		self.Guard1=Sounds.CreateEntitySound('../../sounds/'+language+'/guard1.wav', 'GuardTalk1')
		self.Guard1.Volume = 1.0
		self.Guard1.MinDistance= 5000
		self.Guard1.MaxDistance=25000
		self.Guard2=Sounds.CreateEntitySound('../../sounds/'+language+'/guard2.wav', 'GuardTalk2')
		self.Guard2.Volume = 1.0
		self.Guard2.MinDistance= 5000
		self.Guard2.MaxDistance=25000

	def StopTalking (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.HearFunc = self.ExHearFunc
		me.SeeFunc = self.ExSeeFunc
		me.SetOnFloor()

		if (EntityName == "Terry"):
			#me.Angle = 0.5
			#self.Guard2.Stop()
			self.Guard2.Volume = 0
		else:
			#me.Angle = 5.5
			#self.Guard1.Stop()
			self.Guard1.Volume = 0

		Actions.QuickTurnToFaceEntity(me.Name,"Player1")
		me.SetActiveEnemy(Bladex.GetEntity("Player1"))

	def LaunchSound1(self):
		self.Guard1.PlaySound(0)

	def LaunchSound2(self):
		self.Guard2.PlaySound(0)

	def HearEvent(self,EntityName,SoundName, x, y, z, Volume):
		self.StopTalking(EntityName)

	def StartTalking1 (self):
		me = Bladex.GetEntity(self.Name)
		friend = Bladex.GetEntity("Terry")

		if me and me.Life > 0 and me.GetActionMode() == Enm_Def.ROUTE_WATCH and friend and friend.GetActionMode() == Enm_Def.ROUTE_WATCH:
			me.SetSound("")
			Bladex.AddScheduledFunc(Bladex.GetTime() + 6.0/20.0,self.LaunchSound1,())
			self.Guard1.Position = me.Position
			self.ExHearFunc = me.HearFunc
			self.ExSeeFunc = me.SeeFunc
			me.HearFunc = self.HearEvent
			me.SeeFunc = self.StopTalking
			Reference.debugprint (self.Name + ": Im starting to talk")
			#me.SetTmpAnmFlags(1,1,1,0,3,1,0) # no cicla, colisiona y no hace transicion
			#me.LaunchAnimation ("Tkn_speak01")
			#me.AnmEndedFunc=self.StopTalking
			me.SetOnFloor()

	def StartTalking2 (self):
		me = Bladex.GetEntity(self.Name)
		friend = Bladex.GetEntity("Eric")
		if me and me.Life > 0 and me.GetActionMode() == Enm_Def.ROUTE_WATCH and friend and friend.GetActionMode() == Enm_Def.ROUTE_WATCH:
			me.SetSound("")
			Bladex.AddScheduledFunc(Bladex.GetTime() + 3.0,self.LaunchSound2,())
			self.Guard2.Position = me.Position
			self.ExHearFunc = me.HearFunc
			self.ExSeeFunc = me.SeeFunc
			me.HearFunc = self.HearEvent
			me.SeeFunc = self.StopTalking
			Reference.debugprint (self.Name + ": Im starting to talk")
			#me.SetTmpAnmFlags(1,1,1,0,3,1,0) # no cicla, colisiona y no hace transicion
			#me.LaunchAnimation ("Tkn_speak02")
			#me.AnmEndedFunc=self.StopTalking
			me.SetOnFloor()

	# Functions for loading and saving state
	def __getstate__(self):
		#print "TalkingKnight.__getstate__"
		NPCPerson_state=EnemyTypes.Knight_Traitor.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			#print "ERROR: TalkingKnight.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["TalkingKnight"]=(
											GameStateAux.SaveEntityAux(self.Guard1),
											GameStateAux.SaveEntityAux(self.Guard2)
											)
		return NPCPerson_state

	def __setstate__(self,parm):
		#print "TalkingKnight.__setstate__"
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		EnemyTypes.Knight_Traitor.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["TalkingKnight"]
			self.Guard1=GameStateAux.LoadEntityAux(parms[0])
			self.Guard2=GameStateAux.LoadEntityAux(parms[1])


#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Sleeping_Knight.py **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class SleepingKnight (EnemyTypes.Knight_Traitor):

	ronquidos=None
	SleepXOffset = 500


	def __init__(self, me):
		EnemyTypes.Knight_Traitor.__init__(self, me)
		self.ronquidos=Sounds.CreateEntitySound("../../Sounds/snore-loop.wav", "Ronquidos2")
		self.ronquidos.Volume=1
		#self.ronquidos.Scale=1.112
		self.ronquidos.MinDistance= 5000
		self.ronquidos.MaxDistance=15000

		self.PutMeToSleep(self.Name)
		me.ImDeadFunc=self.ImDeadFuncJodete

	def ImDeadFuncJodete (self,EntityName):
		Enm_Def.NPCPerson.StdImDead(self,EntityName)
		me = Bladex.GetEntity(EntityName)
		me.Wuea=Reference.WUEA_ENDED
		me.LaunchAnmType("dth0")
		self.ronquidos.StopSound()

	# We sleep against a wall rather than on the floor, so override the basic sleep funcs

	def PutMeToSleep(self,EntityName):
		if not self.Asleep:
			me = Bladex.GetEntity(EntityName)

			self.SleepXOffset = 500
			#me.Position = (me.Position[0]-self.SleepXOffset, me.Position[1], me.Position[2])
			me.Wuea=Reference.WUEA_ENDED
			me.SetTmpAnmFlags(1,1,0,0,0,1,1)
			me.LaunchAnimation("Tkn_sleep_wall")
			me.Blind=1  #just in case
			#me.Deaf=1
			self.Asleep = TRUE
			Bladex.AddScheduledFunc(Bladex.GetTime() + 30.0,self.RePlaySounds,(me,))

	def RePlaySounds(self,me):
			self.ronquidos.Position = me.Position
			self.ronquidos.PlaySound(-1)


	def WakeMeUp(self,EntityName):
		if self.Asleep:
			me = Bladex.GetEntity(EntityName)
			me.Blind=0  #just in case
			self.ronquidos.StopSound()

			# alert animation
			if me.AnimName[:5] == "Sleep" or me.AnimName[:5] == "sleep":
				me.Position = -75975,-6100,53688
				me.Wuea=Reference.WUEA_ENDED
				me.SetTmpAnmFlags(1,0,1,0,1,1)
				me.LaunchAnimation("Tkn_alarm01")
				me.SetOnFloor()
			self.Asleep = FALSE


	# Functions for loading and saving state
	def __getstate__(self):
		#print "SleepingKnight.__getstate__"
		NPCPerson_state=EnemyTypes.Knight_Traitor.__getstate__(self)
		if(NPCPerson_state[0]!=1):
			#print "ERROR: SleepingKnight.__getstate__(): Base class version differs."
			return NPCPerson_state
		NPCPerson_state[1]["SleepingKnight"]=(GameStateAux.SaveEntityAux(self.ronquidos),
											  self.SleepXOffset
											  )
		return NPCPerson_state

	def __setstate__(self,parm):
		#print "SleepingKnight.__setstate__"
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase
		EnemyTypes.Knight_Traitor.__setstate__(self,parm)
		version=parm[0]
		if version==1:
			parms=parm[1]["SleepingKnight"]
			self.ronquidos=GameStateAux.LoadEntityAux(parms[0])
			self.SleepXOffset=parms[1]




#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Ragnar_Actions.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

##class RagnarActions(Enm_Def.NPCPerson):
##	def __init__(self, person):
##		# base class init
##		Enm_Def.NPCPerson.__init__(self, person)
##
##		# Set up orc specific sound priorities
##		self.SoundPriorities[Reference.SND_ARROW] = 10.0
##		self.SoundPriorities[Reference.SND_HIT] = 50.0
##		self.SoundPriorities[Reference.SND_NPC] = 25.0
##		self.SoundPriorities[Reference.SND_NOISYPC] = 30.0
##		self.SoundPriorities[Reference.SND_PC] = 80.0
##
##		self.risaragnar=Bladex.CreateSound("../../Sounds/risa-ragnar.wav", "RisaRagnar")
##		self.risaragnar.Volume=1
##		#self.risaragnar.Scale=0.56
##		#self.risaragnar.MinDistance= 5000
##		#self.risaragnar.MaxDistance=90000
##		self.risaragnar.Scale=3.41
##		self.risaragnar.MinDistance= 5000
##		self.risaragnar.MaxDistance=90000
##
##
##	def Laugh(self, entity_name):
##		person=Bladex.GetEntity(self.Name)
##		self.risaragnar.Play(person.Position[0], person.Position[1], person.Position[2], 0)
##
##	def Escaping(self, risa=0):
##		person=Bladex.GetEntity(self.Name)
##		person.LaunchAnimation("Rgn_escape")
##		if risa:
##			person.AnmEndedFunc=self.Laugh
##
##	def CommandingAndEscaping(self, risa=0):
##		person=Bladex.GetEntity(self.Name)
##		person.LaunchAnimation("Rgn_escape2")
##		if risa:
##			person.AnmEndedFunc=self.Laugh
##
##	def ResetCombat (self,EntityName):
##		Enm_Def.NPCPerson.ResetCombat(self, EntityName)
##		me = Bladex.GetEntity(EntityName)
##		if me and me.Life>0:
##			self.AttacksOwnKind=0
##			self.ChanceOfFury = 0.00
##			me.BlockingPropensity = 0.2
##			me.AttackList = copy.copy(Combat.RagnarAttackData)
