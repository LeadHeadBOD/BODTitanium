import Bladex
import DMusic
import string
import AuxFuncs

language = Language.CheckFallback()

Bladex.AddMusicEventMP3("tablillatomb","../../Sounds/"+language+"/tumba-escena3.mp3" , 0.1, 1.0, 1.0, 1000, 0, 0 )



###SORPRESAS


Bladex.AddMusicEventMP3("coro6","../../Sounds/CORO6.mp3",        	    1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1","../../Sounds/SORPRESA1.wav",        1.0, 1.0, 1.0, 500, 0, 0 )



Bladex.AddMusicEventWAV("incomb4","../../Sounds/INICIOCOMBATE4.wav",    1.0, 1.0, 1.0, 800, 0, 0 )


###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 600, 1, 1 )


###MUSICAS

Bladex.AddMusicEventWAV("acomblh","../../Sounds/combate-ligth.wav",     0.1, 0.1, 1.0, 1  , 1, -1 )

Bladex.AddMusicEventMP3( "atm24","../../Sounds/ATMOSFERA24.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )

Bladex.AddMusicEventWAV("combate6","../../Sounds/COMBATE6.wav",       1.0, 1.0, 1.0, 600, 1, 0 )


Bladex.AddMusicEventMP3  ( "atm1","../../Sounds/ATMOSFERA1.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm4","../../Sounds/ATMOSFERA4.wav"   , 0.1, 0.1, 1.0, 1  , 1, -1 )


Bladex.AddMusicEventWAV( "atm16","../../Sounds/ATMOSFERA16.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm18","../../Sounds/ATMOSFERA18.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm19","../../Sounds/ATMOSFERA19.mp3"   , 1.0, 1.0, 1.0, 1  , 1, -1 )


#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("grutas") )
