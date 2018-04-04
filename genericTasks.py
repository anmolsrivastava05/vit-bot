import sqlite3
from fuzzywuzzy import fuzz # String matching algorithms used.
from fuzzywuzzy import process
import json
#Import Quotes from quotes module (self developed module)
from quotes import quotes
import random

#implementing timed arguments using timeit

import timeit


# Pre Set tasks :

tasks = [
    'remind me for quiz',
    'Am i debarred in any subject?',
    'How many days are there in exams?',
    'I need some motivation',
    'Do I have any morning classes?',
    'show me all my reminders'
]

#Days mapping for fetching morning classes with Monday on index 0

days = [
    "mon", "tue", "wed", "thu", "fri", "sat", "sun"
]
def runTasks():
    CURRENT_TIME_IN_SECONDS = timeit.default_timer()
# User inputs on tasks and follow ups on the basis of indexes
    exitValue = 0
    while not exitValue:
        if(timeit.default_timer()-CURRENT_TIME_IN_SECONDS<10):
            pass
        else:
            print "Heyyy! Are you there???"
        userInputString = raw_input("\nHow may I help you?\n")
        if userInputString.lower() != "bye":
            fuzzScores = []
            for i in tasks:
                fuzzScores.append(fuzz.ratio(i, userInputString))

            print "Fuzz Scores sorted"

            # Sort tasks from best matching and relevant task Instrutction
            print "Best task matched:::::" + tasks[fuzzScores.index(max(fuzzScores))]
            print "\n"
            print "Best fuzz score value: " + str(max(fuzzScores)) + "\n\n"
            choice = fuzzScores.index(max(fuzzScores))
            if(max(fuzzScores)<20):
                choice = -1
            # Choice based responses:

            if(choice==0):
                print "\nSure! Can you please tell the date of the quiz? I'll set a reminder. (dd/mm/yy)\n"
                dateOfReminder = raw_input("You:")
                taskString = "You have a quiz on " + dateOfReminder
                tasksJSON = json.load(open('tasks.json'))
                tasksJSON['tasks'].append(taskString)
                with open('tasks.json', 'w') as f:
                    json.dump(tasksJSON, f)
                f.close()
                print "\n I have stored the date! All the best for the quiz. \n"

            elif choice==1:
                tasksJSON = json.load(open('tasks.json'))
                debarredSubjects = tasksJSON['debarred']
                if(len(debarredSubjects)):
                    print "\nYou are debarred in:\n"
                    for i in debarredSubjects:
                        print i
                else:
                    print "\nHurrayyyy! You're not debarred in any of the subjects!"

            elif choice==2:
                tasksJSON = json.load(open('tasks.json'))
                examDays = tasksJSON['days_remaining']
                if examDays>0:
                    print "You have " + str(examDays) + " days left in your exams!!"
                elif examDays==0:
                    print "You had an exam today! How was it?"
                else:
                    print "There are no upcoming exams! Enjoy!"

            elif choice==3:
                randomQuote = quotes[random.randint(0,len(quotes)-1)]
                print "\nToday's quote of the day:\n" + randomQuote

            elif choice==4:
                dayIndex = -1
                day = raw_input("Please enter day (first 3 letters -> mon for Monday)\n")
                for i in days:
                    if day.lower() == i:
                        dayIndex = days.index(i)
                        break
                tasksJSON = json.load(open('tasks.json'))
                classSchedule = tasksJSON['morning_classes']
                if(classSchedule[dayIndex]):
                    print "You have a morning class on " + day + " at " + str(classSchedule[dayIndex]) + "AM"
                else:
                    print "No morning classes on " + day + "!!!"

            elif choice ==5:
                tasksJSON = json.load(open('tasks.json'))
                reminders = tasksJSON['tasks']
                print "\nYour added reminders:\n=================================\n"
                for reminder in reminders:
                    print u"\u2022  " + reminder
                print "\n=================================\n"
            elif choice == -1:
                print "Sorry! I didn't get it! :( \n"
            CURRENT_TIME_IN_SECONDS = timeit.default_timer()
            
        else:
            exitValue = 1
            print "\n Byeeee! I'll miss you. Have a great time! :)"
