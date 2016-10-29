
from firebase import firebase


firebase = firebase.FirebaseApplication('https://mariasadventure-b810c.firebaseio.com')
currMission = None
currMissionIndex = -1
STORY_INDEX = 2


def getCurrMission():
	global currMissionIndex
	global currMission
	currMissionIndex = firebase.get('/','missionIndex')
	currMission = firebase.get('/missionSegments', currMissionIndex)
	if currMission != None:
		print('')
		print("MISSION " + str(currMissionIndex) + ": " + currMission['title'])
		print('')
		print(currMission['story'])
		print("")
		print(currMission['mission'])
	else:
		print('')
		print("Looks like you don't have any new missions yet.  Don't worry, it won't be that way for long!  With Rapta, action's always around the corner.")


def help():
	print("AVAILABLE COMMANDS:")
	print('')
	print("help(): If you're here, presumably you already know what this one does.")
	print('')
	print("story(): Get the most recent segment of the story.")
	print('')
	print("fullStory(): Print all story segments.")
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



#TODO:
	# Fix fullStory()
	# Make sure the level passing oworks fine
	# Make print statements sound better
	# Actually write story
	# Comment code
	# (If time) add Easter Egg

	# Time frame: 1 hr


#Got to be a better way to do this than get ALL of them
# In normal firebase, you can shoose a limit on how many
def fullStory():
	allMissions = firebase.get('/', None)
	del allMissions['missionIndex']
	print('')
	for mission in allMissions.values():
		mission = mission[0]
		if mission.
		print(mission['story'])
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
		# Increment currMissionIndex
		firebase.post('/missionIndex', currMissionIndex + 1)
		print('')
		print('You got it!  We are one step closer to defeating (SOMEONE')
		# Get next mission
		getCurrMission()
	else:
		print("Your solution isn't correct :(")
		print(" Make sure your answer is right and in the reqested format.")



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