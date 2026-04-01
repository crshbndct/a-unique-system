extends Node3D

# This will hold our "DNA" list
var file_data = []

func _ready():
	# Run the scan as soon as the game starts
	# Change "." to any path you want to test, like "C:/" or "/home/nathan"
	run_scanner(".")

func run_scanner(path):
	var output = []
	# Use 'executable_path' for Python if 'python3' isn't in your local project path
	OS.execute("python3", [ProjectSettings.globalize_path("res://scanner.py"), path], output)
	
	if output.size() > 0:
		# We join the output array and trim whitespace to be safe
		var raw_text = output[0].strip_edges()
		
		var json = JSON.new()
		var error = json.parse(raw_text)
		
		if error == OK:
			file_data = json.data
			print("System Access Granted. Files found: ", file_data.size())
			spawn_all_towers()
		else:
			print("JSON Error: ", json.get_error_message())
			print("Raw Output was: ", raw_text) # This helps us see the culprit!

func spawn_all_towers():
	print("Ready to build the towers...")
	# We will fill this part in next!
