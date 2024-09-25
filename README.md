# Pick 'n' Pack

This document propose the design of an online grocery market for the retail 
supplies of fresh food items at a uniform price anywhere in Nigeria (excluding the delivery cost), 
where customers can make purchase online from anywhere in the country using their electronic mobile 
device and complete payment online, and they can receive their supplies in short time 
(less than 4 hours depending on proximity) after completing the transaction

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Installation

1. **Prerequisites**: List any software, packages, or configurations needed before installation.
    - Example: Python 3.10
    - Example: Flask 3.0.3

2. **Clone the Repository**:
    ```bash
    git clone https://https://github.com/MahoneyT1/Pack_n_pick.git
    ``` 

3. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

    ```

5. Set up environment variables (Optional, if applicable):
   ```
   export FLASK_APP=run.py
   export FLASK_ENV=.Pick_n_pack_env
   ```

6. Run the application:
   ```
   flask run
   ```

2.  ## **Features**
    ``` User authentication (Login/Signup)
    - Create, update, delete, and view tasks
    - search and filter products
    ```

3.  ## ** Usage**
    - After installation, open your browser and navigate to:
    http://localhost:5000

    You can interact with the following endpoints (examples for an API):

    GET /users - Retrieves list of users
    POST /users/<user_id> posts new user
    PUT /users/<user_id> updates users
    DELETE /users/<user_id> deletes user

    GET /products - Retrieves list of products
    POST /products/<product_id> posts new product
    PUT /products/<product_id> updates products
    DELETE /products/<product_id> deletes products

    GET /suppliers - Retrieves list of suppliers
    POST /suppliers/<supplier_id> posts new supplier
    PUT /suppliers/<supplier_id> updates suppliers
    DELETE /suppliers/<supplier_id> deletes supplier

    GET /orders - Retrieves list of orders
    POST /orders/<order_id> posts new order
    PUT /orders/<order_id> updates orders
    DELETE /orders/<order_id> deletes order

    ## Configuration
        FLASK_APP:app.api.v1.app Entry point
        DATABASE_URL: connection_string = f"mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
                    mysql database isn't deployed online yet, you can create a database locally for testing purposes

        SECRET_KEY: you-will-never-guess

    ### **Technologies Used**
        ```
        - Flask
        - SQLALchemy
        - Jinja2
        - Mysql
        - Flask-login
        - Flask-wtf
        - Flask-migrate
        - email valiator
        ```

    ### **Acknowledgments**
        ```
        I thank my partner who has shown great strength so far even with the project been completed due to lack of power in our country, We have been able to get this far and will also complete the project after the presentation.

        Special thanks to Flask Mega Tutorial where i learned most of the technologies used here (Miguel Grinberg)
        ```
    ### **Main Contributors**
        ```
        - Ifeanyi kenneth Victor ([ifeanyitech15@gmail.com](mailto:ifeanyitech15@gmail.com)) 
    ```                                               