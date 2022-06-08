# Be My Baby ()
## About

Be my baby is an eCommerce site aimed to new parents or parents to be, that are looking for equipment for the new addition to the the family.
This site is designed to be resposive and easy to navigate from different devices as well as to be accesible for all users.

[View the live project here.](https://8000-gloria21-bemybaby-sy6g7t62dw6.ws-eu45.gitpod.io/)

##  Contents
### UX (User experience)
- ### User stories
    1. As a user you will be able to find the products that you are looking for
    2. As a user you will be able to click on them and see their characteristic
    3. As a user you will be able to add and remove items to the bag
    4. As a user you will be able to check out and pay for your items

### Desing Choices
* **favicon**

     I have chosen the symbol of a pram as it is quite relatable to website theme. To create it I have used [canva](https://www.canva.com/en_in/)
* **Typograghy**

    The font use on the website has been chosen from [Google Fonts](https://fonts.google.com/).
* **Colour Scheme**

    The colour scheme chose for this proyect is a soft-pastel palette as the theme is baby items.
    To create it I have used [coolors](https://coolors.co/)

    ![Palette](/media/be_my_baby.png)

    However, as the project was taking shape I decided to not use the pink colour and follow the less is more quote

* **Wireframe**

* [Desktop Wireframe Home](https://drive.google.com/file/d/1qqa30S-FQxxlqpJSE5VpgMmted6ee5LR/view?usp=sharing)
                    
* [Mobile Wireframe](https://drive.google.com/file/d/1i0BgbKDtbHuSWoE3gigl7cpu8fDkUwii/view?usp=sharing)

### Features
* **Future Features**

In the near future I would like to finish the project, due to time constriction it is not quite done. I want to  develop further the profiles and the admin section. In  the longer term I would love to add a blog section with advice for new parents on which products are more suitables for their babies. Also I would like to add a different range of products to the shop.

### Tecnologies used
* **Languages**

    * [HTML5](https://en.wikipedia.org/wiki/HTML5) 

    * [CSS3](https://en.wikipedia.org/wiki/CSS)

    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    
    * [Python 3](https://www.python.org/)

* **Tools**

    * [Git](https://git-scm.com/)

        Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub

    * [Github](https://github.com/)

        Used to store, host and deploy the project files and source code after being pushed from Git

    * [Stripe](https://stripe.com/gb)
    
    * [Heroku](https://www.heroku.com/home)

        Used for the deployment of live site

    * [Font Awesome](https://fontawesome.com/)

         Used for the icons on this website

    * [TinyPNG](https://tinypng.com/)

        Used to compress images for better user experience

    * [Favicon](https://favicon.io/)

        Used to generate a favicon for the website title.


### Testing

I have done the testing for my website using the dev tools on google chrome. I have been testing regularly checking that the results were the expected on different sizes, from mobile devices to desktop and tablet, making sure the website was responsive in all of them.
I used this tool as a main source to implement my code, trying the functionality and styling effects there first and adding them to my code afterwards.

### Validator testing

To check the validity of the codes I have used 
* [W3C Markup Validation](https://validator.w3.org/)
   - For [index.html](/static/docs/images/index_validator.png)



* [W3C CSS Validation](/static/docs/images/validator-base.css.png)

* [JS Hint](https://jshint.com/)

* [PEP8Online](http://pep8online.com/)
    - For [urls.py](/static/docs/images/urls.py.png)

### Performance

To check the website performance level as well as the speed I used [Google lighthouse](https://developers.google.com/web/tools/lighthouse)

* [Homepage](/static/docs/images/lighthouse-homepage.png)
* [Products](/static/docs/images/lighthouse-products.png)
* [Checkout](/static/docs/images/lighthouse-checkout.png)


### Bugs

* My account and Bag Icons were proving challeging as they weren't taking the colours chosen due to inheriting elements from CSS. In the end logo-font and specific class for each solved the problem
* Navbar is not reponsive to changes in size/ desing desired
* Issue with models.py when applied to products.json. On the 0001_initial.py was showing img_url on the fields migrated instead of image_url used on the product.json. the migration process had to be run twice in order to solve the issue as it wasn't applying the migration properly.

### unfixed bugs
* Minus button not in the correct place when there is a prodcut selected and ready to add into the bag, I have tried move location, CSS but it is not fixed
* Another bug unsolved due to lack to time is the links on my account, and shopping bag that change colour when moved to a different size such as mobile

### Test user stories

1. As a user you will be able to find the products that you are looking for:
    As a new parent I want to access the website and in an intuitive way I want to filter the products and find what I am looking for very easily.
    The user has two different ways to filter the products. A dropdown that filters by price, rating and category and another (Home and Nursery) that filters by Cot Bed, Chaning Units, chairs and all products [Filters](/static/docs/images/filters.png)

2. As a user you will be able to click on them and see their characteristic
    As a user I would like to have more information about the product that I am internded to buy, when the selected product is clicked, it shows the information and has the possibility to be added to the bag or keep shopping if the product is not meeting your expectations
    [Product](/static/docs/images/product.png)

3. As a user you will be able to add item to the bag
    Once the product is selected there is a button to add it to the bag. In this case a message will pop up to inform the user taht the product has been successfully added to the bag
    [Add to bag](/static/docs/images/stripe-sucess.png)
    Also the bag can be modified and the user can remove an item that is already in there. The user will received another message informing that the product has been successfully removed 
    [Remove from the bag](/static/docs/images/stripe_remove.png)

 4. As a user you will be able to check out and pay for your items. 
    The user will be able to do the checkout securely, the user will be redireceted to the shopping bag screen
    [Shopping bag](/static/docs/images/shoppingbag.png)
    Once in there the user will click the secure checkout button and be redirected to the checkout page and being to fill a form in order to get payement and get the product delivered
    [Checkout](/static/docs/images/checkout.png)
    After that the user will see a screen with all the information of the purchase and an email will be send to the address provided 
    [Checkout-sucess](/static/docs/images/checkout.png)


### Deployment

This website has been developed on Gitpod, using Github to host the repository

### Via Gitpod 

These are the step followed to deploy via Gitpod:
1. Log in to the Gitpod account 
2. Chose the Weird and Wondeful repository
3. Add your code 
4. Type "python3 -m http.server" on the terminal
5. A new screen will pop up with the results of the code on the browser
### GitHub pages

These are the steps followed to deploy this website using GitHub:

1. Log in to your  GitHub account
2. Select Weird and wonderful on my repositories
3. Go to settings on the repository
4. Scroll down to the GitHub pages area
5. Select the Master Branch from the Source dropdown menu
6. Confirm my selection 

After this, the website was live on GitHub pages

### Making a Local Clone

Making a local clone of your repository allow others to view the original code and even to add changes on their own local copy.

To do so you have to 
1. Log in to GitHub and select teh repository you wish to clone
2. Click the download button or Code button
3. Copy the url that will show on the box
4. Open Gitpod (or your preferred IDE)
5. Use the "git clone" command in the terminal followed by url copied before

A clone of the original repository should be available on your computer

### Heroku App



### Credits

To create this project I have used images from [Babyblooms](https://www.babyblooms.co.uk/collections/home-nursery)
I have followed the proyect Boutique Ado, form Code Institute, that has been very instructive
Also I have been inspired by the wonderful project that [Suzybee1987](https://github.com/suzybee1987) has done [Knit-happens](https://github.com/suzybee1987/knit-happens)

