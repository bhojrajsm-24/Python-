questions = [
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "b"],
    ["What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", "a"],
    ["How many days are there in a leap year?", "364", "365", "366", "367", "c"],
    ["Which animal is known as the King of the Jungle?", "Tiger", "Lion", "Elephant", "Leopard", "b"],
    ["Which is the largest ocean in the world?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", "b"],
    ["What is the national flower of India?", "Lotus", "Rose", "Sunflower", "Lily", "a"],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "c"],
    ["Which is the smallest continent?", "Asia", "Europe", "Australia", "Africa", "c"],
    ["Which device is used to measure temperature?", "Thermometer", "Barometer", "Anemometer", "Compass", "a"],
    ["Who invented the light bulb?", "Alexander Graham Bell", "Albert Einstein", "Thomas Edison", "Isaac Newton", "c"]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"question for RS. {levels[i]}")
    print(question[0])
    print(f"a.  {question[1]}           b.  {question[2]}")
    print(f"c.  {question[3]}              d.  {question[4]}")
    reply = (input("Enter your answer (a-d) :- "))
    if(reply == question[-1]):
        print(f"correct answer, you have won {levels[i]}")
        if(i == 4):
            money = 10000
        elif(1 == 9):
            money = 320000
    else:
        print("wrong answer!")