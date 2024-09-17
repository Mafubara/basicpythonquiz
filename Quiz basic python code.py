import time
#Score
score = 0

#Error Displayed
INVALIDG = "\n❌Invalid Choice! Please Try Again...❌"
INVALID = "\n❌Invalid Letter! Please try again...❌"
REALLY = "\n🤷‍♂️Are you for real??🤷‍♂️"

print("Starting Program...")
time.sleep(5)
print(r"""
  __   _  _  __  ____    ____  __  _  _  ____  _  _   
 /  \ / )( \(  )(__  )  (_  _)(  )( \/ )(  __)/ \/ \  
(  O )) \/ ( )(  / _/     )(   )( / \/ \ ) _) \_/\_/  
 \__\)\____/(__)(____)   (__) (__)\_)(_/(____)(_)(_)""")
time.sleep(3)
print("\n*******************************************************************************")
print("***                    This quiz contains 10 questions                      ***")
print("*******************************************************************************")
time.sleep(3)
print("\n*******************************************************************************")
print("***                       🖥️QUIZ TOPIC: COMPUTER🖥️                          ***")
print("********************************************************************************")
time.sleep(2)
Name = input("\nPlease type your name here: ")
print ("************************************")
print ("*** 👨🏻Male                       ***")
print ("*** 👩🏻Female                     ***")
print ("************************************")
Gender = input("\nGender: ")
while Gender != 'Female' and Gender != 'female' and Gender != 'Male' and Gender != 'male':
    print(INVALIDG)
    print("\n************************************")
    print("*** 👨🏻Male                       ***")
    print("*** 👩🏻Female                     ***")
    print("************************************")
    Gender = input("\nGender: ")
if Gender == 'Female' or Gender == 'female':
    Gender = "👩🏻"
else:
    Gender = "👨🏻"

print ("\n\n**************Your Stats**************")
print (f"  {Gender}{Name}                         ")
print (f"  Score: {score} / 10                    ")
print ("**************************************")
print(r"""
  __   _  _  __  ____    ____  ____  __   ____  ____  ____    __  __ _    ____            
 /  \ / )( \(  )(__  )  / ___)(_  _)/ _\ (  _ \(_  _)/ ___)  (  )(  ( \  ( __ \           
(  O )) \/ ( )(  / _/   \___ \  )( /    \ )   /  )(  \___ \   )( /    /   (__ ( _  _  _   
 \__\)\____/(__)(____)  (____/ (__)\_/\_/(__\_) (__) (____/  (__)\_)__)  (____/(_)(_)(_)  
""")
time.sleep(1)
print(r"""
 ____ 
(___ \
 / __/
(____)
""")
time.sleep(1)
print(r"""
  __  
 /  \ 
(_/ / 
 (__) 
""")
time.sleep(1)
print(r"""
 ____  ____  __   ____  ____ 
/ ___)(_  _)/ _\ (  _ \(_  _)
\___ \  )( /    \ )   /  )(  
(____/ (__)\_/\_/(__\_) (__) 
""")

#Prompt user to input valid letter, otherwise the question repeats.
q1 = input("\n\n🖥️1. What is the latest version of Windows OS??🖥️"
      "\nA. Windows 10 \nB. Windows 11 \nC. Windows 7 \nD. Windows 8.1"
      "\nYour Answer: ")
#However if you type nothing, I can't tell if you're joking..
while q1 != 'A' and q1 != 'B' and q1 != 'C' and q1 != 'D' and q1 != 'a' and q1 != 'b' and q1 != 'c' and q1 != 'd':
    if q1 == '':
        print(REALLY)
    else:
        print(INVALID)
    q1 = input("\n1. What is the latest version of Windows OS??"
               "\nA. Windows 10 \nB. Windows 11 \nC. Windows 7 \nD. Windows 8.1"
               "\nYour Answer: ")
#If the answer is correct, score is added by one point, if not then no points for you.
if q1 == 'B' or q1 == 'b':
    score = 1
else:
    score = 0

q2 = input("\n🖥️2. Which one is not an operating system??🖥️"
      "\nA. Linux \nB. macOS \nC. Android \nD. iPad"
      "\nYour Answer: ")
while q2 != 'A' and q2 != 'B' and q2 != 'C' and q2 != 'D' and q2 != 'a' and q2 != 'b' and q2 != 'c' and q2 != 'd':
    if q2 == '':
        print(REALLY)
    else:
        print(INVALID)
    q2 = input("\n🖥️2. Which one is not an operating system??🖥️"
               "\nA. Linux \nB. macOS \nC. Android \nD. iPad"
               "\nYour Answer: ")
if q2 == 'D' or q2 == 'd':
    score = score + 1
else:
    score = score

q3 = input("\n🖥️3. What is the operating system that an iPhone uses??🖥️"
      "\nA. Android \nB. macOS \nC. iOS \nD. iPadOS"
      "\nYour Answer: ")
while q3 != 'A' and q3 != 'B' and q3 != 'C' and q3 != 'D' and q3 != 'a' and q3 != 'b' and q3 != 'c' and q3 != 'd':
    if q3 == '':
        print(REALLY)
    else:
        print(INVALID)
    q3 = input("\n🖥️3. What is the operating system that an iPhone uses??🖥️"
               "\nA. Android \nB. macOS \nC. iOS \nD. iPadOS"
               "\nYour Answer: ")
if q3 == 'C' or q3 == 'c':
    score = score + 1
else:
    score = score

q4 = input("\n🖥️4. Which one is not a type of computer??🖥️"
      "\nA. Microcomputer \nB. Personal Computer \nC. Supercomputer \nD. Mainframe Computer"
      "\nYour Answer: ")
while q4 != 'A' and q4 != 'B' and q4 != 'C' and q4 != 'D' and q4 != 'a' and q4 != 'b' and q4 != 'c' and q4 != 'd':
    if q4 == '':
        print(REALLY)
    else:
        print(INVALID)
    q4 = input("\n🖥️4. Which one is not a type of computer??🖥️"
      "\nA. Microcomputer \nB. Personal Computer \nC. Supercomputer \nD. Mainframe Computer"
      "\nYour Answer: ")
if q4 == 'B' or q4 == 'b':
    score = score + 1
else:
    score = score

q5 = input("\n🖥️5. It is the core of the computer that is responsible for processing and storing data\n and controls all computer functions??🖥️"
      "\nA. CPU \nB. Motherboard \nC. Processor \nD. System Unit"
      "\nYour Answer: ")
while q5 != 'A' and q5 != 'B' and q5 != 'C' and q5 != 'D' and q5 != 'a' and q5 != 'b' and q5 != 'c' and q5 != 'd':
    if q5 == '':
        print(REALLY)
    else:
        print(INVALID)
    q5 = input("\n🖥️5. It is the core of the computer that is responsible for processing and storing data\n and controls all computer functions??🖥️"
        "\nA. CPU \nB. Motherboard \nC. Processor \nD. System Unit"
        "\nYour Answer: ")
if q5 == 'D' or q5 == 'd':
    score = score + 1
else:
    score = score

print(r"""
____  ____  _  _  ____ 
(_  _)(  _ \/ )( \(  __)
  )(   )   /) \/ ( ) _) 
 (__) (__\_)\____/(____)""")
time.sleep(1)
print(r"""
  __  ____ 
 /  \(  _ \
(  O ))   /
 \__/(__\_)""")
time.sleep(1)
print(r"""
 ____  __   __    ____  ____  _  _   
(  __)/ _\ (  )  / ___)(  __)/ \/ \  
 ) _)/    \/ (_/\\___ \ ) _) \_/\_/  
(__) \_/\_/\____/(____/(____)(_)(_)""")
time.sleep(3)
q6 = input("\n🖥️6. BIOS means Basic Input Output System.🖥️"
      "\nA. TRUE \nB. FALSE \nYour Answer: ")
while q6 != 'A' and q6 != 'B' and q6 != 'a' and q6 != 'b':
    if q6 == '':
        print(REALLY)
    else:
        print(INVALID)
    q6 = input("\n🖥️6. BIOS means Basic Input Output System.🖥️"
                   "\nA. TRUE \nB. FALSE \nYour Answer: ")
if q6 == 'A' or q6 == 'a':
    score = score + 1
else:
    score = score

q7 = input("\n🖥️7. Monitor is an example of an input device.🖥️"
      "\nA. TRUE \nB. FALSE \nYour Answer: ")
while q7 != 'A' and q7 != 'B' and q7 != 'a' and q7 != 'b':
    if q7 == '':
        print(REALLY)
    else:
        print(INVALID)
    q7 = input("\n🖥️7. Monitor is an example of an input device.🖥️"
                   "\nA. TRUE \nB. FALSE \nYour Answer: ")
if q7 == 'B' or q7 == 'b':
    score = score + 1
else:
    score = score

q8 = input("\n🖥️8. In Egyptian Numbering System, Tadpole is equal to 100,000.🖥️"
      "\nA. TRUE \nB. FALSE \nYour Answer: ")
while q8 != 'A' and q8 != 'B' and q8 != 'a' and q8 != 'b':
    if q8 == '':
        print(REALLY)
    else:
        print(INVALID)
    q8 = input("\n🖥️8. In Egyptian Numbering System, Tadpole is equal to 100,000.🖥️"
                   "\nA. TRUE \nB. FALSE \nYour Answer: ")
if q8 == 'A' or q8 == 'a':
    score = score + 1
else:
    score = score
time.sleep(1)
print("\nBack to multiple choices...")
time.sleep(1)

q9 = input("\n🖥️9.It is an output device that takes the electronic data stored on a computer or other device and generates a hard copy.🖥️"
      "\nA. Camcorder \nB. Printer \nC. Monitor \nD. Scanner"
      "\nYour Answer: ")
while q9 != 'A' and q9 != 'B' and q9 != 'C' and q9 != 'D' and q9 != 'a' and q9 != 'b' and q9 != 'c' and q9 != 'd':
    if q9 == '':
        print(REALLY)
    else:
        print(INVALID)
    q9 = input("\n🖥️9.It is an output device that takes the electronic data stored on a computer or other device and generates a hard copy.🖥️"
      "\nA. Camcorder \nB. Printer \nC. Monitor \nD. Scanner"
      "\nYour Answer: ")
if q9 == 'B' or q9 == 'b':
    score = score + 1
else:
    score = score
q10 = input("\n🖥️10.What is the Android Skin that is exclusive to Samsung Devices?.🖥️"
      "\nA. HyperOS \nB. OxygenOS \nC. EMUI \nD. OneUI"
      "\nYour Answer: ")
while q10 != 'A' and q10 != 'B' and q10 != 'C' and q10 != 'D' and q10 != 'a' and q10 != 'b' and q10 != 'c' and q10 != 'd':
    if q10 == '':
        print(REALLY)
    else:
        print(INVALID)
    q10 = input("\n🖥️10.What is the Android Skin that is exclusive to Samsung Devices?.🖥️"
                "\nA. HyperOS \nB. OxygenOS \nC. EMUI \nD. OneUI"
                "\nYour Answer: ")
if q10 == 'D' or q10 == 'd':
    score = score + 1
else:
    score = score
time.sleep(3)
print(r"""
  ___  __   __ _   ___  ____   __  ____  _  _  __     __  ____  __  __   __ _  ____  _  _   
 / __)/  \ (  ( \ / __)(  _ \ / _\(_  _)/ )( \(  )   / _\(_  _)(  )/  \ (  ( \/ ___)/ \/ \  
( (__(  O )/    /( (_ \ )   //    \ )(  ) \/ (/ (_/\/    \ )(   )((  O )/    /\___ \\_/\_/  
 \___)\__/ \_)__) \___/(__\_)\_/\_/(__) \____/\____/\_/\_/(__) (__)\__/ \_)__)(____/(_)(_)""")
print("\n🎉🥳Congratulations!! You have completed the quiz!!🥳🎉")


#Score is Displayed after finishing all 10 questions.
time.sleep(2)
print("\n⏳Calculating your score...⏳")
time.sleep(4)
print("\n⌛Done!⌛")
time.sleep(2)
print ("\n\n**************Your Stats**************")
print (f"  {Gender}{Name}                         ")
print (f"  Score: {score} out of 10               ")
print ("**************************************")

print("🌟Victoria Quizette is commenting....🌟")
time.sleep(5)
if score == 10:
    print("\n🌟Victoria Quizette: Verily, thou hast achieved a most splendid score, one that is nigh unto perfection!"
          "\nSuch an accomplishment doth shine like the brightest star in the firmament, a testament to thy diligence and skill.🌟")
elif score >= 9:
    print("\n🌟Victoria Quizette: Thou art on the precipice of achieving a most splendid score, verily near to the pinnacle of perfection.🌟")
elif score >= 6:
    print("\n🌟Victoria Quizette: In truth, thy skill and diligence are commendable, and I find myself compelled to "
          "\nexpress my admiration for the remarkable work thou hast accomplished. Such prowess is rare and worthy of high praise.🌟")
elif score >= 3:
    print("\n🌟Victoria Quizette: Thou hast exerted thy utmost effort! Fear not, for the opportunity shall arise once more for thee to endeavor anew.🌟")
elif score >= 1:
    print("\n🌟Victoria Quizette: Thou hast performed adequately, I suppose, in thy endeavors.🌟")
else:
    print("\n🌟Victoria Quizette: Womp womp.🌟")
time.sleep(5)
print("\nThank you for playing!!!!!")
time.sleep(2)
print("\nCoded by Naven Marl M. Cuenca")
time.sleep(2)
print("❤Goodbye!!❤")
