import Bladex
import DMusic
import string
import Language

language = Language.CheckFallback()

Bladex.AddMusicEventMP3("final","../../Sounds/"+language+"/pergamino-enano.mp3"    , 0.1, 1.0, 1.0, 1000, 0,  0 )
Bladex.AddMusicEventMP3("enano","../../Sounds/"+language+"/llegada-enano.mp3"      , 0.1, 1.0, 1.0, 2000, 0,  0 )
Bladex.AddMusicEventMP3("inicio","../../Sounds/"+language+"/carga-enano.mp3"       , 0.1, 1.0, 1.0, 1000, 0,  0 )




###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 800, 1, 1 )
Bladex.AddMusicEventMP3( "empty2",  "", 2.0, 3.0, 1.0, 800, 1, 1 )

###SORPRESAS
Bladex.AddMusicEventMP3("coro5","../../Sounds/CORO5.mp3",        	     1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro6","../../Sounds/CORO6.mp3",        	     1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1","../../Sounds/SORPRESA1.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1a","../../Sounds/SORPRESA1a.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1b","../../Sounds/SORPRESA1b.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa3","../../Sounds/SORPRESA3.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3( "biblio","../../Sounds/CORO4.mp3"     ,         1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3( "biblio2","../../Sounds/CORO1.mp3"     ,        1.0, 1.0, 1.0, 400, 0, 0 )

###COMBATE
#DMusic.AddCombatMusic("Ork",  "../../sounds/COMBATE2.wav", prioridad,pre-abierto 0 , vol , f in , f out)

DMusic.AddCombatMusic("Troll_Dark",  "../../sounds/COMBATE3.wav",  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("3ORC",  "../../sounds/COMBATE2.wav"	   ,  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("9ORC",  "../../sounds/COMBATE2.wav"	   ,  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("17ORC",  "../../sounds/COMBATE2.wav"	   ,  300 , 0 , 1 , 1.0 , 2.0)
DMusic.AddCombatMusic("11ORC",  "../../sounds/COMBATE2.wav"	   ,  300 , 0 , 1 , 1.0 , 2.0)


###MUSICAS
#Bladex.AddMusicEventADPCM( "Orc","../../Sounds/ATMOSFERA5.wav",  f in , f out, vol, prioridad , 1, loop )

Bladex.AddMusicEventADPCM( "escena_Orc","../../Sounds/COMBATE3.wav"        , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "tambores_Orc1","../../Sounds/ATMOSFERA5.mp3"   , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "tambores_Orc2","../../Sounds/ATMOSFERA21.mp3"   , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "misterio_Orc","../../Sounds/ATMOSFERA7.mp3"    , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "grutas","../../Sounds/ATMOSFERA8.mp3"  	      , 1.0, 1.0, 1.0, 0  , 1, -1 )


Bladex.AddMusicEventMP3  ( "secreto1","../../Sounds/ATMOSFERA3.mp3"   , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "secreto2","../../Sounds/ATMOSFERA2.mp3"   , 1.0, 1.0, 1.0, 0  , 1, -1 )



#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("grutas") )
