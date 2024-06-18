import time
import random

sentences = [
    "She sells seashells by the seashore.",
    "I scream, you scream, we all scream for ice cream.",
    "I saw a kitten eating chicken in the kitchen.",
    "I wish to wash my Irish wristwatch.",
    "A big black bear sat on a big black rug.",
    "I have got a date at a quarter to eight; I’ll see you at the gate, so don’t be late."
]

def typing_master_game():
    sentence = random.choice(sentences)
    
    print("Welcome to the Typing Master Game!")
    print("Type the following sentence as fast and accurately as you can:\n")
    print(f"Sentence: {sentence}\n")
    
    input("Press Enter to start...")
    
    start_time = time.time()
    
    user_input = input("\nType here: ")
    
    end_time = time.time()

    time_taken = end_time - start_time
    
    accuracy = calculate_accuracy(sentence, user_input)
    
    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original, typed):
    correct_chars = 0
    for o, t in zip(original, typed):
        if o == t:
            correct_chars += 1
    accuracy = (correct_chars / len(original)) * 100
    return accuracy

typing_master_game()
