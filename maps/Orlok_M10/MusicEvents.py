import Bladex
import DMusic
import Language

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



### Locuciones

Bladex.AddMusicEventMP3  ( "musica_inicio",    locspath+"orlok-carga.mp3",       0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3  ( "musica_llave",     locspath+"orlok-llave.mp3",       0.1, 1.0, 1.0, 10000, 0, 0 )


### Ambientes y musicas sin voz para escenas

Bladex.AddMusicEventMP3  ( "musicaexterior",   musicspath+"ATMOSFERA18.mp3",     1.0, 1.0, 0.2, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicavalles",     musicspath+"ATMOSFERA5.mp3",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicacuevas",     musicspath+"ATMOSFERA22.mp3",     1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicafortific",   musicspath+"ATMOSFERA21.mp3",     1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musicaapgolem",    musicspath+"SORPRESA4.wav",       0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3  ( "musicafinal",      musicspath+"ATMOSFERA11.mp3",     0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventADPCM( "susto",            musicspath+"SORPRESA1b.wav",      0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "accesofortific",   musicspath+"INICIOCOMBATE7.wav",  0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "accesocuevas",     musicspath+"INICIOCOMBATE33.wav", 0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "encuentrallave",   musicspath+"INICIOCOMBATE2.wav",  0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "encuentraorbe",    musicspath+"INICIOCOMBATE2.wav",  0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventMP3  ( "cogeorbe",         musicspath+"CORO1.mp3",           1.0, 1.0, 0.5, 500,   0, 0 )
Bladex.AddMusicEventMP3  ( "usaorbe",          musicspath+"CORO2.1.mp3",         3.0, 1.0, 0.5, 500,   0, 0 )
Bladex.AddMusicEventWAV  ( "combategolem",     musicspath+"COMBATE3.wav",        2.0, 1.0, 1.0, 500,   1, -1)
Bladex.AddMusicEventMP3  ( "emptyloquesea",    "",                               0.1, 0.1, 1.0, 0,     1, 0 )


### Combates

# orcos puente inicio
DMusic.AddCombatMusic    ("OrlokOrcoPuente1",     musicspath+"COMBATE4.wav",       126, 0)
DMusic.AddCombatMusic    ("OrlokOrcoPuente2",     musicspath+"COMBATE4.wav",       126, 0)

# jefes orcos cuevas
DMusic.AddCombatMusic    ("OrlokJefeOrcoLabDer",  musicspath+"combate-ligth.wav",  126, 1)
DMusic.AddCombatMusic    ("OrlokJefeOrcoLabIzq",  musicspath+"combate-ligth.wav",  126, 1)

# caballeros oscuros
DMusic.AddCombatMusic    ("OrlokDknPatio",        musicspath+"COMBATE2.wav",       127, 1)
DMusic.AddCombatMusic    ("OrlokDknPiso",         musicspath+"COMBATE2.wav",       127, 1)

# troll guarida cuevas
DMusic.AddCombatMusic    ("OrlokTrollLab",        musicspath+"COMBATE2.wav",       127, 1)

# zombies explanada fortificacion
DMusic.AddCombatMusic    ("OrlokZombieExpl1",     musicspath+"COMBATE6.wav",       126, 0)
DMusic.AddCombatMusic    ("OrlokZombieExpl2",     musicspath+"COMBATE6.wav",       126, 0)
DMusic.AddCombatMusic    ("OrlokZombieExpl3",     musicspath+"COMBATE6.wav",       126, 0)
