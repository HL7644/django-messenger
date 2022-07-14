# django-messenger
Messenger website using Django

#1 AWS Elastic Beanstalk
http://messenger-env.eba-pzkghukm.us-west-2.elasticbeanstalk.com/

#2 To run in your local server
1) download & put messenger file(entire folder) into your desired directory
2) In your directory: in your terminal, use: "virtualenv env" to create virtual environment
3) activate virtual environment using "source env/bin/activate"
4) Install django: "pip install django"
5) go inside the messenger directory: "cd messenger"
6) make migrations and migrate use: "python manage.py makemigrations", "python manage.py migrate" sequentially
7) Run the server: "python manage.py runserver" -> ready to go

