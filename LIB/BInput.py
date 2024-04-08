##///
##||| BINPUT.PY TITANIUM
##||| Change list:
##||| * Added wrapped function to translate one bound function to another.
##||| * Added wrapper for determining if an action is held.
##\\\ 


# This file was created automatically by SWIG.
import BInputc
import Bladex # Needed for func wrappers


class B_InputListenerPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def SetPythonFunc(self,arg0):
        val = BInputc.B_InputListener_SetPythonFunc(self.this,arg0)
        return val
    def EventCallback(self,arg0,arg1,arg2):
        val = BInputc.B_InputListener_EventCallback(self.this,arg0,arg1,arg2)
        return val
    def __str__(self):
        val = BInputc.B_InputListener___str__(self.this)
        return val
    def __repr__(self):
        return "<C B_InputListener instance>"
class B_InputListener(B_InputListenerPtr):
    def __init__(self,arg0) :
        self.this = BInputc.new_B_InputListener(arg0)
        self.thisown = 1




class B_InputDevicePtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def AddListener(self,arg0):
        val = BInputc.B_InputDevice_AddListener(self.this,arg0.this)
        return val
    def RemoveListener(self,arg0):
        val = BInputc.B_InputDevice_RemoveListener(self.this,arg0)
        return val
    def nListeners(self):
        val = BInputc.B_InputDevice_nListeners(self.this)
        return val
    def IsBinded(self,arg0,*args):
        val = apply(BInputc.B_InputDevice_IsBinded,(self.this,arg0,)+args)
        return val
    def __str__(self):
        val = BInputc.B_InputDevice___str__(self.this)
        return val
    def __repr__(self):
        return "<C B_InputDevice instance>"
class B_InputDevice(B_InputDevicePtr):
    def __init__(self,this):
        self.this = this




class B_nInputEventPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def GetPress(self):
        val = BInputc.B_nInputEvent_GetPress(self.this)
        return val
    def GetDevice(self):
        val = BInputc.B_nInputEvent_GetDevice(self.this)
        return val
    def GetKey(self):
        val = BInputc.B_nInputEvent_GetKey(self.this)
        return val
    def __repr__(self):
        return "<C B_nInputEvent instance>"
class B_nInputEvent(B_nInputEventPtr):
    def __init__(self,this):
        self.this = this




class B_InputActionPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __str__(self):
        val = BInputc.B_InputAction___str__(self.this)
        return val
    def Name(self):
        val = BInputc.B_InputAction_Name(self.this)
        return val
    def IsConst(self):
        val = BInputc.B_InputAction_IsConst(self.this)
        return val
    def nInputEvents(self):
        val = BInputc.B_InputAction_nInputEvents(self.this)
        return val
    def nProcs(self):
        val = BInputc.B_InputAction_nProcs(self.this)
        return val
    def AddEvent(self,arg0,arg1,arg2):
        val = BInputc.B_InputAction_AddEvent(self.this,arg0.this,arg1,arg2)
        return val
    def GetnInputEvent(self,*args):
        val = apply(BInputc.B_InputAction_GetnInputEvent,(self.this,)+args)
        val = B_nInputEventPtr(val)
        return val
    def GetTimeActivated(self):
        val = BInputc.B_InputAction_GetTimeActivated(self.this)
        return val
    def CurrentlyActivated(self):
        val = BInputc.B_InputAction_CurrentlyActivated(self.this)
        return val
    def RemoveEvent(self,arg0,arg1,arg2):
        val = BInputc.B_InputAction_RemoveEvent(self.this,arg0.this,arg1,arg2)
        return val
    def RemoveAllEvents(self):
        val = BInputc.B_InputAction_RemoveAllEvents(self.this)
        return val
    def RemoveAllDeviceEvents(self, device):
        val = BInputc.B_InputAction_RemoveAllDeviceEvents(self.this, device)
        return val
    def RemoveAllProcs(self):
        val = BInputc.B_InputAction_RemoveAllProcs(self.this)
        return val
    def __repr__(self):
        return "<C B_InputAction instance>"
class B_InputAction(B_InputActionPtr):
    def __init__(self,this):
        self.this = this




class B_InputActionsPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def nElements(self):
        val = BInputc.B_InputActions_nElements(self.this)
        return val
    def GetAction(self,arg0):
        val = BInputc.B_InputActions_GetAction(self.this,arg0)
        val = B_InputActionPtr(val)
        return val
    def Find(self,arg0):
        val = BInputc.B_InputActions_Find(self.this,arg0)
        val = B_InputActionPtr(val)
        return val
    def RemoveAction(self,arg0):
        val = BInputc.B_InputActions_RemoveAction(self.this,arg0)
        return val
    def __str__(self):
        val = BInputc.B_InputActions___str__(self.this)
        return val
    def __repr__(self):
        return "<C B_InputActions instance>"
class B_InputActions(B_InputActionsPtr):
    def __init__(self,this):
        self.this = this




class B_InputManagerPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            BInputc.delete_B_InputManager(self.this)
    def GetTimeActionHeld(self,arg0,arg1):
        val = BInputc.B_InputManager_GetTimeActionHeld(self.this,arg0,arg1)
        return val
    def GetTimeActionActivated(self,arg0):
        val = BInputc.B_InputManager_GetTimeActionActivated(self.this,arg0)
        return val
    def AddInputAction(self,arg0,arg1):
        val = BInputc.B_InputManager_AddInputAction(self.this,arg0,arg1)
        return val
    def AssocKey(self,arg0,arg1,arg2,arg3):
        val = BInputc.B_InputManager_AssocKey(self.this,arg0,arg1,arg2,arg3)
        return val
    def DisassocKey(self,arg0,arg1):
        val = BInputc.B_InputManager_DisassocKey(self.this,arg0,arg1)
        return val
    def Bind2(self,arg0,arg1,arg2,arg3):
        val = BInputc.B_InputManager_Bind2(self.this,arg0,arg1,arg2,arg3)
        return val
    def GetInputActions(self):
        val = BInputc.B_InputManager_GetInputActions(self.this)
        val = B_InputActionsPtr(val)
        return val
    def GetAttachedDevice(self,arg0):
        val = BInputc.B_InputManager_GetAttachedDevice(self.this,arg0)
        val = B_InputDevicePtr(val)
        return val
    def AddInputActionsSet(self,arg0):
        val = BInputc.B_InputManager_AddInputActionsSet(self.this,arg0)
        return val
    def ClearInputActionsSet(self,arg0):
        val = BInputc.B_InputManager_ClearInputActionsSet(self.this,arg0)
        return val
    def SetInputActionsSet(self,arg0):
        val = BInputc.B_InputManager_SetInputActionsSet(self.this,arg0)
        return val
    def GetInputActionsSet(self):
        val = BInputc.B_InputManager_GetInputActionsSet(self.this)
        return val
    def __repr__(self):
        return "<C B_InputManager instance>"
class B_InputManager(B_InputManagerPtr):
    def __init__(self) :
        self.this = BInputc.new_B_InputManager()
        self.thisown = 1






#-------------- FUNCTION WRAPPERS ------------------

def GetInputManager():
    val = BInputc.GetInputManager()
    val = B_InputManagerPtr(val)
    return val

#-------------- TITANIUM ACTION TRANSLATOR ---------
# Used to translate existing binds to another function.
# In Titanium used to make menus and level-select navigable with movement keys
# Even if you have re-bound them and not rely on WASD defaults
# Although it can be used for any function for custom purposes.
#
#               -LeadHead

def TranslateInputFromTo(origin, newAction, keyDevice="Keyboard"):
    
    inManager = GetInputManager()
    desManager  = GetInputManager()
    DestinationSet = inManager.GetInputActionsSet()
    # print DestinationSet
    # if DestinationSet == ("MenuRedefine"):
        # desManager.SetInputActionsSet("Menu")
    # else:
    desManager.SetInputActionsSet(DestinationSet)
    
    inManager.SetInputActionsSet("Default")
    
    nrOriginAction=inManager.GetInputActions().Find(origin).nInputEvents()
    for i in range(nrOriginAction):
        inManager.SetInputActionsSet("Default")
        
        OriginAction=inManager.GetInputActions().Find(origin).GetnInputEvent(i)
        ActionDevice=OriginAction.GetDevice()
        if ActionDevice == keyDevice:

            NeededActionKey=OriginAction.GetKey()
            
            inManager.SetInputActionsSet(DestinationSet)
            WantedAction = desManager.GetInputActions().Find(newAction)
            
            # We want to check whether we already have this function assigned to this key first
            # prevents duplicated inputs (for example, if player's movement is bound to arrowkeys)
            
            if WantedAction.nInputEvents() == 0:
                inManager.SetInputActionsSet(DestinationSet)
                Bladex.AssocKey(newAction,keyDevice,NeededActionKey)
                # inManager.SetInputActionsSet("Default")
            else:
                # print `newAction` + " already has something bound"
                for k in range(WantedAction.nInputEvents()):
                    if WantedAction.GetnInputEvent(k).GetKey() == NeededActionKey:
                        # print `WantedAction` + " already bound to " + `NeededActionKey`
                        break
                else:
                    inManager.SetInputActionsSet(DestinationSet)
                    Bladex.AssocKey(newAction,keyDevice,NeededActionKey)
                    # inManager.SetInputActionsSet("Default")
                    # print "could not find " + `newAction` + " so it was assigned"


#-------------- VARIABLE WRAPPERS ------------------

def IsActionBeingHeld(actionName):
    action= GetInputManager().GetInputActions().Find(actionName)
    if action and action.this!="NULL":
        return action.CurrentlyActivated()
    else:
        # Shouldn't get here, but you never know
        print " ~!UNEXPECTED ERROR!~ BInput.IsActionBeingHeld() - invalid action? " + `actionName`
        
        