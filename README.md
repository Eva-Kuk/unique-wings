Milestone 4 Unique Wings Shoes - by Eva Kukla

![althomepage](static/images/logo.png)

- [Overview](#overview)

- [User stories](#user-stories)

- [UX](#ux)

  - [Strategy](#strategy)

  - [Scope](#scope)

  - [Structure](#structure)

  - [Skeleton](#skeleton)
  
  - [Surface](#surface)


- [Features](#features)

- [Technologies used](#technologies-used)

- [Resources](#resources)

- [Testing](#testing)

- [Code validity](#code-validity)

- [Version Control](#version-control)

- [Deployment](#deployment)

  - [Database Deployment](#database-deployment)

  - [Deployment Platform](#deployment-platform)

- [Credits](#credits)

- [Acknowledgments](#acknowledgments)


## Demo

---

![altamiresponsive](wireframes/readme/am-i-responsive.jpg)


- A live demo can be found [here](https://eva-kuk.github.io/unique-wings/)

- A github repository can be found [here]()


## Overview
This is my fourth of Milestone Project 4 which is part of the Code Institute's FullStack Software Development Diploma Course and the main requirements is to build a full-stack website based around busines logic used to control a centtrally-owned dataset which contain set up an authentication access mechanism and provide paid access to the site's data andpurchase of the product.

This project demonstrates the skills and knowledge of using the HTML5, CSS3, JavaScript, Python, Django, Relational database Poistgres and Stripe payments in Back-End development which I have learned recently on the course.

The aim of this project is to create an e-commerce web application name **Unique Wings** for women who love shoes and are interested in extraordinary and unusual shoes. They will be able to find and purchase those unique shoes from various amazing designers in one place. The project is for educational purposes only.

Users can search for and purchase unique shoes via text search, designers or categories.

Users can create an account to save delivery information for future use, review their orders and logged in users are also able to leave revives on shoes.

???
A user can subscribe and have a 30%  on the first purchase

The owner/administrator of the shop  (with the appropriate access) can add, edit and delete products, and create news posts for keeping their members up to date with latest information.

---


## User stories

---
**Viewing and navigation**

| User Story ID | AS a/an                     | I want to be able to ...                                   | So that I can ...                                            |
| ------------- | --------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| 1.            | new user                    | recognise the purpose of the site immediately              | identify whether I am interested in the content and wish to use the site |
| 2.            | new user                    | easily navigate the site                                   | find what I need effectively                                 |
| 3.            | new user                    | to access the website on a desktop and also mobile devices | use it on a desktop or on the go                             |
| 4.            | general visitor             | to contact the website owner                               | make about the product, purchase, return policy              |
| 5.            | general user                | to read some information about shoe designers              | get to know their brand better                               |
| 6.            | general user                | view blogs                                                 | get new information's about the shop, designers              |
| 7.            | new user and future shopper | view a list of shoes                                       | find which shoes I'd like to purchase                        |
| 8.            | new user and future shopper | view individual shoe details                               | identify the price, description, shoes rating,  image and available sizes before deciding to purchase. |
| 9.            | new user and future shopper | quickly identify sales, pomotions and special offers       | take advantage of special savings on products I'd like to purchase |
| 10.           | new user and future shopper | easily view the total of my purchases at any time          | avoid spending too much                                      |


**Registration and User Accounts**       

| **User Story ID** | **AS a/an**                 | **I want to be able to ...**                    | **So that I can ...**                                        |
| ----------------- | --------------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| 11.               | new user and future shopper | easily register for an account                  | have a personal account and be able to view my profile       |
| 12.               | registered user             | easily login/out                                | access my personal account information                       |
| 13.               | registered user             | easily reset my password in case I forget it    | recover  access to my account if I have forgotten my password |
| 14                | registered user             | receive an email confirmation after registering | verify that my account registration was succesful            |
| 15                | registered user             | have a customized dashboard                     | view my personal order history and order confirmation, and save my payment information |

**Sorting and searching**      

| **User Story ID** | **AS a/an** | **I want to be able to ...**                                | **So that I can ...**                                        |
| ----------------- | ----------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| 16.               | Shopper     | sort the list of available shoes                            | easily identify the best rated, best priced and categorically sorted products |
| 17.               | Shopper     | sort a specific category of shoes depending on the designer | find the best-priced or best-rated shoes in a specific designer category, or sort the shoes in that category |
| 18.               | Shopper     | sort multiple categories of shoes simultaneously            | find the best-priced or best-rated product across broad categories, such as "high hills" , "flats", "boots" |
| 19.               | Shopper     | search for a product by name or description                 | Find a specific product I'd like to purchase                 |
| 20.               | Shopper     | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available       |


**Purchasing the checkout**

| **User Story ID** | **AS a/an** | **I want to be able to ...**                                 | **So that I can ...**                                        |
| ----------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 21.               | shopper     | easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
| 22.               | shopper     | view details about the items in my shopping bag              | decide if I want to purchase an item or edit it              |
| 23.               | shopper     | easily add, edit & delete items in my shopping bag           | adjust my total to fit into my budget                        |
| 24.               | shopper     | revisit my shopping cart after logging in and logging out    | complete my purchase without re-adding every single item     |
| 25.               | shopper     | checkout using credit/debit card                             | purchase chosen products                                     |
| 26.               | shopper     | receive my digital order via email                           | access the item I just purchased                             |

**Navigation**  

| **User Story ID** | **AS a/an** | **I want to be able to ...**                         | **So that I can ...**              |
| ----------------- | ----------- | ---------------------------------------------------- | ---------------------------------- |
| 27.               | site owner  | access product management from the homepage          | access my account                  |
| 28.               | site owner  | access my dashboard from the homepage                | return to my dashboard at any time |
| 29.               | site owner  | receive a notification when there is a pending order | know when I am making money        |

**Product management**

| **User Story ID** | **AS a/an** | **I want to be able to ...**                                | **So that I can ...**                                        |
| ----------------- | ----------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| 30.               | site owner  | add new products                                            | add new items to my online store                             |
| 31.               | site owner  | edit/update products                                        | update products prices, descriptions, images and other product criteria |
| 32.               | site owner  | delete products                                             | remove erroneous products or products that are no longer available |
| 33.               | site owner  | preview & verify new products before submitting to the shop | check for correct description, grammatical errors and mistakes |
| 35.               | site owner  | add, edit, delete blog post                                 | add new posts to their blog                                  |
| 36.               | site owner  | Edit/Update a blog post                                     | change post name, content, and image                         |
| 37.               | site owner  | Delete a blog post                                          | remove a blog post                                           |
| 38.               | site owner  | make a draft blog post                                      | work on a blog post before letting it be viewable to the website visitors |


 **Authentication & account**    

 | **User Story ID** | **AS a/an** | **I want to be able to ...**           | **So that I can ...**                      |
| ----------------- | ----------- | -------------------------------------- | ------------------------------------------ |
| 39.               | site owner  | verify my email address                | set up my account securely                 |
| 40.               | site owner  | update my account information          | maintain access to my account              |
| 41.               | site owner  | logout when I am finished with my work | logoutof my account                        |
| 42.               | site owner  | reset my password                      | recover my account or upgrade its security |


## UX 
(5 planes)

---
1. ## Strategy

**Project purpose:**


**Site owner goals:**

**Customer Goals:**


2. ## Scope

**Functional Requirements**


**Content Requirements**



3. ## Structure



**FRONT END**


**BACK END**


4. ## Skeleton

**Wireframe mockups:**


5. ## Surface

**Colors**

 **Typography**

 **Images**


## Features

---



## Technologies Used

**1. Languages**

-  ![html5](wireframes/readme/html5.png) – [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)

-  ![css3](wireframes/readme/css3.png)- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)

-  ![python](wireframes/readme/python.png) - [Python](https://www.python.org/)

-  ![javascript](wireframes/readme/js.png) – [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)


**2. Integrations**

-  ![django](wireframes/readme/django.png) - [django](https://www.djangoproject.com/)  website creating framework software.

-  ![stripe](wireframes/readme/stripe.jpg) [stripe]( https://balsamiq.com/) - a secure processing payment platform.


-  ![bootstrap](wireframes/readme/bootstrap.png) – [bootstrap](https://getbootstrap.com/)  CSS framework directed at responsive, mobile-first front-end web development

-  ![fontawesome](wireframes//readme/font-awesome.png) - [Font Awesome](https://fontawesome.com/) is the source of all icons.

-  ![googlefonts](wireframes/readme/google-fonts.png) - [Google Fonts](https://fonts.google.com/) used on the website courtesy of Google Fonts

-  ![jquery](wireframes/readme/jquery.png) - [jQuery](https://jquery.com/) The project uses JQuery to simplify DOM manipulation.

**3.Version Control, database and hosting**

-  ![gitpod](wireframes/readme/gitpod.png) - [Gitpod](https://www.gitpod.io/) Main workspace IDE (Integrated Development Environment)

-  ![gitversioncontrol](wireframes/readme/git-version-control.png) – [Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control ) Distributed Version Control tool to store versions of files and track changes.

-  ![github](wireframes/readme/github.png) - [GitHub](https://wikipedia.org/wiki/GitHub) Used to store the project repository and deploy the site via github pages.

- ![heroku](wireframes/readme/heroku.png) - [Heroku](https://www.heroku.com/what) was used in order to deploy the website

- ![aws](wireframes/readme/aws.png) - [Amazon Web Services](https://en.wikipedia.org/wiki/Amazon_Web_Services) a cloud platform and hosting website

- ![PostgreSQL](wireframes/readme/postgresql.png) - [PostgreSql](https://www.postgresql.org/) PostgreSQL is an object-relational database system 


**4.Editors**

-  ![typora](wireframes/readme/typora.png) - [Typora]( https://typora.io/) was used to simplify creation of the README.md file.

-  ![dbdiagram](wireframes/readme/dbdiagram.png) - [dbdiagram]( https://dbdiagram.io/home) was used to create Entity Relationship Diagrams of the database.

-  ![balsamiq](wireframes/readme/balsamiq.png) [balsamiq]( https://balsamiq.com/) - Wireframing design tool to create wireframes.

**5. Tools Used**
Red Ketchup
- [Colors](https://coolors.co/) - color schemes generator.
- [TinyPNG](https://tinypng.com/) - Efficient compression of images for site.
- [RedKetchup](https://redketchup.io/) - to convert an image into a favicon and edit icons for used technologies.

**5. IDE Extensions used in GitPod**

- Auto Close Tag

- Prettier - Code Formatter

- Bracket Pair Colorizer

- Code spell Checker

- Font Awesome Auto-complete


**6. Other**


## Resources

---

## Testing

- Click [here](TESTING.md) for the full testing process.


Overview

- [Encountered Issues](TESTING.md#encountered-issues)

- [Code Validation](TESTING.md#code-validation)

- [Testing User stories](TESTING.md#testing-user-stories)

- [Testing Functionality](TESTING.md#testing-functionality)

- [Testing Compatibility](TESTING.md#testing-compatibility)

- [Testing Accessibility](TESTING.md#testing-accessibility)

- [Testing Performance](TESTING.md#testing-performance)

- [Further Testing](TESTING.md#further-testing)

---

## Code validity

- HTML - [Markup Validation W3C Service](https://validator.w3.org/)

- CSS - [Jigsaw Validation W3C Service](https://jigsaw.w3.org/css-validator/)

- JSHint - [JSHint for detecting errors in JavaScript code](https://jshint.com/)

- Link checker - [Check links and anchors in Web pages or full Web sites](https://validator.w3.org/checklink)
- PEP8 - [PEP8](http://pep8online.com/) check code for code requirements

- Lighthouse in Google dev tool for testing the performance of the website


## Version Control

[Git](https://git-scm.com/) as a local repository and [GitHub](https://github.com/) as a remote repository are used for the project, and below is how I use them as the version control for the project.


**- - Setting Up New Repository - -**

1. Create a remote repository in GitHub by clicking "New repository" on the main page

![new repository](wireframes/readme/new-repository.png)

2. Use Code Institute Template, put the repository name and click Create Repository **making sure to select public**

![repository template](wireframes/readme/repository-template.png)

![public](wireframes/readme/public.png)

![create-repository](wireframes/readme/create-repository.png)

3. Open the repository with Gitpod which is my Integrated Development Environment (IDE). 

![opengitpod](wireframes/readme/open-gitpod.png)



**- - Commitments - -**


When a section or even a group of work is completed, it is committed in git and pushed into GitHub, to make sure to keep the history of the work logged properly and not to lose the work in unexpected situations. Below commands are used for this.

```
 - git status | we use to check the status of new/modified folders, files, and documents
```


```
- git add -A | we use to put all new and updated work on the stage in git
```

```
 - git add <specific file name> | we use when different types of work is done but do not want to commit everything on the same commitment
```

```
 - git commit -m "Example commit" | To commit the work on the stage in git before pushing it to GitHub
```

```
 - git push | we use to update the repository in GitHub for main branch
```

```
 - git push origin <branch name> | we use when pushing git into GitHub for sub-branches
```

 ** - - Branches - -**

When some testing is needed, create a branch and test is on it instead of using main branch. When the testing is successful, then merge the branch into main, when it is not, leave the branch unmerged and keep working on main branch. Below commands are used for this.

```
* git branch <branch name> | To create a new branch
```

```
* git checkout <branch name> | To switch branch
```

```
* git branch | To check current branch
```

```
* git merge <branch name> | To merge sub-branch into main, do this on main branch
```

### **To fork the GitHub Repository**

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without

affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [Repository](https://github.com/Eva-Kuk/smoothie-lovers).

2. At the top right of the Repository just above the "Settings" Button on the menu, locate and click the "Fork" Button.

3. You should have a copy of the original repository in your GitHub account now.


### **To make a Local Clone**

1. Log in GitHub and locate the [Repository](https://github.com/Eva-Kuk/smoothie-lovers).

2. At the top of the Repository locate the "Code" dropdown menu.

3. To clone the repository using HTTPS, under "CLONE", make sure "HTTPS" is selected and copy the link then.
4. Open Git Bash.

Change the current working directory to the location where you want the cloned directory to be made.

5. Type `git clone` and past the URL you copied in Step 3.

```
$ git clone https://github.com/Eva-Kuk/smoothie-lovers
```

6. Press Enter and you local clone will be created.


## Deployment
The application project requires back-end technologies such as server, application, and database so it was deployed using [Heroku](https://dashboard.heroku.com/apps) which is a cloud platforn with a service supporting several programming languages including python. GitHub can only host a static website. There are two ways to deploy a website in Heroku. One is to use Heroku Command Line Interface (CLI) by using a  command: `heroku login` or `heroku login -i` and another one is to connect to GitHub repository by Heroku.This is deploying by Connecting to GitHub repository. 

### **Requirements**
 
- AWS cloud storage and an S3 bucket for online backup of static files.
- [Stripe Account](https://dashboard.stripe.com/register) (account, test keys and webhooks) as a secure payment platform.
- an IDE, I used GitPod.
- PIP, for Python packages.
- Python3
- Git for version control.
- Email account, I used Gmail.

1. First we need to install gunicorn which will act as our webserver

    `pip3 install gunicorn`

2. Create `requirements.txt` file which contains the names of packages being used in Python. It is important to update the file if other packages or modules are installed during the project.

    `pip3 freeze > reqiurements.txt`

3. Create `Procfile` which contains the name of the application file so that Heroku knows what to run: unicorn and serve our django app. Use the following command:

  `web: gunicorn unique-wings.wsgi:application`

Procfile may have a blank line when it is created so remove it as it may cause problems. 

4. Push both files to GitHub.

### Deployment Platform
1. Go to [Heroku](https://dashboard.heroku.com/apps) and login or create and account.

2. Click **New** and choose from dropdown menu **Create new app** to create a new app

![heroku new app](wireframes/readme/heroku-new-app.png)

3. Enter an **App name**, which must be unique but the best practice is put the same name as in our github repository project(lowercase with a dash used instead of spaces), then choose a region and click **create app**

![heroku app name](wireframes/readme/heroku-app-name.png)

4. From Heroku dashboard resources section, provision 'Heroku Postgres' addon (hobby dev free version). 

5. Install 'dj_database_url' and 'psycopg2' via the CLI using the pip3 install prefixed to the module names
pip3 install dj_database_url
pip3 install psycopg2

6. Disable Heroku from collecting static files -
'heroku config:set DISABLE_COLLECTSTATIC=1 --app your-app-name
7. Add the host name to your settings.py file, under ALLOWED_HOSTS
ALLOWED_HOSTS = ['you-app-name.herokuapp.com', 'localhost']
8. Go to the Deploy tab and click **Connect to GithHub**

![deploy connect to github](wireframes/readme/deploy-connect-to-github.png)

9. Search for the name of the repository and click **Connect**.

![heroku search repository](wireframes/readme/heroku-search-repository.png)

10. Go to **Settings**, click **Reveal Config Vars** and fill out necessary keys and values
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - DATABASE_URL
    - DISABLE_COLLECT_STATIC = 1
    - EMAIL_HOST_PASS
    - EMAIL_HOST_USER
    - SECRET_KEY
    - STRIPE_PRICE_ID
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - STRIPE_WH_SECRET
    - USE_AWS = True
11. Once all the hidden variables are recorded, then click **Enable Automatic Deploys** 

12. Click **Deploy Branch** (Main should be selected unless you want other branches to be deployed)

![heroku automatic deploys](wireframes/readme/heroku-automatic-deploys.png)

13. When the app is deployed by Heroku correctly, the message will appear saying 'Your app was successfully deployed.'

![heroku successfully deployed](wireframes/readme/heroku-successfully-deployed.png)

14. Click **View**.

### **AWS S3 Bucket**
1. Create your AWS account
2. Search for S3 and create a new bucket, select 'allow public access'
3. Under Properties go to static website hosting. Select enable typle index.html as index.html and save.
4. In Permissions, under CORS use :
    - [ { "AllowedHeaders": [ "Authorization" ], "AllowedMethods": [ "GET" ], "AllowedOrigins": [ "*" ], "ExposeHeaders": [] } ]
5. Still in permissions, select bucket policy:
    - Generate bucket policy and copy the bucket ARN
    - Choose S3 Bucket Policy as type of policy
    - For Principle enter *
    - Paste ARN copied from above
    - Add Statement
    - Generate Policy
    - Copy Policy JSON Document
    - Paste policy into Edit Bucket policy on the previous tab
    - Save
6. Under Access Control List (ACL):
    - For Everyone (public access), tick List
    - Accept that everyone in the world may access the Bucket
    - Save
### **AWS IAM**
1. From the IAM dashboard within AWS, select User Groups:
    - Create a new group
    - Click through and create group
2. Select Policies:
    - Create policy
    - Under JSON tab, click Import managed policy
    - Choose AmazongS3FullAccess
    - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
    - Click next step and go to Review policy
    - Give the policy a name and description of your choice
    - Create policy
3. Go back to User Groups and choose the group created earlier
    - Under Permissions > Add permissions, choose Attach Policies and select the one just created
    - Add permissions
4. Under Users::
    - Choose a user name
    - Selecet programmatic access as the access type
    - Click through next
    - Add the user to the group just created
    - Click next and create a user
5. Download the ``.csv` containing the access key and secret access key.
    - The .csv file is onlu available once and cannot be downloaded again
### **Connecting Heroku to AWS S3**
1. Install boto3 and django-storages and freeze your requirements
2. Add the values from the .csv you downloaded to the Heroku configvars
3. Delete 'DISABLE_COLLECT_STATIC = 1' from the config vars
4. Create a custom storage python file in your development environment with the following
    - from django.conf import settings
    - from storages.backends.s3boto3 import S3Boto3Storage
    - class StaticStorage(S3Boto3Storage): location = settings.STATICFILES_LOCATION
    - class MediaStorage(S3Boto3Storage): location = settings.MEDIAFILES_LOCATION
5. Deploy the app
6. In the S3 bucket, set up a new media folder at the same level as the tatic folder and upload any required files. Both files need to be publicly accessible.

### Database Deployment







## Credits



**Media**

**Content**



**Code Snippets**



## Acknowledgments



