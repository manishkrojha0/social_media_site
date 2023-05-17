### Social Media Site

- This is a social media platform built with Django and Django Rest Framework (DRF). The application allows users to create accounts, create and edit their profiles, follow     and unfollow other users, add posts and view posts and like or comment on the post.
### Installation and Setup

- Clone this repository 
   ```bash
   git clone https://github.com/manishkrojha0/social_media_site.git
- Navigate to the project directory
  ```bash 
  cd social_media_site
- Create a new virtual environment:
  ```bash
  python -m venv venv
- Install project dependencies
  ``` bash
  pip install -r requirements.txt
- Run the migrations file by command
  ```bash
  python manage.py migrate
- Run the application
  ```bash
  python manage.py runserver

### Test cases
  - test cases to test the urls and endpoints of the project.
     ```bash 
     python manage.py test core.test_cases

### Docker

- A Dockerfile and docker-compose.yml file have been provided for easy deployment. To deploy the application using Docker, follow these steps:

    - Clone this repository
      ```bash
      git clone [https://github.com/manishkrojha0/social_media_site](https://github.com/manishkrojha0/social_media_site.git)
    - Navigate to the project directory
      ```bash
      cd social_media_site
    - Run this command for creating the Docker image.
        ```bash
        docker build -t social_media_platform .
    - Run this commant to build the multiple Docker images if you want.
      ```bash
         docker-compose build       
    - Run this command to start the Docker container
       ```bash
          docker-compose up
    - Run the Docker container:
       ```bash
          docker run -p 8000:8000 social_media_platform
    - Access the application at http://0.0.0.0:8000/

### Deployment
 - Deployment has been done on render, link to my deployed url - https://minsta-ymk1.onrender.com/admin
 - You have to go through the postman api collections, I've mentioned below.

### API Endpoints

- POSTMAN API COLLECTIONS - [social_media_site](https://rb.gy/93ahy)
