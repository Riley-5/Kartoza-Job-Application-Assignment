# Portfolio App

## How to start the application
**Docker**\
If you have Docker and Docker Compose installed run the following in your terminal
```
docker compuse up
```
Go to localhost:8000 in your browser to open the app

**Normal Python**\
If you do not have Docker or want to run the application with Python run the following in your terminal
```
python3 manage.py runserver
```
Go to localhost:8000 in your browser to open the app

---

## How to run unit tests
To run the unit tests in your terminal run
```
python3 manage.py test
```

---

## App Requirements
- [x] Extend Django user model to include home address, phone number, location (point geometry) where they live
- [x] A user profile page and a page to edit the user's profile
- [x] A page with a full screen map that shows all registered users location
- [x] When clicking the user icon, it will display the user's profile in a popup
- [ ] Users can login from the default Django admin page. User can only se their own profile page, but not others 
- [x] User can only access Django admin page for all models by logging in as a super user
- [x] Add test cases
- [x] CI integration so that when new code is added via a pull request (PR), the code will be automatically tested and and indicator as to whether the tests have passed or not will be displayed 
- [x] Sign up and sign in page
- [ ] Log the user login/logout activity by showing who and when on the admin page
- [x] Push work to GitHub

**Problem Areas**\
Users can login via the admin page but they cannot see any other models or their own profile... But when on the app if they sign in via the admin page or the app sign in page the user will only be able to view their profile. 

Logging the user login and logout activities prints the users username and when they logged in or out to the console instead of logging the output to the Django admin page.

---

