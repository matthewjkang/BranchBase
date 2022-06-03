#UPDATE : Its up and live at blog.mattkang.com


## A blog web application that I wrote in Django.  

### How to use it : 

1. fork the repo
2. enter into the project directory through the terminal
3. Create, equip, and start your python virtual environment
    * 'python3 -m venv venv'
    * 'pip install -r django_project/requirements.txt'
    * 'source venv/bin/activate'
    * your virtual env should not be inside of the django_project directory btw
4. 'cd django_project'
5. 'python3 manage.py runserver'
    *If something goes wrong, try running 'python3 manage.py migrate', then 'python3 manage.py makemigrations'

### If you are on an m1 mac ...

For some reason the PIL python library does not want to work on m1 macs. If you are running this in your terminal, make sure that you are running it in Rosetta mode. 

### Lessons that I've learned

1. Deploying an application for production requires a lot more work than I would have expected.
    * Handling thing's like secret keys and AWS keys requires reading more documentation about how to safely store them.
2. An exposed secret key gives hackers the opportunity to turn YOUR system into THEIR system. 
