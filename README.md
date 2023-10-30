<h1 align="center">Roller Criú</h1>

[View the live project here](https://roller-criu-54a9c256735c.herokuapp.com/)

![Roller Criú](documentation/support_images/roller_criu_main.png)

Roller Criú is a website for a fictional roller skating school based in Cork, Co. Cork, Ireland.

Guest users can visit the website and view the lists of lessons available, the About page that displays the details of Roller Criú, or submit a contact form if they want to send a message. 

If the Guest users want to access more functionality such as: like/unlike lessons, submit a booking request, view and manage their bookings. The user must be registered and logged in to access those functions.

## Table of Contents
---
* [User Experience](#user-experience)
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience
---

### User Stories :

* USER STORY (#1) : Gather ideas and general requirements for the project.
  * As a **developer**, I can **visualise how the website should be designed**, so that **the website gets developed methodically**.

* USER STORY (#2) : Intial Django project setup
  * As a **developer**, I can **set up the developing environment and deploy to Heroku**, so that **I can solve any deployment issue that arises early on**.
* USER STORY (#3) : Create bootstrap template
  * As a **developer**, I can **create an essential website using Bootstrap**, so that **it meets my site's requirements**.
* USER STORY (#4) : Demonstrate the application's purpose using its user interface
  * As a **Site User**, I can **visit the website**, so that **I can understand and determine the purpose of the website**.
* USER STORY (#5) : Navigate site
  * As a **Site user**, I can **navigate the website using the menu**, so that **I can easily access the website's funcationality**.
* USER STORY (#6) : View lessons list
  * As a **Site User**, I can **view a list of lessons**, so that **I can select on to access for more details**.
* USER STORY (#7) : View lesson information
  * As a **Site User**, I can **click on a lesson**, so that **I can view the full details of the lesson**.
* USER STORY (#8) : Book a lesson
  * As a **Site User**, I can **submit a lesson booking request**, so that **a place reserved for me**.
* USER STORY (#9) : View booked lessons
  * As a **Site user**, I can **access the list of lessons that I have sent a booking request**, so that **I can see if my lessons has been approved or not**.
* USER STORY (#10) : Cancel a lesson booking
  * As a **Site user**, I can **cancel a lesson booking request**, so that **the place is no longer reserved for me**.
* USER STORY (#11) : View likes on a lesson
  * As a **Site User**, I can **view the number of likes on each lesson**, so that **I can see which is the most popular**.
* USER STORY (#12) : Like / Unlike a lesson
  * As a **Site User**, I can **like or unlike a lesson**, so that **I can give quick feedback on my experience**.
* USER STORY (#13) : Feedback on a lesson
  * As a **Site User**, I can **leave feedback on the lesson**, so that **give more detailed feedback on my experience**.
* USER STORY (#14) : View feedback
  * As a **Site user**, I can **view feedback on individual lessons**, so that **I can use the feedback to help me make a decision to submit a booking request or not**.
* USER STORY (#15) : Approve/Not Approve feedback
  * As a **Site Admin**, I can **approve or not approve feedback**, so that **I can filter out unsuitable or objectionable feedback**.
* USER STORY (#16) : Create lesson draft
  * As a **Site Admin**, I can **create a draft for a lesson**, so that **I can come back to finish writing the lesson details later**.
* USER STORY (#17) : Manage Lesson
  * As a **Site Admin**, I can **create, read, update and delete lessons**, so that **I can manage lesson availability and site's content**.
* USER STORY (#18) : Account registration & Login
  * As a **Site user**, I can **register an account**, so that **I can log in to book, leave feedback, and/or like a lesson**.
* USER STORY (#19) : Manage Coach
  * As a **Site Admin**, I can **create, read, update and delete coaches**, so that **I can manage coaches content**.
* USER STORY (#20) : Create coach draft
  * As a **Site Admin**, I can **create a draft for a coach**, so that **I can come back to finish writing the class details later**.
* USER STORY (#21) : Approve bookings
  * As a **Site Admin**, I can **review and approve or disapprove a booking request**, so that **I can manage the capacity of the lesson**.
* USER STORY (#22) : View Contact Form
  * As a **Site User**, I can **visit the contact form page**, so that **I can fill out the form to submit my message**.


## Features
---

### Existing Features

1. 

### Feature that could be implemented in the future

1. 

## Design
---

* Lucidchart: 

## Technologies Used
---

### Languages Used

* [Python 3.11.1](https://www.python.org/downloads/release/python-3111/)

### Frameworks, Libraries & Programs Used

* [Lucidchart](https://www.lucidchart.com/pages/): Used to create a flowchart during the design and planning stage. Outline what function is needed for the program.

* [Git](https://git-scm.com/): was used for version controlling purposes through git commands via the terminal on GitPod and is pushed to GitHub for cloud-based storage.

* [GitHub](https://github.com/): is used to host the repository of the project.

* [Heroku](https://heroku.com): is used to host and deploy the program.

## Testing
---

### Validator Testing

* [CI Python Linter](https://pep8ci.herokuapp.com/)

    - result for run.py

    ![Python Validator Results](documentation/validation_results/python_validator_result.png)

### Test Cases and Results

* The table below details the testing case that was used and the result of the test.

### Known Bugs

### Unfixed Bugs
* There are no unfixed bugs that the developer is aware of.

## Deployment
---

### How to clone this repository
* Visit the main repository at https://github.com/yamesjamess/p4-roller-criu.

* Click the "Code" button to the right of the screen, click HTTPs and copy the link present there.

* Open a GitBash terminal and navigate to the directory where you want to clone.

* In the terminal, type "git clone" then paste in the copied URL and press the Enter key to begin the cloning process.

### How to fork this repository
* Visit the main repository at https://github.com/yamesjamess/p4-roller-criu.

* On the top right-hand corner click on the "Fork" button.

* You will be redirected to a new page, from there enter the name you desire the name the forked repository and click "Create Fork"

* You will now have a Fork copy of the repository on your own repository.

### How to deploy the program on Heroku

__Steps to deploy the project on Heroku__

* Update the requirements.txt file by following the following steps.
    * Enter 'pip3 freeze > requirements.txt' into the terminal and press Enter
    * Once the IDE finishes updating the file, commit it to git and push it to GitHub.
* Log in to [Heroku](https://www.heroku.com/)
    * Heroku account is required.
* From the dashboard, click "New" to create a new application.
* Enter an app name, for this project it will be roller-criu and select the appropriate region. Then click the Create App button
* On the next page, go to the Settings tab and go to the Config Vars section.
* To create a new Config Vars, press Reveal Config Vars, and fill in the KEY and VALUE fields.
    * In the KEY field, enter 'CREDS' and in the VALUE field, copy and paste all the code from the creds.json file into the field. Then press Add.
    * In the next KEY and VALUE fields, enter 'PORT' and '8000' respectively.
* Scroll down to the Buildpacks section and click Add buildpacks.
    * Select Python from the options and click Save Changes.
    * Click Add Buildpacks again, and this time select nodejs and click Save Changes.
    * Make sure that in the buildpacks list, Python is on the top and nodejs is below.
* Go to the Deploy tab
* Select GitHub as the deployment method and connect to your GitHub account.
* Search for the name of the repository, for this project it's [https://github.com/yamesjamess/p4-roller-criu](https://github.com/yamesjamess/p4-roller-criu), and click Connect to link the repository to Heroku.
* Scroll down and select either Automatic Deploys or Manual Deploys.
    * Automatic deploys will automatically build your application every time new changes are pushed to GitHub
    * Manual deploys allow you to deploy your project manually
    * For this project, the Automatic deployment method was selected.
* The application can be run by clicking the Open app button.
* The live project can be viewed [here](#).

## Credits
---

### Contents

* All other content was written by the developer

### Achknowledgements
* Thank you to my wonderful mentor, Brian Macharia, for helping me during all phases of the project.

* Special thanks to Adam Lloyd