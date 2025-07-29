##///
##||| ACTIONS.PY TITANIUM
##||| Change list:
##||| * StdToggleWeapons() completely rewritten
##||| * ToggleWEvent() heavily modified
##||| * Fixed "Press F1" prompt to be correct for all weapons and hero characters.
##||| * Quivers on back don't disappear when picking up arrows/quivers.
##||| * Quivers don't disappear from hands when picking them up.
##||| * Quivers immediately go to back if possible.
##||| * Added and edited bow related functions for bow cancelling.
##||| * Added JumpHandler for DodgeFix. ( # PLAGUE: Needs to be re-written to support real-time config)
##||| * Exiting the level with a limb in hand and nothing on back no longer crashes (See PutAllInBack)
##||| * Should report the message "not in reach" more correctly now.
##||| * Character will no longer try to draw arrows from an empty quiver after picking/using items.
##||| * No longer will draw shield when have a two-handed weapon on InstanAttack
##||| * DropRelease --> added "DropLeft2Event", called from Damage.
##\\\ 

import Bladex
### /    Added by Dario    \ ####
import Ontake
import Stars
import string
### \   Added by Dario    / ####
import math
import Reference
import Breakings
import InitDataField
import OnInitTake # Added by Manuel
import AuxFuncs #Para Faces de camara
import B3DLib
import netgame
import Damage
import CharStats
import MenuText
import BInput
import Select

import Netval
import Torchs
import ItemTypes

#
# Fade out values -> For Enric
#
START_FADEOUT_IN_BIG_FALL=1.5
END_FADEOUT_IN_BIG_FALL=6.0

#START_FADEOUT_IN_BIG_FALL=2.0
#END_FADEOUT_IN_BIG_FALL=2.5

if Reference.DEBUG_INFO == 1:
	import pdb
import pdb
TRUE=(1==1)
FALSE=(1!=1)
#
#Values returned by StatR
#Tells what is being carried in the right hand
#
RA_NO_WEAPON=0  #Nothing in hand
RA_1H_WEAPON=1  #Carring 1 hand weapon
RA_BOW=2        #A bow
RA_2H_OBJECT=3  #A 2 hand object
RA_TORCH=4      #NEW : Now the torch is in the right hand!

#
#Values returned by StatL
#Tells what is being carried in the left hand
#
LA_NO_WEAPON=0  #Nothing
LA_SHIELD=1     #Shield
LA_BOW=2        #A bow

LA_2H_OBJECT=2  #A 2 hand object

PI = math.pi
TWOPI = PI*2
FACINGANGLE =  PI * 0.125
BEHINDANGLE =  PI * 0.75

B_SOLID_MASK_PERSON     =1
B_SOLID_MASK_FLOOR      =2
B_SOLID_MASK_CAMERA     =4
B_SOLID_MASK_PARTICLES  =8

MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8

MESSAGE_START_TRAIL         =14
MESSAGE_STOP_TRAIL          =15

# Interpolation Types for DoAction()
InterpWithOff=0,
InterpWithOutOff=1,
InertialIntrp=2,
FixedRFootIntep=3,
FixedLFootIntep=4,
FixedFootAutoInterp=5


# Table to be used by other libraries
TryToTakeCallBacks = []

#
# Message Support Functions
#


# Message to the user, maybe this should go to the screen
def ReportMsg(Msg):
	if netgame.GetNetState()==0:
		import GameText
		GameText.AbortText()
		GameText.WriteTextAux(MenuText.GetMenuText(Msg),2.0,255,255,255,[],None,1)


def GetListOfObjectsAt(inv,id):

	if inv.GetNumberObjectsAt(id)==1:
		name = inv.GetObject(id)
		if name:
			return [name]
		else:
			return []
	else:
		corray = range(inv.GetNumberObjectsAt(id))

	resulto = []
	for i in corray:
		name = inv.GetObject(id)
		if not name:
			return []
		inv.RemoveObject(name)
		ExtendedTakeObject(inv,name)
		resulto.append(name)
	return resulto


def RemoveAllKeys(EntityName):
	me = Bladex.GetEntity(EntityName)
	inv= me.GetInventory()
	keyNames = []

	for j in range(inv.nKeys):
		keyNames.append(inv.GetKey(j))

	for key in keyNames:
		inv.RemoveKey(key)

def RemoveNoTravelObjects(EntityName):

	me        = Bladex.GetEntity(EntityName)
	inv       = me.GetInventory()
	objname   = inv.GetObject(0)
	counterid = 0

	while objname:
		obj     = Bladex.GetEntity(objname)
		if obj.Kind in Reference.TravelObjects:
			counterid = counterid + 1
		else:
			inv.RemoveObject(objname)
		objname = inv.GetObject(counterid)

#
#
#
def PutAllInBack(EntityName):
    me = Bladex.GetEntity(EntityName)
    right= me.InvRight
    left= me.InvLeft
    rightback= me.InvRightBack
    leftback= me.InvLeftBack


    inv= me.GetInventory()
    inv.LinkRightHand ("")
    inv.LinkLeftHand ("")

    inv.LinkRightBack("")
    inv.LinkLeftBack("")


    # Left Back
    if leftback:
        inv.LinkLeftBack(leftback)
    elif not leftback and left:
        inv.LinkLeftBack(left)
    elif leftback and left:
        print "ERROR - Actions.PutAllInBack -> leftback and left both diff on none!!!"
        inv.LinkLeftBack(leftback)
        print "   Linked only the back one..."


    # Right Back
    if rightback:
        inv.LinkRightBack(rightback)
    elif not rightback and right:
        if Bladex.GetEntity(right).Kind[:4] == "Limb":                                # Bugfix.
            print ("ERROR - Actions.PutAllInBack -> trying to put a limb on back")    # Exiting the level with a limb in hand
            inv.LinkRightBack("")                                                     # and nothing on back
        else:                                                                         # should no longer crash the game.
            inv.LinkRightBack(right)                                                  #                 - LeadHead
    elif rightback and right:
        print "ERROR - Actions.PutAllInBack -> rightback and right both diff on none!!!"
        inv.LinkRightBack(rightback)
        print "   Linked only the back one..."




#
#
#
def Start_Weapon (EntityName,EventName):
	me = Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			weapon_name= inv.GetActiveWeapon()
			if weapon_name:
				weapon= Bladex.GetEntity(weapon_name)
				if weapon:
					#print "Start Weapon"
					weapon.MessageEvent(Reference.MESSAGE_START_WEAPON,0,0)

def Stop_Weapon (EntityName,EventName):
	me = Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			weapon_name= inv.GetActiveWeapon()
			if weapon_name:
				weapon= Bladex.GetEntity(weapon_name)
				if weapon:
					#print "Stop Weapon"
					weapon.MessageEvent(Reference.MESSAGE_STOP_WEAPON,0,0)

def Start_Weapon_Special (EntityName,EventName):
	me = Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			weapon_name= inv.GetActiveWeapon()
			if weapon_name:
				weapon= Bladex.GetEntity(weapon_name)
				if weapon:
					if weapon.Data:
						try: weapon.Data.Start_Weapon_Special (EntityName,EventName)
						except AttributeError: pass

def Stop_Weapon_Special (EntityName,EventName):
	me = Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			weapon_name= inv.GetActiveWeapon()
			if weapon_name:
				weapon= Bladex.GetEntity(weapon_name)
				if weapon:
					if weapon.Data:
						try: weapon.Data.Stop_Weapon_Special (EntityName,EventName)
						except AttributeError: pass

def Start_Trail (EntityName,EventName):
	me = Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			weapon_name= inv.GetActiveWeapon()
			if weapon_name:
				weapon= Bladex.GetEntity(weapon_name)
				if weapon:
					weapon.MessageEvent(Reference.MESSAGE_START_TRAIL,0,0)

def Stop_Trail (EntityName,EventName):
	me = Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			weapon_name= inv.GetActiveWeapon()
			if weapon_name:
				weapon= Bladex.GetEntity(weapon_name)
				if weapon:
					weapon.MessageEvent(Reference.MESSAGE_STOP_TRAIL,0,0)

def DthFllArrivedAux(EntityName):
	print "aux1"
	me= Bladex.GetEntity(EntityName)
	me.RaiseEvent("DthFllArrived")
	print "aux2"

def DthFllArrivedWarper(EntityName,EventName):
	me= Bladex.GetEntity(EntityName)
	print "DthFlllArrivedWarper"
	print "t2fall is " + str(me.T2Fall)
	print "bye bye"
	Bladex.AddScheduledFunc(Bladex.GetTime()+me.T2Fall, DthFllArrivedAux,(EntityName,),"DthFllArrivedAux"+EntityName)


def GraspString (EntityName,EventName):
	me= Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			if inv.HoldingBow:
				bow= Bladex.GetEntity(inv.GetBow())
				try: bow.Data.GraspString()
				except AttributeError: print "No string on bow. Do ItemTypes.ItemDefaultFuncs(Bladex.GetEntity('"+bow.Name+"'))"

def UnGraspString (EntityName,EventName):
	me= Bladex.GetEntity(EntityName)
	if me:
		inv= me.GetInventory()
		if inv:
			if inv.HoldingBow:
				bow= Bladex.GetEntity(inv.GetBow())
				try: bow.Data.UnGraspString()
				except AttributeError: print "No string on bow. Do ItemTypes.ItemDefaultFuncs(Bladex.GetEntity('"+bow.Name+"'))"


def AddQuiver(inv, new_quiver_name):                        # edited some parts to fix quiver stuff -LeadHead
	new_quiver= Bladex.GetEntity(new_quiver_name)
	me = Bladex.GetEntity(inv.Owner)

	# Do we already have a quiver of this type
	for i in range (inv.nQuivers):
		quiver_name= inv.GetQuiver(i)
		quiver= Bladex.GetEntity(quiver_name)
		if quiver.Data.ArrowType==new_quiver.Data.ArrowType:
			me=Bladex.GetEntity(inv.Owner)        

			# Select this quiver
			inv.SetCurrentQuiver(quiver_name)
			if inv.HoldingBow:
				inv.LinkRightBack(quiver_name)

			# Add the arrows, and delete the new quiver
			quiver.Data.ReceiveArrows (new_quiver.Data.NumberOfArrows(), inv.Owner)
			new_quiver.SubscribeToList("Pin")
			inv.LinkRightHand("None")
			
			return

	# Else add a new quiver to the inventory and select it
	inv.AddQuiver(new_quiver_name)                   # PLAGUE: Don't switch if already have a quiver on back.

    # Everything that follows added. We want to check what we have or haven't before selecting quivers. -LeadHead
	inv.LinkRightHand("None")
	if inv.HoldingBow or inv.HasBowOnBack:
		if not me.InvRightBack:     # Check again if don't already have another kind of quiver on back just in case
			inv.SetCurrentQuiver(new_quiver_name)
			inv.LinkRightBack(new_quiver_name)


def ExtendedTakeObject(inv,Object2TakeName):
	global StakObjects

	o = Bladex.GetEntity(Object2TakeName)
	if o:
		if o.Kind in Reference.StackObjects.keys():
			inv.AddObject(Object2TakeName,Reference.StackObjects[o.Kind]-1)
		else:
			inv.AddObject(Object2TakeName,0)
	else:
		print "ExtendedTakeObject: "+Object2TakeName+" cannot be found to take"



def TakeObject(EntityName,Object2TakeName, force_take=TRUE):
	#print "Take object "+EntityName+", "+Object2TakeName
	me=Bladex.GetEntity(EntityName)
	inv=me.GetInventory()

	#if me.Data and me.Data.pickup_entity:
	#	me.Data.pickup_entity=Object2TakeName
	#PickupEventHandler(EntityName,"PickupEvent")

	if IsOneTooMany (EntityName, Object2TakeName):
		if force_take:
			DropToMakeRoomFor(EntityName, Object2TakeName)
		else:
			print (EntityName+": Too many objects of this type: "+Object2TakeName)
			return

	object_flag=Reference.GiveObjectFlag(Object2TakeName)
	try:
		me.Data.RegisterObjectAsTaken(Object2TakeName)
	except:
		if EntityName=='Player1':
			print Object2TakeName+" not registered as taken, Players Data class not created yet"

	if object_flag == Reference.OBJ_ITEM:
		ExtendedTakeObject(inv,Object2TakeName)
	elif object_flag == Reference.OBJ_SHIELD:
		inv.AddShield(Object2TakeName)
		if not me.InvLeftBack and not me.InvRightBack and not me.InvLeft:
			inv.LinkLeftHand(Object2TakeName)
	elif object_flag == Reference.OBJ_WEAPON:
		flag=Reference.GiveWeaponFlag(Object2TakeName)
		inv.AddWeapon(Object2TakeName,flag)
		if me.InvLeftBack=="" and me.InvRightBack=="" and me.InvRight=="":
			inv.LinkRightHand(Object2TakeName)
	elif object_flag == Reference.OBJ_BOW:	#Corregir?
		inv.AddBow(Object2TakeName)
		if not me.InvLeftBack and not me.InvRightBack and not me.InvRight and not me.InvLeft:
			inv.LinkLeftHand(Object2TakeName)
			#inv.LinkRightHand(Object2TakeName) # Esta bien ? Revisar !
	elif object_flag == Reference.OBJ_QUIVER:
		AddQuiver(inv, Object2TakeName)              # -LeadHead?
	elif object_flag == Reference.OBJ_STANDARD:
		if not me.InvLeftBack and not me.InvRightBack and not me.InvRight:
			inv.LinkRightHand(Object2TakeName)
	elif object_flag == Reference.OBJ_KEY:
		inv.AddKey(Object2TakeName)
	elif object_flag == Reference.OBJ_SPECIALKEY:
		inv.AddSpecialKey(Object2TakeName)
	elif object_flag == Reference.OBJ_TABLET:
		inv.AddTablet(Object2TakeName)
	elif object_flag == Reference.OBJ_ARROW:
		pass
	elif object_flag == Reference.OBJ_USEME and EntityName != "Player1" :
		ExtendedTakeObject(inv,Object2TakeName)
	else:
		print "ERROR adding an object to a character !!!"
		print "Not classified properly in Reference.py!!!"


def StatR(EntityName):
	me=Bladex.GetEntity(EntityName)
	ObjectName=me.InvRight
	if ObjectName=="None" or not ObjectName:
		return RA_NO_WEAPON

	object_flag=Reference.GiveObjectFlag(ObjectName)

	if object_flag==Reference.OBJ_BOW:
		return RA_BOW
	#elif object_flag==Reference.OBJ_TORCH:
	#	return RA_TORCH
	else:
		return RA_1H_WEAPON

def StatL(EntityName):
	me=Bladex.GetEntity(EntityName)
	ObjectName=me.InvLeft
	if ObjectName=="None" or not ObjectName:
		return LA_NO_WEAPON

	object_flag=Reference.GiveObjectFlag(ObjectName)

	if object_flag==Reference.OBJ_SHIELD:
		return LA_SHIELD
	elif object_flag==Reference.OBJ_BOW:
		return LA_BOW
	else:
		print "ERROR - Invalid object in left hand!!!"
		print "Check it in Reference.py!!!"
		return

#
# IsRightHandStandardObject
#
def IsRightHandStandardObject(EntityName):
	me=Bladex.GetEntity(EntityName)
	if not me.InvRight:
		return FALSE

	# Get object type
	object_flag= Reference.GiveObjectFlag(me.InvRight)
	return object_flag == Reference.OBJ_STANDARD

#
#
#
def IsRightHandWeaponObject(EntityName):
	me=Bladex.GetEntity(EntityName)
	if not me.InvRight:
		return FALSE

	# Get object type
	object_flag= Reference.GiveObjectFlag(me.InvRight)
	return object_flag == Reference.OBJ_WEAPON or object_flag == Reference.OBJ_BOW # Do not include bow ?

# Func to detect if the weapon is 2 handed
# 
#   -LeadHead
def IsWeapon2Handed(WepName):
    wep_Flag = Reference.GiveWeaponFlag(WepName)
    if wep_Flag == Reference.W_FLAG_2W or wep_Flag == Reference.W_FLAG_AXE or wep_Flag == W_FLAG_SP:
        return TRUE
    else:
        return FALSE


#
# IsRightHandAutomaticObject
#
def IsRightHandAutomaticObject(EntityName):
	me=Bladex.GetEntity(EntityName)
	if not me.InvRight:
		return FALSE

	# Get object type
	object_flag= Reference.GiveObjectFlag(me.InvRight)
	return object_flag == Reference.OBJ_USEME


#
# ShieldOnLeft
#
"""
def ShieldOnLeft(EntityName):
	me=Bladex.GetEntity(EntityName)
	if not me.InvLeft:
		return FALSE

	# Get object type
	object_flag= Reference.GiveObjectFlag(me.InvLeft)
	return object_flag == Reference.OBJ_USEME
"""

#################
#
#  A C T I O N S
#
#################

#
# Turning Actions -> Shoudl NOT be here!
#

def IsBehindEntity(MyName, OtherName):
	them=Bladex.GetEntity(OtherName)
	angle1 = them.Angle
	angle2 = B3DLib.GetEntity2EntityAngle (OtherName, MyName)
	return abs (B3DLib.DiffAngle (angle1, angle2))  >=  BEHINDANGLE


def IsFacingEntity(MyName, OtherName):
	me=Bladex.GetEntity(MyName)
	angle1 = me.Angle
	angle2 = B3DLib.GetEntity2EntityAngle (MyName, OtherName)
	return abs (B3DLib.DiffAngle (angle1, angle2))  <=  FACINGANGLE

def IsFacingPos(MyName, x, z):
	me=Bladex.GetEntity(MyName)
	angle1 = me.Angle;
	p1=me.Position
	x = x-p1[0]
	z = z-p1[2]
	angle2 = B3DLib.GetXZAngle (x, 0.0, z)
	return abs (B3DLib.DiffAngle (angle1, angle2))  <=  FACINGANGLE

def Turn180(MyName):
	me=Bladex.GetEntity(MyName)
	angle = me.Angle+PI
	if angle >= TWOPI:
		angle = angle - TWOPI
	me.Face(angle)

def QuickTurn180(MyName):
	me=Bladex.GetEntity(MyName)
	angle = me.Angle+PI
	if angle >= TWOPI:
		angle = angle - TWOPI
	me.QuickFace(angle)

def TurnToFaceEntity(MyName, OtherName):
	me=Bladex.GetEntity(MyName)
	angle = B3DLib.GetEntity2EntityAngle (MyName, OtherName)
	me.Face(angle)

def TurnToFaceEntityNow(MyName, OtherName):
	me=Bladex.GetEntity(MyName)
	angle = B3DLib.GetEntity2EntityAngle (MyName, OtherName)
	me.Angle = angle

def QuickTurnToFaceEntity(MyName, OtherName):
	me=Bladex.GetEntity(MyName)
	angle = B3DLib.GetEntity2EntityAngle (MyName, OtherName)
	me.QuickFace(angle)

def TurnToFacePos(MyName, x, z):
	me=Bladex.GetEntity(MyName)
	p1=me.Position
	x = x-p1[0]
	z = z-p1[2]
	angle = B3DLib.GetXZAngle (x, 0.0, z)
	me.Face(angle)

def QuickTurnToFacePos(MyName, x, z):
	me=Bladex.GetEntity(MyName)
	p1=me.Position
	x = x-p1[0]
	z = z-p1[2]
	angle = B3DLib.GetXZAngle (x, 0.0, z)
	me.QuickFace(angle)





#
# Using Actions
#

# Use locations
USE_FROM_INV=0
USE_FROM_NEARBY=2
USE_FROM_TAKE=4





        
        

def StdUse (EntityName):
	me = Bladex.GetEntity(EntityName)

	if me.Wuea==Reference.WUEA_ENDED:
		return FALSE

	if me.Wuea==Reference.WUEA_WAIT:
		return FALSE

	if me.AnimName=="Rlx" and me.AnmEndedFunc:
		me.AnmEndedFunc= None

	#Para evitar bug de usar un segundo objeto indefinidamente
	if me.AnmEndedFunc:
		return FALSE



	###Reference.debugprint (EntityName + ": In StdUse")
	TryWithAnother = 1
	if (me.Name[0:6]=="Player") and (me.Data.InventoryActive):
		inv = me.GetInventory()
		object_name = inv.GetSelectedObject()
		if object_name:
			###Reference.debugprint (EntityName + ": Using "+object_name)
			object = Bladex.GetEntity(object_name)
			if object and object.CanUse:
				me.Data.obj_used=object
				InitDataField.Initialise(object)
				object.Data.UsedBy = EntityName
				object.UseFunc(object_name, USE_FROM_INV)
				TryWithAnother = 0


	if TryWithAnother:
		if me.Data and me.Data.selected_entity:
			UsingFailed=0                # Added
			TakingFailed=0               #
			if IsValidForUsing (me.Data.selected_entity[0], EntityName):
				object_flag= Reference.GiveObjectFlag(me.Data.selected_entity[0])
				if object_flag!=Reference.OBJ_USEME and object_flag!=Reference.OBJ_ITEM:	# Automatics get picked up first
					object = Bladex.GetEntity(me.Data.selected_entity[0])
					me.Data.obj_used=object
					InitDataField.Initialise(object)
					object.Data.UsedBy = EntityName
					object.UseFunc(object.Name, USE_FROM_NEARBY)
					return
				else:
					UsingFailed=1

			if IsValidForTaking (me.Data.selected_entity[0]):
				me.Data.toggle4t_clearback= FALSE
				me.Data.stuff_onback_b4= SthOnBack(EntityName)
				if TryToTake(EntityName, me.Data.selected_entity[0]):
					return
				else:
					TakingFailed=1

			else:
				# if(Bladex.IsUseMsgActive()==0):       # PLAGUE: this function literally does nothing and always returns 1. Might be a deprecated function.
				if UsingFailed and TakingFailed and (Bladex.IsUseMsgActive()==0):       # I don't remember why I started doing this, please send help. -LeadHead
					return
				ReportMsg ("The selected object cannot be taken")
		else:
			if(Bladex.IsUseMsgActive()==0):
				return
			ReportMsg ("Nothing selected")


def IsValidForUsing(instance_name, EntityName):
	me = Bladex.GetEntity(EntityName)
	object = Bladex.GetEntity(instance_name)

	if not me or not object or not object.CanUse or not object.UseFunc:
		return FALSE

	dist = B3DLib.GetXZDistance (EntityName, instance_name)
	chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)

	# Is it too far?
	if dist > chartype.Reach*1.5:	# Patch because we extend our reach to use (e.g. with a torch)
		ReportMsg ("Not in reach")  # Added -LeadHead
		return FALSE


	# Is it too low?
	heightdiff = -(object.Position[1] - (me.Position[1]+me.Dist2Floor))
	if heightdiff < chartype.MinTake:
		ReportMsg ("Not in reach")  # Added -LeadHead
		return FALSE

	#Is it too high?
	if heightdiff > chartype.MaxTake5:
		ReportMsg ("Not in reach")  # Added -LeadHead
		return FALSE

	return TRUE

def has_torch (EntityName):
	me=Bladex.GetEntity (EntityName)
	obj_name = me.InvRight
	if obj_name:
		obj = Bladex.GetEntity(obj_name)
		if obj:
			return obj.Kind == "Antorcha"       # PLAGUE: We never even check if it's lit???
	return 0


def DestroyBurningItem (EntityName, DestroyTime):
	###Reference.debugprint (EntityName + ": Im being destroyed")
	obj=Bladex.GetEntity(EntityName)
	#obj.SubscribeToList("Pin")
	if obj:
		try:
			if not obj.Data.brkobjdata:
				Breakings.SetBreakable(EntityName, DestroyTime, DestroyTime)
		except:
			Breakings.SetBreakable(EntityName, DestroyTime, DestroyTime)

		###Reference.debugprint (EntityName + ": Setting Light to pieces with destroy time " + `DestroyTime`)
		brkobj=obj.Data.brkobjdata
		Breakings.ExplodeSpecialObject (EntityName, 3500.0)

	# Set light to the pieces
	###Reference.debugprint (EntityName + ": Setting Light to pieces...")
	try:
		for n in brkobj.n_piezas:
			brkobj.pieza[n].CatchOnFire(0.0,0.0,0.0)
	except:
		pass



def StdSetFireToUseFunc(ObjectName,use_from):
	object=Bladex.GetEntity(ObjectName)
	from_pos = (0.0, 0.0, 0.0)
	if use_from==USE_FROM_INV or use_from==USE_FROM_NEARBY or use_from==USE_FROM_TAKE:
		EntityName = object.Data.UsedBy
		me = Bladex.GetEntity(EntityName)
		if me:
			if not has_torch (EntityName):
				ReportMsg ("The selected object cannot be taken")   # Added -LeadHead
				return 0
			torch = Bladex.GetEntity(me.InvRight)
			if torch.Data.torchobjdata.LightStatus==Torchs.OFF:
				ReportMsg ("The selected object cannot be taken")   # Added -LeadHead
				return 0
			object.UseFunc = 0
			object.Data.UsedBy = me.InvRight
			QuickTurnToFaceEntity (EntityName, ObjectName)
			# Launch the set fire to animation depending on the height diff
			heightdiff = -(object.Position[1] - (me.Position[1]+me.Dist2Floor))
			chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)

			me.AddAnmEventFunc("SetAlightEvent",SetAlightEventHandler)
			if heightdiff <= chartype.MaxTake1:
				me.LaunchAnmType("fire_g")
			elif heightdiff <= chartype.MaxTake2:
				me.LaunchAnmType("fire0")
			elif heightdiff <= chartype.MaxTake3:
				me.LaunchAnmType("fire1")
			elif heightdiff <= chartype.MaxTake4:
				me.LaunchAnmType("fire2")
			elif heightdiff <= chartype.MaxTake5:
				me.LaunchAnmType("fire3")
			return 1

def SetAlight (ObjectName):
	object = Bladex.GetEntity (ObjectName)
	if object:
		try:
			UserName = object.Data.UsedBy
			user = Bladex.GetEntity(UserName)
			user_pos = user.Position
		except:
			user_pos = (0.0, 0.0, 0.0)
		object.CatchOnFire(user_pos[0], user_pos[1], user_pos[2])
		###Reference.debugprint("Setting "+ ObjectName +" alight")
		# Set up the destruction of the item
		# after a given amount of time
		if object.Data.BurnTime:
			Bladex.AddScheduledFunc(Bladex.GetTime()+object.Data.BurnTime, DestroyBurningItem,(ObjectName,object.Data.DestroyTime,),"SetAlight"+ObjectName)

def SetBurnable (EntityName, BurnTime, DestroyTime):
	object=Bladex.GetEntity(EntityName)
	object.UseFunc = StdSetFireToUseFunc
	InitDataField.Initialise(object)
	object.Data.BurnTime = BurnTime
	object.Data.DestroyTime = DestroyTime

def SetAlightEventHandler(EntityName, EventName):
	me = Bladex.GetEntity(EntityName)
	me.DelAnmEventFunc(EventName)
	###Reference.debugprint(EntityName+": in SetAlightEventHandler")
	# Check valid event type
	if EventName != "SetAlightEvent":
		###Reference.debugprint(EntityName+":-( SetAlightEventHandler has unhandled event")
		return

	object = me.Data.obj_used
	if object:
		SetAlight(object.Name)


# Taking Actions
#

"""
		Valid Object Checks

"""
def IsValidForTaking(instance_name):
	object = Bladex.GetEntity(instance_name)
	if(object):
		if object.Static or (object.Weapon and object.WeaponMode==Reference.ACTIVE_WEAPON_MODE):
			###Reference.debugprint(instance_name+" is static and cannot be taken")
			return FALSE
		if object.Parent:
			parent=Bladex.GetEntity(object.Parent)
			if parent and parent.Person:
				return FALSE
		if object.Data and "Takeable" in dir(object.Data) and not object.Data.Takeable:
			return FALSE
		object_data = None
		if Reference.EntitiesObjectData.has_key(instance_name):
			object_data = Reference.EntitiesObjectData[instance_name]
		elif Reference.DefaultObjectData.has_key(object.Kind):
			object_data = Reference.DefaultObjectData[object.Kind]
		if not object_data:
			###Reference.debugprint ("The object " + instance_name + " of type " + object.Kind + " is not referenced in any dictionary.")
			return FALSE
		# if its an automatic, and does't have a use func
		if object_data[0] == Reference.OBJ_USEME and not object.CanUse:
			###Reference.debugprint ("The object " + instance_name + " cannot be used.")
			return FALSE

	return TRUE

def IsValidForThrowing(object_name):
	object = Bladex.GetEntity(object_name)
	if(object):
		# Get object type
		if Reference.EntitiesObjectData.has_key(object_name):
			object_data = Reference.EntitiesObjectData[object_name]
		elif Reference.DefaultObjectData.has_key(object.Kind):
			object_data = Reference.DefaultObjectData[object.Kind]
		else:
			return FALSE
		object_flag = object_data[0]
		if object_flag == Reference.OBJ_WEAPON or object_flag == Reference.OBJ_BOW or object_flag == Reference.OBJ_STANDARD:
			return TRUE
	return FALSE

def IsValidForDropping(ObjectName):
	if Reference.EntitiesObjectData.has_key(ObjectName):
		object_data = Reference.EntitiesObjectData[ObjectName]
	else:
		object = Bladex.GetEntity(ObjectName)
		if not Reference.DefaultObjectData.has_key(object.Kind):
			return TRUE
		object_data = Reference.DefaultObjectData[object.Kind]

	object_flag = object_data[0]

	# Should check against our drop tables, when they are created
	if object_flag == Reference.OBJ_KEY:
		return FALSE
	elif object_flag == Reference.OBJ_SPECIALKEY:
		return FALSE
	elif object_flag == Reference.OBJ_TABLET:
		return FALSE
	elif object_flag == Reference.OBJ_ITEM:
		return FALSE
	else:
		return TRUE

def GetCheckSelected (func, Data):
	if Data:
		if Data.selected_entity:
			s = Data.selected_entity[0]
			if func(s):
				return s
	return None

def DropToMakeRoomFor (EntityName, ObjectName):
	me = Bladex.GetEntity(EntityName)

	# Get object type
	object_flag=Reference.GiveObjectFlag(ObjectName)
	inv = me.GetInventory()

	# parse the object flag
	DropObjectName= None
	if object_flag == Reference.OBJ_ARMOUR:
		print "Warning DropToMakeRoomFor() unimplimented for Armour..."
	elif object_flag == Reference.OBJ_ITEM:
		ObjectKind =  Bladex.GetEntity(ObjectName).Kind
		for i in range(inv.nObjects):
			auxname = inv.GetObject(i)
			if auxname:
				if Bladex.GetEntity(auxname).Kind == ObjectKind:
					DropObjectName= auxname
					break
			else: break
	elif object_flag == Reference.OBJ_SHIELD:
		DropObjectName= inv.GetShield(0)
	elif object_flag == Reference.OBJ_WEAPON:
		DropObjectName= inv.GetWeapon(0)
	elif object_flag == Reference.OBJ_BOW:
		if inv.HasBow:
			DropObjectName= inv.GetBow()
		else:
			DropObjectName= inv.GetWeapon(0)
	elif object_flag == Reference.OBJ_QUIVER:
		DropObjectName= inv.GetQuiver(0)
	elif object_flag == Reference.OBJ_STANDARD:
		DropObjectName= me.InvRight
	elif object_flag == Reference.OBJ_KEY:
		print "Warning DropToMakeRoomFor() unimplimented for Keys..."
	elif object_flag == Reference.OBJ_SPECIALKEY:
		print "Warning DropToMakeRoomFor() unimplimented for Special Keys..."
	elif object_flag == Reference.OBJ_TABLET:
		print "Warning DropToMakeRoomFor() unimplimented for Tablets..."
	elif object_flag == Reference.OBJ_USEME:
		DropObjectName= me.InvRight
	elif object_flag == Reference.OBJ_ARROW:
		print "Warning DropToMakeRoomFor() unimplimented for Arrows..."

	if DropObjectName:
		object= Bladex.GetEntity(DropObjectName)
		if object:
			RemoveFromInventory (me, object, "DropToMakeRoomFor "+ObjectName)
			object.Position= me.Position
			object.ExcludeHitFor(me)
			if object.TestHit:
				object.RemoveFromWorld()
			else:
				object.Alpha= 1.0
				object.Impulse(0.0, 0.0, 0.0)

# Do we have all that we can carry of an object type
def IsOneTooMany (EntityName, ObjectName):
	me = Bladex.GetEntity(EntityName)
	# Get object type
	if Reference.EntitiesObjectData.has_key(ObjectName):
		object_data = Reference.EntitiesObjectData[ObjectName]
	else:
		object = Bladex.GetEntity(ObjectName)
		object_data = Reference.DefaultObjectData[object.Kind]

	object_flag = object_data[0]   

	ret_val=FALSE

	inv = me.GetInventory()
	#if object_flag == Reference.OBJ_ARMOUR:
	#	if me.CharTypeExt<>object_data[1]:
	#		ReportMsg ("Type of armour not for me")
	#		return TRUE
	#	if me.Data.armour_level>=object_data[2]:
	#		ReportMsg ("Quality of armour not worthy")
	#		return TRUE
	#	return FALSE
	#else:
	if object_flag == Reference.OBJ_ITEM:
		ret_val =  inv.nObjects >= inv.maxObjects
		if not ret_val:
			ObjectEntity =  Bladex.GetEntity(ObjectName)
			for i in range(inv.nObjects):
				auxname = inv.GetObject(i)
				if auxname:
					if Bladex.GetEntity(auxname).Kind == ObjectEntity.Kind:
						ret_val =  inv.GetMaxNumberObjectsAt(i)<=inv.GetNumberObjectsAt(i)
						break
				else:
					break
	elif object_flag == Reference.OBJ_SHIELD:
		ret_val = inv.nShields >= inv.maxShields
	elif object_flag == Reference.OBJ_WEAPON:
		ret_val = inv.nWeapons >= inv.maxWeapons
	elif object_flag == Reference.OBJ_BOW: #Corregir?
		ret_val = inv.nWeapons >= inv.maxWeapons or inv.HasBow
	elif object_flag == Reference.OBJ_QUIVER:
		ret_val= not CouldTakeQuiver(inv, ObjectName)
	elif object_flag == Reference.OBJ_STANDARD:
		#if me.InvRight and SthOnBack(EntityName):	# Check right hand is holding
		#	return TRUE
		#else:
		ret_val = FALSE
	elif object_flag == Reference.OBJ_KEY:
		ret_val = FALSE
		#return me.InvRight	# Check right hand is holding
	elif object_flag == Reference.OBJ_SPECIALKEY:
		ret_val = FALSE
	elif object_flag == Reference.OBJ_TABLET:
		ret_val = FALSE
		#return me.InvRight	# Check right hand is holding
	elif object_flag == Reference.OBJ_USEME:
		ret_val = FALSE
		#return me.InvRight 	# Check right hand is holding
	elif object_flag == Reference.OBJ_ARROW:
		# Check if we have a full quiver of these already
		# Do we have a quiver
		ret_val= not CouldSheatheArrow(inv, ObjectName)

	return ret_val


def TryToTake(EntityName, ObjectName):
	global TryToTakeCallBacks

	me = Bladex.GetEntity(EntityName)

	if me.Wuea==Reference.WUEA_ENDED:
		return FALSE
	if me.Wuea==Reference.WUEA_WAIT:
		return FALSE

	if me.AnimName=="Rlx" and me.AnmEndedFunc:
		me.AnmEndedFunc= None

	#Para evitar bug de coger un segundo objeto indegfinidamente
	if me.AnmEndedFunc:
		return FALSE

	inv=me.GetInventory()
	if inv.CarringObject(ObjectName):
		return FALSE

	object = Bladex.GetEntity(ObjectName)
	dist = B3DLib.GetXZDistance (EntityName, ObjectName)
	chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)

	# Is it too far?
	if dist > chartype.Reach:
		ReportMsg ("Not in reach")
		return FALSE

	# Is it too low?
	me.Data.last_heightdiff= -(object.Position[1] - (me.Position[1]+me.Dist2Floor))
	###Reference.debugprint ("START TAKE:  ObjPos: " + `object.Position[1]` + ", MyHeight: "+`me.Position[1]` + ", Dist2Floor: "+`me.Dist2Floor`+", HeightDiff = "+`me.Data.last_heightdiff`)
	###Reference.debugprint ("MinTake: "+`chartype.MinTake`+ ", MaxTake1: "+`chartype.MaxTake1`+ ", MaxTake2: "+`chartype.MaxTake2`+ ", MaxTake3: "+`chartype.MaxTake3`+ ", MaxTake4: "+`chartype.MaxTake4`+ ", MaxTake5: "+`chartype.MaxTake5`)
	if me.Data.last_heightdiff < chartype.MinTake:
		#pdb.set_trace()
		ReportMsg ("Too low to pick up")
		return FALSE

	# Is it too high?
	elif me.Data.last_heightdiff > chartype.MaxTake5:
		ReportMsg ("Too high to pick up")
		return FALSE

	# Do I have too many
	elif IsOneTooMany (EntityName, ObjectName):
		ReportMsg ("Too many objects of this type")
		return FALSE

    # Moved armour check here -LeadHead
	if Reference.EntitiesObjectData.has_key(ObjectName):
		object_data = Reference.EntitiesObjectData[ObjectName]
	else:
		object_data = Reference.DefaultObjectData[object.Kind]
	object_flag = object_data[0]

	if object_flag==Reference.OBJ_ARMOUR:

		if me.CharTypeExt<>object_data[1]:
			ReportMsg ("Type of armour not for me")
			print "Info is " + str(object_data[1])
			return FALSE
		if me.Data.armour_level>=object_data[2]:
			ReportMsg ("Quality of armour not worthy")
			return FALSE

	# If someone have something to say, speak now or keep silence forever!
	for f in TryToTakeCallBacks:
		if not f(me, object):
			return FALSE

	###Reference.debugprint(EntityName+": Im Taking"+ObjectName)
	QuickTurnToFaceEntity (EntityName, ObjectName)
	# Store the name of this for the PickupEvent
	me.Data.pickup_entity = ObjectName

	IntermediateTake(EntityName,ObjectName)

	return TRUE



def UnSheatheArrow(inv):
	des_quiver_name=inv.GetSelectedQuiver()
	inv.LinkRightHand("None")
	if des_quiver_name:
		inv.SetCurrentQuiver(des_quiver_name)
		inv.LinkRightBack("None")
		inv.LinkRightBack(des_quiver_name)
		quiver= Bladex.GetEntity(des_quiver_name)
		if quiver and quiver.Data.NumberOfArrows() > 0:
			arrow= quiver.Data.GiveArrow ()
			if arrow:
				inv.LinkRightHand(arrow.Name)
				return
	if inv.Owner == 'Player1':                                                                      # Previously would always reportMsg 
		ReportMsg ("Out of Arrows")                                                                 # Even if it wasn't the player who had no arrows
	else:                                                                                           #
		print "!!!ACTIONS.UNSHEATHEARROW ERROR!!! - Possible char with bow but no arrows spawned"   #       -LeadHead

def CouldTakeQuiver(inv, QuiverName):
	if inv.maxQuivers and not inv.nQuivers: # Skip all of this if have no quiver at all      
		return TRUE                         #
	me = Bladex.GetEntity(inv.Owner)        # -LeadHead
	ret_val = inv.nQuivers < inv.maxQuivers
	if ret_val:
		new_quiver=Bladex.GetEntity(QuiverName)
		for i in range (inv.nQuivers):
			quiver_name= inv.GetQuiver(i)
			quiver= Bladex.GetEntity(quiver_name)
			if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:                                  # Added.
				currentArrow=Bladex.GetEntity(me.InvRight)                                                                  # Fixes same bug as for CouldSheatheArrow
				if (currentArrow.Kind==new_quiver.Data.ArrowType) and (quiver.Data.ArrowType==new_quiver.Data.ArrowType):   # See explanation there
					return quiver.Data.NumberOfArrows() + 1 < quiver.Data.MaxArrows                                         #
				elif quiver.Data.ArrowType==new_quiver.Data.ArrowType:                                                      #
					return quiver.Data.NumberOfArrows() < quiver.Data.MaxArrows                                             #               -LeadHead
			elif quiver.Data.ArrowType==new_quiver.Data.ArrowType:
				return quiver.Data.NumberOfArrows() < quiver.Data.MaxArrows

	return ret_val

def CouldSheatheArrow(inv, ArrowName):          
	me = Bladex.GetEntity(inv.Owner)                       #       -LeadHead                      
	arrow=Bladex.GetEntity(ArrowName)

	for i in range (inv.nQuivers):
		quiver_name= inv.GetQuiver(i)
		quiver= Bladex.GetEntity(quiver_name)
		if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:                # Added.
			#print me.InvRight                                                                        # This fixes a bug that's caused by the disppearing quiver fix
			currentArrow=Bladex.GetEntity(me.InvRight)                                                # If you had an arrow in hand and a full quiver on back,
			if (quiver.Data.ArrowType==arrow.Kind) and (currentArrow.Kind==arrow.Kind):               # you would drop your current arrow and pick up another one immediately.
				#print currentArrow.Kind                                                              # We don't want to pick up an arrow if the one
				return quiver.Data.NumberOfArrows() < quiver.Data.MaxArrows - 1                       # we are holding would put us at maximum after sheathing -LeadHead
		elif quiver.Data.ArrowType==arrow.Kind:
			return quiver.Data.NumberOfArrows() < quiver.Data.MaxArrows
            
	# If we get this far, a quiver of the correct type was not encountered, so we could create one
	return TRUE

def SheatheArrow(inv, ArrowName):
	UnGraspString (inv.Owner,"UnGraspString")
	arrow=Bladex.GetEntity(ArrowName)
	for i in range (inv.nQuivers):
		quiver_name= inv.GetQuiver(i)
		quiver= Bladex.GetEntity(quiver_name)
		if quiver.Data.ArrowType==arrow.Kind:
			# Select this quiver
			inv.SetCurrentQuiver(quiver_name)
			if inv.HoldingBow:
				inv.LinkRightBack("None")
				inv.LinkRightBack(quiver_name)
			if quiver.Data.ReceiveArrow (arrow, inv.Owner):
				inv.LinkRightHand("None")
			else:
				# We have found a quiver of the correct type,
				# but it is probably full.  Just drop the arrow
				DropReleaseEventHandler(inv.Owner, "DropRightEvent", FALSE)
			return

	# If we get this far, a quiver of the correct type was not encountered, so we create one
	new_quiver_type= Reference.GiveQuiverType(arrow.Kind)
	if new_quiver_type:
		new_quiver= Bladex.CreateEntity(new_quiver_type+"_for_"+inv.Owner, new_quiver_type+'_E', 0,0,0, "Physic")
		ItemTypes.ItemDefaultFuncs (new_quiver)
		inv.AddQuiver(new_quiver.Name)
		inv.SetCurrentQuiver(new_quiver.Name)
		if inv.HoldingBow:
			inv.LinkRightBack(new_quiver.Name)
		new_quiver.Data.SetNumberOfArrows(0, inv.Owner)
		if new_quiver.Data.ReceiveArrow (arrow, inv.Owner):
			inv.LinkRightHand("None")
			return

	# If we get this far, a quiver of the correct type could not be created
	DropReleaseEventHandler(inv.Owner, "DropRightEvent", FALSE)


def Toggle4TakingEvent(pj_name,event):
	me=Bladex.GetEntity(pj_name)
	inv=me.GetInventory()
	me.DelAnmEventFunc(event)

	# If we're carrying an arrow in the right hand then we can put it back in the quiver
	if inv.HoldingBow:
		if me.InvRight:
			if Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
				SheatheArrow(inv, me.InvRight)	# We must be carrying an arrow in the right hand, lets sheathe it
		else:
			# Take an arrow
			UnSheatheArrow(inv)
	elif me.InvRightBack and Reference.GiveObjectFlag(me.InvRightBack)<>Reference.OBJ_QUIVER:
		#Pasar lo de right en espada a mano dch
		if (not me.Data.stuff_onback_b4) and me.Data.toggle4t_clearback:
			tmpr_back=me.InvRightBack
			inv.LinkRightBack("None")
			inv.LinkRightHand(tmpr_back)
		else:
			inv.LinkRightHand("None")
	else:
		if me.InvRight and (not me.Data.toggle4t_clearback):
			inv.LinkRightBack(me.InvRight)
		inv.LinkRightHand("None")

	if me.Data.toggle4t_clearback:
		me.Data.toggle4t_clearback= FALSE
		if me.InvLeftBack and Reference.GiveObjectFlag(me.InvLeftBack)==Reference.OBJ_BOW:
			ToggleWEvent(pj_name,event)

def ToggleRight4Taking(EntityName):
	me=Bladex.GetEntity(EntityName)

	if IsRightHandStandardObject(EntityName):
		if TryDropRight(EntityName):
			print "TryDropRight is ok"
			DropReleaseEventHandler(EntityName, "DropRightEvent")
			if me.InvRight:
				#print "Still stuff on riht!!!"
				ReportMsg ("Cannot be dropped")
				return FALSE
		me.Wuea=Reference.WUEA_ENDED


	if me.InvRight:
		#if Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW or (me.InvLeftBack and Reference.GiveObjectFlag(me.InvLeftBack)==Reference.OBJ_BOW):
		#	me.AddAnmEventFunc("ChangeRLEvent",Toggle4TakingEvent)
		#	me.LaunchAnmType("Chg_r_l")
		#else:
		me.AddAnmEventFunc("ChangeREvent",Toggle4TakingEvent)

		UnGraspString (EntityName,"UnGraspString")
		me.LaunchAnmType("Chg_r")

	return TRUE


def IntermediateTake(EntityName,ObjectName):
	me = Bladex.GetEntity(EntityName)
	object = Bladex.GetEntity(ObjectName)

	inv=me.GetInventory()
	if inv.CarringObject(ObjectName):
		return

	if inv.HoldingBow: UnGraspString(EntityName, "UnGraspString")
	# Get object type
	if Reference.EntitiesObjectData.has_key(ObjectName):
		object_data = Reference.EntitiesObjectData[ObjectName]
	else:
		object_data = Reference.DefaultObjectData[object.Kind]
	object_flag = object_data[0]

	if object_flag==Reference.OBJ_ARMOUR:

		if me.CharTypeExt<>object_data[1]:
			ReportMsg ("Type of armour not for me")
			print "Info is " + str(object_data[1])
			return
		if me.Data.armour_level>=object_data[2]:
			ReportMsg ("Quality of armour not worthy")
			return

		if (FreeBothHands(EntityName,None,(),0)):
			TakeMainAnm(EntityName)
		else:
			me.AnmEndedFunc=TakeMainAnm

	#Do we have sthing on the hands?
	if object_flag==Reference.OBJ_SHIELD:
		###Reference.debugprint("Taking a shield...")
		if me.InvRight:
			if ToggleRight4Taking(EntityName)==FALSE:
				return
			me.AnmEndedFunc=TakeMainAnm
		else:
			TakeMainAnm(EntityName)
	elif object_flag==Reference.OBJ_BOW:
		###Reference.debugprint("Taking a bow...")
		if me.InvRight:
			if ToggleRight4Taking(EntityName)==FALSE:
				return
			me.AnmEndedFunc=TakeMainAnm
		else:
			TakeMainAnm(EntityName)

	elif object_flag==Reference.OBJ_WEAPON:
		###Reference.debugprint("Taking a weapon ...")
		if me.InvRight:
			if ToggleRight4Taking(EntityName)==FALSE:
				return
			me.AnmEndedFunc=TakeMainAnm
		else:
			#Are taking a 2h W and do we have a shield? Store shield if so
			w_flag=Reference.GiveWeaponFlag(ObjectName)
			if me.InvLeft<>"" and w_flag<>Reference.W_FLAG_1H:
				me.AddAnmEventFunc("ChangeLEvent",Left2InvEvent)
				me.LaunchAnmType("Chg_l")
				me.AnmEndedFunc=TakeMainAnm
			else:
				TakeMainAnm(EntityName)
	elif object_flag==Reference.OBJ_STANDARD:
		###Reference.debugprint("Taking a standard object ...")
		if inv.HoldingBow:
			# We have a problem here because the standard object cannot
			# be used with the bow, and it cannot be put into the inventory.
			# The solution is to link the bow to the back
			if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
				SheatheArrow(inv, me.InvRight)
			inv.LinkLeftBack(me.InvLeft)
			inv.LinkLeftHand("None")

		if me.InvRight:
			if ToggleRight4Taking(EntityName)==FALSE:
				return
			me.AnmEndedFunc=TakeMainAnm
		else:
			TakeMainAnm(EntityName)
	else:
		###Reference.debugprint("Taking sthing thast is NOT shield/weapon/standard ...")
		if me.InvRight:
			if ToggleRight4Taking(EntityName)!=FALSE:
				me.AnmEndedFunc=TakeMainAnm
		else:
			TakeMainAnm(EntityName)


def ToggleAfterTakeObj(EntityName):
	me = Bladex.GetEntity(EntityName)
	me.AnmEndedFunc=None
	###Reference.debugprint("Im in ToggleAfterTakeObj")

	inv = me.GetInventory()

	if IsRightHandStandardObject(EntityName):
		return

	me.Data.toggle4t_clearback= TRUE
	if me.Data.stuff_onback_b4:
		###Reference.debugprint ("SthingOnBack b4 taking - End")
		if SthOnBack(EntityName):
			ToggleRight4Taking(EntityName)
		else:
			ToggleRight4Taking(EntityName)
	else:
		###Reference.debugprint ("NOthingOnBack b4 taking - End")
		ToggleRight4Taking(EntityName)

#
# Consulta
#
def TakeObject2Inv(EntityName):
	me = Bladex.GetEntity(EntityName)

	if not me.Data or not me.Data.pickup_entity:
		return FALSE

	object_flag= Reference.GiveObjectFlag(me.Data.pickup_entity)

	if object_flag==Reference.OBJ_ARROW and me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW:
		return FALSE

	back_flag=SthOnBack(EntityName)
	if back_flag and object_flag==Reference.OBJ_WEAPON:
		w_flag=Reference.GiveWeaponFlag(me.Data.pickup_entity)
		if w_flag<>Reference.W_FLAG_1H:
			back_flag=0

	weapon_stay=0
	if (not me.Data.stuff_onback_b4) and (not back_flag) and (object_flag == Reference.OBJ_WEAPON):
		if not me.InvLeft or Reference.GiveObjectFlag(me.InvLeft)!=Reference.OBJ_BOW:
			weapon_stay=1
	if object_flag <> Reference.OBJ_STANDARD and object_flag <> Reference.OBJ_USEME and (not weapon_stay):
		return TRUE
	return FALSE

def TakeObject2Left(EntityName):
	me = Bladex.GetEntity(EntityName)

	#
	# Not sure , but with the following the error of trying to take a weapon and WHEN TAKING , pressing the key to
	#take a shield , leaving the weapon on the LEFT hand ( and not taking the shield ) , , dissaers ( more or less )
	#
	if me.Data and not (me.Data.pickup_entity==me.InvRight):
		#print "    ERROR INVENT!!!!"
		#print "    pickup_entity is " + me.Data.pickup_entity
		if me.InvRight:
			#print "    Right was" + me.InvRight
			return FALSE



	if me.Data and me.Data.pickup_entity:
		if not me.InvLeft:
			object_flag= Reference.GiveObjectFlag(me.Data.pickup_entity)
			if object_flag==Reference.OBJ_SHIELD:
				#DO not left it in left hand if on back a 2hWeapon before taking it!
				#if me.Data.stuff_onback_b4==0 and TwoHandedWeaponOnBack(EntityName):
				if TwoHandedWeaponOnBack(EntityName):
					return FALSE
				if not me.InvLeftBack:
					return TRUE
			if object_flag==Reference.OBJ_BOW:
				# the bow requires both hands to be free
				if not me.InvLeftBack and not me.InvRightBack:
					return TRUE
	return FALSE

def RemoveRightHandler(EntityName, EventName):
	me = Bladex.GetEntity(EntityName)

	me.DelAnmEventFunc(EventName)
	inv=me.GetInventory()
	if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
		SheatheArrow(inv, me.InvRight)
	if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_QUIVER:     # Added
		AddQuiver(inv, me.InvRight)                                                     #  - LeadHead
	else:
		object_name= me.InvRight
		inv.LinkRightHand("None")
		try:
			if object_name and me.Data.obj2left:
				inv.LinkLeftHand(object_name)
			me.Data.obj2left= None
		except AttributeError:
			pass
		if me.InvLeftBack and Reference.GiveObjectFlag(me.InvLeftBack)==Reference.OBJ_SHIELD and (not me.InvRightBack):		# Added
			if Reference.GiveWeaponFlag(object_name)==Reference.W_FLAG_1H:													#
				inv.LinkRightBack(object_name)																				#	-LeadHead



def TakeArmour(EntityName):
	me = Bladex.GetEntity(EntityName)
	Data = me.Data
	ObjectName=Data.pickup_entity
	object=Bladex.GetEntity(ObjectName)

	# Get object type
	if Reference.EntitiesObjectData.has_key(ObjectName):
		object_data = Reference.EntitiesObjectData[ObjectName]
	else:
		object_data = Reference.DefaultObjectData[object.Kind]

	if object_data[0]<>Reference.OBJ_ARMOUR:
		print "ERROR in Actions.TakeArmour , object is not an armour!!!"
		return

	ct = Bladex.GetCharType(me.CharType,me.CharTypeExt)

	sound=Bladex.CreateSound("../../Sounds/cambio-armadura2.wav",EntityName+"SoundNewArmour")
	sound.Volume=0.6
	sound.MinDistance=10000
	sound.MaxDistance=20000
	sound.PlayStereo()

	right= me.InvRight
	left= me.InvLeft
	rightback= me.InvRightBack
	leftback= me.InvLeftBack


	inv= me.GetInventory()
	inv.LinkRightHand ("")
	inv.LinkLeftHand ("")
	inv.LinkBack("")

	Data.UnlinkAll (EntityName, "")  # Dettatch arrows
	me.ResetWounds()

	if object_data[2]==0:
		me.SetMesh(ct.NoArmour)
	elif object_data[2]==1:
		me.SetMesh(ct.LowArmour)
	elif object_data[2]==2:
		me.SetMesh(ct.MedArmour)
	elif object_data[2]==3:
		me.SetMesh(ct.HighArmour)
	else:
		print "ERROR in Actions.TakeArmour , armour level!!!"

	#
	# Link again the stuff
	#

	# Right Back
	if rightback:
		inv.LinkRightHand (rightback)
		inv.LinkRightBack(rightback)
	# Left Back
	if leftback:
		inv.LinkLeftHand (leftback)
		inv.LinkLeftBack(leftback)

	# Right hand
	if right:
		inv.LinkRightHand (right)
	# Left hand
	if left:
		inv.LinkLeftHand (left)


	Data.armour_level=object_data[2]
	Data.armour_prot_factor=object_data[3]

	object.SubscribeToList("Pin")

	# to fix bug with taking objects later.....
	me=Bladex.GetEntity(EntityName)
	if me:
		me.AnmEndedFunc(EntityName)
	else:
		pass

	return

def TakeMainAnm(EntityName):
	me = Bladex.GetEntity(EntityName)
	chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)

	#MOvido mas abajo!!!
	#obj2inv=TakeObject2Inv(EntityName)
	#me.Data.obj2left= TakeObject2Left(EntityName)


	# Added by Manuel --->
	object_name=me.Data.pickup_entity
	ret=OnInitTake.OnInitTakeFunc(object_name)

	if OnInitTake.InitTakeDictionary.has_key(object_name) and not ret:
		return FALSE

	if not me.Data.pickup_entity:
		return FALSE
	# <---Added by Manuel


	inv=me.GetInventory()
	if inv.CarringObject(object_name):
		#print "---------CARRING IT ALREADY - Skipping"
		return FALSE

	obj2inv=TakeObject2Inv(EntityName)
	me.Data.obj2left= TakeObject2Left(EntityName)

	if Reference.GiveObjectFlag(object_name)==Reference.OBJ_ARMOUR:
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.5, AuxFuncs.FadeTo, (0.5, 0.5))
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, TakeArmour, (EntityName,))


	elif me.Data.last_heightdiff <= chartype.MaxTake1:
		if obj2inv:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.AddAnmEventFunc("Key_down",RemoveRightHandler)
			me.LaunchAnmType("tke_r_key00")
		else:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.LaunchAnmType("tke_r_01")
		###Reference.debugprint (me.AnimName)
	elif me.Data.last_heightdiff <= chartype.MaxTake2:
		if obj2inv:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.AddAnmEventFunc("Key_down",RemoveRightHandler)
			me.LaunchAnmType("tke_r_key01")
		else:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.LaunchAnmType("tke_r_02")
		###Reference.debugprint (me.AnimName)
	elif me.Data.last_heightdiff <= chartype.MaxTake3:
		if obj2inv:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.AddAnmEventFunc("Key_down",RemoveRightHandler)
			me.LaunchAnmType("tke_r_key02")
		else:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.LaunchAnmType("tke_r_03")
		###Reference.debugprint (me.AnimName)
	elif me.Data.last_heightdiff <= chartype.MaxTake4:
		if obj2inv:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.AddAnmEventFunc("Key_down",RemoveRightHandler)
			me.LaunchAnmType("tke_r_key03")
		else:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.LaunchAnmType("tke_r_04")
		###Reference.debugprint (me.AnimName)
	elif me.Data.last_heightdiff <= chartype.MaxTake5:
		if obj2inv:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.AddAnmEventFunc("Key_down",RemoveRightHandler)
			me.LaunchAnmType("tke_r_key04")
		else:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.LaunchAnmType("tke_r_05")
		###Reference.debugprint (me.AnimName)
	else:
		print "Error in SubTake (last_height_diff) , Actions.py"
		if obj2inv:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.AddAnmEventFunc("Key_down",RemoveRightHandler)
			me.LaunchAnmType("tke_r_key04")
		else:
			me.AddAnmEventFunc("PickupEvent",PickupEventHandler)
			me.LaunchAnmType("tke_r_05")
		###Reference.debugprint (me.AnimName)

	if Reference.GiveObjectFlag(object_name)==Reference.OBJ_ARMOUR:
		return

	if obj2inv:
		me.AnmEndedFunc=TakeStraightRecover
	else:
		me.AnmEndedFunc=MainTake2Inv
		# if me.InvRightBack and Reference.GiveObjectFlag(me.InvRightBack)==Reference.OBJ_QUIVER:       # Commented out. Fixes disappearing quivers -LeadHead
			# inv.LinkRightBack("None")
	return TRUE


def TakeStraightRecover(EntityName):
	me = Bladex.GetEntity(EntityName)

	me.Data.toggle4t_clearback= TRUE
	if (not me.Data.stuff_onback_b4) and (SthOnBack(EntityName) or (me.InvRightBack and Reference.GiveObjectFlag(me.InvRightBack)==Reference.OBJ_QUIVER)):
		if me.InvRightBack and Reference.GiveObjectFlag(me.InvRightBack)==Reference.OBJ_QUIVER:     # Bugfix
			quiver = Bladex.GetEntity(me.InvRightBack)                                              # If we have a quiver on back, but no arrows in it, don't try to draw arrows.
			if quiver.Data.NumberOfArrows() < 1: return                                             #       -LeadHead
            
		me.AddAnmEventFunc("ChangeREvent",Toggle4TakingEvent)
		UnGraspString (EntityName,"UnGraspString")
		me.LaunchAnmType("Chg_r")
		#ToggleRight4Taking(EntityName)


def MainTake2Inv(EntityName):
	me = Bladex.GetEntity(EntityName)

	if not me.Data or not me.Data.pickup_entity:
		return

	#IS the object left in the right hand ?
	object_name = me.Data.pickup_entity

	if IsRightHandStandardObject(EntityName):
		###Reference.debugprint("Object not 2 inv . Standard object.")
		return
	if IsRightHandAutomaticObject(EntityName):
		###Reference.debugprint("Object not 2 inv . Automatic object.")
		return

	object_flag= Reference.GiveObjectFlag(object_name)
	if object_flag==Reference.OBJ_ARROW and me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW:
		return

	if (not me.Data.stuff_onback_b4) and (not SthOnBack(EntityName)) and IsRightHandWeaponObject(EntityName):
		###Reference.debugprint("Nthing on back now nor b4 taking  . Skipping ToggleAfterTakeObj.")
		return

	ToggleAfterTakeObj(EntityName)

def PickupEventHandler(EntityName, EventName, force_take=TRUE):
	me = Bladex.GetEntity(EntityName)

	if EventName != "PickupEvent":
		###Reference.debugprint(EntityName+":-( PickupEventHandler has unhandled event")
		return

	# Check the object is valid
	if not me.Data or not me.Data.pickup_entity:
		return

	if Bladex.GetEntity(me.Data.pickup_entity)==None:
		return

	object_name = me.Data.pickup_entity

	dist = B3DLib.GetXZDistance (EntityName, object_name )
	chartype = Bladex.GetCharType(me.CharType,me.CharTypeExt)

	# Is it too far?
	if dist > chartype.Reach*1.5:
		ReportMsg ("Not in reach")
		# to fix problem when 2 chars go to pickup same item (or enemy archer and player go for same arrow)
		return FALSE

	me.InterruptCombat()	# This may be necessary if a queued attack has the wrong flags
	object =Bladex.GetEntity(object_name)

	if object.Parent:
		parent= Bladex.GetEntity(object.Parent)
		if parent.Person:
			# also to fix problem when 2 chars go to pickup same item (or enemy archer and player go for same arrow)
			return
		parent.Unlink(object)

	#print "PickupEventHandler "+EntityName+", "+EventName+", "+object_name

	if object.Data and "Takeable" in dir(object.Data) and not object.Data.Takeable:
		return FALSE

	### /    Added by Dario    \ ####
	Ontake.OnTakeFunc(object_name)
	Stars.DeTwinkle(object_name)
	### \   Added by Dario     / ####

	###Reference.debugprint(EntityName+":-) Im picking up " + object_name)
	me.Data.selected_entity = None
	me.DelAnmEventFunc(EventName)

	if IsOneTooMany (EntityName, object_name):
		# Should never get here, as its checked before trying to take, but as scripts do weird things...
		if force_take:
			DropToMakeRoomFor(EntityName, object_name)
		else:
			print (EntityName+": Too many objects of this type: "+object_name)
			return

	# Get object type
	object_flag= Reference.GiveObjectFlag(object_name)

	inv = me.GetInventory()

	#NEW : So after taking , we launch the Chg_r anm...
	weapon_added=FALSE
	if not me.InvRight:		# Check right hand is still free
		if object_flag == Reference.OBJ_WEAPON:
			flag=Reference.GiveWeaponFlag(object_name)
			inv.AddWeapon(object_name,flag)
			WeaponName = Bladex.GetEntity(object_name).Kind
			weapon_added=TRUE
			if(netgame.GetNetState()==0):
				if (not me.Data.NPC) and not me.Data.WasObjectAlreadyTaken(object_name):
					# Race-Ordered Weapons, originals were wrong. Should be fixed now -LeadHead
					KnightWeaps = [	"QueenSword","IceSword","FireSword","Gladius","Espadaelfica" ,
									"Espadaromana","Espadacurva","Dagesse","Cimitarra","Espadafilo",
									"Espada","Maza","Maza2","Maza3","HookSword","DoubleSword"]

					DwarfWeaps = [	"QueenSword","CrushHammer","FireAxe","IceHammer","Hacha","Hacha5","Hacha4","Hacha3",
									"Hacha6","Hacha2","Garrote","Martillo","Martillo2","Garropin","MazaDoble",
									"Garrote2","Martillo3"]

					AmazonWeaps = [	"QueenSword","SteelFeather","FireBo","IceWand","LanzaAncha","Bichero",
									"Bo","Lanza","Naginata","Tridente","Arpon","Axpear","Crosspear",
									"Hachacuchilla","Naginata2","DeathBo","CrushBo"]

					BarbWeaps  = [	"QueenSword","FireBigSword","IceAxe","Chaosword",
									"DeathSword","LongSword","Alfanje","BigSword","SawSword","FlatSword",
									"Eclipse","Guadanya","Hacha2hojas","RhinoClub","Hacharrajada"]

					char = Bladex.GetEntity("Player1")

					import Scorer
					"""
					#############
					#   All of this is absolutely stupid. Instead of checking whether a weapon we picked up belongs to our char.Kind,
					#   it checks if the weapon is not in any other character's list. What mad man does something like this?
					#   It also parses 3 separate lists which is slow and non-aligned weapons end up triggering the script. 
					#############
					
					if char.Kind == "Barbarian_N":
						if  (
							(not AmazonWeaps.count(WeaponName)) and
							(not  DwarfWeaps.count(WeaponName)) and
							(not KnightWeaps.count(WeaponName))
							):
							Scorer.SlideTBS(0)

					if char.Kind == "Amazon_N":
						if  (
							(not   BarbWeaps.count(WeaponName)) and
							(not  DwarfWeaps.count(WeaponName)) and
							(not KnightWeaps.count(WeaponName))
							):
							Scorer.SlideTBS(0)

					if char.Kind == "Dwarf_N":
						if  (
							(not AmazonWeaps.count(WeaponName)) and
							(not   BarbWeaps.count(WeaponName)) and
							(not KnightWeaps.count(WeaponName))
							):
							Scorer.SlideTBS(0)

					if char.Kind == "Knight_N":
						if  (
							(not AmazonWeaps.count(WeaponName)) and
							(not  DwarfWeaps.count(WeaponName)) and
							(not   BarbWeaps.count(WeaponName))
							):
							Scorer.SlideTBS(0)
							"""
						### Re-written in a sensible manner -LeadHead
					if char.Kind[:9]=="Barbarian":
						if BarbWeaps.count(WeaponName):
							Scorer.SlideTBS(0)
					elif char.Kind[:6]=="Knight":
						if KnightWeaps.count(WeaponName):
							Scorer.SlideTBS(0)
					elif char.Kind[:6]=="Amazon":
						if AmazonWeaps.count(WeaponName):
							Scorer.SlideTBS(0)
					elif char.Kind[:5]=="Dwarf":
						if DwarfWeaps.count(WeaponName):
							Scorer.SlideTBS(0)
					else:
						print ("!!ERROR @ ACTIONS.PY!! - Couldn't parse char.Kind!")

		inv.LinkRightHand (object_name)


	if object_flag == Reference.OBJ_ITEM:
		ExtendedTakeObject(inv,object_name)
	elif object_flag == Reference.OBJ_SHIELD:
			###Reference.debugprint("AddShield... " + object_name +" ok ?")
			inv.AddShield(object_name)
	elif object_flag == Reference.OBJ_WEAPON:
		if weapon_added==FALSE:
			flag=Reference.GiveWeaponFlag(object_name)
			inv.AddWeapon(object_name,flag)
			if (not me.Data.NPC) and not me.Data.WasObjectAlreadyTaken(object_name):
				import Scorer
				Scorer.SlideTBS(0)

	elif object_flag == Reference.OBJ_BOW:	#Corregir?
		inv.AddBow(object_name)
	elif object_flag == Reference.OBJ_QUIVER:
		# AddQuiver(inv, object_name)                           # Part of quiver fix
		# print "PickupEventHandler - AddQuiver skipped!"       # 
		pass                                                    # -LeadHead
	elif object_flag == Reference.OBJ_STANDARD:
		pass
	elif object_flag == Reference.OBJ_KEY:
		inv.AddKey(object_name)
	elif object_flag == Reference.OBJ_SPECIALKEY:
		inv.AddSpecialKey(object_name)
	elif object_flag == Reference.OBJ_TABLET:
		inv.AddTablet(object_name)
	elif object_flag == Reference.OBJ_USEME:
		#me.TakeObject(object_name)
		if IsValidForUsing (object_name, EntityName):
			###Reference.debugprint(EntityName+":-) Will Use... " + object_name)
			me.Data.obj_used= Bladex.GetEntity(object_name)
			object= Bladex.GetEntity(object_name)
			object.Data.UsedBy= EntityName
			object.UseFunc(object_name, USE_FROM_TAKE)			# Need to link this object to the player first
		else:
			pass
			###Reference.debugprint(EntityName+":-) Cannot use " + object_name)
	elif object_flag == Reference.OBJ_ARROW and not inv.HoldingBow:
		#SheatheArrow(inv, object_name)
		pass

	me.Data.RegisterObjectAsTaken(object_name)


#
# Throwing Actions
#
def ThrowTime2ThrowForce(throw_pressed):
	curve_f= 3.0
	if throw_pressed<Reference.THROW_TIME_MIN:
		MinThrowForce= Reference.THROW_TIME_MIN / Reference.THROW_TIME_MAX
		MinThrowForce= pow (MinThrowForce, curve_f)
		ThrowForce= throw_pressed/Reference.THROW_TIME_MIN * MinThrowForce
	elif throw_pressed<Reference.THROW_TIME_MAX:
		ThrowForce= min (throw_pressed, Reference.THROW_TIME_MAX) / Reference.THROW_TIME_MAX
		ThrowForce= pow (ThrowForce, curve_f)
	else:
		ThrowForce= 1.0
	return ThrowForce

def TestThrowRight(EntityName):
	me = Bladex.GetEntity(EntityName)

	throw_pressed = Bladex.GetTimeActionHeld ("Throw")
	if not throw_pressed:
		return

	#attack_pressed = Bladex.GetTimeActionHeld ("Attack")
	#if not attack_pressed:
	#	return

	#if throw_pressed < attack_pressed:
	#	return

	if throw_pressed < Reference.THROW_TIME_MIN:
		if(netgame.GetNetState()!=2):
			TryDropRight(EntityName)
		else:
			netgame.SendUserString(Netval.NET_GAME_THROW_WEAPON,netgame.GetClientId()+" "+`-1`)
	else:
		if(netgame.GetNetState()!=2):
			# Clamp and normalize the force, record for later
			me.Data.ThrowForce = ThrowTime2ThrowForce (throw_pressed)
			StdThrowObject (EntityName)
		else:
			netgame.SendUserString(Netval.NET_GAME_THROW_WEAPON,netgame.GetClientId()+" "+`ThrowTime2ThrowForce (throw_pressed)`)

def EnterThrowingMode(EntityName):
	pass

def TestThrowLeft(EntityName):
	me = Bladex.GetEntity(EntityName)
	#print(EntityName+": In TestThrowLeft")
	###Reference.debugprint(EntityName+": In TestThrowLeft")

	throw_pressed = Bladex.GetTimeActionHeld ("Throw")
	###Reference.debugprint(EntityName+": In TestThrowLeft: throw_pressed = "+`throw_pressed`)
	if not throw_pressed:
		return

	# Only capable so far of dropping with the left
	TryDropLeft (EntityName)

# Requires that me.Data.ThrowForce has been set up
def StdThrowObject(EntityName):
	me = Bladex.GetEntity(EntityName)
	###Reference.debugprint(EntityName+": Im in StdThrowObject")
	# Have I got anything in the right hand
	statR = StatR(EntityName)
	if statR <> RA_NO_WEAPON and statR <>RA_BOW:
		###Reference.debugprint(EntityName+': Right hand obj = '+me.InvRight)
		object = Bladex.GetEntity(me.InvRight)
		if IsValidForThrowing (object.Name):
			#if object.TestHit:
			#	###Reference.debugprint(EntityName+": Pre-colliding - abandoning throw")
			#	return
			object.ExcludeHitFor(me)
			mass = object.Mass
			###Reference.debugprint ("Mass is "+`mass`)
			if mass <= Reference.LightMassMax:
				# In Combat Light Object Animation
				me.AddAnmEventFunc("ThrowLightFacingEvent",ThrowReleaseEventHandler)
				me.LaunchAnmType("1tw_l_f")
				###Reference.debugprint (me.AnimName)
			else:
				# In Combat Heavy Object Animation
				me.AddAnmEventFunc("ThrowHeavyFacingEvent",ThrowReleaseEventHandler)
				me.LaunchAnmType("1tw_h_f")
				###Reference.debugprint (me.AnimName)
		else:
			ReportMsg ("Cannot be thrown")
			StdDropObject(EntityName)


def RemoveFromInventory (me, object, EventName):

	me.Unlink(object)
	inv = me.GetInventory()

	object_name = object.Name

	if object_name==me.InvRight:
		me.RemoveFromInventRight()

	if object_name==me.InvLeft:
		me.RemoveFromInventLeft()

	# Get object type
	object_flag= Reference.GiveObjectFlag(object_name)

	if object_flag == Reference.OBJ_ITEM:
		inv.RemoveObject(object_name)
	elif object_flag == Reference.OBJ_SHIELD:
		inv.RemoveShield(object_name)
	elif object_flag == Reference.OBJ_WEAPON:
		inv.RemoveWeapon(object_name)
	elif object_flag == Reference.OBJ_BOW:
		inv.RemoveBow(object_name)
	elif object_flag == Reference.OBJ_QUIVER:
		inv.RemoveQuiver(object_name)
	elif object_flag == Reference.OBJ_STANDARD:
		pass
	elif object_flag == Reference.OBJ_KEY:
		inv.RemoveKey(object_name)
	elif object_flag == Reference.OBJ_SPECIALKEY:
		inv.RemoveSpecialKey(object_name)
	elif object_flag == Reference.OBJ_TABLET:
		inv.RemoveTablet(object_name)
	elif object_flag == Reference.OBJ_USEME:
		pass

	"""
	if me.Name == "Player1":
		if object_flag == Reference.OBJ_ITEM:
			ObjectsControl.SetBODs()
		elif object_flag == Reference.OBJ_SHIELD or object_flag == Reference.OBJ_QUIVER:
			ShieldsControl.SetBODs()
		elif object_flag == Reference.OBJ_WEAPON or object_flag == Reference.OBJ_BOW:
			WeaponsControl.SetBODs()
	"""

def ThrownWeaponStopFunc(EntityName):
	object= Bladex.GetEntity(EntityName)
	#print "Thrown object stopping"
	if object:
		object.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
		object.MessageEvent(MESSAGE_STOP_TRAIL,0,0)

		try:
			if object.Data.PrevHitFunc:
				object.HitFunc= object.Data.PrevHitFunc
				object.Data.PrevHitFunc= None
				object.HitFunc (EntityName)
		except AttributeError:
			pass
	#object.Data.ThrownBy= None

def ThrownWeaponInflictHitFunc(EntityName, VictimName, ImpX, ImpY, ImpZ):
	object= Bladex.GetEntity(EntityName)
	victim= Bladex.GetEntity(VictimName)
	#print "Thrown object hitting "+VictimName
	object.MessageEvent(MESSAGE_STOP_WEAPON,0,0)
	if object.Data.PrevInflictHitFunc:
		object.InflictHitFunc= object.Data.PrevInflictHitFunc
		object.Data.PrevInflictHitFunc= None
		object.InflictHitFunc (EntityName, VictimName, ImpX, ImpY, ImpZ)
	else:
		object.InflictHitFunc=0
	#object.Data.ThrownBy= None
	#if victim.Life <= 0:
	#	node= 0
	#	victim.LinkToNode(object,node)

def AutoCalcThrow (d, h, V, g):

	g2= g**2
	V2= V**2
	V4= V**4
	d2= d**2
	d4= d**4

	a= h**2+d2
	b= d2*(-1.0-(h*g/V2))
	c= 0.25*g2*d4/V4

	sq_term= b**2-4*a*c

	if sq_term<0.0:
		print "Auto calc doesn't reach"
		return -PI*0.25, 2.0
	else:
		sq_term= math.sqrt(sq_term)
		k= (-b+sq_term)/(2.0*a)
		angle= -math.acos(math.sqrt(k))
		time= d / (V*math.cos(angle))
		if abs(h-(V*math.sin(angle)*time+0.5*g*time*time)) > 0.001:
			angle= -angle
			time= d / (V*math.cos(angle))
		print "Auto calc gives angle: " + `angle` + " with time: " +`time`
		return angle, time

def ThrowReleaseEventHandler(EntityName, EventName):

	me = Bladex.GetEntity(EntityName)
	###Reference.debugprint(EntityName+": Im in ThrowReleaseEventHandler")


	if EventName=="ThrowLeftEvent":
		#print "LeftThrow"
		if me.InvLeft=="None" or not me.InvLeft:
			return
		object = Bladex.GetEntity(me.InvLeft)
	else:
		if me.InvRight=="None" or not me.InvRight:
			return
		object = Bladex.GetEntity(me.InvRight)

	try:
		object.Data.ThrowReleaseEventHandler (me.Name, EventName)
	except AttributeError:
		if object.TestHit:
			###Reference.debugprint(EntityName+": Pre-colliding - abandoning throw")
			return

		# Remove from inventory
		RemoveFromInventory (me, object, EventName)
		# Calculate impulse depending on event type

		# calculate impulse from keypress duration multiplier and character strength
		F= me.Data.ThrowForce*34000.0

		if me.InCombat:
			target= Bladex.GetEntity(me.ActiveEnemy)
			target_pos= target.Position
			source_pos= object.Position
			x= target_pos[0]-source_pos[0]
			y= target_pos[1]-source_pos[1]
			z= target_pos[2]-source_pos[2]

			angle, time= AutoCalcThrow (math.sqrt(x*x+z*z), y, F/object.Mass,+9800.0)
		elif EventName == "ThrowLightFacingEvent":
			angle= -PI*0.0625 # max angle/4
		elif EventName == "ThrowHeavyFacingEvent":
			angle= -PI*0.125 # max angle/2
		else:
			angle= -PI*0.0625 # max angle/4

		impulse = me.Rel2AbsVector(0.0, -math.cos(angle)*F, -math.sin(angle)*F)

		if me.InCombat:
			angle= B3DLib.Pos2PosXZAngle(source_pos[0], source_pos[1], source_pos[2],target_pos[0], target_pos[1], target_pos[2])
			diff_angle= min (max (B3DLib.DiffAngle(angle, me.Angle), -FACINGANGLE), FACINGANGLE)
			x,y,z= impulse
			cos_ang= math.cos(diff_angle); sin_ang= math.sin(diff_angle)
			impulse = (x*cos_ang-z*sin_ang, y, x*sin_ang+z*cos_ang)

		object.Impulse(impulse[0], impulse[1], impulse[2])

		throw_style= Reference.THR_SPINNING
		if Reference.EntitiesObjectData.has_key(object.Name):
			if Reference.EntitiesObjectData[object.Name][0] == Reference.OBJ_WEAPON or Reference.EntitiesObjectData[object.Name][0] == Reference.OBJ_STANDARD:
				weaponData= Reference.EntitiesObjectData[object.Name]
				if len(weaponData) > 4:
					throw_style= weaponData[4]
		else:
			kind = Bladex.GetEntity(object.Name).Kind
			if Reference.DefaultObjectData.has_key(kind):
				if Reference.DefaultObjectData[kind][0] == Reference.OBJ_WEAPON or Reference.DefaultObjectData[kind][0] == Reference.OBJ_STANDARD:
					weaponData = Reference.DefaultObjectData[kind]
					if len(weaponData) > 4:
						throw_style= weaponData[4]
		# exclude people from collision
		object.ExclusionMask= object.ExclusionMask | B_SOLID_MASK_PERSON

		if throw_style == Reference.THR_SPINNING:
			# Add an angular velocity component as well...
			#print object.AngularVelocity
			axis= object.GetDummyAxis("1H_R", 0.0, 1.0, 0.0)
			mass= object.Mass
			#print mass
			scale = (TWOPI*10/mass) * me.Data.ThrowForce						### Added scaling of angular velocity with throwforce -LeadHead
			object.AngularVelocity=axis[0]*scale,axis[1]*scale,axis[2]*scale
		object.MessageEvent(MESSAGE_START_WEAPON,0,0)
		object.MessageEvent(MESSAGE_START_TRAIL,0,0)
		InitDataField.Initialise(object)
		object.Data.PrevHitFunc= None
		#object.Data.PrevHitFunc= object.HitFunc
		#object.HitFunc= ThrownWeaponStopFunc
		Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, ThrownWeaponStopFunc,(object.Name,),"Stop Weapon: "+object.Name)
		object.Data.PrevInflictHitFunc= object.InflictHitFunc
		object.InflictHitFunc= ThrownWeaponInflictHitFunc
		object.Data.ThrownBy= me

	me.DelAnmEventFunc(EventName)

#
# Dropping Actions
#


def StdDropObject(EntityName):
	me = Bladex.GetEntity(EntityName)
	###Reference.debugprint(EntityName+": Im in StdDropObject")
	if TryDropRight(EntityName):
		pass
		###Reference.debugprint(EntityName+": Dropping Right")
	elif TryDropLeft(EntityName):
		pass
		###Reference.debugprint(EntityName+": Dropping Left")
	else:
		pass
		###Reference.debugprint(EntityName+": Nothing to Drop")

def TryDropRight (EntityName):
	me = Bladex.GetEntity(EntityName)
	# Have I got anything in the right hand
	statR = StatR(EntityName)
	if statR <> RA_NO_WEAPON:
		###Reference.debugprint(EntityName+": Right hand obj = "+me.InvRight)
		object = Bladex.GetEntity(me.InvRight)
		if IsValidForDropping (object.Name):
			object.ExcludeHitFor(me)
			#if object.TestHit:
			#	###Reference.debugprint(EntityName+": Pre-colliding - abandoning drop")
			#	return FALSE
			if statR == RA_2H_OBJECT:                                               # PLAGUE: No 2h objects exist in game anymore, nor does the animation 
				# 2 Handed Object Animation 
				me.AddAnmEventFunc("Drop2HandedEvent",DropReleaseEventHandler)
				me.LaunchAnmType("drp_2o")
				###Reference.debugprint (me.AnimName)
				return	TRUE
			else:
				# Right Handed Object Animation
				me.AddAnmEventFunc("DropRightEvent",DropReleaseEventHandler)
				me.Attack=0
				me.LaunchAnmType("drp_r")
				#The next : for not attacking just after droping!

				###Reference.debugprint (me.AnimName)
				return	TRUE
		else:
			ReportMsg ("Cannot be dropped")
			return FALSE
	else:
		return FALSE

def TryDropLeft (EntityName):
	me = Bladex.GetEntity(EntityName)
	statL=StatL(me.Name)
	if statL <> LA_NO_WEAPON and statL <> LA_BOW:
		###Reference.debugprint(EntityName+": Left hand obj = "+me.InvLeft)
		object = Bladex.GetEntity(me.InvLeft)
		if IsValidForDropping (object.Name):
			object.ExcludeHitFor(me)
			#if object.TestHit:
			#	###Reference.debugprint(EntityName+": Pre-colliding - abandoning drop")
			#	return FALSE

			# Left Handed Object Animation
			me.AddAnmEventFunc("DropLeftEvent",DropReleaseEventHandler)
			me.LaunchAnmType("drp_l")
			###Reference.debugprint (me.AnimName)
			return TRUE
		else:
			ReportMsg ("Cannot be dropped")
	else:
		return FALSE

def DropReleaseEventHandler(EntityName, EventName, TestHit=TRUE):
	me = Bladex.GetEntity(EntityName)
	###Reference.debugprint(EntityName+": Im in DropReleaseEventHandler")

	if EventName == "DropLeftEvent":
		object = Bladex.GetEntity(me.InvLeft)
	elif EventName == "DropLeft2Event":         # Added, fixes delayed attack_drink potion dropping     -LeadHead
		object = Bladex.GetEntity(me.InvLeft2)
	else:
		object = Bladex.GetEntity(me.InvRight)

	try:
		object.Data.DropReleaseEventHandler (me.Name, EventName)

	except AttributeError:
		if TestHit and object.TestHit:
			return

		RemoveFromInventory (me, object, EventName)

		if EventName == "DropLeftEvent":
			impulse = me.Rel2AbsVector(500.0, -750.0, 0.0)
		elif EventName == "Drop2HandedEvent":
			impulse = me.Rel2AbsVector(0.0, -750.0, 0.0)
		else:
			impulse = me.Rel2AbsVector(-1000.0, -1500.0, 0.0)

		object.Impulse(impulse[0],impulse[1],impulse[2])
		object.ExcludeHitFor(me)
		me.DelAnmEventFunc(EventName)

################
#
#
#
################


def SqDistanceToGpj(entity):
	global Gpj
	return(Gpj.SQDistance2(entity))

def SthOnBack(EntityName):
	me=Bladex.GetEntity(EntityName)
	if me.InvLeftBack:
		return TRUE
	if me.InvRightBack:
		if Reference.GiveObjectFlag(me.InvRightBack)==Reference.OBJ_QUIVER:
			return FALSE
		else:
			return TRUE
	else:
		return FALSE

def TwoHandedWeaponOnBack(EntityName):
	me=Bladex.GetEntity(EntityName)
	if SthOnBack(EntityName) and me.InvRightBack:
		back_object_flag= Reference.GiveObjectFlag(me.InvRightBack)
		if back_object_flag==Reference.OBJ_WEAPON:
			w_flag=Reference.GiveWeaponFlag(me.InvRightBack)
			if w_flag!=Reference.W_FLAG_1H:
				return TRUE
	return FALSE

def Left2InvEvent(pj_name,event):
	me=Bladex.GetEntity(pj_name)
	me.DelAnmEventFunc(event)
	inv=me.GetInventory()
	if me.InvLeft:
		inv.LinkLeftHand("None")

def Left2BackEvent(pj_name,event):
	me=Bladex.GetEntity(pj_name)
	me.DelAnmEventFunc(event)
	inv=me.GetInventory()
	if me.InvLeft:
		inv.LinkLeftBack(me.InvLeft)


### Func heavily modified. 
### Fixes multiple weird interactions.
###                     -LeadHead
def ToggleWEvent(pj_name,event):
	me=Bladex.GetEntity(pj_name)



	#
	# So the standard obnject that could NOT ve dropped at the beggining ( cause inside B_world ) , do NOT dissapear!
	#
	if IsRightHandStandardObject(pj_name) and not event=="ChangeLEvent":        # Added "not LEvent"    -LeadHead
		#print "TryDropRight is ok"
		DropReleaseEventHandler(pj_name, "DropRightEvent")
		if me.InvRight:
			print "Actions.ToggleWEvent-> Could not drop standard object!"
			ReportMsg ("Cannot be dropped")
			return FALSE
		me.Wuea=Reference.WUEA_ENDED



	if event=="ChangeRLEvent":
		me.DelAnmEventFunc("ChangeRLEvent")
	elif event=="ChangeREvent":
		me.DelAnmEventFunc("ChangeREvent")
	elif event=="ChangeLEvent":
		me.DelAnmEventFunc("ChangeLEvent")
	else:
		print "ToggleWEvent : Unexpected error! \n"

	inv=me.GetInventory()
	tmp_rback=me.InvRightBack
	tmp_lback=me.InvLeftBack
	rback_backup=0                       ### Start of retarded fix -LeadHead
	if tmp_rback:
		if Reference.GiveObjectFlag(tmp_rback)==Reference.OBJ_QUIVER:
			rback_backup=me.InvRightBack ### Retarded fix -LeadHead
			tmp_rback=""

	something_on_back= SthOnBack(pj_name)
	inv.LinkBack("None")

	ArrowDrawn=0 ### Part of the retarded fix -LeadHead
	add_quiver=0
	if something_on_back and (event=="ChangeRLEvent" or event=="ChangeREvent"):

		if me.InvRight:
			###Reference.debugprint ("Removeing right hand thing on ToggleWEvent")
			inv.LinkRightHand("None")
		#inv.LinkBack("None") #Only here ! It deal with BOTH of them

		if tmp_lback and Reference.GiveObjectFlag(tmp_lback)==Reference.OBJ_BOW:
			add_quiver=1
		if me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW:
			add_quiver=1


	if event=="ChangeRLEvent" or event=="ChangeREvent":
		if me.InvRight:
			if me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW and me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
				SheatheArrow(inv, me.InvRight)	# We must be carrying an arrow in the right hand, lets sheathe it           
			else:
				inv.LinkBack(me.InvRight)
		else:
			if inv.HoldingBow:
				if me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW and rback_backup:  # The core part of the retarded fix
					#print "we have bow in left and rback_backup ("+`rback_backup`+") was found"             # Fixes a bug where after using an item/key/lever with a bow in hand
					inv.LinkBack(rback_backup)                                                               # the arrow would be sheathed, the animation would play to unsheath it
					UnSheatheArrow(inv)                                                                      # but no arrow would actually be drawn
					ArrowDrawn=1                                                                             #                          -LeadHead
				else: 
					des_quiver_name=inv.GetSelectedQuiver()
					if des_quiver_name:
						inv.SetCurrentQuiver(des_quiver_name)
						inv.LinkRightBack(des_quiver_name)
					#print "BUG KK"

		if not tmp_rback and not ArrowDrawn:
			inv.LinkRightHand("None")
		elif not ArrowDrawn:
			inv.LinkRightHand(tmp_rback)
			# tmp_rback=""      # PlAGUE: Is this even necessary?

	if event=="ChangeRLEvent" or event=="ChangeLEvent":
		#inv.LinkBack("None")
		# if tmp_rback:                             # PLAGUE: Not sure if this was supposed to fix something at some point
			# print "Pseudo bug? ERROR , MIRAR"     #         but after my code changes it only causes problems
			# inv.LinkBack(tmp_rback)               #         commented out for now.
		if me.InvLeft:
			if tmp_rback:
				if Reference.GiveWeaponFlag(tmp_rback) in [Reference.W_FLAG_2W, Reference.W_FLAG_AXE, Reference.W_FLAG_SP]:     # Added check for 2handed weapon
					inv.LinkBack("None")                                                                                        #        -LeadHead
			else: 
				inv.LinkBack(me.InvLeft)
		if not tmp_lback:
			inv.LinkLeftHand("None")
		else:
			inv.LinkLeftHand(tmp_lback)
		if rback_backup:                    # Added, fixes bug with disappearing quiver
			inv.LinkBack(rback_backup)      # when drawing bow and have empty quiver on back    -LeadHead

	if add_quiver:
		UnSheatheArrow(inv)



### Following function has been re-written. Refer to LegacyToggleWeapons() for the original. -LeadHead
# Fixes the following:
#   - Locking on to an opponent with shield in hand and weapon on back no longer puts shield away before drawing both
#   - No longer tries to draw arrows from empty quivers
#   - No longer possible to fool the game into having a two handed weapon with a shield
#   - No longer draws arrow and puts bow on back when have only bow on left hand.
#   - No longer loses an arrow when already have one in hand and trying to draw bow
#   - Fixes bug where putting sword on back with shield already on back makes the sword disappear
#   - Easier to debug (subjective, but whatever)
ReworkedWepSwitch = 1

def StdToggleWeapons(EntityName):
    
	if ReworkedWepSwitch != 1:
		LegacyToggleWeapons(EntityName)
		return

	me=Bladex.GetEntity(EntityName)
	#If in combat, abort and return
	if me.ActiveEnemy:
		me.SetActiveEnemy("")
		me.Data.time_deactive_enemy=Bladex.GetTime()
		return

	if me.OnFloor==0 and me.AnimName!="JOG" and me.AnimName!="WBK_JOG" and me.AnimName!="WLK" and me.AnimName!="WBK":
		return

	if me.AnmEndedFunc:
		return FALSE

	inv= me.GetInventory()

	UnGraspString (EntityName,"UnGraspString")
	right_standard=IsRightHandStandardObject(EntityName)
	drop_right=0
	# Bow related crap
	QuiverOnBack = me.InvRightBack and Reference.GiveObjectFlag(me.InvRightBack)==Reference.OBJ_QUIVER
	QuiverOnBackEmpty = QuiverOnBack and Bladex.GetEntity(me.InvRightBack).Data.NumberOfArrows() < 1
		
	### We start by checking which hand is full and which is empty.
	if me.InvLeft and me.InvRight:
		if Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW:
			me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r_l")
			return
		elif right_standard:
			# drop_right=1
			## drop whatever stupid item you have and draw thing from back
				if TwoHandedWeaponOnBack(EntityName):
					drop_right=1
				elif not me.InvRightBack:
					drop_right=3
				else:
					drop_right=2
		else:
			me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r_l")
			return
			
			
	elif me.InvLeft and not me.InvRight:
		if Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW:     # We don't care if we have a quiver on back or not
			me.AddAnmEventFunc("ChangeLEvent",Left2BackEvent)           # If we want to shoot, we will press Attack
			me.LaunchAnmType("Chg_l")                                   # If not, we always prioritize putting bow away
			return
		elif TwoHandedWeaponOnBack(EntityName):
			me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r_l")
			return
		elif not me.InvRightBack:
			me.AddAnmEventFunc("ChangeLEvent",Left2BackEvent)
			me.LaunchAnmType("Chg_l")                        
			return
		else:
			me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r")
			return
		
		### PLAGUE: might need to rework this condition
	elif me.InvRight and not me.InvLeft:
		if not me.InvRightBack and not me.InvLeftBack:
			if right_standard:
				return
			else:
				me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
				me.LaunchAnmType("Chg_r")
				return
		elif inv.HasBowOnBack:
			if Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
				me.AddAnmEventFunc("ChangeLEvent",ToggleWEvent)
				me.LaunchAnmType("Chg_l")
				return
			elif right_standard and QuiverOnBack and not QuiverOnBackEmpty:
				drop_right=1
			elif right_standard and (QuiverOnBackEmpty or not me.InvRightBack):
				drop_right=3
				
		elif right_standard and not inv.HasBowOnBack:
			if me.InvRightBack and me.InvLeftBack:
				drop_right=1
			elif me.InvRightBack and not me.InvLeftBack:
				drop_right=2
			elif me.InvLeftBack and not me.InvRightBack:
				me.AddAnmEventFunc("ChangeLEvent",ToggleWEvent)
				me.LaunchAnmType("Chg_l")
				return
		elif Reference.GiveWeaponFlag(me.InvRight) in [Reference.W_FLAG_2W, Reference.W_FLAG_AXE, Reference.W_FLAG_SP]:
			me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r")
			return
	

	### If we had a standard item in hand, set up necessary drop event
	if drop_right!=0:
		if TryDropRight(EntityName):
			DropReleaseEventHandler(EntityName, "DropRightEvent")
		me.Wuea=Reference.WUEA_ENDED

		if drop_right==1:
			me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r_l")
			return
		elif drop_right==2:
			me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r")
			return
		elif drop_right==3:
			me.AddAnmEventFunc("ChangeLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_l")
			return
		else:
			print "!!! ERROR @ StdToggleWeapons - unexpected drop_right event !!! "

	
	
	### Getting this far means our hands are empty,
	### so we start another loop depending on what we have on our back
	### and don't conncern ourselves with hands
	if me.InvLeftBack and me.InvRightBack:
		if inv.HasBowOnBack and QuiverOnBack:
			if QuiverOnBackEmpty:
				me.AddAnmEventFunc("ChangeLEvent",ToggleWEvent)
				me.LaunchAnmType("Chg_l")
				return
			else:
				me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
				me.LaunchAnmType("Chg_r_l")
				return
		elif TwoHandedWeaponOnBack(EntityName):
			me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r")
			return
		else:
			me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r_l")
			return
	
	elif me.InvLeftBack and not me.InvRightBack:
		me.AddAnmEventFunc("ChangeLEvent",ToggleWEvent)
		me.LaunchAnmType("Chg_l")
		return
		
	elif me.InvRightBack and not me.InvLeftBack:
		me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
		me.LaunchAnmType("Chg_r")
		return
	
	else:
		# print "Nothing to draw or sheath"
		return
	
    ### If we got here, we have failed our mission spectacularly
	print "ERROR - ToggleW"

		
def LegacyToggleWeapons(EntityName):

	me=Bladex.GetEntity(EntityName)

	#Are we in combat mode
	#If so , abort it and return
	if me.ActiveEnemy:
		###Reference.debugprint ("StdToggleWeapons - Aborting combat mode")
		me.SetActiveEnemy("")
		me.Data.time_deactive_enemy=Bladex.GetTime()
		return

	if me.OnFloor==0 and me.AnimName<>"JOG" and me.AnimName<>"WBK_JOG" and me.AnimName<>"WLK" and me.AnimName<>"WBK":
		return

	if me.AnmEndedFunc:
		return FALSE

	inv= me.GetInventory()

	right_standard=IsRightHandStandardObject(EntityName)
	drop_right=0
	#pdb.set_trace()
	if me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)<>Reference.OBJ_BOW and me.InvRightBack: 
		if not me.Attack and not me.Block:                      # PLAGUE: This is practically impossible to call because me.Attack requires 
			me.AddAnmEventFunc("ChangeLEvent",Left2BackEvent)   #         to be already locked on and nobody tries to draw weapon holding block.
			me.LaunchAnmType("Chg_l")
			return
		else:
			me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r")
			return
	elif ((me.InvRight and right_standard==1)) and (me.InvLeft or me.InvLeftBack) and me.InvRightBack and not inv.HasBowOnBack:
		me.AddAnmEventFunc("ChangeLEvent",ToggleWEvent)
		me.LaunchAnmType("Chg_l")
		return
	elif ((me.InvRight and right_standard==0) or me.InvRightBack) and (me.InvLeft or me.InvLeftBack):
		drop_right=1
		if inv.HasBowOnBack:
			if right_standard:
				object= Bladex.GetEntity(me.InvRight)
				object.ExcludeHitFor(me)
				if not object.TestHit:
					if TryDropRight(EntityName):
						DropReleaseEventHandler(EntityName, "DropRightEvent")
						me.Wuea=Reference.WUEA_ENDED
					else:
						me.Wuea=Reference.WUEA_ENDED
						return
				else:
					ReportMsg ("Cannot be dropped")
					return
	elif ((me.InvRight and right_standard==0) or me.InvRightBack) and (not me.InvLeft and not me.InvLeftBack):
		drop_right=2
	elif (not me.InvRight and not me.InvRightBack) and (me.InvLeft or me.InvLeftBack):
		if inv.HasBowOnBack:
			if right_standard:
				object= Bladex.GetEntity(me.InvRight)
				object.ExcludeHitFor(me)
				if not object.TestHit:
					if TryDropRight(EntityName):
						DropReleaseEventHandler(EntityName, "DropRightEvent")
						me.Wuea=Reference.WUEA_ENDED
					else:
						me.Wuea=Reference.WUEA_ENDED
						return
				else:
					ReportMsg ("Cannot be dropped")
					return

			me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_r_l")
			return
		else:
			me.AddAnmEventFunc("ChangeLEvent",ToggleWEvent)
			me.LaunchAnmType("Chg_l")
			return
	else:
		return



	if drop_right<>0 and IsRightHandStandardObject(EntityName):
		if TryDropRight(EntityName):
			DropReleaseEventHandler(EntityName, "DropRightEvent")
		me.Wuea=Reference.WUEA_ENDED


	if drop_right==1:
		me.AddAnmEventFunc("ChangeRLEvent",ToggleWEvent)
		me.LaunchAnmType("Chg_r_l")
	elif drop_right==2:
		me.AddAnmEventFunc("ChangeREvent",ToggleWEvent)
		me.LaunchAnmType("Chg_r")
	else:
		print "ERROR - ToggleW"

# Added by Dario
def FreeBothHands(EntityName,CallBack=None,Params=(),ForceNow = 1):
	me=Bladex.GetEntity(EntityName)

	if IsRightHandStandardObject(EntityName):
		if TryDropRight(EntityName):
			DropReleaseEventHandler(EntityName, "DropRightEvent")
		me.Wuea=Reference.WUEA_ENDED

	if (me.InvRight) or (me.InvLeft):
		if ForceNow:
			me.Wuea=Reference.WUEA_ENDED
			me.SetTmpAnmFlags(1,1,1,0,5,1,0)
			me.LaunchAnmType("rlx")
			me.Wuea=Reference.WUEA_ENDED
			me.SetTmpAnmFlags(1,1,1,0,5,1,0)
		# StdToggleWeapons(EntityName)
		LegacyToggleWeapons(EntityName)     # Placeholder - "Legacy" code prioritizes putting stuff away. -LeadHead

		if CallBack:
			Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, CallBack,Params)
		return 0
	if CallBack:
		Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, CallBack,Params)
	return 1


def RelaxTurn180(EntityName):           # PLAGUE: this func is unused
	me=Bladex.GetEntity(EntityName)
	me.LaunchAnmType("rlx_turn")


import BInput


def FrwdDown(EntityName):
	me=Bladex.GetEntity(EntityName)
	if netgame.GetNetState() != 2:
		if me.InCombat:
			return

	binput_time_down=BInput.GetInputManager().GetTimeActionActivated("FrwdDown")
	diff=binput_time_down-me.Data.last_frwdup

	if diff>0.0 and diff<0.125:
		me=Bladex.GetEntity(EntityName)
		me.Run=1


def FrwdUp(EntityName):
	me=Bladex.GetEntity(EntityName)
	if netgame.GetNetState() != 2:
		if me.InCombat:
			return

	me.Data.last_frwdup=BInput.GetInputManager().GetTimeActionActivated("FrwdUp")


	if me.Gob==FALSE:
		me.Run=0


def BrwdDown(EntityName):
	me=Bladex.GetEntity(EntityName)
	if netgame.GetNetState() != 2:
		if me.InCombat:
			return

	binput_time_down=BInput.GetInputManager().GetTimeActionActivated("BrwdDown")
	diff=Bladex.GetTime()-me.Data.last_brwdup

	if diff>0.0 and diff<0.125:
		me=Bladex.GetEntity(EntityName)
		me.Run=1


def BrwdUp(EntityName):
	me=Bladex.GetEntity(EntityName)
	if netgame.GetNetState() != 2:
		if me.InCombat:
			return

	me.Data.last_brwdup=BInput.GetInputManager().GetTimeActionActivated("BrwdUp")

	if me.Gof==FALSE:
		me.Run=0




# BowStuff

# Added -LeadHead
BowCancelCalled = 0

def TakeArrowEventHandler(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)
	if me:
		#print EntityName+" TakeArrowEventHandler, "+me.AnimName+": "+`me.AnmPos`
		inv= me.GetInventory()
		UnSheatheArrow(inv)
		#if me.InvRight:
		#	print EntityName+" TakeArrowEventHandler: aimpressed: "+`me.Data.AimPressed`

def CurrentlyBowing(EntityName):
	me= Bladex.GetEntity(EntityName)
	anm= me.AnimName
	return (anm=="B1" or anm=="B2" or anm=="B3" or anm=="b1" or anm=="b2" or anm=="b3")

def InitBowing(EntityName):
	#print EntityName+" InitBowing"
	me= Bladex.GetEntity(EntityName)
	cam= Bladex.GetEntity("Camera")
	if EntityName=='Player1':
		try:
			if me.Data.LastPViewType==None:
				me.Data.LastPViewType= cam.PViewType
		except AttributeError:
			me.Data.LastPViewType= cam.PViewType
		try:
			if me.Data.LastReturns==None:
				me.Data.LastReturns= me.Returns
		except AttributeError:
			me.Data.LastReturns= me.Returns
		cam.PViewType= 3
	me.Returns= 0
	me.Aim= 1
	me.Data.AimPressed= 1
	me.Accuracy= CharStats.GetCharAccuracy(me.Kind, me.Level)
	me.AimOffTarget= TWOPI

def TestDrawBow(EntityName):
	global BowCancelCalled
	me= Bladex.GetEntity(EntityName)
	if BowCancelCalled==1:     # Added -LeadHead
		if EntityName=="Player1":
			return
	#print EntityName+" TestDrawBow"
	#pdb.set_trace()
	# Are we carrying a bow
	if me.Aim==0 or not CurrentlyBowing(EntityName):
		if me.InvLeft and Reference.GiveObjectFlag(me.InvLeft)==Reference.OBJ_BOW:
			# check we can interrupt the animation
			if me.Wuea==Reference.WUEA_WAIT:
				if (me.AnimName[:3]=="Rlx" or me.AnimName[:3]=="rlx"):
					me.Wuea=Reference.WUEA_NONE
				else: return
			# Are we carrying an arrow
			if me.InvRight and Reference.GiveObjectFlag(me.InvRight)==Reference.OBJ_ARROW:
				InitBowing(EntityName)
				GraspString (EntityName,"GraspString")
				me.SetTmpAnmFlags(1,0,1,1,2,0)
				me.LaunchAnmType ("b1")
				arrow= Bladex.GetEntity(me.InvRight)
				tensar_sound=Bladex.CreateEntity(arrow.Name+"RedrawSound", "Entity Sound", 0, 0, 0)
				tensar_sound.SetSound("../../Sounds/M-CREAKCUERDA-3b.wav")
				tensar_sound.MinDistance=5000
				tensar_sound.MaxDistance=10000
				arrow.Link(tensar_sound)
				tensar_sound.PlaySound(0)
					# Problems: Cannot get the animation to stay on last frame, or allow rotation
			# else if we have arrows draw an arrow and continue
			elif not CurrentlyBowing(EntityName):
				inv=me.GetInventory()
				des_quiver_name=inv.GetSelectedQuiver()
				if des_quiver_name:
					inv.SetCurrentQuiver(des_quiver_name)
					inv.LinkRightBack(des_quiver_name)
					quiver= Bladex.GetEntity(des_quiver_name)
					if quiver and quiver.Data.NumberOfArrows() > 0:
						InitBowing(EntityName)
						if me.Wuea==Reference.WUEA_WAIT:
							print "Trying to draw bow during other animation, wait and try again"
						else:
							me.LaunchAnmType ("b2")


def EndBowMode(EntityName):
	#print EntityName+" in EndBowMode"
	me= Bladex.GetEntity(EntityName)
	#print EntityName+" EndBowMode"
	#import pdb
	#pdb.set_trace()

	try:
		if me.Data.LastPViewType!=None:
			cam= Bladex.GetEntity("Camera")
			cam.PViewType= me.Data.LastPViewType
			me.Data.LastPViewType= None
	except AttributeError:
		pass
	try:
		if me.Data.LastReturns!=None:
			me.Returns= me.Data.LastReturns
			me.Data.LastReturns= None
	except AttributeError:
		pass
	me.Aim= 0
	me.Data.AimPressed= 0

def CancelBowMode(EntityName):          #Added -LeadHead
    me=Bladex.GetEntity(EntityName)
    global BowCancelCalled
    if CurrentlyBowing(EntityName):
        #print   "Bowing cancelled"
        BowCancelCalled = 1
        me.Wuea=Reference.WUEA_NONE
        me.LaunchAnmType("rlx_b")
        me.Aim= 0
        me.Data.AimPressed= 0
        try:
            if me.Data.LastPViewType!=None:
                cam= Bladex.GetEntity("Camera")
                cam.PViewType= me.Data.LastPViewType
                me.Data.LastPViewType= None
        except AttributeError:
            pass
        try:
            if me.Data.LastReturns!=None:
                me.Returns= me.Data.LastReturns
                me.Data.LastReturns= None
        except AttributeError:
            pass


def CancelDelayHandler():
    global BowCancelCalled
    if BowCancelCalled==1:
        BowCancelCalled=0

def TestReleaseArrow(EntityName):
	me= Bladex.GetEntity(EntityName)
	#print EntityName+' TestReleaseArrow setting AimPressed to 0'
	me.Data.AimPressed= 0
	if not CurrentlyBowing(EntityName):
		#print "    exited abnormally"
		EndBowMode(EntityName)


def EndDrawBowEventHandler(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)
	#print EntityName+" EndDrawBowEventHandler, "+me.AnimName+": "+`me.AnmPos`
	if me.Data.AimPressed==0:
		me.Aim= 0
		arrow= Bladex.GetEntity(me.InvRight)
		if arrow:
			#print EntityName+" EndDrawBowEventHandler:Letting Arrow Fly"
			# exclude people from collision
			#arrow.ExclusionMask= arrow.ExclusionMask | B_SOLID_MASK_PERSON

			# play arrow sound
			me.Unlink(arrow)
			me.RemoveFromInventRight()
			UnGraspString (EntityName,"UnGraspString")
			# Release the arrow
			arrow.ExcludeHitFor(me)
			arrow.PutToWorld()

			# Let the arrow fly along its own Z axis
			if me.Data.NPC:
				vx,vy,vz= me.AimVector
			else:
				vx,vy,vz= arrow.Rel2AbsVector(0,0,-40000)
			arrow.Fly(vx,vy,vz)

			arrow.MessageEvent(MESSAGE_START_WEAPON,0,0)
			arrow.MessageEvent(MESSAGE_START_TRAIL,0,0)

			# Arrange for the MESSAGE_STOP_WEAPON to be sent
			InitDataField.Initialise(arrow)
			Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, ThrownWeaponStopFunc,(arrow.Name,),"Stop Weapon: "+arrow.Name)
			arrow.Data.PrevInflictHitFunc= arrow.InflictHitFunc
			arrow.InflictHitFunc= ThrownWeaponInflictHitFunc
			arrow.Data.ThrownBy= me

			soltar_sound=Bladex.CreateEntity(arrow.Name+"FlySound", "Entity Sound", 0, 0, 0)
			soltar_sound.SetSound("../../Sounds/ARCO-DISPARO-3.wav")
			soltar_sound.MinDistance=5000
			soltar_sound.MaxDistance=10000
			arrow.Link(soltar_sound)
			soltar_sound.PlaySound(0)
			#"ARCO-DISPARO-3.wav"
			#"M-CREAKCUERDA-44.wav"

			# Draw another arrow
			me.SetTmpAnmFlags(1,0,1,1,2,0)
			#print "Drawn another"
			me.LaunchAnmType ("b2")
			return
	#print EntityName+" EndDrawBowEventHandler:b3"
	me.LaunchAnmType ("b3")


def CheckRefireBowEventHandler(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)
	#print EntityName+" CheckRefireBowEventHandler, "+me.AnimName+": "+`me.AnmPos`
	if me.InvRight:
		action= BInput.GetInputManager().GetInputActions().Find("Attack")
		if action and action.this!="NULL" and action.CurrentlyActivated():
			me.Aim= 1
			me.Data.AimPressed= 1

		if me.Data.AimPressed:
			arrow= Bladex.GetEntity(me.InvRight)
			if arrow:
				#print "CheckRefireBowEventHandler:Refire"
				GraspString (EntityName,"GraspString")
				me.DoActionWI ("b1", FixedFootAutoInterp, 0.3, 0.9)
				tensar_sound=Bladex.CreateEntity(arrow.Name+"RedrawSound", "Entity Sound", 0, 0, 0)
				tensar_sound.SetSound("../../Sounds/M-CREAKCUERDA-44.wav")
				tensar_sound.MinDistance=5000
				tensar_sound.MaxDistance=10000
				arrow.Link(tensar_sound)
				tensar_sound.PlaySound(0)
				return
		#else:
		#	print EntityName+" CheckRefireBowEventHandler, aimpressed: "+`me.Data.AimPressed`
		#	print EntityName+" CheckRefireBowEventHandler, InvRight: "+me.InvRight
		#print EntityName+" CheckRefireBowEventHandler:EndBowMode"
	EndBowMode(EntityName)

def EndReloadBowEventHandler(EntityName, EventName):
	#print EntityName+" In EndReloadBowEventHandler"
	me= Bladex.GetEntity(EntityName)
	if me.Aim:
		#print EntityName+" EndReloadBowEventHandler: b1"
		me.DoAction ("b1")
		#me.LaunchAnmType ("b1")
	else:
		# Default, go to rlx
		#print EntityName+" EndReloadBowEventHandler: Rlx_b"
		if not me.InvRight:
			TakeArrowEventHandler(EntityName, EventName)
		me.LaunchAnmType ("Rlx_b")
		#me.DoAction ("Rlx_b")


def FadeMeOut(EntityName,timer):
	if EntityName=="Player1":
		return

	me= Bladex.GetEntity(EntityName)
	current_alpha=me.Alpha
	if current_alpha>0.0:
		current_alpha=current_alpha-0.02
	else:
		prevLife = me.Life
		me.Life=0
		me.RemoveFromList("Timer60")
		if netgame.GetNetState()==1:
			Damage.PlayerHitFunc(me.Name,"BigFall", me.Life, prevLife)

	if current_alpha<0:
		current_alpha=0

	me.Alpha=current_alpha
	if me.InvRight:
		right=Bladex.GetEntity(me.InvRight)
		right.Alpha=current_alpha
	if me.InvLeft:
		left=Bladex.GetEntity(me.InvLeft)
		left.Alpha=current_alpha
	if me.InvRightBack:
		right2=Bladex.GetEntity(me.InvRightBack)
		right2.Alpha=current_alpha
	if me.InvLeftBack:
		left2=Bladex.GetEntity(me.InvLeftBack)
		left2.Alpha=current_alpha



def ClientCallBack(id,type,cad):
	if type==Netval.NET_GAME_FADE_DUE2BIGFALL:
		if netgame.GetClientId()==cad:
			AuxFuncs.FadeTo(START_FADEOUT_IN_BIG_FALL,END_FADEOUT_IN_BIG_FALL)

def ServerCallBack(id,type,cad):
	if type==Netval.NET_GAME_THROW_WEAPON:
		if netgame.GetNetState() == 1:
			params = string.split(cad)
			me = Bladex.GetEntity(params[0])
			coso = string.atof(params[1])
			if coso == -1:
				TryDropRight(params[0])
			else:
				me.Data.ThrowForce = coso
				StdThrowObject(params[0])




def StartFadingOutPlayer(EntityName):
	me= Bladex.GetEntity(EntityName)

	net_state=netgame.GetNetState()

	if net_state==0:
		if EntityName=="Player1"and me.WillCrashInFloor==0:
			AuxFuncs.FadeTo(START_FADEOUT_IN_BIG_FALL,END_FADEOUT_IN_BIG_FALL)
	elif EntityName=="Player1":
		if me.WillCrashInFloor==0:
			AuxFuncs.FadeTo(START_FADEOUT_IN_BIG_FALL,END_FADEOUT_IN_BIG_FALL)
		netgame.SendUserString(Netval.NET_GAME_FADE_DUE2BIGFALL,EntityName)
	else:
		netgame.SendUserString(Netval.NET_GAME_FADE_DUE2BIGFALL,EntityName)
		me.TimerFunc=FadeMeOut
		me.SubscribeToList("Timer60")


def EndFadingOutPlayer(EntityName):
	me= Bladex.GetEntity(EntityName)

	prevLife = me.Life
	me.Life=0

	print "In EndFadingOutPlayer"

	net_state=netgame.GetNetState()

	me.Wuea=Reference.WUEA_ENDED

	if net_state==0: # NO red
		#me.LaunchAnmType("rlx")
		me.ImDeadFunc(me.Name)
		if EntityName=="Player1":
			if me.WillCrashInFloor==0:
				int_pos=me.InitPos
				me.Position=int_pos[0],int_pos[1],int_pos[2]
			else:
				int_pos=me.InitPos
				me.Position=int_pos[0],int_pos[1],int_pos[2]

	elif net_state==1: #Red -> Servidor
		me.Alpha=1.0
		Damage.PlayerHitFunc(me.Name,"BigFall", me.Life, prevLife)
	elif net_state==2: #Red -> Cliente
		me.Alpha=1.0
	else:
		print "Actions.py->EndFadingOutPlayer error . Unknown GetNetState()!!!"


def LinkNextAttack(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)

	if me:
		me.RaiseEvent("HitFinalItpC")

	if not me.Data.NPC:
		Select.AutoSelectInAttack(EntityName)



def EndOfAttack(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)
	if me:
		me.RaiseEvent("ActionEndC")

	if not me.Data.NPC:
		Select.AutoSelectInAttack(EntityName)

def BackUpEnemy(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)
	me.Data.TmpEnemy=me.ActiveEnemy


def Swap180Handler(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)

	if me.Data and me.Data.TmpEnemy and me.Data.TmpEnemy==me.ActiveEnemy:
		me.SetActiveEnemy(None)

		#Quitada la sigu comprobacion
		if me.Data.selected_enemy:
			ene=Bladex.GetEntity(me.Data.selected_enemy[0])
			if me and ene.Person:
				me.SetActiveEnemy(ene)
	else:
		if me.Data.selected_enemy:
			ene=Bladex.GetEntity(me.Data.selected_enemy[0])
			if me and ene.Person:
				me.SetActiveEnemy(ene)


def InterruptFllHugeHandler(EntityName, EventName):
    me= Bladex.GetEntity(EntityName)
    print "In InterruptFllHugeHandler!!!!!!!!!"
    EndFadingOutPlayer(EntityName)

def EndTransitionFllHugeHandler(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)

	#enemigos?

	Bladex.AddScheduledFunc(Bladex.GetTime()+0.2, StartFadingOutPlayer,(EntityName,),"StartFadingOutPlayer "+EntityName)
	me.AnmEndedFunc=TakeMainAnm=EndFadingOutPlayer
	#Puesto en AnmEnd en lugar de Scheduled...
	#Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, EndFadingOutPlayer,(EntityName,),"EndFadingOutPlayer "+EntityName)

def W2hToLeftHandler(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)
	ObjectName=me.InvRight
	if ObjectName=="None" or not ObjectName:
		print "W2hToLeftHandle-> Event in a unexpected situation!!! Entity " + EntityName + " in animation " +me.AnimName
		return

	inv=me.GetInventory()
	inv.LinkRightHand("None")

	object=Bladex.GetEntity(ObjectName)
	node= me.GetNodeIndex("L_Hand")
	me.LinkToNode(object,node)
	me.Data.TmpW2h=ObjectName


def W2hToRightHandler(EntityName, EventName):
	me= Bladex.GetEntity(EntityName)

	if not("TmpW2h" in dir(me.Data)):
		me.Data.TmpW2h=""
		return

	if me.Data.TmpW2h == None:
		return

	if me.Data.TmpW2h=="":
		return

	inv=me.GetInventory()
	object=Bladex.GetEntity(me.Data.TmpW2h)
	me.Unlink(object)
	inv.LinkLeftHand("None")
	inv.LinkRightHand(me.Data.TmpW2h)
	me.Data.TmpW2h=""

# simple take used for network bindings
def AutoTake(EntityName):
	me = Bladex.GetEntity(EntityName)
	if me.InvRight:
		if not FreeBothHands(EntityName,None,(),0):
			return

	head_pos=me.Rel2AbsPoint(0.0,0.0,0.0)
	pj_dir=me.Rel2AbsVector(0.0,-1.0,0.0)
	list=Bladex.GetObjectEntitiesVisibleFrom(head_pos,5000.0,pj_dir,0.0)
	for n in list:
		o = Bladex.GetEntity(n)
		if (o.Parent == None) | (o.Parent == ""):
			if IsValidForTaking(n) & o.Weapon :
				if TryToTake(EntityName,n):
					return 1

##################################################################################################
##########################################  INSTANT ATTACK  ##########################################
##################################################################################################



def ToggleIAttackRight(EntityName,event):
	me = Bladex.GetEntity(EntityName)
	if not me.InvRightBack or me.InvRightBack=="":
		print "Error in Actions.ToggleIAttackRight"
		return

	inv= me.GetInventory()

	tmpr_back=me.InvRightBack

	inv.LinkRightBack("None")
	inv.LinkRightHand(tmpr_back)

	if not me.InCombat:
		import DefaultSelectionData
		DefaultSelectionData.SelectEnemy()


def ToggleIAttackLeft(EntityName,event):
	me = Bladex.GetEntity(EntityName)
	if not me.InvLeftBack or me.InvLeftBack=="" or TwoHandedWeaponOnBack(EntityName):       # Added check for TwoHandedWeapons -LeadHead
		return

	inv= me.GetInventory()

	tmpl_back=me.InvLeftBack
	inv.LinkLeftBack("None")
	inv.LinkLeftHand(tmpl_back)


def InstantAttackSlow(EntityName, EventName):
	me = Bladex.GetEntity(EntityName)
	if (not me.Data.NPC) and me.GotAnmType("g_draw_rlx"):
		me.AddAnmEventFunc("ChangeREvent",ToggleIAttackRight)
		me.AddAnmEventFunc("ChangeLEvent",ToggleIAttackLeft)
		me.AttackFunc (EntityName, "g_draw_rlx")
	elif not me.Data.NPC:
		print "No instant attack for not having the animation!! ----3D Dept---" + EntityName


def InstantAttackRun(EntityName, EventName):
	me = Bladex.GetEntity(EntityName)
	if me.GotAnmType("g_draw_run"):
		me.AddAnmEventFunc("ChangeREvent",ToggleIAttackRight)
		me.AddAnmEventFunc("ChangeLEvent",ToggleIAttackLeft)
		me.AttackFunc (EntityName, "g_draw_run")
	else:
		if me.Data.NPC==0:
			print "No instant attack for not having the animation!! ----3D Dept---" + EntityName



def LinkContinuosSoundAux(csound):
    csound.PlaySound(-1)



def LinkContinuosSound(EntityName,SoundName,max_dist=12000,min_dist=5000):
    me = Bladex.GetEntity(EntityName)
    csound=Bladex.CreateEntity(EntityName+"ContinuosSound", "Entity Sound", 0,0,0)
    csound.SetSound(SoundName)
    csound.MinDistance=min_dist
    csound.MaxDistance=max_dist
    me.Link(csound)
    #Otherwise it would not work (the SS does NOT launch any sounds when loading!!!)
    Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,LinkContinuosSoundAux,(csound,),"LinkContinuosSoundAux")







##################################################################################################
##########################################  FIRE DEATH  ##########################################
##################################################################################################

def CicloDeluz(PersonName,val):
	per = Bladex.GetEntity(PersonName)
	if per:
		if per.Life > 0:
			per.Alpha = 1
			per.SelfIlum = 0
			return
		if   val < 1.0:
			per.SelfIlum = val
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, CicloDeluz,(PersonName,val+0.1))
			wps=Bladex.GetEntity(PersonName+"WPS")
			if wps:
				wps.PPS=wps.PPS+25
		elif val < 2.0:
			per.Alpha = -val+1.9
			Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, CicloDeluz,(PersonName,val+0.1))

def HumoDeFuego(PersonName):
	per = Bladex.GetEntity(PersonName)
	if per:
		if per.Life > 0:
			per.Alpha = 1
			per.SelfIlum = 0
			return
		wps=Bladex.CreateEntity(PersonName+"WPSmk", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
		wps.PersonName=PersonName
		wps.ParticleType="DarkSmoke"
		wps.Time2Live=96
		wps.RandomVelocity=0
		wps.Velocity=0,0,0
		wps.NormalVelocity=5
		wps.YGravity=0
		wps.PPS=125
		wps.DeathTime=Bladex.GetTime()+1.0

def FreezeMeGuy(PersonName):
	import GameText
	per = Bladex.GetEntity(PersonName)
	if per.Life > 0:
		per.Alpha = 1
		per.SelfIlum = 0
		return
	if (netgame.GetNetState()==0) and (Reference.DEMO_MODE==0) and (PersonName=="Player1") and GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
		import SaveGame
		Bladex.AddScheduledFunc(Bladex.GetTime()+7.0,SaveGame.MenuStart,(PersonName,))


def FireDeath(PersonName = "Player1",ParType="LargeFire",NumPart=32):
	if netgame.GetNetState()!=0:
		QuickSmokeBall(PersonName)
		return

	TIME_TO_FIRE = 12.0
	per = Bladex.GetEntity(PersonName)
	if per:
		if per.Life > 0:
			per.Alpha = 1
			per.SelfIlum = 0
			return
		wps=Bladex.CreateEntity(PersonName+"WPS", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
		wps.PersonName=PersonName
		wps.ParticleType=ParType
		wps.Time2Live=NumPart
		wps.RandomVelocity=1.0
		wps.Velocity=0,-300,0
		wps.NormalVelocity=3
		wps.YGravity=0
		wps.PPS=200
		wps.DeathTime=Bladex.GetTime()+TIME_TO_FIRE
		Bladex.AddScheduledFunc(Bladex.GetTime()+TIME_TO_FIRE-0,  HumoDeFuego, (PersonName,))
		if netgame.GetNetState()!=2:
			per.SelfIlum = 0.0
			per.Alpha    = 1.0
			Bladex.AddScheduledFunc(Bladex.GetTime()+TIME_TO_FIRE-2,   CicloDeluz,  (PersonName,0))
			per.Wuea=Reference.WUEA_ENDED
			per.LaunchAnmType("dth_burn")
			per.SetOnFloor()
			per.AnmEndedFunc = FreezeMeGuy
			if per.Name == "Player1":
				cam  = Bladex.GetEntity("Camera")
				cam.SType = 0
				cam.TType = 0

def QuickSmokeBall(PersonName):
	per = Bladex.GetEntity(PersonName)
	if per:
		wps=Bladex.CreateEntity(PersonName+"WPFr", "Entity Particle System Dperson", 0.0, 0.0, 0.0)
		wps.PersonName=PersonName
		wps.ParticleType="LargeFire"
		wps.Time2Live=32
		wps.RandomVelocity=0
		wps.Velocity=0,0,0
		wps.NormalVelocity=5
		wps.YGravity=0
		wps.PPS=2048
		wps.DeathTime=Bladex.GetTime()+0.125
		if netgame.GetNetState()!=2:
			per.Alpha = 0.0



##################################################################################################
def ToggleInvincibility():
	me= Bladex.GetEntity("Player1")
	try:
		if me:
			if not me.Data.Invincibility:
				import pocimac
				me.Life= CharStats.GetCharMaxLife(me.Kind,me.Level)
				pocimac.RestoreWoundsToLifeLevel(me.Name)
				me.Data.Invincibility= TRUE
				ReportMsg ("Enabling INVINCIBILITY mode")
			else:
				me.Data.Invincibility= FALSE
				ReportMsg ("Disabling INVINCIBILITY mode")
	except AttributeError: pass

profiler_on=1
def ToggleProfiling():
	global profiler_on
	profiler_on= not profiler_on
	if not profiler_on:
		print "Switching off Profiler"
		Bladex.SetCallCheck(3)
		Bladex.SaveProfileData("Profile.txt")
		Bladex.StartProfile()
		Bladex.DisableProfiler()
	else:
		print "Switching on Profiler"
		Bladex.SetCallCheck(11)
		Bladex.EnableProfiler()
		Bladex.StartProfile()

def QuickDeath(EntityName,EventName):
	Bladex.GetEntity(EntityName).Life = 0
	if EntityName == "Player1":
		import SaveGame
		Bladex.AddScheduledFunc(Bladex.GetTime()+5.0,SaveGame.MenuStart,(EntityName,))
		AuxFuncs.FadeTo(3.5,10.0,128,0,0)

##################################################################################################
'''

                                        T I T A N I U M

                                                                                               '''
##################################################################################################
""" Commented out because I suspect it's not needed after all.
######
# ForceUse, needed for hotkeys far as I can tell -LeadHead
#

def ForceUse (EntityName, ItemName):
    me = Bladex.GetEntity(EntityName)
    object=Bladex.GetEntity(ItemName)
    if not object.UseFunc:
        print "!ERROR! @ Actions.ForceUse - " +ItemName+ " has no UseFunc"
        return
    else:
        me.Data.obj_used=object
        InitDataField.Initialise(object)
        object.Data.UsedBy = EntityName
        object.UseFunc(ItemName, USE_FROM_INV)
#
# The function skips checking a character's viability of using an item
# It will cause conflicts if called out of place, so DON'T DO IT
# StdUse still exists for a good reason.
#######


    ## Titanium Config Fuctions ##
    TiCfgFound=0
    try:
        import TitaniumConfig
        TiCfgFound=1
    except:
        print "ActionTables.py --- Could not find Titanium Configurator"
        
        
    if TitaniumConfig.TitaniumSetting("DodgeFix") == 1:
        DodgeFix = 1
    else:
        DodgeFix = 0
    ## - - - - - - - - - - - - - ##
"""

## PLAGUE: make configurable
DodgeFix = 1

### JumpHandler for relaxed state dodging fix.
def JumpHandler (EntityName, EventName):
    # print "Calling Actions.JumpHandler"
    me = Bladex.GetEntity(EntityName)
    
    if me.Name == "Player1" and DodgeFix:
        RightPressed = BInput.IsActionBeingHeld("Turn Right")
        LeftPressed = BInput.IsActionBeingHeld("Turn Left")
        BackPressed = BInput.IsActionBeingHeld("Backwards")
        ForwardPressed = BInput.IsActionBeingHeld("Forwards")
        if RightPressed or LeftPressed or BackPressed:
            me.RaiseEvent("Dodge")
        elif ForwardPressed:
            me.RaiseEvent("JumpWrap")

    else:
        me.RaiseEvent("JumpWrap")
