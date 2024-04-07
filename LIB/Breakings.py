##///
##||| BREAKINGS.PY TITANIUM
##||| Change list:
##||| * 
##||| * Added new brkobj parameter - piezaRot[X,Y,Z]
##||| * Adjusted brkobj positions for: Escudo1, Escudo2, Escudo3 Escudo4, Escudo5, 
##|||                                  Escudo6, VampShield
##\\\ 

import Bladex
import InitDataField
import B3DLib
import Interpolator
import netgame

EXGRP_TOTALEXCLUSION=1



class BrkObj:
  pass



class FadeOutPiece(Interpolator.LinearInt):
  "Clase para hacer desaparecer las piezas."

  def __init__(self,piece):
    piece_entity=Bladex.GetEntity(piece)
    if piece_entity is not None:
      piece_entity.CastShadows=0

      Interpolator.LinearInt.__init__(self,1.0,0.0)
      self.Interpolator=Interpolator.Interp(piece)
      self.piece=piece
      time=Bladex.GetTime()
      self.Interpolator.AddAction(time,time+3.0,self)


  def Execute(self,value):
    ret=Interpolator.LinearInt.Execute(self,value)
    piece_entity=Bladex.GetEntity(self.piece)
    if piece_entity is None:
      self.Interpolator.Kill()
      self.piece=None
    else:
      piece_entity.Alpha=ret


  def EndExecute(self):
    piece_entity=Bladex.GetEntity(self.piece)
    if piece_entity is not None:
      piece_entity.SubscribeToList("Pin")
    self.Interpolator.Kill()
    self.piece=None
    #print "End FadeOut ChaosKnight"









def RemovePieces(brkobj):

#	for n in range(brkobj.n_piezas):
  for obj_name in brkobj.piezanoborrada:
    if type(obj_name) is type("c"):
      #pieza.SubscribeToList("Pin")
      brkobj.FadeOutPiece=FadeOutPiece(obj_name)
    else:
      print "RemovePieces() -> Getting Entity",obj_name,"obtained number."



def RemoveSinglePiece(obj_name):
  pieza=Bladex.GetEntity(obj_name)
  if not pieza:
    return
  else:
    brkobj=pieza.Data.brkparent
    brkobj.piezanoborrada.remove(obj_name)
    #pieza.SubscribeToList("Pin")
    brkobj.FadeOutPiece=FadeOutPiece(obj_name)



def LeftLife(obj_name):

	pieza=Bladex.GetEntity(obj_name)
	if not pieza:
		return
	else:
		brkobj=pieza.Data.brkparent
		Bladex.AddScheduledFunc(Bladex.GetTime()+brkobj.life_time, RemoveSinglePiece, (obj_name,),"LeftLife"+obj_name)


### PLAGUE: Need to change breaking sound for multiple shields, currently it is too weak.

def ExplodeSpecialObject(obj_name, expl_imp,delta = (0,0,0)):

	obj=Bladex.GetEntity(obj_name)
	if obj.Data is None:
		print "Trying to break "+obj_name+" AND it was NOT breakable!!!"
		return 0
	brkobj=obj.Data.brkobjdata
#	for n in range(brkobj.n_piezas):
	for n in brkobj.n_piezas:
		brkobj.piezapos[n]=obj.Rel2AbsPoint(brkobj.piezaposrel[n][0], brkobj.piezaposrel[n][1], brkobj.piezaposrel[n][2])
		brkobj.piezavector[n]=obj.Rel2AbsVector(brkobj.piezaposrel[n][0], brkobj.piezaposrel[n][1], brkobj.piezaposrel[n][2])
		brkobj.piezavector[n]=B3DLib.Normalize(brkobj.piezavector[n])
		brkobj.pieza[n].Position=brkobj.piezapos[n][0], brkobj.piezapos[n][1], brkobj.piezapos[n][2]
		brkobj.pieza[n]=Bladex.GetEntity(obj_name+"Pieza"+`n+1`)
		brkobj.pieza[n].Orientation=obj.Orientation
		### Added, rotate the pieces if they have any rotation data         -LeadHead
		try: brkobj.pieza[n].RotateRel(0,0,0,1,0,0, brkobj.piezaRotX[n]) # ; print ("assigned" + `brkobj.piezaRotX[n]`)
		except: pass  #print ("no RotX")
		try: brkobj.pieza[n].RotateRel(0,0,0,0,1,0, brkobj.piezaRotY[n]) #; print ("assigned" + `brkobj.piezaRotY[n]`)
		except: pass  # print ("no RotY")
		try: brkobj.pieza[n].RotateRel(0,0,0,0,0,1, brkobj.piezaRotZ[n]) # ; print ("assigned" + `brkobj.piezaRotZ[n]`)
		except: pass # print ("no RotZ")

	if brkobj.hidobjname:
		brkobj.hidobj.Position=obj.Rel2AbsPoint(brkobj.hidobj.Position[0], brkobj.hidobj.Position[1], brkobj.hidobj.Position[2])
	#obj.Static=1
	#obj.RemoveFromWorld()

	""" # Commented out - doesn't do what I want it to and causes weirdness with linked particles.
	n_child=obj.GetNChildren()                      # Added
	for n in range(n_child):                        # Now unlinks arrows and other stuff before breaking.
		child=Bladex.GetEntity(obj.GetChild(n))     #
		if child and child.Kind!="Entity Spot":     # 
			obj.Unlink(child)                       #
			child.Impulse(0,0,0)                    #       -LeadHead
	"""
	brkobj.sonido_rotura.Play(obj.Position[0], obj.Position[1], obj.Position[2], 0)
	if netgame.GetNetState() == 1:
		netgame.CallEventSound(obj.Name,5)
		obj.Alpha=0.0
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, obj.SubscribeToList,("Pin",))
		brkobj.Broken=1
	else:
		obj.SubscribeToList("Pin")
		brkobj.Broken=1

#	for n in range(brkobj.n_piezas):
	for n in brkobj.n_piezas:
		brkobj.pieza[n].Impulse(brkobj.piezavector[n][0]*expl_imp+delta[0], brkobj.piezavector[n][1]*expl_imp+delta[1], brkobj.piezavector[n][2]*expl_imp+delta[2])
	if brkobj.hidobjname:
		brkobj.hidobj.Impulse(0, 1, 0)
	if brkobj.life_time:
#		for n in range(brkobj.n_piezas):
		for n in brkobj.n_piezas:
			brkobj.pieza[n].OnStopFunc=LeftLife
	if brkobj.max_life_time:
		Bladex.AddScheduledFunc(Bladex.GetTime()+brkobj.max_life_time, RemovePieces, (brkobj,),"ExplodeSpecialObject"+obj_name)

	return 1



def BreakSpecialObject(hit_entity, hitting_entity, xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse,wcx,wcy,wcz,wdx,wdy,wdz):

  obj=Bladex.GetEntity(hit_entity)
  if obj is None:
    print "BreakSpecialObject() -> Getting entity",hit_entity,"is None"
    return 0

  brkobj=obj.Data.brkobjdata
#	for n in range(brkobj.n_piezas):
  for n in brkobj.n_piezas:
    brkobj.piezapos[n]=obj.Rel2AbsPoint(brkobj.piezaposrel[n][0], brkobj.piezaposrel[n][1], brkobj.piezaposrel[n][2])
    brkobj.piezavector[n]=brkobj.piezapos[n][0]-xhit_point, brkobj.piezapos[n][1]-yhit_point, brkobj.piezapos[n][2]-zhit_point
    brkobj.piezavector[n]=B3DLib.Normalize(brkobj.piezavector[n])
    brkobj.pieza[n]=Bladex.GetEntity(hit_entity+"Pieza"+`n+1`)
    brkobj.pieza[n].Position=brkobj.piezapos[n][0], brkobj.piezapos[n][1], brkobj.piezapos[n][2]
    brkobj.pieza[n].Orientation=obj.Orientation
  if brkobj.hidobjname:
    brkobj.hidobj.Position=obj.Rel2AbsPoint(brkobj.hidobj.Position[0], brkobj.hidobj.Position[1], brkobj.hidobj.Position[2])

	""" # Commented out - doesn't do what I want it to and causes weirdness with linked particles.
  n_child=obj.GetNChildren()                    # Added
  for n in range(n_child):                      # Now unlinks arrows and other stuff before breaking.
    child=Bladex.GetEntity(obj.GetChild(n))     #
    if child and child.Kind!="Entity Spot":     # 
      obj.Unlink(child)                         #
      child.Impulse(0,0,0)                      #       -LeadHead
	""" # Commented out - doesn't do what I want it to and causes weirdness with linked particles.

  brkobj.sonido_rotura.Play(obj.Position[0], obj.Position[1], obj.Position[2], 0)
  if netgame.GetNetState() == 1:
  	netgame.CallEventSound(obj.Name,5)
  	obj.Alpha=0.0
  	Bladex.AddScheduledFunc(Bladex.GetTime()+1.0, obj.SubscribeToList,("Pin",))
  else:
  	obj.SubscribeToList("Pin")

  polvillo=Bladex.CreateEntity("PolvoGolpe", "Entity Particle System D1", xhit_point, yhit_point, zhit_point)
  polvillo.ParticleType="MediumDust"
  polvillo.YGravity=0.0
  polvillo.Friction=0.2
  polvillo.PPS=480
  polvillo.DeathTime=Bladex.GetTime()+4.0/60.0
  dir_imp=B3DLib.Normalize((ximpulse, yimpulse, zimpulse))
  polvillo.Velocity=dir_imp[0]*4000, dir_imp[1]*4000, dir_imp[2]*4000
  polvillo.RandomVelocity=80.0
  polvillo.RandomVelocity_V=80.0
#	mod_imp=(xhit_point**2+yhit_point**2+zhit_point**2)**0.5
  ximpulse=ximpulse/len(brkobj.n_piezas)
  yimpulse=yimpulse/len(brkobj.n_piezas)
  zimpulse=zimpulse/len(brkobj.n_piezas)
#	mod_imp=mod_imp/(19-brkobj.n_piezas)
#	for n in range(brkobj.n_piezas):
  for n in brkobj.n_piezas:
    brkobj.pieza[n].ImpulseC(xhit_point, yhit_point, zhit_point, ximpulse, yimpulse, zimpulse)
#		brkobj.pieza[n].Impulse(brkobj.piezavector[n][0]*mod_imp, brkobj.piezavector[n][1]*mod_imp, brkobj.piezavector[n][2]*mod_imp)
  if brkobj.hidobjname:
    brkobj.hidobj.Impulse(0, 1, 0)
  if brkobj.life_time:
#	  for n in range(brkobj.n_piezas):
    for n in brkobj.n_piezas:
      brkobj.pieza[n].OnStopFunc=LeftLife
  if brkobj.max_life_time:
    Bladex.AddScheduledFunc(Bladex.GetTime()+brkobj.max_life_time, RemovePieces, (brkobj,),"BreakSpecialObject")

  return 1

def SetBreakableWS(obj_name,life_time=0, max_life_time=0):
  SetBreakable(obj_name,life_time,max_life_time)
  obj=Bladex.GetEntity(obj_name)
  obj.HitFunc=None

def GetBreakingData(obj):
  brkobj=BrkObj()

  if obj.Kind=="Barril":
    brkobj.piezaposrel=[(109.07, 237.75, 0.0), (225.62, 121.20, 0.0), (-109.07, -213.50, 0.0), (-225.62, 121.20, 0.0),
                        (0.0, 12.12, 380.12), (0.0, 12.12, -199.40)]
    brkobj.pieza=[0, 0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0, 0]
#   brkobj.n_piezas=6
    brkobj.n_piezas=(0, 1, 2, 3, 4, 5)
    brkobj.tipo_pieza="BarrilPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Cajon2" or obj.Kind=="Cajon" or obj.Kind=="Caja_i_r":
    brkobj.piezaposrel=[(28.272, 534.757, 418.248), (28.272, -498.214, 418.248), (28.272, -498.214, -487.698), (28.272, 534.757, -487.698),
            (-487.592, 18.569, 481.407), (-278.193, 18.569, 481.407), (134.529, 18.569, 481.407), (550.081, 18.569, 481.407),
            (-488.986, 531.658, -34.389), (132.575, 531.658, -34.389), (550.116, 531.658, -34.389), (823.732, 221.439, -35.535),
            (823.732, -186.086, -35.535), (550.485, -494.75, -34.389), (-71.076, -494.75, -34.389), (-488.617, -494.75, -34.389),
            (-761.979, -186.086, -35.535), (-761.979, 221.439, -35.535)]
    brkobj.pieza=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#   brkobj.n_piezas=18
    brkobj.n_piezas=(5, 7, 8, 9, 11, 13, 14, 16)
    brkobj.tipo_pieza="CajonPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Tinaja":
    brkobj.piezaposrel=[(-21.686, 0.367, 724.515), (38.1, -227.947, 228.405), (-218.001, -227.947, -304.276), (-54.958, 117.132, -64.425),
                        (329.977, -138.236, -75.871)]
    brkobj.pieza=[0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0]
#   brkobj.n_piezas=5
    brkobj.n_piezas=(0, 1, 2, 3, 4)
    brkobj.tipo_pieza="TinajaPieza"
    fichero_sonido="../../Sounds/rotura-ceramica.wav"
  elif obj.Kind=="Cajama":
    brkobj.piezaposrel=[(-337.772, 0.877, 218.503), (421.175, 0.877, 218.503), (421.175, 0.877, -355.754), (-337.772, 0.877, -355.754),
                        (183.611, 0.075, -394.448), (173.921, 0.075, 258.537), (-87.693, 0.075, 258.538), (-98.858, 0.075, -394.447),
                        (-335.807, -307.355, -68.413), (-335.807, 61.637, -68.413), (-335.807, 301.305, -68.413), (-97.069, 479.326, -69.139),
                        (181.251, 479.326, -69.139), (418.979, 301.539, -68.412), (418.979, -67.453, -68.413), (418.979, -307.121, -68.413),
                        (181.251, -478.297, -69.139), (-97.069, -478.298, -69.139)]
    brkobj.pieza=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#   brkobj.n_piezas=18
    brkobj.n_piezas=(5, 7, 8, 9, 11, 13, 14, 16)
    brkobj.tipo_pieza="CajamaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Altar":
    brkobj.piezaposrel=[(-833.25,-375,747.364), (-1458.187,0,747.364), (1249.875,0,747.364), (833.25,250,747.364),
                        (833.25,-500,747.364), (-624.937,-250,747.364), (-833.25,500,747.364), (1458.187,0,-747.363),
                        (-1249.875,0,-747.364), (-833.25,250,-747.364), (-833.25,-500,-747.364), (833.25,500,-747.363),
                        (624.937,-250,-747.364), (833.25,-375.0,-747.364), (-750,0,-312.5), (-750,0,0),
                        (375,-208.5,0), (750,0,0), (375,417,-312.5), (-750,417,0)]
    brkobj.pieza=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    brkobj.tipo_pieza="AltarPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Mesa":
    brkobj.piezaposrel=[(33.241, 424.587, 400.46), (33.241, -217.44, 400.46), (33.363, 907.747, -91.095), (33.363, -893.396, -91.095),
                        (33.916, 3.982, -348.49)]
    brkobj.pieza=[0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3, 4)
    brkobj.tipo_pieza="MesaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Armero":
    brkobj.piezaposrel=[(11.266, 39.284, 757.876), (11.266, 40.419, -71.098), (-640.369, 0.0, 0.0), (661.679, 0.0, 0.0)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="ArmeroPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Armero2":
    brkobj.piezaposrel=[(27.662, 266.313, -28.901), (426.008, 152.541, 0.0), (426.008, 0.0, -328.916), (-370.354, 83.482, 0.0),
                        (-370.354, 0.0, -474.776)]
    brkobj.pieza=[0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3, 4)
    brkobj.tipo_pieza="Armero2Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Cofre":
    brkobj.piezaposrel=[(1.306, 28.918, -214.936), (1.306, -405.853, 322.404), (1.306, 282.072, 322.404)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="CofrePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Mesita":
    brkobj.piezaposrel=[(27.229, 22.51, 256.355), (26.086, 257.192, -37.821), (-283.792, 25.133, -35.87), (26.086, -206.182, -40.361)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="MesitaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Meson":
    brkobj.piezaposrel=[(-83.423, -1456.786, -86.22), (-83.423, 762.365, -86.22)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="MesonPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
#  elif obj.Kind=="Tabla_xl":
#    brkobj.piezaposrel=[(-125.775, 0, 0), (446.675, 0, 0)]
#    brkobj.pieza=[0, 0]
#    brkobj.piezapos=[0, 0]
#    brkobj.piezavector=[0, 0]
#    brkobj.piezanoborrada=[0, 0]
#    brkobj.n_piezas=(0, 1)
#    brkobj.tipo_pieza="Tabla_xlPieza"
#    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Alabarda":
    brkobj.piezaposrel=[(-239.138,-0.061,992.281), (87.891,-0.044,855.715), (-62.253,-0.044,-276.193)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="AlabardaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Escudo1":
    # brkobj.piezaposrel=[(104.963,-32.225,-195.003), (104.963,-53.769,9.489)]
    brkobj.piezaposrel=[(-155.48,-44.316,-16.998), (52.099,-44.67,0.0)]     # Changed -LeadHead
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    # brkobj.piezaRotX=[0.0, 0.0]               # 
    brkobj.piezaRotY=[1.5708, 1.5708]           # Added
    brkobj.piezaRotZ=[-1.5708, -1.5708]         #   -LeadHead
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Escudo1Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Escudo2":
    # brkobj.piezaposrel=[(14.612,48.857,89.699), (85.172,-64.777,-24.035)]
    brkobj.piezaposrel=[(109.079,28.678,78.173), (-26.116,-64.591,-23.205)]     # Changed -LeadHead
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    # brkobj.piezaRotX=[0.0, 0.0]               # 
    brkobj.piezaRotY=[1.5708, 1.5708]           # Added
    brkobj.piezaRotZ=[-1.5708, -1.5708]         #   -LeadHead
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Escudo2Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Espadacurva":
    brkobj.piezaposrel=[(-27.724,321.626,-0.381), (6.363,-282.968,.006)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadacurvaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Espadaromana":
    brkobj.piezaposrel=[(-.031,350.225,4.607), (-.021,-250.782,4.508)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadaromanaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Gladius":
    brkobj.piezaposrel=[(0,0,252.933), (0,0,-204.365)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="GladiusPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Lanza":
    brkobj.piezaposrel=[(-.028,-6.682,743.075), (.148,-6.682,575.643)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="LanzaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
#  elif obj.Kind=="Naginata":
#    brkobj.piezaposrel=[(.135,617.232,-16.631), (.135,-389.267,17.343)]
#    brkobj.pieza=[0, 0]
#    brkobj.piezapos=[0, 0]
#    brkobj.piezavector=[0, 0]
#    brkobj.piezanoborrada=[0, 0]
#    brkobj.n_piezas=(0, 1)
#    brkobj.tipo_pieza="NaginataPieza"
#    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Silla":
    brkobj.piezaposrel=[(0,322.592,299.363),(0,-4.161,-124.623),(-195.632,-230.832,-426.122),(199.562,-230.832,-426.122),(-198.548,268.085,-426.123), (199.562,268.085,-426.123)]
    brkobj.pieza=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.piezapos=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.piezavector=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.piezanoborrada=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.n_piezas=(0, 1, 2, 3, 4, 5)
    brkobj.tipo_pieza="SillaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Taburete":
    brkobj.piezaposrel=[(0,42.127,184.677),(-208.95,161.695,-95.812),(.071,-199.74,-95.812),(208.95,161.695,-95.812)]
    brkobj.pieza=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.piezapos=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.piezavector=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.piezanoborrada=[0, 0 ,0 ,0 ,0 ,0]
    brkobj.n_piezas=(0, 1, 2, 3, 4, 5)
    brkobj.tipo_pieza="TaburetePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Chaosword":
    brkobj.piezaposrel=[(0,446.07,-0.39), (0,-303.205,17.343)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="ChaoswordPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Cimitarra":
    brkobj.piezaposrel=[(-8.573,-396.5,-0.058), (-16.409,206.364,-0.428)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="CimitarraPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Cuchillo":
    brkobj.piezaposrel=[(-0,345,155,137,13,785), (-0,345,-64,583,2,653)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="CuchilloPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Daga":
    brkobj.piezaposrel=[(0,0.322,95.339), (0,0.322,-92.652)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="DagaPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Escudo3":
    # brkobj.piezaposrel=[(-61.382,-35.532,39.465), (-16.783,-95.768,-105.507)]
    brkobj.piezaposrel=[(-91.837,-30.167,16.741), (77.282,-30.167,-55.469)]     # Changed -LeadHead
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    # brkobj.piezaRotX=[0.0, 0.0]               # 
    brkobj.piezaRotY=[1.5708, 1.5708]           # Added
    brkobj.piezaRotZ=[-1.5708, -1.5708]         #   -LeadHead
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Escudo3Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Escudo4":
    # brkobj.piezaposrel=[(95.325,-97.759,-34.15), (95.325,155.514,-9.344)]
    brkobj.piezaposrel=[(95.325, -34.15,155.514), (95.325, -9.344 ,-97.759)]    # Changed -LeadHead
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    # brkobj.piezaRotX=[0.0, 0.0]               # 
    brkobj.piezaRotY=[1.5708, 1.5708]           # Added
    brkobj.piezaRotZ=[-1.5708, -1.5708]         #   -LeadHead
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Escudo4Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Escudo5":
    # brkobj.piezaposrel=[(57.387,-125.758,-49.121), (98.352,26.177,-28.672)]
    brkobj.piezaposrel=[(-85.187,21.053,-20.667), (88.184,-8.672,0.0)]   # Changed -LeadHead
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    # brkobj.piezaRotX=[0.0, 0.0]               # 
    # brkobj.piezaRotY=[1.5708, 1.5708]         # Added
    brkobj.piezaRotZ=[-1.5708, -1.5708]         #   -LeadHead
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Escudo5Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Escudo6":
    # brkobj.piezaposrel=[(-22.748,-110.34,131.577), (21.852,-35.463,-75.853), (53.894,-203.998,-258.912)]
    brkobj.piezaposrel=[(166.604,0,0), (-46.381,-35.984,-96.308), (-245.775,-62.236,-77.521)]    # Changed -LeadHead
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    # brkobj.piezaRotX=[0.0, 0.0]               # 
    brkobj.piezaRotY=[1.5708, 1.5708]           # Added
    brkobj.piezaRotZ=[-1.5708, -1.5708]         #   -LeadHead
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="Escudo6Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Escudo7":
    brkobj.piezaposrel=[(-220.298,-44.599,0), (131.282,0,0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Escudo7Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Escudo8":
    brkobj.piezaposrel=[(-226.484,32.694,126.691), (89.198,47.513,301.536), (60.782,77.293,-209.227)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="Escudo8Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Escudo9":
    brkobj.piezaposrel=[(-227.405,-12.437,267.696), (62.055,0,69.057), (-136.066,-11.596,-205.709)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="Escudo9Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Espadaelfica":
    brkobj.piezaposrel=[(0,-262.339,0.123), (0,230.204,0.123)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadaelficaPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="EspadaMagica1":
    brkobj.piezaposrel=[(0,-22.538,-311.895), (0.059,-22.653,267.473)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadaMagica1Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="EspadaMagica2":
    brkobj.piezaposrel=[(0,-19.849,-148.038), (0.004,-19.845,243.376)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadaMagica2Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="EspadaMagica3":
    brkobj.piezaposrel=[(3.676,-21.791,258.245), (0.00,-21.791,-265.286)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadaMagica3Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Espada":
    brkobj.piezaposrel=[(0,-269.601,-0.051), (-5.704,177.461,-0.122)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadaPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Espadafilo":
    brkobj.piezaposrel=[(0.01,-318.21,-0.201), (8.752,241.708,-0.201)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EspadafiloPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Garropin":
    brkobj.piezaposrel=[(2.949,167.267,-250.285), (0.00,3.416,179.329)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="GarropinPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Garrote":
    brkobj.piezaposrel=[(0.0,-1.009,207.236), (0,-1.009,-141.056)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="GarrotePieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Gladius":
    brkobj.piezaposrel=[(0.0,-19.655,-254.188), (0.00,-19.655,177.446)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="GladiusPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Garrote2":
    brkobj.piezaposrel=[(53.797,36.284,-202.901), (0.0,21.664,304.433)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Garrote2Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Hacha":
    brkobj.piezaposrel=[(-0.307,142.303,-205.916), (-0.307,20.626,269.659)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="HachaPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Hacha2":
    brkobj.piezaposrel=[(0.047,-0.697,-262.585), (0.047,-0.697,296.286)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Hacha2Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Hacha3":
    brkobj.piezaposrel=[(-0.136,0,-312.819), (-0.136,-0.697,208.508)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Hacha3Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Hacha4":
    brkobj.piezaposrel=[(0,0,0), (0,0,0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Hacha4Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Hacha5":
    brkobj.piezaposrel=[(0,0,0), (0,0,0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Hacha5Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Hacha6":
    brkobj.piezaposrel=[(0,0,0), (0,0,0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Hacha6Pieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Hachacuchilla":
    brkobj.piezaposrel=[(0,0,0), (0,0,0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="HachacuchillaPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="MartilloForja":
    brkobj.piezaposrel=[(0,0,0), (0,0,0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="MartilloForjaPieza"
    fichero_sonido="../../Sounds/golpe-metal-mediano.wav"
  elif obj.Kind=="Tridente":
    brkobj.piezaposrel=[(-8.059,-94.044,307.664), (-7.811,-93.962,913.814)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="TridentePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Ninjato":
    brkobj.piezaposrel=[(0.412,0.341,-685.041), (0.412,0.341,485.074)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="NinjatoPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Naginata":
    brkobj.piezaposrel=[(0.135,-389.267,18.622), (0.135,424.167,-16.631)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="NaginataPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Maza3":
    brkobj.piezaposrel=[(0.0,-0.01,-255.693), (0.0,0,129.948)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Maza3Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Maza2":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Maza2Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Maza":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="MazaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Martillo2":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Martillo2Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Martillo":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="MartilloPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Katana":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="KatanaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Orksword":
    brkobj.piezaposrel=[(-12.78,0.76,214.75), (32.99,0.76,-276.63)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="OrkswordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Varita7":
    brkobj.piezaposrel=[(0.0,0.0,307.92), (1.18,-6.15,-90.29)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Varita7Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Varita6":
    brkobj.piezaposrel=[(0.0,-2.38,265.38), (-30.06,-2.38,-123.64)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Varita6Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Varita5":
    brkobj.piezaposrel=[(0.0,0.0,283.83), (0.0,-26.38,-120.16)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Varita5Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Varita2":
    brkobj.piezaposrel=[(0.0,0.0,299.09), (0.0,0.0,-111.53)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Varita2Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Varita1":
    brkobj.piezaposrel=[(0.0,0.0,294.1), (0.0,0.0,-115.59)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Varita1Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="VampWeapon":
    brkobj.piezaposrel=[(3.91,-526.57,0.0), (10.61,199.21,216.6)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="VampWeaponPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="VampShield":
    # brkobj.piezaposrel=[(3.529,-130.665,-31.627), (-65.514,217.216,25.712)]
    brkobj.piezaposrel=[(-79.211,-14.422,189.417), (-10.193,40.967,-185.956)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    # brkobj.piezaRotX=[0.0, 0.0]               # 
    brkobj.piezaRotY=[1.5708, 1.5708]           # Added
    brkobj.piezaRotZ=[-1.5708, -1.5708]         #   -LeadHead
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="VampShieldPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Sablazo":
    brkobj.piezaposrel=[(26.289,75.04,330.01), (0.0,75.04,-434.98)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="SablazoPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Phurbhu":
    brkobj.piezaposrel=[(-1.45,0.0,207.64), (15.65,0.0,-138.28)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="PhurbhuPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Mazapiedra":
    brkobj.piezaposrel=[(0.0,62.47,620.34), (-8.51,-73.87,-193.72), (65.78,173.94,308.63)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="MazapiedraPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="KingShield":
    brkobj.piezaposrel=[(-261.974,-22.36,267.893), (-128.144,17.982,74.314), (86.993,62.582,0)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="KingShieldPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="KingSword":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="KingSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="QueenSword":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="QueenSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="MazaDoble":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="MazaDoblePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Chakram":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="ChakramPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Chakram2":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Chakram2Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Eclipse":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EclipsePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="DeathSword":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="DeathSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="EgyptSword":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="EgyptSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Dagarrojar":
    brkobj.piezaposrel=[(0.0,0.0,0.0), (0.0,0.0,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="DagarrojarPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Dagesse":
    brkobj.piezaposrel=[(0.0,0.01,331.24), (0.0,0.0,-240.1)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="DagessePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="DalWeapon":
    brkobj.piezaposrel=[(0.07,498.65,0.0), (0.07,-498.76,0.0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="DalWeaponPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="DalShield":
    brkobj.piezaposrel=[(-9.389,-39.118,244.813), (30.764,-39.118,-152.951), (81.501,-206.624,-299.82)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="DalShieldPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Katar":
    brkobj.piezaposrel=[(0.0,0.0,156.3), (0.0,0.0,239.37), (0.0,1.27,-265.31)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="KatarPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Hachacarnicero":
    brkobj.piezaposrel=[(4.86,10.51,289.41), (180.65,11.68,182.09), (150.1,-51.7,-129.0), (143.94,8.36,-514.07)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="HachacarniceroPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Hacha2hojas":
    brkobj.piezaposrel=[(-145.43,0.0,393.78), (328.13,0.0,390.9), (-1.03,0.0,-352.07)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="Hacha2hojasPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"
  elif obj.Kind=="Hacharrajada":
    brkobj.piezaposrel=[(-2.3,0.0,54.89), (31.68,0.0,330.74), (251.32,0.0,-584.44)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="HacharrajadaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Banco":
    brkobj.piezaposrel=[(-67.18,490.33,134.23), (-67.18,-980.66,134.23), (-66.45,1494.56,-144.52), (-66.45,-1487.65,-144.52)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="BancoPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Katarmoon":
    brkobj.piezaposrel=[(-0.285,185.9,161.88), (-0.051,-57.056,3.39), (-0.029,-81.147,95.269), (0.033,-100.199,-60.945)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="KatarmoonPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Bo":
    brkobj.piezaposrel=[(-0.662,494.711,-0.927), (-0.662,-505.878,-1.214)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="BoPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="DeathBo":
    brkobj.piezaposrel=[(0,0,711.633), (-11.685,11.685,0.316),(0,0,-741.809)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="DeathBoPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="KatarDoble":
    brkobj.piezaposrel=[(-0.182,153.394,312.986), (-0.208,-53.583,312.986),(-0.21,39.94,-180.351),(-0.21,-145.398,-180.351)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="KatarDoblePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Martillo3":
    brkobj.piezaposrel=[(0,0,325.566), (0,0.319,0)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="Martillo3Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Guadanya":
    brkobj.piezaposrel=[(-101.582,1.1,638.168), (353.767,0.784,283.665), (320.618,0.752,-661.758)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="GuadanyaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="RhinoClub":
    brkobj.piezaposrel=[(-2.33,0,573.906), (171.053,4.583,-345.98)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="RhinoClubPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="LongSword":
    brkobj.piezaposrel=[(-3.768,-0.172,657.17), (25.969,-0.172,31.724), (29.416,-0.18,-626.322)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="LongSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Alfanje":
    brkobj.piezaposrel=[(0,-0.728,572.855), (46.11,-0.728,-132.907), (45.283,-0.613,-688.097)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="AlfanjePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="BigSword":
    brkobj.piezaposrel=[(-0.019,-0.552,588.416), (-0.006,-0.552,-152.926), (0,-0.38,-729.077)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="BigSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="SawSword":
    brkobj.piezaposrel=[(-85.349,-0.039,377.614), (6.326,0,-626.014)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="SawSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="FlatSword":
    brkobj.piezaposrel=[(0,-0.015,733.141), (0,0,-271.848)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="FlatSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="CrushHammer":
    brkobj.piezaposrel=[(-163.556,-0.067,315.065), (219.866,0.067,393.945), (0,0.641,-292.008)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="CrushHammerPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="TaiSword":
    brkobj.piezaposrel=[(0,16.687,469.136), (10.622,16.687,333.306), (0,16.687,108.669), (0,16.687,-254.198)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="TaiSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="IceHammer":
    brkobj.piezaposrel=[(0,0,573.752), (179.492,-58.747,444.756), (179.494,0,413.737), (-179.494,58.747,444.756), (0,0,318.22), (0,0,0)]
    brkobj.pieza=[0, 0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3, 4, 5)
    brkobj.tipo_pieza="IceHammerPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="IceAxe":
    brkobj.piezaposrel=[(195.203,0,0), (-159.931,0.096,588.766), (-195.488,0.096,359.554), (-307.34,0.096,92.469), (-111.447,0.096,-177.108)]
    brkobj.pieza=[0, 0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3, 4)
    brkobj.tipo_pieza="IceAxePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="IceSword":
    brkobj.piezaposrel=[(20.178,-3.127,454.8), (20.178,2.867,169.377), (1.319,-0.363,5.251), (0,0,-339.913)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="IceSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="DeathKatar":
    brkobj.piezaposrel=[(-0.502,47.937,137.044), (-0.433,-79.69,-317.551)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="DeathKatarPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="FireBo":
    brkobj.piezaposrel=[(-0.429,-1.212,781.945), (-0.429,-1.212,-239.367)]
    brkobj.pieza=[0, 0]
    brkobj.piezapos=[0, 0]
    brkobj.piezavector=[0, 0]
    brkobj.piezanoborrada=[0, 0]
    brkobj.n_piezas=(0, 1)
    brkobj.tipo_pieza="FireBoPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="FireBigSword":
    brkobj.piezaposrel=[(-67.518,-0.254,620.076), (160.753,-0.254,102.378), (91.842,-0.272,-483.034)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="FireBigSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="FireAxe":
    brkobj.piezaposrel=[(-232.206,0,144.275), (-189.959,0,-63.984), (269.165,0,243.343)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="FireAxePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="FireSword":
    brkobj.piezaposrel=[(-18.737,0,456.196), (12.522,0,200.119), (-19.227,0,-106.604), (0,0,-438.341)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="FireSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Naginata2":
    brkobj.piezaposrel=[(0,1.383,814.593), (54.263,1.383,424.016), (38.07,1.429,-512.302)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="Naginata2Pieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="CrushBo":
    brkobj.piezaposrel=[(0,0,849.847), (0,0,132.774), (0,0,-704.838)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="CrushBoPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="SteelFeather":
    brkobj.piezaposrel=[(-65.077,-0.196,925.256), (89.876,-0.196,424.912), (105.438,-0.196,-145.965), (79.168,-0.196,-839.472)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="SteelFeatherPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="LightEdge":
    brkobj.piezaposrel=[(-57.815,16.828,144.91), (96.914,16.828,326.207), (-0.198,16.687,-461.883)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="LightEdgePieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="HookSword":
    brkobj.piezaposrel=[(22.436,16.581,479.761), (-42.572,16.581,217.851), (-20.648,16.581,-140.253), (-43.247,16.574,-445.694)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="HookSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="DoubleSword":
    brkobj.piezaposrel=[(0,-0.798,536.655), (11.647,-0.798,80.308), (0,-0.798,-264.045), (0,-0.798,-648.778)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="DoubleSwordPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="LanzaAncha":
    brkobj.piezaposrel=[(0,0,923.956), (0,0,418.338), (-0.107,0.043,-162.571), (-0.107,0.043,-874.046)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="LanzaAnchaPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Axpear":
    brkobj.piezaposrel=[(2.957,-0.619,1088.37), (-106.142,0.257,698.323), (-29.747,-0.619,371.623), (-29.747,-0.619,-706.331)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="AxpearPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Arpon":
    brkobj.piezaposrel=[(0,-0.548,969.24), (0,-0.548,651.62), (0,-0.548,269.935), (0,-0.548,-672.17)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="ArponPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="IceWand":
    brkobj.piezaposrel=[(1.937,2.582,826.34), (0.941,1.924,248.935), (0.133,1.642,-571.2)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="IceWandPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Bichero":
    brkobj.piezaposrel=[(-16.853,-0.645,821.589), (62.048,-0.58,297.013), (62.048,-0.58,-250.226)]
    brkobj.pieza=[0, 0, 0]
    brkobj.piezapos=[0, 0, 0]
    brkobj.piezavector=[0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0]
    brkobj.n_piezas=(0, 1, 2)
    brkobj.tipo_pieza="BicheroPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"

  elif obj.Kind=="Crosspear":
    brkobj.piezaposrel=[(-106.277,-0.388,823.84), (170.436,-0.388,802.581), (-0.005,-0.4,48.933), (-0.005,-0.4,-733.476)]
    brkobj.pieza=[0, 0, 0, 0]
    brkobj.piezapos=[0, 0, 0, 0]
    brkobj.piezavector=[0, 0, 0, 0]
    brkobj.piezanoborrada=[0, 0, 0, 0]
    brkobj.n_piezas=(0, 1, 2, 3)
    brkobj.tipo_pieza="CrosspearPieza"
    fichero_sonido="../../Sounds/rotura-madera.wav"



  elif obj.Kind=="Skeleton_Optimiced":
    brkobj.piezaposrel=[(-1.1,47.6,411.3),(0.3,45.2,877.2),(-234.0,33.4,-31.4),(-218.0,63.0,337.7),(233.9,32.9,-35.3),(215.8,63.0,339.2),(96.7,-48.5,-686.0),(-92.7,-48.5,-684.4),(141.3,1.3,-167.5),(-137.0,1.3,-167.5)]
    brkobj.pieza=[0,0,0,0,0,0,0,0,0,0]
    brkobj.piezapos=[0,0,0,0,0,0,0,0,0,0]
    brkobj.piezavector=[0,0,0,0,0,0,0,0,0,0]
    brkobj.piezanoborrada=[0,0,0,0,0,0,0,0,0,0]
    brkobj.n_piezas=(0,1,2,3,4,5,6,7,8,9)
    brkobj.tipo_pieza="EsqueletoPieza"
    fichero_sonido="../../Sounds/golpe-piedra-ligera.wav"
  else:
    print "El Objeto "+obj.Name+" no es rompible"
    return ("","")
  brkobj.Broken=0
  return (brkobj, fichero_sonido)

def SetBreakable(obj_name, life_time=0, max_life_time=0, hiddenobject=""):
  obj=Bladex.GetEntity(obj_name)
  try:
  	if obj.Data.brkobjdata:
  		return
  except AttributeError:
  	pass

  databreak = GetBreakingData(obj)
  if databreak[1] == "":
  	return
  brkobj         = databreak[0]
  fichero_sonido = databreak[1]


  brkobj.sonido_rotura=Bladex.CreateSound(fichero_sonido, "SonidoRotura"+obj_name)
  brkobj.max_life_time=max_life_time
  brkobj.life_time=life_time
  #grupoexcl=Bladex.GetNewExclusionGroupId()
  #obj.ExclusionGroup=EXGRP_TOTALEXCLUSION
  obj.HitFunc=BreakSpecialObject
#	for n in range(brkobj.n_piezas):
  for n in brkobj.n_piezas:

    int_obj_name=obj_name+"Pieza"+`n+1`
    pieza_exist=Bladex.GetEntity(int_obj_name)
    if pieza_exist is None:
      brkobj.pieza[n]=Bladex.CreateEntity(int_obj_name, brkobj.tipo_pieza+`n+1`, 0.0, 0.0, 0.0,"Physic")
    else:
      brkobj.pieza[n]=pieza_exist
    brkobj.pieza[n].Scale=0.9*obj.Scale
    brkobj.pieza[n]=Bladex.GetEntity(int_obj_name)
    brkobj.pieza[n].ExclusionGroup=EXGRP_TOTALEXCLUSION
    brkobj.pieza[n].RemoveFromWorld()
    InitDataField.Initialise(brkobj.pieza[n])
    brkobj.pieza[n].Data.brkparent=brkobj
    brkobj.piezanoborrada[n]=int_obj_name
  ceros=0
  for n in brkobj.piezanoborrada:
    if not n:
      ceros=ceros+1
  if ceros:
    for n in range(ceros):
      brkobj.piezanoborrada.remove(0)
  if hiddenobject:
    brkobj.hidobj=Bladex.GetEntity(hiddenobject)
#		brkobj.hidobj.ExclusionGroup=EXGRP_TOTALEXCLUSION
    brkobj.hidobj.RemoveFromWorld()
  brkobj.hidobjname=hiddenobject
  InitDataField.Initialise(obj)
  obj.Data.brkobjdata=brkobj




def CreateHiddenObject(obj_name, entity_name, scale=1.0, position=(0.0, 0.0, 0.0), orientation=(1.0, 0.0, 0.0, 0.0)):

	hidobj=Bladex.CreateEntity(obj_name, entity_name, position[0], position[1], position[2],"Physic")
	hidobj.Scale=scale
	hidobj.Orientation=orientation
	hidobj.RemoveFromWorld()
	return hidobj

BreakSound={}
#
# Lanza el sonido de quebrarse de un objeto X
##############################################
def PlayBreakSound(obj_name):
	o = Bladex.GetEntity(obj_name)
	d = GetBreakingData(o)
	if(not BreakSound.has_key(obj_name)):
		BreakSound[o.Kind] = Bladex.CreateSound(d[1], "SonidoRotura "+o.Kind)
	BreakSound[o.Kind].Play(o.Position[0], o.Position[1], o.Position[2], 0)
