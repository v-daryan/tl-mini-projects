from random import randint

def generate_num():
	randNum = randint(0,2)
	return randNum


def story1():
    print("==== Story #1 ====")

    measure_of_time = input('Measure of time: ')
    num2 = input('Input a number: ')
    adjective1 = input('Input a Adjective 1 (place): ')
    adjective2 = input('Input a Adjective 2: ')
    adjective3 = input('Input a Adjective 3: ')
    noun1 = input('Input a Noun 1: ')
    noun2 = input('Input a Noun 2: ')
    noun3 = input('Input a Noun 3: ')
    noun4 = input('Input a Noun 4: ')
    color1 = input('Input a Color: ')
    verb = input('Input a verb: ')
    silly_Word = input('Silly Word: ')

    body_part1 = "hair"
    body_part2 = "eyes"

    tmode = ["car", "taxi", "nlo"]
    the_num = generate_num()

    if the_num == 0:
        transport = tmode[0]
    elif the_num == 1:
        transport = tmode[1]
    else:
        transport = tmode[2]

    print("============")
    print(f"It was about {measure_of_time} ago when I arrived at the hospital in a {transport}. The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here. There are nurses here who have {color1} {body_part1}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {num2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. I heard that all doctors {verb} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_Word} {noun1}!")


def story2():
    print("==== Story #2 ====")
    person_name = input('Person Name: ')
    measure_of_time = input('Measure of time: ')
    noun1 = input('Input a Noun 1: ')
    noun2 = input('Input a Noun 2: ')
    adjective1_1 = input('Input a Adjective 1 (Feeling): ')
    adjective2_1 = input('Input a Adjective 2 (Feeling): ')
    color = input('Input a Color: ')
    animal = input('Input a Animal: ')
    num = input('Input a number: ')
    verb = input('Input a verb: ')
    verb2 = input('Input a verb 2: ')
    verb1_1 = input('Input a verb + ing: ')
    adverb = input('Input a Adverb + ly: ')
    silly_Word = input('Silly Word: ')

    print("============")
    print(f"This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun1}. I am so {adjective1_1} to {verb} in a tent. I am {adjective2_1} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb1_1}. Then we will {adverb} hike through the forest for {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {num} {silly_Word} stories and roast {noun2} around the campfire!!")


def story3():
    print("==== Story #3 ====")
    person_name = input('Person Name: ')
    measure_of_time = input('Measure of time: ')
    creature1 = input('Magical Creature 1: ')
    creature2 = input('Magical Creature 2: ')
    color1 = input('Input a Color: ')
    animal = input('Input a animal: ')
    adjective1 = input('Input a Adjective 1: ')
    adjective2 = input('Input a Adjective 2: ')
    adjective3 = input('Input a Adjective 3: ')
    adjective4 = input('Input a Adjective 4: ')
    adjective5 = input('Input a Adjective 5: ')
    noun1 = input('Input a Noun 1: ')
    noun2 = input('Input a Noun 2: ')
    noun3 = input('Input a Noun 3: ')
    noun4 = input('Input a Noun 4: ')
    noun5 = input('Input a Noun 5: ')
    verb1_1 = input('Input a verb + ing: ')
    room = ("Room in a House")
    place = input('Input a Place: ')

    print("============")
    print(f"Dear {person_name}, I am writing to you from a{adjective1} castle in an enchanted forest. I found myself here one day after going for a ride on a {color1} {animal}) in {place}. There are {adjective2} {creature1} and {adjective3} {creature2} here! In the {room} there is a pool full of {noun1}. I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. It feels as though I have lived here for {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verb1_1} on a {adjective5} {noun5}!!")


def create_story():
    stories = ("1", "2", "3")
    print("Enter template ID (1, 2 or 3)")
    command = input(stories)

    if command == "1":
        story1()
    elif command == "2":
        story2()
    elif command == "3":
        story3()
    else:
        print("Please, enter valid template ID")
    print("============")

create_story()
