# Use an official Python runtime as a parent image
FROM python:3.10.11

# Set the working directory to /app
WORKDIR /social_media_site

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set environment variables
ENV SECRET_KEY=django-insecure-dalct!2)13oq&2&t7wxe)q90ofjkvg44w)rk2io91)8p_@8f$j
ENV DEBUG=False
ENV DATABASE_URL=postgres://testdb_4c6d_user:xFIu6G3qmqNeOKP1XiXjBvjTVmasqRqK@dpg-ch54g94s3fvqdildms20-a.oregon-postgres.render.com/testdb_4c6d
# ENV DB_NAME=your_db_name
# ENV DB_USER=your_db_user
# ENV DB_PASSWORD=your_db_password
# ENV DB_HOST=db
# ENV DB_PORT=5432

# Expose port 8000 for the Django app
EXPOSE 8000

# Run database migrations and start the Django app
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
