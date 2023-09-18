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
    print("Instructions:\n")
    print("""  You are asked to answer 57 questions. The questions are aimed at identifying your usual way of behavior. 
Try to imagine typical situations and give the first “natural” answer that comes to mind. If you agree with the statement, 
indicate 'yes', if not, indicate 'no'.\n""")

info()   