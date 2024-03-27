import time


def create_timer(t):
	while t:
		mins, secs = divmod(t, 60)
		hours, mins = divmod(mins, 60)
		print(f"{hours:02}:{mins:02}:{secs:02}")
		time.sleep(1)
		t -= 1
	print("TIME'S UP!")


def countdown():
	timer_text = input("Insert time to count down (h:m:s) ")
	try:
		hours, mins, secs = map(int, timer_text.split(":"))
		timer = hours + mins + secs
		create_timer(timer)
	except:
		print("Please enter valid time format.")

countdown()
