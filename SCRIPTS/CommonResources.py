##///
##||| CommonResources.PY TITANIUM
##||| Change list:
##||| * pocimas_e.mmp to make sure empty potions work
##||| 
##\\\ 


def Init():
    import Bladex
    import BBLib

    BBLib.ReadMMP('../../3dChars/Kgt.mmp')
    BBLib.ReadMMP('../../3dChars/Amz.mmp')
    BBLib.ReadMMP('../../3dChars/Dwf.mmp')
    BBLib.ReadMMP('../../3dChars/Bar.mmp')
    BBLib.ReadMMP('../../3dobjs/weapons.mmp')
    BBLib.ReadMMP('../../3dobjs/genericos.mmp')
    BBLib.ReadMMP('../../3dobjs/pocimas_e.mmp') # Added -LeadHead

    
    Bladex.BodInspector()
    BBLib.LoadBOD('Piedra_01')
    BBLib.LoadBOD('Llavero')
    
    
    BBLib.LoadBOD('Pocima25_E')  # Added, preload empty bottles to prevent prevent microstutter
    BBLib.LoadBOD('Pocima50_E')  # when empty potion models are loaded during drinking -LeadHead
    BBLib.LoadBOD('Pocima100_E')
    BBLib.LoadBOD('Pocima200_E')
    BBLib.LoadBOD('PocimaTodo_E')
    BBLib.LoadBOD('PowerPotion_E')