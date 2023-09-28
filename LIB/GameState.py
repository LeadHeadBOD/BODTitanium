##///
##||| GAMESTATE.PY TITANIUM
##||| Change list:
##||| * Values of 0 should now be correctly assigned upon loading game
##||| * Spot Entity (lights) flickering now gets properly saved
##\\\ 


import Bladex
import BBLib
import time
import types
import cPickle
import os
import shutil
import string
import GameStateAux
import ObjStore
import Language
import MemPersistence



NotSave          = []
ModulesToBeSaved = []

def GetPickFileName(data):
    filename=None
    try:
        filename="%s/%s.dat"%("f",data.persistent_id())
    except:
        if type(data) in (types.DictionaryType,types.ListType,types.TupleType):
            filename="%s/%s%s.dat"%("f",str(type(data)),ObjStore.GetNewId())
        elif type(data) == types.FunctionType:
            filename="%s/%s%s.dat"%("f",data.func_name,ObjStore.GetNewId())
        elif type(data) == types.MethodType:
            filename="%s/%s%s.dat"%("f",data.im_func.func_name,ObjStore.GetNewId())
        else:
##            filename="%s/%s.dat"%("f",ObjStore.GetNewId())
            filename="%s/%s%s.dat"%("f",str(type(data)),ObjStore.GetNewId())

    return filename



def SavePickDataAux(file,data,assign):
##    if type(data)==types.MethodType:
##        print "SavePickDataAux() -> Warning: omiting method."
##        return

    if (data) != None:  # Added "!= None". -LeadHead
        filename=GetPickFileName(data)
        restorestring='GameStateAux.GetPickledData("%s")'%(filename,)
        file.write(assign%(restorestring,))

        GameStateAux.SavePickData(filename,data)


## Aproximadamente 2.5 segundos sobre 87, Se puede optimizar pasandolo a binario?
def SavePickledObjects(file,aux_dir):

    filename="%s/%s.dat"%(aux_dir,"DinObjs")

    ObjStore.CheckStore()

    try:
        funcfile=open(filename,"wt")
        p=cPickle.Pickler(funcfile)
        p.dump(ObjStore.ObjectsStore)
        funcfile.close()
    except IOError:
        print "Failed to open file" + filename
        return 0
    except pickle.PicklingError:   
        print "Failed to pickle file"+filename
        return 0
    return 1




class EntityState:
    def __init__(self,entity):
        self.CreationProps={}
        self.SpecialProps={}

        self.CreationProps["Name"]=entity.Name
        self.CreationProps["Kind"]=entity.Kind
        self.CreationProps["Position"]=entity.Position

##        self.SpecialProps["InternalState"]=entity.InternalState
        if entity.Data:
            self.SpecialProps["Data"]=entity.Data
        if entity.FrameFunc:
            self.SpecialProps["FrameFunc"]=entity.FrameFunc
        if entity.HitFunc:
            self.SpecialProps["HitFunc"]=entity.HitFunc
        if entity.InflictHitFunc:
            self.SpecialProps["InflictHitFunc"]=entity.InflictHitFunc
        if entity.DamageFunc:
            self.SpecialProps["DamageFunc"]=entity.DamageFunc
        if entity.TimerFunc:
            self.SpecialProps["TimerFunc"]=entity.TimerFunc
        if entity.HearFunc:
            self.SpecialProps["HearFunc"]=entity.HearFunc
        if entity.UseFunc:
            self.SpecialProps["UseFunc"]=entity.UseFunc
        if entity.SeeFunc:
            self.SpecialProps["SeeFunc"]=entity.SeeFunc
        if entity.StickFunc:
            self.SpecialProps["StickFunc"]=entity.StickFunc
        #self.SpecialProps["ChangeNodeFunc"]=entity.ChangeNodeFunc

        # Esta la trato como caso especial.
        self.InWorld=entity.InWorld

    def SaveCreation(self,file,aux_dir):
        file.write('\n\n\n')
        file.write('o=Bladex.CreateEntity("%s","%s",%f,%f,%f)\n' %
                    (self.CreationProps["Name"],
                     self.CreationProps["Kind"],
                     self.CreationProps["Position"][0],
                     self.CreationProps["Position"][1],
                     self.CreationProps["Position"][2]
                    )
                  )




    def SaveSpecialProperties(self,file,aux_dir):
        name=self.CreationProps["Name"]

        for i in self.SpecialProps.keys():
            curr_func=self.SpecialProps[i]
            f_rest_string="o.%s="%(i)
            SavePickDataAux(file,curr_func,f_rest_string+'%s\n')



    def SaveStatePass2(self,file,aux_dir):

        if self.SpecialProps.keys():
            file.write('o=Bladex.GetEntity("%s")\n'%(self.CreationProps["Name"]))
            self.SaveSpecialProperties(file,aux_dir)
            file.write('\n\n')
##        if save or self.SpecialProps["Data"]:
##            file.write('o=Bladex.GetEntity("%s")\n'%(self.CreationProps["Name"]))
##            self.SaveSpecialProperties(file,aux_dir)
##            data=self.SpecialProps["Data"]
##            SavePickDataAux(file,data,'o.Data=%s\n\n\n\n')


class EntitySpotState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        if entity.Flick == 0:                        # Added.
            # print entity.Name + " has no Flick"    #
            self.SpecialProps["Flick"]=0             #      -LeadHead



class EntityObjectState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)



class EntityPhysicState(EntityObjectState):
    def __init__(self,entity):
        EntityObjectState.__init__(self,entity)
        if entity.OnStopFunc:
            self.SpecialProps["OnStopFunc"]=entity.OnStopFunc




class EntityWeaponState(EntityPhysicState):
    def __init__(self,entity):
        EntityPhysicState.__init__(self,entity)
        if entity.HitShieldFunc:
            self.SpecialProps["HitShieldFunc"]=entity.HitShieldFunc



class EntityActorState(EntityObjectState):
    def __init__(self,entity):
        EntityObjectState.__init__(self,entity)



class EntityArrowState(EntityWeaponState):
    def __init__(self,entity):
        EntityWeaponState.__init__(self,entity)



class EntityParticleSystemState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)



class EntityFireState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)





class EntityCameraState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)




class EntityAuraState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)




class EntitySlidingAreaState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        self.Displacement=entity.Displacement
        self.SpecialProps["OnStopFunc"]=entity.OnStopFunc

        self.Limit = entity.DisplacementLimit
        self.V_D = entity.V_D
        self.A_D = entity.A_D
        self.IsStopped = entity.IsStopped

    def SaveProperties(self,file,aux_dir):
        EntityState.SaveProperties(self,file,aux_dir)
        file.write('o.Displacement=%s\n'%( str(self.Displacement)))

    def SaveSpecialProperties(self,file,aux_dir):
        EntityState.SaveSpecialProperties(self,file,aux_dir)
        SavePickDataAux(file,self.SpecialProps["OnStopFunc"],'o.OnStopFunc=%s\n')
        #if not self.IsStopped:
        #    file.write('o.SlideTo(%s,%s,%s)\n'%( str(self.Limit),str(self.V_D),str(self.A_D)))


class EntityWaterState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        if entity.TouchFluidFunc:
            self.SpecialProps["TouchFluidFunc"]=entity.TouchFluidFunc




class EntitySoundState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)




class EntityMagicMissileState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        if entity.OnHitFunc:
            self.SpecialProps["OnHitFunc"]=entity.OnHitFunc




class EntityElectricBoltState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)




class EntityPoolState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)




class EntityParticleState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)




class EntityDecalState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)



class EntityLavaState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)
        if entity.TouchFluidFunc:
            self.SpecialProps["TouchFluidFunc"]=entity.TouchFluidFunc




class EntityBipedState(EntityState):
    def __init__(self,entity):
        EntityState.__init__(self,entity)






class EntityPersonState(EntityBipedState):
    def __init__(self,entity):
        EntityBipedState.__init__(self,entity)
        self.SpecialProps["EnterPrimaryAAFunc"]=entity.EnterPrimaryAAFunc
        self.SpecialProps["EnterSecondaryAAFunc"]=entity.EnterSecondaryAAFunc
        self.SpecialProps["EnterCloseFunc"]=entity.EnterCloseFunc
        self.SpecialProps["EnterLargeFunc"]=entity.EnterLargeFunc
        self.SpecialProps["AnmEndedFunc"]=entity.AnmEndedFunc
        self.SpecialProps["DelayNoSeenFunc"]=entity.DelayNoSeenFunc
        self.SpecialProps["RouteEndedFunc"]=entity.RouteEndedFunc
        self.SpecialProps["ImHurtFunc"]=entity.ImHurtFunc
        self.SpecialProps["ImDeadFunc"]=entity.ImDeadFunc
        self.SpecialProps["EnemyDeadFunc"]=entity.EnemyDeadFunc
        self.SpecialProps["NoAllowedAreaFunc"]=entity.NoAllowedAreaFunc
        self.SpecialProps["EnemyNoAllowedAreaFunc"]=entity.EnemyNoAllowedAreaFunc
        self.SpecialProps["CharSeeingEnemyFunc"]=entity.CharSeeingEnemyFunc
        self.SpecialProps["AnmTranFunc"]=entity.AnmTranFunc
        self.SpecialProps["TakeFunc"]=entity.TakeFunc
        self.SpecialProps["ThrowFunc"]=entity.ThrowFunc
        self.SpecialProps["MutilateFunc"]=entity.MutilateFunc
        self.SpecialProps["CombatDistFlag"]=entity.CombatDistFlag


        self.InitInventory(entity)


    def SaveSpecialProperties(self,file,aux_dir):
        pass


    def InitInventory(self,entity):
        import Actions
        inv=entity.GetInventory()
        self.Inventory={}
        self.Inventory["Objects"]=[]
        for i in range(inv.nKindObjects):
            for name in Actions.GetListOfObjectsAt(inv,i):
                self.Inventory["Objects"].append(name)

        self.Inventory["maxWeapons"]=inv.maxWeapons
        self.Inventory["Weapons"]=[]
        for i in range(inv.nWeapons):
            self.Inventory["Weapons"].append(inv.GetWeapon(i))

        self.Inventory["Shields"]=[]
        for i in range(inv.nShields):
            self.Inventory["Shields"].append(inv.GetShield(i))

        self.Inventory["Quivers"]=[]
        for i in range(inv.nQuivers):
            self.Inventory["Quivers"].append(inv.GetQuiver(i))

        self.Inventory["Keys"]=[]
        for i in range(inv.nKeys):
            self.Inventory["Keys"].append(inv.GetKey(i))

        self.Inventory["SpecialKeys"]=[]
        for i in range(inv.nSpecialKeys):
            self.Inventory["SpecialKeys"].append(inv.GetSpecialKey(i))

        self.Inventory["Tablets"]=[]
        for i in range(inv.nTablets):
            self.Inventory["Tablets"].append(inv.GetTablet(i))

        self.Inventory["InvLeft"]=entity.InvLeft
        self.Inventory["InvLeft2"]=entity.InvLeft2
        self.Inventory["InvRight"]=entity.InvRight
        self.Inventory["InvLeftBack"]=entity.InvLeftBack
        self.Inventory["InvRightBack"]=entity.InvRightBack



    def SaveStatePass2(self,file,aux_dir):
        #print "begin PersonEntity.SaveStatePass2() "
        #EntityBipedState.SaveStatePass2(self,file,aux_dir)

        file.write('\no=Bladex.GetEntity("%s")\n'%(self.CreationProps["Name"]))

        if self.SpecialProps.has_key("Data"):
            data=self.SpecialProps["Data"]
            SavePickDataAux(file,data,'o.Data=%s\n')

        file.write('inv=o.GetInventory()\n')
        for i in self.Inventory["Objects"]:
            #inv.AddObject(i)
            file.write('Actions.ExtendedTakeObject(inv,"%s")\n'%(i,))

        file.write('inv.maxWeapons=%d\n'%(self.Inventory["maxWeapons"],))
        for i in self.Inventory["Weapons"]:
            file.write('GameStateAux.AddWeaponToInventory(inv,"%s")\n'%(i,))

        for i in self.Inventory["Shields"]:
            #inv.AddShield(i)
            #Breakings.SetBreakableWS(i)
            file.write('inv.AddShield("%s")\n'%(i,))
            real_ent=Bladex.GetEntity(i)
            try:
                a=real_ent.Data.brkobjdata
                file.write('Breakings.SetBreakableWS("%s")\n'%(i,))
            except Exception,exc:
                print "Exception in SaveStatePass2",exc

        for i in self.Inventory["Quivers"]:
            file.write('GameStateAux.AddQuiverToInventory(inv,"%s")\n'%(i,))

        for i in self.Inventory["Keys"]:
            file.write('inv.AddKey("%s")\n'%(i,))

        for i in self.Inventory["SpecialKeys"]:
            file.write('inv.AddSpecialKey("%s")\n'%(i,))

        for i in self.Inventory["Tablets"]:
            file.write('inv.AddTablet("%s")\n'%(i,))


        if self.Inventory["InvLeft"]:
            file.write('GameStateAux.LinkLeft("%s",inv,o)\n'%(self.Inventory["InvLeft"],))
            # SetBreakable?

        if self.Inventory["InvLeft2"]:
            file.write('GameStateAux.LinkLeft2B("%s",inv,o)\n'%(self.Inventory["InvLeft2"],))
            # SetBreakable?

        if self.Inventory["InvRight"]:
            file.write('GameStateAux.LinkRight("%s",inv,o)\n'%(self.Inventory["InvRight"],))
            # SetBreakable?

        if self.Inventory["InvRightBack"]:
            file.write('GameStateAux.LinkRightBack("%s",inv,o)\n'%(self.Inventory["InvRightBack"],))
            # SetBreakable?

        if self.Inventory["InvLeftBack"]:
            file.write('GameStateAux.LinkLeftBack("%s",inv,o)\n'%(self.Inventory["InvLeftBack"],))
            # SetBreakable?

        #print "end PersonEntity.SaveStatePass2() "




v__entities_saved=0

class EntitiesStateAux:
    def __init__(self,EntClass):
        self.EntClass=EntClass
        self.Entities=[]

    def AddEntityState(self,entity):
        self.Entities.append(self.EntClass(entity))

    def SaveStates(self,file,aux_dir):
        file.write('# There are %d entities\n\n'%(len(self.Entities),))
        for i in self.Entities:
            i.SaveState(file,aux_dir)

    def SaveStatesPass2(self,file,aux_dir):
        for i in self.Entities:
            global v__entities_saved
            v__entities_saved=v__entities_saved+1
            if not v__entities_saved%5:
                file.write('__load_bar.Increment("Entity")\n')
            i.SaveStatePass2(file,aux_dir)

    def DestroyEntities(self):
        for i in self.Entities:
            if i.CreationProps["Name"]!="Camera":
                realent=Bladex.GetEntity(i.CreationProps["Name"])
                realent.SubscribeToList("Pin")
        self.Entities=[]







class EntitiesState:
    def __init__(self):
        self.State={}
        #self.State["Entity"]=EntitiesStateAux(EntityState)
        self.State["Entity Object"]=EntitiesStateAux(EntityObjectState)
        self.State["Entity PhysicObject"]=EntitiesStateAux(EntityPhysicState)
        self.State["Entity Weapon"]=EntitiesStateAux(EntityWeaponState)
        self.State["Entity Arrow"]=EntitiesStateAux(EntityArrowState)
        self.State["Entity Actor"]=EntitiesStateAux(EntityActorState)
        self.State["Entity Biped"]=EntitiesStateAux(EntityBipedState)
        self.State["Entity Person"]=EntitiesStateAux(EntityPersonState)
        self.State["Entity Spot"]=EntitiesStateAux(EntitySpotState)
        self.State["Entity PrtclSys"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System D1"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System D2"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System D3"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System Dobj"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Particle System Dperson"]=EntitiesStateAux(EntityParticleSystemState)
        self.State["Entity Fire"]=EntitiesStateAux(EntityFireState)
        #self.State["Entity Dynamic Fire"]=EntitiesStateAux(EntityDynamicFireState)
        self.State["Entity Camera"]=EntitiesStateAux(EntityCameraState)
        self.State["Entity Water"]=EntitiesStateAux(EntityWaterState)
        #self.State["Entity Trail"]=EntitiesStateAux(EntityTrailState)
        self.State["Entity Sound"]=EntitiesStateAux(EntitySoundState)
        self.State["Entity Magic Missile"]=EntitiesStateAux(EntityMagicMissileState)
        self.State["Entity ElectricBolt"]=EntitiesStateAux(EntityElectricBoltState)
        self.State["Entity Pool"]=EntitiesStateAux(EntityPoolState)
        self.State["Entity Particle"]=EntitiesStateAux(EntityParticleState)
        self.State["Entity Decal"]=EntitiesStateAux(EntityDecalState)
        self.State["Entity Lava"]=EntitiesStateAux(EntityLavaState)
        self.State["Entity Sliding Area"]=EntitiesStateAux(EntitySlidingAreaState)
        #self.State["Sparks"]=EntitiesStateAux(EntityObjectState)
        #self.State["Clients"]=EntitiesStateAux(EntityObjectState)
        self.State["Entity Aura"]=EntitiesStateAux(EntityAuraState)

    def GetState(self):
        for i in range(Bladex.nEntities()):
            entity=Bladex.GetEntity(i)
            kind=entity.Kind
            state=None

            if kind in self.State.keys():
                self.State[kind].AddEntityState(entity)
            else: # Estamos con una entidad con BOD
                if entity.Object:
                    self.State["Entity Object"].AddEntityState(entity)
                elif entity.Person:
                    self.State["Entity Person"].AddEntityState(entity)
                elif entity.Weapon:
                    self.State["Entity Weapon"].AddEntityState(entity)
                elif entity.Arrow:
                    self.State["Entity Arrow"].AddEntityState(entity)
                elif entity.Physic:
                    self.State["Entity PhysicObject"].AddEntityState(entity)
##                elif entity.Actor:
##                    self.State["Entity Actor"].AddEntityState(entity)



    def SaveStatePass2(self,file,aux_dir):
        for i in self.State.keys():
            if i not in NotSave:
                self.State[i].SaveStatesPass2(file,aux_dir)
            file.write('\n\n')


    def DestroyEntities(self):
        for i in self.State.keys():
            if i not in NotSave:
                self.State[i].DestroyEntities()






def CreateEntAux(obj_tuple,obj_kind):
    obj=Bladex.GetEntity(obj_tuple[0])
    if not obj:
        BBLib.ReadBOD(obj_tuple[2])
        obj=Bladex.CreateEntity(obj_tuple[0],obj_tuple[1],0,0,0,obj_kind)
    return obj











class SectorState:
    def __init__(self):
        self.Index=-1
        self.OnEnter=None
        self.OnLeave=None
        self.OnHit=None
        self.OnWalkOn=None
        self.OnWalkOut=None
        self.Active=None
        self.ActiveSurface=None
        self.Save=0
        self.BreakInfo=None

    def GetState(self,idx):
        import Sparks # Por GenericSectorOnHit

        s=Bladex.GetSector(idx)
        if s:
            self.Index=s.Index
            self.OnEnter=s.OnEnter
            self.OnLeave=s.OnLeave
##            self.OnHit=s.OnHit
            self.OnWalkOn=s.OnWalkOn
            self.OnWalkOut=s.OnWalkOut
            self.Active=s.Active
            self.ActiveSurface=s.ActiveSurface
            self.BreakInfo=s.BreakInfo
            if (Sparks.GenericSectorOnHit!=s.OnHit and s.OnHit!=None):
                self.OnHit=s.OnHit
            if s.Active!=1 or s.BreakInfo or s.OnEnter or s.OnLeave or s.OnWalkOn or s.OnWalkOut or self.OnHit:
                self.Save=1

    def SaveState(self,file,aux_dir):
        import Sparks # Por GenericSectorOnHit

        if(self.Save):
            file.write('s=Bladex.GetSector(%d)\n'%(self.Index))
            self.__SaveCallbackFunction(file,"OnEnter",aux_dir,self.OnEnter)
            self.__SaveCallbackFunction(file,"OnLeave",aux_dir,self.OnLeave)
            self.__SaveCallbackFunction(file,"OnHit",aux_dir,self.OnHit)
            self.__SaveCallbackFunction(file,"OnWalkOn",aux_dir,self.OnWalkOn)
            self.__SaveCallbackFunction(file,"OnWalkOut",aux_dir,self.OnWalkOut)
            file.write('s.Active=%d\n'%(self.Active))
            if self.BreakInfo:
                file.write('s.BreakInfo=%s\n'%(str(self.BreakInfo)))
##            file.write('s.ActiveSurface=%d'%(self.ActiveSurface))
            file.write('\n\n')


    def __SaveCallbackFunction(self,file,cbname,aux_dir,function):
        r_cb_str='s.%s='%(cbname,)
        SavePickDataAux(file,function,r_cb_str+'%s\n')


class MapState:
    def __init__(self):
        self.SectorsState=[]

    def GetState(self):
        nSectors=Bladex.nSectors()
        for i in range(nSectors):
            s=SectorState()
            s.GetState(i)
            if s.Save:
                self.SectorsState.append(s)

    def SaveState(self,file,aux_dir):
        for i in self.SectorsState:
            i.SaveState(file,aux_dir)


class TriggerSectorState:
    def __init__(self):
        self.Index=-1
        self.OnEnter=None
        self.OnLeave=None
        self.Data=None
        self.Name=None
        self.Grupo= None
        self.Points = []
        self.FloorHeight = 0
        self.RoofHeight = 0

    def GetState(self,idx):
        self.Name=Bladex.GetTriggerSectorName(idx)
        self.Index=idx
        self.OnEnter=Bladex.GetTriggerSectorFunc(self.Name,"OnEnter")
        self.OnLeave=Bladex.GetTriggerSectorFunc(self.Name,"OnLeave")
        self.Data=Bladex.GetTriggerSectorData(self.Name)
        self.Grupo= Bladex.GetTriggerSectorGroup(self.Name)
        self.Points = Bladex.GetTriggerSectorPoints(self.Name)
        self.FloorHeight =Bladex.GetTriggerSectorFloorHeight(self.Name)
        self.RoofHeight = Bladex.GetTriggerSectorRoofHeight(self.Name)

    def SaveState(self,file,aux_dir):
        file.write('Bladex.AddTriggerSector("%s","%s",%f,%f,%s)\n'%(self.Name,self.Grupo,self.FloorHeight,self.RoofHeight,self.Points))
        SavePickDataAux(file,self.OnEnter,'Bladex.SetTriggerSectorFunc("'+self.Name+'","OnEnter",%s)\n')
        SavePickDataAux(file,self.OnLeave,'Bladex.SetTriggerSectorFunc("'+self.Name+'","OnLeave",%s)\n')
        SavePickDataAux(file,self.Data,'Bladex.SetTriggerSectorData("'+self.Name+'",%s)\n')
        file.write('\n\n')



class TriggersState:
    def __init__(self):
        self.SectorsState=[]

    def GetState(self):
        nSectors=Bladex.nTriggerSectors()
        for i in range(nSectors):
            s=TriggerSectorState()
            s.GetState(i)
            self.SectorsState.append(s)

    def SaveState(self,file,aux_dir):
        for i in self.SectorsState:
            i.SaveState(file,aux_dir)



class WorldState:
    def __init__(self):
        self.EntitiesState=EntitiesState()
        self.MapState=MapState()
        self.TriggersState=TriggersState()
        #print "__name__",__name__

    def GetState(self):
        self.EntitiesState.GetState()
        self.MapState.GetState()

    def SaveState(self,filename):
        print "[SAVE STARTED]"
        if(self.SaveLState(filename)==0):
            print "[SAVE FAILED]: "+filename
            Bladex.ShowCriticalWarning("SaveWarning","failed to save"+filename);
            return

        print "[SAVE COMPLETED]"

    def SaveLState(self,filename):
        import os
         
        aux_dir=(os.path.splitext(filename)[0])+"_files"

        tempfilename = "../../Save/Temp.py"
        temp_dir = "../../Save/SaveGame_Temp/"
        
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        try:
            os.mkdir(temp_dir)
        except:
            pass

        import LoadBar
        load_bar=LoadBar.AutoProgressBar(26,"Saving ","../../Data/Menu/Save/"+Language.Current+"/Guardando_hi.jpg")
        load_bar.Increment("AutoBODs")
        self.SaveAutoBODs(temp_dir)
##        self.SaveFunctions(temp_dir)
        try:
            file_data_aux=open("%s/%saux"%(temp_dir,"aux"),"wt")
        except OSError:
            print "Could not open"+("%s/%saux"%(temp_dir,"aux"),"wt")
            return 0

        file_data_aux.write(Bladex.GetCurrentMap())
        file_data_aux.close()

        # Ahora genero el script que al ejecutarse regenera el mundo
        try:
            file=open(tempfilename,"wt")
        except OSError:
            print "Could not open"+tempfilename
            return 0
            

        file.write('############################################################\n')
        file.write('#   Blade Game State %s\n'%(filename,))
        file.write('#   Do not modify\n')
        file.write('#   File created %s \n'%(time.asctime(time.gmtime(time.time())),))
        file.write('############################################################\n\n\n\n')
        file.write('import Bladex\n')
        file.write('Bladex.SetTime(%f)\n'%(Bladex.GetTime(),))
        file.write('import BBLib\n')
        file.write('import cPickle\n')
        file.write('import GameStateAux\n')
        file.write('import Reference\n')
        file.write('import Breakings\n')
        file.write('import Sounds\n')
        file.write('import Actions\n')
        file.write('import os\n')
        file.write('import sys\n')
        file.write('import darfuncs\n\n\n\n')
        file.write('import LoadBar\n\n\n\n')
        file.write('import Language\n')
        file.write('############################################################\n')
        file.write('#\n\n\n')

        file.write('my_last_player_ctype="%s"\n'%(Bladex.GetLastPlayerCType(),))

        file.write('Bladex.KillMusic()\n')
        file.write('Bladex.ShutDownSoundChannels()\n')
        file.write('Bladex.PauseSoundSystem()\n')

        file.write('Bladex.BeginLoadGame()\n')
        file.write('__load_bar=LoadBar.AutoProgressBar(%d,"Loading ","%s")\n'%(Bladex.nEntities()/5,"../../Data/Menu/Save/"+Language.Current+"/Cargando_hi.jpg"))
        file.write('GameStateAux.aux_dir="%s"\n'%(aux_dir,))

        file.write('InNewMap=0\n')
        file.write('if Bladex.GetCurrentMap()!="%s":\n'%(Bladex.GetCurrentMap(),))
        file.write('  InNewMap=1\n')
##        file.write('InNewMap=1\n')

        file.write('print "InNewMap",InNewMap\n')

        file.write('Bladex.SetCurrentMap(\"%s\")\n'%(Bladex.GetCurrentMap(),))
        file.write('sys.path.insert(0,os.getcwd())\n')
        file.write('Bladex.SetSaveInfo(%s)\n'%(str(Bladex.GetSaveInfo(),)))

        load_bar.Increment("MMPs")
        ResFiles=self.GetMMPFiles()
        file.write('__load_bar.Increment("MMPs")\n')
        file.write('GameStateAux.LoadMMPs(%s)\n'%(str(ResFiles),))
        file.write('__load_bar.Increment()\n')

        load_bar.Increment("BMPs")
        ResFiles=self.GetBMPFiles()
        file.write('__load_bar.Increment("BMPs")\n')
        self.SaveList('GameStateAux.LoadBMPs(%s)\n',ResFiles,file)
        file.write('__load_bar.Increment()\n')


        load_bar.Increment("AlphaBMPs")
        ResFiles=self.GetAlphaBMPFiles()
        file.write('__load_bar.Increment("AlphaBMPs")\n')
        self.SaveList('GameStateAux.LoadAlphaBMPs(%s)\n',ResFiles,file)
        file.write('__load_bar.Increment()\n')

        load_bar.Increment("Sounds")
        file.write('__load_bar.Increment("Sounds")\n')
        #file.write('if InNewMap:\n')
        file.write('Bladex.LoadSoundDataBase("%s/Sounds.sdb")\n'%(aux_dir,))
        #can return false
        if(Bladex.SaveSoundDataBase('%s/Sounds.sdb'%(temp_dir,))==0):
            print "Didn't save "+('%s/Sounds.sdb'%(temp_dir,))
        else:
            print "Saved "+('%s/Sounds.sdb'%(temp_dir,))
        #file.write('else:\n')
        #file.write('  if Bladex.GetLastPlayerCType()<>my_last_player_ctype:\n')
        #file.write('    Bladex.LoadSoundDataBase("%s/Sounds.sdb")\n'%(temp_dir,))

        file.write('__load_bar.Increment("AutoBODs")\n')
        file.write('BBLib.LoadAutoBODData("%s/AutoBOD.dat")\n\n\n'%(aux_dir,))

        load_bar.Increment("BODInspector")
        file.write('Bladex.BodInspector()\n')
##        self.SaveParticleSystems(file)
        psys_data_file=temp_dir+'/psys_data.dat'
        load_bar.Increment("ParticleSystem")
        #can return false
        if(Bladex.SaveParticleSystemsData(psys_data_file)==1):
            print "Saved "+psys_data_file
        else:
            print "Didn't save "+psys_data_file
            
        file.write('__load_bar.Increment("Particle Systems")\n')
        file.write('Bladex.LoadParticleSystemsData("%s")\n'%(aux_dir+'/psys_data.dat',))
        file.write('__load_bar.Increment("ObjStore")\n')


##        file.write('Bladex.SetTime(%f)\n'%(Bladex.GetTime(),))
        self.SaveTimers(file)
        file.write('if InNewMap:\n')
        file.write('  Bladex.LoadWorld(\"%s")\n'%(Bladex.GetWorldFileName(),))
        file.write('__load_bar.Increment()\n')

        file.write('import ObjStore\n')
        file.write('ObjStore.StoreIndex=%d\n'%(ObjStore.StoreIndex,))

        file.write('import BODInit\n')
        file.write('BODInit.Init()\n\n')
        file.write('__load_bar.Increment()\n')
        file.write('import PickInit\n')
        file.write('PickInit.Init()\n\n')
        file.write('__load_bar.Increment("Pick")\n')

        file.write('if InNewMap:\n')
        file.write('  __load_bar.Increment("SolidMask")\n')
        file.write('  import SolidMask\n')
        file.write('  SolidMask.Init()\n')
        file.write('  __load_bar.Increment("Material")\n')
        file.write('  import Material\n')
        file.write('  Material.Init()\n')
## Esto deberia seguir en el if
        file.write('__load_bar.Increment("AniSound")\n')
        file.write('import AniSound\n')
        file.write('__load_bar.Increment("anm_def")\n')
        file.write('import anm_def\n')
        file.write('anm_def.Init()\n')
        file.write('__load_bar.Increment("StepSounds")\n')
        file.write('import StepSounds\n')
        file.write('StepSounds.Init()\n')
        file.write('__load_bar.Increment("Enemies")\n')
        file.write('import Enemies\n')
        file.write('Enemies.Init()\n')
        file.write('__load_bar.Increment("Biped")\n')
        file.write('import Biped\n')
        file.write('Biped.Init()\n')
        file.write('__load_bar.Increment("anm_conv")\n')
        file.write('import anm_conv\n')
        file.write('anm_conv.Init()\n')
        file.write('__load_bar.Increment("Anm_Mdf")\n')
        file.write('import Anm_Mdf\n')
        file.write('Anm_Mdf.Init()\n')


        file.write('execfile("../../Scripts/AutoGenTextures.py")\n')
        file.write('__load_bar.Increment()\n')



        file.write('try:\n')
        file.write('  execfile("ActorsInit.py")\n')
        file.write('except IOError:\n')
        file.write('  print "Can\'t find ActorsInit.py"\n\n\n')

        combustion_data_file=temp_dir+'/combustion_data.dat'
        load_bar.Increment("Combustion Data")
        if(Bladex.SaveCombustionData(combustion_data_file)==0):
            print "Didn't save "+ combustion_data_file
        else:
            print "Saved "+ combustion_data_file
      
        file.write('print "About to load Combustion data"\n')
        file.write('if InNewMap:\n')
        file.write('  Bladex.LoadCombustionData("%s")\n'%(aux_dir+'/combustion_data.dat',))
        file.write('else:\n')
        file.write('  Bladex.ReassignCombustionData()\n')
        file.write('__load_bar.Increment()\n')


##        self.EntitiesState.SaveStatePass1(file,temp_dir)
        ent_data_file=temp_dir+'/ent_data.dat'
        load_bar.Increment("Entities Data")
        if(Bladex.SaveEntitiesData(ent_data_file)==0):
           print "Failed to save "+ ent_data_file
        else:
            print "Saved "+ ent_data_file
        file.write('__load_bar.Increment("Entities")\n')
        file.write('Bladex.LoadEntitiesData("%s")\n'%(aux_dir+'/ent_data.dat',))
        file.write('__load_bar.Increment()\n')


        import os
        import sys
        file.write('import sys\n')
        file.write('import os\n')
        #str_path=os.getcwd()
        #adj_str_path=string.replace(str_path,"//","/")
        #adj_str_path=string.replace(adj_str_path,"/","/")
        adj_str_path="../"+Bladex.GetCurrentMap()
        file.write('sys.path.insert(0,"%s")\n\n'%(adj_str_path,))


        file.write('__load_bar.Increment("DefFuncs")\n')
        file.write('try:\n')
        file.write('  execfile("DefFuncs.py")\n')
        file.write('except IOError:\n')
        file.write('  print "Can�t find DefFuncs.py"\n\n\n')
        file.write('__load_bar.Increment()\n')

        file.write('try:\n')
        file.write('  execfile("sol.py")\n')
        file.write('except IOError:\n')
        file.write('  pass\n\n\n')

        file.write('try:\n')
        file.write('  char=Bladex.GetEntity("Player1")\n')
        file.write('  execfile("MusicEvents.py")\n')
        file.write('except IOError:\n')
        file.write('  print "Can\'t find MusicEvents.py"\n\n\n')
        file.write('__load_bar.Increment()\n')


        file.write('__load_bar.Increment("MusDB")\n')
        file.write('Bladex.LoadMusicState("%s/MusState.sdb")\n'%(aux_dir,))
        load_bar.Increment("MusicState")
        musicStateName = '%s/MusState.sdb'%(temp_dir,);
        if(Bladex.SaveMusicState(musicStateName)==0):
            print "Didn't to save "+musicStateName
        else:
            print "Saved "+musicStateName

        file.write('try:\n')
        file.write('  execfile("TextureMaterials.py")\n')
        file.write('except IOError:\n')
        file.write('  print "Can\'t find TextureMaterials.py"\n\n\n')
        file.write('__load_bar.Increment()\n')

        # Grabar las variables, funciones, ...
        file.write( '\n')
        file.write('GameStateAux.InitGameState("%s")\n\n'%(aux_dir,))
        file.write('__load_bar.Increment()\n')

        file.write('__load_bar.Increment("Modules")\n')
        load_bar.Increment("Modules")
        self.SaveModules(file)
        file.write('__load_bar.Increment("Vars")\n')
        load_bar.Increment("Variables")
        if(self.SaveVars(file)==0):
            print "Failed to SaveVars"
        file.write('__load_bar.Increment("Sounds")\n')
        load_bar.Increment("Sounds")
        self.SaveSounds(file)
        file.write('__load_bar.Increment("Sectors")\n')
        load_bar.Increment("Sectors")
        self.SaveSectors(file)
        file.write('__load_bar.Increment("Entities")\n')
        load_bar.Increment("Entities")
        self.SaveEntities(file)
        file.write('__load_bar.Increment("PickledObjects")\n')
        load_bar.Increment("PickledObjects")
        if(SavePickledObjects(file,temp_dir)==0):
            print "Failed to save pickled objects"
            file.close()
            return 0
        file.write('GameStateAux.GetPickledObjects("%s")\n'%("%s/%s.dat"%(aux_dir,"DinObjs"),))
        file.write('__load_bar.Increment("Python Objects")\n')

        load_bar.Increment("Python Objects")
        self.SaveObjects(file)
        file.write('__load_bar.Increment("MapState")\n')


        load_bar.Increment("Map State")
        self.MapState.SaveState(file,temp_dir)
        file.write('__load_bar.Increment("TriggerState")\n')
        load_bar.Increment("Triggers State")
        self.TriggersState.GetState()
        self.TriggersState.SaveState(file,temp_dir)
        file.write('__load_bar.Increment("State pass2")\n')
        load_bar.Increment("Entities State pass 2")
        self.EntitiesState.SaveStatePass2(file,temp_dir)
        file.write('__load_bar.Increment()\n')
        file.write('print "About set objects relations"\n')
        file.write('__load_bar.Increment("Scheduled functions")\n')

        load_bar.Increment("Comp Vars")
        if(self.SaveCompVars(file,temp_dir)==0):
            print "SaveCompVars failed" + temp_dir
            file.close()
            return 0
        globPath="%s/%s.dat"%(aux_dir,"Globs")
        file.write("GameStateAux.LoadGlobalCompVars('%s',globals())\n"%(globPath,))
        file.write('__load_bar.Increment("Global comp vars")\n')

        load_bar.Increment("Scheduled Functions")
        self.SaveScheduledFuncs(file)
        file.write('__load_bar.Increment("AfterFrame functions")\n')
        load_bar.Increment("After Frame Functions")
        self.SaveAfterFrameFuncs(file)

        load_bar.Increment("Extra Data")
        GameStateAux.SaveExtraDataAux(file,temp_dir)

        load_bar.Increment("Extra Modules")
        self.SaveModulesToBeSaved(file,temp_dir,aux_dir,ModulesToBeSaved)

        load_bar.Increment("Cleaning up")
        GameStateAux.EndGameState(temp_dir)

        file.write('\n')
        file.write('Bladex.SetCombos("Player1",%s)'%(Bladex.GetCombos("Player1"),))
        file.write('\n')
        file.write('# Scorer Data init\n')
        file.write('#\n')
        file.write('import Scorer\n')
        file.write('Scorer.ActivateScorer()\n\n')
        file.write('Scorer.SetVisible(1)\n\n')
        file.write('__load_bar.Increment()\n')
        file.write('import CharStats\n')
        file.write('__load_bar.Increment()\n')
        file.write('import GameText\n')
        file.write('GameText.SetLanguage(Language.Current)\n')
        file.write('import DefaultScorerData\n')
        file.write('DefaultScorerData.Init()\n\n')
        file.write('__load_bar.Increment()\n')

        file.write('# Inicio del personaje y sus marcadores\n')
        file.write('char=Bladex.GetEntity("Player1")\n')
        file.write('Scorer.SetLevelLimits(0,CharStats.GetCharExperienceCost(char.CharType,char.Level))\n')
        file.write('Scorer.SetLevelBarValue(char.PartialLevel)\n')
        file.write('#Scorer.SetLevelValue(char.Level)\n')
        file.write('#\n')
        file.write('# Controls ( keyboard,mouse...) stuff\n')
        file.write('#\n')
        file.write('execfile("../../Scripts/InputInit.py")\n')
        file.write('import acts\n')
        file.write('acts.InitBindings("Player1")\n')
        file.write('acts.SetNoConfigurableActions()\n')
        file.write('__load_bar.Increment()\n')
        file.write('try:\n')
        file.write('  execfile("../../Config/Control.py")\n')
        file.write('  print "BladeInit -> Executed Control.py"\n')
        file.write('except:\n')
        file.write('  execfile("../../Scripts/DefControl.py")\n')
        file.write('  print "BladeInit -> Executed DefControl.py"\n\n')
        file.write('__load_bar.Increment()\n')
        file.write('#\n')
        file.write('# Menu\n')
        file.write('#\n')
        file.write('#execfile("../../Scripts/Menu.py")\n')
        file.write('import Menu\n')
        file.write('Menu.InitMenuKeys()\n')
        file.write('__load_bar.Increment()\n')
        file.write('execfile("../../Scripts/Globals.py")\n')

        import GotoMapVars
        file.write('import GotoMapVars\n')
        file.write('GotoMapVars.Get2DMapValuesAux(%s)\n'%(str(GotoMapVars.Set2DMapValuesAux()),))

        # Store at persistence these values
        file.write('import MemPersistence\n')
        file.write('MemPersistence.Store("2DMapValues",%s)\n'%(str(MemPersistence.Get("2DMapValues")),))
        file.write('MemPersistence.Store("MainChar",%s)\n'%(str(MemPersistence.Get("MainChar")),))

        import Reference
        file.write('Reference.PYTHON_DEBUG=%d\n'%(Reference.PYTHON_DEBUG,))

        file.write('if Reference.PYTHON_DEBUG >= 1:\n')
        file.write('############### DEBUG LEVEL ONE ###############\n')
        file.write('  execfile("../../Scripts/DebugControl.py")\n')

        file.write('if Reference.PYTHON_DEBUG >= 2:\n')
        file.write('############### DEBUG LEVEL TWO ###############\n')
        file.write('  Bladex.SetCallCheck(3)\n')
        file.write('else:\n')
        file.write('  Bladex.SetCallCheck(0)\n')

        file.write('__load_bar.Increment("AnmCameras")\n')
        file.write('import AnmCameras\n')
        file.write('AnmCameras.Init()\n')

        file.write('Bladex.ResumeSoundSystem()\n')

        file.write('Bladex.DoneLoadGame()\n')
        file.write('GameStateAux.CleanLoadTemp()\n\n\n')

        file.write('if Reference.PYTHON_DEBUG >= 1:\n')
        file.write('  try:\n')
        file.write('    execfile("Positions.py")\n')
        file.write('  except IOError:\n')
        file.write('    print "Can\'t find Positions.py"\n\n\n')

        file.write('__load_bar.Clear()\n')
        file.write('del __load_bar\n')
        file.write('Bladex.SetTime(%f)\n'%(Bladex.GetTime(),))


        file.write('#   Good Bye! (Enjoy The Silence)\n')
        GameStateAux.CleanSaveTemp()

        file.close()

        #Move temp file
        saveNumber = filename[len(filename)-4]
        imageTempPath = "../../Save/Temp.BMP"
        svTempPath = "../../Save/Temp.sv"
        if os.path.isfile(svTempPath)==0:
            print "Sv file "+svTempPath +" doesn't exist"
            return 0
        if os.path.isfile(imageTempPath)==0:
            print "Image "+imageTempPath +" doesn't exist"
            return 0


        print "Removing Old folder"
        imagePath = "../../Save/"+str(saveNumber)+".BMP"
        svPath = "../../Save/"+str(saveNumber)+".sv"
        if os.path.isdir(aux_dir)==1:
            shutil.rmtree(aux_dir)
        if os.path.isfile(filename)==1:
            os.remove(filename)
        if os.path.isfile(imagePath)==1:
            os.remove(imagePath)
        if os.path.isfile(svPath)==1:
            os.remove(svPath)
        print "Removed Old folder"

        os.rename(temp_dir, aux_dir)
        print filename
        os.rename(tempfilename,filename)
 
        os.rename(imageTempPath,imagePath)
        os.rename(svTempPath, svPath)
        return 1


    def SaveCompVars(self,file,temp_dir):
        globs=GetGlobals()
        globs_dict={}

        global_vars=self.GetGlobalsAux(types.DictionaryType,globs)
        for i in global_vars:
            globs_dict[str(i[0])]=i[1]

        global_vars=self.GetGlobalsAux(types.ListType,globs)
        for i in global_vars:
            globs_dict[str(i[0])]=i[1]

        global_vars=self.GetGlobalsAux(types.TupleType,globs)
        for i in global_vars:
            globs_dict[str(i[0])]=i[1]

        filename="%s/%s.dat"%(temp_dir,"Globs")
        try:
            globfile=open(filename,"wt")
        except OSError:
            print "failed to open "+filename
            return 0
            
        try:
            p=cPickle.Pickler(globfile)
        except pickle.PicklingError:   
            print "Failed to pickle file"+globfile
            globfile.close()
            return 0
            

        p.dump(globs_dict)
        globfile.close()
        return 1



    def SaveVars(self,file):
        "Saves variables in the global scope."
        globs=GetGlobals()

        global_vars=self.GetGlobalsAux(types.IntType,globs)
        file.write('\n# Integer variables\n')
        try:
            for i in global_vars:
                file.write('%s=%s\n'%(str(i[0]),str(i[1])))
        except  IndexError:
            print "SaveVars Integer Variables out of range"
            return 0
        global_vars=self.GetGlobalsAux(types.FloatType,globs)
        file.write('\n# Float variables\n')
        try:
            for i in global_vars:
                file.write('%s=%s\n'%(str(i[0]),str(i[1])))
        except  IndexError:
            print "SaveVars Float Variables out of range"
            return 0
        global_vars=self.GetGlobalsAux(types.StringType,globs)
        file.write('\n# String variables\n')
        try:
            for i in global_vars:
                if str(i[0])!="__doc__":
                    file.write('%s="%s"\n'%(str(i[0]),str(i[1])))
        except  IndexError:
            print "SaveVars Float Variables out of range"
            return 0

        return 1


        
            

    def SaveSounds(self,file):
        "Saves sound objects in the global scope."

        gmadlig=Bladex.CreateSound('../../sounds/golpe_maderamed.wav', 'GolpeMaderaMediana')
        snd_vars=self.GetGlobalsAux(type(gmadlig))

        file.write('\n# Sound objects\n')
        snd_vars_names=[]
        for i in snd_vars:
            snd_vars_names.append((str(i[0]),i[1].Name))

        for i in snd_vars_names:
            file.write('%s=Bladex.GetSound("%s")\n'%(i[0],i[1]))


    def SaveEntities(self,file):
        "Saves entity objects in the global scope."

        ent=Bladex.GetEntity(0)
        ent_vars=self.GetGlobalsAux(type(ent))

        file.write('\n# Entity objects\n')
        ent_vars_names=[]
        for i in ent_vars:
            try:
                ent_vars_names.append((str(i[0]),i[1].Name))
            except AttributeError: #Puede haber entidades que ya no existan
                pass

        for i in ent_vars_names:
            file.write('%s=Bladex.GetEntity("%s")\n'%(i[0],i[1]))
        file.write('\n\n')

    def SaveObjects(self,file):
        "Saves objects (from Lib/Object.py) in the global scope."

        import Objects
        obj=Objects.DinObj()
        obj_vars=self.GetGlobalsAux(type(obj))

        file.write('\n# Object objects\n')
        obj_vars_names=[]
        omit_objs=["__main__.Flecha","state","InputManager"]
        for i in obj_vars:
            if i is not self and str(i[1].__class__):
                if (str(i[0]) not in omit_objs):
                    obj_vars_names.append((str(i[0]),i[1]))
##                print "WorldState.SaveObjects() Added"
                else:
                    print "Omited",str(i[0])

        for i in obj_vars_names:
            try:
                SavePickDataAux(file,i[1],i[0]+"=%s\n")
            except Exception,exc:
                print "Failed saving of",i
                print exc

        file.write('\n\n')


    def SaveSectors(self,file):
        "Saves sector objects in the global scope."

        sec=Bladex.GetSector(0)
        sec_vars=self.GetGlobalsAux(type(sec))

        file.write('\n\n# Sector objects\n')
        sec_vars_names=[]
        for i in sec_vars:
            sec_vars_names.append((str(i[0]),i[1].Index))

        for i in sec_vars_names:
            file.write('%s=Bladex.GetSector(%d)\n'%(i[0],i[1]))
        file.write('\n\n')


    def SaveModulesToBeSaved(self,file,temp_dir,aux_dir,ModulesToBeSaved):
        for i in ModulesToBeSaved:
            tempname="%s/%sData.dat"%(temp_dir,i.__name__)
            filemame="%s/%sData.dat"%(aux_dir,i.__name__)
            file.write('__load_bar.Increment("Module")\n')
            i.SaveData(tempname)
            file.write('import %s\n'%(i.__name__,))
            file.write('%s.LoadData("%s")\n\n'%(i.__name__,filemame,))



    def SaveScheduledFuncs(self,file):

        exclude_funcs=("PowWidgetDraw","PeriodicAutoSelectPlayer1","PlayerRestoreEnergy",
                       "RepeatPeriodicSound","NextText","ClearText","PeriodicSound::PlayPeriodic")

        n_sched_funcs=Bladex.GetnScheduledFuncs()
        #print "SaveScheduledFuncs(). There are ",n_sched_funcs,"functions."
        for i in range(n_sched_funcs):
            f=Bladex.GetScheduledFunc(i)
            if f and f[2] not in exclude_funcs:
                func_string='GameStateAux.LoadFunctionAux(%s)'%(GameStateAux.SaveFunctionAux(f[0]),)
                filename=GetPickFileName(f[1])
                func_parms='GameStateAux.GetPickledData("%s")'%(filename,)
                #print "SaveScheduledFuncs() ",filename,f[1],f[2]
                if( GameStateAux.SavePickData(filename,f[1]) ==0):
                    print "Failed to save pick data"
                    return 0
               
                file.write("Bladex.AddScheduledFunc(%d,%s,%s,'%s')\n"%(f[3],func_string,func_parms,f[2]))


    def SaveAfterFrameFuncs(self,file):

        exclude_funcs=('InterpinterpLevelBar','InterpinterpStrengthBar','InterpinterpEnergyBar',
                       'InterpShields','InterpFadeText','InterpWeapons','InterpObjects','DefaultSelectionData',
                       'Fade')

        n_afrm_funcs=Bladex.GetnAfterFrameFuncs()
        #print "SaveAfterFrameFuncs(). There are ",n_afrm_funcs,"functions."
        for i in range(n_afrm_funcs):
            f_name=Bladex.GetAfterFrameFuncName(i)
            if f_name and f_name not in exclude_funcs:
                f=Bladex.GetAfterFrameFunc(f_name)
                filename=GetPickFileName(f)
                func_string='GameStateAux.GetPickledData("%s")'%(filename,)
                GameStateAux.SavePickData(filename,f)
                #print "SaveAfterFrameFuncs() ",filename,f,f_name,func_string
                file.write("Bladex.SetAfterFrameFunc('%s',%s)\n"%(f_name,func_string))

    def SaveModules(self,file):
        "Saves modules in the global scope."

        import string
        OmitModules=["__builtins__","Scorer","Menu","GameText","GameState","GameStateAux"]
        global_mods=self.GetGlobalsAux(types.ModuleType)
        file.write('\n# Modules\n')
        try:
            for i in global_mods:
                if i[0] not in OmitModules and string.find(i[0],"AnimationSet")==-1 and string.find(i[0],"Widget")==-1:
                    file.write('import %s\n'%(i[0],))
        except IndexError:
            print "SaveModules: i exceeded length"
            return 0

        return 1


    def GetGlobalsAux(self,req_type,globs=None):
        g=None
        if globs:
            g=globs
        else:
            g=GetGlobals()

        elems=[]
        for i in g.items():
            if type(i[1])==req_type:
                elems.append(i)
        return elems




    def SaveAutoBODs(self,path):
        # Primero voy a guardar los BODs que se generan autom�ticamente
##        B_CID_AUTO_OBJDSCR=BBLib.B_CID_AUTO_OBJDSCR
##        RM=BBLib.GetResourceManager()
##        nAutoBODs=RM.NResources(B_CID_AUTO_OBJDSCR)
##        for i in range(nAutoBODs):
##            name="%s/%s.BOD"%(path,RM.GetResourceName(B_CID_AUTO_OBJDSCR,i))
##            RM.SaveResource(B_CID_AUTO_OBJDSCR,i,name)
        name="%s/AutoBOD.dat"%(path,)
        BBLib.SaveAutoBODData(name)

    def SaveList(self,command,lista,file):
        nchunks=len(lista)/5
        for i in range(nchunks):
            lolimit=5*i
            l=lista[lolimit:lolimit+5]
            file.write(command%(str(l),))

    def __AuxGetResFiles(self,kind):
        RM=BBLib.GetResourceManager()
        nRes=RM.NResources(kind)
        ResFiles=[]
        for i in range(nRes):
            res_file=RM.GetResourceFile(kind,i)
            if res_file not in ResFiles:
                ResFiles.append(res_file)
        return ResFiles

    def __AuxGetResFilesAndNames(self,kind):
        RM=BBLib.GetResourceManager()
        nRes=RM.NResources(kind)
        ResFiles=[]
        for i in range(nRes):
            res_file=RM.GetResourceFile(kind,i)
            res_name=RM.GetResourceName(kind,i)
            if res_file not in ResFiles:
                ResFiles.append((res_file,res_name))
        return ResFiles




    def SaveTimers(self,file):

        file.write('\n# Timers\n')
        nTimers=Bladex.GetnTimers()
        for i in range(nTimers):
            cTimer=Bladex.GetTimerInfo(i)
            file.write('Bladex.CreateTimer("%s",%f)\n\n'%(cTimer[0],cTimer[1]))
        file.write('\n')


    def GetMMPFiles(self):
        return self.__AuxGetResFiles(BBLib.B_CID_BITMAP)

    def GetBODFiles(self):
        return self.__AuxGetResFiles(BBLib.B_CID_OBJDSCR)

    def GetBMPFiles(self):
        return self.__AuxGetResFilesAndNames(BBLib.B_CID_BMP)

    def GetAlphaBMPFiles(self):
        return self.__AuxGetResFilesAndNames(BBLib.B_CID_ALPHABMP)


def GetGlobals():
    import sys
    try:
        1 + ''
    except:
        frame = sys.exc_info()[2].tb_frame.f_back

    while frame:
        globs=frame.f_globals
        frame=frame.f_back

    return globs
