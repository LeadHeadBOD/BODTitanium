import Bladex
import DMusic
from Language import Current

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



### Locuciones

Bladex.AddMusicEventMP3  ( "musica_inicio",    locspath+"laberintocarga.mp3",      0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3  ( "musica_agonia",    locspath+"laberintoamigo.mp3",      0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3  ( "musica_tablilla",  locspath+"laberintotablilla.mp3",   0.1, 1.0, 1.0, 10000, 0, 0 )


### Ambientes y musicas sin voz para escenas

Bladex.AddMusicEventMP3  ( "torresalcytabvue", musicspath+"ATMOSFERA7.mp3",        1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicatablida",    musicspath+"ATMOSFERA3.mp3",        1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musicatrampatabl", musicspath+"COMBATE2.wav",          1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicaanilloext",  musicspath+"ATMOSFERA5.mp3",        1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musicaanilloint",  musicspath+"ATMOSFERA26.wav",       1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicatorrecent",  musicspath+"ATMOSFERA21.mp3",       1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "torretronoyfinal", musicspath+"INICIOCOMBATE33.wav",   0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventMP3  ( "llaveyhabitacion", musicspath+"CORO5.mp3",             0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "accesoanilloint",  musicspath+"SORPRESA7.wav",         0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "entradatrampa",    musicspath+"INICIOCOMBATE5.wav",    0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "entradaalcant",    musicspath+"INICIOCOMBATE1.wav",    0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "susto",            musicspath+"SORPRESA1.wav",         0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventMP3  ( "emptyloquesea",    "",                                 0.1, 0.1, 1.0, 0,     1, 0 )


### Combates

# Jefe orco acceso anillo interior
DMusic.AddCombatMusic    ("12bORC",            musicspath+"COMBATE3.wav",       127, 1)

# Orcos en recibidor
DMusic.AddCombatMusic    ("19ORC",             musicspath+"ATMOSFERA17.wav",    126, 1)
DMusic.AddCombatMusic    ("3ORC",              musicspath+"ATMOSFERA17.wav",    126, 1)

# Orcos almacen, descansillo y puerta habitacion duque
DMusic.AddCombatMusic    ("21ORC",             musicspath+"ATMOSFERA17.wav",    126, 1)
DMusic.AddCombatMusic    ("16ORC",             musicspath+"ATMOSFERA17.wav",    126, 1)
DMusic.AddCombatMusic    ("23ORC",             musicspath+"ATMOSFERA17.wav",    126, 1)
DMusic.AddCombatMusic    ("24ORC",             musicspath+"ATMOSFERA17.wav",    126, 1)

# Jefe orco azotea
DMusic.AddCombatMusic    ("25ORC",             musicspath+"COMBATE3.wav",       127, 1)
