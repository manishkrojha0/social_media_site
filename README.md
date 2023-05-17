### Social Media Site

- This is a social media platform built with Django and Django Rest Framework (DRF). The application allows users to create accounts, create and edit their profiles, follow     and unfollow other users, add posts and view posts and like or comment on the post.
### Installation and Setup

    - Clone this repository using git clone https://github.com/manishkrojha0/social_media_site.git
    - Navigate to the project directory cd social_media_site
    - Install project dependencies using pip install -r requirements.txt
    - Run the migrations file by command  python manage.py migrate
    - Run the application using python manage.py runserver

### Test cases
  - test cases to test the urls and endpoints of the project.
    - ``python manage.py test core.test_cases``

### Docker

- A Dockerfile and docker-compose.yml file have been provided for easy deployment. To deploy the application using Docker, follow these steps:

    - Clone this repository using git clone [https://github.com/manishkrojha0/social_media_site](https://github.com/manishkrojha0/social_media_site.git)
    - Navigate to the project directory cd social_media_site
    - Run this command for creating the Docker image.
        ```bash
           docker buid .
    - Run this commant to build the multiple Docker images if you want.
      ```bash
         docker-compos
         
    - Run this command to start the Docker container
       ```bash
          docker-compose up** 
    - Access the application at http://0.0.0.0:8000/

### Deployment
 - Deployment has been done on render, link to my deployed url - https://minsta-ymk1.onrender.com/admin
 - You have to go through the postman api collections, I've mentioned below.

### API Endpoints

- POSTMAN API COLLECTIONS - [social_media_site](https://rb.gy/93ahy)
