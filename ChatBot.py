from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

chatBot = ChatBot('ChatBot')

trainer = ChatterBotCorpusTrainer(chatBot)

trainer.train("chatterbot.corpus.english")

print("Hi , I am ChatBot")
while True:
    query = input(">>>")
    print(chatBot.get_response(Statement(text=query, search_text = query)))