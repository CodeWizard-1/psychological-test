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


# questions = SHEET.worksheet('questions')

# data = questions.get_all_values()

# print(data)


def info():
    """
    Information about the purpose of psychological 
    testing and instructions for taking the test
    """
    
    print("""\n Welcome to psychological testing. By passing the temperament test,
you will be able to better know your own Self. You will understand what
your character is like and will be able to take a more correct position in life.
Knowing the temperament of your loved ones and friends will help you get along comfortably
in the family and in the work team.\n""")
    while True:
        global data_name
        data_name = input("Enter your name: ")
       

        if validate_data(data_name):
            break
    

def validate_data(values):
    """
    This function checks the correctness of the data entered by the user
    """
    try:
        if len(values) < 3 or len(values) > 10:
            raise ValueError(
                f"the length of your name should not be less than 3 characters and not exceed 10 characters. You entered: {len(values)}characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, try again.\n")
        return False
    
    print("\nInstructions:\n")

    print(f"""  {values}, you are asked to answer 57 questions. The questions are aimed at identifying 
your usual way of behavior. Try to imagine typical situations and give the first “natural” 
answer that comes to mind. If you agree with the statement, indicate 'Yes', if not, indicate 'No'.\n""")
        
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
    answer = input(f"\nQuestion № {idx} : {question}(Enter 'Y' or 'N')")
    while answer.lower() not in ('y','n'):
        answer = input("\nPlease, enter 'Y or 'N'")
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



print("\nThanks for the answers, no more questions\n")
print(f"You have scored {resalts_extra_intro} points\n")
print(f"You have scored {resalts_neuroticism} points\n")
print(f"You have scored {resalts_scale_lies} points\n")
 
if resalts_extra_intro <= 12 and resalts_neuroticism <= 12:
    print(f"Your predominant temperament type is Phlegmatic\n")
elif resalts_extra_intro <= 12 and resalts_neuroticism > 12:
    print(f"Your predominant temperament type is Melancholic\n")
elif resalts_extra_intro >= 12 and resalts_neuroticism <= 12:
    print(f"Your predominant temperament type is Sanguine\n")
elif resalts_extra_intro > 12 and resalts_neuroticism > 12:
    print(f"Your predominant temperament type is Choleric\n")

result_data = [
    ["Name", "Extra-Introversion Points", "Neuroticism Points", "Scale Lies Points", "Temperament Type"],
    [data_name, resalts_extra_intro, resalts_neuroticism, resalts_scale_lies, ""]
]
worksheet = SHEET.add_worksheet(title=data_name, rows="100", cols="10")
worksheet.insert_rows(result_data, 2) 