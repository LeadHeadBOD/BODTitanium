##///
##||| MATERIAL.PY TITANIUM
##||| Change list:
##||| * Reverted to 2001 code since both re-release code breaks certain things.
##\\\ 




import Bladex
import InitDataField
import B3DLib
import GameStateAux
import pdb
import ObjStore

REL=0
ABS=1




def DisplaceAndRotateObjectFunc(obj_name, time):

	obj=Bladex.GetEntity(obj_name)

	dinobj=obj.Data.dinobjdata

	if (dinobj.OnMovement==0 and dinobj.OnRotation==0):
		obj.RemoveFromList(dinobj.Timer)
		obj.TimerFunc=""
		return

	if (dinobj.OnMovement==1):
		if (time<dinobj.end_time):
			itime=time-dinobj.last_time
			dinobj.displ=dinobj.init_vel*itime+(dinobj.acc*(itime**2))/2.0
			x=dinobj.displ_vector[0]*dinobj.displ
			y=dinobj.displ_vector[1]*dinobj.displ
			z=dinobj.displ_vector[2]*dinobj.displ
			obj.Move(x,y,z)
			iend_vel=dinobj.init_vel+dinobj.acc*itime
			dinobj.init_vel=iend_vel
			dinobj.last_time=time
			if (dinobj.while_displ_sound):
				dinobj.while_displ_sound.Position=dinobj.obj.Position
			if (dinobj.WhileDisplFunc):
				apply(dinobj.WhileDisplFunc, dinobj.WhileDisplArgs)
		else:
			itime=dinobj.end_time-dinobj.last_time
			dinobj.displ=dinobj.init_vel*itime+(dinobj.acc*(itime**2))/2.0
			x=dinobj.displ_vector[0]*dinobj.displ
			y=dinobj.displ_vector[1]*dinobj.displ
			z=dinobj.displ_vector[2]*dinobj.displ
			obj.Move(x,y,z)
			dinobj.OnMovement=0
			if (dinobj.while_displ_sound and (dinobj.while_displ_sound!=dinobj.next_while_displ_sound or dinobj.last_displ)):
				dinobj.while_displ_sound.StopSound()
			if (dinobj.end_displ_sound):
				dinobj.end_displ_sound.Position=dinobj.obj.Position
				dinobj.end_displ_sound.PlaySound(0)
			if (dinobj.OnRotation==0):
				obj.RemoveFromList(dinobj.Timer)
				obj.TimerFunc=""
			if (dinobj.EndDisplFunc):
				apply(dinobj.EndDisplFunc, dinobj.EndDisplArgs)

	if (dinobj.OnRotation==1):
		if (time<dinobj.end_time_w):
			itime=time-dinobj.last_time_w
			dinobj.angle=dinobj.init_w*itime+(dinobj.acc_w*(itime**2))/2.0
			ce=dinobj.center
			ax=dinobj.axis
			if (dinobj.rotation_type==REL):
				obj.RotateRel(ce[0], ce[1], ce[2], ax[0], ax[1], ax[2], dinobj.angle)
			else:
				obj.RotateAbs(ce[0], ce[1], ce[2], ax[0], ax[1], ax[2], dinobj.angle)
			iend_w=dinobj.init_w+dinobj.acc_w*itime
			dinobj.init_w=iend_w
			dinobj.last_time_w=time
			if (dinobj.while_rot_sound):
				dinobj.while_rot_sound.Position=dinobj.obj.Position
			if (dinobj.WhileRotFunc):
				apply(dinobj.WhileRotFunc, dinobj.WhileRotArgs)
		else:
			itime=dinobj.end_time_w-dinobj.last_time_w
			dinobj.angle=dinobj.init_w*itime+(dinobj.acc_w*(itime**2))/2.0
			ce=dinobj.center
			ax=dinobj.axis
			if (dinobj.rotation_type==REL):
				obj.RotateRel(ce[0], ce[1], ce[2], ax[0], ax[1], ax[2], dinobj.angle)
			else:
				obj.RotateAbs(ce[0], ce[1], ce[2], ax[0], ax[1], ax[2], dinobj.angle)
			dinobj.OnRotation=0
			if (dinobj.while_rot_sound and (dinobj.while_rot_sound!=dinobj.next_while_rot_sound or dinobj.last_rot)):
				dinobj.while_rot_sound.StopSound()
			if (dinobj.end_rot_sound):
				dinobj.end_rot_sound.Position=dinobj.obj.Position
				dinobj.end_rot_sound.PlaySound(0)
			if (dinobj.OnMovement==0):
				obj.RemoveFromList(dinobj.Timer)
				obj.TimerFunc=""
			if (dinobj.EndRotFunc):
				apply(dinobj.EndRotFunc, dinobj.EndRotArgs)





##class DinObj(GameStateAux.PersistentObject):
class DinObj:

	ObjId=""
	Activado=0
	OnMovement=0
	OnRotation=0
	prev_while_displ_sound=None
	while_displ_sound=None
	next_while_displ_sound=None
	end_displ_sound=None
	current_displ=0
	last_displ=1
	prev_while_rot_sound=None
	while_rot_sound=None
	next_while_rot_sound=None
	end_rot_sound=None
	last_rot=1
	Timer="Timer60"
	obj=None

	displ_vector=(0,0,0)
	displ=0
	end_time=0
	last_time=0
	init_vel=0
	acc=0
	init_w=0
	acc_w=0
	center=(0,0,0)
	axis=(0,0,0)
	rotation_type=0
	end_time_w=0
	last_time_w=0

	EndDisplFunc=None
	EndDisplArgs=None
	EndRotFunc=None
	EndRotArgs=None
	
	WhileDisplFunc=None
	WhileDisplArgs=None
	WhileRotFunc=None
	WhileRotArgs=None



	def __init__(self):
##		GameStateAux.PersistentObject.__init__(self)
		self.ObjId=ObjStore.GetNewId()
		ObjStore.ObjectsStore[self.ObjId]=self

	def DisplaceDinObj(self):

		self.OnMovement=1
		if (self.OnRotation==0):
			self.obj.TimerFunc=DisplaceAndRotateObjectFunc
			self.obj.SubscribeToList(self.Timer)


	def RotateDinObj(self):

		self.OnRotation=1
		if (self.OnMovement==0):
			self.obj.TimerFunc=DisplaceAndRotateObjectFunc
			self.obj.SubscribeToList(self.Timer)

	def Stop(self):

		self.OnMovement=0
		self.OnRotation=0

	def StopOnStep(self):

		self.EndDisplFunc=None
		self.EndRotFunc=None

	def StopDisplacement(self):

		self.OnMovement=0

	def StopDisplacementOnStep(self):

		self.EndDisplFunc=None

	def StopRotation(self):

		self.OnRotation=0

	def StopRotationOnStep(self):

		self.EndRotFunc=None

	def persistent_id(self):
		return self.ObjId


	def __getstate__(self):
		# Tiene que devolver como poder guardar el estado de la clase

		return (1,
				self.ObjId,
				self.Activado,
				self.OnMovement,
				self.OnRotation,
				GameStateAux.SaveEntityAux(self.prev_while_displ_sound),
				GameStateAux.SaveEntityAux(self.while_displ_sound),
				GameStateAux.SaveEntityAux(self.next_while_displ_sound),
				self.last_displ,
				GameStateAux.SaveEntityAux(self.prev_while_rot_sound),
				GameStateAux.SaveEntityAux(self.while_rot_sound),
				GameStateAux.SaveEntityAux(self.next_while_rot_sound),
				self.last_rot,
				self.Timer,
				GameStateAux.SaveEntityAux(self.obj),
				self.displ_vector,
				self.displ,
				self.end_time,
				self.last_time,
				self.init_vel,
				self.acc,
				self.init_w,
				self.acc_w,
				self.center,
				self.axis,
				self.rotation_type,
				self.end_time_w,
				self.last_time_w,
				GameStateAux.SaveFunctionAux(self.EndDisplFunc),
				self.EndDisplArgs,
				GameStateAux.SaveFunctionAux(self.EndRotFunc),
				self.EndRotArgs,
				GameStateAux.SaveFunctionAux(self.WhileDisplFunc),
				self.WhileDisplArgs,
				GameStateAux.SaveFunctionAux(self.WhileRotFunc),
				self.WhileRotArgs,
				GameStateAux.SaveEntityAux(self.end_displ_sound),
				self.current_displ,
				GameStateAux.SaveNewMembers(self)
				)

	def __setstate__(self,parm):
		# Toma como parámetro lo que devuelve __getstate__() y debe recrear la clase

		if parm[0]==1:
			#self.ObjId=parm[1] En GameStateAux.PersistentObject()
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.Activado=parm[2]
			self.OnMovement=parm[3]
			self.OnRotation=parm[4]

			self.prev_while_displ_sound=GameStateAux.LoadEntityAux(parm[5])
			self.while_displ_sound=GameStateAux.LoadEntityAux(parm[6])
			self.next_while_displ_sound=GameStateAux.LoadEntityAux(parm[7])

			self.last_displ=parm[8]
			
			self.prev_while_rot_sound=GameStateAux.LoadEntityAux(parm[9])
			self.while_rot_sound=GameStateAux.LoadEntityAux(parm[10])
			self.next_while_rot_sound=GameStateAux.LoadEntityAux(parm[11])

			self.last_rot=parm[12]
			self.Timer=parm[13]
			self.obj=GameStateAux.LoadEntityAux(parm[14])

			self.displ_vector=parm[15]
			self.displ=parm[16]
			self.end_time=parm[17]
			self.last_time=parm[18]
			self.init_vel=parm[19]
			self.acc=parm[20]
			self.init_w=parm[21]
			self.acc_w=parm[22]
			self.center=parm[23]
			self.axis=parm[24]
			self.rotation_type=parm[25]
			self.end_time_w=parm[26]
			self.last_time_w=parm[27]

			GameStateAux.LoadFunctionAux(parm[28],self,"EndDisplFunc")
			self.EndDisplArgs=parm[29]
			GameStateAux.LoadFunctionAux(parm[30],self,"EndRotFunc")
			self.EndRotArgs=parm[31]
			GameStateAux.LoadFunctionAux(parm[32],self,"WhileDisplFunc")
			self.WhileDisplArgs=parm[33]
			GameStateAux.LoadFunctionAux(parm[34],self,"WhileRotFunc")
			self.WhileRotArgs=parm[35]
			self.end_displ_sound=GameStateAux.LoadEntityAux(parm[36])
			self.current_displ=parm[37]

			GameStateAux.LoadNewMembers(self,parm[38])

			if self.obj:
				self.obj.Data=self
		else:
			print "DinObj.__setstate__() -> Version mismatch"
			self.ObjId=ObjStore.GetNewId()
			ObjStore.ObjectsStore[self.ObjId]=self




def DisplaceObject(dinobj, displ, displ_vector, init_vel, end_vel, init_displ_sound="", while_displ_sound="", end_displ_sound="", WhileDisplFunc="", WhileDisplArgs=(), EndDisplFunc="", EndDisplArgs=()):

	dinobj.displ=displ
	dinobj.displ_vector=B3DLib.Normalize(displ_vector)
	dinobj.init_vel=float(init_vel)
	dinobj.init_displ_sound=init_displ_sound
	dinobj.while_displ_sound=while_displ_sound
	dinobj.end_displ_sound=end_displ_sound
	dinobj.WhileDisplFunc=WhileDisplFunc
	dinobj.WhileDisplArgs=WhileDisplArgs
	dinobj.EndDisplFunc=EndDisplFunc
	dinobj.EndDisplArgs=EndDisplArgs
	dinobj.acc=(end_vel**2-init_vel**2)/(2.0*displ)
	if (dinobj.acc==0.0):
		displ_time=displ/float(init_vel)
	else:
		displ_time=(end_vel-init_vel)/dinobj.acc
	if (dinobj.init_displ_sound):
		dinobj.init_displ_sound.Position=dinobj.obj.Position
		dinobj.init_displ_sound.PlaySound(0)
	if (dinobj.while_displ_sound and dinobj.while_displ_sound!=dinobj.prev_while_displ_sound):
		dinobj.while_displ_sound.Position=dinobj.obj.Position
		dinobj.while_displ_sound.PlaySound(-1)
	start_time=Bladex.GetTime()
	dinobj.last_time=Bladex.GetTime()
	dinobj.end_time=start_time+displ_time
	dinobj.DisplaceDinObj()


def DisplaceObjectFromTo(dinobj, init_point, end_point, init_vel, end_vel, init_displ_sound="", while_displ_sound="", end_displ_sound="", WhileDisplFunc="", WhileDisplArgs=(), EndDisplFunc="", EndDisplArgs=()):
##	pdb.set_trace()
	displ_vector=end_point[0]-init_point[0], end_point[1]-init_point[1], end_point[2]-init_point[2]
	displ=(displ_vector[0]**2+displ_vector[1]**2+displ_vector[2]**2)**0.5
	dinobj.obj.Position=init_point
	DisplaceObject(dinobj, displ, displ_vector, init_vel, end_vel, init_displ_sound, while_displ_sound, end_displ_sound, WhileDisplFunc, WhileDisplArgs, EndDisplFunc, EndDisplArgs)


def RotateObject(dinobj, angle, init_w, end_w, center, axis, rotation_type=REL, init_rot_sound="", while_rot_sound="", end_rot_sound="", WhileRotFunc="", WhileRotArgs=(), EndRotFunc="", EndRotArgs=()):

	dinobj.angle=angle
	if (angle<0):
		init_w=-init_w
		end_w=-end_w
	dinobj.init_w=float(init_w)
	dinobj.center=center
	dinobj.axis=axis
	dinobj.rotation_type=rotation_type
	dinobj.init_rot_sound=init_rot_sound
	dinobj.while_rot_sound=while_rot_sound
	dinobj.end_rot_sound=end_rot_sound
	dinobj.WhileRotFunc=WhileRotFunc
	dinobj.WhileRotArgs=WhileRotArgs
	dinobj.EndRotFunc=EndRotFunc
	dinobj.EndRotArgs=EndRotArgs
	dinobj.acc_w=(end_w**2-init_w**2)/(2.0*angle)
	if (dinobj.acc_w==0.0):
		rotat_time=angle/float(init_w)
	else:
		rotat_time=(end_w-init_w)/dinobj.acc_w
	if (dinobj.init_rot_sound):
		dinobj.init_rot_sound.Position=dinobj.obj.Position
		dinobj.init_rot_sound.PlaySound(0)
	if (dinobj.while_rot_sound and dinobj.while_rot_sound!=dinobj.prev_while_rot_sound):
		dinobj.while_rot_sound.Position=dinobj.obj.Position
		dinobj.while_rot_sound.PlaySound(-1)
	start_time=Bladex.GetTime()
	dinobj.last_time_w=Bladex.GetTime()
	dinobj.end_time_w=start_time+rotat_time
	dinobj.RotateDinObj()


def NDisplacement(dinobj, displ, displ_vector, init_vel, end_vel, init_displ_sound, while_displ_sound, end_displ_sound):

	dinobj.currentdispl=dinobj.currentdispl+1
	n=dinobj.currentdispl
	dinobj.prev_while_displ_sound=while_displ_sound[n-1]
	if (n<dinobj.ndispl-1):
		dinobj.next_while_displ_sound=while_displ_sound[n+1]
		DisplaceObject(dinobj, displ[n], displ_vector[n], init_vel[n], end_vel[n], init_displ_sound[n], while_displ_sound[n], end_displ_sound[n], dinobj.WhileDisplFunc, dinobj.WhileDisplArgs, NDisplacement, (dinobj, displ, displ_vector, init_vel, end_vel, init_displ_sound, while_displ_sound, end_displ_sound))
	else:
		dinobj.next_while_displ_sound=""
		dinobj.last_displ=1
		DisplaceObject(dinobj, displ[n], displ_vector[n], init_vel[n], end_vel[n], init_displ_sound[n], while_displ_sound[n], end_displ_sound[n], dinobj.WhileDisplFunc, dinobj.WhileDisplArgs, dinobj.EndNDisplFunc, dinobj.EndNDisplArgs)


def NDisplaceObject(dinobj, displ, displ_vector, init_vel, end_vel, init_displ_soundlist=(), while_displ_soundlist=(), end_displ_soundlist=(), WhileDisplFunc="", WhileDisplArgs=(), EndDisplFunc="", EndDisplArgs=()):

	init_displ_sound=[]
	while_displ_sound=[]
	end_displ_sound=[]
	for n in range(len(displ)):
		init_displ_sound.append("")
		while_displ_sound.append("")
		end_displ_sound.append("")
	for n in range(len(init_displ_soundlist)):
		init_displ_sound[n]=init_displ_soundlist[n]
	for n in range(len(while_displ_soundlist)):
		while_displ_sound[n]=while_displ_soundlist[n]
	for n in range(len(end_displ_soundlist)):
		end_displ_sound[n]=end_displ_soundlist[n]
	dinobj.EndNDisplFunc=EndDisplFunc
	dinobj.EndNDisplArgs=EndDisplArgs
	dinobj.ndispl=len(displ)
	dinobj.currentdispl=0
	dinobj.prev_while_displ_sound=""
	dinobj.next_while_displ_sound=while_displ_sound[1]
	dinobj.last_displ=0
	DisplaceObject(dinobj, displ[0], displ_vector[0], init_vel[0], end_vel[0], init_displ_sound[0], while_displ_sound[0], end_displ_sound[0], WhileDisplFunc, WhileDisplArgs, NDisplacement, (dinobj, displ, displ_vector, init_vel, end_vel, init_displ_sound, while_displ_sound, end_displ_sound))


def NRotation(dinobj, angle, init_w, end_w, center, axis, init_rot_sound, while_rot_sound, end_rot_sound):

	dinobj.currentangle=dinobj.currentangle+1
	n=dinobj.currentangle
	dinobj.prev_while_rot_sound=while_rot_sound[n-1]
	if (n<dinobj.nangle-1):
		dinobj.next_while_rot_sound=while_rot_sound[n+1]
		RotateObject(dinobj, angle[n], init_w[n], end_w[n], center[n], axis[n], dinobj.rotation_type, init_rot_sound[n], while_rot_sound[n], end_rot_sound[n], dinobj.WhileRotFunc, dinobj.WhileRotArgs, NRotation, (dinobj, angle, init_w, end_w, center, axis, init_rot_sound, while_rot_sound, end_rot_sound))
	else:
		dinobj.next_while_rot_sound=""
		dinobj.last_rot=1
		RotateObject(dinobj, angle[n], init_w[n], end_w[n], center[n], axis[n], dinobj.rotation_type, init_rot_sound[n], while_rot_sound[n], end_rot_sound[n], dinobj.WhileRotFunc, dinobj.WhileRotArgs, dinobj.EndNRotFunc, dinobj.EndNRotArgs)


def NRotateObject(dinobj, angle, init_w, end_w, center, axis, rotation_type=REL, init_rot_soundlist=(), while_rot_soundlist=(), end_rot_soundlist=(), WhileRotFunc="", WhileRotArgs=(), EndRotFunc="", EndRotArgs=()):

	init_rot_sound=[]
	while_rot_sound=[]
	end_rot_sound=[]
	for n in range(len(angle)):
		init_rot_sound.append("")
		while_rot_sound.append("")
		end_rot_sound.append("")
	for n in range(len(init_rot_soundlist)):
		init_rot_sound[n]=init_rot_soundlist[n]
	for n in range(len(while_rot_soundlist)):
		while_rot_sound[n]=while_rot_soundlist[n]
	for n in range(len(end_rot_soundlist)):
		end_rot_sound[n]=end_rot_soundlist[n]
	dinobj.EndNRotFunc=EndRotFunc
	dinobj.EndNRotArgs=EndRotArgs
	dinobj.nangle=len(angle)
	dinobj.currentangle=0
	dinobj.prev_while_rot_sound=""
	dinobj.next_while_rot_sound=while_rot_sound[1]
	dinobj.last_rot=0
	RotateObject(dinobj, angle[0], init_w[0], end_w[0], center[0], axis[0], rotation_type, init_rot_sound[0], while_rot_sound[0], end_rot_sound[0], WhileRotFunc, WhileRotArgs, NRotation, (dinobj, angle, init_w, end_w, center, axis, init_rot_sound, while_rot_sound, end_rot_sound))


def CreateDinamicObject(obj_name):

	dinobj=DinObj()
	dinobj.obj=Bladex.GetEntity(obj_name)
	InitDataField.Initialise(dinobj.obj)
	dinobj.obj.Data.dinobjdata=dinobj
	return dinobj
