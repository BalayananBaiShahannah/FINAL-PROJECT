import random

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the only US state starting with the letter F?", "answer": "Florida"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "What is the largest country in the world (by land area)?", "answer": "Russia"},
    {"question": "Which ocean is located between Europe and North America?", "answer": "Atlantic Ocean"},
    {"question": "Which country is Budapest the capital of?", "answer": "Hungary"},
    {"question": "In which country can you find the Statue of Liberty?", "answer": "United States of America"},
    {"question": "In which lake can you find Nessie?", "answer": "Loch Ness, Scotland"},
    {"question": "Which country is Manila the capital of?", "answer": "Philippines"},
    {"question": "What is the largest natural rainforest in the world?", "answer": "Amazon Forest"},
    {"question": "In which country can you find the island of Bali?", "answer": "Indonesia"},
    {"question": "What is the highest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the capital city of South Korea?", "answer": "Seoul"},
    {"question": "In which country can you find lake Titicaca?", "answer": "Peru"},
    {"question": "In which country can you find the Great Barrier Reef?", "answer": "Australia"},
    {"question": "Italy is home to two enclaved countries. Can you name them?", "answer": "Vatican City and San Marino"},
    {"question": "What is the longest river in Africa?", 'answer': "Nile River"},
    {"question": "Which countries formed the United Kingdom? (give all 4 of them)", "answer": "England, Wales, Scotland and Northern Ireland"},
    {"question": "What is the name of the volcano located 100km from Tokyo?", "answer": "Mount Fuji"},
    {"question": "In which city were the twin towers of the World Trade Center?", "answer": "New York City"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "What is the capital of Pakistan?", "answer": "Islamabad"},
    {"question": "What is the capital of Bangladesh?", "answer": "Dhaka"}, 
    {"question": "What is the capital of Nepal?", "answer": "Kathmandu"},
    {"question": "What is the capital of Bhutan?", "answer": "Thimpu"}, 
    {"question": "What is the capital of Sri Lanka?", "answer": "Colombo"},
    {"question": "What is the capital of Maldives?", "answer": "Male"},
    {"question": "What is the capital of Saudi Arabia?", "answer": "Riyadh"},
    {"question": "What is the capital of Lebanon?", "answer": "Beirut"},
    {"question": "What is the capital of Jordan?", "answer": "Amman"},
    {"question": "What is the capital of Syria?", "answer": "Damascus"},
    {"question": "What is the capital of Iraq?", "answer": "Baghdad"},
    {"question": "What is the capital of Kuwait?", "answer": "Kuwait city"},
    {"question": "What is the capital of Yemen?", "answer": "Sana'a"},
    {"question": "What is the capital of Oman?", "answer": "Muscat"},
    {"question": "What is the capital of UAE?", "answer": "Abu Dhabi"},
    {"question": "What is the capital of Qatar?", "answer": "Doha"},
    {"question": "What is the capital of Bahrain?", "answer": "Manama"},
    {"question": "What is the capital of Iran?", "answer": "Tehran"},
    {"question": "What is the capital of Palestine?", "answer": "East Jerusalem"},
    {"question": "What is the capital of Cyprus?", "answer": "Nicosia"},
    {"question": "What is the capital of Turkey?", "answer": "Ankara"},
    {"question": "What is the capital of China?", "answer": "Beijing"},
    {"question": "What is the capital of Mongolia?", "answer": "Ulaan Baatar"},
    {"question": "What is the capital of Taiwan?", "answer": "Taipei"},
    {"question": "What is the capital of North Korea?", "answer": "Pyongyang"},
    {"question": "What is the capital of Myanmar?", "answer": "Napyidaw"},
    {"question": "What is the capital of Thailand?", "answer": "Bangkok"},
    {"question": "What is the capital of Vietnam?", "answer": "Hanoi"},
    {"question": "What is the capital of Indonesia?", "answer": "Jakarta"},
    {"question": "What is the capital of Malaysia?", "answer": "Kuala Lumpur"},
    {"question": "What is the capital of Timor Leste?", "answer": "Dili"},
    {"question": "What is the capital of Singapore?", "answer": "Singapore"},
    {"question": "What is the capital of Brunei?", "answer": "Bendar Seri Bengawan"},
    {"question": "What is the capital of Uzbekistan?", "answer": "Tashkent"},
    {"question": "What is the capital of Turkmenistan?", "answer": "Ashgabat"},
    {"question": "What is the capital of Kazakhstan?", "answer": "Astana"},
    {"question": "What is the capital of Kyrgyzstan?", "answer": "Bishkek"},
    {"question": "What is the capital of Tajikistan?", "answer": "Dushanbe"},
    {"question": "What is the capital of Albania?", "answer": "Tirana"},
    {"question": "What is the capital of Andorra?", "answer": "Andorra la Vella"},
    {"question": "What is the capital of Austria?", "answer": "Vienna"},
    {"question": "What is the capital of Belarus?", "answer": "Minsk"},
    {"question": "What is the capital of Belgium?", "answer": "Brussels"},
    {"question": "What is the capital of Bulgaria?", "answer": "Sofia"},
    {"question": "What is the capital of Croatia?", "answer": "Zagreb"},
    {"question": "What is the capital of Cyprus?", "answer": "Nicosia"},
    {"question": "What is the capital of Czech Republic?", "answer": "Prague"},
    {"question": "What is the capital of Estonia?", "answer": "Tallin"},
    {"question": "What is the capital of Finland?", "answer": "Helsinki"},
    {"question": "What is the capital of Georgia?", "answer": "Tbilisi"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "What is the capital of Greece?", "answer": "Athens"},
    {"question": "What is the capital of Hungary?", "answer": "Budapest"},
    {"question": "What is the capital of Iceland?", "answer": "Reykjavik"},
    {"question": "What is the capital of Ireland?", "answer": "Dublin"},
    {"question": "What is the capital of ?Italy", "answer": "Rome"},
    {"question": "What is the capital of Kosovo?", "answer": "Pristina"},
    {"question": "What is the capital of Latvia?", "answer": "Riga"},
    {"question": "What is the capital of Lithuania?", "answer": "Vilnius"},
    {"question": "What is the capital of Macedonia?", "answer": "Skopje"},
    {"question": "What is the capital of Malta?", "answer": "Valletta"},
    {"question": "What is the capital of Moldova?", "answer": "Chisinau"},
    {"question": "What is the capital of Monaco?", "answer": "Monaco"},
    {"question": "What is the capital of Netherlands?", "answer": "Amsterdam"},
    {"question": "What is the capital of Norway?", "answer": "Oslo"},
    {"question": "What is the capital of Poland?", "answer": "Warsaw"},
    {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    {"question": "What is the capital of Romania?", "answer": "Bucharest"},
    {"question": "What is the capital of Russia?", "answer": "Moscow"},
    {"question": "What is the capital of San Marino?", "answer": "San Marino"},
    {"question": "What is the capital of Serbia?", "answer": "Belgrade"},
    {"question": "What is the capital of Slovenia?", "answer": "Ljubljana"},
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "What is the capital of Sweden?", "answer": "Stockholm"},
    {"question": "What is the capital of Switzerland?", "answer": "Bern"},
    {"question": "What is the capital of Ukraine?", "answer": "Kiev"},
    {"question": "What is the capital of United Kingdom?", "answer": "London"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "What is the capital of Mexico?", "answer": "Mexico city"},
]

random.shuffle(questions)

def quiz():
    score = 0
    total_questions = len(questions)
    answers = []

    print("Welcome to the Geography Quiz!")
    print(f"There are {total_questions} questions. Try to answer them all correctly!\n")

    for index, q in enumerate(questions):
        print(f"Question {index + 1}: {q['question']}")
        user_answer = input("Your answer: ")

        answers.append({
            "question": q['question'],
            "user_answer": user_answer,
            "correct_answer": q['answer']
        })

        if user_answer.strip().lower() == q['answer'].strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.\n")

    print("Quiz Complete!")
    print(f"Your final score is {score} out of {total_questions}.\n")

    print("Review your answers:")
    for index, answer in enumerate(answers):
        print(f"Question {index + 1}: {answer['question']}")
        print(f"Your answer: {answer['user_answer']}")
        print(f"Correct answer: {answer['correct_answer']}")
        print("Correct!" if answer['user_answer'].strip().lower() == answer['correct_answer'].strip().lower() else "Incorrect.")
        print()

quiz()
