# Key in password with 3 chances
# If pwd correct print "Login success." 
# If not, print "Login failed, _ more try."
# If exceed max try times, print "Login failed" and quit

password = "55688"
try_time = 3
while try_time > 0:
	key_in = input("Please key in password:")
	if key_in == password:
		print("Login success.")
		try_time = -1
	else:
		try_time = try_time - 1
		if try_time == 0:
			print("Login failed. Bye")
			break
		print("Login failed,", try_time, "more try.")

SystemExit