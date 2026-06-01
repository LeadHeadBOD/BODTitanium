##///
##||| OBJSTORE.PY TITANIUM
##||| Change list:
##||| * Fixed re-release specific memory leak (thanks, Tomash!)
##||| * (0.6) Properly fixed it this time (thanks, Sryml!)
##\\\ 

import sys




ObjectsStore={}

StoreIndex=0 # Que no se me olvide guardar este valor al guardar partida


def GetNewId():
    global StoreIndex

    StoreIndex=StoreIndex+1
    key=str(StoreIndex)
    while ObjectsStore.has_key(key):
        StoreIndex=StoreIndex+1
        key=str(StoreIndex)

##    print "GetNewId()",key
    return key


def CheckStore():

##    # Recoleccion de basura
    for i in ObjectsStore.keys():
        if sys.getrefcount(ObjectsStore[i])<=2:
            # garbage collection, if the only reference to the class is here, delete it
            print "CheckStore(): "+`ObjectsStore[i]`+" deleted by garbage collection" # ,rfcount # To FireFalcom, SNEG and GeneralArcade,
            del ObjectsStore[i]                                                                  # Your "massive patchwork" introduced a memory leak, good job!
                                                                                                 # Thanks, Tomash, for finding the cause        -LeadHead
    # Objetos que ya no son validos
    for i in ObjectsStore.keys():    
        try:
            obj=ObjectsStore[i]
            ret=obj.persistent_check()
            if not ret:
                del ObjectsStore[i]
        except AttributeError:
            pass
        except TypeError:
            pass
    
 