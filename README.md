# Django Blog

A feature-rich blog application built with Django 5

## Features

- User authentication (signup, login, logout)
- Create, read, update, and delete blog posts
- Comment on posts
- Tag system for posts using django-taggit
- Post sharing via email
- RSS feed for blog posts
- Similar posts suggestion based on shared tags
- Search functionality using PostgreSQL full-text search
- Sitemap for better SEO
- Pagination for post listings

## Requirements

- Python 3.8+
- Django 5.0+
- PostgreSQL
- Additional packages (see requirements.txt)

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

4. Set up environment variables:

   Create a `.env` file in the project root with the following variables:
   ```
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_email_app_password
   DEFAULT_FROM_EMAIL=your_email@gmail.com
   ```

5. Create PostgreSQL database:
   ```bash
   createdb your_db_name
   ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Register a new user or login with an existing account
- Create, edit, and delete blog posts
- Add tags to posts for better organization
- Share posts via email
- Comment on posts
- Search posts using the search functionality
- Browse posts by tags
- Access the RSS feed at `/blog/feed/`
- Manage posts and comments from the admin panel at `http://127.0.0.1:8000/admin/`

## Testing

Run the test suite:

```bash
python manage.py test
```

The application includes tests for:
- Models (Post creation, validation, tags)
- Views (Post list, detail, sharing)
- URLs (Pattern matching and resolution)

## Email Configuration

The application uses Gmail's SMTP server for sending emails. To set this up:

1. Enable 2-Step Verification in your Google Account
2. Generate an App Password for your application
3. Use this App Password in your `.env` file for `EMAIL_HOST_PASSWORD`

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details