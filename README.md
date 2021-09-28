# UNETTO pizza delivery app

Unetto is an interactive e-commerce project for a food delivery pizza shop. This project is a fully functioning interactive application that allow users to order and pay food online.

The site provides all the functionality for a common shopping experience, such as: browsing the menu, providing a shopping cart to save chosen items, have a secure checkout payment and have a personalised emailed message. Backed inside the app there are admin, user and database funtionalities.

**Please note:** _This site is purely for educational purposes only. The payments use a real API but remain in test mode, so no real payment will be taken. Please do not enter real credit card details when using this site._

----

### **Contents** ###

- [UX Design](#ux-design)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
    - [Viewing and Navigation](#viewing-and-navigation)
    - [Registration and User Accounts](#registration-and-user-accounts)
    - [Sorting and Searching](#sorting-and-earching)
    - [Purchasing and Checkout](#purchasing-and-checkout)
    - [Admin and Store Management](#admin-and-store-management)
- [Design Choices](#Design-Choices)
  - [Colours](#Colours)
  - [Wireframes](#Wireframes)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Database](#database)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Features](#Features)
  - [Features Implemented](#Features-Implemented)
  - [Responsive Front-end Design](#Responsive-Front-end-Design)
  - [Back-end Design](#Back-end-Design)
  - [User Stories Implemented](#User-Stories-Implemented)
  - [Site Construction](#Site-Construction)
    - [Topology](#Topology)
  - [Database Schema](#Database-Schema)
    - [Fixtures JSON File creation](#Fixtures-JSON-File-creation)
  - [CRUD Functionality](#CRUD-Functionality)
  - [Messages](#Messages)
  - [Defensive Programming](#Defensive-Programming)
  - [Additional Site Features](#Additional-Site-Features)
  - [Future Features](#Future-Features)
- [Project Management](#Project-Management)
- [Version Control](#Version-Control)
- [Testing](#Testing)
- [Bugs](#Bugs)
- [Deployment](#deployment)
  - [Cloning Unetto from GitHub](#cloning-unetto-from-github)
    - [Prerequisites](#prerequisites)
    - [Cloning the GitHub repository](#Cloning-the-GitHub-repository)
    - [Creation of a Python Virtual Environment](#Creation-of-a-Python-Virtual-Environment)
    - [Install the App dependencies and external libraries](#Install-the-App-dependencies-and-external-libraries)
    - [Create the database in sqlite3](#Create-the-database-in-sqlite3)
    - [Create .env file](#Create-.env-file)
    - [Run the application locally](#Run-the-application-locally)
  - [Deploying Unetto app to Heroku](#Deploying-Unetto-app-to-Heroku)
    - [Creating the Heroku app](#Creating-the-Heroku-app)
    - [Adding a PostgreSQL database to Heroku](#Adding-a-PostgreSQL-database-to-Heroku)
    - [Load the data into PostgreSQL](#Load-the-data-into-PostgreSQL)
    - [Push your repository to GitHub](#Push-you-repository-to-GitHub)
    - [Launch the app](#Launch-the-app)
- [Credits](#Credits)
  - [Images](#Images)
  - [Colour](#Colour)
  - [Inspiration](#Inspiration)
  - [Acknowledgements](#Acknowledgements)


---

## **UX DESIGN** ##

### **Project Goals** ###    

The **goal** of this project is to build a fully functioning e-commerce website for a delivery pizzeria business, allowing the user to browse and order products to be delivered at home.

The **features** of the website will be:

- Display a Menu or search for products by category, or type.
- Sort items by name or price.
- Inform the user about allergens.
- Select items to purchase, select a quantity, and place the order in the shopping cart.
- Checkout. The user inserts personal detail along with delivery details and pay with a secure transaction. Payment integration with Stripe.
- Registration through a personal user profile, a private user page that shows order history and delivery details.
- Email order confirmation and registration confirmation.

I achieve this by:

- Purchases can be made whether the user is registered with an account or not.
- Each product is associated with a list of allergens, that are linked to external medical informations about their properties. 
- Providing a registration form with username and password for users to create a personal account and relative account page.
- Providing a log in page for existing users.
- Utilising Stripe online payments infrastructure to permit purchasing of products.
- Email functionality are connected with Google Gmail, so that our checkout system send the order confirmation by email.

### **User Stories** ###    

#### Viewing and Navigation ####    

1. As a **shopper**, I want to be able to view a list of products so that I can choose some items to purchase.
2. As a **shopper**, I want to be able to filter products that I am interested in without searching through all the products.
3. As a **shopper**, I want to be able to select individual products to see more detailed information and add the item to my shopping cart.
4. As a **shopper**, I want to be able to see any product special offers, new arrivals and available deals, taking advantage of any reduced prices shown.
5. As a **shopper**, I want to be able to see items I have placed in my shopping cart easily so that I can keep track oof what I am buying
6. As a **shopper**, I want to be able to see breadcrumb navigation links to see where I am on the site easily.

#### Registration and User Accounts ####

7. As a **site user**, I want to be able to register for an account to make future purchases easier
8. As a **site user**, I want to be able to easily log in and out of my account so that I can access my personal account information
9. As a **site user**, I want to be able to receive and email requireing me to verify my email account to finish account registeration.
10. As a **site user**, I want to be able to log in and have a personal profile page containing my delivery details and order history
11. As a **site user**, I want to be able to save and update my delivery information on my personal profile page.

#### Sorting and Searching ####

12. As a **shopper**, I want to be able to sort the available products by price, main category, sub-category or product type
13. As a **shopper**, I want to be able to filter and group products for men, women, unisex or kids.
14. As a **shopper**, I want to be able to see how many products are available based on the sorting / filtering I have applied
15. As a **shopper**, I want to be able to search for a product by name, type or category.

#### Purchasing and Checkout ####

16. As a **shopper**, I want to be able to easily select the size and qualtity of a product when adding it to the shopping cart
17. As a **shopper**, I want to be able to view the items in my shopping cart waiting to be purchased, seeing the sub-total, delivery costs and grand total amounts.
18. As a **shopper**, I want to be able to easily update the items in the shopping cart by changing the quantities of products or remove them from the cart.
19. As a **shopper**, I want to be able to checkout securely where I can enter my delivery and credit card payment details with confidence.
20. As a **shopper**, I want to be able to view an order confirmation page as well as receive and email order confirmation once the transaction has succeeded.

#### Admin and Store Management ###

21. As a **store owner**, I want to be able to add new products to my store
22. As a **store owner**, I want to be able to edit / update the current product details and replace the product image file
23. As a **store owner**, I want to be able to delete a product that is no longer for sale.

[Back to contents](#contents)

---

## Design Choices ##


### **Colours** ###

I've chosen worm and light colors. As background site a light bisque and a more white flour tone for each card element. Mainly all the colours have a white, yellow and orange character. I used a strong orange accent color for buttons and element of focus. Green is the color of the logo and the color of basilicum. All this palette draws the color of a pizza!

![Colors Palette](readme_media/palette.png)

### **Wireframes** ###

The mock-ups are made using [Figma](https://figma.com/). 
I used rounded corner and smooth compositions. Cards define structural divisions between elements and hierarchies.
I tryed to avoid depth and I used color to diversify the user interaction.

- [Home Page](readme_media/Desktop1.png)
- [User Registration](readme_media/Desktop2.png)
- [User Log In](readme_media/Desktop3.png)
- [Menu Category](readme_media/Desktop4.png)
- [Product Details](readme_media/Desktop5.png)
- [About Page](readme_media/Desktop10.png)
- [Shopping Cart](readme_media/Desktop12.png)
- [Checkout](readme_media/Desktop13.png)
- [Product Management](readme_media/Desktop14.png)

[Back to contents](#contents)

---

## Technologies ##

### **Languages** ###

- [Python3](https://www.python.org/)
  - Used to create the main application functionality
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used to create the interactive functionality of the website


### **Database** ###

- [PostgreSQL](https://www.postgresql.org/)
  - A powerful, open-source object-relational database.
- [sqlite3](https://www.sqlitetutorial.net/sqlite-python/)
  - Default database created with Django used for app development on localhost.

### **Libraries / Frameworks** ###

- [Bootstrap5](https://getbootstrap.com/)
  - Used to design a mobile-first responsive website layout.
- [Django](https://www.djangoproject.com/)
  - A high-level Python Web framework.
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
  - Python user authentication and login plugin for Django.
- [Stripe](https://stripe.com/en-gb)
  - Online payments platform used for the shopping basket functionality.
- [Green Unicorn (gunicorn)](https://gunicorn.org/)
  - Python WSGI HTTP Server for Unix used on the Heroku deployment.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
  - PostgreSQL database adapter for Python.
- [Pillow](https://pillow.readthedocs.io/en/stable/)
  - Python Image Library image processing capabilities.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  - AWS SDK for Python (Boto3) used to create, configure, and manage AWS S3 services.
- [jQuery](https://jquery.com/)
  - Used for the initialisation of the Bootstrap components functionality and enhance the shopping bag functionality.

### **Tools** ###

- [Git](https://git-scm.com/)
  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
  - Used to store, host and deploy the project files and source code after being pushed from Git.
- [Gitpod](https://www.gitpod.io/)
  - An online IDE linked to the GitHub repository used for the majority of the code development.
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
  - Used for icons to enhance headings and add emphasis to text.
- [Heroku](https://www.heroku.com)
  - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [AWS S3](https://aws.amazon.com/s3/)
  - Amazon Simple Storage Service (Amazon S3) is an object storage service used to store the site static files
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
  - Used to generate new secret keys for environment variables.
- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) 
  - Modify photo, resizing, color correction and exporting for web
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html)
  - Used to create the Unetto logo and favicon

[Back to contents](#contents)

---

### **Site Construction** ##

#### Topology ####

- User Logged Out







![Data relationship Diagram](readme_media/data-structure.png)


## Testing ##

- Testing information can be found in a separate [TESTING.md](TESTING.md) file.

[Back to contents](#contents)

---

## Deployment ##

The website was developed using both Gitpod and Visual Studio Code and using Git pushed to GitHub, which hosts the repository. I made the following steps to deploy the site using Heroku:

### **Cloning Unetto** ###

#### **Prerequisites** ###

Ensure the following are installed locally on your computer:

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [PIP3](https://pypi.org/project/pip/) Python package installer
- [Git](https://git-scm.com/) Version Control

*Please ensure you have an account created at [Stripe](https://stripe.com/gb) in order to use the online payment processing for the checkout app.*

#### **Cloning the GitHub repository** ####

- navigate to [NicolaLampis/ms4-unetto-pizza](https://github.com/NicolaLampis/ms4-unetto-pizza) GitHub repository.
- Click the **Code** button
- **Copy** the clone url in the dropdown menu
- Using your favourite IDE open up your preferred terminal.
- **Navigate** to your desired file location.

Copy the following code and input it into your terminal to clone Sportswear-Online:

```Python
git clone https://github.com/NicolaLampis/ms4-unetto-pizza.git
```


#### **Creation of a Python Virtual Environment** ####


*Note: The process may be different depending upon your own OS - please follow this [Python help guide](https://python.readthedocs.io/en/latest/library/venv.html) to understand how to create a virtual environment.*


#### **Install the App dependencies and external libraries** ####

- In your IDE terminal window, install the dependencies from the requirements.txt file with the following command:

```Python
pip3 install -r requirements.txt
```


#### **Create the database in sqlite3** ####

The installaton of the requirements.txt file will initialise the sqlite3 development database locally.

Run the following commands to create the database tables:

- Check there are no changes to the models already configured.

```Python
python3 manage.py makemigrations --dry-run
```

- Check which migrations will be applied.

```Python
python3 manage.py migrate --plan

```

- Apply the migrations.

```Python
python3 manage.py migrate
```

Load the fixtures files into the database in the following order:

```Python
python3 manage.py loaddata categories
python3 manage.py loaddata deals
python3 manage.py loaddata allergens
python3 manage.py loaddata products
```

#### **Create .env file** ####

- Import and initialise environ in settings.py.
  - A helpful guide can be found [here](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)
- The .env file should contain at least the following information:

```Python
DEVELOPMENT=True
SECRET_KEY=[YOUR SECRET KEY]
STRIPE_PUBLIC_KEY=[YOUR STRIPE PUBLIC KEY]
STRIPE_SECRET_KEY=[YOUR STRIPE SECRET KEY]
STRIPE_WH_SECRET=[YOUR STRIPE WEBHOOK SECRET KEY]
```

- Please ensure you add in your own `SECRET_KEY`, `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`  and `STRIPE_WH_SECRET` values.
- The Stripe keys can be found in the Developers section under API Keys and Webhooks of your [Stripe Account](https://stripe.com/gb)
- ***Important:*** Add the `.env` file to your `.gitignore` file before pushing your files to any public git repository.


#### **Run the application locally** ####

- To run the application, enter the following command into the terminal window:

```Python
python3 manage.py runserver
```

### **Deploying Unetto web app to Heroku** ###

#### **Creating the Heroku app** ####

*Please ensure you have an account created at [Heroku](https://signup.heroku.com/login) in order to deploy the app.*

- Log in to your Heroku account dashboard and create a new app.
- Enter the App name.
- Choose a geographical region closest to where you live.


#### **Adding a PostgreSQL database to Heroku** ####

- Select the **Resources** tab on your Heroku app dashboard
- Select `Heroku Postgres` as a new add-on with a Plan name of `Hobby Dev - Free`
- Heroku will build the PostgresQL database instance and add a config variable automatically.


#### **Load the data into PostgreSQL** ####

- Add the following variable to the `.env` file:
```Python
DATABASE_URL=[YOUR POSTGRESQL DATABASE URL FROM HEROKU CONFIG VARS]
```

- Apply the migrations to the Heroku PostgreSQl database tables.

```Python
python3 manage.py migrate
```

- Load the fixtures files into the PostgreSQL database in the following order:

```Python
python3 manage.py loaddata categories
python3 manage.py loaddata deals
python3 manage.py loaddata allergens
python3 manage.py loaddata products
```

### **Push your repository to GitHub** ###
 - In the Heroku App Settings page, open the section Config Vars
 - Add all the environmant variables from your local `.env` file into the Heroku Config Vars:

| Key | Value |
| --- | --- |
| SECRET_KEY | [YOUR SECRET KEY] |
| STRIPE_PUBLIC_KEY | [YOUR STRIPE PUBLIC KEY] |
| STRIPE_SECRET_KEY | [YOUR STRIPE SECRET KEY] |
| STRIPE_WH_SECRET | [YOUR STRIPE WEBHOOK SECRET KEY] |
| DATABASE_URL | [YOUR POSTGRESQL DATABASE URL] |
| EMAIL_HOST_PASS | [YOUR GMAIL APP SIGN IN PASSWORD] |
| EMAIL_HOST_USER | [YOUR ORDER CONFIRMATION EMAIL ADDRESS FROM GMAIL]



- In the Heroku App Deploy page:
  - Select GitHub from the Deployment Method options.
  - Select Connect to GitHub.
  - Log in to your GitHub account from Heroku to link the App to GitHub.
  - Search for and select the repository to be linked in GitHub.
  - Select Connect.
  - Select Enable Automatic Deployment from the GitHub Master / Main branch.

#### **Launch the app** ####

- Click Open App in Heroku to launch the App in a new browser window.

***Note: The static files served from GitHub will be much slower to load than running locally. It is recommended to copy the static files to an online service such as an AWS S3 Bucket and connect this to Heroku.***

[Back to contents](#contents)

---