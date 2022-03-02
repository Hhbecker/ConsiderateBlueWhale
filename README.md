# ConsiderateBlueWhale
A Django web application that tracks the bpm of uploaded audio files.

This project marks my introduction to python backend development in general and to Django specifically. My original goal was to create a RESTful api for storing music files but I decided to add a simple frontend and integrate that into the backend instead of creating a separate API and frontend. I learned a lot more about web development during this project which makes it a smashing success. 

### What is Django?
Django is a python based web framework that can be used for many different kinds of web applications. Django (without any additional libraries) can be used to create REST compliant APIs. Django REST Framework is a popular library you install on top of Django that makes creating APIs that comply with RESTful rules much easier.


<img src="/images/djangoFlow.png">

This drawing shows the general flow of django requests and responses. 



#### Storing audio files 
* as BLOBs (A binary large object - a collection of binary data stored as a single entity)
* in the filesystem of the server that hosts the API

You could store the relevant information like path, name, description, etc... in the database and keep the file itself on the server filesystem.

I used function based views 
I used the

## To Do
* can't get delete page to refresh automatically
* can't get update form to change url back to just /api/list/ after you submit it
* can't switch out link to update to a button

* unclear on how file data is passed along in POST requests and responses
* don't understand how to return serialized json objects that the frontend parses through (separating fontend and backend)

* possibly add music player to list page (watch spotify clone and vanilla js audio player videos)
* figure out where to catch/block improper file formats

* write tests

* comment everythinhg
* readme explanation with lucid chart design diagrams


### Resources
* How to write an API in 3 lines of code https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4

* Views on views matt layman https://www.mattlayman.com/understand-django/views-on-views/
