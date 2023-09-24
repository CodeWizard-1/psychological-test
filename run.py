# These are the instructions for importing the libraries

import gspread
import time
from google.oauth2.service_account import Credentials
from pprint import pprint

# Setting up credentials for the Google Sheets API using the service key
# stored in 'creds.json'. The gspread library is used for integration with
# Google Sheets

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('psychological_test')


# Terminal text style

RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'


# This is an ASCII-art representation that is printed to the console
# at the beginning of your script for decorative purposes

art = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠟⠁⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀⣠⣾⣿⣿⣿⡇⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⠃⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠈⠻⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⠟⠁⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠛⠀⠀⠀⠀⠛⠉⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⠀⠀⠀⠀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

"""
for sign in art:
    print(sign, end='', flush=True)
    time.sleep(0.005)



def menu():
    """
    Display a menu and prompt the user for their choice.
    """
    while True:
        print(f"{BLUE}\nMenu:{RESET}\n")
        time.sleep(0.5) 
        for letter in "1. Start psychological testing":
            print(letter, end='', flush=True)
            time.sleep(0.05)

        print()

        time.sleep(0.05)
        for letter in "2. View previous test results":
            print(letter, end='', flush=True)
            time.sleep(0.05)
        time.sleep(0.5)

        print()

        for letter in "3. Exit the program":
            print(letter, end='', flush=True)
            time.sleep(0.05)
        
        print()
        
        choice = input(f"{BLUE}\nEnter the number of your choice: {RESET}")
        for letter in choice:
            print(letter, end='', flush=True)
            time.sleep(0.05)
        
        if choice == "1":
            info()
        elif choice == "2":
            check_previous_score()
        elif choice == "3":
            exit_masage = (f"{YELLOW}\n Thank you for your time. You can take the test at any time convenient for you. See you again!!{RESET}")
            for letter in exit_masage:
                print(letter, end='', flush=True)
                time.sleep(0.05)
            break
        else:
            print(f"{RED}\nInvalid choice. Please enter 1, 2, or 3.{RESET}")


def check_previous_score():
    """
    Check the user's previous score by entering their name.
    """
    existing_sheets = [worksheet.title for worksheet in SHEET.worksheets()]
    data_name = input(f"{BLUE}\nEnter your name to get your previous test results: {RESET}\n")

    if data_name in existing_sheets:
        worksheet = SHEET.worksheet(data_name)
        rows = worksheet.get_all_values()

        if len(rows) > 0:
            print(f"\n{BLUE}Your previous test results:{RESET}\n")

            for row in rows[2:]:
                print(" ".join(row))
        else:
            print(f"\n{RED}No data found for '{data_name}'. Please check the spelling of your name or take the test first.{RESET}")
    else:
        print(f"\n{RED}No data found for '{data_name}'. Please check the spelling of your name or take the test first..{RESET}")

def info():
    """
    Information about the purpose of psychological testing and instructions for taking the test
    """
    welcome_text = f"\n{BLUE}Welcome to psychological testing.{RESET} In this test you will find out your predominant temperament type. You may be Sanguine, Choleric, Phlegmatic or Melancholic. You will be able to better know your own Self. You will understand what your character is like and will be able to take a more correct position in life. Knowing the temperament of your loved ones and friends will help you get along comfortably in the family and in the work team.\n"

    for letter in welcome_text:
        print(letter, end='',flush=True)
        time.sleep(0.05)

    existing_sheets = [worksheet.title for worksheet in SHEET.worksheets()]

    while True:
        global data_name
        data_name = input(f"{BLUE}\nEnter your name:{RESET}\n")
        
        if data_name not in existing_sheets:
            if validate_data(data_name):            
                break
        else:
            print(f"\n{RED}A user named '{data_name}' already exists in the database. Please choose a different name.{RESET}")
            continue

    psychological_test(get_questions())

def validate_data(values):
    """
    This function checks that the user has entered their name correctly
    """
    try:
        if not values.isalpha():
            raise ValueError(
                f"{RED}Invalid characters in your name. Please enter only letters.{RESET}"
            )
        if len(values) < 3 or len(values) > 10:
            raise ValueError(
                f"{RED}the length of your name should not be less than 3 characters and not exceed 10 characters. You entered: {len(values)} characters,{RESET}"
            )
    except ValueError as e:
        print(f"{RED}Invalid data: {e} {RED}try again.{RESET}\n")
        return False
    
    instructions_text = (f"\n{YELLOW}Instructions:{RESET}\n")
    for letter in instructions_text:
        print(letter, end='', flush=True)
        time.sleep(0.05)

    description_instructions = (f"  {GREEN}{values}{RESET}, you are asked to answer 57 questions. "
    "The questions are aimed at identifying your usual way of behavior. "
    "Try to imagine typical situations and give the first “natural” answer that comes to mind. "
    f"If you agree with the statement, indicate {GREEN}'Yes'{RESET}, if not, indicate {GREEN}'No'{RESET}.\n")
     
    for letter in description_instructions:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    
    return True   



def get_questions():
    """
    Access questions from a Google Sheets sheet named 'questions'.
    """
    table_access = SHEET.worksheet('questions')
    questions = table_access.col_values(2)

    return questions

 
def psychological_test(questions):
    """
    Calculation of points based on user answers
    """
    target_question_extra_intro_yes = [1, 3, 8, 10, 13, 17, 22, 25, 27, 39, 44, 46, 49, 53, 56]
    target_question_extra_intro_no = [5, 15, 20, 29, 32, 34, 37, 41, 51]
    target_question_neuroticism_yes = [2, 4, 7, 9, 11, 14, 16, 19, 21, 23, 26, 28, 31, 33, 35, 38, 40, 43, 45, 47, 50, 52, 55, 57]
    target_question_scale_lies_yes = [6, 24, 36]
    target_question_scale_lies_no = [12, 18, 30, 42, 48, 54]

    resalts_extra_intro = 0
    resalts_neuroticism = 0
    resalts_scale_lies = 0


    for idx, question in enumerate (questions, start = 1):
        answer = input(f"\n{BLUE}Question № {idx}{RESET} : {question} ({GREEN}Y/N){RESET}")
        while answer.lower() not in ('y','n'):
            answer = input(f"\n{RED}Please, enter 'Y or 'N'{RESET}")
        if idx in target_question_extra_intro_yes and answer.lower() == 'y':
            resalts_extra_intro += 1
        if idx in target_question_extra_intro_no and answer.lower() == 'n':
            resalts_extra_intro += 1
        if idx in target_question_neuroticism_yes and answer.lower() == 'y':
            resalts_neuroticism += 1
        if idx in target_question_scale_lies_yes and answer.lower() == 'y':
            resalts_scale_lies += 1
        if idx in target_question_scale_lies_no and answer.lower() == 'n':
            resalts_scale_lies += 1
    
    
    
    temperament_type = determine_temperament(resalts_extra_intro, resalts_neuroticism)
    description_temperament_type = describe_temperament(resalts_extra_intro, temperament_type)
    description_extra_intro = describe_introversion_extroversion(resalts_extra_intro)
    description_resalts_neuroticism = describe_neuroticism(resalts_neuroticism)
    description_scale_lies, sign_profile = check_honesty(resalts_scale_lies)
    print_final_message(data_name)
    save_results_to_google_sheets(data_name, resalts_extra_intro, resalts_neuroticism, resalts_scale_lies, temperament_type, description_extra_intro, description_resalts_neuroticism, sign_profile, description_temperament_type)
    return resalts_extra_intro, resalts_neuroticism, resalts_scale_lies, temperament_type, description_extra_intro, description_resalts_neuroticism, sign_profile
    

def determine_temperament(resalts_extra_intro, resalts_neuroticism):
    """
    Determine the predominant type of temperament based on calculated points.
    """
    if resalts_extra_intro <= 12 and resalts_neuroticism <= 12:
        temperament_type = 'Phlegmatic'
    elif resalts_extra_intro <= 12 and resalts_neuroticism > 12:
        temperament_type = 'Melancholic'
    elif resalts_extra_intro >= 12 and resalts_neuroticism <= 12:
        temperament_type = 'Sanguine'
    elif resalts_extra_intro > 12 and resalts_neuroticism > 12:
        temperament_type = 'Choleric'
    
    intro_text = (f"\n  Your predominant temperament type is {YELLOW}{temperament_type}{RESET}")
    for letter in intro_text:
        print(letter, end='', flush=True)
        time.sleep(0.05)

    print()    

    return temperament_type

def describe_temperament(resalts_extra_intro, temperament_type):
    """
    Describe the temperament type based on the result.
    """
    if temperament_type == 'Melancholic':
        description_temperament_type = (f"\n{YELLOW} Melancholic (weak, unbalanced) {RESET} - the owner of a slightly inhibited reaction. "
        "Usually these are indecisive, closed people, prone to deep feelings. "
        "They can easily and steadfastly solve life's problems. On the negative side, "
        "a melancholic can be fearful, squeamish, concentrating on minor events and getting upset because of them.\n")
    elif temperament_type == 'Phlegmatic':
        description_temperament_type = (f"\n{YELLOW} Phlegmatic (strong, inert) {RESET} has a low level of activity. "
        "He is calm, prudent, able to bring the work he has begun to the end. As a rule, "
        "he treats his forces economically and does not waste them on unnecessary activities "
        "or on those that he considers so. Negative manifestations: lethargy, apathy, "
        "lack of will, weakly expressed emotional indicators. Others may seem boring and callous.\n")
    elif temperament_type == 'Sanguine':
        description_temperament_type = (f"\n{YELLOW} Sanguine{RESET} - the person is sociable, cheerful, easily makes new acquaintances. "
        "Such people are also called the soul of the company. His feelings are unstable, "
        "and preferences often change. He is characterized by expressive gestures and facial expressions. "
        "He constantly needs vivid impressions. In rare cases, he plans his day, spontaneity haunts the sanguine "
        "throughout his life in almost all areas. According to the main properties of the central nervous system, "
        "it has a strong and balanced character.\n")
    elif temperament_type == 'Choleric':
        description_temperament_type = (f"\n{YELLOW} Choleric (an unbalanced, strong type of temperament){RESET} is energetic, "
        "his actions are characterized by discontinuity. They can be harsh and emotional. "
        "Due to excessive enthusiasm for any business, they act too diligently, as a result of which "
        "they are quickly exhausted and tired. At its worst, the choleric becomes irritable and unable to control himself.\n")
    else:
        description_temperament_type = "Invalid temperament type"
    
    describe_introversion_extroversion(resalts_extra_intro)

    text_description_temperament_type = description_temperament_type
    for letter in text_description_temperament_type:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    
    print()

    return description_temperament_type


def describe_introversion_extroversion(resalts_extra_intro):
    """
    Describe introversion or extroversion based on the result.
    """
    if resalts_extra_intro > 12:
        description_extra_intro = (" The results also showed that you are an extroverted personality type. "
        "This characterizes you as friendly, talkative, and energetic.\n")

    else:
        description_extra_intro = (" The results also showed that you are an introverted personality type. "
        "This manifests itself in more withdrawn and solitary behavior.\n")
    
    
    return description_extra_intro



def describe_neuroticism(resalts_neuroticism):
    """
    Describe the level of neuroticism based on the result.
    """
    if resalts_neuroticism <= 7:
        description_resalts_neuroticism = (" You are usually characterized by stable and low-intensity emotional reactions. "
        "You rarely experience extreme anxiety, nervousness, or depression and usually cope with stress better.\n")

    elif 8 < resalts_neuroticism <= 13:
        description_resalts_neuroticism = (" You usually have more stable emotional reactions. You may experience stress and anxiety, "
        "but not as much or as often as people with higher levels of neuroticism.\n")

    elif 14 < resalts_neuroticism <= 18:
        description_resalts_neuroticism = (" You tend to have emotional fluctuations and reactions to stress. You may experience anxiety, "
        "nervousness, and worry more often, but not as intensely as people with very high levels of neuroticism.\n")
    else:
        description_resalts_neuroticism = (" You often experience intense and frequent emotional reactions. You may be prone to excessive anxiety, "
        "fears, depression, and feelings of restlessness. You can easily fall into states of nervousness and uncertainty.\n")
    
    text_description_resalts_neuroticism = description_resalts_neuroticism
    for letter in text_description_resalts_neuroticism:
        print(letter, end='', flush=True)
        time.sleep(0.05)
   
    print()

    return description_resalts_neuroticism



def check_honesty(resalts_scale_lies):
    """
    Check if the user's answers may not have been honest.
    """
    if resalts_scale_lies >= 5:
        description_scale_lies = (f" {RED}Important!{RESET}{GREEN} {data_name}{RESET}, {RED}you answered not as you really are, "
        f"but as you would like or as accepted in society. In other words, your answers are not reliable.{RESET}\n")
        sign_profile = "The test subject was not sufficiently honest, the test results are not reliable."
    else:
        description_scale_lies = ""
        sign_profile = "The subject was honest and the test results are reliable."
    
    
    text_description_scale_lies = description_scale_lies
    for letter in text_description_scale_lies:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    
    print()

    return description_scale_lies, sign_profile


def save_results_to_google_sheets(data_name, resalts_extra_intro, resalts_neuroticism, resalts_scale_lies, temperament_type, description_extra_intro, description_resalts_neuroticism, sign_profile, description_temperament_type):
    """
    Create a new sheet with the user's name and add test results to it.
    """
    result_data = [
        ["Temperament Type", "Extra-Introversion Points", "Neuroticism Points", "Scale Lies Points"],
        [description_temperament_type, description_extra_intro, description_resalts_neuroticism, sign_profile]
    ]
    
    worksheet = SHEET.add_worksheet(title=data_name, rows="100", cols="10")
    worksheet.insert_rows(result_data, 2)

    
def print_final_message(data_name):
    """
    Print a final message to the console.
    """
    final_message = (f"{GREEN}{data_name}, {RESET}{YELLOW}thanks for the answers, testing is completed!{RESET}\n"
    "\n\nTo take the test again or view your results, select the desired item in the menu below: ")
    for letter in final_message:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


if __name__ == "__main__":
    menu()
    
     