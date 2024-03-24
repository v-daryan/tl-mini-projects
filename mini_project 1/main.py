from random import randint

def generate_num():
	randNum = randint(0,2)
	return randNum


def story_text():
	tmode = ["car", "taxi", "nlo"]
	theNum = generate_num()
	num1 = input('Enter number #1: ')
	num2 = input('Enter number #2: ')
	adj1 = input('Enter Adjective 1 (place): ')
	adj2 = input('Enter Adjective 2: ')
	adj3 = input('Enter Adjective 3: ')
	noun1 = input('Enter Noun 1: ')
	noun2 = input('Enter Noun 2: ')
	noun3 = input('Enter Noun 3: ')
	noun4 = input('Enter Noun 4: ')
	color1 = input('Enter Color: ')
	verb = input('Enter verb: ')
	place = input('Silly Word: ')

	bpart1 = "hair"
	bpart2 = color1 + " eyes"

	if  theNum == 0:
		transport = tmode[0]
	elif theNum == 1:
		transport = tmode[1]
	else:
		transport = tmode[2]


	print("============")
	print("It was about " +num1+ " ago when I arrived at the hospital in a " +transport+ ". The hospital is a/an " +adj1+ " place, there are a lot of " +adj2+ ", " +noun1+ " here. There are nurses here who have " +color1+ " " +bpart1+ ". If someone wants to come into my room I told them that they have to "+verb+ " first. I’ve decorated my room with "+num2+ " " + noun2 + ". Today I talked to a doctor and they were wearing a " +noun3+ " on their " +bpart2+ ". I heard that all doctors " +verb+ " " +noun4+ " every day for breakfast. The most" +adj3+ " thing about being in the hospital is the " + place+ " " +noun1+ "!")

def story1():
	print("==== Story #1 ====")
	story_text()


def story2():
	print("==== Story #2 ====")
	story_text()


def story3():
	print("==== Story #3 ====")
	story_text()


def create_story():
	stories = ("1","2", "3")
	print ("Enter template ID")
	command = input(stories)

	if command == "1":
		story1()
	elif command == "2":
		story2()
	elif command == "3":
		story3()
	else:
		print("Please, enter valid template ID")


create_story()
