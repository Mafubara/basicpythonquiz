import time
#All of the questions and answers are stored here
questions_computer = [
    {
        "question": "What is the brain of a computer?",
        "options": ["Motherboard", "GPU", "CPU", "RAM"],
        "answer": "CPU"
    },
    {
        "question": "It is the core of the computer that is responsible for processing and storing data and controls all computer functions.",
        "options": ["CPU", "Motherboard", "Processor", "System Unit"],
        "answer": "System Unit"
    },
    {
        "question": "What is the term for a computer's ability to perform multiple tasks simultaneously?",
        "options": ["Multitasking", "Multiprocessing", "Multithreading", "Parallel Processing"],
        "answer": "Multitasking"
    },
    {
        "question": "It is an output device that takes the electronic data stored on a computer or other device and generates a hard copy.",
        "options": ["Camcorder", "Printer", "Monitor", "Scanner"],
        "answer": "Printer"
    },
    {
        "question": "Which type of software manages a computer's hardware resources?",
        "options": ["Application Software", "Operating System", "Utility Software", "Firmware"],
        "answer": "Operating System"
    },
    {
        "question": "What is the term for a network of interconnected computers?",
        "options": ["Internet", "Intranet", "Extranet", "Network"],
        "answer": "Network"
    },
    {
        "question": "Which type of storage retains data even when power is off?",
        "options": ["RAM", "ROM", "Hard Drive", "SSD"],
        "answer": "ROM"
    },
    {
        "question": "What is malware that replicates itself?",
        "options": ["Virus", "Worm", "Trojan", "Spyware"],
        "answer": "Virus"
    },
    {
        "question": "What is the primary function of a computer's CPU?",
        "options": ["Data Storage", "Power Supply", "Input/Output Operations", "Execution of Instructions"],
        "answer": "Execution of Instructions"
    },
    {
        "question": "What is the purpose of a firewall?",
        "options": ["To block unauthorized access", "To allow all network traffic", "To improve network performance", "To provide antivirus protection"],
        "answer": "To block unauthorized access"
    }
]


questions_python = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": [".py", ".python", ".pyt", ".txt"],
            "answer": ".py"
        },
        {
            "question": "What does the input() function do in Python??",
            "options": ["It displays output on the screen.", "It reads data from the user.", "It returns the length of a string.", "It starts a loop."],
            "answer": "It reads data from the user."
        },
        {
            "question": "What type of error will occur if you try to divide by zero in Python?",
            "options": ["SyntaxError", "TypeError", "ZeroDivisionError", "ValueError"],
            "answer": "ZeroDivisionError"
        },
        {
            "question": "What does the and operator do in Python?",
            "options": ["Returns True only if both conditions are True", "Returns True if at least one condition is True", "Negates the condition", "Compares two values for equality"],
            "answer": "Returns True only if both conditions are True"
        },
        {
            "question": "What does the or operator do in Python?",
            "options": ["Compares two values for equality", "Negates the condition", "Returns True if at least one condition is True", "Returns True only if both conditions are True"],
            "answer": "Returns True if at least one condition is True"
        },
        {
            "question": "What does the not logical operator do in Python?",
            "options": ["Compares two values for equality", "Returns True if at least one condition is True", "Returns True if both conditions are True", "Negates a condition (turns True into False and vice versa)"],
            "answer": "Negates a condition (turns True into False and vice versa)"
        },
        {
            "question": "What does the print() function do in Python?",
            "options": ["It adds two numbers together.", "It displays output to the console.", "It stores a value in a variable.", "It defines a function."],
            "answer": "It displays output to the console."
        },
        {
            "question": "Which Python keyword is used to define a function?",
            "options": ["def", "function", "func", "define"],
            "answer": "def"
        },
        {
            "question": "Which of these is used to create an empty list in Python?",
            "options": ["[]", "{}", "()", "<>"],
            "answer": "[]"
        },
        {
            "question": "Which of the following is the correct way to declare a variable in Python?",
            "options": ["var x = 5", "x = 5", "int x = 5", "5 = x"],
            "answer": "x = 5"
        }
    ]

#Quiz about computer
def computer_quiz():
    score = 0
    total_questions = len(questions_computer)

    # Prompt user to input their name:
    name = input("\nPlease type your name here: ")
    print("*************************************************************************************************************")
    print("                                                   👨🏻Male                                                    ")
    print("                                                  👩🏻Female                                                   ")
    print("*************************************************************************************************************")

    # Prompt user to input their gender:
    gender = input("\nGender: ").lower()

    # Type it properly otherwise it's considered "Invalid":
    while gender != 'female' and gender != 'male':
        print(INVALID)
        print("*************************************************************************************************************")
        print("                                                   👨🏻Male                                                    ")
        print("                                                  👩🏻Female                                                   ")
        print("*************************************************************************************************************")
        gender = input("\nGender: ")

    # Typing your gender will give you an emoji based on it:
    if gender == 'female':
        gender = "👩🏻"
    else:
        gender = "👨🏻"

    # Stats is displayed after inputting your name and gender:
    print("\n\n*********************************************Your Stats******************************************************")
    print(f"                                              {gender}{name}                                                ")
    print(f"                                          Score: {score} out of 10                                          ")
    print("*************************************************************************************************************\n")
    print("Loading Computer Quiz.....\n")

    time.sleep(5)
    print(r"""

 .d8888b.   .d88888b.  888b     d888 8888888b.  888     888 88888888888 8888888888 8888888b.        .d88888b.  888     888 8888888 8888888888P 888 
d88P  Y88b d88P" "Y88b 8888b   d8888 888   Y88b 888     888     888     888        888   Y88b      d88P" "Y88b 888     888   888         d88P  888 
888    888 888     888 88888b.d88888 888    888 888     888     888     888        888    888      888     888 888     888   888        d88P   888 
888        888     888 888Y88888P888 888   d88P 888     888     888     8888888    888   d88P      888     888 888     888   888       d88P    888 
888        888     888 888 Y888P 888 8888888P"  888     888     888     888        8888888P"       888     888 888     888   888      d88P     888 
888    888 888     888 888  Y8P  888 888        888     888     888     888        888 T88b        888 Y8b 888 888     888   888     d88P      Y8P 
Y88b  d88P Y88b. .d88P 888   "   888 888        Y88b. .d88P     888     888        888  T88b       Y88b.Y8b88P Y88b. .d88P   888    d88P        "  
 "Y8888P"   "Y88888P"  888       888 888         "Y88888P"      888     8888888888 888   T88b       "Y888888"   "Y88888P"  8888888 d8888888888 888 
                                                                                                          Y8b                                      
""")
    time.sleep(3)
    print("\nAnswer the 10 following questions:\n")

    time.sleep(3)
    print("Quiz starts now!!\n")

    # List of possible answer choices
    answer_choices = ["A", "B", "C", "D"]

    # Iterate through each question
    for i, question in enumerate(questions_computer):
        print(f"\n{i + 1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{answer_choices[j]}. {option}")

        # Loop until the user provides a valid input
        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

            # Check if the input is a valid letter (A, B, C, D)
            if user_answer in answer_choices:
                if question['options'][answer_choices.index(user_answer)] == question['answer']:
                    score += 1
                    break
                else:
                    break
            else:
                print("\nInvalid choice! Please enter a letter (A/B/C/D).\n")


    time.sleep(2)
    print("\n⏳Calculating your score...⏳")

    time.sleep(3)
    print("\n⌛Done!⌛")

    time.sleep(2)
    print("\n\n*********************************************Your Stats******************************************************")
    print(f"                                              {gender}{name}                                                ")
    print(f"                                          Score: {score} out of 10                                          ")
    print("*************************************************************************************************************")

    # This person judges your score elegantly...
    print("\n🌟Victoria Quizette is commenting....🌟")

    time.sleep(3)
    # The comments will vary according to your score: 10, 9-7, 6-4, 3-2, 1, 0
    if score == 10:
        print(
            "\n🌟Victoria Quizette: Verily, thou hast achieved a most splendid score, one that is nigh unto perfection!"
            "\nSuch an accomplishment doth shine like the brightest star in the firmament, a testament to thy diligence and skill.🌟")
    elif score >= 9:
        print(
            "\n🌟Victoria Quizette: Thou art on the precipice of achieving a most splendid score, verily near to the pinnacle of perfection.🌟")
    elif score >= 6:
        print(
            "\n🌟Victoria Quizette: In truth, thy skill and diligence are commendable, and I find myself compelled to "
            "\nexpress my admiration for the remarkable work thou hast accomplished. Such prowess is rare and worthy of high praise.🌟")
    elif score >= 3:
        print(
            "\n🌟Victoria Quizette: Thou hast exerted thy utmost effort! Fear not, for the opportunity shall arise once more for thee to endeavor anew.🌟")
    elif score >= 1:
        print("\n🌟Victoria Quizette: Thou hast performed adequately, I suppose, in thy endeavors.🌟")
    else:
        print("\n🌟Victoria Quizette: Womp womp.🌟")
    time.sleep(3)

    print("\n🎉🥳Congratulations!! You have completed the quiz!!🥳🎉")

    reset()

#Quiz about python
def python_quiz():
    score = 0
    total_questions = len(questions_python)

    # Prompt user to input their name:
    name = input("\nPlease type your name here: ")
    print("*************************************************************************************************************")
    print("                                                   👨🏻Male                                                    ")
    print("                                                  👩🏻Female                                                   ")
    print("*************************************************************************************************************")
    # Prompt user to input their gender:

    gender = input("\nGender: ").lower()

    # Type it properly otherwise it's considered "Invalid":
    while gender != 'female' and gender != 'male':
        print(INVALID)
        print("*************************************************************************************************************")
        print("                                                   👨🏻Male                                                    ")
        print("                                                  👩🏻Female                                                   ")
        print("*************************************************************************************************************")
        gender = input("\nGender: ")

    # Typing your gender will give you an emoji based on it:
    if gender == 'female':
        gender = "👩🏻"
    else:
        gender = "👨🏻"

    # Stats is displayed after inputting your name and gender:
    print("\n\n*********************************************Your Stats******************************************************")
    print(f"                                              {gender}{name}                                                ")
    print(f"                                          Score: {score} out of 10                                          ")
    print("*************************************************************************************************************")
    print("\nLoading Python Quiz.....\n")

    time.sleep(5)
    print(r"""

8888888b. Y88b   d88P 88888888888 888    888  .d88888b.  888b    888       .d88888b.  888     888 8888888 8888888888P 888 
888   Y88b Y88b d88P      888     888    888 d88P" "Y88b 8888b   888      d88P" "Y88b 888     888   888         d88P  888 
888    888  Y88o88P       888     888    888 888     888 88888b  888      888     888 888     888   888        d88P   888 
888   d88P   Y888P        888     8888888888 888     888 888Y88b 888      888     888 888     888   888       d88P    888 
8888888P"     888         888     888    888 888     888 888 Y88b888      888     888 888     888   888      d88P     888 
888           888         888     888    888 888     888 888  Y88888      888 Y8b 888 888     888   888     d88P      Y8P 
888           888         888     888    888 Y88b. .d88P 888   Y8888      Y88b.Y8b88P Y88b. .d88P   888    d88P        "  
888           888         888     888    888  "Y88888P"  888    Y888       "Y888888"   "Y88888P"  8888888 d8888888888 888 
                                                                                 Y8b                                      
""")

    time.sleep(3)
    print("\nAnswer the 10 following questions:\n")

    time.sleep(3)
    print("Quiz starts now!!\n")

    # List of possible answer choices
    answer_choices = ["A", "B", "C", "D"]

    # Iterate through each question
    for i, question in enumerate(questions_python):
        print(f"\n{i + 1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{answer_choices[j]}. {option}")

        # Loop until the user provides a valid input
        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

            # Check if the input is a valid letter (A, B, C, D)
            if user_answer in answer_choices:
                if question['options'][answer_choices.index(user_answer)] == question['answer']:
                    score += 1
                    break
                else:
                    break
            else:
                print("\nInvalid choice! Please enter a letter (A/B/C/D).\n")

    time.sleep(2)
    print("\n⏳Calculating your score...⏳")

    time.sleep(3)
    print("\n⌛Done!⌛")

    time.sleep(2)
    print("\n\n**********************************************Your Stats****************************************************")
    print(f"                                              {gender}{name}                                                ")
    print(f"                                          Score: {score} out of 10                                          ")
    print("*************************************************************************************************************\n")

    # This person judges your score elegantly...
    print("🌟Victoria Quizette is commenting....🌟")

    time.sleep(3)
    # The comments will vary according to your score: 10, 9-7, 6-4, 3-2, 1, 0
    if score == 10:
        print(
            "\n🌟Victoria Quizette: Verily, thou hast achieved a most splendid score, one that is nigh unto perfection!"
            "\nSuch an accomplishment doth shine like the brightest star in the firmament, a testament to thy diligence and skill.🌟")
    elif score >= 9:
        print(
            "\n🌟Victoria Quizette: Thou art on the precipice of achieving a most splendid score, verily near to the pinnacle of perfection.🌟")
    elif score >= 6:
        print(
            "\n🌟Victoria Quizette: In truth, thy skill and diligence are commendable, and I find myself compelled to "
            "\nexpress my admiration for the remarkable work thou hast accomplished. Such prowess is rare and worthy of high praise.🌟")
    elif score >= 3:
        print(
            "\n🌟Victoria Quizette: Thou hast exerted thy utmost effort! Fear not, for the opportunity shall arise once more for thee to endeavor anew.🌟")
    elif score >= 1:
        print("\n🌟Victoria Quizette: Thou hast performed adequately, I suppose, in thy endeavors.🌟")
    else:
        print("\n🌟Victoria Quizette: Womp womp.🌟")

    time.sleep(3)
    print("\n🎉🥳Congratulations!! You have completed the quiz!!🥳🎉")

    reset()

# Resets the game
def reset():
    reset = input("\nWould you like to restart the quiz?? (Y/N)").upper()

    while reset != 'Y' and reset != 'N':
        print(Error)
        reset = input("\nWould you like to restart the quiz?? (Y/N)").upper()

    if reset == 'Y':
        score = 0
        name = ""
        gender = ""
        return main_menu()
    else:
        time.sleep(3)
        print("Thank your for playing our game!!!⭐⭐⭐")
        print("Brought to you by:")
        time.sleep(3)
        print(r"""
   ___ _   _ ___ _  _  ___   _     
  / __| | | | __| \| |/ __| /_\    
 | (__| |_| | _|| .` | (__ / _ \   
  \___|\___/|___|_|\_|\___/_/_\_\_ 
   /_\ | \| |/ __| __| |  | __/ __|
  / _ \| .` | (_ | _|| |__| _|\__ \
 /_/_\_\_|\_|\___|___|____|___|___/
 | _ \ __| _ \ |    /_\ / __|      
 |  _/ _||   / |__ / _ \\__ \      
 |_| |___|_|_\____/_/ \_\___/      
                                   """)
        time.sleep(3)
        print(r"""

  _______   ______     ______    _______  .______   ____    ____  _______  __  
 /  _____| /  __  \   /  __  \  |       \ |   _  \  \   \  /   / |   ____||  | 
|  |  __  |  |  |  | |  |  |  | |  .--.  ||  |_)  |  \   \/   /  |  |__   |  | 
|  | |_ | |  |  |  | |  |  |  | |  |  |  ||   _  <    \_    _/   |   __|  |  | 
|  |__| | |  `--'  | |  `--'  | |  '--'  ||  |_)  |     |  |     |  |____ |__| 
 \______|  \______/   \______/  |_______/ |______/      |__|     |_______|(__) 
                                                                               

""")
        exit()

Error = "Invalid Choice, please try again..."
score = 0

# Main Menu
def main_menu():
    print("*************************************************************************************************************")
    print("                                             1. Start                                                        ")
    print("                                             2. Exit                                                         ")
    print("*************************************************************************************************************")
    start = input("\nEnter Choice(1/2): ").lower()
    while start != '1' and start != '2':
        print(Error)
        start = input("Enter Choice (1/2): ")
    if start == '1':
        topic()
    else:
        print(r"""
          _______   ______     ______    _______  .______   ____    ____  _______  __  
         /  _____| /  __  \   /  __  \  |       \ |   _  \  \   \  /   / |   ____||  | 
        |  |  __  |  |  |  | |  |  |  | |  .--.  ||  |_)  |  \   \/   /  |  |__   |  | 
        |  | |_ | |  |  |  | |  |  |  | |  |  |  ||   _  <    \_    _/   |   __|  |  | 
        |  |__| | |  `--'  | |  `--'  | |  '--'  ||  |_)  |     |  |     |  |____ |__| 
         \______|  \______/   \______/  |_______/ |______/      |__|     |_______|(__) 
""")
        exit()

# Topic of the quiz
def topic():
    print("*************************************************************************************************************")
    print("                                             1. Computer                                                     ")
    print("                                             2. Python                                                       ")
    print("                                             3. Back                                                         ")
    print("*************************************************************************************************************")
    choice = input("\nEnter Choice (1/2/3): ")
    while choice != '1' and choice != '2' and choice != '3':
        print(Error)
        choice = input("\nEnter Choice (1/2/3): ")
    if choice == '1':
        computer_quiz()
    elif choice == '2':
        python_quiz()

    else:
        main_menu()

# Game loading...
print("Starting game...")
time.sleep(3)
print(r"""
    .d88888b.           d8b               88888888888 d8b                        888 
   d88P" "Y88b          Y8P                   888     Y8P                        888 
   888     888                                888                                888 
   888     888 888  888 888 88888888          888     888 88888b.d88b.   .d88b.  888 
   888     888 888  888 888    d88P           888     888 888 "888 "88b d8P  Y8b 888 
   888 Y8b 888 888  888 888   d88P            888     888 888  888  888 88888888 Y8P 
   Y88b.Y8b88P Y88b 888 888  d88P             888     888 888  888  888 Y8b.      "  
    "Y888888"   "Y88888 888 88888888          888     888 888  888  888  "Y8888  888 
          Y8b                                                                        

                                                                                     """)
time.sleep(3)
main_menu()
