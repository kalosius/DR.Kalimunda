Set up the virtual enviroment:
 We use pip to install the virtual enviroment
 Activate the virtual enviroment

Configuring Django:
 From the virtual enviroment, Install django with pip
 We create a project in django using django adminstart project
 Then create an application in django using manage.py
 From the second folder in the name as the project we install application in the installed apps in settings.py
 From settings.py you specify where static and template files should be found
 Specify the urls where login and logout redirects should be
 If your going to use crispy_bootstrap4, also include it in the installed apps section: Dont forget to insatll it using pip
 For the first time run migrate for the installed apps in django.("This will create for you a data base")
 After data base,
 Create a super user(python manage.py createsuperuser)
 after, RUN your SERVER

Serving custom templates(html files) amd static files(js and css files, images too)
 Create a directory in the apps directory
 Create a 'templates' directory int the project directory for html files

 from the urls files of the project, specify django to use the urls in your application
 from the urls file in the app, we determine the url string and how it will be responded to
 (We attach a url request string to its corresponding view for response)
  NB:
  some views are installed in django, we just need to use them such as the login and the logout
  url is a way/route to reach a file(html)