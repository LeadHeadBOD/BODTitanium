##///
##||| Combat.PY TITANIUM
##||| Change list:
##||| * Added LavaGolemAttackData
##\\\ 

 # General Combat Logic for enemies
import Bladex
import Actions
import pdb
import Reference
import CharStats


"""
bow attack? --- return
|no
--- WUEA? --- return
    |no
	--- in pause? --- return
	    |no
	    --- start pause? --- return
		    |no
			--- CheckFullAttack? -- dodge
"""
# Combat Moves
ATTACK=0     # Melee attack
BLOCK=1      # Block
DODGE=2      # Dodge
MOVE=3       # Positional Move
RANGE=4      # Range Attack
ATTACKDOWN=5 # Melee attack for stairs

"""
Predefined moves &  sequences
=============================

Blocks and Moves
================
"tr" -- Turn (Strafe) Right
"tl" -- Turn (Strafe) Left
"tb" -- Turn (Strafe) to move behind
"tf" -- Turn (Strafe) to face in front

Dodges
======
"d_r" -- Dodge Right
"d_l" -- Dodge Left
"d_b" -- Dodge Back

Attack Sequences
================
Use () to desgnate a combo sequence, with a comma seperated set of strings inside 
referring to atttack sets / meta-attacks.

Special Attack "RespectDistance"

Python Functions
================
If a python function is given, it will expect 1 argument, the entity name, and
should return a boolean specifying whether the action it describes has been 
succesfully performed. If no return value is given, it defaults to true.


"""

# return to the default range, for use as a reset function after a temporary move in...
def MoveBackProc (EntityName):
	me=Bladex.GetEntity(EntityName)
	if me and me.Life>0 and me.CombatGroup:				
		if len(me.GetGroupMembers()) > 1 and not me.Data.group_fighter:
			me.CombatDistFlag= 1
		else:
			me.CombatDistFlag= 0


# If an opening can be seen, move in for a temporary attack.
def TempMoveInProc (EntityName):
	# temporarily move in for close range attacks
	me=Bladex.GetEntity(EntityName)
	MoveInTime= 6.0 # seconds
	if me and me.Life>0 and me.CombatDistFlag==1 and me.ActiveEnemy:
		enemy= Bladex.GetEntity(me.ActiveEnemy)
		time= Bladex.GetTime()
		if Actions.StatR(me.ActiveEnemy) <> Actions.RA_1H_WEAPON or Actions.IsBehindEntity (EntityName, me.ActiveEnemy) or ((time-enemy.LastAttackTime)>me.Data.ImpatientAttackTime):
			me.CombatDistFlag= 0
			Bladex.AddScheduledFunc(Bladex.GetTime() + MoveInTime, MoveBackProc,(EntityName,))
			return 1
	return 0

def FearFire (EntityName):
	me=Bladex.GetEntity(EntityName)
	FearTime= 3.0 # seconds
	if me and me.Life>0 and me.CombatDistFlag==0 and me.ActiveEnemy and Actions.has_torch(me.ActiveEnemy) and not Actions.IsBehindEntity(EntityName, me.ActiveEnemy):	
		me.CombatDistFlag= 1
		Bladex.AddScheduledFunc(Bladex.GetTime() + FearTime, MoveBackProc,(EntityName,))
		return 1
	return 0
		

def TempMoveOutProc (EntityName):
	# temporarily move away from close range attacks
	me=Bladex.GetEntity(EntityName)
	MoveOutTime= 12.0 # seconds
	if me and me.Life>0 and me.CombatDistFlag==0 and me.ActiveEnemy:
		me.CombatDistFlag= 1
		Bladex.AddScheduledFunc(Bladex.GetTime() + MoveOutTime, MoveBackProc,(EntityName,))
		return 1
	return 0


# Launch laugh animation if we have one, but don't all laugh at the same time
def Laugh (EntityName):
	me=Bladex.GetEntity(EntityName)
	if me and me.Life>0 and me.CombatGroup:
		memberlist = me.GetGroupMembers()
		for member_name in memberlist:
			member = Bladex.GetEntity(member_name)
			if member and member.Life > 0:
				if member.AnimName == "laugh":
					return 0
	me.Wuea=Reference.WUEA_ENDED
	me.LaunchAnmType("laugh")
	return me.AnimName=="laugh"

# Launch insult animation if we have one, but don't all insult at the same time	
def Insult (EntityName):
	me=Bladex.GetEntity(EntityName)
	if me and me.Life>0 and me.CombatGroup:
		memberlist = me.GetGroupMembers()
		for member_name in memberlist:
			member = Bladex.GetEntity(member_name)
			if member and member.Life > 0:
				if member.AnimName == "insult":
					return 0
	me.Wuea=Reference.WUEA_ENDED
	me.LaunchAnmType("insult")
	if me.AnimName=="insult":
		Actions.UnGraspString(EntityName,"InsultUngrasp")
		return 1

	return 0

# Launch relax animation if we have one, but don't all relax at the same time	
def Relax (EntityName):
	me=Bladex.GetEntity(EntityName)
	if me and me.Life>0 and me.CombatGroup:
		memberlist = me.GetGroupMembers()
		for member_name in memberlist:
			member = Bladex.GetEntity(member_name)
			if member and member.Life > 0:
				if member.AnimName == "rlx_f":
					return 0
	me.Wuea=Reference.WUEA_ENDED
	me.LaunchAnmType("rlx_f")	
	if me.AnimName=="rlx_f":
		Actions.UnGraspString(EntityName,"InsultUngrasp")
		me.Gof=0
		me.Gob=0
		return 1
		
	return 0

# for stripping away certain moves when angry, add checks here
def DoneInAnger (move):
	if move[2] == Laugh:
		return 0
	if move[2] == Insult:
		return 0
	return 1

# for stripping away certain moves when furious, add checks here, extra to above
def DoneInFury (move):
	if not DoneInAnger (move):
		return 0
	if move[0] == BLOCK:
		return 0
	if move[0] == DODGE:
		return 0
	if move[0] == ATTACK:
		return 0
	return 1

def GetAngry (EntityName):
	me=Bladex.GetEntity(EntityName)
	me.BlockingPropensity = 0
	me.AttackList=filter(DoneInAnger,me.AttackList)
	me.Data.Angry = 1
	return 1

def GetFurious (EntityName):
	me=Bladex.GetEntity(EntityName)
	if me.Data.Furious == 0:
		me.Data.GetFurious (EntityName)
		return 1
	return 0

def GiveOrders (EntityName):
	me=Bladex.GetEntity(EntityName)
	if me and me.Life>0 and me.Data.group_leader and me.CombatDistFlag == 1 and me.CombatGroup:				
		if len(me.GetGroupMembers()) > 1:
			me.LaunchAnmType("order")
			# Kinds of orders
			# Go berserk / Fury
			#me.Data.CallGroupMemberFunc(EntityName, GetFurious, 0)
			# Move In
			me.Data.CallGroupMemberFunc(EntityName, TempMoveInProc, 0)
			return 1
	return 0


# Use a potion in combat if we have one, and our life is low
def UsePotion (EntityName):
	import pocimac
	me=Bladex.GetEntity(EntityName)	
	if me and me.Life >0:
		
		inv = me.GetInventory()
		for x in range (inv.nObjects):
			item_name = inv.GetObject(x)
			item = Bladex.GetEntity(item_name)
			if item.Data and item.Data.__class__==pocimac.Pocima:
				max_life= CharStats.GetCharMaxLife(me.Kind, me.Level)
				if (me.Life <= max_life/4.0) or (item.Data.Increment and me.Life+item.Data.Increment<=max_life):
					# we have found a potion, I hope its the life giving one...
					me.Data.obj_used=item
					item.Data.UsedBy = EntityName
					item.UseFunc(item_name, Actions.USE_FROM_INV)
					return 1
					
		
			
	return 0
	
def SetCombatMoveProbability(MoveType, Probability, List):
	if List:
		tot=0.0
		for move in List:
			if move[0]==MoveType:
				tot= tot+move[1]		
		if tot != Probability:
			for move in List:
				if move[0]==MoveType:
					move[1]= (move[1]/tot) * Probability

def GetMoveMinDist (MoveType, DesMove, List):
	if List:
		for move in List:
			if move[0]==MoveType and move[2]==DesMove:
				return move[3]
	raise TypeError, 'Move not found'

def GetMoveAveDist (MoveType, DesMove, List):
	if List:
		for move in List:
			if move[0]==MoveType and move[2]==DesMove:
				return move[4]
	raise TypeError, 'Move not found'

def GetMoveMaxDist (MoveType, DesMove, List):
	if List:
		for move in List:
			if move[0]==MoveType and move[2]==DesMove:
				return move[5]
	raise TypeError, 'Move not found'

		
def MagicShield (EntityName):
	#pdb.set_trace()
	me= Bladex.GetEntity(EntityName)
	if me and me.Life>0:
		me.Data.MagicShield (EntityName)
		return 1
	return 0

def Disappear (EntityName):
	me= Bladex.GetEntity(EntityName)
	if me and me.Life>0:
		return me.Data.Disappear (EntityName)
	return 0

def LaunchFireBall (EntityName):
	me= Bladex.GetEntity(EntityName)
	if me and me.Life>0:
		return me.Data.LaunchFireBall (EntityName)
	return 0

def LaunchMissile (EntityName):
	me= Bladex.GetEntity(EntityName)
	if me and me.Life>0:
		return me.Data.LaunchMissile (EntityName)
	return 0

def LaunchWeapon (EntityName):
	me= Bladex.GetEntity(EntityName)
	if me and me.Life>0:
		return me.Data.LaunchWeapon (EntityName)
	return 0

def KeepDistance (EntityName):
	me= Bladex.GetEntity(EntityName)
	return me.AnimName!="rlx"
	

#           Type    Weight  Move                  MinD  BestD  MaxD     Time (s [Interruptable])
################################################################################
TraitorKnightAttackData = [
           # inner zone blocks:
            [BLOCK,  0.08, (),                   500.0, 1000.0, 3000.0, 0.35],
            [BLOCK,  0.05, "tr",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tl",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tb",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.20, "tf",                 750.0, 1500.0, 3500.0, 0.50],

           # outer zone blocks:
            [BLOCK,  0.05, "tr",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.05, "tl",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.35, "tb",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.10, "tf",                3500.0, 7000.0, 9000.0, 0.50],

           # dodges:
            [DODGE,  0.25, "d_r",                500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.25, "d_l",                500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.00, "d_b",                500.0, 1200.0, 2800.0, 0.35],

           # attacks:
        [ATTACKDOWN, 0.90, ("STAIRS",),         1200.0, 1400.0, 2500.0, 0.35],

            [ATTACK, 0.00, ("GA","GA","GA","GM1",), 1200.0, 1400.0, 2500.0, 0.35],
            [ATTACK, 0.60, ("GA",),                0.0, 1400.0, 2500.0, 0.35],
            [ATTACK, 0.40, ("GA", "GA"),        1200.0, 1600.0, 2500.0, 0.35],
            [ATTACK, 0.10, ("GA", "GA", "GM1"),    0.0, 1600.0, 2500.0, 0.35],
            [ATTACK, 0.25, ("GM2",),            1200.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 0.25, ("GM2",),            2000.0, 2250.0, 2500.0, 0.35],
            [ATTACK, 0.60, "RespectDistance",      0.0,  500.0, 1000.0, 0.30, 1],

           # inner zone moves:
            [MOVE,   0.05, "tr",                   0.0, 2000.0, 5000.0, 0.35],
            [MOVE,   0.05, "tl",                   0.0, 2000.0, 5000.0, 0.35],
            [MOVE,   0.10, "tb",                   0.0, 2000.0, 5000.0, 0.35],
            [MOVE,   0.25, "tf",                   0.0, 2000.0, 5000.0, 0.35],

           # outer zone moves:
            [MOVE,   0.06, "tr",                5001.0, 7000.0, 9000.0, 0.50, 1],
            [MOVE,   0.06, "tl",                5002.0, 7000.0, 9000.0, 0.50, 1],
            [MOVE,   0.15, "tb",                5003.0, 7000.0, 9000.0, 0.50, 1],
            [MOVE,   0.05, "tf",                5004.0, 7000.0, 9000.0, 0.50, 1],
            [MOVE,   0.15, TempMoveInProc,      3000.0, 7000.0, 9000.0, 0.35, 1],
            [MOVE,   0.005, Laugh,              5000.0, 7000.0, 9000.0, 0.35, 1],
            [MOVE,   0.005, Insult,             5000.0, 7000.0, 9000.0, 0.35, 1],
            [MOVE,   0.02, GiveOrders,          5000.0, 7000.0, 9000.0, 0.35, 1],
            [MOVE,   0.05, UsePotion,           3000.0, 7000.0, 9000.0, 1.00],
]

SkeletonAttackData = [
           # inner zone blocks:
            [BLOCK,  0.30, (),                   500.0, 1000.0, 3000.0, 0.35],
            [BLOCK,  0.08, "tr",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.08, "tl",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.08, "tb",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.20, "tf",                 750.0, 1500.0, 3500.0, 0.50],

           # outer zone blocks:
            [BLOCK,  0.05, "tr",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.05, "tl",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.10, "tb",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.05, "tf",                3500.0, 7000.0, 9000.0, 0.50],
            
           # attacks:
        [ATTACKDOWN, 1.00, ("STAIRS",),         1200.0, 1600.0, 2500.0, 0.35],
            
            [ATTACK, 0.00, ("GA","GA","GA","GM1",), 1200.0, 1400.0, 2500.0, 0.35],
            [ATTACK, 0.50, ("GA",),             1200.0, 1400.0, 2500.0, 0.35],
            [ATTACK, 0.40, ("GM2",),               0.0, 1600.0, 2500.0, 0.35],
            [ATTACK, 0.40, ("GA", "GA"),        1200.0, 1600.0, 2500.0, 0.35],
            [ATTACK, 0.10, ("GA", "GA", "GM1"),    0.0, 1600.0, 3000.0, 0.35],
            [ATTACK, 0.25, ("GM2",),            1200.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 0.25, ("G22",),            2014.0, 3000.0, 5327.0, 0.35],
            [ATTACK, 1.00, "RespectDistance",      0.0,  500.0, 1200.0, 0.30,1],

           # inner zone moves:
            [MOVE,   0.05, "tr",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.05, "tl",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.10, "tb",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.25, "tf",                   0.0, 2000.0, 5000.0, 0.50],

           # outer zone moves:
            [MOVE,   0.01, "tr",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.01, "tl",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.05, "tb",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.02, "tf",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.06, TempMoveInProc,      3000.0, 7000.0, 9000.0, 0.35],
]

OrkAttackData =	[ 
           # inner zone blocks:
            [BLOCK,  0.25, (),                   500.0, 1000.0, 3000.0, 0.50],
            [BLOCK,  0.05, "tr",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tl",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tb",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tf",                 750.0, 1500.0, 3500.0, 0.50],
           # total inner zone 0.45
           
           # outer zone blocks:
            [BLOCK,  0.07, (),                  3000.0, 4000.0, 5000.0, 0.50],
            [BLOCK,  0.035,"tr",                3500.0, 7000.0, 9000.0, 0.50,1],
            [BLOCK,  0.035,"tl",                3500.0, 7000.0, 9000.0, 0.50,1],
            [BLOCK,  0.245,"tb",                3500.0, 7000.0, 9000.0, 0.50,1],
            [BLOCK,  0.07, "tf",                3500.0, 7000.0, 9000.0, 0.50,1],
           # total outer zone 0.455
           
           # dodges:
            [DODGE,  0.30, "d_r",                500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.30, "d_l",                500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.30, "d_b",                500.0, 1200.0, 2800.0, 0.35],

           # attacks:
        [ATTACKDOWN, 1.00, ("STAIRS",),         1200.0, 1800.0, 2500.0, 0.35],

            [ATTACK, 0.50, ("g_01",),            765.0, 2397.5, 3265.0, 0.35],
            [ATTACK, 0.40, ("g_02",),            873.0, 2123.0, 3373.0, 0.35],
            [ATTACK, 0.40, ("g_06",),            764.0, 2014.0, 3264.0, 0.35],
            [ATTACK, 0.20, ("g_15",),            844.0, 2094.0, 3344.0, 0.35],
            [ATTACK, 0.20, ("g_16",),            243.0, 1493.0, 2743.0, 0.35],
            [ATTACK, 0.15, ("g_18",),           1917.0, 3167.0, 4417.0, 0.35],
            [ATTACK, 0.60, "RespectDistance",      0.0,  500.0, 1200.0, 1.00,1],
            
            # combinations
            [ATTACK, 0.40, ("COMBO1",),            764.0, 2014.0, 3264.0, 0.35],
            [ATTACK, 0.40, ("COMBO2",),            243.0, 1493.0, 2743.0, 0.35],
            [ATTACK, 0.40, ("COMBO3",),            873.0, 2123.0, 3000.0, 0.35],

           # inner zone moves:
            [MOVE,   0.03, "tr",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.03, "tl",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.05, "tb",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.10, "tf",                   0.0, 2000.0, 5000.0, 0.50],

           # outer zone moves:
            [MOVE,   0.03, "tr",                5000.0, 7000.0, 9000.0, 0.50,1],
            [MOVE,   0.03, "tl",                5000.0, 7000.0, 9000.0, 0.50,1],
            [MOVE,   0.05, "tb",                5000.0, 7000.0, 9000.0, 0.50,1],
            [MOVE,   0.03, "tf",                5000.0, 7000.0, 9000.0, 0.50,1],
            [MOVE,   0.15, TempMoveInProc,      5000.0, 7000.0, 9000.0, 0.35,1],
            [MOVE,   0.05, UsePotion,           3000.0, 7000.0, 9000.0, 1.00],
]

EnanoAttackData =	[ 
           # inner zone blocks:
            [BLOCK,  0.25, (),                   500.0, 1000.0, 3000.0, 0.50],
            [BLOCK,  0.05, "tr",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tl",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tb",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.05, "tf",                 750.0, 1500.0, 3500.0, 0.50],
           # total inner zone 0.45
           
           # outer zone blocks:
            [BLOCK,  0.07, (),                  3000.0, 4000.0, 5000.0, 0.50],
            [BLOCK,  0.035,"tr",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.035,"tl",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.245,"tb",                3500.0, 7000.0, 9000.0, 0.50],
            [BLOCK,  0.07, "tf",                3500.0, 7000.0, 9000.0, 0.50],
           # total outer zone 0.455
           
           # dodges:
            [DODGE,  0.30, "d_r",                500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.30, "d_l",                500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.30, "d_b",                500.0, 1200.0, 2800.0, 0.35],

           # attacks:
        [ATTACKDOWN, 1.00, ("STAIRS",),         1200.0, 1800.0, 2500.0, 0.35],

            [ATTACK, 0.50, ("GA",),             1200.0, 1400.0, 2500.0, 0.35],
            [ATTACK, 0.40, ("GA", "GA"),           0.0, 1600.0, 2500.0, 0.35],
            [ATTACK, 0.40, ("GA", "GA", "GA"),  1000.0, 1600.0, 2500.0, 0.35],
            [ATTACK, 0.40, ("GA", "GA"),        1200.0, 1600.0, 2500.0, 0.35],
            [ATTACK, 0.10, ("GA", "GA", "GM1"),    0.0, 1600.0, 3000.0, 0.35],
            [ATTACK, 0.25, ("GM2",),            1200.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 1.00, "RespectDistance",      0.0,  500.0, 2000.0, 1.00],

           # inner zone moves:
            [MOVE,   0.03, "tr",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.03, "tl",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.05, "tb",                   0.0, 2000.0, 5000.0, 0.50],
            [MOVE,   0.10, "tf",                   0.0, 2000.0, 5000.0, 0.50],

           # outer zone moves:
            [MOVE,   0.03, "tr",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.03, "tl",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.05, "tb",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.03, "tf",                5000.0, 7000.0, 9000.0, 0.50],
            [MOVE,   0.15, TempMoveInProc,      5000.0, 7000.0, 9000.0, 0.35],
            [MOVE,   0.05, UsePotion,           3000.0, 7000.0, 9000.0, 1.00],
]

ChaosKnightAttackData =	[ 
           # inner zone blocks:
            [BLOCK,  0.85, (),                   500.0, 1000.0, 3000.0, 0.35],
			         
           # attacks:
            [ATTACK, 0.02, ("SP1",),            7000.0, 9000.0,50000.0, 0.35],
            [ATTACK, 0.20, ("G01",),            1490.0, 2195.0, 2900.0, 0.35],
            [ATTACK, 0.15, ("G02",),            1410.0, 2105.0, 2800.0, 0.35],
            [ATTACK, 0.10, ("G07",),            1550.0, 2225.0, 2900.0, 0.35],
            [ATTACK, 0.10, ("G08",),            1700.0, 2375.0, 3050.0, 0.35],
            [ATTACK, 0.07, ("G12",),            1850.0, 2525.0, 3200.0, 0.35],
            [ATTACK, 0.07, ("G18",),            3050.0, 3600.0, 3850.0, 0.35],
            [ATTACK, 0.05, ("G31",),            2450.0, 3600.0, 3850.0, 0.35],
]

RagnarAttackData = [ 
           # blocks:
            [BLOCK,  1.00, (),                   500.0, 1000.0, 9000.0, 0.35],
            [BLOCK,  0.10, "tr",                 750.0, 1500.0, 9000.0, 0.35],
            [BLOCK,  0.10, "tl",                 750.0, 1500.0, 9000.0, 0.35],
            [BLOCK,  0.25, "tb",                 750.0, 1500.0, 9000.0, 0.35],
            [BLOCK,  0.15, "tf",                 750.0, 1500.0, 9000.0, 0.35],

           # dodges:
            [DODGE,  0.40, ("GDR",),             500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.40, ("GDL",),             500.0, 1200.0, 2800.0, 0.35],
            [DODGE,  0.20, ("GDB",),             500.0, 1200.0, 2200.0, 0.35],

           # attacks:
            [ATTACK, 0.30, ("G01",),             500.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 0.10, ("G02",),             500.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 0.05, ("G03",),             500.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 0.25, ("G07",),             500.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 0.25, ("G17",),             500.0, 1800.0, 2500.0, 0.35],
            [ATTACK, 0.25, ("G21",),             500.0, 1800.0, 2500.0, 0.35],

           # inner zone moves:
            [MOVE,  0.35, ("GDR",),              500.0, 1200.0, 2800.0, 0.35],
            [MOVE,  0.35, ("GDL",),              500.0, 1200.0, 2800.0, 0.35],
            [MOVE,  0.30, ("GDB",),              500.0, 1200.0, 2200.0, 0.35],
            
           # all zone moves:
            [MOVE,   0.05, "tr",                2800.0, 4000.0, 9000.0, 0.35],
            [MOVE,   0.05, "tl",                2800.0, 4000.0, 9000.0, 0.35],
            [MOVE,   0.25, "tb",                2800.0, 4000.0, 9000.0, 0.35],
            [MOVE,   0.05, "tf",                2800.0, 4000.0, 9000.0, 0.35],

           # outer zone moves:
            [MOVE,   0.02, Laugh,               6000.0, 7000.0, 9000.0, 0.35,1],
            [MOVE,   0.02, Insult,              6000.0, 7000.0, 9000.0, 0.35,1],
            [MOVE,   0.05, UsePotion,           3500.0, 6000.0, 9000.0, 1.00],

]

TrollAttackData =	[ 
           # inner zone blocks:
            [BLOCK,  0.80, (),                   500.0, 1750.0, 3000.0, 0.65],

           # attacks:			         
            [ATTACKDOWN, 0.90, ("G04",),         650.0, 1225.0, 2150.0, 0.35],
            [ATTACKDOWN, 0.60, ("G18",),        2050.0, 3025.0, 3900.0, 0.35],

            [ATTACK, 0.25, ("G01",),            1250.0, 1625.0, 1800.0, 0.35],
            [ATTACK, 0.20, ("G02",),            1000.0, 1500.0, 2000.0, 0.35],
            [ATTACK, 0.15, ("G04",),             650.0, 1225.0, 2050.0, 0.35],
            [ATTACK, 0.15, ("G06",),             950.0, 1405.0, 1860.0, 0.35],
            [ATTACK, 0.10, ("G12",),            2150.0, 2505.0, 2850.0, 0.35],
            [ATTACK, 0.10, ("G18",),            2150.0, 3025.0, 3900.0, 0.35],
            [ATTACK, 0.10, ("G19",),             250.0, 2500.0, 3900.0, 0.35],
            [ATTACK, 0.05, ("G31",),            2220.0, 3060.0, 3900.0, 0.35]

]

CosAttackData = [
           # attacks:
            [ATTACK, 0.15, ("GA",),              1500.0, 1500.0, 2200.0, 0.35],

            # inner zone moves:
            [MOVE,   0.05, "tr",                1400.0, 1700.0, 2200.0, 0.25],
            [MOVE,   0.05, "tl",                1400.0, 1700.0, 2200.0, 0.25],
            [MOVE,   0.10, "tb",                1400.0, 1700.0, 2200.0, 0.25],
            [MOVE,   0.10, "tf",                1400.0, 1700.0, 2200.0, 0.25],
            [MOVE,   0.25, FearFire,               0.0, 1700.0, 2200.0, 0.05],

           # outer zone moves:
            [MOVE,   0.06, "tr",                2200.0, 3000.0, 4000.0, 0.25],
            [MOVE,   0.06, "tl",                2200.0, 3000.0, 4000.0, 0.25],
            [MOVE,   0.15, "tb",                2200.0, 3000.0, 4000.0, 0.25],
            [MOVE,   0.05, "tf",                2200.0, 7000.0, 4000.0, 0.25],
]

SpiderSmallAttackData = [
           # attacks:
            [ATTACK, 0.25, ("GA",),              500.0, 1000.0, 1400.0, 0.35],
            [ATTACK, 0.03, ("SP",),             2800.0, 3000.0, 3500.0, 0.20],

           # inner zone moves:
            [MOVE,   0.25, FearFire,               0.0, 1700.0, 2500.0, 0.05],
]

VampireAttackData =	[ 
           # inner zone blocks:
            [BLOCK,  1.32, (),                   500.0, 1000.0, 3000.0, 0.35],
            [BLOCK,  0.32, (),                   500.0, 1000.0, 3000.0, 0.35],
            [BLOCK,  0.10, "tr",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.14, "tl",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.19, "tb",                 750.0, 1500.0, 3500.0, 0.50],
            [BLOCK,  0.10, "tf",                 750.0, 1500.0, 3500.0, 0.50],

           # dodges:  sometimes the best form of defence is to attack...
            [DODGE,  0.90, ("g_26",),            500.0, 1800.0, 2930.0, 0.35],
            [DODGE,  0.90, Disappear,           1500.0, 1800.0, 4930.0, 0.35],

           # attacks:
            [ATTACK, 0.15, ("disappear",),       500.0, 1000.0, 1200.0, 0.35],
            [ATTACK, 0.15, Disappear,           2000.0, 3000.0, 9000.0, 0.35],
            [ATTACK, 0.10, ("disappear",),      9000.0,10000.0,20000.0, 0.35],
            [ATTACK, 0.14, ("g_01",),            800.0, 2421.0, 3178.0, 0.35],
            [ATTACK, 0.09, ("g_06",),           1010.0, 2320.0, 2800.0, 0.35],
            [ATTACK, 0.14, ("g_07",),           1100.0, 2400.0, 3020.0, 0.35],
            [ATTACK, 0.08, ("g_26",),            500.0,  850.0, 1100.0, 0.35],
            
            [ATTACK, 0.10, ("COMBO1",),         1100.0, 2400.0, 2820.0, 0.35],
            [ATTACK, 0.10, ("COMBO2",),          800.0, 2421.0, 2978.0, 0.35],
            
            
           # inner zone moves:
            [MOVE,   0.025, "tr",                750.0, 1500.0, 3000.0, 0.35],
            [MOVE,   0.025, "tl",                750.0, 1500.0, 3000.0, 0.35],
            [MOVE,   0.0625,"tb",                750.0, 1500.0, 3000.0, 0.35],
            [MOVE,   0.0375,"tf",                750.0, 1500.0, 3000.0, 0.35],
            
           # outer zone moves:
            [MOVE,   0.002, Insult,             5000.0, 7000.0, 9000.0, 0.50,1],
            [MOVE,   0.002, Insult,             6000.0, 6250.0, 6500.0, 0.50,1],
            [MOVE,   0.002, Insult,             7000.0, 7250.0, 7500.0, 0.50,1],
            [MOVE,   0.002, Insult,             8000.0, 8250.0, 8500.0, 0.50,1],
            [MOVE,   0.002, Insult,             9000.0, 9250.0, 9500.0, 0.50,1],
            
            [MOVE,   0.025,  "tr",              3000.0, 3500.0, 4500.0, 0.35,1],
            [MOVE,   0.025,  "tl",              3000.0, 3500.0, 4500.0, 0.35,1],
            [MOVE,   0.0625,"tb",               3000.0, 3500.0, 4500.0, 0.35,1],
            [MOVE,   0.0375,"tf",               3000.0, 3500.0, 4500.0, 0.35,1],

            [MOVE,   0.80,  KeepDistance,       2800.0, 6250.0, 9500.0, 0.35,1],

]


LittleDemonAttackData =	[ 
           # inner zone blocks:
            #[DODGE,  0.30, MagicShield,        500.0, 1000.0, 3000.0, 2.00],
			         
           # attacks:
            [ATTACK, 0.40, ("SP1",),               0.0, 1500.0, 3000.0, 0.35],
            [ATTACK, 0.40, ("SP1",),            5000.0, 7000.0, 9000.0, 0.35],
            [ATTACK, 0.20, ("G03",),            2085.0, 2500.0, 2829.0, 0.35],
            [ATTACK, 0.20, ("G06",),            3217.0, 3700.0, 3997.0, 0.35],
            [ATTACK, 0.90, ("G07",),            2400.0, 2500.0, 2600.0, 0.35],
            [ATTACK, 0.10, ("G22",),            3097.0, 3700.0, 3855.0, 0.35],
            [ATTACK, 0.10, ("G27",),            2274.0, 2600.0, 2700.0, 0.35],
            [ATTACK, 0.20, ("ZIG",),            5000.0, 9000.0,12000.0, 0.53],
            [ATTACK, 0.20, ("ZAG",),            5000.0, 9000.0,12000.0, 0.57],
]


LichAttackData =	[  
           # outer zone moves:
#            [MOVE,   0.02, Insult,              5000.0, 7000.0, 9000.0, 0.35,1],
]

MinotaurAttackData =	[            
            [ATTACK, 0.18, ("G01",),            1500.0, 3000.0, 3500.0, 0.35],
            [ATTACK, 0.18, ("G07",),            1500.0, 3000.0, 3500.0, 0.35],
            [ATTACK, 0.18, ("G08",),            1500.0, 3000.0, 3500.0, 0.35],
            [ATTACK, 0.06, ("G12",),            2800.0, 3300.0, 3750.0, 0.35],
            [ATTACK, 0.06, ("G31",),            2800.0, 3300.0, 3750.0, 0.35],
]

SalamanderAttackData =	[  
           # attacks:
            [ATTACK, 0.30, ("g_bite",),            3400.0, 3700.0, 4200.0, 0.35],
            [ATTACK, 0.10, ("g_r",),               2500.0, 2800.0, 3500.0, 0.35],            
            [ATTACK, 0.01, ("spit",),               0.0, 1500.0, 3950.0, 0.35],
            [ATTACK, 0.02, ("spit",),               0.0, 1500.0, 2274.0, 0.35],
            [ATTACK, 0.04, ("spit",),             6000.0,9000.0,10000.0, 0.35],

]

DalGurakPhase1 = [ 

           # attacks:
            [ATTACK,  0.02, LaunchFireBall,     7000.0,21000.0,32000.0, 0.35],
            [ATTACK,  0.02, LaunchMissile,      7000.0,21000.0,32000.0, 0.35],

           # all zone moves:
            [MOVE,    0.80, Disappear,          1000.0, 5000.0, 7000.0, 0.35],
            [MOVE,    0.003,Disappear,          1000.0, 5000.0,32000.0, 0.35]
            

#            [MOVE,   0.02, "tr",                   0.0, 2000.0, 9000.0, 0.35],
#            [MOVE,   0.02, "tl",                   0.0, 2000.0, 9000.0, 0.35],
#            [MOVE,   0.04, "tb",                   0.0, 2000.0, 9000.0, 0.35],
#            [MOVE,   0.02, "tf",                   0.0, 2000.0, 9000.0, 0.35],
]

DalGurakPhase2 = [ 
           # blocks:
            [BLOCK,  0.10, (),                   500.0, 1000.0, 9000.0, 0.50],
            [BLOCK,  0.05, "tr",                 750.0, 1500.0, 4500.0, 0.50],
            [BLOCK,  0.05, "tl",                 750.0, 1500.0, 4500.0, 0.50],
            [BLOCK,  0.05, "tb",                 750.0, 1500.0, 4500.0, 0.50],
            [BLOCK,  0.20, "tf",                 750.0, 1500.0, 4500.0, 0.50],
            
           # dodges:
            [DODGE,  0.50, ("g_d_l",),          2400.0, 3000.0, 3550.0, 0.35],
            [DODGE,  0.50, ("g_d_r",),          2200.0, 2700.0, 3150.0, 0.35],

           # attacks on stairs:      	
        [ATTACKDOWN,  0.20, LaunchWeapon,       4000.0, 6900.0,20000.0, 4.00],
        [ATTACKDOWN,  0.10, ("GMG1",),          8000.0, 9000.0,30000.0, 4.00],
        [ATTACKDOWN,  0.10, ("GMG2",),          8000.0, 9000.0,30000.0, 4.00],
        [ATTACKDOWN,  0.05, ("g_08_new",),      1386.0, 2000.0, 2061.0, 0.35],
        [ATTACKDOWN,  0.05, ("g_21_6_s8new",),  1228.0, 2500.0, 2635.0, 0.35],
        [ATTACKDOWN,  0.05, ("g_19_bs1_new",),  1306.0, 3700.0, 3864.0, 0.35],

           # attacks:
           # launch weapon attacks:
            [ATTACK,  0.10, LaunchWeapon,       4000.0, 6900.0, 9000.0, 4.00],
           # accumulated attack total 0.1
           
           # launch trail attacks:
            [ATTACK,  0.05, ("GMG1",),          8000.0, 9000.0,30000.0, 4.00],
            [ATTACK,  0.05, ("GMG2",),          8000.0, 9000.0,30000.0, 4.00],
           # accumulated attack total 0.2
           
           # melee simples:
            [ATTACK,  0.15, ("g_07_new",),       500.0, 1700.0, 1778.0, 0.35],
            [ATTACK,  0.10, ("g_08_new",),      1386.0, 2000.0, 2061.0, 0.35],
            [ATTACK,  0.10, ("g_02_new",),      1304.0, 2000.0, 2100.0, 0.35],
            [ATTACK,  0.10, ("g_01_7_new",),    1068.0, 2000.0, 2130.0, 0.35],
            [ATTACK,  0.10, ("g_22lowkata_new",),1128.0,2800.0, 2871.0, 0.35],
           # accumulated attack total 0.75
           
           # melee specials
            [ATTACK,  0.05, ("g_21_6_s8new",),  1228.0, 2000.0, 2135.0, 0.35],
            [ATTACK,  0.05, ("g_19_bs1_new",),  1306.0, 3700.0, 3864.0, 0.35],
            [ATTACK,  0.05, ("g_b32kata_new",), 1082.0, 3000.0, 3127.0, 0.35],
            [ATTACK,  0.05, ("g_29_3new",),     1130.0, 2800.0, 2964.0, 0.35],
#           [ATTACK,  0.00, ("g_back",),        1173.0, 1400.0, 1490.0, 0.35],
           # accumulated attack total 0.95
                       
           # all zone moves:
            [MOVE,   0.02, "tr",                   0.0, 2000.0, 9000.0, 0.35],
            [MOVE,   0.02, "tl",                   0.0, 2000.0, 9000.0, 0.35],
            [MOVE,   0.04, "tb",                   0.0, 2000.0, 9000.0, 0.35],
            [MOVE,   0.02, "tf",                   0.0, 2000.0, 9000.0, 0.35],
]

GreatDemonAttackData = [                        
           # Close attacks
            [ATTACK,  0.50, ("g_magic",),          0.0, 2000.0, 3000.0, 0.50],
            [ATTACK,  0.20, ("g_claw",),        1000.0, 2000.0, 4500.0, 0.50],
            [ATTACK,  0.10, ("g_01",),          4000.0, 4200.0, 4600.0, 0.50],
            [ATTACK,  0.10, ("g_12",),          5500.0, 6000.0, 7500.0, 0.50],
            
           # Long range spit attacks
            [ATTACK,  0.012,("g_spit_around",), 3000.0, 6000.0, 12000.0, 0.50],
            [ATTACK,  0.015,("g_spit_f",),      3000.0, 7500.0,12000.0, 0.50],
            [ATTACK,  0.030,("g_spitball",),    8000.0, 9500.0,12000.0, 0.50],
                        
           # All range attack should be activated later...
            [ATTACK,  0.25, "RespectDistance",  1000.0, 2000.0, 3000.0, 0.35, 1],
            [ATTACK,  0.25, KeepDistance,       7000.0,12000.0,30000.0, 0.50],
            
            # Reserved for later in life
            #[ATTACK,  0.03, ("g_quake",),       1000.0, 7000.0, 9000.0, 0.50],
            
            # Not implimented back attacks...
            #[ATTACK,  0.03, ("g_back",),        6000.0, 6500.0, 7000.0, 0.50],
]


AnAhkardAttackData = [
            [ATTACK,  0.25, ("g_01",),          1500.0, 3000.0, 3400.0, 0.50],
            [ATTACK,  0.25, ("g_02",),          2500.0, 3200.0, 4700.0, 0.50],
            [ATTACK,  0.25, ("g_07",),          2500.0, 3200.0, 4500.0, 0.50],
            [ATTACK,  0.007, ("g_mgc03",),       4000.0, 6000.0,10000.0, 0.50],  #AimLaser
]

StoneGolemAttackData = [
            [ATTACK,  0.05, ("g_01",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.05, ("g_114",),         1500.0, 2000.0, 2700.0, 0.50],
            [ATTACK,  0.05, ("g_12",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.05, ("g_21",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.10, ("g_21_27",),       3000.0, 3500.0, 4000.0, 0.50],
            [ATTACK,  0.05, ("g_31",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.016,("g_1tw",),         5500.0, 7500.0,10000.0, 0.50],
]

LavaGolemAttackData = [
            [ATTACK,  0.05, ("g_01",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.05, ("g_114",),         1500.0, 2000.0, 2700.0, 0.50],
            [ATTACK,  0.05, ("g_12",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.05, ("g_21",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.10, ("g_21_27",),       3000.0, 3500.0, 4000.0, 0.50],
            [ATTACK,  0.05, ("g_31",),          1500.0, 2000.0, 2500.0, 0.50],
            [ATTACK,  0.07, ("g_spit",),        2000.0, 3500.0, 4500.0, 0.50],      # Added
            [ATTACK,  0.016,("g_1tw",),         5500.0, 7500.0,10000.0, 0.50],
]

"""
Notes
=====
If the total weights of a category are less than 1.00, then 
the remainder is used as the chance that nothing is selected 
out of this category.

ToDo
====
Anticipation of enemy moves, if they just perform 
the same attack repeatedly....


Extra information: 
?* best angle
?* max angle
* distance
* max distance
* overall time to execute
* (possibly additional for dodge & block.  Special counters vs.)
* (for attack, damage)



Questions and bugs 
Com moves don't seem to be launched (e.g sr and sl)?
Currenly waiting for a fixed paused before continuing from setting a com mode, can we vary this?
Why is it moving forwards when very close?
Still bug in LastAnmPos, when PossibleXZPos returns false for Kgt_r_f animation
Slow Attacks...


##########################################################
Consider Blocks first.

	if block found don't comsider dodge

##########################################################
Consider Dodges next (and Positional Moves)
	Remove dodges from list if:
		* angle > max angle
		* distance > max distance 
		* action takes us out of action area max or collides with scenery

	Evaluate each dodge based on:
		?* length of time to execute the dodge (-)
		* Dodge Effectiveness
			?* distance from the dodge's ideal angle (-)
			* distance from the dodge's ideal distance (-)
			?* whether countering Jump, or Long Range (+)		
		* Other factors
			* how often we have used the dodge before (-)			
			?* angle to enemy improvement for us (+)
			?* angle to us improvement for enemy (-)
			* how much we like the dodge (pregiven) (*)
	
	Roulette method to choose a dodge
	
	if dodge found then return

##########################################################
Consider Attacks Next
	Remove attacks from list if:
		?* angle > max angle
		* distance > max distance 
		* action takes us out of action area max or collides with scenery

	Evaluate each attacks based on:
		?* length of time to execute the attack (-)
		* Attack Effectiveness			
			* distance from the attack's ideal angle (-)
			* distance from the attack's ideal distance (-)
			
		* Other factors
			* how often we have used the dodge before (-)			
			* angle to enemy improvement for us (+)
			* angle to us improvement for enemy (-)
			* how much we like the attack (pregiven) based on (*)
				* likely damage done by the attack if it connects
				* length of time to execute the attack
	
	Roulette method to choose an attack
	
	if attack found then return

Consider Positional Moves Last
	eg Strafing, GoF, and GoB, and combinations of above


"""
					
					
					
					
					
					
