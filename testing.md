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
- Links destination correct.
- Links opens in a new tab.
- Responsive behaviuor of columns works correctly at any size.

### Menu
- If you enter in the URL a query with non existent category a message inform the user no match query were found
- Category links displayed and linked correctly
- Sorting dropdown for names and price work correctly
- Confirm that the appropriate *current category* name is displayed for the selected category
- For each product the right image/name/description/category/price is displayed correctly
- Only superuser can see the **Edit** button in each product and clicking it access the right product detail page
- Banner shows the correct delivery threshold amount(valid for all the pages)


### Product detail
- The quantity input works as expected. Buttons disable for numbers =< 0 and =>60
- For each product the right image/name/description/category/price is displayed correctly
- List of allergens is correctly displayed. No allergens insn't showing as expected.
- Link of allergen opens an external page with the right allergen info
- The **Add To Cart** button is displayed correctly
- Clicking the **Add To Cart** buttons adds the product and quantity to the cart, the cart total is updated, a success message toast inform the user that the product has been successfully added to the order
- Clicking **Keep Shopping** button you are redirected to the menu
- **Edit** and **Delete** buttons are displayed correctly for superusers
- Only for superuser. Clicking the **Edit** button redirects the superuser to the Product Management page.
- Only for superuser. Clicking the **Delete** button opens a modal windows for the delete confirmation. Delete button delete the specific product 


### Profile - user logged in
- **Update information** button update the form and info of the user
- The two column are displayed correctly and their responsive behaviour is correct
#### Default delivery information
- The form is displayed correctly
- If the form isn't correct a message inform the user about requested field to be filled in
- A correct form will be updated and a success message will inform the user
#### Order history
- The table displays all the values correctly
- Table responsive
- The table rows have alternating color
- The orders are all displayed


### Cart
- Products are displayed correctly, with the right quantity, price and subtotal
- When **quantity** is being changed the update button will update the new quantity correctly with a success message
- The **delete** button delete the product from the order correctly with a success message
- If you digit quantity zero the product will be removed
- Delivery charge and order total are correct and are displayed correctly
- Keep shopping button works and redirect to the menu
- Checkout button opens che checkout page


### Checkout
- The two column are displayed correctly and their responsive behaviour is correct
- A correct form will be updated correctly and a loading page will be displayed
- After submission the user will be redirected to the Checkout success page
#### Payment form
- The form is displayed correctly
- Requested fields have an *
- If the form isn't correct a message inform the user about requested field to be filled in before submit
- Other imput error messages are displayed correctly
- Save delivery informations checkbox works correctly
#### Stripe form
- The stripe card form is displayed correctly
- Stripe error message are displayed in red below the input
#### Order summary
- The table is displayed correctly with all the right info

### Checkout Success 
- A success message inform the user that the order has been processed correctly. Correct order number shown
- The page shows all the order info correctly
- The page shows all the delivery info correctly
- The page shows all the billing info correctly
- The long order number can break for small display and is shown correctly without overflow
- The responsive behaviour changes correctly
- Our latest deal button redirect correctly to the menu query deals

### Add - product management

### Edit - product page

### Authentication - Allauth pages

### Messages

## Bugs
Fixed: ✔️
Integrity error at /menu/add/
null value in column "favourite" of relation "menu_product" violates not-null constraint

Adding a new product this bug showed. It started after deleting the favourite field in the Product model.
Favourites will be a future features on the app.
The bug wasn't present in local.
After reinitializing the heroku app the bug was solved.