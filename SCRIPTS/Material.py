##///
##||| MATERIAL.PY TITANIUM
##||| Change list:
##||| * Added empty potions to the list for default materials.
##||| * Added random pitch.
##||| * Added  Barb_M1 and Orc_M9 bridges.
##||| * Metal torch is now actually metal.
##||| * Added reinforced boxes.
##||| * Added missing shields (KingShield, Barbarian Shield).
##||| * Added some other misc items to have a default material.
##\\\ 



def Init():
    import Bladex

    # **********************************
    # *           Materiales           *
    # **********************************


    # *** Creaci�n de sonidos ***

    s=Bladex.CreateSound('../../sounds/golpe-madera-ligera.wav', 'GolpeMaderaLigera')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('madera ligera')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-madera-mediana.wav', 'GolpeMaderaMediana')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('madera mediana')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-madera-pesada.wav', 'GolpeMaderaPesada')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('madera pesada')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-metal-ligero.wav', 'GolpeMetalLigero')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('metal ligero')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-metal-mediano.wav', 'GolpeMetalMediano')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('metal mediano')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-metal-pesado.wav', 'GolpeMetalPesado')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('metal pesado')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-piedra-ligera.wav', 'GolpePiedraLigera')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('piedra ligera')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-piedra-mediana.wav', 'GolpePiedraMediana')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('piedra mediana')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-piedra-pesada.wav', 'GolpePiedraPesada')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('piedra pesada')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-generico2.wav', 'GolpeGenerico2')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('generico2')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-cristal.wav', 'GolpeCristal')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('cristal')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-hueso.wav', 'GolpeHueso')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('hueso')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-ceramica-ligera.wav', 'GolpeCeramicaLigera')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('ceramica ligera')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-ceramica-mediana.wav', 'GolpeCeramicaMediana')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('ceramica mediana')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-ceramica-pesada.wav', 'GolpeCeramicaPesada')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('ceramica pesada')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-carne.wav', 'GolpeCarne')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('carne')
    mat.HitSound=s





















    # *** Asignaci�n de materiales ***


    # *** Madera ligera  ***

    Bladex.SetDefaultMaterial('Antorcha', 'madera ligera')
    Bladex.SetDefaultMaterial('Boingtotem2', 'madera ligera')
    Bladex.SetDefaultMaterial('Flecha', 'madera ligera')
    Bladex.SetDefaultMaterial('FlechaEnvenenada', 'madera ligera')
    Bladex.SetDefaultMaterial('FlechaFuego', 'madera ligera')
    Bladex.SetDefaultMaterial('PuenteFernando', 'madera ligera')
    Bladex.SetDefaultMaterial('Rama1', 'madera ligera')
    Bladex.SetDefaultMaterial('Rama2', 'madera ligera')
    Bladex.SetDefaultMaterial('Silla', 'madera ligera')
    Bladex.SetDefaultMaterial('VigaPlana', 'madera ligera')


    # *** Madera mediana ***
    Bladex.SetDefaultMaterial('Arco', 'madera mediana')
    Bladex.SetDefaultMaterial('Arco2', 'madera mediana')
    Bladex.SetDefaultMaterial('Arco3', 'madera mediana')
    Bladex.SetDefaultMaterial('Astillas1', 'madera mediana')
    Bladex.SetDefaultMaterial('Astillas2', 'madera mediana')
    Bladex.SetDefaultMaterial('Astillas3', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza1', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza2', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza3', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza4', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza5', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza6', 'madera mediana')
    Bladex.SetDefaultMaterial('Baston3', 'madera mediana')
    Bladex.SetDefaultMaterial('Bo', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza1', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza2', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza3', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza4', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza5', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza6', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza7', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza8', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza9', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza10', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza11', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza12', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza13', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza14', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza15', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza16', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza17', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza18', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza1', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza2', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza3', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza4', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza5', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza6', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza7', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza8', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza9', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza10', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza11', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza12', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza13', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza14', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza15', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza16', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza17', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza18', 'madera mediana')
    Bladex.SetDefaultMaterial('Cubo', 'madera mediana')
    Bladex.SetDefaultMaterial('Cofrepeque', 'madera mediana')
    Bladex.SetDefaultMaterial('CrushBo', 'madera mediana')
    Bladex.SetDefaultMaterial('Escudo2', 'madera mediana')
    Bladex.SetDefaultMaterial('Garropin', 'madera mediana')
    Bladex.SetDefaultMaterial('Garrote', 'madera mediana')
    Bladex.SetDefaultMaterial('Garrote2', 'madera mediana')
    Bladex.SetDefaultMaterial('Hoguera', 'madera mediana')
    Bladex.SetDefaultMaterial('Mesita', 'madera mediana')
    Bladex.SetDefaultMaterial('Palanca2', 'madera mediana')
    Bladex.SetDefaultMaterial('Taburete', 'madera mediana')
    Bladex.SetDefaultMaterial('Timon', 'madera mediana')
    Bladex.SetDefaultMaterial('Escudo9', 'madera mediana')      # Added -LeadHead



    # *** Madera pesada  ***
    Bladex.SetDefaultMaterial('Arbolseco', 'madera pesada')
    Bladex.SetDefaultMaterial('Arbolseco2', 'madera pesada')
    Bladex.SetDefaultMaterial('ArbolNevado2', 'madera pesada')      # Added -LeadHead
    Bladex.SetDefaultMaterial('Armero', 'madera pesada')
    Bladex.SetDefaultMaterial('Barril', 'madera pesada')
    Bladex.SetDefaultMaterial('Cajama', 'madera pesada')
    Bladex.SetDefaultMaterial('Cajon', 'madera pesada')
    Bladex.SetDefaultMaterial('Cajon2', 'madera pesada')
    Bladex.SetDefaultMaterial('Cofre', 'madera pesada')
    Bladex.SetDefaultMaterial('Mesa', 'madera pesada')
    Bladex.SetDefaultMaterial('Meson', 'madera pesada')
    Bladex.SetDefaultMaterial('RhinoClub', 'madera pesada')
    Bladex.SetDefaultMaterial('Caja_i_i', 'madera pesada')          # Added
    Bladex.SetDefaultMaterial('Caja_i_r', 'madera pesada')          # 
    Bladex.SetDefaultMaterial('PuenteAurelio', 'madera pesada')     # 
    Bladex.SetDefaultMaterial('Puenteau_Plano', 'madera pesada')    #       -LeadHead





    # *** Metal ligero   ***
    Bladex.SetDefaultMaterial('Antorcha2', 'metal ligero')
    Bladex.SetDefaultMaterial('Amuletofantasma', 'metal ligero')
    Bladex.SetDefaultMaterial('Amuletoserpiente', 'metal ligero')
    Bladex.SetDefaultMaterial('Argolla', 'metal ligero')
    Bladex.SetDefaultMaterial('Caliz', 'metal ligero')
    Bladex.SetDefaultMaterial('Candil', 'metal ligero')
    Bladex.SetDefaultMaterial('Canica', 'metal ligero')
    Bladex.SetDefaultMaterial('Casco3', 'metal ligero')
    Bladex.SetDefaultMaterial('Casco5', 'metal ligero')
    Bladex.SetDefaultMaterial('Casco4', 'metal ligero')
    Bladex.SetDefaultMaterial('Corona', 'metal ligero')
    Bladex.SetDefaultMaterial('Cincel', 'metal ligero')
    Bladex.SetDefaultMaterial('Cuchillo', 'metal ligero')
    Bladex.SetDefaultMaterial('Daga', 'metal ligero')
    Bladex.SetDefaultMaterial('Dagarrojar', 'metal ligero')
    Bladex.SetDefaultMaterial('Farol', 'metal ligero')
    Bladex.SetDefaultMaterial('Farol2', 'metal ligero')
    Bladex.SetDefaultMaterial('Gancho', 'metal ligero')
    Bladex.SetDefaultMaterial('Garfio2', 'metal ligero')
    Bladex.SetDefaultMaterial('Garfio', 'metal ligero')
    Bladex.SetDefaultMaterial('Lampared', 'metal ligero')
    Bladex.SetDefaultMaterial('Llave', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavecob', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavecobox', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavecutre', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavedor', 'metal ligero')       # Added
    Bladex.SetDefaultMaterial('Llavepla', 'metal ligero')       #       -LeadHead
    Bladex.SetDefaultMaterial('Llavemaz', 'metal ligero')
    Bladex.SetDefaultMaterial('LlaveAmarilla', 'metal ligero')
    Bladex.SetDefaultMaterial('MartilloForja', 'metal ligero')
    Bladex.SetDefaultMaterial('Suriken', 'metal ligero')
    Bladex.SetDefaultMaterial('Candelpeque', 'metal ligero')   # Added
    Bladex.SetDefaultMaterial('Tacita', 'metal ligero')        #
    Bladex.SetDefaultMaterial('Cazo', 'metal ligero')          #        -LeadHead






    # *** Metal  mediano ***
    Bladex.SetDefaultMaterial('Antorchaenpared', 'metal mediano')   # Moved to metal from wood
    Bladex.SetDefaultMaterial('Candelabro', 'metal mediano')        # Added         -LeadHead
    Bladex.SetDefaultMaterial('Alabarda', 'metal mediano')
    Bladex.SetDefaultMaterial('Bloodbol', 'metal mediano')
    Bladex.SetDefaultMaterial('Brasero1', 'metal mediano')
    Bladex.SetDefaultMaterial('CandilAurelio', 'metal mediano')
    Bladex.SetDefaultMaterial('Candil2', 'metal mediano')
    Bladex.SetDefaultMaterial('Cimitarra', 'metal mediano')
    Bladex.SetDefaultMaterial('Coraza1', 'metal mediano')
    Bladex.SetDefaultMaterial('Coraza2', 'metal mediano')
    Bladex.SetDefaultMaterial('Coraza3', 'metal mediano')
    Bladex.SetDefaultMaterial('CrushHammer', 'metal mediano')
    Bladex.SetDefaultMaterial('Dagesse', 'metal mediano')
    Bladex.SetDefaultMaterial('DeathBo', 'metal mediano')
    Bladex.SetDefaultMaterial('DoubleSword', 'metal mediano')
    Bladex.SetDefaultMaterial('Espada', 'metal mediano')
    Bladex.SetDefaultMaterial('EgyptSword', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadafilo', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadacurva', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadaelfica', 'metal mediano')
    Bladex.SetDefaultMaterial('EspadaMagica1', 'metal mediano')
    Bladex.SetDefaultMaterial('EspadaMagica2', 'metal mediano')
    Bladex.SetDefaultMaterial('EspadaMagica3', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadaromana', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo1', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo3', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo4', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo5', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo6', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo7', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo8', 'metal mediano')
    Bladex.SetDefaultMaterial('KingShield', 'metal mediano')    # Added     -LeadHead
    Bladex.SetDefaultMaterial('FireAxe', 'metal mediano')
    Bladex.SetDefaultMaterial('FireBo', 'metal mediano')
    Bladex.SetDefaultMaterial('Gancholamp', 'metal mediano')
    Bladex.SetDefaultMaterial('Gladius', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha2', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha3', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha4', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha5', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha6', 'metal mediano')
    Bladex.SetDefaultMaterial('Hachacuchilla', 'metal mediano')
    Bladex.SetDefaultMaterial('HookSword', 'metal mediano')
    Bladex.SetDefaultMaterial('Keysup', 'metal mediano')
    Bladex.SetDefaultMaterial('Katana', 'metal mediano')
    Bladex.SetDefaultMaterial('Lamparaegipto', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaMiguel', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaNegra', 'metal mediano')
    Bladex.SetDefaultMaterial('Lamparacobra', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaMiguelsinpeana', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaAurelio', 'metal mediano')
    Bladex.SetDefaultMaterial('Lampcolg', 'metal mediano')
    Bladex.SetDefaultMaterial('Lanza', 'metal mediano')
    Bladex.SetDefaultMaterial('LightEdge', 'metal mediano')
    Bladex.SetDefaultMaterial('Martillo', 'metal mediano')
    Bladex.SetDefaultMaterial('Martillo2', 'metal mediano')
    Bladex.SetDefaultMaterial('Martillo3', 'metal mediano')
    Bladex.SetDefaultMaterial('Maza', 'metal mediano')
    Bladex.SetDefaultMaterial('Maza2', 'metal mediano')
    Bladex.SetDefaultMaterial('Maza3', 'metal mediano')
    Bladex.SetDefaultMaterial('MazaDoble', 'metal mediano')
    Bladex.SetDefaultMaterial('Naginata', 'metal mediano')
    Bladex.SetDefaultMaterial('Naginata2', 'metal mediano')
    Bladex.SetDefaultMaterial('Ninjato', 'metal mediano')
    Bladex.SetDefaultMaterial('Orksword', 'metal mediano')
    Bladex.SetDefaultMaterial('QueenSword', 'metal mediano')
    Bladex.SetDefaultMaterial('KingSword', 'metal mediano')     # Added -LeadHead
    Bladex.SetDefaultMaterial('Reja', 'metal mediano')
    Bladex.SetDefaultMaterial('Rastrillo', 'metal mediano')
    Bladex.SetDefaultMaterial('Semipuxero', 'metal mediano')
    Bladex.SetDefaultMaterial('SteelFeather', 'metal mediano')
    Bladex.SetDefaultMaterial('TaiSword', 'metal mediano')
    Bladex.SetDefaultMaterial('Tridente', 'metal mediano')
    Bladex.SetDefaultMaterial('Varilla', 'metal mediano')
    Bladex.SetDefaultMaterial('Varillaancha', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita1', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita2', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita5', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita6', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita7', 'metal mediano')
    Bladex.SetDefaultMaterial('VampWeapon', 'metal mediano')







    # *** Metal pesado   ***
    Bladex.SetDefaultMaterial('Alfanje', 'metal pesado')
    Bladex.SetDefaultMaterial('BarroteAurelio', 'metal pesado')
    Bladex.SetDefaultMaterial('BigSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Chaosword', 'metal pesado')
    Bladex.SetDefaultMaterial('DalBlade', 'metal pesado')
    Bladex.SetDefaultMaterial('DalWeapon', 'metal pesado')
    Bladex.SetDefaultMaterial('DeathSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Eclipse', 'metal pesado')
    Bladex.SetDefaultMaterial('FireBigSword', 'metal pesado')
    Bladex.SetDefaultMaterial('FlatSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Guadanya', 'metal pesado')
    Bladex.SetDefaultMaterial('Hacha2hojas', 'metal pesado')
    Bladex.SetDefaultMaterial('Hacharrajada', 'metal pesado')
    Bladex.SetDefaultMaterial('LeonBronce', 'metal pesado')
    Bladex.SetDefaultMaterial('LongSword', 'metal pesado')
    Bladex.SetDefaultMaterial('PinchoManuel', 'metal pesado')
    Bladex.SetDefaultMaterial('Sablazo', 'metal pesado')
    Bladex.SetDefaultMaterial('SawSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Yunque', 'metal pesado')



    # *** Piedra ligera  ***
    Bladex.SetDefaultMaterial('CristalMineral', 'piedra ligera')
    Bladex.SetDefaultMaterial('Gema', 'piedra ligera')


    # *** Piedra mediana ***
    Bladex.SetDefaultMaterial('Bloque', 'piedra mediana')
    Bladex.SetDefaultMaterial('Gozne', 'piedra mediana')
    Bladex.SetDefaultMaterial('Palanca', 'piedra mediana')


    # *** Piedra pesada  ***
    Bladex.SetDefaultMaterial('AntorchaAtlante', 'piedra pesada')
    Bladex.SetDefaultMaterial('Cabezon', 'piedra pesada')
    Bladex.SetDefaultMaterial('Cebolla', 'piedra pesada')
    Bladex.SetDefaultMaterial('Columna', 'piedra pesada')
    Bladex.SetDefaultMaterial('Columnaestrecha', 'piedra pesada')
    Bladex.SetDefaultMaterial('Halcon', 'piedra pesada')
    Bladex.SetDefaultMaterial('Halcon2', 'piedra pesada')
    Bladex.SetDefaultMaterial('LapidaManuel', 'piedra pesada')
    Bladex.SetDefaultMaterial('Monjema', 'piedra pesada')
    Bladex.SetDefaultMaterial('Peanapiedra', 'piedra mediana')
    Bladex.SetDefaultMaterial('Roca1', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca2', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca3', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca1Aurelio', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca2Aurelio', 'piedra pesada')
    Bladex.SetDefaultMaterial('Tronoliso', 'piedra pesada')
    Bladex.SetDefaultMaterial('TronoEscarabeu', 'piedra pesada')



    # *** Hueso          ***
    Bladex.SetDefaultMaterial('Cracorn1', 'hueso')
    Bladex.SetDefaultMaterial('CraneoCornudo3', 'hueso')
    Bladex.SetDefaultMaterial('CraneoCornudo4', 'hueso')
    Bladex.SetDefaultMaterial('Femur', 'hueso')
    Bladex.SetDefaultMaterial('Restos', 'hueso')
    Bladex.SetDefaultMaterial('Skull', 'hueso')


    # *** Cristal        ***
    Bladex.SetDefaultMaterial('Botella', 'cristal')
    Bladex.SetDefaultMaterial('Botella2', 'cristal')
    Bladex.SetDefaultMaterial('BotellaVerde', 'cristal')
    Bladex.SetDefaultMaterial('IceAxe', 'cristal')
    Bladex.SetDefaultMaterial('IceHammer', 'cristal')
    Bladex.SetDefaultMaterial('IceSword', 'cristal')
    Bladex.SetDefaultMaterial('Pocima100', 'cristal')
    Bladex.SetDefaultMaterial('Pocima50', 'cristal')
    Bladex.SetDefaultMaterial('Pocima25', 'cristal')
    Bladex.SetDefaultMaterial('Pocima200', 'cristal')
    Bladex.SetDefaultMaterial('PocimaTodo', 'cristal')
    Bladex.SetDefaultMaterial('PowerPotion', 'cristal')
    
    Bladex.SetDefaultMaterial('Pocima25_E', 'cristal') ### Empty potions -LeadHead
    Bladex.SetDefaultMaterial('Pocima50_E', 'cristal')
    Bladex.SetDefaultMaterial('Pocima100_E', 'cristal')
    Bladex.SetDefaultMaterial('Pocima200_E', 'cristal')
    Bladex.SetDefaultMaterial('PocimaTodo_E', 'cristal')
    Bladex.SetDefaultMaterial('PowerPotion_E', 'cristal')    
    
    
    
    # *** Ceramica ligera***
    # Even though the material was created, it was completely unused -LeadHead
    Bladex.SetDefaultMaterial('Jarra', 'ceramica ligera')
    
    
    # *** Ceramica mediana***

    Bladex.SetDefaultMaterial('Mortero', 'ceramica mediana')
    Bladex.SetDefaultMaterial('Palangana', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza1', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza2', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza3', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza4', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza5', 'ceramica mediana')
    
    # *** Ceramica pesada***
    Bladex.SetDefaultMaterial('Tinaja', 'ceramica pesada')




    # *** Carne          ***
    Bladex.SetDefaultMaterial('VampShield', 'carne')

    # *** Generico       ***
    Bladex.SetDefaultMaterial('Alforjas', 'generico2')
    Bladex.SetDefaultMaterial('Cirio', 'generico2')
    Bladex.SetDefaultMaterial('Libro', 'generico2')
    Bladex.SetDefaultMaterial('Libro2', 'generico2')    # Added
    Bladex.SetDefaultMaterial('Libro3', 'generico2')    #       -LeadHead
    Bladex.SetDefaultMaterial('Saquito', 'generico2')
    Bladex.SetDefaultMaterial('RollodeCuerda', 'generico2')     # Added
