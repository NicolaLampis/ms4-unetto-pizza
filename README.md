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

