# Be My Baby
## About

Be my baby is an eCommerce site aimed to new parents or parents to be, that are looking for equipment for the new addition to the the family.
This site is designed to be resposive and easy to navigate from different devices as well as to be accesible for all users.

[View the live project here](https://be-my-baby.herokuapp.com/)

##  Contents
### UX (User experience)
- ### User stories
    1. As a user, you will be able to find the products that you are looking for
    2. As a user, you will be able to click on them and see their characteristic
    3. As a user, you will be able to add and remove items to the bag
    4. As a user, you will be able to check out and pay for your items
    5. As a superuser, you will be able to add, edit and delete products 

## Desing Choices
* **Favicon**

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

## Features

* **Create Profile**
    * Users can:
        * Create a profile to save their orders and personal information
        * Confirm their details are correct via email verification
        * Store details for faster checkout

* **Login to Profile**
    * Users can:
        * Log in to profile to see their orders and personal information
        * Edit personal information if required

* **Product page**
    * Users can:
        * See products by Name, category and price
        * Filter by different categories of products
        * Click on the product to find more information about it
        * Add a review to a chosen product

    * Superusers can:
        * Add, edit and delete products

* **Header**
    * All users can navigate to home, products and bag pages
    * Users logged in can access profile pages
    * Users not logged in can access log in and register pages

* **Defensive Design**
    * Form Validation:
        * Form validation has been added to every form to ensure all required information is included before submitting. If incorrect data is input a warning text appears to advise the user how to continue
    * Unauthorised Attempts:
        * An error is launched if the user attempts to visit a part of the site where they are not authorised
    * @login_required:
        * @login_required decorator added to restrict access to certain pages. If a logged-out user tries to access a restricted page, they will be redirected to the login page.
        * Only authorised users may perform certain actions: Eg add, edit, delete product and edit

* **Future Features**

In the near future I would like to improve the blog section as it hasn't being developed fully due to time constriction. Also I would like to add a different range of products to the shop.

## Tecnologies used
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

        Payment processing platform
    
    * [Heroku](https://www.heroku.com/home)

        Used for the deployment of live site
    
    * [AWS](https://aws.amazon.com/)

        Cloud application used to hold media files

    * [Font Awesome](https://fontawesome.com/)

         Used for the icons on this website

    * [TinyPNG](https://tinypng.com/)

        Used to compress images for better user experience

    * [Favicon](https://favicon.io/)

        Used to generate a favicon for the website title.


## Testing

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


## Bugs

* My account and Bag Icons were proving challeging as they weren't taking the colours chosen due to inheriting elements from CSS. In the end logo-font and specific class for each solved the problem
* Navbar is not reponsive to changes in size/ desing desired
* Issue with models.py when applied to products.json. On the 0001_initial.py was showing img_url on the fields migrated instead of image_url used on the product.json. the migration process had to be run twice in order to solve the issue as it wasn't applying the migration properly.

### Unfixed bugs
* Minus button not in the correct place when there is a product selected and ready to add into the bag, I have tried move location, CSS but it is not fixed
* Another bug unsolved due to lack to time is the links on my account, and shopping bag that change colour when moved to a different size such as mobile
## Test user stories

1. As a user you will be able to find the products that you are looking for:
    As a new parent I want to access the website and in an intuitive way I want to filter the products and find what I am looking for very easily.
    The user has two different ways to filter the products. A dropdown that [filters](/static/docs/images/filters.png) by price, rating and category and another (Home and Nursery) that filters by Cot Bed, Chaning Units, chairs and all products.

2. As a user you will be able to click on them and see their characteristics:
    As a user I would like to have more information about the [product](/static/docs/images/product.png) that I am intended to buy, when the selected product is clicked, it shows the information and has the possibility to be added to the bag or keep shopping if the product is not meeting your expectations.

3. As a user you will be able to add item to the bag:
    Once the product is selected there is a button to [add it to the bag](/static/docs/images/stripe-sucess.png). In this case a message will pop up to inform the user taht the product has been successfully added to the bag.
    
    Also the bag can be modified and the user can [remove](/static/docs/images/stripe_remove.png) an item that is already in there. The user will received another message informing that the product has been successfully removed.

 4. As a user you will be able to check out and pay for your items: 
    The user will be able to do the checkout securely, the user will be redirected to the [shopping bag](/static/docs/images/shoppingbag.png)  screen.
    Once in there the user will click the secure checkout button and be redirected to the [checkout](/static/docs/images/checkout.png) page and being to fill a form in order to get payement and get the product delivered.

    After that the user will see a screen with all the information of the [purchase](/static/docs/images/checkout-success.png) and after clicking the checkout button a new screen with an spinnig icon will show while the payment on [Stripe](/static/docs/images/stripe.png) is being processed.
    After this an email will be send to the address provided.

5. As a superuser you will be able to add, [edit](/static/docs/images/edit-delete.png) and [delete](/static/docs/images/delete.png) products throught the [product management](/static/docs/images/product_management.png) tool


## Deployment

This website has been developed on Gitpod, using Github to host the repository

### Via Gitpod 

These are the step followed to deploy via Gitpod:
1. Log in to the Gitpod account 
2. Chose the Be_my_baby repository
3. Add your code 
4. Type "python3 -m http.server" on the terminal
5. A new screen will pop up with the results of the code on the browser
### GitHub pages

These are the steps followed to deploy this website using GitHub:

1. Log in to your  GitHub account
2. Select Be_my_baby on my repositories
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

The project was developed using GitPod and pushed to GitHub then deployed on Heroku using these instructions:

1. Log in to Heroku and create a new app by clicking "New" and "Create New App" and giving it an original name and setting the region to closest to your location.
2. Navigate to Heroku Resources and add Postgres using the free plan.
3. Create a requirements.txt file using command pip3 freeze > requirements.txt
4. Create a Procfile with the terminal command web: gunicorn be_my_baby.wsgi:application and at this point checking the Procfile to make sure there is no extra blank     line as this can cause issues when deploying to Heroku.
5. Use the loaddata command to load the fixtures for both json files: python3 manage.py loaddata categories.json and python3 manage.py loaddata products.json
6. If it returns error message: django.db.utils.OperationalError: FATAL: role does not exist run unset PGHOSTADDR in your terminal and run the commands in step 11 again.
7. From the CLI log in to Heroku using command heroku login -i.
8. Temporarily disable Collectstatic by running: heroku:config:set DISABLE_COLLECTSTATIC=1 --app So that Heroku won't try to collect static files when we deploy.
9. Add Heroku app name to ALLOWED_HOSTS in settings.py.
10. Commit changes to GitHub using git add ., git commit -m , git push.
11. Then deploy to Heroku using git push heroku main. If the git remote isn't initialised you may have to do that first by running *heroku git:remote -a
12. Create a superuser using command: heroku run python3 manage.py createsuperuser so that you can log in to admin as required.
13. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
14. Search for your GitHub repo and connect then Enable Automatic Deploys.
15. Generate secret key. Strong secret keys can be obtained from MiniWebTool. This automatically generates a secret key 50 characters long with alphanumeric characters and symbols.
16. Add secret key to GitPod variables and Heroku config vars.
17. Set up Amazon AWS S3 bucket 

### AWS S3 Bucket Set up

1. Create an Amazon AWS account
2. Search for S3 and create a new bucket and allow public access
3. On the Properties tab turn on Static website hosting using the default values of index.html and errors.html
4. Under Permissions tab include the CORS configuration using the following:
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]

5. Create security policy: S3 Bucket Policy, allow all principles by adding a * and Amazon S3 services and selecting Get Object action. Paste ARN from Bucket Policy, add statement, generate policy and copy and paste into Bucket Policy. Also add /* at end of resource key to allow use of all pages.
6. Under public access select access to all List Objects.
7. Create Group for the bucket through IAM. Create policy by importing AWS S3 Full Access policy and add ARN from bucket to the policy resources. Attach policy to group.
8. Create user, give programmatic access and add user to the group. Download CSV file when prompted to save access key ID an secret access key to save to environment and config variables.
9. Add AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME = 'eu-west-2' to settings.py.
10. Add, commit and push to GitHub then navigate to Heroku to confirm static files collected successfully on the Build Log. The DISABLE_COLLECTSTATIC variable can now be deleted.
11. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.

### Gmail Client

In settings.py change the DEFAULT_FROM_EMAIL to your own email address.

1. Go to your Gmail account and navigate to the 'Settings' tab.
2. Go to 'Accounts and Imports', 'Other Google Account Settings'.
3. Go to the 'Security' tab, and scroll down to 'Signing in to Google'.
4. If required, click to turn on '2-step Verification**', then 'Get Started', and enter your password.
5. Verify using your preferred method, and turn on 2-step verification.
6. Go back to 'Security', 'Signing in to Google', then go to 'App Passwords'.
7. Enter your password again if prompted, then set 'App' to Mail, 'Device' to Other, and type in Django.
8. Copy and paste the passcode that shows up, this is your 'EMAIL_HOST_PASS' variable to add to your environment/config variables.                'EMAIL_HOST_USER' is the Gmail email address.

## Credits

- I have to thank my mentor Victor Miclovich for suggesting me the germen of the idea for this project, also for his patients and support and providing essential information on the calls during a very challenging time for me.
- To create Be_my_baby I have followed the project Boutique Ado, from the Code Institute. The main functionality for this project has been taken from it. 
- Images: To create this project I have used images from [Babyblooms](https://www.babyblooms.co.uk/collections/home-nursery)
- [Code with Stein](https://www.youtube.com/c/CodeWithStein) has been quite useful in order to create the review section and the blog for this project.
- I have been inspired by the wonderful project that [Suzybee1987](https://github.com/suzybee1987) has done [Knit-happens](https://github.com/suzybee1987/knit-happens) and [Harry Dhillon](https://github.com/Harry-Leepz) with his project [Nourish-and-lift](https://github.com/Harry-Leepz/Nourish-and-Lift)

