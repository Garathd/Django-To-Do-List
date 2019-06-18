[![Build Status](https://travis-ci.org/Garathd/django-project.svg?branch=master)](https://travis-ci.org/Garathd/django-project)

# Trackx

This project was inspired by the constant paper To Do lists that I seem to have lying around the house. I thought it might be good to create something that can categorize various tasks and projects to make my workflow more efficient. Tasks have status's and and priority to help figure out which task is the most important

## UX Design

My UX process was to analyze what I thought would streamline my original paper to do list and try to develop this into a user friendly website that is easy to navigate

The requirements are:

- To be able to register different users and create accounts
- To be able to view and edit user profile.
- To be able to purchase a pro version of the app
- For a trial user to be only able to create 1 project and 3 tasks
- To be able to to create, edit and delete a project
- To be able to create, edit and delete a task
- To be able to assign a projects type as Work, Educational or Personal
- To be able to search  projects by Work, Educational or Personal
- To be able to view only the tasks for a specific project
- To be able to search tasks by High, Medium or Low Priority as well as To Do, In Progress and Done(Not sure about Done just yet)
- To be able to assign a project a Job, A Status and a Priority

User stories:

- As a user I want to be able to register an account
- As a user I want to be able to edit profile
- As a user I want to be able to update my account to pro version
- As a user I want to be able to create edit and delete projects and tasks
- As a user I want to be able to filter projects by Work, Educational or Personal
- As a user I want to be able to filter tasks by Priorities and Status

## Design

### Front-End

### Back-End

For local testing i'm using sqlite and for live version I'm using Postgre SQL as an add with Heroku
Not to sure what else to add here for now


## Features

## Features Left to Implement and Future Features

At the moment this application only caters to myself as the nature of this project is essentially a task and project management system that is for me to keep track on what I need to do. 

In the future I hope to have additional users that can be setup to different projects as groups of users.

Also a feature I just thought of could be good maybe upload a screenshot for a task and install pillow

## Technologies Used

### Python and Django

Django is the Python Framework I’m using for this application

### CSS

Im using Bootstrap for my CSS but i'm thinking I should look more into using Materialize in conjunction with Bootstrap 4

### JQuery

Using Minimal at the moment should really style this up a bit better

### Gulp

Will be using this to convert SCSS to CSS

## Testing

### Manual Testing

For manual testing I have tested on the following browsers. *Firefox*, *Chrome*, *Edge* and *IE11*. I had to add some css fixes for both Microsoft Browsers.

I used an Alcatel U5 for mobile phone resolution testing and a Dell Inspiron 5567 for all other testing.

After running each possible scenario multiple times, going over each feature, user stories and client requirements I then validated my HTML and CSS using the following:

- [HTML Validation](https://www.freeformatter.com/html-validator.html)
- [CSS Validation](https://jigsaw.w3.org/css-validator/)

### Unit Testing

This project has 24 Unit Tests overall. Tests can be run in terminal with the following command: "python3 manage.py test".
Each app has associated tests. The first app is the accounts app, so to run tests on this app the command would be: "python3 manage.py test accounts" 

#### Acounts App Testing ####

- ***Test Login Form***: This tests the login form validation

- ***Test Registration Form***: This tests the registration form validation

- ***Test User Profile Form***: This tests the user profile form validation

- ***Test User Profile Model***: This tests the user profile models

- ***Test Register View***: This tests if a user can access the register page and if the page gets a http 200 response and then checks the if template was used.

- ***Test Login View***: This tests if a user can access the login page and if the page gets a http 200 response and then checks the if template was used.

- ***Test Profile View***: This tests if a user can access the profile page and if the page gets a http 200 response and then checks the if template was used.

- ***Test Edit Profile View***: This tests if a user can access the edit profile page and if the page gets a http 200 response and then checks the if template was used.


####  Cart App Testing ####

- ***Test Cart View***: This tests if the cart is empty and if the page gets a http 302 response if the user navigates to the cart page 


####  Checkout App Testing ####

- ***Test Checkout View***: This tests if the cart is empty and if the page gets a http 302 response if the user navigates to the checkout page

- ***Test Order Form***: This tests the customer order form validation

- ***Test Order Model***: This tests the order model


####  Dashboard App Testing ####

- ***Test Dashboard View***: This tests to see if a logged in user can access the dashboard and the page and if the page gets a http 200 response and if the template was used


####  Home App Testing ####

- ***Test Home Logged In View***: This tests to see if a logged in user can access the dashboard and the page gets a http 200 response and checks if the template was used

- ***Test Home Not Logged In View***: This tests to see if a non logged in user can access the dashboard and if the page gets a http 302 response and checks if the template was not used


####  Products App Testing ####

- ***Test Product View***: This tests to see if a user can access the products page and if the page gets a http 200 response and checks if the template was used

- ***Test Product Model***: This tests the Product Model


####  Projects App Testing ####

- ***Test Project Form***: This tests the project form validation

- ***Test Project Model***: This tests the project model

- ***Test Project View***: This tests to see if a user can access the projects page and if the page gets a http 200 response and then checks if the template was used

- ***Test Project Info View***: This tests first creates a new project and then navigates to the project info page and checks if the page gets a http 200 response and then checks if the template was used

- ***Test View Only View***: This tests first creates a new project and then navigates to the tasks view url associated with the newly created project and then checks if the page gets a http 200 response and then checks if the template was used


####  Tasks App Testing ####

- ***Test Task Form***: This tests the task form validation

- ***Test Task Model***: This tests the task model by creating both a new project and associated task



## Deployment

### Heroku Deployment Steps

DEFAULT STEPS: NEED TO CHANGE THIS AND EXPAND AND MENTION MANUAL DEPLOYMENT FOR LIVE SITE!!!!!!!!

1. Go to the Heroku Website and create new app
2. Create requirements.txt and Procfile to tell heroku what is required to run the app
3. Login into Heroku Account via command line and add the newly created app
4. Go back to Heroku Website and in the settings tab click *Reveal Config Vars* and add IP and PORT vars from Project Config
5. Install [ClearDB](https://elements.heroku.com/addons/cleardb) and import local MySQL Database dump.sql
5. Restart all dynos
6. Finally do an initial git commit and push to heroku

### AWS Static Website Stuff

Mention this in more detail


## Content and Media

## Acknowledgements
