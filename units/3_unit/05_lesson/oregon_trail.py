import random

def should_decrease_health(player_data):
	if player_data[6] < 2:
		random_day = random.randint(0, 30)
		if random_day < 2:
			return True
	return False

# updates the day
def add_day(player_data):
	MONTHS_31_DAYS = [3, 5, 7, 8, 10, 12]
	if should_decrease_health(player_data):
		player_data[1] -= 1
	if player_data[4] < 31:
		player_data[4] += 1
	elif player_data[4] == 30 and player_data[5] in MONTHS_31_DAYS:
		player_data[4] += 1
	else:
		player_data[5] += 1
		player_data[4] = 1
	player_data[4] += 1
	player_data[2] -= 5

# PROVIDE THIS TO STUDENTS
def update_days(low_range, high_range, player_data):
	days = random.randint(low_range, high_range)
	for i in range(0, days):
		add_day(player_data)

# moves the player 30-60 miles and takes 3-7 days
def travel(player_data):
	miles_traveled = random.randint(30, 61)
	player_data[3] -= miles_traveled
	update_days(3, 7, player_data)

# increase health 1 level and takes 2-5 days
def rest(player_data):
	if player_data[1] < 5:
		player_data[1] += 1
	update_days(2, 5, player_data)

# adds 100lbs of food and takes 2-5 days
def hunt(player_data):
	player_data[2] += 100
	update_days(2, 5, player_data)

# displays status
def display_status(player_data):
	print("Current Health: " + str(player_data[1]))
	print("Food: " +  str(player_data[2]) + "lbs")
	print("Distance Traveled: " + str(2000-player_data[3]) + "miles")
	print("Day is (Month/Day): " + str(player_data[5]) + "/" + str(player_data[4]))

# displays commands
def display_help():
	print("Commands are travel, rest, hunt, status, help, and quit")

# ends game before next turn
def quit_game(player_data):
	player_data[0] = True

# check if the game is over
def is_game_over(player_data):
	if player_data[0]:
		return True
	if (player_data[4] == 31 and player_data[5] == 12) or player_data[5] > 12:
		print("It is Dec. 31st and you are not in Oregon.")
		player_data[0] = True
		return True
	if player_data[1] < 1:
		print("You're health detiorated, and you died :(")
		player_data[0] = True
		return True
	if player_data[2] < 1:
		print("You ran out of food and starved")
		player_data[0] = True
		return True
	if player_data[3] < 1:
		print("You MADE IT")
		player_data[0] = True
		return True
	return False

# parse and act upon input
def process_user_input(user_input, player_data):
	if user_input == "travel":
		travel(player_data)
	elif user_input == "rest":
		rest(player_data)
	elif user_input == "hunt":
		hunt(player_data)
	elif user_input == "status":
		display_status(player_data)
	elif user_input == "help":
		display_help()
	elif user_input == "quit":
		quit_game(player_data)
	else:
		print("Not Correct Input.")

def game_loop():
	GAME_OVER = False
	PLAYER_HEALTH = 5
	PLAYER_FOOD_POUNDS = 500
	MILES_TO_GO = 2000
	CURRENT_DAY = 1
	CURRENT_MONTH = 3
	HEALTH_DECREASES_THIS_MONTH = 0

	player_data = [GAME_OVER, PLAYER_HEALTH, PLAYER_FOOD_POUNDS, MILES_TO_GO, CURRENT_DAY, CURRENT_MONTH, HEALTH_DECREASES_THIS_MONTH]

	while not is_game_over(player_data):
		user_input = input("What is your choice? ")
		process_user_input(user_input, player_data)


if __name__ == "__main__":
	game_loop()
