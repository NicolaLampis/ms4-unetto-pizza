## Testing

Manual testing was performed for this project due to time constraints.

### HTML Validation    

HTML Online validator [HTML validator](https://validator.w3.org/nu/)
- Check Validate for: https://unetto-pizza.herokuapp.com    
/    
/menu    
/about    
/contact    
/profile    
/cart    
/checkout     
No Error Found. 

### CSS Validation     

CSS Online validator [jigsaw.w3.org](https://jigsaw.w3.org/css-validator/#validate_by_uri+with_options)
- profile-style.css
- base.css
- checkout-style.css
No Error Found. 

### JavaScript Validation     

JavaScript Online validator [jshint.com](https://jshint.com/)
- JavaScript files:
- city-field-selector.js
- stripe_elements.js
No major Error Found. 

### Python Validation     

[PEP8 requirements](http://pep8online.com/)
My python code is been refactored during development. 
I used the IntelliSense (Pylance) for VScode and Gitpod extension to checks the validity of my Python code.

### Responsive Layout     

The web pages render well on a variety of devices or screen size.
Is ensured content legibility in any size.
The grids resize correctly. Bootstrap media queries works fine.
Flexible images are also correctly responsive.
Responsive layouts automatically adjust and adapt to any device (desktop, laptop, tablet, mobile phone) or screen size.

Responsibe behaviour was tested using Chrome Developer Tools and Firefox Developer Tools 

Physical devices used for testing:

- Xiaomi redmi note 6pro- 
- Asus x53s laptop
- Acer switch 3 laptop

### Browsers tested

- Chrome
- Firefox
- Opera
No Error Found.

## Authentication

To ensure security only authenticated user can access personal information.
Every attempt to access restricted pages are prevented.
Functionality like create/update/delete product are allowed only to admin and superuser.

A user logged out that try to access certain restricted functionality are redirected to the login page.
A simple user logged in that try to access restricted functionality like add/update/delete are stopped with an error message.
Only superusers can see in the template the restricted functionalities.

### Images

Product without images renders a dummy image instead. Uploaded images are correctly displayed.

## Behaviour of Individual Pages

### Home
- Background image is displayed correctly and is responsive

#### Navbar
- Links destination correct.
- Dropdowns menus works and are displayed with appropriate style.
- Search functionality brings you in the menu page, where the query is shown correctly. Empty result show a message. The query text is displayed on top
- Cart displays correct total amount, when total is zero the delivery charge is not present.
- Small size, collapse and the burger icon when clicked opens the menu.
#### Footer

### Menu
- If you enter in the URL a query with non existent category a message inform the user no match query were found
- Category links displayed and linked correctly
- Sorting dropdown for names and price work correctly
- Confirm that the appropriate *current category* name is displayed for the selected category
- For each product the right image/name/description/category/price is displayed correctly
- Only superuser can see the **Edit** button in each product and clicking it access the right product detail page


### Product detail
- The quantity input works as expected
- The **Add To Cart** button is displayed correctly
- Clicking the **Add To Cart** buttons adds the product and quantity to the cart, the cart total is updated, a success message toast inform the user that the product has been successfully added to the order
- *Edit* and **Delete** buttons are displayed correctly for superusers
- Clicking the **Edit** button redirects the superuser to the Product Management page.
- Clicking the **Delete** button opens a modal windows for the delete confirmation. Delete button delete the specific product 

### Profile

### Cart

### Checkout
#### Payment form
#### Order summary
#### Stripe form

### Checkout Success 


### Add - product management

### Edit - product page

### Authentication - Allauth pages

## Bugs
Fixed: ✔️
Integrity error at /menu/add/
null value in column "favourite" of relation "menu_product" violates not-null constraint

Adding a new product this bug showed. It started after deleting the favourite field in the Product model.
Favourites will be a future features on the app.
The bug wasn't present in local.
After reinitializing the heroku app the bug was solved.