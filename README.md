## PROJECT NAME
* GALLERY

## AUTHOR
* Hawa Evakali

## DESCRIPTION
This is a photo gallery web Application where you can view photos and see the details of each photo

## Features
As a user of the application you will be able to:
1. View different photos that interest you.
2. Search for different categories of photos. (ie. Travel, Food)
3. Click on share icon to share the image with any of your social account or alternatively Copy a link to the photo and share with your friends.
View photos based on the location they were taken or category.

## Admin Dashboard
username : `hawa`

password : `2444`

## Installation and setup instructions
1. Clone this repo: git clone
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.
4. To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt

5. On your terminal,Create database gallery using the command below.

CREATE DATABASE gallery;

6. Migrate the database using the command below

python3.8 manage.py migrate

7. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver

8. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## TECHNOLOGIES USED
* Python3.8
* Django
* Heroku
* HTML
* CSS

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

