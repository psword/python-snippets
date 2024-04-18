import random

name = "Bob"
question = "Why?"
answer = random.randint(1,10)



if name == "":
  print("Question:", question)
else:
  print(name, "asks:", question)

if question == "":
  print("There's no question")
else:
  if answer == 1:
      answer = "Yes - definitely"
  elif answer == 2:
      answer = "It is decidedly so"
  elif answer == 3:
      answer = "Without a doubt"
  elif answer == 4:
      answer = "Reply hazy, try again"
  elif answer == 5:
      answer = "Ask again later"
  elif answer == 6:
      answer = "Better not tell you now"
  elif answer == 7:
      answer = "My sources say no"
  elif answer == 8:
      answer = "Outlook not so good"
  elif answer == 9:
      answer = "Very doubtful"
  elif answer == 10:
      answer = "Too hard a question to answer"
  else:
      answer = "Error"

  print("Magic answer:", answer)