# Social Meet Backend
Social Meet Backend is a project that provides a backend solution for a social networking platform. This project uses Django, Django Rest Framework, and PostgreSQL to build the backend APIs that can be used by the frontend application to handle user authentication, friend requests, messaging, and other social features.


## Features
* User authentication
* User registration and login
* Friend requests and messaging
* User profiles and social feeds
* Data persistence with PostgreSQL


## Installation
To install and run Social Meet Backend, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/preciousimo/social_meet_backend.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the server:
```bash
python manage.py runserver
```

## API Documentation
The Social Meet Backend project offers a RESTful API that follows the best practices of API design, with a clear separation of concerns between the API views, serializers, and models. The API documentation can be found in the [API documentation file](API_DOC.md). You can use this documentation to explore the available endpoints, their inputs and outputs, and the expected behavior.


## Contributing
This project is designed to be scalable and can be used as a starting point for building a social networking platform or as a learning resource for developers who want to learn how to build backend APIs for social apps. If you're interested in contributing to the project, feel free to fork it and submit pull requests. We welcome contributions of any kind, including bug fixes, new features, and documentation improvements.


## Acknowledgements
* [Django Docs](https://docs.djangoproject.com/en/4.2/)
* [DRF Docs](https://www.django-rest-framework.org/)
