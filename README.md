<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>

<div>
  <p align="center">
    <a href="https://github.com/Oluwatemmy/Yetti-Assessment/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#sample">View Demo</a>
    ·
    <a href="https://github.com/Oluwatemmy/Yetti-Assessment/issues">Report Bug</a>
    ·
    <a href="https://github.com/Oluwatemmy/Yetti-Assessment/issues">Request Feature</a>
  </p>
</div>

<!-- Table of Contents -->
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#about">About</a>
            <ul>
                <li><a href="#authentication">Authentication</a></li>
                <li><a href="#comprehensive-testing">Comprehensive Testing</a></li>
                <li><a href="#built-with">Built With</a></li>
            </ul>
        </li>
        <li>
            <a href="#usage">Usage</a>
            <ul>
                <li>
                <a href="#localhost">Localhost</a>
                <ul>
                    <li><a href="#prerequisites">Prerequisites</a></li>
                    <li><a href="#installation">Installation</a></li>
                </ul>
                </li>
            </ul>
        </li>  
        <li><a href="#sample">Sample</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li> 
    </ol>
    <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About -->
## About

Welcome to my assessment website, a Django-based web application designed to show user authentication and testing. This project demonstrate creating secure and reliable web application.

<p align="right"><a href="#readme-top">back to top</a></p>

### Authentication

The primary goal in this project was to implement robust user authentication, enhancing the security and functionality of the application. Key authentication features include:

- **User Registration**: A user-friendly registration view and URL that allow new users to easily sign up using their email and password.

- **User Login and Logout**: The implementation includes user login and logout views with corresponding URLs, ensuring smooth user interactions.

- **Access Control**: To validate the effectiveness of the authentication system, restriction access was put to the default "Hello World" page, allowing entry only to authenticated users.

<p align="right"><a href="#readme-top">back to top</a></p>

### Comprehensive Testing

To maintaining code quality and ensuring the security of the authentication system. To achieve this, I've implemented a comprehensive suite of tests using Django's testing framework. The test scenarios cover:

- **User Registration**: The unit tests meticulously verify that user registration functions correctly. It ensure that the registration view accurately validates input data and successfully creates new user accounts.

- **User Login and Logout**: This tests works to confirm that users can log in and out without issues, ensuring a seamless authentication process.

- **Access Control**: Unauthorized users are prevented from accessing the task management views, seamlessly redirected to the login page.

- **Error Handling**: The tests cover various edge cases and error scenarios, such as incorrect passwords, non-existent users, logging in with empty fields, and registering with with an existing email.

- **Security Validation**: The tests include checks for potential vulnerabilities like session fixation and CSRF attacks, demonstrating that the user data are always protected

<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:
-**Django**
-**Python**
-**HTML, CSS**
-**SQLITE3**
-**Django's Testing Framework**
-**Git**
-**Github**
-**Virtual Environment**
-**Markdown**

<p align="right"><a href="#readme-top">back to top</a></p>


<!-- Getting Started -->
## Usage

This website can be run locally on your computer.

### Localhost

To run the application locally on your computer, follow the steps below.

#### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

* Python3: [Get Python](https://www.python.org/downloads/)
* Git: [Get Git](https://git-scm.com/downloads)

#### Installation
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to store the project: