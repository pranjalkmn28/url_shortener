# URL Shrotner Service

## Overview

A simple service to shorten long URLs into shorter, more manageable ones. The application is built using Django and MySQL, and runs in Docker containers for both the web service and the database.

## Features

	•	Shorten long URLs into custom short URLs.
	•	Optionally set an alias for the shortened URL.
	•	Set an expiry time for the shortened URLs.
	•	Store data in a MySQL database.

## Tech Stack
	•	Backend: Django
	•	Database: MySQL
	•	Containerization: Docker
	•	ORM: Django’s built-in ORM for interacting with MySQL.

## Prerequisites

Before running the project, ensure you have the following installed:

- Docker
- Docker Compose

## Setup and Configuration

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/pranjalkmn28/url_shortener.git
cd url_shortener
```

### 2. Create a .env File

Create a `.env` file in the root directory of the project to store environment variables. You can use the provided `.env.example` file as a template. Make sure to set the following variables:

```
# Database Configuration
MYSQL_DATABASE=your_database
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_HOST=your_host
MYSQL_PORT=3306

# Django Secrets
DJANGO_SECRET_KEY=your_django_secret_key
```

### 3. Build and Run with Docker

Build and run the Docker containers using Docker Compose:

```bash
docker-compose up --build
```

This command will:

	•	Set up the MySQL database inside a container.
	•	Set up the Django application inside another container.
	•	Expose the necessary ports for both the web service and MySQL.


### 4. Migrate the Database

After the containers are up, run the following command to apply the database migrations:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```


### 5. Access the Application

Once the containers are up and running, you can access the FastAPI application at:

```
http://localhost:8000/
```

### 6. Creating Short URLs

To shorten a URL:

	1.	Navigate to the home page.
	2.	Enter the long URL, alias (optional), and expiry time (optional).
	3.	Click the “Shorten” button.
	4.	You will be presented with a shortened URL that you can share.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to adjust any specific details related to your project or usage.
