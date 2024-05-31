# Django Blog

A simple blog application built with Django 5

## Features

- User authentication (signup, login, logout)
- Create, read, update, and delete blog posts
- Comment on posts
- List all blog posts
- View individual blog posts

## Requirements

- Python 3.8+
- Django 5.0+
- SQLite (default) or any other database supported by Django

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/luifer-villalba/django-blog.git
    cd django-blog
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Register a new user or login with an existing account.
- Create, edit, and delete blog posts.
- Comment on posts.
- Manage posts and comments from the admin panel at `http://127.0.0.1:8000/admin/`