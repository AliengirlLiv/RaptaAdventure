
from firebase import firebase


firebase = firebase.FirebaseApplication('https://mariasadventure-b810c.firebaseio.com')
currMission = None
currMissionIndex = -1


def getCurrMission():
	currMissionIndex = firebase.get('/','missionIndex')
	currMission = firebase.get('/missionSegments', currMissionIndex)
	global currMission = currMission
	global currMissionIndex = currMissionIndex
	if currMission != None:
		print('')
		print("MISSION " + str(currMissionIndex) + ": " + currMission['title'])
		print('')
		print(currMission['story'])
		print("")
		print(currMission['mission'])
	else:
		print("Looks like you don't have any missions yet.  Don't worry, it won't be that way for long!  With Rapta, action's always around the corner.")


def help():
	print("AVAILABLE COMMANDS:")
	print('')
	print("help(): If you're here, presumably you already know what this one does.")
	print('')
	print("story(): Get the most recent segment of the story.")
	print('')
	print("mission(): Get the most recent challenge.")
	print('')
	print("submit(myAnswer): Submit your answer to the most recent challenge.")
	print("                  This answer must be in the right format (a string unless otherwise specified).")
	print("                  Unless specified, there should be no spaces, capitals, or punctuation")

	

def story():
	if currMission == None:
		print("Sorry, looks like you don't have any new story segments.")
	else:		
		print('')
		print(currMission['story'])
		print('')

def fullStory():
	allMissions = firebase.get('/', None)
	del allMissions['missionIndex']
	print('')
	for mission in allMissions.values():
		print(data['story'])
		print('')


def mission():
	if currMission == None:
		print("Sorry, looks like you don't have any new missions.")
	else:
		print('')
		print(currMission['mission'])
		print('')



def submit(submission):
	if str(submission).strip() == currMission['answer']:
		firebase.post('/missionIndex', currMissionIndex + 1)
		# Increment currMissionIndex
		print('You got it!  We are one step closer to defeating (SOMEONE')
		print("To get your next challenge, type 'mission()")
		# Get next mission
	else:
		print("Your solution isn't correct :(  Make sure your answer is right, and is in the reqested format.")
		print("Make sre there are no extra spaces, capitals, commas, etc.")



def main():
	print("***NOTE: type help() to see a list of available commands.")
	getCurrMission()

if __name__ == "__main__":
    main()


#     <script src="https://www.gstatic.com/firebasejs/3.5.2/firebase.js"></script>
# <script>
#   // Initialize Firebase
#   var config = {
#     apiKey: "AIzaSyDdeqwQHOuDuav76zcSmExDLbULCh6IuHc",
#     authDomain: "mariasadventure-b810c.firebaseapp.com",
#     databaseURL: "https://mariasadventure-b810c.firebaseio.com",
#     storageBucket: "mariasadventure-b810c.appspot.com",
#     messagingSenderId: "536560823779"
#   };
#   firebase.initializeApp(config);
# </script>