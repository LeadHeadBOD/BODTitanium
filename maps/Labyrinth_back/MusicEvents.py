import Bladex
from Language import Current

language = Language.CheckFallback()

locspath="../../Sounds/"+language+"/"
musicspath="../../Sounds/"



### Locuciones

Bladex.AddMusicEventMP3  ( "musica_tablilla",  locspath+"laberintotablilla.mp3", 0.1, 1.0, 1.0, 10000, 0, 0 )


### Ambientes y musicas sin voz para escenas

Bladex.AddMusicEventMP3  ( "alcantytabvue",    musicspath+"ATMOSFERA7.mp3",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musicatablida",    musicspath+"ATMOSFERA3.mp3",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musicatrampatabl", musicspath+"COMBATE2.wav",        1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventMP3  ( "musica1anillo",    musicspath+"ATMOSFERA18.mp3",     1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "musica2anillo",    musicspath+"ATMOSFERA4.wav",      1.0, 1.0, 1.0, 0,     1, -1)
Bladex.AddMusicEventADPCM( "entradatrampa",    musicspath+"INICIOCOMBATE5.wav",  0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventADPCM( "entradaalcant",    musicspath+"INICIOCOMBATE33.wav", 0.1, 1.0, 1.0, 100,   0, 0 )
Bladex.AddMusicEventMP3  ( "musicaapchaos",    musicspath+"ATMOSFERA11.mp3",     0.1, 1.0, 1.0, 0,     1, 0 )
