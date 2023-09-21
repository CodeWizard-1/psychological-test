# **Psychological test**


![Deployed Site View](docs/devices/coffee-run-deployed-mockup.png)

<br>

[View the deployed app on Heroku](https://psychological-test-9b5971c1081a.herokuapp.com/)

[View the Google Sheets worksheet for the app here](https://docs.google.com/spreadsheets/d/1hX7cJoDRUog7TXDuHcymWQj5D4xJEn-X63nRIaiNijA/edit#gid=0)

<br>

## **CONTENTS**

* [User Experience (UX)](#user-experience-ux)
    * [Strategy](#strategy)
        * [Project Goals](#project-goals)
    * [Scope](#scope)
    * [Design](#design)
        * [Python Logic Flow Chart](#python-logic-flow-chart)
        * [App Functionality and Features](#app-functionality-and-features)
        * [Database](#database)
        * [Error Handling](#error-handling)
        * [Typography](#typography)
        * [Imagery](#imagery)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Programs Used](#programs-used)
    * [Frameworks and Libraries used](#frameworks-and-libraries-used)
* [Deployment and Local Development](#deployment-and-local-development)
* [Testing](#testing)
    * [Automated Testing](#automated-testing)
    * [Manual Testing](#manual-testing)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Solved Bugs](#solved-bugs)
* [Credits](#credits)
    * [Code Used and Referenced](#code-used-and-referenced)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)


# **User Experience (UX)**

## **STRATEGY**
___

## **Project Goals**

<br>

1. Personality Assessment: Testing can be used to assess a person's personality characteristics, such as temperament, introversion/extroversion, neuroticism, and other psychological traits. This can help a person better understand themselves and their individual characteristics.

2. Career Guidance: Personality tests can help determine which professions or career paths may be suitable for a particular person. For example, some temperament types may be more suited to leadership roles, while others may be suited to creative tasks.

3. Stress and Emotion Management: Test results can help a person better understand their emotional reactions and stress management strategies. This can promote better psychological well-being.

4. Psychological consultation: Psychologists can use test results to more accurately diagnose and develop psychological assistance. The tests can help identify psychological problems and give an initial idea of what types of therapy may be effective.
  

## **SCOPE**
___

### **Features**

<br>

* Allow the user to enter username information so that test results can be saved for that user as well.

* Provide the user with information about the purpose of testing, as well as the possibilities of using the information received

* Provide the user with instructions for performing the test

* Allow the user to select their preferred answer to questions provided

<br>

### **Future Implementations**

<br>

Functionality that is not in the scope of this project but may be added later to improve the user experience:

* Ability for users to create an account in which they can store and see all test results
* Possibility for the user to send the results via the provided email

<br>

## **DESIGN**
___

<br>

## **Python Logic Flow Chart**

<br>

![Flow Chart displaying stages and logic of the program](documentation/flow-charts-psychological-test-logic.png)

## **Functionality and Features**

<br>

### **Main Menu**

<br>

![Main Menu](image.png))

When starting the application, users see the large Greek letter psi "Ψ". The words psyche, psychology, psychiatry begin with this letter, and therefore this letter has become part of the logo of almost all psychological organizations in the world.
  This letter was created using an ASCII art generator and lets the user know that a psychological test will be taken.
A welcome message also appears in front of the user, informing about the purposes of testing, as well as the possibilities of applying the results obtained.

### **Instruction block**

<br>
Below the welcome message, the user is asked to enter their name:

![User Enter Name](image-2.png)

To pass verification, the name entered must contain at least three characters, but more than 10 characters. If this verification test fails, the following message is displayed:

![Name Input  Enter Less Than 3 And More Than 10 Characters](image-1.png)

If the entered name is already in the Google spreadsheet, the application will prompt you to enter a new unique name:

![Selecting Name If There Repetition In Database](image-3.png)

After specifying a valid name, the user will be shown instructions for taking a psychological test:

![Instructions](image-4.png)

The next step is to show test questions where the user needs to answer “Yes” or “No”:

![Questions](image-5.png)

This is followed by checking the user's answer and if he answers other than "Y" or "N" then the following message appears:

![Checking Correctness Entered Answer](image-7.png)

After answering all questions, test results appear:

![Test Results](image-8.png)

If the user was not honest enough when answering, then the psychological test will reveal this and the program will show about this message. In this case, the test results are considered invalid:

![Results Not Valid](image-9.png)

Also, when testing is completed, a message appears indicating that testing is completed:

![Testing Сompleted](image-10.png)

<br>

## **Database**

The data is stored in a Google Sheets document and the app accesses it through the Google Drive and Google Sheets APIs. The table can be viewed [here](https://docs.google.com/spreadsheets/d/1hX7cJoDRUog7TXDuHcymWQj5D4xJEn-X63nRIaiNijA/edit#gid=0).  The spreadsheet consists of the following sheets:

### **Questions**

<br>

All questions that participate in testing are stored here. If necessary, you can update them:

![Questions Sheet](image-11.png)


### **User Page**

<br>

When passing the test, a separate tab with the user name is formed in the Google spreadsheet, and all information about the test results is also recorded here. This new data tab is created for each new user:

![User Page](image-12.png)


## **Error Handling**

<br>
As stated in the [Functionality and Features](#functionality-and-features) section, all user input is validated and any errors are handled gracefully so the user is kept aware of the problem and feedback is provided to help the user correct their error


## **Typography**

<br>

Consistent color schemes were used throughout the application to provide an intuitive user experience and ensure key information was highlighted. Green text informs the user that a value is required, red text marks user input errors and provides the user with information on how they can enter a valid value. Key information is highlighted in blue.

<br>

## **Imagery**

This project is deployed on Heroku and uses the Code Institute template to run the application in a mock terminal. I made some changes to the default html and css files to personalize the application and also to help the user immediately understand the purpose of the site: 

![Deployed Site Landing Page](image-13.png)

The following background image has been added to the css class 'body' in the layout.html file:

![Deployed Site Background Image](assets/img/psychology-background.webp)


I also added the following icon to the head element of the layout.html file:

![Favicon Image](image-14.png)

<br>

# **Technologies Used**

## **Languages Used**

<br>

Python was used to create this project.

<br>

## **Programs Used**

<br>

* Git -  Version control.
* [GitHub](https://github.com/) - All files for the website stored and saved in a repository.
* Gitpod - IDE used to write the code.
* [LucidChart](https://www.lucidchart.com/pages/) -For creating a flow diagram
* [Heroku](https://dashboard.heroku.com/apps) - For deployment of the project.
* [PEP8](https://pep8ci.herokuapp.com/) CI Python Linter
* [Cloudconvert](https://cloudconvert.com/jpg-to-webp) - For compression of image files to improve website performance.
* [UiDev](https://ui.dev/amiresponsive) - For generating an image of the deployed app on devices 

<br>
