import pytest
import subprocess
import os
from config import TestingConfig
from app.models import User, Transaction, Category
from flask_login import login_user
from datetime import datetime, timezone
from app import create_app

# Setup tests
@pytest.fixture()
def app():
    app = create_app(TestingConfig)
    yield app

# Setup test client
@pytest.fixture
def client(app):
    from app import db
    with app.app_context():
        db.create_all()
        print(f"Testing with database:{app.config['SQLALCHEMY_DATABASE_URI']}")
        with app.test_client() as client:
            yield client
        db.session.remove()
        db.drop_all()

# Some helper fixtures to reduce repetition
@pytest.fixture
def init_database():
    from app import db
    # Setup test user
    user = User(username='testuser', email='testuser@example.com')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()

@pytest.fixture
def logged_in_client(client,init_database,app):
    # Log in the user before running the test
    # client.post('/login', data=dict(username='testuser', password='password'))
    with app.test_request_context():
        user = User.query.first()
        login_user(user)
    return client

@pytest.fixture
def init_transaction(init_database):
    from app import db
    # Setup test user
    user = User.query.first()
    # set-up test transaction
    cat = Category(name='Groceries', user=user)
    db.session.add(cat)
    t = Transaction(description = 'Buy Bread',
        amount = 5.00,
        transaction_type = 'expense',
        date=datetime.now(timezone.utc),
        user = user,
    )
    t.categories.append(cat)
    db.session.add(t)
    db.session.commit()

###  Start of test Suite

def test_database_config(client, app):
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'

def test_home_page(logged_in_client):
    response = logged_in_client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_add_transaction_page(logged_in_client):
    # Test that the add transaction page loads and contains the transaction form
    response = logged_in_client.get('/transactions/add')
    assert response.status_code == 200
    assert b'Add Transaction' in response.data  # Check if the page title is present
    assert b'<form' in response.data  # Check if a form is present

def test_edit_transaction_page(logged_in_client,init_transaction):
    # Test that the edit transaction page loads (mock id)
    response = logged_in_client.get('/transactions/1')
    assert response.status_code == 200
    assert b'Edit Transaction' in response.data  # Check if the page title is present

def test_manage_categories_page(logged_in_client):
    # Test that the manage categories page loads and contains the category form
    response = logged_in_client.get('/categories/add')
    assert response.status_code == 200
    assert b'Manage Categories' in response.data  # Check if the page title is present
    assert b'<form' in response.data  # Check if a form is present

def test_reports_page(logged_in_client):
    # Test that the reports page loads correctly
    response = logged_in_client.get('/reports')
    assert response.status_code == 200
    assert b'Reports' in response.data  # Check if the page title is present

def test_form_validation(logged_in_client):
    # Test that form fields have client-side validation (e.g., 'required' attribute)
    response = logged_in_client.get('/transactions/add')
    assert b'required' in response.data  # Check if 'required' attribute is used

def test_template_inheritance(client):
    # Test that base.html is being used (assume base.html contains the word 'Footer')
    response = client.get('/login')
    assert b'footer' in response.data  # Check if footer text is present

def test_static_css(client):
    # Test that a CSS file is available and linked correctly
    response = client.get('/login')
    assert b'<link' in response.data  # Check if a link tag is present
    assert b'.css' in response.data  # Check if a CSS file is linked
    
def test_git_commits():
    # Check that at least one commit exists in the Git repository
    result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True)
    commit_count = int(result.stdout.strip())
    assert commit_count > 0, "No Git commits found"

def test_git_ignore():
    # Ensure a .gitignore file exists to handle unwanted files
    assert os.path.exists('.gitignore'), ".gitignore file not found"


def test_user_model(client):
    from app import db
    user = User(username='newuser', email='newuser@example.com')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
    assert User.query.count() == 1

def test_user_registration(client):
    # Attempt to register a new user through the registration form
    response = client.post('/register', data=dict(
        username='registeruser',
        email='registeruser@example.com',
        password='password',
        confirm_password='password',
        submit='submit'
    ), follow_redirects=True)

    # Check that the registration was successful by verifying response and database
    assert response.status_code == 200
    assert b'Account created successfully' in response.data  # Check for success message
    assert User.query.filter_by(username='registeruser').first() is not None  # Check if user exists in the DB


def test_logout_protection(client, init_database):
    response = client.get('/transactions/add')
    assert response.status_code == 302 #redirect to login page if not logged in

def test_login(client, init_database):
    response = client.post('/login', data = dict(username='testuser', password='password', submit='Login' ), follow_redirects = True)
    assert response.status_code == 200
    assert b'Welcome, testuser!' in response.data

def test_add_transaction(client, init_database):
    from app import db
    user = User.query.first()
    category = Category(name='Groceries', user=user)
    db.session.add(category)
    db.session.commit()
    assert Category.query.count() == 1
    
    client.post('/login', data=dict(username=user.username, password='password'))
    
    response = client.post('/transactions/add', data= dict(
        description = 'Buy Milk',
        amount = 1.82,
        categories = [1],
        transaction_type = 'expense',
        date = '2024-09-19',
        submit='submit'
    ), follow_redirects = True)
    assert response.status_code == 200
    assert Transaction.query.count() == 1
    assert Transaction.query.first().description == 'Buy Milk'

def test_edit_transaction(logged_in_client, init_transaction):
    from app import db
    transaction = Transaction.query.first()
    assert Transaction.query.count() == 1
    response = logged_in_client.post(f'/transactions/{transaction.id}', data= dict(
        description = 'Buy Milk',
        amount = 1.82,
        categories = [1],
        transaction_type = 'expense',
        date = '2024-09-19',
        submit='submit'
    ), follow_redirects = True)
    assert response.status_code == 200
    assert Transaction.query.count() == 1
    assert Transaction.query.first().description == 'Buy Milk'
    assert Transaction.query.first().amount == 1.82

def test_delete_transaction(logged_in_client, init_transaction):
    from app import db
    transaction = Transaction.query.first()
    assert Transaction.query.count() == 1
    response = logged_in_client.get(f'transactions/delete/{transaction.id}', follow_redirects=True)
    assert response.status_code == 200
    assert Transaction.query.count() == 0

def test_add_category(logged_in_client,init_database):
    from app import db
    response = logged_in_client.post('/categories/add', data = dict(name='Entertainment'), follow_redirects = True)
    
    assert response.status_code == 200
    assert b'Entertainment' in response.data
    assert Category.query.filter_by(name='Entertainment').first() is not None

def test_category_validation(logged_in_client, init_database):
    response = logged_in_client.post('/categories/add', data = dict(name=''), follow_redirects = True) # empty category name
    
    assert b'This field is required' in response.data  #should return validation error message

def test_transaction_amount_validation(logged_in_client, init_database):
    from app import db
    user = User.query.first()
    category = Category(name='Groceries', user_id=user.id)
    db.session.add(category)
    db.session.commit()
    
    # Attempt to add a transaction with a negative amount (invalid)
    response = logged_in_client.post('/transactions/add', data= dict(
        description = 'Buy Milk',
        amount = -1.82,  # Invalid amount
        categories = [1],
        transaction_type = 'expense',
        date = '2024-09-19',
        submit='submit'    ), follow_redirects = True)
    
    assert b'Invalid amount' in response.data # Expect validation error for negative amount
    assert Transaction.query.count() == 0
