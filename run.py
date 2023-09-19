import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('psychological_test')

RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RESET = '\033[0m'

# questions = SHEET.worksheet('questions')

# data = questions.get_all_values()

# print(data)


def info():
    """
    Information about the purpose of psychological 
    testing and instructions for taking the test
    """
    
    print("\n Welcome to psychological testing. By passing the temperament test, you will be able to better know your own Self. You will understand what your character is like and will be able to take a more correct position in life. Knowing the temperament of your loved ones and friends will help you get along comfortably in the family and in the work team.\n")
    while True:
        global data_name
        data_name = input("Enter your name:\n")
       

        if validate_data(data_name):
            break
    

def validate_data(values):
    """
    This function checks the correctness of the data entered by the user
    """
    try:
        if len(values) < 3 or len(values) > 10:
            raise ValueError(
                f"{RED}the length of your name should not be less than 3 characters and not exceed 10 characters. You entered: {len(values)} characters,{RESET}"
            )
    except ValueError as e:
        print(f"{RED}Invalid data: {e} {RED}try again.{RESET}\n")
        return False
    
    print("\nInstructions:\n")
    print(f"""  {GREEN}{values}{RESET}, you are asked to answer 57 questions. The questions are aimed at identifying your usual way of behavior. Try to imagine typical situations and give the first “natural” answer that comes to mind. If you agree with the statement, indicate 'Yes', if not, indicate 'No'.\n""")
        
    return True   



start_block = info()
 
table_access = SHEET.worksheet('questions')
questions = table_access.col_values(2)

target_question_extra_intro_yes = [1, 3, 8, 10, 13, 17, 22, 25, 27, 39, 44, 46, 49, 53, 56]
target_question_extra_intro_no = [5, 15, 20, 29, 32, 34, 37, 41, 51]
target_question_neuroticism_yes = [2, 4, 7, 9, 11, 14, 16, 19, 21, 23, 26, 28, 31, 33, 35, 38, 40, 43, 45, 47, 50, 52, 55, 57]
target_question_scale_lies_yes = [6, 24, 36]
target_question_scale_lies_no = [12, 18, 30, 42, 48, 54]

resalts_extra_intro = 0
resalts_neuroticism = 0
resalts_scale_lies = 0


for idx, question in enumerate (questions, start = 1):
    answer = input(f"\n{BLUE}Question № {idx}{RESET} : {question} ({GREEN}Enter 'Y' or 'N'){RESET}")
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



print(f"\n{BLUE}Thanks for the answers, no more questions{RESET}\n")
 
if resalts_extra_intro <= 12 and resalts_neuroticism <= 12:
    temperament_type = 'Phlegmatic'
elif resalts_extra_intro <= 12 and resalts_neuroticism > 12:
    temperament_type = 'Melancholic'
elif resalts_extra_intro >= 12 and resalts_neuroticism <= 12:
    temperament_type = 'Sanguine'
elif resalts_extra_intro > 12 and resalts_neuroticism > 12:
    temperament_type = 'Choleric'

print(f"Your predominant temperament type is {temperament_type}\n")

if temperament_type == 'Melancholic':
    print(f"  Melancholic (weak, unbalanced) - the owner of a slightly inhibited reaction. Usually these are indecisive, closed people, prone to deep feelings. They can easily and steadfastly solve life's problems. On the negative side, a melancholic can be fearful, squeamish, concentrating on minor events and getting upset because of them.\n")
elif temperament_type == 'Phlegmatic':
    print(f"  Phlegmatic (strong, inert) has a low level of activity. He is calm, prudent, able to bring the work he has begun to the end. As a rule, he treats his forces economically and does not waste them on unnecessary activities or on those that he considers so. Negative manifestations: lethargy, apathy, lack of will, weakly expressed emotional indicators. Others may seem boring and callous.\n")
elif temperament_type == 'Sanguine':
    print(f"  The person is sociable, cheerful, easily makes new acquaintances. Such people are also called the soul of the company. His feelings are unstable, and preferences often change. He is characterized by expressive gestures and facial expressions. He constantly needs vivid impressions. In rare cases, he plans his day, spontaneity haunts the sanguine throughout his life in almost all areas. According to the main properties of the central nervous system, it has a strong and balanced character.\n")
elif temperament_type == 'Choleric':   
    print(f"  Choleric (an unbalanced, strong type of temperament) is energetic, his actions are characterized by discontinuity. They can be harsh and emotional. Due to excessive enthusiasm for any business, they act too diligently, as a result of which they are quickly exhausted and tired. At its worst, the choleric becomes irritable and unable to control himself.\n")

# print(f"You have scored {resalts_extra_intro} points\n")
# print(f"You have scored {resalts_neuroticism} points\n")
# print(f"You have scored {resalts_scale_lies} points\n")

if resalts_extra_intro > 12:
    print(f"The results also showed that you are an extroverted personality type. This characterizes you as friendly, talkative and energetic.\n")
if resalts_extra_intro <= 12:
    print(f"The results also showed that you are an introverted personality type. This manifests itself in more withdrawn and solitary behavior.\n")
# if resalts_neuroticism > 12:
#     print(f"Your are ...")
# if resalts_neuroticism <= 12:
#     print(f"Your are ...")



if resalts_scale_lies >= 4:
    print(f"{RED}Important! {data_name}, you answered not as you really are, but as you would like or as accepted in society. In other words, your answers are not reliable.{RESET}\n")
    

result_data = [
    ["Name", "Extra-Introversion Points", "Neuroticism Points", "Scale Lies Points", "Temperament Type"],
    [data_name, resalts_extra_intro, resalts_neuroticism, resalts_scale_lies, temperament_type]
]
worksheet = SHEET.add_worksheet(title=data_name, rows="100", cols="10")
worksheet.insert_rows(result_data, 2) 