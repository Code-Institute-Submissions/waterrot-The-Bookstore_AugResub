![The Bookstore Holland Logo](media/thebookstore_logo.png)
# The Bookstore Holland

- [intro](#intro)
- [UX](#ux)
  - [Project Goal](#project-goal)
  - [User Stories](#user-stories)
    - [User Stories for Customers](#user-stories-for-customers)
    - [User Stories for Shop Administrators](#user-stories-for-shop-administrators)
  - [Wireframes](#wireframes)
  - [Data Structure](#data-structure)
  - [Design](#design)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to implement](#features-left-to-implement)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Technologies](#technologies)
- [Tools Used](#tools-used)
- [Credits](#credits)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

---

## Intro
The Bookshop is a website designed to light out some of the best books writen over the last 100 years. Right now the shop has 101 product, writen by 26 authors.

The site will be deployed to Heroku and can then be viewed [here](https://the-bookstore-holland.herokuapp.com/).

## UX

### Project Goal

This project is my fourth and final Milestone Project in the Code Institute's Fullstack Development program. The purpose of this project was to create an e-commerce site using the Django framework, static file hosting with AWS, and a functional payment system with Stripe. This e-commerce site is fully functional and could be used by a real beer distribution company with minimal setup.

### User Stories

#### User Stories for Customers



| **As a customer I would like to**                  | **So that I can**                                    |
| -------------------------------------------------- | -----------------------------------------------------|
| Browse through books                               | purchase what I need                                 |
| Search for books                                   | find something specific                              |
| Filter books by category                           | compare the offerings                                |
| Filter books by price                              | compare the offerings                                |
| Filter books by author                             | compare the offerings                                |
| See books of a specific author                     | compare the offerings                                |
| Buy a book                                         | serve it to customers                                |
| Pay using a card                                   | complete my purchase                                 |
| Create a profile                                   | save my information and review past orders           |
| Update my profile information                      | so the delivery will be send to the righ address     |                  |
| See my shopping cart before paying                 | know the cost and content before the purchase        |
| Update my shopping cart                            | make decisions before the purchase                   |
| See details about a product                        | make an informed purchasing decision                 |
| View my order history                              | be reminded of previous purchases                    |
| Receive an email confirmation about my order       | have archived information about it                   |


#### User Stories for Shop Administrators

| **As an administrator I would like to**     | **So that I can**                                |
| ------------------------------------------- | ------------------------------------------------ |
| Add/Update/Remove a book                    | keep the store up to date                        |
| Add/Update/Remove a category                | create a more diversified offer                  |
| Receive orders from customers in my mailbox | fulfill the orders                               |
| Mark a book as a new arrival                | entice customers with fresh products             |

### Wireframes

Following these user stories, wireframes were drawn to provide a starting point and guidance throughout the development process.

*this is the place where the wireframe will be in the future*

### Data Structure

Before starting the development of the application, its models and their relationships were delineated:

![The Book store Modules](README-files/data-structure.jpeg)

### Design

The application was built using bootstrap and its responsive grid system. The main layout is based on [Lux](https://bootswatch.com/lux/), while Bootswatch works really well with bootstrap.
Colors are chosen to stand out. The buttons needed to be an eye catcher and the normal elements needed to show some peace to the eye.

## Features

### Existing Features

#### home page
- the homepage shows a carousel that links to 3 different part on the site to give those products more attention.
- the homepage shows 3 new books chosen by the owner of the site that are very good seller.

#### product pages
- browser through different products and use filters for it. 
- click on one of the category buttons to go directly to the category search page.

#### product information page
- read more information about the product.
- select the format you would like the book in and see live how the price changes.
- select the quantity and buy the product and send it to the shopping bag.

#### shopping bag page
- remove/add/edit the products in your shopping bag.
- continue to the payout page.

#### checkout page
- fill in your delivery address.
- fill in your creditcard information.
- continue to buy the product.

#### profile page
- see your order history.
- edit your personal information.
- add new products

#### author page
- browse through the different authors.
- filter them by name.

#### author information page
- read more about an other.
- go to the amazon page of the other.
- see the other books the author has writen.


### Features Left to implement
- add new authors



## Testing


## Deployment


### Local Deployment

These are the steps to deploy Beer WareHaus locally.

1.  From the application's [repository](https://github.com/waterrot/The-Bookstore), click the "code" button and download the zip of the repository.

    Alternatively, you can clone the repository using the following line in your terminal:

        git clone https://github.com/waterrot/The-Bookstore.git

2.  Access the folder in your terminal window and install the application's required modules using the following command:

        python -m pip -r requirements.txt

3.  Create a file containing your environmental variables called `env.py` at the root level of the application. It will need to contain the following lines and variables:

    ```
    import os
    (the import code line will come here)
    ```

    Please note that you will need to update the `SECRET_KEY` with your own secret key, as well as the Untappd and strip keys and secret variables with those provided by those applications.

    If you plan on pushing this application to a public repository, ensure that `env.py` is added to your `.gitignore` file to protect your secrets.

4.  The application can now be run locally. In your terminal, type the command `python3 manage.py runserver`. The application will be available in your browser at the address `http://localhost:8000`.

### Deployment to Heroku



## Technologies

-   HTML
-   CSS
-   JavaScript / jQuery
-   Python
-   Django

## Tools Used

-   Github
-   Heroku
-   [Google Fonts](https://fonts.google.com/)
-   [Font Awesome](https://fontawesome.com/)

## Credits

### Media

### Acknowledgements

-   This site is meant for educational use.
-   [Felipe Alarcon](https://github.com/fandressouza) for his helpful feedback and advice, and constant availability as a mentor
-   [Beer Warehause](https://github.com/jumboduck/beer-warehaus) for the basic structure of the README file.
-   Many thanks to the team at the Code Institute for their help throughout the development process.