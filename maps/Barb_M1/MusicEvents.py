import Bladex
import DMusic
import string
import Language

language = Language.CheckFallback()

###ESCENITAS
Bladex.AddMusicEventMP3("final","../../Sounds/"+language+"/kashgar-antepasados.mp3", 0.1, 1.0, 1.0, 10000, 0, 0 )
Bladex.AddMusicEventMP3("inicio","../../Sounds/"+language+"/carga-kashgar.mp3",      0.1, 1.0, 1.0, 10000, 0, 0 )


###SORPRESAS
Bladex.AddMusicEventMP3("ABREPTAFINAL","../../Sounds/INICIOCOMBATE1.wav",         1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("ABREPTATRAMP","../../Sounds/SORPRESA1.wav",     1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("ENTRACASA_J","../../Sounds/SORPRESA12.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1a","../../Sounds/SORPRESA1a.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1b","../../Sounds/SORPRESA6.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("trampapin","../../Sounds/COMBATE2.wav",    	    1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("inicombate6","../../Sounds/INICIOCOMBATE6.wav", 1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("inicombate4","../../Sounds/INICIOCOMBATE4.wav", 1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("inicombate7","../../Sounds/INICIOCOMBATE7.wav", 1.0, 1.0, 1.0, 500, 0, 0 )



###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 600, 1, 1 )

###COMBATE
#DMusic.AddCombatMusic("Ork",  "../../sounds/COMBATE2.wav", prioridad,pre-abierto 0 , vol , f in , f out)


DMusic.AddCombatMusic("Great_Ork",  "../../sounds/COMBATE2.wav",  300 , 0 , 1 , 1.0 , 1.5)
#DMusic.AddCombatMusic("Ork",  "../../sounds/ATMOSFERA5.wav",     300 , 0 , 1 , 1.0 , 1.5)



###MUSICAS
#Bladex.AddMusicEventADPCM( "Orc","../../Sounds/ATMOSFERA5.wav",  f in , f out, vol, prioridad , 1, loop )

Bladex.AddMusicEventMP3  ( "tambores_Orc","../../Sounds/ATMOSFERA5.mp3"   , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "ATMOSFERA12","../../Sounds/ATMOSFERA12.mp3"     , 1.0, 1.0, 0.8, 0  , 1,  0 )
Bladex.AddMusicEventADPCM( "ATMOSFERA32","../../Sounds/ATMOSFERA32.wav"     , 1.0, 1.0, 0.8, 0  , 1,  0 )
Bladex.AddMusicEventMP3  ( "tambores_Orc2","../../Sounds/ATMOSFERA5.mp3"  , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "grutas","../../Sounds/ATMOSFERA8.mp3"	     , 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventMP3  ( "tambores_pueblo","../../Sounds/ATMOSFERA19.mp3", 1.0, 1.0, 1.0, 0  , 1, -1 )
Bladex.AddMusicEventADPCM("Casaguagua","../../Sounds/ATMOSFERA28.wav",      1.0, 1.0, 1.0,   0, 1, 0 )

Bladex.AddMusicEventADPCM( "casa_jefe","../../Sounds/ATMOSFERA4.wav",       1.0, 1.0, 0.6, 0  , 1, -1 )



Bladex.AddMusicEventADPCM("TRAMPA",  "../../sounds/COMBATE6.wav", 	1.0, 1.0, 1.0, 0, 1, -1 )



#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("grutas") )