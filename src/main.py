from pystyle import Colors, Colorate, Center, Write
from html2text import html2text
from utils import *
import Get

clearConsole()

# Print Title
title = '''
███████ ██████  ██████  ██    ██ ███████ ███████ ██      ███████ ██████  
██      ██   ██ ██   ██ ██    ██    ███     ███  ██      ██      ██   ██ 
█████   ██   ██ ██████  ██    ██   ███     ███   ██      █████   ██   ██ 
██      ██   ██ ██      ██    ██  ███     ███    ██      ██      ██   ██ 
███████ ██████  ██       ██████  ███████ ███████ ███████ ███████ ██████  
                                                                         
                                                                         
'''
print(Center.XCenter(Colorate.Vertical(Colors.cyan_to_blue, title, 1)))

# Get Username and Password
username = str(Write.Input("Username: ", Colors.cyan_to_blue, 0.01))
password = str(Write.Input("Password: ", Colors.cyan_to_blue, 0.01))

# Get Tokens And Classes
csrf_token, token = Get.Tokens(username, password)

if token is None:
    print(Colorate.Error(f"ERROR: Invalid Username Or Password{Colors.reset}"))
    quit()

classes_response = Get.Classes(csrf_token, token)

clearConsole()

# Get Wanted Class
for i, classes in enumerate(classes_response):
    if i == len(classes_response) - 1:
        print(Colorate.Vertical(Colors.cyan_to_blue, f"[{i}] - {classes['name']}", 1))
        class_choice = int(input())
    else:
        print(Colorate.Vertical(Colors.cyan_to_blue, f"[{i}] - {classes['name']}", 1))
    
classId = classes_response[class_choice]["_id"]

clearConsole()

# Get Assignments
assignments_response = Get.Assignments(classId, csrf_token, token)
for i, assignment in enumerate(assignments_response):
    if i == len(assignments_response) - 1: 
        print(Colorate.Vertical(Colors.cyan_to_blue, f"[{i}] - {assignment['title']}", 1))
        assignment_choice = int(input())
    else:
        print(Colorate.Vertical(Colors.cyan_to_blue, f"[{i}] - {assignment['title']}", 1))

clearConsole()

questions = assignments_response[assignment_choice]['questions']
for i, question in enumerate(questions):
    if question['type'] == 'multiple-choice':
        for answer in question['choices']:
            if answer['isCorrect']:
                answer_text = answer['body'][0]['html']
                answer_text = answer_text[3:]
                answer_text = answer_text[:len(answer_text) - 4]
                answer_text = html2text(answer_text)
    
        question_text = html2text(question['body'][0]['html'])
        print(Colorate.Vertical(Colors.cyan_to_blue, f'\n{question_text}\n', 1))
        print(Colorate.Vertical(Colors.green_to_yellow, f'{answer_text}', 1))
    
    elif question['type'] == 'open-ended':
        question_text = html2text(question['body'][0]['html'])
        print(Colorate.Vertical(Colors.cyan_to_blue, f"\n{question_text}\n", 1))
        print(Colorate.Vertical(Colors.green_to_yellow, 'OPEN ENDED', 1))

while True:
    pass