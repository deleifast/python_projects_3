vnc = VNCClient(host="127.0.0.1",
			 password=None, 
			 port=5902,
			 depth=32,
			 fast=False,
			 shared=True) # Default parameters
			 
vnc.start()    # Starts the vnc client (Threaded)

vnc.send_key("a") # Sends the key "a"
vnc.send_mouse("Left", (200, 200)) # Left Clicks at x=200, y=200
vnc.send_mouse("Right", (200, 200)) # Right Clicks at x=200, y=200
vnc.get_screen() # Get a array representation of the screen shape: (?, ?, 3)
vnc.join() # Exit
