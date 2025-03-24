# Social Media API
This project implements a user authentication system using Django Rest Framework (DRF). It provides functionality for user registration, login, and token-based authentication. The custom user model includes additional fields for bio, profile picture, and follower relationships.

# Features
 - User Registration: Allow Creation of new user accounts
 - User Login: Allows Created users to login and are provided token authentication
 - Custome User Model: Inherits the AbstractUser class to allow inclusion of custom fields


# Project Setup

1. Clone the repository
2. Create and activate virtual environment in your system
3. Apply Migrations
4. Run the Development Server


# API Endpoints
This Endpoints can be accessed using your browser or Postman

1. Register
- HTTP METHOD: POST
- URL: /accounts/register

- Request Body(JSON):
    `{
        "username": "your_username",  
        "password": "your_password",  
        "email": "your_email"  
    }`

2. Login
- HTTP METHOD: POST
- URL: /accounts/login

- Request Body(JSON):
    `{
        "username": "your_username",
        "password": "your_password"
    }`