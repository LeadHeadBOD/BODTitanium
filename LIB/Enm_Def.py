##///
##||| Enm_Def.PY TITANIUM
##||| Change list:
##||| * Reworked item dropping on death, refer to StdImDead. Fixes disappearing items.
##||| * 
##\\\ 

import Bladex
import whrandom
import AuxTran
import ScorerActions
import Actions
import Reference
import Basic_Funcs
import Combat
import CharStats
import copy
import whrandom
#import BDAux
import Damage
import Stars
import DMusic
import GameStateAux
#if Reference.DEBUG_INFO == 1:
import pdb

### Magic exclusion group that is assigned to all inventory items and limbs. -LeadHead
EXG_MAGIC = 1337
DEBUG_SOUNDS=0
##################################################################################
#  E V E N T S

	# We see the enemy ["SeeFunc"]
	#
	# We have lost the enemy ["DelayNoSeenFunc"]
	# We have entered an illegal area ["NoAllowedAreaFunc"]
	# Our enemy (who we are chasing) enters an illegal area) ["EnemyNoAllowedAreaFunc"]
	# We are hurt ["ImHurtFunc"]
	# We die ["ImDeadFunc"]
	# Our enemy dies ["EnemyDeadFunc"]
	# An animation ends ["AnmEndedFunc"]
	# We enter close weapon range with our enemy ["EnterCloseFunc"]
	# We enter far weapon range (bows/crossbows) ["EnterLargeFunc"]
	# We enter our primary action area  ["EnterPrimaryAAFunc"]
	# We enter our secondary action area["EnterSecondaryAAFunc"]
	# Another character entity sees his enemy ["CharSeeingEnemyFunc"]
	# Executed a combo for the first time ["NewComboFunc"]
	# Engage/disengage combat mode ["ToggleCombatFunc"]

##################################################################################
#
#
# Pseudo defines
#
#
##################################################################################

#
# Twinkle FX for several kinds of objects
#
TwinkleObjs = ["Gema"]

THROWNHURTTIME_GAP=45
#
#Several sets of values needed for the SetAnmFlags() and SetTmpAnmFlags() methods
#

#"bng_mov" parameter
BM_IDC=0
BM_NONE=1
BM_XYZ=2
BM_XZ=3
BM_2ANM=4
BM_SCRIPT=5

#"headf" parameter
HEADF_ENG=0
HEADF_ANM=1
HEADF_ANM2SEE=2
HEADF_ANM2ENG=3



#
#Values returned by AstarState
#
ASTAR_THINKING=0
ASTAR_NOSOLVED=1
ASTAR_SOLVED=2
ASTAR_RECALCULATING=3

#
# Boolean value
#
TRUE = 1==1
FALSE = not TRUE


#
#NOTE :Values returned by StatR() AND StatL() are declared in Actions.py
#


#
#Values returned by the Wuea("WaitUntilEnfofAnimation")
#
WUEA_NONE=0    #It does not have to wait (relax , jog or similars)
WUEA_WAIT=1    #It has to wait , and is waiting to end it
WUEA_ENDED=2   #It has to wait , and it has just ended

#
#Values returned by GetActionMode()
#
ROUTE_WATCH=0  #Watch mode
ROUTE_BAY=1    #Performing a bay route
ROUTE_CHASE=2  #Chase a character
ROUTE_SINGLE=3 #Following a single route (going to just a point)
ROUTE_BOWING=4 #Bowing (OR trying to bow) an enemy
##################################################################################

# Comparison results for sorting
CHOOSE_FIRST  = -1
CHOOSE_SECOND =  1
CHOOSE_EITHER =  0

# yeah! cool sounds
new_key_sound = Bladex.CreateSound('../../Sounds/Manipulado-llave2.wav', 'NewKeySound')
new_key_sound.Volume=1
new_key_sound.MinDistance=10000
new_key_sound.MaxDistance=20000

##################################################################################
#
#
# Sorting enemy functions
#
#
##################################################################################

### 
def ResetExclusionGroup(ent_name):
	me= Bladex.GetEntity(ent_name)
	me.ExclusionGroup= EXG_MAGIC
	me.OnStopFunc= None

def ChooseNearest (entity1name, entity2name):
	p1 = Bladex.GetEntity(entity1name)
	p2 = Bladex.GetEntity(entity2name)
	if not p1 and not p2:
		return CHOOSE_EITHER
	elif not p1:
		return CHOOSE_SECOND
	elif not p2:
		return CHOOSE_FIRST

	if p1.Life <= 0 and p2.Life <= 0:
		return CHOOSE_EITHER
	elif p1.Life <= 0:
		return CHOOSE_SECOND
	elif p2.Life <= 0:
		return CHOOSE_FIRST


	# If it just comes down to distance, group leaders may order others before them
	if p1.Data.group_leader:
		return CHOOSE_SECOND
	elif p2.Data.group_leader:
		return CHOOSE_FIRST

	enemy=Bladex.GetEntity(p1.GetEnemyName())
	if not enemy:
		return CHOOSE_EITHER

	val = enemy.SQDistance2(p1) - enemy.SQDistance2(p2)

	if val < 0:
		return CHOOSE_FIRST
	elif val > 0:
		return CHOOSE_SECOND
	else:
		return CHOOSE_EITHER

def ChooseFurthest (entity1name, entity2name):
	p1 = Bladex.GetEntity(entity1name)
	p2 = Bladex.GetEntity(entity2name)
	if not p1 and not p2:
		return CHOOSE_EITHER
	elif not p1:
		return CHOOSE_SECOND
	elif not p2:
		return CHOOSE_FIRST

	if p1.Life <= 0 and p2.Life <= 0:
		return CHOOSE_EITHER
	elif p1.Life <= 0:
		return CHOOSE_SECOND
	elif p2.Life <= 0:
		return CHOOSE_FIRST

	# If it just comes down to distance, group leaders may order others before them
	if p1.Data.group_leader:
		return CHOOSE_SECOND
	elif p2.Data.group_leader:
		return CHOOSE_FIRST

	enemy=Bladex.GetEntity(p1.GetEnemyName())
	if not enemy:
		return CHOOSE_EITHER

	val = enemy.SQDistance2(p1) - enemy.SQDistance2(p2)

	if val < 0:
		return CHOOSE_SECOND
	elif val > 0:
		return CHOOSE_FIRST
	else:
		return CHOOSE_EITHER


def ChooseMostLife (entity1name, entity2name):
	p1 = Bladex.GetEntity(entity1name)
	p2 = Bladex.GetEntity(entity2name)

	if not p1 and not p2:
		return CHOOSE_EITHER
	elif not p1:
		return CHOOSE_SECOND
	elif not p2:
		return CHOOSE_FIRST

	if p1.Life <= 0 and p2.Life <= 0:
		return CHOOSE_EITHER
	elif p1.Life <= 0:
		return CHOOSE_SECOND
	elif p2.Life <= 0:
		return CHOOSE_FIRST

	l1 = p1.Life
	l2 = p2.Life
	val = l2 - l1
	if val < 0:
		return CHOOSE_FIRST
	elif val > 0:
		return CHOOSE_SECOND
	else:
		return ChooseNearest (entity1name, entity2name)

def ChooseFighter (entity1name, entity2name):
	p1 = Bladex.GetEntity(entity1name)
	p2 = Bladex.GetEntity(entity2name)

	if not p1 and not p2:
		return CHOOSE_EITHER
	elif not p1:
		return CHOOSE_SECOND
	elif not p2:
		return CHOOSE_FIRST

	if p1.Life <= 0 and p2.Life <= 0:
		return CHOOSE_EITHER
	elif p1.Life <= 0:
		return CHOOSE_SECOND
	elif p2.Life <= 0:
		return CHOOSE_FIRST

	enemy=Bladex.GetEntity(p1.GetEnemyName())

	if not p1.InCombat:
		if not p2.InCombat:
			# Neither are in combat, just choose the closest
			return ChooseNearest (entity1name, entity2name)
		# Second entity is only one in combat
		return CHOOSE_SECOND
	elif not p2.InCombat:
		# First entity is only one in combat
		return CHOOSE_FIRST

	# This far means both are in combat
	if not p1.CanISee(enemy):
		if not p2.CanISee(enemy):
			# Neither can see the enemy, but both are in combat,
			# choose the one with most life
			return ChooseMostLife (entity1name, entity2name)
		# Second entity is only one to see the enemy
		return CHOOSE_SECOND

	elif not p2.CanISee(enemy):
		# First entity is only one to see the enemy
		return CHOOSE_FIRST

	# This far means both are in combat and both can see the enemy
	return ChooseMostLife (entity1name, entity2name)

def ChooseLeaderOutOfCombat (entity1name, entity2name):
	p1 = Bladex.GetEntity(entity1name)
	p2 = Bladex.GetEntity(entity2name)

	# Best to see the other to give them orders
	if p1.CanISee(p2):
		if not p2.CanISee(p1):
			return CHOOSE_FIRST
	elif p2.CanISee(p1):
		return CHOOSE_SECOND

	# Best to see the enemy next
	enemy=Bladex.GetEntity(p1.GetEnemyName())
	if p1.CanISee(enemy):
		if not p2.CanISee(enemy):
			return CHOOSE_FIRST
	elif p2.CanISee(enemy):
		return CHOOSE_SECOND

	# Both or neither can see the other,
	# Both or neither can see the enemy,
	# Just choose the furthest from the enemy,
	# to order the other into combat more easily
	return ChooseFurthest (entity1name, entity2name)


def ChooseLeader (entity1name, entity2name):
	p1 = Bladex.GetEntity(entity1name)
	p2 = Bladex.GetEntity(entity2name)

	if not p1 and not p2:
		return CHOOSE_EITHER
	elif not p1:
		return CHOOSE_SECOND
	elif not p2:
		return CHOOSE_FIRST

	if p1.Life <= 0 and p2.Life <= 0:
		return CHOOSE_EITHER
	elif p1.Life <= 0:
		return CHOOSE_SECOND
	elif p2.Life <= 0:
		return CHOOSE_FIRST

	enemy=Bladex.GetEntity(p1.GetEnemyName())

	if p1.Data.group_fighter:
		if p2.InCombat or (p2.CanISee(enemy) and p2.GetActionMode()==ROUTE_CHASE and p2.AstarState==ASTAR_SOLVED):
			return CHOOSE_SECOND
		# Fighter would put himself before
		return CHOOSE_FIRST

	elif p2.Data.group_fighter:
		if p1.InCombat or (p1.CanISee(enemy) and p1.GetActionMode()==ROUTE_CHASE and p1.AstarState==ASTAR_SOLVED):
			return CHOOSE_FIRST
		# Fighter would put himself before
		return CHOOSE_SECOND

	# This far means neither are group fighters
	if not p1.InCombat:
		if not p2.InCombat:
			return ChooseLeaderOutOfCombat (entity1name, entity2name)
		# Second entity is only one in combat
		return CHOOSE_SECOND
	elif not p2.InCombat:
		# First entity is only one in combat
		return CHOOSE_FIRST

	# This far means neither are group fighters and both are in combat
	if not p1.CanISee(enemy):
		if not p2.CanISee(enemy):
			# Neither can see the enemy, but both are in combat,
			# choose the one with most life
			return ChooseMostLife (entity1name, entity2name)
		# Second entity is only one to see the enemy
		return CHOOSE_SECOND

	elif not p2.CanISee(enemy):
		# First entity is only one to see the enemy
		return CHOOSE_FIRST

	# This far means neither are group fighters and both are in combat
	# and both can see the enemy
	return ChooseMostLife (entity1name, entity2name)
##################################################################################



# Define the default NPC python person class
class NPCPerson (Basic_Funcs.PlayerPerson):
	InvestigatingSound = FALSE
	SoundPriorities = [-1.0, -1.0, -1.0, -1.0, -1.0]
	Asleep = FALSE
	SleepYOffset = 1100.0		# this may need adjusting for non-knight chars
	group_fighter=TRUE
	group_leader=TRUE
	AttackingNPC=FALSE
	goto_limit2aa=TRUE
	imusic_noseen_warp=0
	DelayNoSeenFuncMusicBackUp=0
	last_insulting_time_1AA=-1
	LastThrownHurtTime=0
	AttacksOwnKind=FALSE
	AttackNPCTime = 5
	Angry=FALSE
	Furious=FALSE
	ChanceOfFuryOnHurt = 0.00
	ChanceOfFuryOnLeaderDeath = 0.00
	ImpatientAttackTime= 5.0


	def __init__(self, me):
		Basic_Funcs.PlayerPerson.__init__(self, me)
		self.SoundPriorities = [-1.0, -1.0, -1.0, -1.0, -1.0]
		self.inheritance = 1

		#_________________________________________#
		#  Record some personal data              #
		#_________________________________________#
		AddMyWatchAnims(me.Name)
		self.NPC = 1


		#pdb.set_trace()
		self.ResetCombat(me.Name)
		self.NoFXOnHit= FALSE


		#_________________________________________#
		# Initialise core                         #
		#_________________________________________#
		me.SubscribeToList("Listeners")
		me.Deaf = 0
		me.CombatGroup = "Group of " + me.Name


		#_________________________________________#
		# Set up the core functions               #
		#_________________________________________#
		me.SeeFunc=self.StdSeeTheEnemy
		me.HearFunc=self.StdHearFunc
		me.DelayNoSeenFunc=self.StdDelayNoSeen
		me.NoAllowedAreaFunc=self.StdNoAllowedArea
		me.EnemyNoAllowedAreaFunc=self.StdEnemyNoAllowedArea
		me.ImHurtFunc=self.StdImHurt
		me.ImDeadFunc=self.StdImDead
		me.EnemyDeadFunc=self.StdEnemyDead
		me.AnmEndedFunc=self.StdAnmEnded
		me.EnterCloseFunc=self.StdEnterClose
		me.EnterLargeFunc=self.StdEnterLarge
		me.EnterPrimaryAAFunc=self.StdEnterPrimaryAA
		me.EnterSecondaryAAFunc=self.StdEnterSecondaryAA
		me.CharSeeingEnemyFunc=self.StdCharSeeingEnemy
		me.ToggleCombatFunc=self.StdToggleCombat

		# Set us up to start in the large range, so archers get your bows out!
		#pdb.set_trace()
		self.WeaponsOut(me.Name)

	#_________________________________________#
	# Define our functions                    #
	#_________________________________________#

	def ResetCombat (self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			me.BlockingPropensity = 0.5
			me.AttackList = []
			me.CombatDistFlag = not self.group_fighter

		self.AttacksOwnKind=FALSE
		self.AttackNPCTime = 5
		self.Angry=FALSE
		self.Furious=FALSE
		self.ChanceOfFuryOnHurt = 0.00
		self.ChanceOfFuryOnLeaderDeath = 0.00
		self.ImpatientAttackTime= 5.0

	def StopNPCsAttacking (self,EntityName):
		#print EntityName+" should stop attacking enemy now "+`Bladex.GetTime()`
		# Stop both combatants
		me = Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			enemy = Bladex.GetEntity(me.GetEnemyName())
			self.StopAttackingNPC (EntityName)
			if enemy and enemy.Life > 0 and enemy.Data.NPC:
				enemy.Data.StopAttackingNPC (enemy.Name)



	def StopAttackingNPC (self,EntityName):
		if self.AttackingNPC:
			me = Bladex.GetEntity(EntityName)
			if me and me.Life>0:
				enemy = Bladex.GetEntity(me.GetEnemyName())
				if not enemy or enemy.Data.NPC:
					enemy = Bladex.GetEntity("Player1")
					if not enemy:
						print EntityName+": Cannot access handle to Player, in StopAttackingNPC()"
						Bladex.AddScheduledFunc(Bladex.GetTime() + self.AttackNPCTime, self.StopNPCsAttacking,(EntityName,))
						return
					#print EntityName+": Stopping attacking "+me.GetEnemyName()+" at time: "+`Bladex.GetTime()`
					Damage.DropInvalidObjectsOnImpact (EntityName)
					me.Wuea=Reference.WUEA_ENDED
					me.InterruptCombat()
					if me.SetEnemy(enemy):
						self.AttackingNPC=FALSE
						MaxCombatDist = Bladex.GetCharType(me.CharType,me.CharTypeExt).MaxCombatDist
						if me.SQDistance2(enemy) < (MaxCombatDist*MaxCombatDist) or me.CanISee(enemy):
							me.SetActiveEnemy(enemy)
							me.Chase(enemy, me.ActionAreaMax)
							if me.GetActionMode()==ROUTE_CHASE and self.IsArcher():
								self.Switch2MeleeWeapons(EntityName)
						else:
							me.LaunchWatch()
							Damage.DropInvalidObjectsOnImpact (EntityName)
							me.Wuea=Reference.WUEA_ENDED
							me.LaunchAnmType("attack_look",1)
						self.CheckToJoin (EntityName)
					else:
						print EntityName+": Cannot SetEnemy to Player, in StopAttackingNPC()"
						Bladex.AddScheduledFunc(Bladex.GetTime() + self.AttackNPCTime, self.StopNPCsAttacking,(EntityName,))
						return

	#
	# Standard function of ending a route
	#
	def StdRouteEnded(self,EntityName):
		pass


	#
	# Standard function of ending a chase without combat
	#
	def StdEndChase(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		# Check I'm not dead
		if me and me.Life >0:
			if not me.InCombat:
				Reference.debugprint(EntityName + ": I have ended a chase without combat (StdEndChase1)")
				enemy_pos=me.EnemyLastSeen
				if Actions.IsFacingPos(EntityName, enemy_pos[0], enemy_pos[2]):
					self.StdEndChase2(EntityName)
				else:
					Actions.TurnToFacePos(EntityName, enemy_pos[0], enemy_pos[2])
					me.RouteEndedFunc=self.StdEndChase2		# Continue when we're facing


	def StdEndChase2(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		# Check I'm not dead
		if me and me.Life > 0:
			Reference.debugprint(EntityName + ": I have ended a chase without combat (StdEndChase2)")
			me.RouteEndedFunc=self.StdRouteEnded
			me.StopLooking()
			self.InvestigatingSound = FALSE
			enemy=Bladex.GetEntity(me.GetEnemyName())
			enemy_in_sight = enemy and me.CanISee(enemy)
			if enemy_in_sight and enemy.InsideActionArea(me.ActionAreaMax):
				if Actions.IsFacingEntity(EntityName, me.GetEnemyName()):
					self.LaunchMyWatch (EntityName)
				else:
					Actions.TurnToFaceEntity(EntityName, me.GetEnemyName())
					me.RouteEndedFunc=self.LaunchMyWatch
			else:
				if enemy_in_sight:
					self.StdSeeEnemyUnreachable (EntityName)
				else:
					Damage.DropInvalidObjectsOnImpact (EntityName)
					me.Wuea=Reference.WUEA_ENDED
					if me.GetActionMode() != ROUTE_WATCH:
						self.LaunchMyWatch (EntityName)
					me.LaunchAnmType("look_around",1)
				# The enemy has disappeared for us around here
				# If we cannot find him, change our behaviour from the standard no seen function
				me.DelayNoSeenFunc=self.EndChaseDelayNoSeen
				if me.Data.imusic_noseen_warp==1:
					DMusic.RestoreMusicWarperDelayNoSeenFunc(EntityName)

	def PutMeToSleep(self,EntityName):
		if not self.Asleep:
			me = Bladex.GetEntity(EntityName)
			me.SetTmpAnmFlags(1,1,0,0,1,1)
			# doesn't work for the traitor knight, so just call the Tkn version instead!
			#We need to move the char down as well to touch the floor
			me.Position = (me.Position[0], me.Position[1]+self.SleepYOffset, me.Position[2])
			me.LaunchAnimation("Tkn_sleep")
			me.Blind=1  #just in case
			self.Asleep = TRUE

	def WakeMeUp(self,EntityName):
		if self.Asleep:
			me = Bladex.GetEntity(EntityName)
			me.Blind=0  #just in case
			# alert animation
			me.Position = (me.Position[0], me.Position[1]-(self.SleepYOffset*0.5), me.Position[2])
			if me.AnimName[:5] == "Sleep" or me.AnimName[:5] == "sleep":
				me.Wuea=Reference.WUEA_ENDED
				me.LaunchAnmType("alarm01",1)
			self.Asleep = FALSE

	#
	# Standard function of trying to initialise a chase,
	#
	def StdStartChase(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		enemy=Bladex.GetEntity(me.GetEnemyName())
		me.AnmEndedFunc=self.StdAnmEnded
		#enemy_pos=enemy.Position
		#me.StartLooking(enemy_pos[0], enemy_pos[1], enemy_pos[2])
		if enemy.InsideActionArea(me.ActionAreaMax) or (self.IsArcher() and me.InsideActionArea(me.ActionAreaMax)):
			self.StdStartChase2 (EntityName)
		else:
			# The following is to turn to face the enemy when we are already at an illegal border
			self.StdSeeEnemyUnreachable (EntityName)

	def StdSeeEnemyUnreachable(self,EntityName,check1aaTo2aa=1):
		me = Bladex.GetEntity(EntityName)
		Reference.debugprint(EntityName + ": Enemy Unreachable")
		if Bladex.GetTime()-self.LastThrownHurtTime<THROWNHURTTIME_GAP:
			return

		if me.InsideActionArea(me.ActionAreaMin) and (check1aaTo2aa and not me.Will1aaTo2aa):

			if me.Data.goto_limit2aa:
				back_area_min=me.ActionAreaMin
				back_area_max=me.ActionAreaMax
				me.ActionAreaMin=0
				me.ActionAreaMax=0
				enemy=Bladex.GetEntity(me.GetEnemyName())
				des_pos=enemy.Position
				me.GoToJogging=1
				if me.GoTo(des_pos[0],des_pos[1],des_pos[2]):
					me.ActionAreaMin=back_area_min
					me.ActionAreaMax=back_area_max
				else:
					Reference.debugprint(EntityName + ": GoTo enemy_pos not working, with action area 0!")
					me.ActionAreaMin=back_area_min
					me.ActionAreaMax=back_area_max


			return

		elif me.InsideActionArea(me.ActionAreaMin):
			if me.GetActionMode() != ROUTE_WATCH:
				self.LaunchMyWatch (EntityName)
			if not Actions.IsFacingEntity(EntityName, me.GetEnemyName()):
				Actions.TurnToFaceEntity(EntityName, me.GetEnemyName())
			else:
				curr_time=Bladex.GetTime()
				if curr_time-self.last_insulting_time_1AA>4:
					insult_prob=whrandom.uniform(0.0, 1.0)
					if insult_prob<0.8:
						Combat.Insult(EntityName)
					insult_var=whrandom.uniform(-2.0, 1.0)
					self.last_insulting_time_1AA=Bladex.GetTime()+insult_var
		else:
			back_area_min=me.ActionAreaMin
			back_area_max=me.ActionAreaMax
			me.ActionAreaMax= 0
			me.ActionAreaMin= 0

			init_pos=me.InitPos
			me.InvertedRoute=1 # Move backwards
			if me.GoTo(init_pos[0],init_pos[1],init_pos[2]):
				me.ActionAreaMin=back_area_min
				me.ActionAreaMax=back_area_max
			else:
				Reference.debugprint(EntityName + ": GoTo init_pos not working, with action area 0!")
				me.ActionAreaMin=back_area_min
				me.ActionAreaMax=back_area_max


	def StdStartChase2(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		enemy=Bladex.GetEntity(me.GetEnemyName())
		oldActionMode = me.GetActionMode()
		if (oldActionMode == ROUTE_WATCH) or (oldActionMode == ROUTE_BOWING):
			# We could have got here after turning, so reset the RouteEndedFunc.
			me.RouteEndedFunc=self.StdRouteEnded
		if oldActionMode == ROUTE_CHASE:
			pass
		else:
			self.ResetCombat(EntityName)
			last_time_seen=me.LastTimeSeen       #Note that the "Chase" function updates the LastSeenTime!
			me.Chase(enemy, me.ActionAreaMax)
			if me.GetActionMode()==ROUTE_CHASE:
				if self.IsArcher():
					self.Switch2MeleeWeapons(EntityName)
				else:
					if Bladex.GetTime()-last_time_seen>40 or last_time_seen<0:
						me.LaunchAnmType("alarm01",1)
					#else:
					#	print "Too early to alarm..." + str(me.LastTimeSeen)

				self.InvestigatingSound = FALSE
				me.RouteEndedFunc=self.StdEndChase
				if me.Aim or Actions.CurrentlyBowing(EntityName):
					me.Wuea=Reference.WUEA_ENDED
					Actions.EndBowMode(EntityName)
			else:
				self.StdChaseFailed (EntityName, oldActionMode)


	# Is Chase() going to put us in BOWING mode when it fails
	def IsArcher(self):							# Needs to more sopisticated when inventory is working
		return Actions.StatL(self.Name)==Actions.RA_BOW


	def StdChaseFailed(self,EntityName, oldActionMode):	# Try to restore our state to whatever we were doing before attempting to chase
		me = Bladex.GetEntity(EntityName)
		newActionMode = me.GetActionMode()
		if newActionMode == ROUTE_BOWING:
			Reference.debugprint(EntityName + ": I cannot start a chase so I will bow")
			pass
		#NOTA : R_WATCH incluye _BAY (al fallar un GoTo desde una W_BAY se pasa AUTOMATICAMEnTE a watch!!!)
		elif oldActionMode == ROUTE_WATCH:
			Reference.debugprint(EntityName + ": I cannot start a chase so I will watch again")
			self.LaunchMyWatch(EntityName)

			enemy=Bladex.GetEntity(me.GetEnemyName())
			if enemy and me.CanISee(enemy) and me.InsideActionArea(me.ActionAreaMin):
				inv = me.GetInventory()
				if inv.HasBow and me.RangeActive:
					#print "StdChaseFailed-> Just facing due to carry bow"
					enemy_pos=me.EnemyLastSeen
					if not Actions.IsFacingPos(EntityName, enemy_pos[0], enemy_pos[2]):
						Actions.TurnToFacePos(EntityName, enemy_pos[0], enemy_pos[2])
				else:
					self.StdSeeEnemyUnreachable (EntityName,0)



	def GiveOrders (self, EntityName):
		me=Bladex.GetEntity(EntityName)
		if me and me.Life>0 and self.NextOrdersTo and self.NextOrders:
			me.Wuea=Reference.WUEA_ENDED
			me.SetTmpAnmFlags(1,0,1,0,1,1)
			me.LaunchAnmType("order",1)
			me.AnmEndedFunc=self.GiveOrders2

	def GiveOrders2 (self, EntityName):
		me=Bladex.GetEntity(EntityName)
		if me and self.NextOrdersTo and self.NextOrders:
			for name in self.NextOrdersTo:
				self.NextOrders(name)

	def CheckToJoin (self, EntityName):
		##startmem = BDAux.GetAvailablePhysicalMemory()
		me = Bladex.GetEntity(EntityName)
		##if BDAux.GetAvailablePhysicalMemory() != startmem:
		##	pdb.set_trace()
		# Get a list of the enemies of my enemy currently in combat
		#pdb.set_trace()
		ally_list = me.GetCombatants()
		##if BDAux.GetAvailablePhysicalMemory() != startmem:
		##	pdb.set_trace()
		for ally_name in ally_list:
			if ally_name != EntityName:	# Cannot really happen I think
				ally = Bladex.GetEntity (ally_name)
				if ally:
					if me.CombatGroup != ally.CombatGroup:
						self.JoinGroup (EntityName, ally.CombatGroup)
					return
		##if BDAux.GetAvailablePhysicalMemory() != startmem:
		##	pdb.set_trace()

		self.CheckGoodGroupFormation (EntityName, TRUE)
		##if BDAux.GetAvailablePhysicalMemory() != startmem:
		##	pdb.set_trace()

	def JoinGroup (self, EntityName, GroupName):
		me = Bladex.GetEntity(EntityName)
		# Joining Group Logic
		me.CombatGroup = GroupName
		self.group_fighter = FALSE
		self.group_leader  = FALSE
		if not self.Furious:
			me.CombatDistFlag = 1		# move out
		self.CheckGoodGroupFormation (EntityName, TRUE)

	def LeaveGroup(self, EntityName):
		# Make sure the group we are leaving has a fighter and a leader
		me = Bladex.GetEntity(EntityName)
		if self.group_fighter or self.group_leader:
			self.SetGroupFormation(EntityName, FALSE, self.group_leader)
		NewCombatGroup = "Group of " + me.Name
		if me.CombatGroup == NewCombatGroup:
			NewCombatGroup= NewCombatGroup + '... Splitters'
		me.CombatGroup = NewCombatGroup
		self.group_leader = TRUE
		self.group_fighter = TRUE


	#
	# Standard function of seeing an enemy
	#
	def StdSeeTheEnemy(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		Reference.debugprint (EntityName + ": I see the enemy");
		life = me.Life
		if life > 0.0:		# Check I'm not dead
			if me.Blind==1:
				pass
			else:
				me.LookAtEntity(me.GetEnemyName())

				#Just in case we were doing a wait animation
				if me.GetActionMode() == ROUTE_BAY:
					me.Wuea=Reference.WUEA_ENDED

				self.CheckToJoin(EntityName)
				if me.GetActionMode()!=ROUTE_CHASE:
					self.StdStartChase(EntityName)

				if me.GetActionMode()==ROUTE_BOWING:
					if self.AimPressed:
						angle= Reference.TARGET_ANGLE_MAX- me.Accuracy*(Reference.TARGET_ANGLE_MAX-Reference.TARGET_ANGLE_MIN)
						if me.AimOffTarget<angle:
							# print "Releasing Arrow"
							Actions.TestReleaseArrow(EntityName)
					else:
						if me.Wuea!=Reference.WUEA_WAIT:
							# print "Drawing Bow"
							Actions.TestDrawBow (EntityName)
				elif me.Aim or Actions.CurrentlyBowing(EntityName):
					me.Wuea=Reference.WUEA_ENDED
					Actions.EndBowMode(EntityName)
					me.SetOnFloor()
		else:
			print (EntityName + ": Cannot get a handle on me")
	#
	# Standard function of hearing an enemy
	#
	# make a default database here.  Other entities can have other databases...
	# Sonidas Flechas (Arrow sounds)
	# Objeto Arrojado o golpeado (thrown objects or hitting sounds)
	# Sonido de enemigo.  Por grito o herida (Other NPCs shouting, or injured)
	# Sonido de personaje ojando no esta en modo siglo (pisadas) (PC sounds when they're not walking silently -- footsteps)
	# Gritas de atao o herida (Battle cries or injuries of the PC)

	def GetSoundType(self, SoundName):
		if Reference.SoundTypes.has_key(SoundName):
			return Reference.SoundTypes[SoundName][0]
		return Reference.SND_UNCLASSIFIED

	def GetSoundPriority (self, EntityName,  SoundName, Volume):
		me = Bladex.GetEntity(EntityName)
		# Check against our sound tables
		priority = Reference.SND_UNCLASSIFIED		# look this up in a dictionary for our race, or -1.0 if not present
		sound_type= self.GetSoundType(SoundName)
		if sound_type != Reference.SND_UNCLASSIFIED:
			priority = self.SoundPriorities [sound_type]
			# volume should be between 0.0 and 1.0 or an order of magnitude smaller
			# than the base priority.  Scale it down to be sure
			return  priority + (Volume * 0.01)

	def IsSoundHigherPriority (self, EntityName, SoundName, Volume):
		me = Bladex.GetEntity(EntityName)
		priority = self.GetSoundPriority (EntityName, SoundName, Volume)
		if priority <= 0.0:	# if we're not interested in this kind of sound:
			return FALSE
		elif (not self.InvestigatingSound) or (me.GetActionMode()!=ROUTE_SINGLE):
			return TRUE
		else:
			investigating_priority = self.GetSoundPriority (EntityName, self.InvestigatingSoundName, self.InvestigatingSoundVolume)
			return priority > investigating_priority

	def StdInvestigateSound(self,EntityName):
		me = Bladex.GetEntity(EntityName)

		if me and me.Life > 0:
			me.StartLooking(self.InvestigatingSoundX, self.InvestigatingSoundY, self.InvestigatingSoundZ)
			Reference.debugprint (EntityName + ": Im going to investigate "+self.InvestigatingSoundName+" at pos "+`self.InvestigatingSoundX`+", "+`self.InvestigatingSoundY`+", "+`self.InvestigatingSoundZ`);
			me.GoToSneaking=1
			me.GoTo(self.InvestigatingSoundX,self.InvestigatingSoundY,self.InvestigatingSoundZ)

			if me.AstarState<>ASTAR_SOLVED:
				# We cannot get there, just look at the source of the sound instead
				me.GoToSneaking=0
				if Actions.IsFacingPos(EntityName, self.InvestigatingSoundX, self.InvestigatingSoundZ):
					self.LaunchMyWatch (EntityName)
				else:
					Actions.TurnToFacePos(EntityName, self.InvestigatingSoundX, self.InvestigatingSoundZ)
					me.RouteEndedFunc=self.LaunchMyWatch
			else:
				# We can use the same end func as ending a chase
				me.Heard = TRUE
				me.RouteEndedFunc=self.StdEndChase2

	def CanGoTo (self, EntityName, x, y, z):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life > 0:
			me.GoTo(x,y,z)
			if me.AstarState==ASTAR_SOLVED:
				me.LaunchWatch()
				return TRUE
		return FALSE


	def StdHearFunc(self,EntityName, SoundName, x, y, z, Volume):
		me = Bladex.GetEntity(EntityName)

		if me and Bladex.InsideActionArea(me.ActionAreaMax, x , y , z)==0:
			#print "About to investigate a sound NO in AAs " + EntityName
			return


		if me and me.Life > 0 and me.Deaf<>1:

			# try:
				# Is the sound below audible range
				if Volume < Bladex.GetCharType(me.CharType,me.CharTypeExt).HearMinVolume:
					return

				# No need to bother responding if we're already in combat
				if me.InCombat:
					return

				#if DEBUG_SOUNDS:
				#	pdb.set_trace()
				sound_type= self.GetSoundType(SoundName)

				# Is the sound unknown
				if sound_type==Reference.SND_UNCLASSIFIED:
					return

				# If our enemy is dead, don't bother going to investigate
				enemy=Bladex.GetEntity(me.GetEnemyName())
				if (not enemy) or (not enemy.Person) or enemy.Life <= 0:
					return

				# for footsteps etc, Check they belong to the player, not realistic, but quick
				if sound_type==Reference.SND_NOISYPC:
					#if self.GroupCoveringPoint (EntityName, x, y, z, FALSE):
					#	return
					if enemy.LastSound != SoundName:
						return

					elsp= enemy.LastSoundPosition
					if elsp[0]!= x or elsp[1]!=y or elsp[2]!=z:
						return

				# Was the sound generated by oureself
				#if me.TestPosInOwnBox (x, y, z, 1.05):
				if me.LastSound==SoundName:
					lsp= me.LastSoundPosition
					if lsp[0]== x and lsp[1]==y and lsp[2]==z:
						return

				# Is the sound from our last thrown hurt ?
				if Bladex.GetTime()-self.LastThrownHurtTime<THROWNHURTTIME_GAP*0.5:
					return

				# The see functions will take care of this
				if me.CanISee(enemy):
					return

				if self.Asleep:
					self.WakeMeUp(EntityName)

				if me.GetActionMode() == ROUTE_BAY and not me.CanGoTo(x,y,z):
					#print "StdHearFunc, debug - BAY stuff..."
					return


				if self.group_leader:
					# record that we have dealt with the sound
					self.DealtWithSound= SoundName
					self.DealtWithSoundX= x
					self.DealtWithSoundY= y
					self.DealtWithSoundZ= z

					# Assign an investigator
					investigator = self.GetGroupFighter(EntityName)
					if (not investigator) or (investigator.Name != me.Name):
						if (not investigator) or investigator.GetActionMode()==ROUTE_CHASE or investigator.InCombat or not investigator.CanGoTo(x,y,z):
							investigator = me
				else:
					group_leader = self.GetGroupLeader(EntityName)
					if group_leader and not (group_leader.InCombat or group_leader.GetActionMode()==ROUTE_CHASE):
						# does the leader know already?
						try:
							ldr_data= group_leader.Data
							if SoundName==ldr_data.DealtWithSound and x==ldr_data.DealtWithSoundX and y==ldr_data.DealtWithSoundY and z==ldr_data.DealtWithSoundZ:
								return
						except:
							pass
						group_leader.HearFunc(group_leader.Name, SoundName, x, y, z, Volume)
						# leader will tell investigator what to do
						# but we can take the initiative to turn around
						if (not me.InCombat) and (me.GetActionMode()!=ROUTE_CHASE):
							if not Actions.IsFacingPos(EntityName, x, z):
								Actions.QuickTurnToFacePos(EntityName, x, z)
						return
					else:
						# leader is busy, investigate ourself
						investigator = me

				if investigator.Data.InvestigatingSound and SoundName == investigator.Data.InvestigatingSoundName and x == investigator.Data.InvestigatingSoundX and y == investigator.Data.InvestigatingSoundY and z == investigator.Data.InvestigatingSoundZ:
					# investigator is already investigating this sound
					return
				elif investigator.Data.IsSoundHigherPriority(investigator.Name, SoundName, Volume) and investigator.GetActionMode()!=ROUTE_CHASE and not investigator.InCombat:
					me.StartLooking(x, y, z)

					# Turn to face the sound
					if not Actions.IsFacingPos(EntityName, x, z):
						Actions.QuickTurnToFacePos(EntityName, x, z)


					# React to the sound, with alarm
					if investigator.Name != EntityName:
						# Tell investigator to turn to face the sound
						if not Actions.IsFacingPos(investigator.Name, x, z):
							Actions.QuickTurnToFacePos(investigator.Name, x, z)

						if (not investigator.Data.InvestigatingSound):
							if (me.AnimName[:4] != "hurt" and me.AnimName[:5] != "sleep"):
								if investigator.Data.CanGoTo(investigator.Name, x, y, z):
									me.Wuea=Reference.WUEA_ENDED
									me.SetTmpAnmFlags(1,0,1,0,1,1)
									me.LaunchAnmType("alarm01",1)

					# Send off fighter to investigate
					investigator.Data.InvestigatingSound = TRUE
					investigator.Data.InvestigatingSoundName = SoundName
					investigator.Data.InvestigatingSoundVolume = Volume
					investigator.Data.InvestigatingSoundX = x
					investigator.Data.InvestigatingSoundY = y
					investigator.Data.InvestigatingSoundZ = z

					if me.AnimName=="alarm01":
						if EntityName != investigator.Name:
							self.NextOrdersTo = []
							self.NextOrdersTo.append(investigator.Name)
							self.NextOrders = investigator.Data.StdInvestigateSound
							me.AnmEndedFunc=self.GiveOrders
						else:
							me.AnmEndedFunc=self.StdInvestigateSound
					else:
						if EntityName != investigator.Name:
							self.NextOrdersTo = []
							self.NextOrdersTo.append(investigator.Name)
							self.NextOrders = investigator.Data.StdInvestigateSound
							self.GiveOrders (EntityName)
						else:
							self.StdInvestigateSound (EntityName)
			# except TypeError,detail:
				# print "TypeError Exception",detail
				# pdb.set_trace()


	#
	# Aux funcs
	#

	def LaunchMyWatch(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life > 0:
			enemy=Bladex.GetEntity(me.GetEnemyName())
			if not enemy or not me.CanISee(enemy):
				me.StopLooking()

			#Just in case . This is the best place 4 this
			me.GoToJogging=0
			me.GoToSneaking=0

			me.LaunchWatch()


	def Turn180AndWatch(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		Actions.Turn180(EntityName)
		me.RouteEndedFunc=self.LaunchMyWatch

	def LaunchMyPatrol(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		me.StopLooking()

		init_pos=me.InitPos
		my_pos=me.Position
		x = init_pos[0] - my_pos[0]
		z = init_pos[2] - my_pos[2]
		DiscountDistance = 1000.0  #Used 2b 500
		if (not me.InsideActionArea(me.ActionAreaMin)) or (x*x+z*z)>(DiscountDistance*DiscountDistance):
			me.GoTo(init_pos[0],init_pos[1],init_pos[2])
			Reference.debugprint(EntityName+": Going 2 InitPos - self.LaunchMyPatrol")
			me.RouteEndedFunc=self.Turn180AndWatch
		else:
			Reference.debugprint(EntityName+": Not back2init cause quite close and inside MinAA")
			pass

	#
	# Standard function of what to do when the enemy is out of sight for some time
	#
	def StdDelayNoSeen(self,EntityName):
		##startmem = BDAux.GetAvailablePhysicalMemory()
		me = Bladex.GetEntity(EntityName)
		# Check I'm not dead
		if me.Life > 0:
			if (not self.Asleep) and (not me.Blind):
				##if BDAux.GetAvailablePhysicalMemory() != startmem:
				##	pdb.set_trace()

				if me.Aim or Actions.CurrentlyBowing(EntityName):
					me.Wuea=Reference.WUEA_ENDED
					Actions.EndBowMode(EntityName)
					me.SetOnFloor()

				Reference.debugprint(EntityName+": Im in StdDelayNoSeen")
				#self.SetGroupFormation (EntityName, TRUE, FALSE)
				##if BDAux.GetAvailablePhysicalMemory() != startmem:
				##	pdb.set_trace()

				me.StopLooking()
				enemy_name=me.GetEnemyName()
				##if BDAux.GetAvailablePhysicalMemory() != startmem:
				##	pdb.set_trace()

				enemy=Bladex.GetEntity(enemy_name)
				##if BDAux.GetAvailablePhysicalMemory() != startmem:
				##	pdb.set_trace()

				if me.GetActionMode() != ROUTE_CHASE:
					if me.GetActionMode() != ROUTE_SINGLE and me.GetActionMode() != ROUTE_BAY:
						##if BDAux.GetAvailablePhysicalMemory() != startmem:
						##	pdb.set_trace()

						Reference.debugprint(EntityName+": I am not chasing")
						self.LaunchMyPatrol(EntityName)
						##if BDAux.GetAvailablePhysicalMemory() != startmem:
						##	pdb.set_trace()

				else:
					Reference.debugprint(EntityName+": I am chasing")
					if me.AstarState<>ASTAR_SOLVED:
						# Face enemy as much as possible
						lastseenpos = me.EnemyLastSeen
						me.StartLooking(lastseenpos[0], lastseenpos[1], lastseenpos[2])
						##if BDAux.GetAvailablePhysicalMemory() != startmem:
						##	pdb.set_trace()

						if Actions.IsFacingPos(EntityName, lastseenpos[0], lastseenpos[2]):
							self.LaunchMyWatch (EntityName)
							##if BDAux.GetAvailablePhysicalMemory() != startmem:
							##	pdb.set_trace()

						else:
							Actions.TurnToFacePos(EntityName, lastseenpos[0], lastseenpos[2])
							me.RouteEndedFunc=self.LaunchMyWatch
							##if BDAux.GetAvailablePhysicalMemory() != startmem:
							##	pdb.set_trace()

		##if BDAux.GetAvailablePhysicalMemory() != startmem:
		##	pdb.set_trace()

	#
	# Alternate function if we've just ended a chase and the enemy is out of sight for some time
	#
	def EndChaseDelayNoSeen(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		Reference.debugprint(EntityName + ": Im in EndChaseDelayNoSeen!")
		# Check I'm not dead
		if me.Life > 0:
			me.DelayNoSeenFunc=self.StdDelayNoSeen
			self.StdDelayNoSeen(EntityName)
			if me.Data.imusic_noseen_warp==1:
				DMusic.RestoreMusicWarperDelayNoSeenFunc(EntityName)


	#
	# Standard function for entering a non allowed area (see the "Action Areas" thing)
	#
	def StdNoAllowedArea(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		Reference.debugprint(EntityName + ": Im entering non-allowed area!")
		back_area_min=me.ActionAreaMin
		back_area_max=me.ActionAreaMax
		me.ActionAreaMin=0
		me.ActionAreaMax=0
		init_pos=me.InitPos
		me.InvertedRoute=0
		if me.GoTo(init_pos[0],init_pos[1],init_pos[2]):
			me.ActionAreaMin=back_area_min
			me.ActionAreaMax=back_area_max


	#
	# Standard function for when the enemy BEING CHASED (imp!) enters a non allowed area
	#
	def StdEnemyNoAllowedArea(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		enemy=Bladex.GetEntity(me.GetEnemyName())

		if me.GetActionMode()<>ROUTE_CHASE:
			return

		init_pos=me.InitPos
		if (not me.InsideActionArea(me.ActionAreaMin)) and me.InsideActionArea(me.ActionAreaMax):
			me.InvertedRoute=1
		else:
			me.InvertedRoute=0
		me.GoTo(init_pos[0],init_pos[1],init_pos[2])
		Reference.debugprint(EntityName + ": My enemy has entered a non-allowed area")

	#
	# Standard function for taking injury
	#
	def StdImHurt(self,EntityName):
		Reference.debugprint(EntityName+": Oh! That hurt.")
		me = Bladex.GetEntity(EntityName)
		#
		# Rest of stuff
		#
		if self.NPC==0:
			return

		if self.Asleep:
			self.WakeMeUp(EntityName)

		#if me.GetActionMode() == ROUTE_WATCH:
		#	print "See due2 being hurt"
		#	me.SeeFunc(EntityName)


	#
	# Combat Group Functions
	#
	def GroupCoveringPoint (self, EntityName, x, y, z, include_me=TRUE):
		me = Bladex.GetEntity(EntityName)
		if me.CombatGroup:
			memberlist = me.GetGroupMembers()
			for member_name in memberlist:
				if include_me or member_name != EntityName:
					member = Bladex.GetEntity (member_name)
					if member.TestPosInOwnBox (x, y, z, 1.05):
						return TRUE
		elif include_me:
			return me.TestPosInOwnBox (x, y, z, 1.05)
		return FALSE

	def GetGroupLeader (self, EntityName):
		me = Bladex.GetEntity(EntityName)
		if me.CombatGroup:
			memberlist = me.GetGroupMembers()
			for member_name in memberlist:
				member = Bladex.GetEntity (member_name)
				if member and member.Life > 0 and member.Data.group_leader:
					return member
		return None

	def GetGroupFighter (self, EntityName):
		me = Bladex.GetEntity(EntityName)
		if me.CombatGroup:
			memberlist = me.GetGroupMembers()
			for member_name in memberlist:
				member = Bladex.GetEntity (member_name)
				if member and member.Life > 0 and member.Data.group_fighter:
					return member
		return None


	def CheckGoodGroupFormation(self,EntityName, include_me):
		me = Bladex.GetEntity(EntityName)

		if me.CombatGroup:
			memberlist = me.GetGroupMembers()
			if len(memberlist) > 1:
				fighter_found = None
				leader_found = None
				enemy=Bladex.GetEntity(me.GetEnemyName())
				for member_name in memberlist:
					if include_me or member_name != EntityName:
						member = Bladex.GetEntity (member_name)

						if (not leader_found) and member and member.Data.group_leader and member.Life > 0:
							if (not member.Data.group_fighter) and (not member.Data.Furious):
								member.CombatDistFlag = 1
							leader_found = member.Name
						else:
							member.Data.group_leader = FALSE

						if (not fighter_found) and member and member.Data.group_fighter and member.Life > 0 and enemy and member.CanISee(enemy):
							member.CombatDistFlag = 0
							fighter_found = member.Name
						else:
							if member.Data.group_fighter:
								if not member.Data.Furious:
									member.CombatDistFlag = 1
								member.Data.group_fighter = FALSE

				if fighter_found and leader_found and (fighter_found != leader_found):
					return

				# If we get to this point then we're either missing a group leader or a group fighter
				self.SetGroupFormation (EntityName, include_me, not leader_found)

			else:
				if include_me:
					self.group_leader= TRUE
					self.group_fighter= TRUE
					me.CombatDistFlag= 0
				return

	def CallGroupMemberFunc(self,EntityName, func, include_me):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life >0 and me.CombatGroup:
			memberlist = me.GetGroupMembers()
			if (not include_me) and memberlist.count(EntityName) > 0:
				memberlist.remove(EntityName)
			for member_name in memberlist:
				func (member_name)

	def SetNoGroupFighter(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me.CombatGroup:
			memberlist = me.GetGroupMembers()
			for member_name in memberlist:
				member = Bladex.GetEntity (member_name)
				if not member.Data.Furious:
					member.CombatDistFlag = 1
				member.Data.group_fighter = FALSE

	def SetNoGroupLeader(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me.CombatGroup:
			memberlist = me.GetGroupMembers()
			for member_name in memberlist:
				member = Bladex.GetEntity (member_name)
				member.Data.group_leader = FALSE

	def SetGroupFormation(self,EntityName, include_me, new_leader_needed):
		if new_leader_needed:
			self.SetGroupLeader (EntityName, include_me)
		self.SetGroupFighter (EntityName, include_me)

	def SetGroupFighter(self,EntityName, include_me):
		me = Bladex.GetEntity(EntityName)
		if me.CombatGroup:
			self.SetNoGroupFighter (EntityName)
			# Can I find someone else to go in close range
			memberlist = me.GetGroupMembers()
			if (not include_me) and memberlist.count(EntityName) > 0:
				memberlist.remove(EntityName)

			if len(memberlist) > 0:
				memberlist.sort(ChooseFighter)
				member = Bladex.GetEntity (memberlist[0])
				if member and member.Life > 0:
					member.CombatDistFlag = 0	# move in
					member.Data.group_fighter = TRUE

	def SetGroupLeader(self,EntityName, include_me):
		me = Bladex.GetEntity(EntityName)
		if me.CombatGroup:
			self.SetNoGroupLeader (EntityName)
			# Can I find someone else to go in close range
			memberlist = me.GetGroupMembers()
			if (not include_me) and memberlist.count(EntityName) > 0:
				memberlist.remove(EntityName)

			if len(memberlist) > 0:
				memberlist.sort(ChooseLeader)
				member = Bladex.GetEntity (memberlist[0])
				if member and member.Life>0:
					member.Data.group_leader = TRUE

	def Respond2Thrown(self, EntityName, AttackerName):
		me = Bladex.GetEntity(EntityName)
		if self.Asleep:
			self.WakeMeUp(EntityName)
		if AttackerName:
			enemy=Bladex.GetEntity(me.GetEnemyName())
			if enemy and not enemy.InsideActionArea(me.ActionAreaMax):
				self.LastThrownHurtTime=Bladex.GetTime()
				init_pos=me.InitPos
				me.InvertedRoute=0 #Just in case
				me.GoToJogging=1
				if me.GoTo(init_pos[0],init_pos[1],init_pos[2]):
					me.RouteEndedFunc= self.Turn180AndWatch
			else:
				if me.GetActionMode() == ROUTE_WATCH:
					#print "FIX?"
					Actions.QuickTurnToFaceEntity(EntityName,AttackerName)
				else:
					print "Respond2Thrown->Bug?"


	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		# launch appropriate hurt anim
		if self.Asleep:
			self.WakeMeUp(EntityName)

		Basic_Funcs.PlayerPerson.RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded)

		if AttackerName and AttackerName != 'BWorld' and AttackerName != EntityName:
			me = Bladex.GetEntity(EntityName)
			if me and me.Life > 0:
				# consider getting furious
				chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)
				if me.Life <= CharStats.GetCharMaxLife(me.Kind, me.Level)*0.25 and whrandom.random() < self.ChanceOfFuryOnHurt:
					self.GetFurious (EntityName)
				# consider attacking attacker back
				damage_factor = DamagePoints / (me.Life+DamagePoints)
				if damage_factor > me.Data.DamageFactorNone:
					# Only if I'm still alive... Death events handled apart
					if Shielded:
						Bladex.PlayHaptic(1)
					Reference.debugprint(EntityName+": Im being attacked by "+AttackerName)
					if AttackerName != me.GetEnemyName():
						Reference.debugprint(EntityName+": " + AttackerName +" is not my enemy!" )
						attacker = Bladex.GetEntity(AttackerName)
						if attacker and (self.AttacksOwnKind or attacker.Kind != me.Kind):
							Reference.debugprint(EntityName+": I will attack back")
							# Only attack NPCs if not already, otherwise we get multiple scheduled funcs
							if (not attacker.Data.NPC) or (not self.AttackingNPC):
								Reference.debugprint("attacker.Data.NPC: "+ `attacker.Data.NPC`+ ", self.AttackingNPC: " + `self.AttackingNPC`)
								# Interrupt whatever we were doing before
								Damage.DropInvalidObjectsOnImpact (EntityName)
								me.Wuea=Reference.WUEA_ENDED
								me.InterruptCombat()

								# Set up the new enemy, and start chasing him to be sure
								#print EntityName+": Starting attacking "+attacker.Name+" at time: "+`Bladex.GetTime()`
								me.SetEnemy(attacker)
								me.SetActiveEnemy(attacker)
								me.Chase(attacker, me.ActionAreaMax)
								if me.GetActionMode()==ROUTE_CHASE and self.IsArcher():
									self.Switch2MeleeWeapons(EntityName)


								#if not me.CanISee(attacker):
								#	me.Wuea=Reference.WUEA_ENDED
								#	me.LaunchAnmType("attack_look",1)

								# If its another NPC, we should make the switch from the PC temporary
								if attacker.Data.NPC:
									#pdb.set_trace()
									self.AttackingNPC=TRUE
									Bladex.AddScheduledFunc(Bladex.GetTime() + self.AttackNPCTime, self.StopNPCsAttacking,(EntityName,))
									if me.CombatGroup == attacker.CombatGroup:
										self.LeaveGroup (EntityName)
										self.CheckToJoin (EntityName)
										return
					if me.CombatGroup and self.group_fighter and me.Life > 0:	# I am in close range
						self.SetGroupFormation (EntityName, TRUE, FALSE)


	def HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, DirX, DirY, DirZ,wcx,wcy,wcz,wdx,wdy,wdz):
		me= Bladex.GetEntity(EntityName)
		if me and me.Life>0:
			if not me.InCombat:

				#x= pos[0]-DirX*1000.0
				#z= pos[2]-DirZ*1000.0

				weapon= Bladex.GetEntity (WeaponName)
				if weapon and weapon.Parent:
					if not Actions.IsFacingEntity(EntityName, weapon.Parent):
						Actions.QuickTurnToFaceEntity(EntityName, WeaponName)
				else:
					pos= me.Position
					x= pos[0]+(Cx-pos[0])*1000.0
					z= pos[2]+(Cz-pos[2])*1000.0
					if not Actions.IsFacingPos(EntityName, x, z):
						Actions.QuickTurnToFacePos(EntityName, x, z)

		Basic_Funcs.PlayerPerson.HitFunc (self, EntityName, WeaponName, Cx, Cy, Cz, DirX, DirY, DirZ,wcx,wcy,wcz,wdx,wdy,wdz)


	#
	# Standard function for dying
	#


	def StdImDead(self,EntityName):
		global TwinkleObjs
		Reference.debugprint(EntityName+": I died!")
		if self.Asleep:
			self.WakeMeUp(EntityName)
		Basic_Funcs.PlayerPerson.PCImDead(self, EntityName)

		me = Bladex.GetEntity(EntityName)
		if me.Life > 0:
			print EntityName + ': Warning! dead func when Life > 0!'
		try: 
			me.ExclusionGroup = EXG_MAGIC		# Exclude dead people from collision with inventory items -LeadHead
		except:
			print EntityName+" - could not assign exGroup"

		DMusic.InformDead(EntityName)

		me.RemoveFromList("Listeners")
		#pdb.set_trace()
		me.AddAnmEventFunc("UnlinkAll", self.UnlinkAll)
		if self.Asleep:
			me.Wuea=Reference.WUEA_ENDED
			me.LaunchAnmType("sleep_wall_d")
			Reference.debugprint(EntityName+": Uuurgh! I died in my sleep!")

		if self.group_leader:
			memberlist = me.GetGroupMembers()
			if EntityName in memberlist:
				memberlist.remove(EntityName)
			if len(memberlist) == 1:
				# Chance that remaining member gets furious
				#pdb.set_trace()
				member = Bladex.GetEntity(memberlist[0])
				if member and member.Life > 0:
					enemy=Bladex.GetEntity(member.GetEnemyName())
					if member.SQDistance2(enemy) > 3000*3000 or not Actions.IsFacingEntity(enemy.Name, member.Name):
						if whrandom.random() < self.ChanceOfFuryOnLeaderDeath:
							member.Data.GetFurious (member.Name)

		self.CheckGoodGroupFormation (EntityName, FALSE)
		self.CallGroupMemberFunc(EntityName, Combat.GetAngry, FALSE)

		me.RemoveFromList(me.CombatGroup)

		csound=Bladex.GetEntity(EntityName+"ContinuosSound")
		if csound:
			csound.StopSound()
			csound.SubscribeToList("Pin")
		
		"""
		### Added -LeadHead
		Adjusted inventory dropping
		Prevents dropped items from colliding with each other
		and limbs, thus less physics errors and disappearing items
		inv = me.GetInventory()
		weapons = []
		shields = []
		quivers = []
		objects = []
		for w in range (inv.nWeapons): weapons.append(inv.GetWeapon(w))
		for s in range (inv.nShields): shields.append(inv.GetShield(s))
		for q in range (inv.nQuivers): quivers.append(inv.GetQuiver(q))
		for o in range (inv.nObjects): objects.append(inv.GetObject(o))
		
		fullInv = weapons + shields + quivers + objects
		me.ExclusionGroup = EXG_MAGIC
		while fullInv:
			try:
				object = Bladex.GetEntity(fullInv[0])
				object.Alpha=1.0
				if object.Name == me.InvLeft:
					Actions.RemoveFromInventory (me, object,"DropLeftEvent")
					object.Impulse(0.0, 0.0, 0.0)
					object.ExclusionGroup = EXG_MAGIC		# Object has to be dropped first
					fullInv.remove(fullInv[0])
					continue
				if object.Name == me.InvRight:
					Actions.RemoveFromInventory (me, object,"DropRightEvent")
					object.Impulse(0.0, 0.0, 0.0)
					object.ExclusionGroup = EXG_MAGIC		# Object has to be dropped first
					fullInv.remove(fullInv[0])
					continue
				else:
					object.Position = me.Position
					me.Unlink(object)
					inv.RemoveObject(object_name)
					object.ExclusionGroup = EXG_MAGIC
					if object.Kind in TwinkleObjs:
						Bladex.AddScheduledFunc(Bladex.GetTime(), Actions.TakeObject,("Player1",object_name))
						continue
					else:
						fuckthisstupidcrap
				"""

		# Drop the weapons if possible
		inv = me.GetInventory()
		x,y,z = me.Rel2AbsPoint(0.0, 0.0, 0.0)
		
		try:
			object = Bladex.GetEntity(me.InvLeft)
			if me.InvLeft and object:
				Actions.RemoveFromInventory (me, object,"DropLeftEvent")
				if object.Solid:
					object.ExclusionGroup=EXG_MAGIC  ## Added -LeadHead
				object.Alpha=1.0
				if object.TestHit:
					# imp = object.Mass * 3000
					object.Position=x-200.0,y,z+300.0
				object.Impulse(0.0, 0.0, 0.0)
		except AttributeError:
			pass
			#pdb.set_trace()

		try:
			object = Bladex.GetEntity(me.InvRight)
			if me.InvRight and object: # and not object.TestHit:
				Actions.RemoveFromInventory (me, object,"DropRightEvent")
				if object.Solid:
					object.ExclusionGroup=EXG_MAGIC  ## Added -LeadHead
				object.Alpha=1.0
				if object.TestHit:
					# imp = object.Mass * 3000
					object.Position=x+200.0,y,z+300.0
				object.Impulse(0.0, 0.0, 0.0)
		except AttributeError:
			pass
			#pdb.set_trace()

		try:		## Added, drop items on back without moving them -LeadHead
			object = Bladex.GetEntity(me.InvLeftBack)
			if me.InvLeftBack and object: # and not object.TestHit:
				Actions.RemoveFromInventory (me, object,"DropEvent")
				inv.LinkLeftBack("")
				if object.Solid:
					object.ExclusionGroup=EXG_MAGIC 
				object.Alpha=1.0
				object.Impulse(0.0, 0.0, 0.0)
		except AttributeError:
			pass
			
		try:
			object = Bladex.GetEntity(me.InvRightBack)
			if me.InvRightBack and object: # and not object.TestHit:
				Actions.RemoveFromInventory (me, object,"DropEvent")
				inv.LinkRightBack("")
				if object.Solid:
					object.ExclusionGroup=EXG_MAGIC 
				object.Alpha=1.0
				object.Impulse(0.0, 0.0, 0.0)
		except AttributeError:
			pass

		# Drop everything else
		#pdb.set_trace()
		while inv.nObjects > 0:
			object_name = inv.GetObject(0)
			object = Bladex.GetEntity(object_name)
			if object:
				object.Position=me.Position
				me.Unlink(object)
				inv.RemoveObject(object_name)
				object.ExcludeHitFor(me)
				try:
					object.ExclusionGroup=1  ## Added -LeadHead
				except AttributeError:
					print object.Name+": unsupported Attribute"
				if object.Kind in TwinkleObjs:
					Bladex.AddScheduledFunc(Bladex.GetTime(), Actions.TakeObject,("Player1",object_name))
				else:
					if object.TestHit:
						print "WARNING OBJECT "+object.Name+" REMOVED FROM WORLD BECAUSE COLLIDING"
						# object.RemoveFromWorld()
					# else:
					object.Alpha=1.0
					object.Impulse(0.0, 0.0, 0.0)

		while inv.nWeapons > 0:
			object_name = inv.GetWeapon(0)
			object = Bladex.GetEntity(object_name)
			if object:
				object.Position=me.Position
				me.Unlink(object)
				inv.RemoveWeapon(object_name)
				object.ExclusionGroup=EXG_MAGIC  ## Added -LeadHead
				object.ExcludeHitFor(me)
				try:
					if object.TestHit:
						print "WARNING OBJECT "+object.Name+" REMOVED FROM WORLD BECAUSE COLLIDING"
						# object.RemoveFromWorld()
					# else:
					object.Alpha=1.0
					object.Impulse(0.0, 0.0, 0.0)
				except AttributeError:
					print "TestHit unsupported for object "+object.Name
					#pdb.set_trace()

		while inv.nShields > 0:
			object_name = inv.GetShield(0)
			object = Bladex.GetEntity(object_name)
			if object:
				object.Position=me.Position
				me.Unlink(object)
				inv.RemoveShield(object_name)
				object.ExclusionGroup=EXG_MAGIC  ## Added -LeadHead
				object.ExcludeHitFor(me)
				if object.TestHit:
					print "WARNING OBJECT "+object.Name+" REMOVED FROM WORLD BECAUSE COLLIDING"
					# object.RemoveFromWorld()
				# else:
				object.Alpha=1.0
				object.Impulse(0.0, 0.0, 0.0)

		while inv.nQuivers > 0:
			object_name = inv.GetQuiver(0)
			object = Bladex.GetEntity(object_name)
			if object:
				object.Position=me.Position
				me.Unlink(object)
				inv.RemoveQuiver(object_name)
				if object.Solid:
					object.ExclusionGroup=EXG_MAGIC  ## Added -LeadHead
				object.ExcludeHitFor(me)
				if object.TestHit:
					print "WARNING OBJECT "+object.Name+" REMOVED FROM WORLD BECAUSE COLLIDING"
					# object.RemoveFromWorld()
				# else:
				object.Alpha=1.0
				object.Impulse(0.0, 0.0, 0.0)

		while inv.nKeys > 0:
			object_name = inv.GetKey(0)
			object = Bladex.GetEntity(object_name)
			if object:
				object.Position=me.Position
				me.Unlink(object)
				inv.RemoveKey(object_name)
				object.ExclusionGroup=EXG_MAGIC  ## Added -LeadHead
				object.ExcludeHitFor(me)
				Bladex.AddScheduledFunc(Bladex.GetTime(), Actions.TakeObject,("Player1",object_name))

				char = Bladex.GetEntity("Player1")
				new_key_sound.Stop()
				new_key_sound.PlayStereo()
				import Scorer
				Scorer.NewObjectAtInventory(object_name)
				#new_key_sound.Play(char.Position[0],char.Position[1],char.Position[2],0);



	#
	# Standard function for the enemies' death
	#
	def StdEnemyDead(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		print "EntityName, enemy "+me.GetEnemyName()+" dead"
		# Check I'm not dead
		if me:
			if me.Life > 0:
				me.ResetChase()
				if me.GetEnemyName()!="Player1":
					self.AttackingNPC=1
					self.StopAttackingNPC(EntityName)

				if me.GetActionMode()==ROUTE_CHASE or me.InCombat:
					me.DelayNoSeenFunc=self.StdDelayNoSeen
					if me.Data.imusic_noseen_warp==1:
						DMusic.RestoreMusicWarperDelayNoSeenFunc(EntityName)

					self.InvestigatingSound = FALSE
					self.LaunchMyWatch(EntityName)
					Reference.debugprint(EntityName+": My enemy is dead.He he ! - py")


	def GetFurious (self, EntityName):
		me=Bladex.GetEntity(EntityName)

		if me and self.Furious == 0:
			Reference.debugprint(EntityName + ": Getting Furious")
			self.Furious = 1
			me.BlockingPropensity = 0

			# Save the first attack
			movelist = me.AttackList
			first_attack = None
			for move in movelist:
				if move[0]==Combat.ATTACK:
					first_attack = move
					break
			me.AttackList=filter(Combat.DoneInFury,me.AttackList)
			if first_attack:
				first_attack[1]=1.00
				me.AttackList.insert(0, first_attack)

			me.CombatDistFlag = 0
			Damage.DropInvalidObjectsOnImpact (EntityName)
			me.Wuea=Reference.WUEA_ENDED
			me.InterruptCombat()
			me.LaunchAnmType("fury",1)
			FuryTime=30.0
			Bladex.AddScheduledFunc(Bladex.GetTime() + FuryTime, self.ResetCombat,(EntityName,))

	#
	# Standard function for end of animation
	# It is set to null when finish!
	#
	def StdAnmEnded(self,EntityName):
		pass
		Reference.debugprint(EntityName+": Anm ended - py ")

	#
	# Standard function for entering close range combat
	# Called only when CHASING an enemy !
	#
	def StdEnterClose(self,EntityName):
		Reference.debugprint(EntityName+": I am entering close combat")
		#pdb.set_trace()
		me = Bladex.GetEntity(EntityName)
		# Check I'm not dead
		if me and me.Life > 0:
			self.SetGroupFormation (EntityName, TRUE, FALSE)
			self.Switch2MeleeWeapons (EntityName)


	def Switch2MeleeWeapons(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		if me and me.Life > 0 and not me.RangeActive:
			inv= me.GetInventory()
			right_type= Reference.GiveObjectFlag(me.InvRight)

			# Do we have an item in the hand we can fight with
			if inv.HoldingBow or not (right_type== Reference.OBJ_STANDARD or right_type== Reference.OBJ_WEAPON):
				# Don't change if the enemy is unreachable
				enemy=Bladex.GetEntity(me.GetEnemyName())
				if me.AstarState!=ASTAR_NOSOLVED:
					me.SwitchTo1H()
					weapon_name= inv.GetSelectedWeapon()
					if weapon_name and (weapon_name != me.InvRight and weapon_name != me.InvLeft):
						# Launch the swap weapons animation
						out= ScorerActions.CB_WeaponOutX(EntityName,0)
						if not out:
							me.AnmEndedFunc= ScorerActions.CB_WeaponOutX
						Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, self.Switch2MeleeWeapons,(EntityName,),EntityName+"ReSwitch2MeleeWeapons")

					Actions.EndBowMode(EntityName)

	def WeaponsOut(self,EntityName):
		me= Bladex.GetEntity(EntityName)
		if me.Life > 0:
			inv= me.GetInventory()
			if inv.HasBow:
				# Put quiver on back
				des_quiver_name=inv.GetSelectedQuiver()
				if des_quiver_name:
					inv.LinkBack(des_quiver_name)

					# Put arrow in right
					inv.LinkRightHand("None")
					quiver=	Bladex.GetEntity(des_quiver_name)
					if quiver and quiver.Data.NumberOfArrows() > 0:
						arrow= quiver.Data.GiveArrow ()
						inv.LinkRightHand(arrow.Name)

						# Put bow in left
						bow= inv.GetBow()
						inv.LinkLeftHand(bow)

						return

				print "Enemy starting with bow, but without quiver/arrows"

			# Put sword in right
			if inv.nWeapons>0 and not me.InvRight:
				weapon_name= inv.GetSelectedWeapon()
				if not weapon_name:
					weapon_name= inv.GetWeapon(0)
				inv.LinkRightHand("None")
				inv.LinkRightHand(weapon_name)

			# Put shield in left
			if inv.nShields>0 and not me.InvLeft:
				shield_name= inv.GetSelectedShield()
				if not shield_name:
					shield_name= inv.GetShield(0)
				if shield_name and shield_name!=inv.GetMagicShield():
					inv.LinkLeftHand("None")
					inv.LinkLeftHand(shield_name)


	#
	# Standard function for entering large range combat
	# Called only when CHASING an enemy !
	#
	def StdEnterLarge(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		# Check I'm not dead
		Reference.debugprint(EntityName + ": Im entering large area!")
		if me.Life > 0 and not me.MeleeActive:
			inv= me.GetInventory()
			if inv.HasBow:
				left_type= Reference.GiveObjectFlag(me.InvLeft)
				if left_type != Reference.OBJ_BOW:
					me.SwitchToBow()
					if inv.GetSelectedWeapon() != me.InvRight and inv.GetSelectedWeapon() != me.InvLeft:
						# Launch the swap weapons animation
						out= ScorerActions.CB_WeaponOutX(EntityName,0)
						if not out:
							me.AnmEndedFunc= ScorerActions.CB_WeaponOutX
						Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, self.StdEnterLarge,(EntityName,),EntityName+"ReStdEnterLarge")

	#
	# Standard function for entering PRIMARY AA
	#
	def StdEnterPrimaryAA(self,EntityName):
		me = Bladex.GetEntity(EntityName)
		Reference.debugprint(EntityName + ": Im entering primary area!")
		# Check I'm not dead
		if me.Life > 0:
			#NO -> Only called onlled once this function(...) !!!
			#if me.InvertedRoute==1 and not me.Will1aaTo2aa:
			if me.InvertedRoute==1:
				self.LaunchMyWatch (EntityName)
				me.LastTimeSeen=Bladex.GetTime()
			me.InvertedRoute=0 #Por si acaso


	#
	# Standard function for entering SECONDARY AA
	#
	def StdEnterSecondaryAA(self,EntityName):
		Reference.debugprint(EntityName + ": Im entering secondary area!")
		#print "StdEnterSecondaryAA"
		pass


	#
	# Standard function for when another character sees his enemy
	# (...)
	#
	def StdCharSeeingEnemy(self,EntityName,EntityName2):
		me = Bladex.GetEntity(EntityName)
		ally=Bladex.GetEntity(EntityName2)

		if me.CombatGroup==ally.CombatGroup:
			pass #Bob's grouping suff will do it
		# Check I'm not dead
		if me.Life > 0:
			#Reference.debugprint(EntityName + ": Im in StdCharSeeingEnemy with Char being " + EntityName2)

			if ally and me.CanISee(ally) and me.GetActionMode()<>ROUTE_CHASE:
				if ally.GetActionMode()==ROUTE_CHASE and me.GetActionMode()<>ROUTE_CHASE:
					me.SeeFunc(EntityName)
				if ally.GetActionMode()==ROUTE_SINGLE and ally.Data.InvestigatingSound:
					#Volume set to 1 , so he�ll always hear it
					self.StdHearFunc(EntityName,ally.Data.InvestigatingSoundName,ally.Data.InvestigatingSoundX,ally.Data.InvestigatingSoundY,ally.Data.InvestigatingSoundZ,1.0)

			else:
				pass
				#Reference.debugprint(EntityName + ": I cannot see ally")

	#
	# Standard function for enggling on and off with an enemy
	# (...)
	#
	def StdToggleCombat(self,EntityName):
		import DMusic
		if self.NPC==1:
			DMusic.notifyCombat(EntityName)

	# Functions for loading and saving state
	def __save_core_funcs__(self):
		me = Bladex.GetEntity(self.Name)
		if not me:
			print "__save_core_funcs__() Warning: trying to save a non existent entity",self.Name
			return

		core_funcs = []
		j = 0
		funcs=[ ("SeeFunc",               self.StdSeeTheEnemy),
				("HearFunc",              self.StdHearFunc),
				("DelayNoSeenFunc",       self.StdDelayNoSeen),
				("NoAllowedAreaFunc",     self.StdNoAllowedArea),
				("EnemyNoAllowedAreaFunc",self.StdEnemyNoAllowedArea),
				("ImHurtFunc",            self.StdImHurt),
				("ImDeadFunc",            self.StdImDead),
				("EnemyDeadFunc",         self.StdEnemyDead),
				("AnmEndedFunc",          self.StdAnmEnded),
				("EnterCloseFunc",        self.StdEnterClose),
				("EnterLargeFunc",        self.StdEnterLarge),
				("EnterPrimaryAAFunc",    self.StdEnterPrimaryAA),
				("EnterSecondaryAAFunc",  self.StdEnterSecondaryAA),
				("CharSeeingEnemyFunc",   self.StdCharSeeingEnemy),
				("ToggleCombatFunc",      self.StdToggleCombat)]

		for i in funcs:
			exec('f = me.'+i[0])
			if (i[1] <> f):
				#print "Save Core Func para",me.Name," callback ",i[0]," funcion ", f
				core_funcs.append((j,GameStateAux.SaveFunctionAux(f)))
			j = j + 1

		return(core_funcs)

	def __load_core_funcs__(self,param):
		me = Bladex.GetEntity(self.Name)
		if not me:
			print "__load_core_funcs__ -> Warning, trying to get a non existent entity",self.Name
			return

		funcs=[ "SeeFunc",
				"HearFunc",
				"DelayNoSeenFunc",
				"NoAllowedAreaFunc",
				"EnemyNoAllowedAreaFunc",
				"ImHurtFunc",
				"ImDeadFunc",
				"EnemyDeadFunc",
				"AnmEndedFunc",
				"EnterCloseFunc",
				"EnterLargeFunc",
				"EnterPrimaryAAFunc",
				"EnterSecondaryAAFunc",
				"CharSeeingEnemyFunc",
				"ToggleCombatFunc"]

		for i in param:
			# try:
			#print "Load Core Func ",i[1]," para ",me.Name," funcion ",funcs[i[0]]
			try:
				GameStateAux.LoadFunctionAux(i[1],me,funcs[i[0]])
				#print "Loaded for entity"
			except:
				GameStateAux.LoadFunctionAux(i[1],self,funcs[i[0]])
				#assign_func=eval("obj."+method_name)
				exec("me.%s=self.%s"%(funcs[i[0]],funcs[i[0]]))
				#print "Loaded for class"
			# except Exception,exc:
				# print "Exception in __load_core_funcs__ par ",me.Name,funcs[i[0]],i[1]
				# print "Exception is",exc
				# print i

	def __getstate__(self):
		# Tiene que devolver c�mo poder guardar el estado de la clase
		PlayerPerson_state=Basic_Funcs.PlayerPerson.__getstate__(self)
		if(PlayerPerson_state[0]!=1):
			print "ERROR: NPCPerson.__getstate__(): Base class version differs."
			# Throw?
			return playerperson_state
		me=Bladex.GetEntity(self.Name)
		PlayerPerson_state[1]["NPCPerson"]=(self.InvestigatingSound,
									  self.SoundPriorities,
									  self.Asleep,
									  self.SleepYOffset,
									  self.group_fighter,
									  self.group_leader,
									  self.AttackingNPC,
									  self.last_insulting_time_1AA,
									  self.LastThrownHurtTime,
									  self.AttacksOwnKind,
									  self.AttackNPCTime,
									  self.Angry,
									  self.Furious,
									  self.ChanceOfFuryOnHurt,
									  self.ChanceOfFuryOnLeaderDeath,
									  self.ImpatientAttackTime,
									  self.goto_limit2aa,
									  self.imusic_noseen_warp,
									  self.DelayNoSeenFuncMusicBackUp,
									  me.CombatGroup,
									  self.__save_core_funcs__()
									  )
		return PlayerPerson_state

	def __setstate__(self,parm):
		# Toma como par�metro lo que devuelve __getstate__() y debe recrear la clase
		Basic_Funcs.PlayerPerson.__setstate__(self,parm)

		me=Bladex.GetEntity(self.Name)
		#_________________________________________#
		# Set up the core functions               #
		#_________________________________________#
		me.SeeFunc=self.StdSeeTheEnemy
		me.HearFunc=self.StdHearFunc
		me.DelayNoSeenFunc=self.StdDelayNoSeen
		me.NoAllowedAreaFunc=self.StdNoAllowedArea
		me.EnemyNoAllowedAreaFunc=self.StdEnemyNoAllowedArea
		me.ImHurtFunc=self.StdImHurt
		me.ImDeadFunc=self.StdImDead
		me.EnemyDeadFunc=self.StdEnemyDead
		me.AnmEndedFunc=self.StdAnmEnded
		me.EnterCloseFunc=self.StdEnterClose
		me.EnterLargeFunc=self.StdEnterLarge
		me.EnterPrimaryAAFunc=self.StdEnterPrimaryAA
		me.EnterSecondaryAAFunc=self.StdEnterSecondaryAA
		me.CharSeeingEnemyFunc=self.StdCharSeeingEnemy
		me.ToggleCombatFunc=self.StdToggleCombat

		self.inheritance = 1

		version=parm[0]
		if version==1:
			parms=parm[1]["NPCPerson"]
			self.InvestigatingSound=parms[0]
			self.SoundPriorities=parms[1]
			self.Asleep=parms[2]
			self.SleepYOffset=parms[3]
			self.group_fighter=parms[4]
			self.group_leader=parms[5]
			self.AttackingNPC=parms[6]
			self.last_insulting_time_1AA=parms[7]
			self.LastThrownHurtTime=parms[8]
			self.AttacksOwnKind=parms[9]
			self.AttackNPCTime=parms[10]
			self.Angry=parms[11]
			self.Furious=parms[12]
			self.ChanceOfFuryOnHurt=parms[13]
			self.ChanceOfFuryOnLeaderDeath=parms[14]
			self.ImpatientAttackTime=parms[15]
			self.goto_limit2aa=parms[16]
			self.imusic_noseen_warp=parms[17]
			self.DelayNoSeenFuncMusicBackUp=parms[18]
			me.CombatGroup=parms[19]
			self.__load_core_funcs__(parms[20])
		self.ResetCombat(self.Name)
		AddMyWatchAnims(self.Name)
		me=Bladex.GetEntity(self.Name)

		#Revisar estas 3, deber�an estar con las propiedades de la entidad.
		#me.BlockingPropensity = 0.5
		#me.AttackList = []
		me.CombatDistFlag = not self.group_fighter
		self.NoFXOnHit= FALSE
		self.WeaponsOut(self.Name)


def AddMyWatchAnims(EntityName):
	Reference.debugprint(EntityName + " adding WatchAnims")
	me = Bladex.GetEntity(EntityName)
	#me.AddWatchAnim("PATROL_LOOK_D")
	#me.AddWatchAnim("PATROL_LOOK_U")
	#me.AddWatchAnim("PATROL_LOOK_R")
	#me.AddWatchAnim("PATROL_LOOK_L")


##############################################################
#	Clase base para caracteres estupidos, en principio       #
##############################################################

#Nota: Se ira ampliando a medida que haga falta

class StupidNPCPerson (Basic_Funcs.PlayerPerson):

	InvestigatingSound = FALSE
	SoundPriorities = [-1.0, -1.0, -1.0, -1.0, -1.0]

	def __init__(self, me):
		Basic_Funcs.PlayerPerson.__init__(self, me)

		self.SoundPriorities = [-1.0, -1.0, -1.0, -1.0, -1.0]
		###############################
		#  Record some personal data  #
		###############################

		self.NPC = 1

		# self.Asleep = FALSE
		# self.SleepYOffset = 1100.0		# this may need adjusting for non-knight chars

		#####################
		#  Initialise core  #
		#####################

		me.SubscribeToList("Listeners")
		me.Deaf = 0

	def RespondToHit(self, EntityName, AttackerName, DamagePoints, DamageType, DamageZone, Shielded):
		pass

		###############################
		#  Set up the core functions  #
		###############################

#		me.SeeFunc=self.StdSeeTheEnemy
#		me.HearFunc=self.StdHearFunc
#		me.DelayNoSeenFunc=self.StdDelayNoSeen
#		me.NoAllowedAreaFunc=self.StdNoAllowedArea
#		me.EnemyNoAllowedAreaFunc=self.StdEnemyNoAllowedArea
#		me.ImHurtFunc=self.StdImHurt
#		me.ImDeadFunc=self.StdImDead
#		me.EnemyDeadFunc=self.StdEnemyDead
#		me.AnmEndedFunc=self.StdAnmEnded
#		me.EnterCloseFunc=self.StdEnterClose
#		me.EnterLargeFunc=self.StdEnterLarge
#		me.CharSeeingEnemyFunc=self.StdCharSeeingEnemy


	##########################
	#  Define our functions  #
	##########################
