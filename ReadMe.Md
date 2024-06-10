# django-BlogApp

## Introduction
AJ-Blogs is a web application developed using Django, Tailwind CSS, and HTML. It provides a platform for users to create and manage their personal blogs. The application allows users to register, log in, and reset their password. Users can also update their profile information and create new blog posts.

## Table of Contents
1. [Installation](#installation)
2. [Features](#features)
   - [User Authentication](#user-authentication)
   - [Password Reset](#password-reset)
   - [Profile Update](#profile-update)
   - [Blog Post Creation](#blog-post-creation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Installation <a name="installation"></a>
To run the AJ-Blogs application locally, follow these steps:

1. Clone the repository from GitHub:
   
   `git clone <repository-url>`
   
   
2. Create a virtual environment and activate it:
   
   `python3 -m venv myenv`
   `source myenv/bin/activate`
   
   
3. Install the required dependencies:
   
   `pip install -r requirements.txt`
   
   
4. Apply the database migrations:
   
   `python manage.py migrate`
   
   
5. Start the development server:
   
   `python manage.py runserver`
   
   
6. Open your web browser and access the application at `http://localhost:8000`.

## Features <a name="features"></a>

### User Authentication <a name="user-authentication"></a>
AJ-Blogs provides user authentication functionality, allowing users to register, log in, and log out of the application. Users can sign up with their email address and password to create an account.

### Password Reset <a name="password-reset"></a>
The application includes a password reset feature that allows users to reset their password if they forget it. To reset the password, the user needs to provide the email address associated with their account. An email will be sent to that address with a link to reset the password. Upon clicking the link, the user can set a new password.

### Profile Update <a name="profile-update"></a>
Users can update their profile information, such as their name, profile picture, and bio. After logging in, users can navigate to their profile page and make changes to their information. The updated profile details will be saved and displayed on the user's profile page.

### Blog Post Creation <a name="blog-post-creation"></a>
AJ-Blogs allows users to create and publish blog posts. Users can compose their blog content, add a title, and select relevant tags or categories for their posts. The created blog posts will be displayed on the main blog page for other users to read and interact with.

## Usage <a name="usage"></a>
1. Registration:
   - Access the application at `http://localhost:8000`.
   - Click on the "Register" button to register a new account.
   - Provide a valid email address and a secure password.
   - Click on the "Register" button to create your account.

2. Login:
   - After registering, you will be redirected to the login page automatically.
   - Enter your username and password.
   - Click on the "Login" button to log in to your account.

3. Password Reset:
   - If you forget your password, click on the "Forgot Password?" link on the login page.
   - Provide the email address associated with your account.
   - Check your email inbox for a password reset email.
   - Open the password reset email and click on the provided link.
   - You will be redirected to a password reset page.
   - Enter a new password and confirm it.
   - Click on the "Reset Password" button to set your new password.

4. Profile Update:
   - After logging in, click on your username or profile picture in the navigation menu to access your profile page.
   - On the profile page, click on the "Edit Profile" button.
   - Update your desired profile information such as name, profile picture, and bio.
   - Click on the "Save Changes" button to update your profile.

5. Blog Post Creation:
   - To create a new blog post, click on the "Create Post" button on the navigation menu or the main blog page.
   - Provide a title for your blog post.
   - Compose your blog content using the available text editor.
   - Select relevant tags or categories for your post.
   - Click on the "Post" button to create and publish your blog post.

Note: The above instructions provide a general overview of the usage of AJ-Blogs. The actual user interface and functionality may vary based on the specific implementation of the project.

## Contributing <a name="contributing"></a>
Thank you for considering contributing to the AJ-Blogs project! If you'd like to contribute, please follow these guidelines:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix.
3. Make your modifications and ensure they adhere to the project's coding style and guidelines.
4. Commit your changes and push them to your forked repository.
5. Submit a pull request with a clear description of your changes.

## License <a name="license"></a>
All Rights are reserved by [Amit Acharya](https://github.com/AJAmit17)
