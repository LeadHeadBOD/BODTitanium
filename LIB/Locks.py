##///
##||| Locks.PY TITANIUM
##||| Change list:
##||| * Added func "KeyUp"
##||| * Func "LockUseFunc2" had to be subsequently edited.
##||| * 
##||| * 
##||| * 
##||| * 
##\\\ 


import Bladex
import InitDataField
import Actions
import Reference
import GameStateAux
import ObjStore
import darfuncs
import types
import B3DLib

LOCK          = 0
UNLOCK        = 1
LOCK_DISTANCE = 2000
	
def ActivateLock(pj_name,event):
	pj=Bladex.GetEntity(pj_name)
	lock=pj.Data.obj_used.Data.lockdata
	if(lock.state==UNLOCK):
		lock.Lock()
	elif(lock.state==LOCK):
		lock.UnLock()
	pj.Data.obj_used=None
	pj.DelAnmEventFunc("Activate")

def PlayerHasKey(EntityName, key):
	pj=Bladex.GetEntity("Player1")
	inv = pj.GetInventory()	
	for x in range (0, inv.nKeys):
		if key == inv.GetKey(x):
			return 1
	return 0

def KeyDown(pj_name,event):
	pj=Bladex.GetEntity(pj_name)	
	inv = pj.GetInventory()	
	inv.LinkRightHand("None")
	pj.DelAnmEventFunc("Key_down")

def KeyUp(pj_name,event):               # Added this func -LeadHead
	pj=Bladex.GetEntity(pj_name)	
	inv = pj.GetInventory()
	obj = pj.Data.obj_used
	lock = obj.Data.lockdata
	inv.LinkRightHand(lock.key)
	pj.DelAnmEventFunc("Key_up")

def LockUseFunc(lock_name,use_from):		
	import GameText
	import MenuText
	
	obj=Bladex.GetEntity(lock_name)	
	lock=obj.Data.lockdata
	pj=Bladex.GetEntity("Player1")
	
	if B3DLib.GetXZDistance('Player1', lock_name)> LOCK_DISTANCE:
		return
		
	if pj.Wuea==Reference.WUEA_WAIT:
		return
	
	if PlayerHasKey (pj.Name, lock.key):
		if not pj.InvRight:
			pj.Data.SwitchedWeapon = 0
			Actions.QuickTurnToFaceEntity ("Player1", lock_name)
			LockUseFunc2(pj.Name)
		else:
			if Actions.IsRightHandStandardObject(pj.Name):
				if Actions.TryDropRight(pj.Name):	
					Actions.DropReleaseEventHandler(pj.Name, "DropRightEvent")
				pj.Wuea=Reference.WUEA_ENDED					
				if not pj.InvRight:
					pj.Data.SwitchedWeapon = 0
					Actions.QuickTurnToFaceEntity ("Player1", lock_name)
					LockUseFunc2(pj.Name)
			else:
				pj.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)
				pj.LaunchAnmType("Chg_r")
				pj.Data.SwitchedWeapon = 1
				Actions.QuickTurnToFaceEntity ("Player1", lock_name)
				pj.AnmEndedFunc=LockUseFunc2
		import Scorer
		Scorer.wLogFrame.SetVisible(0)
	else:
		GameText.WriteTextAux(MenuText.GetMenuText("I don't have the key"),2.0,255,255,255,[],None,1)


def LockUseFunc2(EntityName):
	pj=Bladex.GetEntity(EntityName)
	# obj = pj.Data.obj_used	        # Commented out, because now is part of Key_up
	# lock = obj.Data.lockdata          #
	# inv = pj.GetInventory()	        #           -LeadHead
	# inv.LinkRightHand(lock.key)
	pj.LaunchAnmType("key")
	pj.AddAnmEventFunc("Key_up",KeyUp)  # Added -LeadHead
	pj.AddAnmEventFunc("Activate",ActivateLock)
	pj.AddAnmEventFunc("Key_down",KeyDown)
	pj.AnmEndedFunc=LockUseFunc3

def LockUseFunc3(EntityName):
	pj=Bladex.GetEntity(EntityName)		
	if pj.Data.SwitchedWeapon:
		pj.AddAnmEventFunc("ChangeREvent",Actions.ToggleWEvent)
		pj.LaunchAnmType("Chg_r")			



class Lock:

	ObjId=""
	state=LOCK
	key="Key"

	OnLockFunc=None
	OnLockArgs=()
	OnUnLockFunc=None
	OnUnLockArgs=()

	UnUsed = 0

	obj=None

	def __init__(self):
		self.ObjId=ObjStore.GetNewId()
		ObjStore.ObjectsStore[self.ObjId]=self

	def DecUser(self):
		if self.UnUsed:
			ll = Bladex.GetEntity(self.key)
			if type(ll.Data) is types.IntType:
				auxv = ll.Data
				ll.Data = darfuncs.EmptyClass()
				ll.Data.Used = auxv

			if ll.Data == None:
				ll.Data = darfuncs.EmptyClass()
				ll.Data.Used = 0
			else:
				ll.Data.Used = ll.Data.Used-1
			self.UnUsed = 0

	
	def Lock(self):
		if(self.state==UNLOCK):
			self.state=LOCK
			if(self.OnLockFunc):
				self.DecUser()
				apply(self.OnLockFunc,self.OnLockArgs)
				
	def UnLock(self):
		if(self.state==LOCK):
			self.state=UNLOCK
			if(self.OnUnLockFunc):
				self.DecUser()
				apply(self.OnUnLockFunc,self.OnUnLockArgs)

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		# Tiene que devolver c䮯 poder guardar el estado de la clase
##		print "Lock._getstate__()",self

		return (1,
				self.ObjId,
				self.state,
				self.key,
				GameStateAux.SaveFunctionAux(self.OnLockFunc),
				self.OnLockArgs,
				GameStateAux.SaveFunctionAux(self.OnUnLockFunc),
				self.OnUnLockArgs,
				self.UnUsed,
				GameStateAux.SaveEntityAux(self.obj),
				GameStateAux.SaveNewMembers(self)
				)

	def __setstate__(self,parm):
		# Toma como par⮥tro lo que devuelve __getstate__() y debe recrear la clase

		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
##			GameStateAux.PersistentObject.__setstate__(self,parm)
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.state=parm[2]
			self.key=parm[3]
			GameStateAux.LoadFunctionAux(parm[4],self,"OnLockFunc")
			self.OnLockArgs=parm[5]
			GameStateAux.LoadFunctionAux(parm[6],self,"OnUnLockFunc")
			self.OnUnLockArgs=parm[7]			
			self.UnUsed=parm[8]
			self.obj=GameStateAux.LoadEntityAux(parm[9]),
			GameStateAux.LoadNewMembers(self,parm[10])
		else:
			print "Lever.__setstate__() -> Version mismatch"
			# Valores de creaci䮠por si valen para algo.
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self
			self.state=LOCK
			self.key="Key"

			self.OnLockFunc=None
			self.OnLockArgs=()
			self.OnUnLockFunc=None
			self.OnUnLockArgs=()
			self.UnUsed=0



def PlaceLock(name,type,position,orientation,scale):
	lock=Lock()
	lock.UnUsed = 1
	lock.obj=Bladex.CreateEntity(name,type,position[0],position[1],position[2])
	lock.obj.Orientation=orientation
	lock.obj.Scale=scale
	InitDataField.Initialise(lock.obj)
	lock.obj.Data.lockdata=lock
	lock.obj.UseFunc=LockUseFunc	
	return lock


