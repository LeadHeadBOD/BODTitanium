##///
##||| BARB_M1/def_class.PY TITANIUM
##||| Change list:
##||| * Restored shadows to ceiling spike trap
##\\\ 
import Bladex
import ObjStore
#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampa_Pinchos.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

MESSAGE_START_WEAPON         =7
MESSAGE_STOP_WEAPON          =8

class PinLinkCeil:
	def __init__(self,ceil,name,r_min,r_max,altura,arenilla1,arenilla2,arenilla3,arenilla4,techo_sound):
		self.ceil = Bladex.GetEntity(ceil)
		self.N_Pin = r_max - r_min
		self.altura = altura
		self.name = name
		self.pincho = []
		self.arenilla1 = arenilla1
		self.arenilla2 = arenilla2
		self.arenilla3 = arenilla3
		self.arenilla4 = arenilla4
		self.Techo_sound = techo_sound

		j = 0

		for i in range(r_min,r_max):
			self.pincho[j:j] = [Bladex.GetEntity(name + `i`)]
			self.pincho[j].MessageEvent(MESSAGE_START_WEAPON,0,0)
			# self.pincho[j].CastShadows = 0	## Don't! -LeadHead
			j = j + 1

	def PinchoSigueTecho(self,entity,time):
		disp = self.ceil.Displacement
		altura = self.altura + disp
		altura2 = -36000 + disp
		i = 0

		self.arenilla1.Position = -50500,altura2,182500
		self.arenilla1.D=5500, 0, 0
		self.arenilla2.Position = -50500,altura2,172500
		self.arenilla2.D=5500, 0, 0
		self.arenilla3.Position = -50500,altura2,182500
		self.arenilla3.D=0, 0, -10000
		self.arenilla4.Position = -45100,altura2,182500
		self.arenilla4.D=0, 0, -10000

		self.Techo_sound.Position = -48000,altura2,177000

		for i in range(self.N_Pin):
			pos = self.pincho[i].Position
			x = pos[0]
			z = pos[2]
			self.pincho[i].Position = x,altura,z

	def Link(self):
		self.pincho[0].TimerFunc = self.PinchoSigueTecho
		self.pincho[0].SubscribeToList("Timer30")

	def UnLink(self):
		self.pincho[0].RemoveFromList("Timer30")

#*************************************************************************************************
#*************************************************************************************************
#*************************************************************************************************
#*******************************								        **************************
#*******************************   Definiciones para Trampa_Pinchos.py  **************************
#*******************************								        **************************
#*************************************************************************************************
#*************************************************************************************************

class BreakSector:
	def __init__(self):
		self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
		ObjStore.ObjectsStore[self.ObjId]=self
		self.sector=None
		self.sector2=None
		self.break_sound=None
		self.hit_sound=None
		self.polvo = 0
		self.polvo_vel=None
		self.polvo_p0=None
		self.polvo_p1=None
		self.polvo_p2=None
		self.polvo_p3=None
		self.life=None
		self.pos = (0,0,0)
		self.normal = (1,0,0)

	def persistent_id(self):
		return self.ObjId

	def __getstate__(self):
		return (1,
				self.ObjId,
				self.sector,
				self.sector2,
				self.break_sound,
				self.hit_sound,
				self.polvo,
				self.polvo_vel,
				self.polvo_p0,
				self.polvo_p1,
				self.polvo_p2,
				self.polvo_p3,
				self.life,
                self.pos,
                self.normal
				)

	def __setstate__(self,parm):
		if parm[0]==1:
			self.ObjId=parm[1]
			ObjStore.ObjectsStore[self.ObjId]=self
			self.sector=parm[2]
			self.sector2=parm[3]
			self.break_sound=parm[4]
			self.hit_sound=parm[5]
			self.polvo=parm[6]
			self.polvo_vel=parm[7]
			self.polvo_p0=parm[8]
			self.polvo_p1=parm[9]
			self.polvo_p2=parm[10]
			self.polvo_p3=parm[11]
			self.life=parm[12]
			self.pos=parm[13]
			self.normal=parm[14]
		else:
			print "Version mismatch in BreakSector"
			self.ObjId=ObjStore.GetNewId() # Para identificarlo al grabar/guardar
			ObjStore.ObjectsStore[self.ObjId]=self
			self.sector=None
			self.sector2=None
			self.break_sound=None
			self.hit_sound=None
			self.polvo = 0
			self.polvo_vel=None
			self.polvo_p0=None
			self.polvo_p1=None
			self.polvo_p2=None
			self.polvo_p3=None
			self.life=None
			self.pos = (0,0,0)
			self.normal = (1,0,0)

	def HitSector(self,sector,weapon,ipx,ipy,ipz,ximpulse=0,yimpulse=0,zimpulse=0,x_norm=0,y_norm=0,z_norm=0,material=""):
		self.life = self.life - 1

		if self.life <= 0:
			self.sector.DoBreak(self.normal, (ipx,ipy,ipz), (0.0, 0.0, 0.0))
			self.sector.Active = 1
			self.sector2.OnHit = ""
			self.break_sound.Play(self.pos[0],self.pos[1],self.pos[2],0)

			if self.polvo:
				self.SetPolvo()
		else:
			self.hit_sound.Play(ipx,ipy,ipz,0)

	def InitBreak(self,pos,pos2,normal,life,dir,dir1,dir2):
		self.sector2 = Bladex.GetSector(pos2[0],pos2[1],pos2[2])
		self.sector = Bladex.GetSector(pos[0],pos[1],pos[2])

		self.break_sound=Bladex.CreateSound('../../Sounds/madera-rotura-pesada.wav', 'SonidoDesprendimiento')
		self.break_sound.Volume=1.0
		self.break_sound.MinDistance=3000
		self.break_sound.MaxDistance=40000

		self.hit_sound=Bladex.CreateSound('../../Sounds/golpe-madera-pesada.wav', 'SonidoHit')
		self.hit_sound.Volume=1.0
		self.hit_sound.MinDistance=3000
		self.hit_sound.MaxDistance=40000

		self.sector.InitBreak(dir, dir1, dir2)
		self.sector2.OnHit = self.HitSector
		self.sector2.ActiveSurface = normal
		self.normal = normal[0] * -6.5,normal[1] * -6.5,normal[2] * -6.5

		self.sector.Active = 0
		self.life = life
		self.pos = pos

	def ActivatePolvo(self,p1,p2,p3,p4,vel):
		self.polvo_vel = vel
		self.polvo_p0 = p1
		self.polvo_p1 = p2
		self.polvo_p2 = p3
		self.polvo_p3 = p4
		self.polvo = 1

	def SetPolvo(self):
		self.polvoTri(self.polvo_p0,self.polvo_p1,self.polvo_p2,self.polvo_vel,"dustA")
		self.polvoTri(self.polvo_p1,self.polvo_p2,self.polvo_p3,self.polvo_vel,"dustB")

	def polvoTri(self,a,b,c,vel,name):
		dust=Bladex.CreateEntity(name, "Entity Particle System D3", a[0],a[1],a[2])
		dust.D1= b[0]-a[0] ,b[1]-a[1] ,b[2]-a[2]
		dust.D2= c[0]-b[0] ,c[1]-b[1] ,c[2]-b[2]
		dust.ParticleType="MediumDust"
		dust.YGravity=230.0
		dust.Friction=0.2
		dust.PPS=1000
		dust.Velocity= vel
		dust.RandomVelocity=20.0
		dust.Time2Live=16
		dust.DeathTime=Bladex.GetTime() + 0.8
