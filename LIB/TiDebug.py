import Bladex
import Actions
import InitDataField

### Prints objects near character
def getNearbyEnts():
    pers = "Player1"; radius = 3000
    ch = Bladex.GetEntity(pers)
    x,y,z = ch.Position
    list = Bladex.GetEntitiesAt(x,y,z, radius)
    for i in list:
        if i == pers: pass
        else: o=Bladex.GetEntity(i); print "ent = " + `i` + "; kind = " + `o.Kind` + "; pos = " + `o.Position`
    Actions.ReportMsg("Results printed to console")


### Toggles invisible blockers on level
toggleState = 0

def toggleBlockers():
    
    global toggleState
    nents= Bladex.nEntities()
    for i in range(nents):
    	ent= Bladex.GetEntity(i)
        if toggleState == 0:
            try:
                if (ent.Alpha)==0.0:
                    InitDataField.Initialise(ent)
                    ent.Data.unmasked=1
                    ent.Alpha=0.8
            except:
                pass
        else:
            try:
                if ent.Data.unmasked==1:
                    ent.Alpha=0.0
                    ent.Data.unmasked=0
            except:
                pass
    if toggleState==1:
        toggleState = 0
    else:
        toggleState = 1
    Actions.ReportMsg("Invis ents toggled")


### Prints targeted enemy info

def getTarget():
    char = Bladex.GetEntity("Player1")
    enm = Bladex.GetEntity(char.ActiveEnemy)
    if char and enm:
        print ("---                    ---")
        print ("Player1 current target:")
        print ("Enemy: "+`enm.Name`+"; kind = "+`enm.Kind`)
        print ("InvRight: "+`enm.InvRight`+"; \n\n InvLeft: "+`enm.InvLeft`)
        print ("---                    ----")
    
    else:
        print ("Player 1 has no target")

"""
n_piezas=(0, 1, 2, 3, 4, 5)
Bladex.GetEntity(obj_name+"Pieza"+`n+1`)
tipo_pieza="IceHammerPieza"
piece.piezaposrel=[(-176.01,0,413.108), (179.492,-58.747,444.756), (179.494,0,413.737), (-179.494,58.747,444.756), (0,0,318.22), (0,0,0)]
piezaAlph=[(0.9, 0.9, 0.9, 0.9, 1.0]
piece.piezapos[n]=obj.Rel2AbsPoint(brkobj.piezaposrel[n][0], brkobj.piezaposrel[n][1], brkobj.piezaposrel[n][2])
pieza[n].Position=brkobj.piezapos[n][0], brkobj.piezapos[n][1], brkobj.piezapos[n][2]
"""


def CreateComplexEntity(name = "complexHammer", kind = "IceHammer"):
    char = Bladex.GetEntity("Player1")
    x,y,z = char.Position
    
    if kind == "IceHammer":
        tipo_pieza=kind+"Pieza"
        piezaposrel=[(-176.01,0,413.108), (179.492,-58.747,444.756), (179.494,0,413.737), (-179.494,58.747,444.756), (0,0,318.22), (0,0,0)]
        n_piezas=(0, 1, 2, 3, 4, 5)
        piezaAlph=(0.7, 0.7, 0.7, 0.7, 0.7, 1.0)
        piezaIlum=(0.2, 0.2, 0.2, 0.2, 0.2, 0.0)
    elif kind == "IceSword":
        tipo_pieza=kind+"Pieza"
        piezaposrel=[(20.178,-3.127,454.8), (20.178,2.867,169.377), (1.319,-0.363,5.251), (0,0,-339.913)]
        n_piezas=(0, 1, 2, 3)
        piezaAlph=(0.7, 0.7, 0.7, 1.0)
        piezaIlum=(0.2, 0.2, 0.2, 0.0)
        
    elif kind == "IceAxe":
        tipo_pieza=kind+"Pieza"
        piezaposrel=[(195.203,0,0), (-159.931,0.096,588.766), (-195.488,0.096,359.554), (-307.34,0.096,92.469), (-111.447,0.096,-177.108)]
        n_piezas=(0, 1, 2, 3, 4)
        piezaAlph=(1.0, 0.7, 0.7, 0.7 , 0.7)
        piezaIlum=(0.0, 0.2, 0.2, 0.2 , 0.2) 
        
    elif kind == "IceWand":
        tipo_pieza=kind+"Pieza"
        piezaposrel=[(1.937,2.582,826.34), (0.941,1.924,248.935), (0.133,1.642,-571.2)]
        n_piezas=(0, 1, 2)
        piezaAlph=(0.7, 0.7, 1.0)
        piezaIlum=(0.2, 0.2, 0.0)

    else:
       print ("~~ComplexEntitity ERROR - invalid entity.Kind provided!!")
    
    mainEnt = Bladex.CreateEntity(name,kind,0.0,0.0,0.0,"Weapon")

    for n in n_piezas:
        int_obj_name=name+"Part"+`n+1`
        pieza=Bladex.CreateEntity(int_obj_name, tipo_pieza+`n+1`, 0.0, 0.0, 0.0)
        pieza.Solid=0
        # pieza= Bladex.GetEntity(int_obj_name)
        # print piezaAlph[n]
        pieza.Alpha=piezaAlph[n]
        pieza.SelfIlum=piezaIlum[n]
        piezapos=mainEnt.Rel2AbsPoint(piezaposrel[n][0], piezaposrel[n][1], piezaposrel[n][2])
        pieza.Position=piezapos[0], piezapos[1], piezapos[2]
        mainEnt.Link(pieza)

    mainEnt.Position = x,y,z
    mainEnt.Alpha = 0.0
    return mainEnt


    
def GiveSpecials():
    import ItemTypes
    import Actions
    Char = Bladex.GetEntity("Player1")
    Char.Level = 19
    Char.Life  = 5000
    x,y,z = Char.Position
    if Char.Kind[0] == "A":
        arm = "ArmaduraAmazonaLigera"
        op  = Bladex.CreateEntity("arm", arm, x,y,z, "Physic")
        ItemTypes.ItemDefaultFuncs(op)
        
        w1  = "IceWand"
        o  = Bladex.CreateEntity("ent1", w1, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)
        
        w2  = "FireBo"
        o  = Bladex.CreateEntity("ent2", w2, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)

        w3  = "SteelFeather"
        o  = Bladex.CreateEntity("ent3", w3, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)
        
    if Char.Kind[0] == "B":
        arm = "ArmaduraBarbaroLigera"
        op  = Bladex.CreateEntity("arm", arm, x,y,z, "Physic")
        ItemTypes.ItemDefaultFuncs(op)
        
        w1  = "IceAxe"
        o  = Bladex.CreateEntity("ent1", w1, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)
        
        w2  = "FireBigSword"
        o  = Bladex.CreateEntity("ent2", w2, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)
        
    if Char.Kind[0] == "K":
        arm = "ArmaduraCaballeroCompleta"
        op  = Bladex.CreateEntity("arm", arm, x,y,z, "Physic")
        ItemTypes.ItemDefaultFuncs(op)
        
        w1  = "IceSword"
        o  = Bladex.CreateEntity("ent1", w1, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)
        
        w2  = "FireSword"
        o  = Bladex.CreateEntity("ent2", w2, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)
        
    if Char.Kind[0] == "D":
        arm = "ArmaduraEnanoMedia"
        op  = Bladex.CreateEntity("arm", arm, x,y,z, "Physic")
        ItemTypes.ItemDefaultFuncs(op)
        
        w1  = "IceHammer"
        o  = Bladex.CreateEntity("ent1", w1, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)
        
        w2  = "FireAxe"
        o  = Bladex.CreateEntity("ent2", w2, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)

        w3  = "CrushHammer"
        o  = Bladex.CreateEntity("ent3", w3, x,y,z, "Weapon")
        ItemTypes.ItemDefaultFuncs(o)
        Actions.TakeObject(Char.Name,o.Name)


### Func to trigger a reaction to the player as if they were hit
import Damage
def HitSimulation():
    char = Bladex.GetEntity("Player1")
    effective_damage = 0
    DamageType       = "Slash"
    DamageZone       = 1
    Shielded         = 0
    if char:
        Damage.CheckRightHandToDrop(char.Name)
        char.Data.RespondToHit(char.Name, "BWorld", effective_damage, DamageType, DamageZone, Shielded)
        # Damage.CalculateDamage(char.Name, "BWorld", "BWorld", "Crush", DamageZone, DamageNode, x, y, z, Shielded)


def printCurrentAnm():
    char = Bladex.GetEntity("Player1")
    print "~Current anm @  " + `Bladex.GetTime()`
    print "Anm:     " + `char.AnimName`
    print "FullAnm: " + `char.AnimFullName`
    print "Frame:   " + `char.AnmPos`


### Debug binds for quick level testing

def initDebugBinds():
    Bladex.AddInputAction("getTarget", 0)
    Bladex.AssocKey("getTarget", "Keyboard", "7", 1)
    Bladex.AddBoundFunc("getTarget", getTarget)

    Bladex.AddInputAction("getNearbyEnts", 0)
    Bladex.AssocKey("getNearbyEnts", "Keyboard", "8", 1)
    Bladex.AddBoundFunc("getNearbyEnts", getNearbyEnts)
    
    Bladex.AddInputAction("toggleBlockers", 0)
    Bladex.AssocKey("toggleBlockers", "Keyboard", "9", 1)
    Bladex.AddBoundFunc("toggleBlockers", toggleBlockers)
    
    Bladex.AddInputAction("GiveSpecials", 0)
    Bladex.AssocKey("GiveSpecials", "Keyboard", "0", 1)
    Bladex.AddBoundFunc("GiveSpecials", GiveSpecials)
    
    Bladex.AddInputAction("HitSimulation", 0)
    Bladex.AssocKey("HitSimulation", "Keyboard", "V", 1)
    Bladex.AddBoundFunc("HitSimulation", HitSimulation)
    
    Bladex.AddInputAction("printCurrentAnm", 0)
    Bladex.AssocKey("printCurrentAnm", "Keyboard", "G", 1)
    Bladex.AddBoundFunc("printCurrentAnm", printCurrentAnm)
    

### Prints a list of the name of all entities of the selected kind
### Used for finding accidentally duplicate entities
def FindEntKind(kind = "Llavecutre"):
    nents= Bladex.nEntities()
    for i in range(nents):
    	ent= Bladex.GetEntity(i)
        if ent.Kind == kind:
            print `ent.Name` + " matches kind " + `ent.Kind`
    
    
    
    
### Sets character stamina to 0 and 
### Prints time it took to get to max stamina
timeStarted = 0.0
timeEnded   = 0.0

import CharStats

def debugStamina():
    global timeStarted
    char = Bladex.GetEntity("Player1")
    char.Energy = 0
    timeStarted = Bladex.GetTime()
    Bladex.SetAfterFrameFunc("debugStaminaFunc", checkStamina)
    

def checkStamina(time):
    global timeEnded
    char = Bladex.GetEntity("Player1")
    if char.Energy == CharStats.GetCharMaxEnergy(char.Kind, char.Level):
        timeEnded = Bladex.GetTime()
        print timeEnded - timeStarted
        Bladex.RemoveAfterFrameFunc("debugStaminaFunc")
    
    




initDebugBinds()

print ("- - - TiDebug functions enabled! - - -")
print ("V - simulate character getting hit"    )
print ("G - print Player1 current anim"        )
print ("7 - print target name to console"      )
print ("8 - print nearby entities to console"  )
print ("9 - toggle invisible entities"         )
print ("0 - give best armour and elemntal weps")
print ("TiDebug.debugStamina()"                )
