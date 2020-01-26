Read at the end how to activate the django environment if you've already set that up.

We're putting our REST API keys/secrets in .env. See .env.example for an example of how your .env should look.
We use https://django-environ.readthedocs.io/en/latest/ 

Beware that if you upgraded Mac OS X recently workon may be broken.
source ~/.bashrc on terminal startup if you've already done the following when bash was the default.
source /Users/mbk/.virtualenvs/my_django_environment/bin/activate

(my_django_environment) ganymede:locallibrary mbk$ python manage.py createsuperuser
Username: admin
Email address: markkauffman2000@gmail.com
Password: 
Password (again): 
Superuser created successfully.

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
sudo pip3 install virtualenvwrapper
macOS virtual environment setup
Setting up virtualenvwrapper on macOS is almost exactly the same as on Ubuntu (again, you can follow the instructions from either the official installation guide or below).

Install virtualenvwrapper (and bundling virtualenv) using pip as shown.

sudo pip3 install virtualenvwrapper
Then add the following lines to the end of your shell startup file.

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
Note: The VIRTUALENVWRAPPER_PYTHON variable points to the normal installation location for Python3, and source /usr/local/bin/virtualenvwrapper.sh points to the normal location of the virtualenvwrapper.sh script. If the virtualenv doesn't work when you test it, one thing to check is that Python and the script are in the expected location (and then change the startup file appropriately).

For example, one installation test on macOS ended up with the following lines being necessary in the startup file:

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
export PROJECT_HOME=$HOME/Devel
source /Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenvwrapper.sh
You can find the correct locations for your system using the commands which virtualenvwrapper.sh and which python3.

$ mkvirtualenv my_django_environment

$ workon my_django_environment

There are just a few other useful commands that you should know (there are more in the tool documentation, but these are the ones you'll use regularly):

deactivate — Exit out of the current Python virtual environment
workon — List available virtual environments
workon name_of_environment — Activate the specified Python virtual environment
rmvirtualenv name_of_environment — Remove the specified environment.

$ pip3 install django

mkdir django_test
cd django_test
You can then create a new skeleton site called "mytestsite" using the django-admin tool as shown. After creating the site you can navigate into the folder where you will find the main script for managing projects, called manage.py.

django-admin startproject mytestsite
cd mytestsite
We can run the development web server from within this folder using manage.py and the runserver command, as shown.

$ python3 manage.py runserver 
Performing system checks...

