# Project: Code Institute January 2022 Hackathon with SODA Social: Mindfulness and Wellbeing

![](assets/images/jan-2022-hackathon-image.png)

# Team: 09

# Table of Contents

## Introduction

This website is a project for Code Institute's January 2022 Hackathon, hosted in collaboration with digital recruitment firm SODA and their networking event SODA Social. The theme of the Hackathon was mindfulness and wellbeing in the workplace. 

The website was created by Naoise Gaffney, Marina Pavlovic, Goran Kuzma, Eva Kuk and Adam Boley, with the project facilitated by Aisha Bushell

The aim of the project is to help digital workers - those working in offices and those working from home - maintain their wellbeing and mindfulness whilst working. When working in an office, workers are often sitting down for long periods, and may not have particularly ergonomic workstations. Those working from home face these issues as well, and more besides - when working from home, it is all too easy for work time to spill over into personal time, with workers constantly in "work-mode", and unable to switch off from work. 

Thus, the website's main features are several timers that are activated at the start of the day. Each timer counts down from a fixed value, and when it expires, it flashes up a message and plays a soft audio tune to alert the user. The message reminds the user to do one of several tasks - drink some water, do some breathing exercises, do some stretching, eat lunch, go for a walk and finally stop work. The idea is to break up the user's day and try to prevent burnout by giving their brain a break. The message to stop work should stop users from working more than their hours and protect their personal time, allowing them to relax and rest


# User Experience

## User Stories


### Site Owner goals


### All Visitor Goals


### First Time Visitor Goals


### Returning Visitor Goals


# Design
## Surface

**Colour Scheme**

We have chosen for the website colours: blue, turquoise and green which are often described as peaceful and stress relief  and are associated with balance and **emotional stability**.

Referring to the colour psychology websites [very well mind](https://www.verywellmind.com/color-psychology-green-2795817) and [graf1x](https://graf1x.com/color-psychology-emotion-meaning-poster/)  

**Blue** calls to mind feelings of **calmness** or serenity and peace. It is often described as peaceful, tranquil, secure, and orderly. It is used to **reduce to stress**, create calmness and relax 

Blue is often used to decorate offices because research has shown that people are more productive in blue rooms. 

**Green** is the colour of growth and **health**. Green has strong association as a **refreshing** and **peaceful colour**. 

Green is the colour of nature and has a calming effect and is often considered relaxing and refreshing colour has been found to influence not only our emotions but our memories. One study provided a group of people with a list of emotionally charged words written in different colours. Therefore, the colour green might give us an optimism bias when it comes to remembering information.

**Turquoise** is a shade of blue that lies on the scale between blue and green. It has characteristics associated with both of these, such as the **calmness** of blue and the **growth** that is represented in green. Turquoise can also has the energy that yellow transmits, becoming an uplifting colour.

The colour turquoise is associated with meanings of refreshing, feminine, calming, sophisticated, energy, wisdom, serenity, wholeness, **creativity**, **emotional balance**, spiritual grounding, friendship.

Turquoise is linked to calmness, serenity and peace of mind, as well as to **mental clarity**.

Turquoise encourages creativity. It is a colour linked to the ocean. It is also associated with balance and **emotional stability**. Turquoise has the characteristics of blue, green and yellow.

![colour scheme palette](/static/images/proposed-color-scheme-1.png)

# Wireframes

The Balsamiq Wireframes app was used to create the initial wireframes and update them through the creation of the project 

Home page

Planner page

Register page

Sign up page

Resources page



# Technologies

[Github](https://github.com/): Adam Boley's Github was used to host the main project files and folders. Other team members then forked to their repositories. 

[Gitpod](https://gitpod.com/): Most team members used the Gitpod IDE to create and edit the project files. Other team members preferred Visual Studio Code.

[Flask](https://palletsprojects.com/p/flask/): Flask was used to create a framework for the project.

[Flask User](https://flask-user.readthedocs.io/en/latest/): Flask User was used to create the registration and login functionality

[Slack](https://slack.com/intl/en-gb/): Slack was used to communicate and coordinate the actions of team members, share screenshots, and join video calls to discuss the project

[Google Docs](https://www.google.com/docs/about/): Google Docs was used to create and edit a shared document to note down ideas. 


# Testing

## Manual Testing

## Testing Site Owner Goals

## Testing All Visitor Goals

## Testing First Time Visitor Goals

## Testing Returning Visitor Goals

## Validation Testing


# Deployment
## Local Deployment

To run this project locally make sure you have installed the following:

- an IDE of your choice (such as Gitpod, VS Code, etc.)
- have the following installed:
    - [Git](https://git-scm.com/)
    - [Python3](https://www.python.org/downloads/)
    - [PIP](https://pypi.org/project/pip/)

### Clone the GitHub Repository

To clone this project and run locally please follow the below steps:
1. Login into GitHub with your account
2. Go to the [project repository](https://github.com/AdamBoley/January-2022-Hackathon) **URL NEEDS TO BE UPDATED**
3. If using Gitpod click on the "Code" button (located next to the green "Gitpod" button)
4. From the dropdown menu copy the HTTPS URL
5. In your local IDE open the terminal
6. Change your working directory to the location where you want the cloned project saved
7. Type `git clone` and paste copied URL from Step 4
8. Press enter to create your local clone

### Install project dependencies
- Install project requirements by typing `pip install -r requirements.txt`

### Create a database on MongoDB

Register for a free account with [MongoDB](https://account.mongodb.com/account/register)

- Create a new Project and call it 'mindful timer'
- Create a Cluster, choose the free tier option and select your region
- Create a new database and call it 'mindfultimer_db'
- Create Collections named **TBA**

### Deploy locally
- To run the project locally, in the terminal type `python3 app.py`
- This will open a localhost address, which is provided in the CLI
- Either copy and paste the url into a new browser tab, or hover over it and click the link

### Deploy to Heroku

The website of this project requires back-end technologies such as server, application, and database so the website is deployed on [Heroku](https://www.heroku.com/), which is a cloud platform with a service supporting several programming languages, because GitHub can only host a static websites.

Before deploying the website to Heroku, there are three important steps to follow to make the application work in Heroku correctly.

1. Create `requirements.txt` file that contains the names of packages being used in Python. It is important to update the file if other packages or modules are installed during the project.
2. Create `Procfile` that contains the name of the application file so that Heroku knows what to run.
3. Push them into GitHub.

Once above steps have been followed the website can be deployed. Please find the steps of the deployment in Heroku:

1. Create an account in [Heroku](https://signup.heroku.com/login)
2. Click **New** & **Create new app** to create a new app
3. Put an app name, which must be unique, choose a region and click create app
4. Go to **Deploy** section and click **Connect to GitHub**
5. Search for the repository by the repository name and connect it
6. Before clicking Enable Automatic Deploys, hidden variables such as IP address, PORT, SECRET_KEY, MONGO_URI and MONGO_DATABASE need to be recorded in Heroku. Go to **Settings**, click **Reveal Config Vars** and fill out necessary keys and values.
7. Once all the hidden variables are recorded, then click **Enable Automatic Deploys** and click **Deploy Branch** (Main should be selected unless you want other branches to be deployed).
8. When the app is deployed by Heroku correctly, there is a confirmation message and you can access the app.

**Note**<br>
*It is important NOT to set `debug=True` when deploying the website.*


# Credits

## Acknowledgements

The team: 
- [Naoise Gaffney](https://github.com/NaoiseGaffney)

- [Marina Pavlovic](https://github.com/FruitbatM)

- [Goran Kuzma](https://github.com/kuzGo)

- [Eva Kuk](https://github.com/Eva-Kuk)

- [Adam Boley](https://github.com/AdamBoley)

Our Facilitator, Aisha Bushell






## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------


