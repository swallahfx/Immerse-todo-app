
USAGE
# Activate the virtual environment if not already activated
On Mac use `source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

# Install all dependencies
use `pip install -r requirements.txt`

# Run database migrations
python manage.py migrate

# Create a superuser for admin access (follow the prompts)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
Visit `http://127.0.0.1:8000/swagger/` to interact with the applications on swagger interface



API Endpoints

# User Authentication API:
/api/register/: User registration
/api/login/: User login and JWT token creation
/api/profiles/: Profile Management


To-Do Management API:

/api/todos/: List and create to-do items
/api/todos/<int:pk>/: Retrieve, update, and delete a specific to-do item

