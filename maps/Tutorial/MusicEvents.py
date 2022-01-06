import Bladex
import DMusic
import string
import Language



###SORPRESAS
Bladex.AddMusicEventMP3("coro4","../../Sounds/CORO4.mp3",        	    1.0, 1.0, 0.2, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro5","../../Sounds/CORO5.mp3",        	    1.0, 3.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("coro6","../../Sounds/CORO6.mp3",        	    1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1","../../Sounds/SORPRESA1.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa3","../../Sounds/SORPRESA3.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa4","../../Sounds/SORPRESA4.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa5","../../Sounds/SORPRESA5.wav",        0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventMP3("sorpresarmadura","../../Sounds/CORO4.mp3",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa8","../../Sounds/SORPRESA8.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa10","../../Sounds/SORPRESA10.wav",        1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1a","../../Sounds/SORPRESA1a.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("sorpresa1b","../../Sounds/SORPRESA1b.wav",      1.0, 1.0, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb33","../../Sounds/INICIOCOMBATE3.wav",    0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb4","../../Sounds/INICIOCOMBATE4.wav",     0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("incomb6","../../Sounds/INICIOCOMBATE6.wav",     0.1, 0.1, 1.0, 500, 0, 0 )

Bladex.AddMusicEventWAV("inicc","../../Sounds/ATMOSFERA32.wav",     0.1, 0.1, 1.0, 500, 0, 0 )
Bladex.AddMusicEventWAV("comb2","../../Sounds/COMBATE2.wav",        1.0, 1.0, 1.0, 500, 0, -1 )


###VACIO
Bladex.AddMusicEventMP3( "empty",  "", 2.0, 3.0, 1.0, 600, 1, 1 )
Bladex.AddMusicEventMP3( "empty2",  "", 2.0, 3.0, 1.0, 300, 1, 1 )

###COMBATE
#DMusic.AddCombatMusic("Great_Ork",  "../../sounds/COMBATE2.wav", prioridad,pre-abierto 0 , vol , f in , f out)

DMusic.AddCombatMusic("kgt1",  "../../sounds/combate-ligth.wav",     300 , 0 , 1 , 1.0 , 4.0)
DMusic.AddCombatMusic("kgt2",  "../../sounds/COMBATE2.wav",  	300 , 0 , 1 , 1.0 , 4.0)
DMusic.AddCombatMusic("kgt3",  "../../sounds/COMBATE2.wav",  	300 , 0 , 1 , 1.0 , 4.0)


###MUSICAS
#Bladex.AddMusicEventADPCM( "atm5","../../Sounds/ATMOSFERA5.wav",  f in , f out, vol, prioridad , 1, loop )


Bladex.AddMusicEventMP3  ( "atm5","../../Sounds/ATMOSFERA5.mp3"     , 1.0, 1.0, 1.0, 1  , 1, -1 )

Bladex.AddMusicEventMP3  ( "atm8","../../Sounds/ATMOSFERA8.mp3"     , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "atm9","../../Sounds/ATMOSFERA9.mp3"     , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventMP3  ( "MAPA2","../../Sounds/MAPA2.mp3"         , 1.0, 1.0, 1.0, 1  , 1, -1 )

Bladex.AddMusicEventADPCM( "atm26","../../Sounds/ATMOSFERA26.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )
Bladex.AddMusicEventADPCM( "atm28","../../Sounds/ATMOSFERA28.wav"   , 1.0, 1.0, 1.0, 1  , 1, 0 )
Bladex.AddMusicEventADPCM( "atm29","../../Sounds/ATMOSFERA29.wav"   , 1.0, 1.0, 1.0, 1  , 1, -1 )

#Bladex.AddMusicEventADPCM("1kd",  "../../sounds/combate-ligth.wav",   1.0, 1.0, 1.0, 1  , 1, -1 )

#Bladex.ExeMusicEvent( Bladex.GetMusicEvent("grutas") )