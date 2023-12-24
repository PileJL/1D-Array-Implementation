#Disclaimer: This is a rushed project. That is why the overall construction's messy and you will see some redundant conditions and pambobong solutions haha, sorry kung masakit sa mata.
from array import *
from Final_Routes import *
import os
import random
import time

underline='\033[04m'
w = "\033[0;97;1m"
r = "\033[2;91;1m"
gry = "\033[37m"
green = '\033[32m'
reset = '\033[0m'
bold = "\033[1m"
yellow ='\033[93m'
italize = "\x1B[3m"

def getBatOrNot():
    while True:
        answer = input(f"\n{r}You're out of Bullets/Baseball Bat!{reset}".center(100)+f"\n {yellow}{italize}!{reset} Would you like to pick up a bat YES|NO? {r}").lower()
        if answer == "yes":
            return "yes"
        elif answer == "no":
            return "no"
        else: 
            print(f"{r}\nPlease enter either YES|NO:{reset}  ".center(100))

def getQuestion(desired_location):
    global cure_wrong_answers,answered_questions,obtained_letters,normal_incorrect_answers,answered_locations
    while True:
        if not obtained_letters:
            print(f"\n{r}Obtained letters : {reset}None")
        else:
            print(f"\n{r}Obtained letters:{reset}", "|".join(obtained_letters))
        questions = ["From what animal did the disease came from","The people who got bitten had a thrilling thirst to what","The scientist was experimenting the chicken for what reason", " ","Where did the Apocalypse started",
                     "What was the first symptom of the virus", " ","\nThe people who got bitten or killed came back to life as","\nWhere did the man first took the chicken"]
        answers = ['chicken', 'human flesh', 'unknown', " ", 'amusement park', 'cough', " ", "zombies", "home"]
        letters_to_be_obtained = [" O | N ", " R | I ", " E | E ", " ", " H | T ", " U | R ", " ", " S | C ", " | E"]
        if not desired_location in original_locations_withQuestions:
            print(f"\nThere's no designated question for this location.{reset}")
            return
        elif not desired_location in locations_that_still_haveQuestion:
            print(f"\nYou've already obtained the set of letters for this location.{reset}")
            return
        while True:
            answer = input(f"\n" + questions[desired_location - 1] +f"{reset}? {r}")
            print(reset)
            if answer.lower() == answers[desired_location - 1]:
                answered_questions += 1
                answered_locations.append(desired_location)
                locations_that_still_haveQuestion.remove(desired_location)
                obtained_letters.append(letters_to_be_obtained[desired_location - 1])
                print("\n" + f"{r}Correct Answer!\n{reset}The letters you earned are: {letters_to_be_obtained[desired_location - 1]}") if desired_location != 9 \
                    else print("\n" + f"{r}Correct answer!\n{reset}The letter you earned is: {letters_to_be_obtained[desired_location - 1]}")
                if answered_questions == 7:
                    print("\n" + f"{r}Way to go! You just have to guess the cure now!{reset}".center(100))
                    while True:
                        print(f"{r}\n\t\tUse all the clues to decode the scientist's secret message.{reset}")
                        print(f'{r}\nObtained letters : {reset} {"|".join(obtained_letters)}')
                        cure_guess = input(f"{r}\nEnter your guess: {reset}").lower()
                        if cure_guess == "there is no cure":
                            print(congrats)
                            return "congrats"
                        else:
                            print("Incorrect guess!".center(85), end="")
                            cure_wrong_answers += 1
                            if cure_wrong_answers==4:
                                print("\n"+f"One more incorrect answer before GAME OVER!".center(85))
                            if cure_wrong_answers == 5:
                                print(game_over)
                                return "game over"
                return
            else:
                normal_incorrect_answers += 1
                if normal_incorrect_answers != 5:
                    print("\n"+f"{r}Incorrect Answer :< {reset}".center(100))
                    if normal_incorrect_answers == 4: print(f"{r}One more incorrect answer before GAME OVER!{reset}\n".center(100))
                    while True:
                        try_again_answer = input(f"Would you like to try again? {r}").lower()
                        print(reset)
                        if try_again_answer == "yes":
                            break
                        elif try_again_answer == "no":
                            return
                        else:
                            print(f"{r}Please enter either YES|NO\n{reset}  ".center(100))
                else:
                    print(game_over)
                    return "game over"

def displayMap(current_location=None,desired_location=None):
    global baseballBat_lifespan,roads_with_killed_zombies,bullets,saver,answered_questions,initial_map,roads_distances,final_map,road1,road1,road3,road4,road5,road6,road7,road8,road9,road10,road11,road12, locations
    player_possible_positions = array("i", [303, 374, 1085, 1121, 1156, 1870, 2161, 1940])
    if not desired_location:
        user_random_posistion = random.choice(player_possible_positions)
        initial_map[user_random_posistion] = "🕵" 
    else:
        if answered_questions != 6:
            initial_map[initial_map.index("🕵")] = " "
            initial_map[player_possible_positions[desired_location - 1]] = "🕵"   
        roads_to_clear = get_route(roads_distances,current_location, desired_location, answered_questions) # ---------------------------------------singit ang possible routes, shortest, time of arrival, pagtanggal ng zombies sa road na nadaanan----------------------------------------------
        zombie_encountered = 0
        if roads_to_clear:
            for road in roads_to_clear: # check how many zombie encountered
                if not road in roads_with_killed_zombies:
                    zombie_encountered+=2
                    roads_with_killed_zombies.append(road) 
            for road_num1 in roads_to_clear: #clear travered roads
                for index in eval(f"road{road_num1}"):
                    if road_num1 in [3, 4, 8, 9]: initial_map[index+1] = " "
                    else: initial_map[index] = " "
            if len(bullets) >= zombie_encountered or len(baseballBat_lifespan)>= zombie_encountered: #check if bullets or bat are enough
                if len(baseballBat_lifespan)==0 and zombie_encountered!=0: 
                    del bullets[-zombie_encountered:]
                elif len(bullets)== 0 and zombie_encountered!=0: 
                    del baseballBat_lifespan[-zombie_encountered:]
            else:
                print(you_died)
                return "you died"
    if desired_location == 9: user_current_position = "[9] Cockfighting Arena 🏟️  " 
    else: user_current_position = locations[player_possible_positions.index(initial_map.index("🕵"))] # ----------------------------- user current loc
    if answered_questions != 6:  # display map------------------------------------------------------------------------------------------------------------------------ bullets or baseball lifespan
        print("".join(initial_map))
        if len(bullets)!=0:
            print(f"{r}Bullets: {yellow}{''.join(bullets)}{reset}")
        elif len(baseballBat_lifespan)!=0:
            print(f"{r}Baseball Bat Lifespan: {yellow}{italize}{''.join(baseballBat_lifespan)}{reset}")
        print("\n" + f"You're currently at the {user_current_position}\n".center(100))
    else:
        player_positions_finalMap = array("i", [273, 345, 1067, 1103, 1138, 1864, 2155, 1934, 310])
        final_map[final_map.index("🕵")] = " "
        final_map[player_positions_finalMap[desired_location - 1]] = "🕵"
        print("".join(final_map))
        print("\n" + f"{reset}You're currently at the {user_current_position}\n".center(100))
    locations_distances_maxLen = max([len(location_len) for location_len in locations_distances])
    print(f"{r}"+("     +"+"-"*((locations_distances_maxLen*2)-10)+"+").center(locations_distances_maxLen)+f"{reset}")
    counter1 = 1
    for counter in range(0,12,2): #table of contents----------------------------------
        print((f"     {locations_distances[counter].ljust(locations_distances_maxLen)} -"+ f"{str(roads_distances[counter])}m".center(6)+f"{r}|{reset}" +
         f"{locations_distances[counter1][14:].ljust(locations_distances_maxLen-13)} -"+ f"{str(roads_distances[counter1])}m".center(6)+f"{r}|{reset}").center(92))
        counter1+=2
    print(f"{r}"+("     +"+"-"*((locations_distances_maxLen*2)-10)+"+").center(locations_distances_maxLen)+f"{reset}")
    # questions----------------------------------------------------------------------------
    if desired_location:
        game_over_or_congrats = getQuestion(desired_location)
        if saver and answered_questions == 6:
            player_positions_finalMap = array("i", [273, 345, 1067, 1103, 1138, 1864, 2155, 1934, 310])
            final_map[player_positions_finalMap[desired_location - 1]] = "🕵"
            print("".join(final_map))
            print("\n"+f"You've been teleported back in time when the apocalypse is yet to start!{reset}".center(100-len(reset)))
            print(f"{r}          You're almost done gathering all clues!{reset}".center( 100))
            print("Go to the [9] Cockfighting Arena 🏟️   to gather them all!".center(100))
            print("\n" + f"{reset}You're currently at the {user_current_position}\n".center(100-len(reset)))
            saver = False
        if game_over_or_congrats == "game over":
            return "game over"
        elif game_over_or_congrats == "congrats":
            return "congrats"
        if len(bullets) ==0 and len(baseballBat_lifespan) ==0 : # check if wants to get bat
            get_bat = getBatOrNot()
            if get_bat == "yes":
                baseballBat_lifespan += list("!!!!")
                print(f"{r}\nBaseball Bat Lifespan: {yellow}{italize}{''.join(baseballBat_lifespan)}{reset}")
    if answered_questions == 6:
        print(f"{r}\nAvailable Locations:{reset}\n\n [9] Cockfighting Arena 🏟️")
        available_locations_asInt = array("i", [9, 0])
    else:
        available_locations = ['[1] Roller Coaster 🎢', "[2] Pirate Ship ⛴", "[3] Double Shot 🗼", "[4] Fountain ⛲","[5] Hammer Swing ⚒", "[6] Ferris Wheel 🎡", "[7] Entrance ⛩", "[8] Carousel 🎠"]
        available_locations_asInt = array("i", [i + 1 for i in range(len(available_locations)) if i != available_locations.index(user_current_position)]) + array("i", [available_locations.index(user_current_position) + 1])
        available_locations.remove(user_current_position)
        beautified_availableLocs = []
        for location in available_locations:
            if int(location[1]) in answered_locations:
                beautified_availableLocs.append(check+location[2:])
            else:
                beautified_availableLocs.append(location)
        print(f"{r}\nAvailable Locations:{reset}\n\n " + "\n ".join(beautified_availableLocs))
    return available_locations_asInt

def main():  # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    global traversed_locations
    available_and_current_locations = displayMap()
    current_location = available_and_current_locations[-1]
    if current_location in original_locations_withQuestions:
        while True:
            answer = input("\n"+f"{r}Your current location has a set of clues.{reset}".center(100)+f"\n\nWould you like to answer the question to get them YES|NO? {r}").lower()
            if answer == "yes":
                game_over = getQuestion(current_location)
                if game_over == "game over":
                    return
                break
            elif answer == "no": break
    traversed_locations.append(current_location)
    while True:
        try:
            desired_location = int(input(f"{underline}{r}\nWhere do you want to go{reset}"+f"{r}?{reset} "))
            if desired_location in available_and_current_locations[:-1] and desired_location != current_location:
                available_and_current_locations = displayMap(current_location,desired_location=desired_location)
                current_location = available_and_current_locations[-1]
                traversed_locations.append(desired_location)
                if available_and_current_locations in ["game over", "congrats", "you died"]:
                    return
            else:
                print("\nYou're already here.") if desired_location == current_location and current_location !=0 else print("\nThere's no such location.")
        except:
            print(f"\nPlease enter an integer based from the available locations.")

check = f"[{green}✓{reset}"
Title = ''' ▄▄▄       ██▓     ██▓        ▒█████    █████▒    █    ██   ██████     ▄▄▄       ██▀███  ▓█████     ▄▄▄       ███▄ ▄███▓ █    ██   ██████ ▓█████ ▓█████▄ 
▒████▄    ▓██▒    ▓██▒       ▒██▒  ██▒▓██   ▒     ██  ▓██▒▒██    ▒    ▒████▄    ▓██ ▒ ██▒▓█   ▀    ▒████▄    ▓██▒▀█▀ ██▒ ██  ▓██▒▒██    ▒ ▓█   ▀ ▒██▀ ██▌
▒██  ▀█▄  ▒██░    ▒██░       ▒██░  ██▒▒████ ░    ▓██  ▒██░░ ▓██▄      ▒██  ▀█▄  ▓██ ░▄█ ▒▒███      ▒██  ▀█▄  ▓██    ▓██░▓██  ▒██░░ ▓██▄   ▒███   ░██   █▌
░██▄▄▄▄██ ▒██░    ▒██░       ▒██   ██░░▓█▒  ░    ▓▓█  ░██░  ▒   ██▒   ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄    ░██▄▄▄▄██ ▒██    ▒██ ▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ░▓█▄   ▌
 ▓█   ▓██▒░██████▒░██████▒   ░ ████▓▒░░▒█░       ▒▒█████▓ ▒██████▒▒    ▓█   ▓██▒░██▓ ▒██▒░▒████▒    ▓█   ▓██▒▒██▒   ░██▒▒▒█████▓ ▒██████▒▒░▒████▒░▒████▓ 
 ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░   ░ ▒░▒░▒░  ▒ ░       ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░    ▒▒   ▓▒█░░ ▒░   ░  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▒▓  ▒ 
  ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░     ░ ▒ ▒░  ░         ░░▒░ ░ ░ ░ ░▒  ░ ░     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░     ▒   ▒▒ ░░  ░      ░░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░ ░ ▒  ▒ 
  ░   ▒     ░ ░     ░ ░      ░ ░ ░ ▒   ░ ░        ░░░ ░ ░ ░  ░  ░       ░   ▒     ░░   ░    ░        ░   ▒   ░      ░    ░░░ ░ ░ ░  ░  ░     ░    ░ ░  ░ 
      ░  ░    ░  ░    ░  ░       ░ ░                ░           ░           ░  ░   ░        ░  ░         ░  ░       ░      ░           ░     ░  ░   ░\n'''

# Timer
def timer():
    time.sleep(.35)

# Colors
c = ['\033[0;31m', '\033[1;91m', '\033[0;37m']
print(f'\n{c[0]}{Title}')

# Objective
while True:
    Continue = input(f'\n                                                             Press ENTER key for MECHANICS ')
    if not Continue:
        break
    else:
        continue
print(f'\n\t\t{c[2]}1. Be careful and attentive to survive and not get killed by the zombies.\n')
timer()
print(f'\t\t2. You will obtain a map of the amusement park to choose your target location.\n')
timer()
print(f'\t\t3. The starting position of the player and zombies inside the amusement park will be random each time.\n')
timer()
print(f'\t\t4. You will have a pistol as a primary weapon (life span of four), then you must get the baseball bat (lifespan of four) \n\t\t   for security and extra self-defense.\n')
timer()
print(f'\t\t5. There will be nine locations and, specifically, seven rides that you need to visit to gain a set of letters per ride, \n\t\t   namely: Roller Coaster (1), Pirate Ship (2), Double Shot (3), Hammer Swing (5), Ferris Wheel (6), Carousel [8], and \n\t\t   Cockfighting Arena (9).\n')
timer()
print(f"\t\t6. To gain the set of letters, you must answer the designated questions (four incorrect answers) per ride concerning the \n\t\t   game's backstory.\n")
timer()
print(f'\t\t7. After getting all clues, you must decode the letters to find the hidden mystery of the cure (four incorrect answers).\n')
timer()

# Backstory
while True:
    Backstory = input(
        f'\n{c[0]}                                                           Press ENTER key to view BACKSTORY ')
    if not Backstory:
        break
    else:
        exit
print(
    f'\n{c[2]}\t\t   100 years ago, a scientist was experimenting with a chicken for unknown reasons. Unfortunately, the chicken escaped.\n')
timer()
print(f'\t\tMeanwhile, a man fond of cockfighting saw the chicken and took it home. He entered a cockfighting match and won. But then,\n')
timer()
print(f'\t\tthe chicken suddenly attacked a bystander. A day later, the chicken died. However, the person bitten started to feel sick.\n')
timer()
print(f'\t\tThe person started coughing uncontrollably and passed it down to his family and friends. Everyone who existed at that time\n')
timer()
print(f'\t\tpaid no mind to the sudden increase in coughing every day. Nevertheless, the coughing worsened to reddish eyes, excessive\n')
timer()
print(f'\t\thair loss, cracked skin, and a thrilling thirst for human flesh just a day later. Eventually, the people bitten or killed\n')
timer()
print(f"\t\thorrifyingly came back to life as mindless zombies. Due to the virus' mystery, the government failed to find the cure and\n")
timer()
print(f'\t\topted to build walls in a town far from the cities. Centuries later, when humanity is on the brink of extinction, a single\n')
timer()
print(f"\t\tdetective arrives at the place where the apocalypse started. An abandoned amusement park where the cockfighting took place.\n")
timer()
print(f"\t\tSurprisingly, he found a century-old letter left by the chicken's scientist. But then, the scientist only wrote one thing: ")
timer()
timer()
print(f'\n{c[1]}\t\tRIDE ALL THOSE ATTRACTIONS AND SURVIVE\n');
timer()

# Start
while True:
    Start = input(f'\n{c[0]}                                                              Press ENTER key to START ')
    if not Start:
        break
    else:
        continue
os.system('cls') # remove intro from console 

locations = ["[1] Roller Coaster 🎢", "[2] Pirate Ship ⛴", "[3] Double Shot 🗼", "[4] Fountain ⛲","[5] Hammer Swing ⚒", "[6] Ferris Wheel 🎡", "[7] Entrance ⛩", "[8] Carousel 🎠", "[9] Cockfighting Arena 🏟️"]
traversed_locations = array("i")
baseballBat_lifespan = list("")
roads_with_killed_zombies = array("i")
bullets = list("iiii")
locations_distances = [f"{r}|{reset}   Roller Coaster → ???????", f"{r}|{reset}   ??????? → Pirate Ship", f"{r}|{reset}   Roller Coaster → Double Shot",f"{r}|{reset}   ??????? → Fountain", f"{r}|{reset}   Pirate Ship → Hammer Swing", 
f"{r}|{reset}   Double Shot → Fountain",f"{r}|{reset}   Fountain → Hammer Swing", f"{r}|{reset}   Double Shot → Ferris Wheel",f"{r}|{reset}   Fountain → Entrance", f"{r}|{reset}   Hammer Swing → Carousel", f"{r}|{reset}   Ferris Wheel → Entrance",
f"{r}|{reset}   Entrance → Carousel"]
saver = True
you_died= f"""{c[0]}
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
 ░ ░                           ░                  ░      {reset}"""
congrats = (f"""\n\n{green} ▄████▄   ▒█████   ███▄    █   ▄████  ██▀███   ▄▄▄     ▄▄▄█████▓ █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █   ██████ 
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ 
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░▒██████▒▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░
░        ░ ░ ░ ▒     ░   ░ ░ ░ ░   ░   ░░   ░   ░   ▒    ░       ░░░ ░ ░   ░ ░    ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ ░  ░  ░  
░ ░          ░ ░           ░       ░    ░           ░  ░           ░         ░  ░     ░  ░         ░      ░ ░           ░       ░  
░                                                                                                                                  
{reset}""")
game_over = f"""{c[0]}
          ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███   ▐██▌ 
         ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒ ▐██▌ 
        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒ ▐██▌ 
        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄   ▓██▒ 
        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒ ▒▄▄  
         ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░ ░▀▀▒ 
          ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ░  ░ 
        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░     ░ 
              ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░      ░ {reset}"""
normal_incorrect_answers = 0
cure_wrong_answers = 0
answered_locations = []
obtained_letters = []
answered_questions = 0
original_locations_withQuestions = array("i", [1, 2, 3, 5, 6, 8, 9])
locations_that_still_haveQuestion = array("i", [1, 2, 3, 5, 6, 8, 9])
initial_map = list(f"""{w}\n                              
                            🎪 {r}AMUSEMENT {w}PARK {r} - Initial {w}Map {r}🎪            
{r}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{w}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━            
{w}         🎢                                                                     ⛴                          
{r} 【ROLLER COASTER】{w}🢀{gry}▒▒▒▒▒▒▒▒▒▒▒▒{w}🢀{r}【     ???????????     】{w}🢂{gry}▒▒▒▒▒▒▒▒▒▒▒{w}🢂{r}【PIRATE SHIP】
{w}         ↕↕                                  ↕↕                                 ↕↕                         
{gry}         ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒ 
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒             
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒ 
{gry}         ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒                          
{w}         ↕↕                                  ↕↕                                 ↕↕                         
{r}  🗼 DOUBLE SHOT 🗼 {w}⟺  {gry}▒▒▒▒▒▒▒▒▒▒▒▒{w} ⟺  {r}⛲ FOUNTAIN ⛲ {w}⟺  {gry}▒▒▒▒▒▒▒▒▒▒▒▒▒{w} ⟺  {r}⚒ HAMMER SWING ⚒
{w}         ↕↕                                  ↕↕                                 ↕↕                         
{gry}         ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒ 
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒             
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒ 
{gry}         ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒                          
{w}         🎡                                  ↕↕                                 🎠                         
{r} 【 FERRIS WHEEL 】{w}🢀{gry}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {w}🢀           🢂{gry} ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{w}🢂{r}【 CAROUSEL 】    
                                         {r}⛩       ⛩
                                        {r}【{w}ENTRANCE{r}】                                          
{w}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━            {reset}""")
final_map = list(f"""{w}\n                              🎪 {r}AMUSEMENT {w}PARK {r} - Final {w}Map {r}🎪            
{r}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{w}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━            
{r}         🎢                                  🏟️                                 ⛴                          
{w} 【ROLLER COASTER】{r}🢀{gry}▒▒▒▒▒▒▒▒▒▒▒▒{r}🢀{w}【 COCKFIGHTING ARENA 】{r}🢂{gry}▒▒▒▒▒▒▒▒▒▒▒▒{r}🢂{w}【PIRATE SHIP】
{r}         ↕↕                                  ↕↕                                 ↕↕                         
{gry}         ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒             
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒             
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒
{gry}         ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒                          
{r}         ↕↕                                  ↕↕                                 ↕↕                         
{r}  🗼 DOUBLE SHOT 🗼 {w}⟺  {gry}▒▒▒▒▒▒▒▒▒▒▒▒{w} ⟺  {r}⛲ FOUNTAIN ⛲ {w}⟺  {gry}▒▒▒▒▒▒▒▒▒▒▒▒▒{w} ⟺  {r}⚒ HAMMER SWING ⚒
{r}         ↕↕                                  ↕↕                                 ↕↕                         
{gry}         ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏    ▒▒             
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒             
{gry}         ▒▒    ▕                        ▏    ▒▒    ▕                       ▏    ▒▒
{gry}         ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏    ▒▒                          
{r}         🎡                                  ↕↕                                  🎠                         
{w} 【 FERRIS WHEEL 】{r}🢀{gry}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ {r}🢀           🢂{gry} ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{r}🢂{w}【 CAROUSEL 】    
                                         {w}⛩       ⛩
                                        {w}【{r}ENTRANCE{w}】                                          
{w}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━            {reset}""")
#map's road indexes
road1 = array("i", [i for i in range(313, 324)])
road2 = array("i", [i for i in range(354, 364)])
road3 = array("i", [682, 771, 872, 961])
road4 = array("i", [718, 807, 908, 997])
road5 = array("i", [758, 847, 948, 1037])
road6 = array("i", [i for i in range(1095, 1107)])
road7 = array("i", [i for i in range(1130, 1141)])
road8 = array("i", [1469, 1558, 1659, 1748])
road9 = array("i", [1505, 1594, 1695, 1784])
road10 = array("i", [1545, 1634, 1735, 1824])
road11 = array("i", [i for i in range(1880, 1896)])
road12 = array("i", [i for i in range(1914, 1931)])
for road_num in range(1, 13):
    road = eval(f"road{str(road_num)}[1:]")
    zombie_position1 = random.choice(road)
    if road_num in [3, 4, 8, 9]:
        initial_map[zombie_position1 + 1] = f"{bold}{green}Z{reset}"
        del road[road.index(zombie_position1)]
        initial_map[random.choice(road) + 1] = f"{bold}{green}Z{reset}"
    else:
        initial_map[zombie_position1] = f"{bold}{green}Z{reset}"
        del road[road.index(zombie_position1) - 1:road.index(zombie_position1) + 1]
        initial_map[random.choice(road)] = f"{bold}{green}Z{reset}"

roads_distances = array("i",[random.choice([i for i in range(10, 101)]) for i in range(12)])
if __name__ == "__main__":
    main()
