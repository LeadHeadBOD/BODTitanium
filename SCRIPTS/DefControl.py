ON_RELEASE=0
ON_PRESS=1	# default



import BInput
InputManager=BInput.GetInputManager()
InputManager.SetInputActionsSet("Default")  # Me aseguro de definir las acciones en el grupo correcto


Bladex.AssocKey("Forwards","Keyboard","W")
Bladex.AssocKey("FrwdUp","Keyboard","W",ON_RELEASE)
Bladex.AssocKey("FrwdDown","Keyboard","W")
Bladex.AssocKey("Backwards","Keyboard","S")
Bladex.AssocKey("BrwdUp","Keyboard","S",ON_RELEASE)
Bladex.AssocKey("BrwdDown","Keyboard","S")
Bladex.AssocKey("Turn Left","Keyboard","A")
Bladex.AssocKey("Turn Right","Keyboard","D")
Bladex.AssocKey("Jump","Mouse","RightButton")
Bladex.AssocKey("Attack","Mouse","LeftButton")
Bladex.AssocKey("Attack Release","Mouse","LeftButton",ON_RELEASE)
Bladex.AssocKey("Block","Keyboard","LCtrl")
Bladex.AssocKey("Block Release","Keyboard","LCtrl",ON_RELEASE)
Bladex.AssocKey("Throw","Keyboard","Q")
Bladex.AssocKey("Throw Release","Keyboard","Q",ON_RELEASE)
Bladex.AssocKey("Sneak","Keyboard","Shift")
Bladex.AssocKey("Use","Keyboard","E")
Bladex.AssocKey("Toggle Weapons","Keyboard","CapsLock")
Bladex.AssocKey("Cycle Weapons","Mouse","WheelUp")
Bladex.AssocKey("Cycle Shields","Mouse","WheelDown")
Bladex.AssocKey("Cycle Objects","Keyboard","C")
Bladex.AssocKey("Select Enemy","Keyboard","Tab")
Bladex.AssocKey("SelectObj","Keyboard","Space")
Bladex.AssocKey("Screen Shot","Keyboard","F2")
Bladex.AssocKey("Next View","Keyboard","Add")
Bladex.AssocKey("Last View","Keyboard","Subtract")
Bladex.AssocKey("PowerPot","Keyboard","1")

# Mouse stuff
Bladex.AssocKey("RotateX","Mouse","X_Axis")
Bladex.AssocKey("RotateY","Mouse","Y_Axis")
Bladex.SetMouseState(0,2.000000,2.000000)

# Have a nice day.


