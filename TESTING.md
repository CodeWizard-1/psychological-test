# **Testing**

<br>

## **Manual Testing**

### **Full Testing:**

<br>

The following steps were taken to test the functionality of the application's features and validate user inputs:

<br>

**Main Menu**

<br>

| Functionality Tested | Expected Outcome | Testing Performed | Pass/Fail |
| ------- | ---------------- | ----------------- | --------- |
|         |
| Load App | The main menu is displayed and the user is prompted to make a choice. | Click the "Run Program" button on the landing page of the deployed application. | Pass |

![App Loaded](./documentation/image-32.png)

| Functionality Tested | Expected Outcome | Testing Performed | Pass/Fail |
| ------- | ---------------- | ----------------- | --------- |
|         |
| Validation for user input: **Enter the number of your choice:** | Error handled and feedback message displayed to user | Attempt input of "q" "empty" "4" | Pass |

![Main Menu User Input Validation](./documentation/image-35.png)

| Functionality Tested | Expected Outcome | Testing Performed | Pass/Fail |
| ------- | ---------------- | ----------------- | --------- |
|         |
| Validation for user input: **Enter the number of your choice:** | Input validated  user input prompt for name displayed | Input "1" | Pass |

<br>

**User Name**

<br>

![User Name Input](./documentation/image-36.png)

| Functionality Tested | Expected Outcome | Testing Performed | Pass/Fail |
| ------- | ---------------- | ----------------- | --------- |
|         |
| Validation for user input: **Enter you name:** | Error handled and feedback message displayed to user | Attempt input of "123" "!!!" "empty" | Pass |

![User Name Input Validation](./documentation/image-37.png)

| Functionality Tested | Expected Outcome | Testing Performed | Pass/Fail |
| ------- | ---------------- | ----------------- | --------- |
|         |
| Validation for user input: **Enter you name:** | Error handled and feedback message displayed to user | Attempt input of "w" "qwertyuiopas" | Pass |

![User Name Input Validation](./documentation/image-38.png)


<br>

**Answers on questions**

<br>

![Answers on questions](./documentation/image-39.png)

| Functionality Tested | Expected Outcome | Testing Performed | Pass/Fail |
| ------- | ---------------- | ----------------- | --------- |
|         |
| Validation for user input: **(Y/N)** | Entering a Yes or No answer | Input of "T""empty"| Pass |

![Wrong answer](./documentation/image-40.png)

<br>

**View previous test results**

<br>

| Functionality Tested | Expected Outcome | Testing Performed | Pass/Fail |
| ------- | ---------------- | ----------------- | --------- |
|         |
| Validation for user input: **Enter your name to get your previos results:** | If such a name is not in the Google table, then the error is processed and a feedback message is displayed to the user. | Attempt input of "qwe" | Pass |

![Alt text](./documentation/image-41.png)
