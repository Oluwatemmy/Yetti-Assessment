from django.test import TestCase
from django.urls import reverse
from .forms import UserRegistrationForm 
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware


# Create your tests here.
class RegistrationTestCase(TestCase):
    def setUp(self):
        # Create a test user for use in login and registration tests
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        
    # test user registration form
    def test_registration_form(self):
        form_data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'password123',
        'password2': 'password123',
        }
        response = self.client.post(reverse('register'), form_data)
        form = UserRegistrationForm(data=form_data)
        self.assertTemplateUsed(response, 'users/register.html') # check if the register.html template was used
        if form.is_valid():
            new_user = form.save()
            self.assertTrue(User.objects.filter(username='newuser').exists())  # Check if user is created
            
class LoginLogoutTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    # test login with valid credentials
    def test_login(self):
        # log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # sends a get request to the homepage
        response = self.client.get(reverse('homepage'))
        
        # Check if the user is logged in
        self.assertTrue(response.context['user'].is_authenticated)
        
        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check for specific contentin the response
        self.assertContains(response, 'Hello World!')
        
    # test login with invalid credentials
    def test_login_invalid(self):
        #Login with wrong credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })        
        # Check that the response status code indicates login failure
        self.assertIn(response.status_code, [200, 401])
        # Check for specific content in the response that indicates a login failure
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
        
    # Test logout route
    def test_logout(self):
        # Log in the user before testing the logout
        self.client.login(username='testuser', password='testpassword')
        
        # sends a get request to the homepage
        response = self.client.get(reverse('homepage'))
        
        # Check if the user is logged in
        self.assertTrue(response.context['user'].is_authenticated)
        
        # Log out the user
        self.client.logout()
        
        # sends a get request to the logout
        response = self.client.get(reverse('logout'))
        
        # Check if the user is logged in
        self.assertFalse(response.context['user'].is_authenticated)
        

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_authenticated_access(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Send a GET request to the homepage view
        response = self.client.get(reverse('homepage'))
        
        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check for specific contentin the response
        self.assertContains(response, 'Hello World!')
        
    def test_unauthenticated_access(self):
        # Send a GET request to the homepage view
        response = self.client.get(reverse('homepage'))
        
        # Assert that the response status code indicates redirection (302) or unauthorized access (403/401)
        self.assertIn(response.status_code, [302, 403, 401])
        
        # Chcek if the user is redirected to the login page
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('homepage'))
        

class ErrorCaseTestCase(TestCase):
    def setUp(self):
        # Create a test user for use in login tests
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
    
    # Test login with non-existent user
    def test_login_non_existent_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'non_existent_user',
            'password': 'testpassword'
        })        
        # Check that the response status code indicates login failure
        self.assertIn(response.status_code, [200, 401])
        
        # Check for specific content in the response that indicates a login failure
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')


    # Test login with empty username or password fields
    def test_login_empty_fields(self):
        response = self.client.post(reverse('login'), {
            'username': '',
            'password': ''
        })
        # Check that the response status code indicates login failure
        self.assertIn(response.status_code, [200, 401])

    # Test registration with an email that already exists
    def test_registration_existing_email(self):
        form_data = {
            'username': 'newuser',
            'email': 'test@example.com',  # Use an email that already exists
            'password1': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(reverse('register'), form_data)
        form = UserRegistrationForm(data=form_data)
        
        # Check that the response status code indicates registration failure
        self.assertEqual(response.status_code, 200)
        
        # Optionally, check for a specific error message in the response
        self.assertContains(response, 'A user has already registered using this email')
        
        
class SecurityTestCase(TestCase):
    def test_csrf_present(self):
        # Django automatically includes CSRF tokens in forms
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken')
    
    # Test CSRF protection by sending a POST request without a CSRF token
    def test_csrf_protection(self):
        # Send a POST request without a CSRF token
        response = self.client.post(reverse('homepage'), data={})
        
        # Check that the response status code indicates a CSRF failure (usually 403 or 302)
        self.assertIn(response.status_code, [403, 302])
        
     # Test session fixation protection by checking for a new session ID after login
    def test_session_fixation_protection(self):
        # Log in a user
        self.client.login(username='testuser', password='testpassword')
        
        # Get the session ID after login
        session_id_after_login = self.client.session.session_key
        
        # Log out the user
        self.client.logout()
        
        # Log in the user again
        self.client.login(username='testuser', password='testpassword')
        
        # Get the session ID after the second login
        session_id_after_second_login = self.client.session.session_key
        
        # Check that the session ID has changed after login (indicating session fixation protection)
        self.assertNotEqual(session_id_after_login, session_id_after_second_login)
