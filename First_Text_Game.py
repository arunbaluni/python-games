print("Welcome to my First Game")

class MyFirstGame():
	def __init__(self):
		self.name = None
		self.age = None
		self.health = 10
	def setName(self):
		self.name = input("What is your name? \n=>")

	def getName(self):
		return self.name

	def setAge(self):
		self.age = int(input("What is your age?\n=>"))

	def getAge(self):
		return self.age

	def quiz(self):
		answer = input("Which Monument in India comes under wonders of world? Red Fort/Qutub Minar/India Gate/Taj Mahal\n =>").lower()

		if(answer == "taj mahal"):
			self.health += 5
			print("Your health is increased by 5 to ", self.health)
		else:
			self.health -= 5
			print("You lost the quiz and your health is decreased by 5 to ", self.health)


	def playGame(self):
		if(self.age >= 18):
			print("You are old enough to play this game")

			interested_in_playing = input("Are you interested in playing this game? Enter Yes or yes to play...\n=>").lower()

			if(interested_in_playing == "yes"):
				print("You are playing with ", self.health, "health")
				print("######################################")
				print("\nLets start playing the game...")

				left_or_right = input("Your first choice... Want to go Left or Right (Type left or right)?\n =>").lower()
				if(left_or_right == "left"):
					while(self.health > 0):
						print("Nice... you followed correct path and reached the river")
						swim_across_or_goaround = input("Do you swim across or go around (Type your choice as either 'across' or 'around') \n =>")
						if(swim_across_or_goaround == "across"):
							print("You went around and reached the other side safely and won the game!!")
							return
						elif(swim_across_or_goaround == "around"):
							print("You are bitten by snake and lost 5 health")
							self.health = self.health - 5
							print("Play quiz to improve your health to continue the game.")
							self.quiz()

						else:
							print("You lost!!")
							return

				elif(left_or_right == "right"):
					print("Bummer...you fell and lost the game")
					return
				else:
					print("You typed wrong option.. You have to choose between left or right only.. Restart the game")
					return
				if(self.health == 0):
					print("No health left.. You have lost the game")
					return

			else:
				print("Sorry to see you go without playing...")


		else:
			print("You should be 18 years to play this game")
			return


if __name__ == "__main__":
	firstGame = MyFirstGame()
	firstGame.setName()
	firstGame.setAge()

	print("Your name is", firstGame.getName(), "and age is ", firstGame.getAge())

	firstGame.playGame()