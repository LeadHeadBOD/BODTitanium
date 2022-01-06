import Bladex
import DMusic
import Language

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



### Locuciones

Bladex.AddMusicEventMP3("templodiosa-carga",           locspath+"templodiosa-carga.mp3",  0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("espadacontodastablillas",     locspath+"espadacontt.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("espadasinalgunatablilla",     locspath+"espadasinat.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("espadasinningunatablilla",    locspath+"espadasinnt.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("solopoderconrestotablillas",  locspath+"solopoderrt.mp3",        0.1, 1.0, 1.0, 10000.0, 0, 0 )
Bladex.AddMusicEventMP3("solotablillas",               musicspath+"solotablillas.mp3",    0.1, 1.0, 1.0, 10000.0, 0, 0 )

if char.Kind[0] == "K":
	Bladex.AddMusicEventMP3("palacellave1",locspath+"palacellave1K.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave2",locspath+"palacellave2K.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave3",locspath+"palacellave3K.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave4",locspath+"palacellave4K.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
elif char.Kind[0] == "A":
	Bladex.AddMusicEventMP3("palacellave1",locspath+"palacellave1A.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave2",locspath+"palacellave2A.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave3",locspath+"palacellave3A.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave4",locspath+"palacellave4A.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
elif char.Kind[0] == "B":
	Bladex.AddMusicEventMP3("palacellave1",locspath+"palacellave1B.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave2",locspath+"palacellave2B.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave3",locspath+"palacellave3B.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave4",locspath+"palacellave4B.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
else:
	Bladex.AddMusicEventMP3("palacellave1",locspath+"palacellave1D.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave2",locspath+"palacellave2D.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave3",locspath+"palacellave3D.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )
	Bladex.AddMusicEventMP3("palacellave4",locspath+"palacellave4D.mp3", 0.1, 1.0, 1.0, 10000.0, 0, 0 )



### Ambientes y musicas sin voz para escenas

Bladex.AddMusicEventADPCM( "aparicionchaos",   musicspath+"SOPRESA13.wav",     0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventADPCM( "estampidaorcos",   musicspath+"ATMOSFERA23.wav",   0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventADPCM( "suspense",         musicspath+"ATMOSFERA29.wav",    1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "genericaantes",    musicspath+"ATMOSFERA27.wav",   1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "genericadespues",  musicspath+"ATMOSFERA30.wav",    1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "miserere",         musicspath+"CORO3.mp3",         1.0, 1.0, 1.0, 0,     1, 0 )
Bladex.AddMusicEventADPCM( "susto",            musicspath+"SORPRESA1b.wav",    0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventMP3  ( "conseguido",       musicspath+"CORO2.2.mp3",       1.0, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventMP3  ( "emptyloquesea",    "",                             0.1, 0.1, 1.0, 0,     1, 0 )



### Combates

# los dos golems
DMusic.AddCombatMusic    ("golemla",           musicspath+"ATMOSFERA20A.mp3",      126, 1)
DMusic.AddCombatMusic    ("golemla2",          musicspath+"ATMOSFERA20A.mp3",      126, 1)

# los tres minotauros
DMusic.AddCombatMusic    ("Minot1",            musicspath+"COMBATE3.wav",      126, 1)
DMusic.AddCombatMusic    ("Minot2",            musicspath+"COMBATE3.wav",      126, 1)
DMusic.AddCombatMusic    ("Minot3",            musicspath+"COMBATE3.wav",      126, 1)

# caballero del caos
DMusic.AddCombatMusic    ("ChaosK1",           musicspath+"combate1.wav",      126, 0)
