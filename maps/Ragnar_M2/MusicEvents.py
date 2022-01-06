import Bladex
import DMusic
import Language

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



### Locuciones

#Bladex.AddMusicEventMP3(nombre, fichero, tiempo_fadein, tiempo_fadeout, volumen, prioridad, ambiente, iNext)
Bladex.AddMusicEventMP3  ( "inicioragnar",    locspath+"ragnar-txtcarga.mp3",  0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3  ( "locuraragnar",    locspath+"loc-locuraragnar.mp3", 0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3  ( "documentoragnar", locspath+"documento-ragnar.mp3", 0.1, 1.0, 1.0, 10000, 0, 0 )



### Ambientes y musicas sin voz para escenas

Bladex.AddMusicEventADPCM( "chaosragnar",     musicspath+"SOPRESA13.wav",        0.1, 1.0, 1.0, 0,     1, 0 )
Bladex.AddMusicEventMP3  ( "suspenselento",   musicspath+"ATMOSFERA24.mp3",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "suspenserapido",  musicspath+"ATMOSFERA1.mp3",       1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicazonacaos",  musicspath+"ATMOSFERA7.mp3",       1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musicatorre",     musicspath+"ATMOSFERA16.wav",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicapendulos",  musicspath+"ATMOSFERA18.mp3",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "presentapatio",   musicspath+"ATMOSFERA11.mp3",      0.1, 1.0, 1.0, 0,     1, 0 )
Bladex.AddMusicEventMP3  ( "musicacapilla",   musicspath+"CORO4.mp3",            0.1, 1.0, 0.4, 0,     1, 0 )
Bladex.AddMusicEventADPCM( "ragnarguardaesp", musicspath+"INICIOCOMBATE7.wav",   0.1, 0.5, 0.8, 0,     1, 0 )
Bladex.AddMusicEventADPCM( "ragnarcuchillas", musicspath+"INICIOCOMBATE5.wav",   0.1, 0.5, 0.8, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "musicatrampa",    musicspath+"INICIOCOMBATE6.wav",   0.1, 0.5, 0.8, 100,   0, 0 )
Bladex.AddMusicEventMP3  ( "recompensa",      musicspath+"CORO5.mp3",            0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3  ( "emptyloquesea",   "",                                0.1, 0.1, 1.0, 0,     1, 0 )



### Combates

# primer caballero
DMusic.AddCombatMusic    ("3kngt",            musicspath+"combate-ligth.wav",    126, 1)

# caballeros del patio
DMusic.AddCombatMusic    ("5bkngt",           musicspath+"COMBATE6.wav",         126, 1)
DMusic.AddCombatMusic    ("4kngt",            musicspath+"COMBATE6.wav",         126, 1)
DMusic.AddCombatMusic    ("5kngt",            musicspath+"COMBATE6.wav",         126, 1)
DMusic.AddCombatMusic    ("tres1kngt",        musicspath+"COMBATE4.wav",         127, 0)

# caballeros parlantes
DMusic.AddCombatMusic    ("Eric",             musicspath+"combate-ligth.wav",         126, 1)
DMusic.AddCombatMusic    ("Terry",            musicspath+"combate-ligth.wav",         126, 1)

# caballeros tras el caballero del caos
DMusic.AddCombatMusic    ("22kngt",           musicspath+"combate-ligth.wav",         126, 1)
DMusic.AddCombatMusic    ("23kngt",           musicspath+"combate-ligth.wav",         126, 1)

# guardaespaldas de Ragnar
DMusic.AddCombatMusic    ("Guarda1",          musicspath+"combate-ligth.wav",         126, 1)
DMusic.AddCombatMusic    ("Guarda2",          musicspath+"combate-ligth.wav",         126, 1)

# Ragnar
DMusic.AddCombatMusic    ("Ragnar",           musicspath+"COMBATE2.wav",         12700, 0)

# caballero del caos
DMusic.AddCombatMusic    ("ChaosK1",          musicspath+"COMBATE3.wav",         127, 0)
