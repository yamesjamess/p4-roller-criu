<h1 align="center">Roller Criú</h1>

[View the live project here](#)

![Roller Criú](documentation/support_images/#)

Brief description of the website

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

### As a user, I want to be able to :

1. 

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


* The inspiration for this application comes from [Elaine Broche's MS3 Event Scheduler](https://github.com/elainebroche-dev/ms3-event-scheduler) and [Alex Kavanagh's Grocery List Generator](https://github.com/alexkavanagh-dev/grocery_list_generator)









* All other content was written by the developer

### Achknowledgements
* Thank you to my wonderful mentor, Brian Macharia, for helping me during all phases of the project.

* Special thanks to Adam Lloyd