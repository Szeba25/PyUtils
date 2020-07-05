import urllib.request
import os.path
from subprocess import call

# CONFIG

program_directory = "C:/Development/Data/Ytdl"

# END

if (not os.path.isdir(program_directory)):
	os.mkdir(program_directory)

if (not os.path.isfile(program_directory + "/youtube-dl.exe")):
	print("youtube-dl.exe is missing... Downloading...")
	urllib.request.urlretrieve("https://yt-dl.org/downloads/latest/youtube-dl.exe", program_directory + "/youtube-dl.exe")
	print("Success!")

run = True

print("Welcome to youtube-dl shell!")
print("> d [url] -> Download video")
print("> u       -> Update youtube-dl.exe")
print("> e       -> Exit")

while(run):
	print("> ", end="")
	command = input()
	if (len(command) > 0):
		prefix = command[0]
		if (prefix == "d"):
			params = command.split()
			if (len(params) > 1):
				os.chdir(program_directory)
				call(['youtube-dl.exe', params[1]])
			else:
				print("Please specify the download url!")
		elif (prefix == "u"):
			print("Updating youtube-dl.exe...")
			urllib.request.urlretrieve("https://yt-dl.org/downloads/latest/youtube-dl.exe", program_directory + "/youtube-dl.exe")
			print("Success!")
		elif (prefix == "e"):
			run = False
		else:
			print("Invalid command")
	else:
		print("Invalid command")
