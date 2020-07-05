from subprocess import call

print("Enter a custom time (in minutes) until shutdown.")
print("Enter nothing to cancel the scheduled shutdown.")

command = input()

try:
  command = int(command)*60
  command = str(command)
  call(["shutdown", "-s", "-t", command])
except:
  if command == "":
    call(["shutdown", "/a"])
  else:
    command = "Invalid command... press any key to exit."
    input(command)
