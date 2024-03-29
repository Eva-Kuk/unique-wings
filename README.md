## Milestone 4 Unique Wings - by Ewa Kukla

![logo](wireframes/readme/logo.png)

- [Overview](#overview)

- [User stories](#user-stories)

- [UX](#ux)

  - [Strategy](#strategy)

  - [Scope](#scope)

  - [Structure](#structure)

    - [Database Schema](#database-schema)

  - [Skeleton](#skeleton) 
    - [Wireframes mockups](#wireframes-mockups)
  
  - [Surface](#surface) 


- [Features](#features)

- [Technologies used](#technologies-used)

- [Resources](#resources)

- [Testing](#testing)

- [Code validity](#code-validity)

- [Version Control](#version-control)

- [Deployment](#deployment)

  - [AWS S3 Bucket](#AWS-S3-Bucket)

  - [Deployment Platform](#deployment-platform)

- [Credits](#credits)

- [Acknowledgments](#acknowledgments)


## Demo

---

![altamiresponsive](wireframes/readme/am-i-responsive1.png)


- A live demo can be found [here](https://unique-wings.onrender.com)

- A github repository can be found [here](https://github.com/Eva-Kuk/unique-wings)


## Overview
This is my Milestone Project 4 which is the 4th installment in the collection of projects and is part of the Code Institute's FullStack Software Development Diploma Course. Main requirements are to build a full-stack website based around business logic used to control a centrally-owned dataset which contains set up authentication access mechanism and provide paid access to the site's data and purchase of the product.

This project demonstrates the skills and knowledge of using the HTML5, CSS3, JavaScript, Python, Django, AWS, Relational database Postgres and Stripe payments in Back-End development which I have learned recently in the course.

The idea to create this website came from the inspiration of my best friend, who is a devoted fashion follower and passionate about unique creations, beautiful shoes and handbags, which she might show a few in her beautiful collection. 
The aim of this project is to create an e-commerce web application named **Unique Wings** for women but not only, for everyone for whom fashion plays a big role, who love and look for unique, unusual and extraordinary shoes and bags, which accent their style. The users will find website products designed with bird and butterfly motives. 

The brand name of the website "Unique Wings" was inspired not only by the beautiful and colorful parrots, peacocks and butterflies, which are the main themes of the collection offered in the store, but it's worth mentioning that the wings in Greek and Roman mythology were once an attribute of the gods. Nowadays they are a symbol of lightness, uniqueness and freedom, just like the shoes offer in the store which are not only unique and beautiful but also light and comfortable to wear. For many people, wings can also mean making their innermost dreams come true and believe that the impossible may become possible. I hope users can find on this page a collection of shoes and handbags which do not belong to the cheapest, but certainly belong to the original and unique models which every woman will be delighted to have in her wardrobe.

Users can search for and purchase unique shoes and bags via text search, designers or categories, can make order and subscribe for the Newsletter without register or loggin.

Users can create an account to save delivery information for future use, review their history orders and logged in users are also able to add, edit and delete rating with comments on products and also write a comment for the blog posts.

The owner/administrator of the shop  (with the appropriate access) can add, edit and delete products, and create news posts about new delivery, promotions, fashion and designers.

The project is for educational purposes only.
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
| 5.            | general user                | view blogs                                                 | get new information's about the shop, designers fashion events, news             |
| 6.            | new user and future shopper | view a list of products                                       | find which product I'd like to purchase                        |
| 7.            | new user and future shopper | view individual product details                               | identify the price, description, product rating,  image and available sizes before deciding to purchase. |
| 8.            | new user and future shopper | quickly identify sales, promotions and special offers       | take advantage of special savings on products I'd like to purchase |
| 9.           | new user and future shopper | easily view the total of my purchases at any time          | avoid spending too much                                      |


**Registration and User Accounts**       

| **User Story ID** | **AS a/an**                 | **I want to be able to ...**                    | **So that I can ...**                                        |
| ----------------- | --------------------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| 10.               | new user and future shopper | easily register for an account                  | have a personal account and be able to view my profile       |
| 11.               | registered user             | easily login/out                                | access my personal account information                       |
| 12.               | registered user             | easily reset my password in case I forget it    | recover  access to my account if I have forgotten my password |
| 13                | registered user             | receive an email confirmation after registering | verify that my account registration was successful            |
| 14                | registered user             | have a customized dashboard                     | view my personal order history and order confirmation, and save my payment information |

**Sorting and searching**      

| **User Story ID** | **AS a/an** | **I want to be able to ...**                                | **So that I can ...**                                        |
| ----------------- | ----------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| 15.               | Shopper     | sort the list of available products                           | easily identify the best rated, best priced and categorically sorted products |
| 16.               | Shopper     | sort multiple categories of products simultaneously            | find the best-priced or best-rated product across broad categories, such as "high hills" , "flats", "boots" |
| 17.               | Shopper     | search for a product by name or description                 | Find a specific product I'd like to purchase                 |
| 18.               | Shopper     | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available       |


**Purchasing the checkout**

| **User Story ID** | **AS a/an** | **I want to be able to ...**                                 | **So that I can ...**                                        |
| ----------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 19.               | shopper     | easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
| 20.               | shopper     | view details about the items in my shopping bag              | decide if I want to purchase an item or edit it              |
| 21.               | shopper     | easily add, edit & delete items in my shopping bag           | adjust my total to fit into my budget                        |
| 22.               | shopper     | revisit my shopping cart after logging in and logging out    | complete my purchase without re-adding every single item     |
| 23.               | shopper     | checkout using credit/debit card                             | purchase chosen products                                     |
| 24.               | shopper     | receive my digital order via email                           | access the item I just purchased                             |

**Navigation**  

| **User Story ID** | **AS a/an** | **I want to be able to ...**                         | **So that I can ...**              |
| ----------------- | ----------- | ---------------------------------------------------- | ---------------------------------- |
| 25.               | site owner  | access product management from the homepage          | access my account                  |
| 26.               | site owner  | access my dashboard from the homepage                | return to my dashboard at any time |
| 27.               | site owner  | receive a notification when there is a pending order | know when I am making money        |

**Product management**

| **User Story ID** | **AS a/an** | **I want to be able to ...**                                | **So that I can ...**                                        |
| ----------------- | ----------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| 28.               | site owner  | add new products                                            | add new items to my online store                             |
| 29.               | site owner  | edit/update products                                        | update products prices, descriptions, images and other product criteria |
| 30.               | site owner  | delete products                                             | remove erroneous products or products that are no longer available |
| 31.               | site owner  | add, edit, delete blog post                                 | add new posts to their blog                                  |
| 32.               | site owner  | Edit/Update a blog post                                     | change post name, content, and image                         |
| 33.               | site owner  | Delete a blog post                                          | remove a blog post                                           |



 **Authentication & account**    

 | **User Story ID** | **AS a/an** | **I want to be able to ...**           | **So that I can ...**                      |
| ----------------- | ----------- | -------------------------------------- | ------------------------------------------ |
| 34.               | site owner  | verify my email address                | set up my account securely                 |
| 35.               | site owner  | update my account information          | maintain access to my account              |
| 36.               | site owner  | logout when I am finished with my work | logout of my account                        |
| 37.               | site owner  | reset my password                      | recover my account or upgrade its security |


## UX 
(5 planes)

---
## 1. Strategy

The target audience for the proposed website are women but not only, for everyone who is a fashion enthusiast, who are looking for unique and unusual shoes and bags. Users will be able to get more information about the shoes designers, follow the news from fashion and new shoe models posted on the blog on an ongoing basis. They will be able to register and login into their account, keep the order history in one place, share their thoughts and add comments on the blogpost, rate shoes and bags at store.

The main goal of this project was to create an e-commerce web application where users can find unusual shoes where the main motives are birds and butterflies. There also will be able to match bags with their shoes or choose just a bag. The users can secure purchase all products through a secure process.     

It is intended to be used as a full-stack application with a clean and user - friendly site design.

**Project purpose:**
- To create an easy-to-use online e-commerce web application, providing a user-friendly interface with full functionality.
- Create an online shop where users can buy unusual shoes and bags.
- An incentive to buy shoes and handbags presented in the store.

**Site owner goals:**
- Build a store with two different collections shoes ang bags where users can search for, secure purchase.
- To create, update and delete unnecessary products.
- To provide the blog with the latest collections, fashion news which encourage users to return to the site.

**Customer Goals:**
- Easy to register and log in into the account.
- Easy to search for shoes ang bags by categories, rating, price, and find  the information about them.
- Easy and secure checkout process.
- Easy to find links to social media accounts to follow the news about the website.
- Easy to find contact form for possible inquiries about profile or recipes.
- Easy to find and enjoy reading latest posts collections, news on the blog.

## 2. Scope

**Functional Requirements**

- Mobile-first website that is responsive on all devices.
- Informative Landing Page.
- The navbar has been fixed, and is accessed by clicking on the 'hamburger' icon in the top left hand corner of the screen on small and medium devices. When the 'hamburger' icon is clicked, the 'All Products', 'Shoes', 'Bags', 'Special Offers',  'Blog' and 'Contact links are displayed, as well as a 'home' link.
- The Search box has been replaced by an icon on small devices, which displays a search box when clicked.
- Search by a keyword function that users can search for product by keyword.

## 3. Structure
The frontend is integrated into the backend using Python and Django with a PostgreSQL Database.
The site has a simple layout, heavily influenced by the Bootstrap framework.
The navbar always sits at the top of each page, taking the user to all the site sections they can access. Only the pages relevant to the user are displayed e.g. a logged-in user will not see a link to the 'login' page as they are logged in. Equally, a logged out user will not see a link to the 'logout' page as they are already logged out.  If a user tries to manually enter an invalid page URL, they will be redirected automatically to the homepage. There is also a search bar on the navbar, prompting a user to search for a 'mountain' or resort.

An unauthenticated user cannot access certain parts of the website such as the 'bag' and 'checkout' pages as only an authenticated user can make purchases.  
If a user tries to access a 'forbidden' page, they will be either automatically redirected with an error message appearing or asked to log in/register as required.

## Database Schema

### **DATA MODELS RELATIONS**

**Database Structure**
The project data schema was planned using [dbdiagram.io](https://dbdiagram.io/home) 

![dbdiagram](wireframes/readme/dbdiagram-structure.png)

**Relational Database tables schema**

### "UserProfile" model
Model used to store user information. The "UserProfile" is related to the "User" and "Order" model. Stores default delivery information. UserProfile is automatically created or updated using a Django receiver when a User object is updated or created.

| *Field*                 | *Field type*  | *Attributes*                                 |
| ----------------------- | ------------- | -------------------------------------------- |
| user                    | OneToOneField | User, on_delete=models.CASCADE               |
| default_full_name       | CharField     | max_length=50, null=True, blank=True         |
| default_email           | EmailField    | max_length=254, null=True, blank=True        |
| default_phone_number    | CharField     | max_length=20, null=True, blank=True         |
| default_country         | CountryField  | blank_label='Country', null=True, blank=True |
| default_postcode        | CharField     | max_length=20, null=True, blank=True         |
| default_town_or_city    | CharField     | max_length=40, null=True, blank=True         |
| default_street_address1 | CharField     | max_length=80, null=True, blank=True         |
| default_street_address2 | CharField     | max_length=80, null=True, blank=True         |
| default_county          | CharField     | max_length=80, null=True, blank=True         |

### "User" model
Model is created by django All Auth on registration, it stores the name, email and password of a user.

| *Field*  | *Field type* | *Attributes* |
| -------- | ------------ | ------------ |
| name     | Charfield    |              |
| username | Charfield    |              |
| email    | EmailField   |              |
| password | Charfield    |              |


### Checkout model
"Order" model is related to the user profile, feeding in the shipping and contact information. It creates an instance of an order on the data base with billing information, date and time of placement and by whom. The order model is linked to the"OrderLineItem" model which holds the product information for the order placed. Order order_number field is automatically added on save. Order discount, order_total, delivery and grand_total fields are automatically updated using a Django signal when an OrderLineItem is added or deleted.

| *Field*         | *Field type*  | *Attributes*                                                 |
| --------------- | ------------- | ------------------------------------------------------------ |
| order_number    | CharField     | max_length=32, null=False, editable=False                    |
| user_profile    | ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| full_name       | CharField     | max_length=50, null=False, blank=False                       |
| email           | EmailField    | max_length=254, null=False, blank=False                      |
| phone_number    | CharField     | max_length=20, null=False, blank=False                       |
| country         | CountryField  | blank_label='Country *', null=False, blank=False             |
| postcode        | CharField     | max_length=20, null=True, blank=True                         |
| town_or_city    | CharField     | max_length=40, null=False, blank=False                       |
| street_address1 | CharField     | max_length=80, null=False, blank=False                       |
| street_address2 | CharField     | max_length=80, null=True, blank=True                         |
| county          | CharField     | max_length=80, null=True, blank=True                         |
| date            | DateTimeField | auto_now_add=True                                            |
| delivery_cost   | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0        |
| order_total     | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0       |
| grand_total     | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0       |
| original_bag    | TextField     | null=False, blank=False, default=''                          |
| stripe_pid      | CharField     | max_length=254, null=False, blank=False, default=''          |


### Checkout  model
"OrderLineItem" model related to Order, Product, Size and quantity to store and add items to order model. Stores each OrderLineItem after successful checkout.

| *Field*        | *Field type* | *Attributes*                                                 |
| -------------- | ------------ | ------------------------------------------------------------ |
| order          | ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| product        | ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE   |
| product_size   | CharField    | max_length=2, null=True, blank=True                          |
| quantity       | IntegerField | null=False, blank=False, default=0                           |
| lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |


### "Product" model
Model creates objects containing individual product information, such as name, description, price, image and sku. The unique ID is auto generated. The product model is related to the categories model, which divides the products into subsections. The product objects will be used for the order model and favorites model. Product is also related to Review model. 

| *Field*     | *Field type* | *Attributes*                                                 |
| ----------- | ------------ | ------------------------------------------------------------ |
| category    | ForeignKey   | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| sku         | CharField    | max_length=254, null=True, blank=True                        |
| name        | CharField    | max_length=254                                               |
| description | TextField    | ()                                                           |
| has_sizes   | BooleanField | default=False, null=True, blank=True                         |
| price       | DecimalField | max_digits=6, decimal_places=2                               |
| avg_rating  | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True        |
| image_url   | URLField     | max_length=1024, null=True, blank=True                       |
| image       | ImageField   | null=True, blank=True                                        |


### Category Model 
Model Related to Product

| *Field*       | *Field type* | *Attributes*                          |
| ------------- | ------------ | ------------------------------------- |
| name          | Charfield    | max_length=254                        |
| friendly_name | CharField    | max_length=254, null=True, blank=True |


### "BlogPost" model
Model used to add and store articles. This model is related to the "BlogComment" Model and stores Blogpost content, image and posted date.

| *Field*     | *Field type*          | *Attributes*                          |
| ----------- | --------------------- | ------------------------------------- |
| author      | ForeignKey            | User, on_delete=models.CASCADE        |
| image       | ImageField            | null=True, blank=True                 |
| title       | "TextField"/CharField | max_length=254, null=True, blank=True |
| info        | Charfield             | models.CharField(max_length=254, null=True, blank=True) |
| content     | TextField             | max_length=1000                       |
| date_posted | DateTimeField         | auto_now_add=True                     |


### "BlogComment" model
Model  is linked to the "BlockPost" and "User" models and it's used to store users comments about the Blogpost

| *Field*      | *Field type*  | *Attributes*                                                |
| ------------ | ------------- | ----------------------------------------------------------- |
| blogpost     | ForeignKey    | BlogPost, on_delete=models.CASCADE, related_name='comments' |
| user_comment | ForeignKey    | user, on_delete=models.CASCADE                              |
| date         | DateTimeField | auto_now_add=True                                           |
| comment      | TextField     | max_length=1024, null=False, blank=False                    |


### "Contact" model
Model stores users queries in the backend for the admin user to view.

| *Field*     | *Field type*  | *Attributes*                                                 |
| ----------- | ------------- | ------------------------------------------------------------ |
| full_name   | Charfield     | max_length=50, null=False, blank=False                       |
| email       | EmailField    | max_length=254, null=False, blank=False                      |
| subject     | CharField     | (max_length=50, choices=SUBJECT_MENU, default='general_query', null=False, blank=False) |
| message     | TextField     | max_length=1000, blank=False, null=True                      |
| date_posted | DateTimeField | auto_now_add=True                                            |

### "NewsletterUserSubscription" model 
Model is used to store users emails for newsletter subscription.

| *Field*     | *Field type* | *Attributes*                      |
| ----------- | ------------ | --------------------------------- |
| email  | EmailField   | max_length=254, null=False, blank=False |
| date_sent | DateTimeField  | auto_now_add=True |


### "Review" model 
Modelis used to store user comments for each product. "Review" model is linked to the "Product" and ""User" Model.

| *Field*     | *Field type* | *Attributes*                      |
| ----------- | ------------ | --------------------------------- |
| product     | ForeignKey   | models.ForeignKey(Product, null=True, blank=True,related_name='reviews', on_delete=models.SET_NULL |
| user        | ForeignKey   | UserProfile, on_delete=models.CASCADE|
| comment     | TextField    | max_length=500                    |
| rate        | IntegerField | choices=RATE                      |
| date_posted | DateTime     | auto_now_add=True                 |


## 4. Skeleton

## Wireframes mockups

Below are the wireframes created in advance of starting the project. I used the wireframing software [Balsamiq](https://balsamiq.com/) for this project.
The initial wireframes do not differ much from the final version. Visually, I centered the login and register form, I also decided to allow registered users to add, edit and delete comments for blogs and products, and I add ratings.
I have also decided to change blog page and display blog articles as four cards in a row. I found it better UX than the previous version. 

**HOME PAGE**

![home page](wireframes/home.png)

**PRODUCTS PAGE**

![products page](wireframes/products.png)

**EXAMPLE PRODUCT PAGE**

![example product page](wireframes/example-product.png)

**MY SHOPPING BAG PAGE**

![my shopping bag page](wireframes/my-shopping-bag.png)

**ORDER CONFIRMATION PAGE**

![order confirmation page](wireframes/order-confirmation.png)

**PROFILE PAGE**

![profile page](wireframes/profile.png)

**LOGIN PAGE**

[login page old version](wireframes/login.png)

![login page](wireframes/login-new.png)

**REGISTER PAGE**

[register page old version](wireframes/register.png)

![register page new](wireframes/register-new.png)

**CONTACT PAGE**

![contact page](wireframes/contact.png)

**ADMIN/PRODUCT MANAGEMENT PAGE**

![admin product management page](wireframes/admin-product-management.png)

**BLOG PAGE**

[blog page old version](wireframes/blog.png)

![blog page new](wireframes/blog-new.png)

**SINGLE BLOGPOST PAGE**

[single blogpost page old version](wireframes/single-blogpost.png)

![single blogpost page](wireframes/single-blogpost-new.png)

**500 INTERNAL SERVER ERROR PAGE**

![500 error page](wireframes/500.png)

**404 NOT FOUND ERROR PAGE**

![404 not found error page](wireframes/404.png)


## 5. Surface

**Colors**

For this project I have decied to use the simple color palette as the website will contain many colourful images with shoes and bags.
- For navigation bar, footer and buttons, I have chosen a shade of teal:  **Blue Munsel (#288FA4)** which is one of the colors of shoes displaying on the home page. Referring to the website 
[color-meanings](https://www.color-meanings.com/teal-color-meaning-the-color-teal/)
teal color, comprised of blue shades and green tones it has unique values and symbolizes individuality, renewal. It is also a very welcoming color.
- For the background color and some text  I have chosen white off - which **Cultured(#F5F9F9)** which will create harmony with images, text, buttons, and icons. Referring to the website: 
[inspiration-feed](https://inspirationfeed.com/how-a-white-background-can-improve-your-website/) - 6 Tips on Using White Background in Modern Website Design. 
White is associated with cleanliness, perfection, newness, honesty, and new beginnings. It can help to create a focus on certain design elements and make text and headlines more readable. A white background is one of the simplest ways to focus visitors’ eyes on something important.
- As a text color, discount information I have chosen the **Ritch Black (#14161F)**
- For the warning signs, delete buttons I have chosen the **Violet Red (#F05193)** which also is one of the shoes' colors.

![color palette](wireframes/readme/color-palette.png) 

During the comprehensive testing the site, I have decided to slightly darken the main teal background color of the navigation bar to maintain a better contrast, increase accessibility and tone it down a bit for better user experience. Additional colors also were changed for better contrast:  the dark pink color for the alert buttons and `delete` pills and a light pink color to inform the user that there is a product for purchase in the cart .
I have added a white background color, which better blended with the photos of products in the store which are also presented on a white background.

![color palette new](wireframes/readme/color-palette-new.png) 

 **Typography**
- For creating logo "Butterfly" and main headings I have chosen the font [Princess Sofia](https://fonts.google.com/specimen/Princess+Sofia?preview.text=All%20products%20Shoes%20&preview.text_type=custom&query=prince#standard-styles) that resembles a butterfly and also because of its originality, which aims to make the brand unique.

- For the navigation bar headings I have selected the font [Lato](https://fonts.google.com/specimen/Lato?preview.text=All%20products%20Shoes%20&preview.text_type=custom&query=lato#standard-styles) with the group of fall-back font of **sans-serif**. 

- For the content, I have chosen the font [Roboto](https://fonts.google.com/specimen/Roboto?preview.text=All%20products%20Shoes%20&preview.text_type=custom&query=roboto) with a fallback of **sans-serif**, which according to "Google font" website not only is a matching font for Princess Sophia and Lato fonts, which won't make it too crowdy using three different fonts but is also considered to be reader-friendly, elegant and designed to be easy on the eye. 
Both the 'Lato' and 'Roboto' are the recommended fonts used on e-commerce sites by article from [rocketium](https://rocketium.com/academy/20-best-fonts-for-ecommerce-businesses/) about 20 best fonts for e-commerce.

 **Images**

As the idea behind the e-commerce site is the collection and sale of unusual shoes and handbags, mainly designed by two designers, on the main page I have created a hero image on which I placed shoes belonging to the collection of both designers. For the store I have chosen pictures of beautiful, unique and unusual shoes and bags with motives of butterflies and birds. 
 Pictures are downloaded from the [Kat Maconie](https://katmaconie.com/) and [Sophia Webster](https://www.sophiawebster.com/). This project is for educational purposes only so the accociated credit has been included in the credits section. 

The default image if image of the product is not available 
![no image](wireframes/readme/noimage.png)
## Features
**Existing Features**

- The site contains 7 separate custom apps. Each app has its own set of features.
    - Home
    - Products
    - Bag
    - Checkout
    - Blog
    - Contact
    - Profile
  
- There are 4 types of toast messages:
    - Success
    - Info
    - Warning
    - Error

    They appear on the right side of the site, when particular actions are performed by the user
    They provide feedback on the action taken.
    Toast examples:

    ![success-toast-update](wireframes/readme/success-toast-update.png)
    ![toast-success](wireframes/readme/toast-success.png)
    ![toast-alert](wireframes/readme/toast-alert.png)
    ![toast-alert](wireframes/readme/toast-error.png)
    ![toast-error-admin](wireframes/readme/toast-error-admin.png)

### Responsiveness
 - All templates of this project have been built with the responsive framework Bootstrap 4.6 and also used targeted media queries to make this project responsive on all screen sizes.

## NAVIGATION BAR
![navigation bar](wireframes/readme/navigation-bar.png)

This project has two navigation bars present on large screens and folded into the dropdownlist on small devices:
1. Main navigation bar:
- Logo  `Unique-wings` and butterfly navigates user to home page.
- `Search bar` allows any user using keywords to search for products by name, word, category.
- `Contact` link navigates the user to the contact form.
- `My account` dropdown menu: Links to register or sign in forms when the user is logged out. User is able to log in as a registered user and is able to access the menu links: the user's profile and the logout page. When logged in as an admin, the user has access to the dropdown links: the product management, blog management pages as well as the profile app and the log out page.
- `Shopping bag` navigate the user to the shopping bag. When the bag is empty it has the same color like the rest of the items on the navigation bar, once an item is added to the bag it displays the price in pink color. When more items are added to the shopping bag it is updated and displays the total price.
2. Navigation bar: All Products/Shoes/Bags/SpecialOffers/Blog:
- This navigation bar allows the user to check the shop collections by two different categories as  Shoes and Bags.
- `All Products` dropdown menu sort all products by Price, Rating, Categories and  All products.
- `Special offer` dropdown menu filter products by New Arrivals, Special and Displays All Specials.
- The user can also navigate to the blog section.
3. On top of navigation bar there is `Free Delivery banner` which informs users of the free delivery threshold and is counted when the user proceeds to the secure checkout.
- On mobile and medium devices navigation bar is hidden behind the hamburger sign and the `Search` icon, `My Account`, `Shopping bag` visible on the main navbar. The butterfly logo is added which navigates users to the home page as well as a Homepage link added to the dropdownmenu.

![navigation bar mobile](wireframes/readme/navigation-bar-mobile.png)

## HOME PAGE

- The home page presents a hero image composed of two shoes from the latest collection of various designers, the store's motto and a button redirecting the visitor to the store products.

![home page](wireframes/readme/home-page.png)

## FOOTER
- The footer contains a list of useful links: Blog, Contact Us, Social media links: Tweeter, Instagram and Facebook and also a newsletter subscription for visitors and users to subscribe to the newsletter.
- The users don't need to be registered to sign up for the newsletter. Once user ubscribe for the newsletter will be informed by the success toast message. If users decide to unsubscribe from a Newsletter, there is a link which redirects the user to the `Unsubscribe Newsletter` form. The form provides an email to fill in and the user will be removed from the database. The toast message will be displayed.

![footer](wireframes/readme/footer.png)
![subscribe-message-toast](wireframes/readme/subscribe-message-toast.png)

## SHOPPING BAG
- Shopping Bag App allows the user to add/adjust/delete products to the shopping bag, view the Grand total price and details in the bag.
- When a product is added, a preview of the shopping bag is displayed in a toast and the Grand total price/shipping price is updated.
- There is free delivery counter that calculates how much users need to spend to get the free delivery.

![shopping-bag-preview-message](wireframes/readme/shopping-bag-preview-message.png)

## CHECKOUT
- Checkout App allows the user to safely purchase the selection of items placed in the bag using the Stripe system.
- Any user is able to purchase the products without being registered and logged into their account. If the payment was successful the user will receive the confirmation email with the order details, confirmation page and the success toast message will display on the screen. If logged in the shipping details will be filled from the details given in the user profile.
- The credit card details section is linked to the payment platform Stripe for a secure payment procedure.
- When the `Complete Order` button is clicked it triggers a loading spinner that will remain while Stripe checks the credit card details.
- If the payment did not go through, the user is redirected to the checkout form and informed of the failed procedure.

![checkout top](wireframes/readme/checkout1.png)

![checkout bottom](wireframes/readme/checkout2.png)

![checkout confirmation page](wireframes/readme/checkout-confirmation-page.png)

## PRODUCTS
- Product App allows the user to see products with basic product information: image, name, price, category, average rating.
- Clicking the image takes the user to the specific product detail page.
- Only the super-user (Admin) can have access to the EDIT/DELETE product pills and is able to edit or delete products that already exist in the database.
- Any user can browse products using a `Sort by...` box which sort actual display for eg. Heels by Price, Rating, Name and Category.
- There is a back to top button at the bottom right of the screen, which brings the user back to top of the page. 

![products page](wireframes/readme/products-page.png)

## PRODUCT DETAIL PAGE
- Product detail page displays the product details (image, name, price, category, average rating, description, sizes for shoes). 
- The quantity button is to choose an amount of products user wants to purchase.
- Only the super-user (Admin) can have access to the EDIT/DELETE product pills and edit or delete products that already exist in the database.
- The review section is added on the bottom of each product. All visitors can read the reviews and ratings.
- The users have the information on the website to Register and Login if they would like to review the product.
- Once the user is registered and logged in the `Add a Review` button is available and user is able to add the review.
- The owners of the review when logged in will have an access to the EDIT/DELETE review pills from the product detail page and also from `My Profile` page and be able to modify their review. 
- All the ratings are counted and average rating is displayed on the product details section. If there is no reviews then No rating information is displayed.

![product-detail top](wireframes/readme/product-detail1.png)
![product-detail bottom](wireframes/readme/product-detail.png)

## REVIEW/RATING
- Only the registered and logged in users can add/edit/delete reviews and rating. By using `Add Review` button users are redirected to the review page which contain the form to fill in. The average rating made by users is counted and displayed on each product details section.
- Once the form is filled and the user clicked the "Submit" button, they will be redirected to the product page and the success toast message will display. The same procedure is for deleting review.

![reviews-form](wireframes/readme/reviews-form.png)
![reviews-success-message](wireframes/readme/reviews-success-message.png)

## PRODUCT MANAGEMENT
- Product management is for a super-user/admin and is visible on `My Account` dropdown menu when admin is logged into their account.
- Only a super-user (Admin) has the possibility to add products to the database by filling in the add product form. Images can be selected directly from the admin's computer. There is an option for url links as well.
- Once admin add the 
![product-management-top](wireframes/readme/product-management1.png)
![product-management-bottom](wireframes/readme/product-management2.png)

- Only Admin can edit/delete products in the database on the product site or on the product detail page by using Delete|Edit product pills which redirect the admin to products form to be edited. The alert toast displays the information about editing the product and success toast for edits. 

![product-management-top](wireframes/readme/product-management-edit1.png)
![product-management-bottom](wireframes/readme/product-management-edit2.png)

- When deleting the product admin is getting modal alert will appear in the middle of the screen.

![modal-alert](wireframes/readme/modal-alert.png)

## REGISTER
- The site visitor can add their details to open an account on the site through the Register form page. Every account requests an email, email-confirmation, username, password and  password confirmation.
- A verification email is sent to the user's email to avoid fake users with no email. That email contains a security link that opens a "confirmed email" page on the website. The user is added to the database and is allowed to complete their profile on their new profile page.

![sign-up](wireframes/readme/sign-up.png)


## LOGIN
- The site visitor can login to the site if they are an existing user through the login page. The user needs their email address or username as well as their password to connect. The user can also retrieve their password if forgotten.
- Once the login form is approved, the user will see the succesfull toast message on the screen.

![sign-in](wireframes/readme/sign-in.png)
![sign-in-message](wireframes/readme/sign-in-message.png)

## PROFILE
- Profile Page is personal and displays for the registered and logged in user by using the link `My Profile` on the `My Account` dropdown menu. 
- User is able to fill in and update the Delivery information and see the order history.
- The order number links to the order confirmation page.
- User is able access reviews he added to the products on the site and edit it from his profile page

![profile](wireframes/readme/profile.png)
![profile-rewiews](wireframes/readme/profile-reviews.png)

## SIGN OUT
- The user can log out by accessing the logout page through the main navigation bar and confirm to log out. The user is then redirected to the index page.

![sign out](wireframes/readme/sign-out.png)
![sign out message](wireframes/readme/sign-out-message.png)

## CONTACT
- Contact page allows the user to sent a query to the admin. User has the possibility to choose the query from the list General Query, Delivery Query, Return Query, Blog Contribution, Complaint.
The query is stored in the database and two emails are sent: one to the user to confirm that the message was received and one to the admin to signal the store owner of a new query.
- Any User can contact the site owner by email.
![contact](wireframes/readme/contact.png)

## BLOG

- Blog page is made to bring to users many interesting facts about fashion industry, designers, collections and events going on. Only the admin can manage the blog posts, and users can sent emails if they would like to contribute to the blog post there is a link which redirects user to the contact form. 
- Blog page can be accessed through the navigation menu.
 ![blog](wireframes/readme/blog1.png)
 ![blog](wireframes/readme/blog2.png)

## BLOG DETAIL PAGE

- Blog detail page display the full blog post (title, author, date posted/last updated, content) and the comment section. All visitors can read the blog post and comments but only registered and logged in users can add/edit/delete comment.
- The edit link redirects to an edit form while the delete link triggers a confirmation modal and permanently deletes the comment if "Delete" is clicked in the modal.
![blog detail page1](wireframes/readme/blog-detail-page1.png)
![blog detail page3](wireframes/readme/blog-detail-page2.png)
![blog detail page3](wireframes/readme/blog-detail-page3.png)

## BLOG MANAGEMENT
- Blog management is for a super-user/admin and is visible on My Account dropdown menu when admin is logged into account.
- Only an Admin has possibility to add blogpost by filling in the add blog post form. Images can be selected directly from the admin's computer. 
- Only an Admin is able to edit/delete blogposts on the blog page or by navigating to a blog detail page and click the Edit|Delete pills
- A confirmation modal is triggered and the comment if "Delete" is clicked in the modal comment, which is deleted permanently.
![blog management](wireframes/readme/blog-management.png)

When testing the site, the lighthouse tool showed insufficient contrast between the background in the navigation bar and the footer and the text and I decided to slightly darken the background to increase the quality and accessibility for the user. Ultimately, the page looks like the picture below
![home-page-after-change-color1](wireframes/readme/home-page-after-change-color1.png)
![home-page-after-change-color2](wireframes/readme/home-page-after-change-color2.png)

## CUSTOM ERROR PAGES
The website has custom error pages for the following errors with the corresponding error messages.The error pages present the butterfly, which matches the theme of the store and allude to a little bit of  lost.

ipad view

![500-erroripad](wireframes/readme/500-error-ipad.png)

ERROR PAGE 500

![500-error](wireframes/readme/500-error.png)


ERROR PAGE 404

![404-error](wireframes/readme/404-error.png)

ERROR PAGE 403

![403-error](wireframes/readme/403-error.png)

**Features Left to Implement when skills develop**
I would like to add the followung features
- **discount 10% on registration** The possibility to get discount on registration
- **Verified Purchases:** The possibility to allow only customers who have bought an item to be able to leave a review for it.
- **Multiple images:** The possibility to add several photos to a single product and blogpost.
- **Social media login:** The possibility to login via social media (Google, Facebook, Instagram).
-  **Different billing addresses:** The possibility for users to be able to specify different billing and delivery addresses.
- **Paypal:** The possibility for users to pay for their items using Paypal.
- **Apple Pay** - The possibility for users to be able to pay for their items using Apple Pay.
- **Wishlist:** The possibility for users to be able to create a wishlist.
- Automated testing for application
---
Accessibility:
Alt Tags:
In order to ensure that all images are accessible for those using a screen reader, I have ensured that all images used throughout the site include alt tags.

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

- Code Spell Checker

- Font Awesome Auto-complete


**6. Other**


## Resources
- [inspirationfeed](https://inspirationfeed.com/how-a-white-background-can-improve-your-website/) - 6 Tips on Using White Background in Modern Website Design
- [Create A Simple Blog With Python and Django - Codemy](https://www.youtube.com/watch?v=B40bteAMM_M) - tutorial from Codemy about making a blog
- [Contact Pages part1 in Django - Codemy ](https://www.youtube.com/watch?v=w4ilq6Zk-08) - tutorial from Codemy about making a contact form
- [Contact Pages part2 in Django - Codemy ](https://www.youtube.com/watch?v=xNqnHmXIuzU) - tutorial from Codemy about sending email with django
- [cloudinary](https://cloudinary.com/) - Cloudinary is being used to access the image through cloud and to edit and use the images.
- [Code Institute Course Content]() - Main source of fundamental knowledge.
- [Responsinator](https://www.responsinator.com/) - Responsive website mock up image generator.
- [Am I Responsive](http://ami.responsivedesign.is/) - Used to check how the website will look on different devices.
- [Autoprefixer](https://autoprefixer.github.io/) - Used to add vendor prefixes.
- [Google chrome developer tools](https://developer.chrome.com/docs/devtools/) - Used to check page elements, help debug issues with the site layout and test different CSS styles and console JS.
- [w3schools](https://www.w3schools.com/) -  Used as a general source of knowledge.
- [StackOverflow](https://stackoverflow.com/) -  Used as a general source of knowledge.
- [Colors](https://coolors.co/738290-a1b5d8-fffcf7-e4f0d0-c2d8b9) - Color schemes generator.
- [RedKetchup](https://redketchup.io/) - Used to convert an image into a favicon and edit icons for used technologies.
- [Grammarly](https://www.grammarly.com/) - Used to help with grammar check.
- [youtube](https://www.youtube.com/) - Used for general resources.
- [webaim contrast checker](https://webaim.org/resources/contrastchecker/) - check contrast betweent colors

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

[Git](https://git-scm.com/) as a local repository and [GitHub](https://github.com/) acts as a remote repository used for the project, and below is how I used them as a version control for the project.


**- - Setting Up New Repository - -**

1. Create a remote repository in GitHub by clicking "New Repository" on the main page.

![new repository](wireframes/readme/new-repository.png)

2. Use Code Institute Template, put the repository name and click Create Repository **making sure to select public**.

![repository template](wireframes/readme/repository-template.png)

![public](wireframes/readme/public.png)

![create-repository](wireframes/readme/create-repository.png)

3. Open the repository with Gitpod, which is my Integrated Development Environment (IDE). 

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

 ### ** - - Branches - -**

When some testing is needed, create a branch and test on it instead of using main branch. When the testing is successful, then merge the branch into main, when it is not, leave the branch unmerged and keep working on main branch. Below commands are used for this.

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

By forking the GitHub Repository we make a copy of the original repository in our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [Repository](https://github.com/Eva-Kuk/smoothie-lovers).

2. At the top right of the Repository just above the "Settings" Button on the menu, locate and click the "Fork" Button.

3. You should have a copy of the original repository in your GitHub account now.


### **To make a Local Clone**

1. Log into GitHub and locate the [Repository](https://github.com/Eva-Kuk/smoothie-lovers).

2. At the top of the Repository locate the "Code" dropdown menu.

3. To clone the repository using HTTPS, under "CLONE", make sure "HTTPS" is selected and copy the link then.
4. Open Git Bash.

Change the current working directory to the location where you want the cloned directory to be made.

5. Type `git clone` and past the URL you copied in Step 3.

```
$ git clone https://github.com/Eva-Kuk/smoothie-lovers
```

6. Press Enter and your local clone will be created.


## Deployment
The application project requires back-end technologies such as a server, application, and database so it was deployed using [Heroku](https://dashboard.heroku.com/apps) which is a cloud platform with a service supporting several programming languages including python. GitHub can only host a static website. There are two ways to deploy a website in Heroku. One is to use Heroku Command Line Interface (CLI) by using a  command: `heroku login` or `heroku login -i` and another one is to connect to GitHub repository by Heroku. This is deployed by Connecting to GitHub repository. 

### **Requirements**
 
- AWS cloud storage and an S3 bucket for online backup of static files.
- [Stripe Account](https://dashboard.stripe.com/register) (account, test keys and webhooks) as a secure payment platform.
- an IDE, I used GitPod.
- PIP, for Python packages.
- Python3
- Git for version control.
- Email account, I used Gmail.

### Deployment Platform
1. Go to [Heroku](https://dashboard.heroku.com/apps) and login or create and account.

2. Click **New** and choose from dropdown menu **Create new app** to create a new app.

![heroku new app](wireframes/readme/heroku-new-app.png)

3. Enter an **App name**, which must be unique but the best practice is to put the same name as in our github repository project (lowercase with a dash used instead of spaces), then choose a region (Europe) and click **create app**.

![heroku app name](wireframes/readme/heroku-app-name.png)

4. From Heroku dashboard `Resources` tab, do provision a new Postgress database  by writing postgress in the `Add-ons` box and choosing 'Heroku Postgress' (Plan name: Hobby Dev - Free version). 

5. To use postgress  we need to install 'dj_database_url' and 'psycopg2' via the CLI using the pip3 install prefixed to the module names and write it in the terminal in github.

`pip3 install dj_database_url`

and

`pip3 install psycopg2`


then freeze the requirements with pip3 freeze

`pip3 freeze > reqiurements.txt`

to check go to requirements file.

![requirements](wireframes/readme/requirements.jpg)

6. Get to our store new database setup by going to unique-wings settings.py and importing dj_database_url

`import dj_database_url`

and in the DATABASES comment out the default configurations and add database from Heroku which you can get from config variables in settings tab

![heroku-database-url](wireframes/readme/heroku-database-url.jpg)

or from the command line by typing

`heroku config`

run migrations to connect to heroku Postgres
`python3 manage.py showmigrations` - chech to see all migrations

`python3 manage.py migrate` - will apply all migrations and get our database set up.
7. To import our product data we can use our fixtures to load in the categories and then products in that order as the products depend on categories

`python3 manage.py loaddata categories`

`python3 manage.py loaddata products`

and create a super-user to login with 

`python3 manage.py createsuperuser`

8. Before commit remove the heroku database and uncomment to original to avoid it in the version control.
9. Add if statement to DATABASE_URL for heroku and version control working.
![heroku-database-setup-in-settings](wireframes/readme/heroku-database-setup-in-settings.png)
10. Next we need to install gunicorn which will act as our webserver.

    `pip3 install gunicorn`

11. Create `requirements.txt` file which contains the names of packages being used in Python. It is important to update the file if other packages or modules are installed during the project.

    `pip3 freeze > requirements.txt`

12. Create `Procfile` below our manage.py file which contains the name of the application file so that Heroku knows what to run: unicorn and serve our django app. Write in the file the following command:

  `web: gunicorn unique-wings.wsgi:application`

Procfile may have a blank line when it is created so remove it as it may cause problems. 

13. Log in to heroku by typing in the terminal.
`heroku login` or `heroku login -i` if `{"error":"Forbidden"}` appear

14. Disable Heroku from collecting static files - so heroku won't try to collect static files when we deploy
`heroku config:set DISABLE_COLLECTSTATIC=1 --app unique-wings`
15. Add the host name to your settings.py file, under ALLOWED_HOSTS
ALLOWED_HOSTS = ['unique-wings.herokuapp.com', 'localhost']
- and git add, git commit, git push 

16. Go to the Deploy tab and click **Connect to GitHub**.

![deploy connect to github](wireframes/readme/deploy-connect-to-github.png)

17. Search for the name of the repository and click **Connect**.

![heroku search repository](wireframes/readme/heroku-search-repository.png)

18. Go to **Settings**, click **Reveal Config Vars** and fill out necessary keys and values
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
19. Once all the hidden variables are recorded, then click **Enable Automatic Deploys**.

20. Click **Deploy Branch** (Main should be selected unless you want other branches to be deployed).

![heroku automatic deploys](wireframes/readme/heroku-automatic-deploys.png)

21. When the app is deployed by Heroku correctly, the message will appear saying 'Your app was successfully deployed.'

![heroku successfully deployed](wireframes/readme/heroku-successfully-deployed.png)

22. Click **View**.


### AWS S3 Bucket
1. Create your AWS account.
2. Search for S3 and create a new bucket, select 'allow public access'.
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
4. Under Users:
    - Choose a user name
    - Select programmatic access as the access type
    - Click through next
    - Add the user to the group just created
    - Click next and create a user
5. Download the `.csv` containing the access key and secret access key.
    - The .csv file is only available once and cannot be downloaded again
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
6. In the S3 bucket, set up a new media folder at the same level as the static folder and upload any required files. Both files need to be publicly accessible.


## Credits

**Media**

The photos of products for e-commerce store, that I have used in my project have been downloaded mostly from the Sophia Webster, Kat Maconie, Aguazzura designers website and are listed below.

Sophia Webster shoes and bags
- [Flamingo Rainbow High Heeled Sandals](https://www.sophiawebster.com/product/35452/flo-flamingo-sandal)
- [Chiara Purple Butterfly Sandals](https://www.sophiawebster.com/product/35453/chiara)
- [Chiara Black Butterfly Sandals](https://www.sophiawebster.com/product/35454/chiara)
- [Chiara Pink Butterfly Sandals](https://www.sophiawebster.com/product/32564/chiara)
- [Evangeline Bronze Butterfly Sandals](https://www.sophiawebster.com/product/35496/evangeline)
- [Chiara Black Butterfly Pump](https://www.sophiawebster.com/product/35467/chiara-pump)
- [Riva Butterfly Platform Sandals](https://www.sophiawebster.com/product/35445/riva-platform)
- [Chiara Ankle Black Butterfly Boot](https://www.sophiawebster.com/product/31556/chiara-ankle-boot)
- [Paloma Mid Ankle Boot](https://www.sophiawebster.com/product/32605/paloma-mid-ankle-boot)
- [Riva Black Espadrile Wedges](https://www.sophiawebster.com/product/35484/riva-espadrille)
- [Flossy Clutch Black Butterfly Bag](https://www.sophiawebster.com/product/35563/flossy)
- [Flossy Clutch Black Butterfly Crystal Bag](https://www.sophiawebster.com/product/32541/flossy-crystal)
- [Valentina Mid Wedges Espadrile](https://www.sophiawebster.com/product/35439/valentina-mid-espadrille)
- [Flamingo Rainbow High Heeled Sandals](https://www.sophiawebster.com/product/35452/flo-flamingo-sandal)
- [Butterfly Flat Blue Sandal](https://www.sophiawebster.com/product/32616/butterfly-flat-sandal)
- [Butterfly Black Flat Pump](https://www.sophiawebster.com/product/35471/butterfly-flat)
- [Butterfly SlingBack Flat](https://www.sophiawebster.com/product/35469/butterfly-slingback)
- [Hola Shopper Leather Bag](https://www.sophiawebster.com/product/32545/hola)
- [Mariposa Black HandBag](https://www.sophiawebster.com/product/35565/mariposa)
- [Margaux Butterflies Printed Handbag](https://www.sophiawebster.com/product/35555/margaux)
- [Clara Bijou Gold Clutch Bag](https://www.sophiawebster.com/product/32555/clara-bijou-box-clutch)
- [Chiara 85 Black & Rainbow Mid Heels](https://www.eu.forzieri.com/shoes/sophia-webster/wb430419-016-04)
- [Butterfly White Platform Espadrile](https://www.sophiawebster.com/product/32690/butterfly-espadrille-platform-flat)
- [Hola Shopper Leather Bag](https://www.sophiawebster.com/product/35575/hola-tote)
- [Butterfly Gold Platform Espadrile](https://www.sophiawebster.com/product/32689/butterfly-espadrille-platform-flat)
- [Chiara Ankle Boot](https://www.sophiawebster.com/product/35650/chiara-ankle-boot)

Kat Maconie shoes
- [Aya Kicker Heel Sandal](https://katmaconie.com/collections/shop-all/products/aya-black-multi-aw21)
- [Aya Kicker Heel Orchid Multi Sandal](https://katmaconie.com/collections/shop-all/products/aya-orchid-multi-aw21)
- [Caya Embroidered Black Sandals](https://katmaconie.com/collections/shop-all/products/caya-black-aw21)
- [Lucie Black Floral Boots](https://katmaconie.com/collections/shop-all/products/lucie-multi-aw21)
- [Selina Kicker Heel Sandals](https://katmaconie.com/collections/shop-all/products/selina-black-multi)
- [Arabella Black High Heel Sandals](https://katmaconie.com/collections/shop-all/products/arabella-black-gold)
- [Frida kicker Heel Milti Sandals](https://katmaconie.com/collections/shop-all/products/frida-crystal-pink-multi)
- [Emmi Chain Candy Heel Sandals](https://katmaconie.com/collections/shop-all/products/emmi-multi-aw21)
- [Mona Flat Black Multi Sandals](https://katmaconie.com/collections/shop-all/products/mona-black-multi-1)
- [Caya Embroidedered White Sandals](https://katmaconie.com/collections/shop-all/products/caya-blanc-multi-aw21)
- [Alba Chain Black Heel Boot](https://katmaconie.com/collections/shop-all/products/alba-black-aw21)
- [Sigrid Chain Heel Yellow Sandals](https://katmaconie.com/collections/best-sellers/products/sigrid-sunny)
- [Aya Kicker Heel Navy Yellow Sandal](https://www.yoox.com/us/17026805MF/item#cod10=17026805MF&sizeId=15)
- [Jihan Hourglass Heel Sandals](https://katmaconie.com/collections/high-heel/products/jihan-pearl-multi)

Other designers shoes and bags
- [Chiara Colored High Heels](https://www.brownsfashion.com/ie/shopping/sophia-webster-chiara-sandals-11809223)
- [Claudie Butterfly Black Shouldes Bag](https://www.bragmybag.com/sophia-webster-claudie-butterfly-bag/)
- [Mini Kensington Actoss Body Rainpow Bag](https://www.zalando.ie/kurt-geiger-london-mini-kensington-across-body-bag-multicoloured-ku051h07o-t11.html)
- [Yara Butterfly Turqoise Pumps](https://www.bragmybag.com/sophia-webster-yara-butterfly-pumps/)
- [Aguazzura Ritch Turqouse Butterfly Sandals](https://www.aquazzura.com/us_en/papillon-sandal-105-rich-turquoise-pplhigs0-snl-rtq.html)
- [Aguazzura Jungle Green Butterfly Sandals](https://www.farfetch.com/ca/shopping/women/aquazzura-papillon-105mm-sandals-item-15209224.aspx?size=21&storeid=11811&clickref=1100lijidbCd&utm_source=laurenlyst&utm_medium=affiliate&utm_campaign=PHCA&utm_term=CANetwork&pid=performancehorizon_int&c=laurenlyst&clickid=1100lijidbCd&af_siteid=1011l2075&af_sub_siteid=1011l274&af_cost_model=CPA&af_channel=affiliate&is_retargeting=true)
- [Aguazzura Canary Yellow Butterfly Sandals](https://www.aquazzura.com/us_en/papillon-sandal-105-sporty-yellow-pplhigs0-snl-spy.html)
- [Furla Flamingo Shoulder Bag](https://www.lyst.com/bags/furla-flamingo-print-metropolis-bag/)
- [Turquoise mini Kensington Hand Bag](https://www.zalando.ie/kurt-geiger-london-fabric-mini-kensington-across-body-bag-turquoise-ku051h08n-l11.html?size=One%20Size&allophones=0&wmc=SEM353_NB_GO._9357456472_1445614975_128503437563.&opc=2211&mpp=google%7cv1%7c%7cpla-422602954492%7c%7c1007850%7c%7cg%7cc%7c%7c555699722328%7c%7cpla%7cKU051H08N-L110ONE000%7c422602954492%7c1%7c&gclid=Cj0KCQjwlOmLBhCHARIsAGiJg7lDQRnXMV2ojg8V4VtuOiLD2r9yv1RWSdBP3N0H3wqhWgrJfbVx4XQaApAREALw_wcB&gclsrc=aw.ds)
- [Kensington Rainbow Handbag](https://8000-scarlet-tiger-6t3dns54.ws-eu18.gitpod.io/products/57/)
- [Kensington Rainbow Shopper Bag](https://www.zalando.ie/kurt-geiger-london-shopper-tote-bag-multi-coloured-ku051h07e-t11.html?size=One%20Size)
- [error image](https://pixabay.com/pl/illustrations/motyl-skrzyd%c5%82o-owad-zwierz%c4%99-2339711/) - error background image from Pixaby by Comfreak
Blogpost articles

**Content**
Imagea and content for blog was taken and modified from sources below:
- [Shoes that celebrities like to wear](https://footwearnews.com/2019/fashion/celebrity-style/sophia-webster-butterfly-heels-red-carpet-1202761466/)
- [Debunking Myths](https://katmaconie.com/blogs/blog/the-widefitchallenge)
- [How to choose the correct shoe size when shopping online?](https://www.dolitashoes.com/blogs/news/how-to-choose-the-correct-shoe-size-when-shopping-online)

**Code Snippets**
- The fantastic [Code Institute](https://codeinstitute.net/) Boutique Ado Project course material enabled me to successfully implement the Basket, Checkout and Stripe payment system including Webhooks.
- [IntegrityError in Django](https://stackoverflow.com/questions/18243149/integrityerror-in-django) - Stack overflow solutions ideas how to solve the integrity error in Django
- [IntegrityError at /posts/12/new-comment/ NOT NULL constraint failed](https://stackoverflow.com/questions/64378553/ integrityerror-at-posts-12-new-comment-not-null-constraint-failed-posts-comme) - Stack overflow solutions ideas how to solve the integrity error in Django
- [Django Tutorial - Create Newsletters App](https://www.youtube.com/watch?v=TBVsILIt4HM) - Django Tutorial - Create Newsletters App from Master Code Online
- [Django Tutorial - Newsletter Sign Up View](https://www.youtube.com/watch?v=Hy94jBBgvpk) - Django Tutorial - Newsletter Sign Up View from Master Code Online
- [Django Tutorial - Newsletter Unsubscribe View](https://www.youtube.com/watch?v=q2B1VpjDjMQ) - Django Tutorial - Newsletter Unsubscribe View from Master Code Online


## Acknowledgments
I would like to thank:

- My mentor Aaron Sinnott for his helpful and valuable feedback and guidance.
- To my tutor Kasia for providing support.
- I would like to thank the whole fantastic Code Institute Tutor Support team for your help. I am very grateful for every minute, you are amazing guys with astonishing knowledge. Thank you for sharing, I have learned a lot from you. I would not be myself if I did not thank: Igor, Fatima, Jo, Sean, Sharyl, Johann, Ed, Alan, James, John, Scott I hope I didn't miss anybody.
- My friend Anna who helped me test and give advice and ideas for better UX improving, my son Adrian for the time devoted to reading and correcting my documentation.
- Slack community for great posts.

Site for educational purposes only :)
