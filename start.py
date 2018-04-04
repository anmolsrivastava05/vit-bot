import bot
import genericTasks
import json

def getInstructions(val):
    if(val==1):
        instructions = """\n\nWelcome to Interaction mode! I have been trained with all the information about VIT.
        You can ask me about schools, hostels, messes, campus, branches and other stuff. I would be happy to assist you!\n
        """
    else:
        instructions = """Welcome to tasks mode! I'm here to help you out with different tasks!
        You can ask me like:
        1. Remind me for quiz
        2. Am i debarred in any subject?
        3. How many days are there in exams?
        4. I need some motivation
        5. Do I have any morning classes?
        6. Show me all my reminders\n
        """
    return instructions

dataJSON = json.load(open('tasks.json'))
userName = dataJSON['user_name']
if userName=="":
    userName = raw_input("Hey there! Can I know your name please?")
    dataJSON['user_name'] = userName
    with open('tasks.json', 'w') as f:
        json.dump(dataJSON, f, indent=4)
        f.close()
print "\n\nHey " + dataJSON['user_name'] + ", I'm VITBOT, your personal assistant!\n"
print "I've two modes:\n1) INTERACTION MODE\n2) TASKS MODE\n"

ch = input("\nPlease choose the mode you want to switch to: ")
if(ch==1):
    print getInstructions(1)
    bot.startBot()
elif(ch==2):
    print getInstructions(2)
    genericTasks.runTasks()
else:
    print "\nSorry!! I cannot get you!"