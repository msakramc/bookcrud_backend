# bookcrud_backend
bookcrud backend using django

# SAMPLE FOLDER STRUCTURE
|
|____env (this env folder you have to create it using below command)
|____bookcrud_backend (cloned from Github)
|    |_______________bookcrud
|    |_______________config
|    |_______________.env
|    |_______________manage.py       
|    |_______________README.md
|    |_______________requirements.txt
|
|

#Follow these setup virtual environment

1. pip3 install virtualenv

2. virtualenv env
# After executing the command 'virtualenv env', a new folder named "env" will be created.

# To activate the virtual environment, run the following command. 
# Make sure you're in the directory where the "env" folder is located, 
# or adjust the path accordingly.
3. env\Scripts\activate

# Once the virtual environment is activated, you will see (env) at the beginning of your command prompt path.
# For example: (env) C:\Users\username\Desktop\bookcrud_backend>

# Now, navigate to your project folder by using the 'cd' command.
# For example: cd bookcrud_backend
# Open VS Code or any other code editor of your choice.
4. pip install -r requirements.txt

# By default, the database in the .env file is set to SQLite. If you wish to use a different database, please update the settings accordingly.

# Now run below commands
5.python manage.py migrate

6.python manage.py runserver

# Now django server will run in http://127.0.0.1:8000/
