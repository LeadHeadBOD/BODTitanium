#####
# B L A D E Ti
# Titanium stuff, yo
#####
import Bladex
import Reference
import AuxFuncs

###          ###
# SHADOW MASKS #
###          ###
"""
Due to an engine limitation, entities which have lights linked
cannot cast shadows, regardless of the CastShadows param.
This includes lights linked via scripts as well as lights
which are part of the mesh (.bod) file.

To overcome this limitation, we create a duplicate entity that is
linked to the parent. This dupe entity has all of its children deleted.


~~~OLD IDEA~~~
Create new mesh files which don't have any of the anchors/fires/spots, etc.
Shadowmask .bod files use the extension _shm and are automatically found
by the GiveShadowMask script, we only need to pass the entity Py object.
Shadowmask meshes are generally lower poly to reduce performance strain.

shadowExceptions is a list of entities that do not have any lights
in their mesh file but can have lights attached via scripts, 
like the fire weapons for example. They do not require any new mesh
for this purpose.
~~~OLD END~~~
"""


#
# shadowExceptions = ["FireAxe","FireSword","FireBigSword","BladeSword2","BladeSword2Barbarian","FireBo"]

def GiveShadowMask(ent):
    if ent.Lights and (ent.Lights[0][0]==0):
        AuxFuncs.GetSpot(ent).SubscribeToList("Pin")
        # if ent.FiresIntensity and (ent.FiresIntensity[0][0]>19):
            # while ent.GetNChildren():
                # Bladex.GetEntity(ent.GetChild(0)).SubscribeToList("Pin")
    else:
        oldPos          = ent.Position
        oldOri          = ent.Orientation
        ent.CastShadows = 0
        ent.Position    = 0.0, 0.0, 0.0
        ent.Orientation = (1.0, 0.0, 0.0, 0.0)

    # if ent.Kind in shadowExceptions:
        # shmKind = ent.Kind
    # else:
        # shmKind = ent.Kind+"_shm"
        shmName = ent.Name+"_shMask"
        shmObj = Bladex.CreateEntity(shmName,ent.Kind,0,0,0)
            while shmObj.GetNChildren():
                Bladex.GetEntity(shmObj.GetChild(0)).SubscribeToList("Pin")
        shmObj.Orientation = (1.0, 0.0, 0.0, 0.0)
        shmObj.Scale = ent.Scale
        shmObj.Solid = 0
        shmObj.CastShadows = 1
        shmObj.Alpha = 0
        shmObj.SendSectorMsgs = 0
        Reference.EntitiesSelectionData[shmName]=(0,0,"")
        ent.Link(shmObj)
        ent.Position = oldPos
        ent.Orientation = oldOri