from chatterbot import ChatBot
#A custom trainer module to train the Bot according to the VIT needs.
import customTrainer
chatbot = ChatBot(
    'VIT BOT',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

#Name of the Chat Bot

name = chatbot.name

from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Training chatbot")
chatterbot.set_trainer(ListTrainer)

def startBot():
	question = ''
	# Get a response to an input statement
	while(question.lower()!="bye"):
		#Ask a question
		question = raw_input('You: ')
		response = chatbot.get_response(question)
		'''
		Print the response based upon the training
		'''
		print name + ': ' + str(response)