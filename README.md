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
* **Django**
* **Python**
* **HTML, CSS**
* **SQLITE3**
* **Django's Testing Framework**
* **Git**
* **Github**
* **Virtual Environment**
* **Markdown**

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
    ```sh
    cd your-preferred-directory
    ```
3. Clone the project repository from GitHub:
    ```sh
    git clone https://github.com/Oluwatemmy/Yetti-Assessment.git
    ```
4. Set Up a Virtual Environment (Optional but Recommended)
    ```sh
    python -m venv <your-venv-name>
    ```
5. Activate the virtual environment:
    * On Windows:
      ```sh
      venv\Scripts\activate
      ```
    * On macOS and Linux:
      ```sh
      source venv/bin/activate
      ```
6. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
7. Database Setup
    ```sh
    python manage.py migrate
    ```
8. Run the Development Server
    ```sh
    python manage.py runserver
    ```
9. Visit http://localhost:8000 in your browser

10. Running Tests
    To run the tests for the project, you can use the following command:
    ```sh
    python manage.py test
    ```

    This command will execute all the tests in the project, including authentication and security tests.

<p align="right"><a href="#readme-top">back to top</a></p>

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/Oluwatemmy/Yetti-Assessment/blob/main/LICENSE">LICENSE</a> for more information.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Contact

Ajayi Oluwaseyi - [@Oluwatemmy15](https://twitter.com/Oluwatemmy15) - oluwaseyitemitope456@gmail.com

Project Link: [Assessment Repo](https://github.com/Oluwatemmy/Yetti-Assessment)

Documentation: [Link-Ease Wiki](https://github.com/Oluwatemmy/Yetti-Assessment/blob/main/README.md)

<p align="right"><a href="#readme-top">back to top</a></p>


<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/Oluwatemmy/Yetti-Assessment.svg?style=for-the-badge
[contributors-url]: https://github.com/Oluwatemmy/Yetti-Assessment/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Oluwatemmy/Yetti-Assessment.svg?style=for-the-badge
[forks-url]: https://github.com/Oluwatemmy/Yetti-Assessment/network/members
[stars-shield]: https://img.shields.io/github/stars/Oluwatemmy/Yetti-Assessment.svg?style=for-the-badge
[stars-url]: https://github.com/Oluwatemmy/Yetti-Assessment/stargazers
[issues-shield]: https://img.shields.io/github/issues/Oluwatemmy/Yetti-Assessment.svg?style=for-the-badge
[issues-url]: https://github.com/Oluwatemmy/Yetti-Assessment/issues
[license-shield]: https://img.shields.io/github/license/Oluwatemmy/Yetti-Assessment.svg?style=for-the-badge
[license-url]: https://github.com/Oluwatemmy/Yetti-Assessment/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@Oluwatemmy15-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/Oluwatemmy15
[twitter-url]: https://twitter.com/Oluwatemmy15
