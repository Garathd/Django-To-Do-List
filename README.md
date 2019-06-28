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
- To be able to assign a project a Status and a Priority

User stories:

- As a user I want to be able to register an account
- As a user I want to be able to edit profile
- As a user I want to be able to update my account to pro version
- As a user I want to be able to create edit and delete projects and tasks
- As a user I want to be able to filter projects by Work, Educational or Personal
- As a user I want to be able to filter tasks by Priorities and Status

## Design

### Front-End

***Login/Register Pages*** These pages are more or less the same design wise. If there is an issue with either login or registration then a brief information message should appear on the screen. New users will be directed to the home page.

***Profile Page*** This page contains user profile information and lets users change their profile picture and description. This page also lets users purchase the pro version of the app.

***Dashboard Page*** This page shows the user both project and task information and also informs the user of their account type. Whether it is the pro version or the trial version of the app. Trial users will have an additional option to purchase the pro version of the app.

***Projects Page*** This page should only allow one project for a free user and unlimited projects for pro users. The page should also let users filter by project type and also options to edit Project and option to view Tasks for a specific project

***Project Info Page*** This page shows more project specific info as well as lets a user edit or delete a project

***Project Task Page*** This page shows all tasks associated with a specific project. It lets users edit, delete and create new tasks. The tasks on this page can be filtered by status and priority.

***Product Page*** This page contains Pro Version of the app. The page and code is setup in a way to only allow users to purchase the pro version only 1 time. If a user has a trial version of the app they will have the option to add to cart. If the product is added to the cart already then the add to cart button is replaced by an added button which redirects the user to the cart page. If the pro version is already bought the button is replaced by a purchased button which redirects a user back to their profile page

***Cart Page*** This page is only accessible if an item is in the cart otherwise it redirects back to the profile page. Also if an item is in the cart it should appear as a menu item. The cart page lets a user remove the item or else continue to the checkout

***Checkout Page*** This page lets the user purchase the pro version of the app using stripe. If there is no items in the cart then the user is redirected back to their profile page

### Back-End

For local testing i'm using sqlite and for live version I'm using Postgre SQL which comes as an add on with Heroku.

#### Accounts Model

***UserProfile***
- ***user*** : _This is a one to one field and is linked to the auth user model_
- ***description*** : _This is just a description of users bio info which is set from the profile page_
- ***picture*** : _This is for a user to upload an image from the profile page_
- ***account*** : _This is set to default as free and changes to pro when a user purchases the pro version_


#### Checkout Models

***Order***
- ***full name*** : _This is the name of the user_
- ***phone number*** : _This is the phone number of the user_
- ***country*** : _This is the country of the user_
- ***postcode*** : _This is the postcode of the user_
- ***city*** : _This is the city of the user_
- ***street address1*** : _This is the street address of the user_
- ***street address2*** : _This is the street address of the user_
- ***county*** : _This is the county of the user_
- ***date*** : _This is for the current date time at time of order_

***OrderLineItem***
- ***order*** : _This is a foreign key of previous model order_
- ***product*** : _This is a foreign key of the Product Model_
- ***quantity*** : _This is to store the amount of items ordered_


#### Product Model

***Product***
- ***name*** : _This is for product name_
- ***description*** : _This is for product description_
- ***price*** : _This is for product price_
- ***image*** : _This is for product image_


#### Project Model

***Project***
- ***name*** : _This is for project name_
- ***description*** : _This is for project description_
- ***status*** : _This is for the status. Choosen from either Work, Education or Personal_
- ***published date*** : _This is for the original project creation time_


#### Task Model

***Task***
- ***name*** : _This is for the task name_
- ***description*** : _This is for the task description_
- ***project*** : _This is a foreign key of Project_
- ***status*** : _This is for the status. Choosen from either To Do, In Progress or Done_
- ***priority*** : _This is for the status. Choosen from either Low, Medium or High_
- ***screenshot*** : _This is to allow users to upload a screenshot for a task_
- ***published date*** : _This is for the original task creation time_


## Features

The features of this application are as follows:

- Ability to Register, Sign Into and Logout of an Account
- Ability to Purchase Pro Version of the App using Credit Card Payments
- Ability to Create, Edit, Delete and View Projects (Pro Version)
- Ability to Create, Edit, Delete and View Tasks (Pro Version)
- Ability to Create, Edit, Delete and View 1 Project (Trial Version)
- Ability to Create, Edit, Delete and View 3 Tasks (Trial Version)
- Ability to Edit Profile Page and Upload User Image

## Features Left to Implement and Future Features

A feature I would like to implement in the future is for pro users to be able to invite users to a specific project and also assign them tasks.

## Technologies Used

### Python and Django

Django is the Python Framework I’m using for this application

### CSS

I'm using SCSS to build my css style sheets and probably a little unconventionally I'm using [Materialize](https://materializecss.com/) and also [Bootstrap 4](https://getbootstrap.com/). To be honest though it doesn't seem to have any adverse effects and over all looks better and is more responsive and visually pleasing out of the box when used together than individually. It was initially a mistake on my part but ended up looking pretty good. I also did a little research and decided to use the two of them after reading this [article](https://stackoverflow.com/questions/28613848/is-it-possible-to-integrate-materializecss-into-bootstrap). I also tried Material Design for bootstrap but wasn't happy with the way it looked

### JQuery

I have only used minimal JQuery. I have used it for the scroll to top button, the mobile menu and for select options for the forms in materialize.

### Gulp

Using Gulp to watch out for SCSS changes and converting SCSS to CSS

## Testing

### Manual Testing

For manual testing I have tested on the following browsers. *Firefox*, *Chrome*, *Edge* and *IE11*. I had to add some css fixes for both Microsoft Browsers.

I used an Alcatel U5 for mobile phone resolution testing and a Dell Inspiron 5567 for all other testing.

After running each possible scenario multiple times, going over each feature, user stories and client requirements I then validated my HTML and CSS using the following:

- [HTML Validation](https://www.freeformatter.com/html-validator.html)
- [CSS Validation](https://jigsaw.w3.org/css-validator/)

### Continuous Integration

For Continuous Integration I used Travis which constantly tests my app every time I push a new change to github

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

1. Create a new app
2. Install [PostgreSQL](https://elements.heroku.com/addons/heroku-postgresql)
3. Add PostgreSQL Database url to the config vars
4. Add Stripe Publishable and Secret Key to the config vars
5. Add AWS Secret Key and Access Key
6. Add Django Secret Key to the config vars
7. Restart all dynos
8. Go to Deploy > Deployment method and connect to github
9. Manual deploy the app with github master branch of selected project
10. Make sure Django Migrations are done and app is now deployed to heroku.

[Live App](https://milestone-project-5.herokuapp.com)


### Amazon S3 

This application uses Amazon S3 Buckets to host my static css and js files as well all user uploaded images.


## Content and Media

All Content and Media are uploaded by the users. Media content is up loaded to an Amazon S3 Bucket.

## Acknowledgements

- [Heroku PostgreSQL](https://elements.heroku.com/addons/heroku-postgresql)
