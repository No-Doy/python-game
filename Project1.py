#Project #1
#Brian Alfano; ID# 101987527
#TA: Halley Profita
print ("Hello World, Welcome To My Game Called 'The Warning'!")
print("")

q1 = input("Do You Enjoy Computer Games?(yes/no):")
if q1 == "yes" or q1 == "Yes" or q1 == "y" or q1 == "Y":
	print("Cool, Then Let Us Begin!")
else:
	print("Well You'll love this one!")
print("")

print("The Games Main Feature Is You! What Is Your Name?")
class gamer1:
	def __init__(self, first):
		
		self.firstName = first
def main():
	f = input("Enter Your First Name:")
	theUser = gamer1(f)
	print("Good morning", theUser.firstName,"." ,"It's about 5:46am and the phone rings.")
	print("")
	
	q2 = input("Do you answer?(yes/no):")
	while q2 != 'yes':
			print("The telephone keeps ringing *ring-ring*.")
			q2 = input("Do you answer?(yes/no):")
	if q2 == "yes":
		print("")
		print(theUser.firstName,"says,'Yo, Who's calling?'")
		
	
	userName = f
	return userName
userName = main()
print("")
print("Sup",userName, "? It's Pop from the Barber Shop.")
print("")
print("I Got to Warn You",userName,". Your Life's in Danger By The Street Rats You Use to Roll With!")
print("")
q3 = input("Do you want Pop to explain more, or Do You Want to Begin Your Attack?(yes/no):")
print("")
if q3 == "yes":
	print("After All The Fame and Fortune",userName,", You Attracked Haters Who Want To See Your Lime Light Vanish!")
print("")
print("Your haters Will Be Coming",userName,"And You Can Chose Your Path.")
print("")

def paths(bothpaths):
	answer = path
	return answer
def main():	
	bothpaths = input("Enter A or B:")
	myList = ["You're Going On This War Path Yourself. It's Time To Pick Up Materials.", "You Have Choosen To Meet With Pop And He Has Some Secret Information That Will Help Your Attack.", "Pop's Intell Suggests You Buy A Ray-Gun Because It's the Ultimate Defense Against A Hater.", "Buy Ray-Gun Dummy!"]
	#while bothpaths != "A" or bothpaths != "B":
		#bothpaths = input("Enter A or B:")
	while bothpaths != "A" or bothpaths != "B":
		
		if bothpaths == "A":
			print(myList[0])
			break
		elif bothpaths == "B":
			print(myList[1], myList[2])
			break
		bothpaths = input("Enter A or B:")
		
		
	
main()	

def material(PathQuestion):
	chose = survival
def main():
	PathQuestion = input("Purchase A Ray-Gun or Harpoon?(Ray-Gun/Harpoon):")
	while PathQuestion != "Ray-Gun" or PathQuestion != "Harpoon":
		if PathQuestion == "Ray-Gun":
			Mon = 100000000
			print("This Will Come In Handy!It Cost You $",Mon,".")
			break
		elif PathQuestion == "Harpoon":
			LitMon = 50
			print("Well, Hope A Harpoon Works out For You",userName,". It Cost you $",LitMon,".")
			break 
		PathQuestion = input("Purchase A Ray-Gun or Harpoon?(Ray-Gun/Harpoon):")	
	Weapon = PathQuestion
	return Weapon
Weapon = main()
print("")
class materials:
	def __init__(self, shelter, timeofDay):
		self.shelter1 = shelter
		self.Day = timeofDay
def main():
	s = input("Do You Want The Haters To Attack At Your Mansion or At Your Beach Front House?(Mansion/Beach House):")
	while s != "Mansion" or s != "Beach House":
		if s == "Mansion":
			print("")
			break
		elif s == "Beach House":
			print("")
			break
		s = input("Do You Want The Haters To Attack At Your Mansion or At Your Beach Front House?(Mansion/Beach House):")

	t = input("Time of Day Is Important. Is the Attack Going Down At Night, Afternoon, or Morning?(Night/Afternoon/Morning):")
	while t != "Night" or t != "Afternoon" or t != "Morning":
		if t == "Night":
			print("")
			break
		elif t == "Afternoon":
			print("")
			break
		elif t == "Morning":
			print("")
			break
		t = input("Time of Day Is Important. Is the Attack Going Down At Night, Afternoon, or Morning?(Night/Afternoon/Morning):")

	userSurvival = materials(s , t)
	
	print("You Will Be At Your", userSurvival.shelter1, " During The", userSurvival.Day,"When Haters Come For You.")
	shelterPick = s
	timePick = t
	return shelterPick, timePick
	
shelterPick, timePick = main()

def conclusion(userName, Weapon, shelterPick, timePick):
	
	sentence = s1
	return sentence
	
def main():
	print("")
	print("It Is Time To Know How The Attack Went Down!")
	print("")
	x = userName
	y = Weapon
	z = shelterPick
	q = timePick
	MorMon = 200000000
	NoMon = 40000000000
	if Weapon == "Ray-Gun" and shelterPick == "Mansion" and timePick == "Night":
		print(x,"Is Always one step ahead of his enimies. On this",q,"at his",z,",", x,"Get's 15 Head Shots With His",y,". Don't Hate The Player Hate The Game. Earned Payment of $",MorMon,".")
	elif Weapon == "Ray-Gun" and shelterPick == "Mansion" and timePick == "Morning":
		print( x,"'s Enimies Are Smart and know that",x,"is sleepy in the morning. But Still in His",z,"the Haters are no match and fall to his",y,". A Harpoon Would Have Never Stopped Them.")
	elif Weapon == "Ray-Gun" and shelterPick == "Mansion" and timePick == "Afternoon":
		print(x,"Is Always one step ahead of his enimies. On this",q,"at his",z,",", x,"Get's 10 Head Shots With His",y,". Don't Hate The Player Hate The Game. Earned Payment of $",MorMon,".")
	elif Weapon == "Ray-Gun" and shelterPick == "Beach House" and timePick == "Morning":
		print(x,"Is Always one step ahead of his enimies. On this",q,"at his",z,",", x,"Get's 15 Head Shots With His",y,", and Then Goes Surfing. Don't Hate The Player Hate The Game. Earned Payment of $",MorMon,".")
	elif Weapon == "Ray-Gun" and shelterPick == "Beach House" and timePick == "Afternoon":
		print(x,"Is Always one step ahead of his enimies. On this",q,"at his",z,",", x,"Get's 10 Head Shots With His",y,", and Then Tans On The Beach. Don't Hate The Player Hate The Game. Earned Payment of $",MorMon,".")
	elif Weapon == "Ray-Gun" and shelterPick == "Beach House" and timePick == "Night":
		print(x,"Is Always one step ahead of his enimies. On this",q,"at his",z,",", x,"Get's 14 Head Shots With His",y,", and just goes back to sleep. Don't Hate The Player Hate The Game.")
	else:
		print("")
	if Weapon == "Harpoon" and shelterPick == "Mansion" and timePick == "Night":
		print("The",y,"Was Not a Smart Choice, but at least your",z,"was strong enough to protect you from the haters. They couldn't see you at",q,"and you survived the attack!")
	elif Weapon == "Harpoon" and shelterPick == "Mansion" and timePick == "Afternoon":
		print("The",y,"Was Not a Smart Choice, but at least your",z,"was strong enough to protect you from the haters. You were Shot by a Stray Bullette and you still survived the", q, "attack!")
	elif Weapon == "Harpoon" and shelterPick == "Mansion" and timePick == "Morning":
		print("The Enimies Are Smart and know that",x,"is sleepy in the morning and only has a ",y,", so the Haters Attack you in your",z," with Ray-Guns during the",q,", and now",x,"is Dead. YOU LOSE! Your Life Savings of $",NoMon,"was over taken." )
	elif Weapon == "Harpoon" and shelterPick == "Beach House" and timePick == "Night":
		print("Having A", y, "At A",z,"Is smart Because There is So Much Ammo.",x,"has trouble hitting his Haters In the",q," but the Haters Retreat and You live anther Day To Die.")
	elif Weapon == "Harpoon" and shelterPick == "Beach House" and timePick == "Afternoon":
		print("Having A", y, "At A",z,"Is smart Because There is So Much Ammo.",x,"is in a constant Fire Exchange During The",q," but the Haters Retreat and You live anther Day To Die.")
	elif Weapon == "Harpoon" and shelterPick == "Beach House" and timePick == "Morning":
		print("The Enimies Are Smart and know that",x,"is sleepy in the morning and only has a ",y,", so the Haters Attack you with Ray-Guns in the",q,". and",x,"is Dead. YOU LOSE! Your Life Savings of $",NoMon,"was over taken.")
	print("GAME-OVER, THANKS FOR PLAYING")

main()

