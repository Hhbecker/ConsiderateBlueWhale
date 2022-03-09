# ConsiderateBlueWhale

<img src="/images/whale.jpg" style="width:200px;height:170px;"/>

source: https://www.freepik.com/free-photos-vectors/cartoon-whale


This project marks my introduction to python backend development in general and to the Django framework specifically. My original goal was to create a RESTful api for storing music files but I decided to add a simple frontend and integrate that into the backend instead of creating a separate API and frontend. I learned a lot more about web development during this project which makes it a smashing success. 

### What is Django?
Django is a python based web framework that can be used for many different kinds of web applications. Django (without any additional libraries) can be used to create REST compliant APIs. Django REST Framework is a popular library you install on top of Django that makes creating APIs that comply with RESTful rules much easier.


<img src="/images/djangoFlow.jpg" style="width:350px;height:590px;"/>

This drawing shows the general flow of django requests and responses. 


The base url is really localhost/api/list

### Project structure
ConsiderateBlueWhale is the project directory
api is the app directory

These are the api endpoints:
* 
* 
* 

base.html is extended by the individual html templates that are returned by each django view
base.html loads the style.css and functions.js files for use in each template


#### Storing audio files 
* as BLOBs (A binary large object - a collection of binary data stored as a single entity)
* in the filesystem of the server that hosts the API

You could store the relevant information like path, name, description, etc... in the database and keep the file itself on the server filesystem.

The audio file is or is not 

I used function based views 
I used the

## To Do
1. Polish ReadMe 
* add important notes from django, djangoProject, and webDev notes in Notes repo
* get Lucid chart diagram 
2. Figure out how file data is trasnferred around 
3. test it and write down weaknesses and flaws 
6. comment all code 

* understand lower level of how your computer actually communicatess with GET and POST etc


* try to parse api/overview json into something displayable on the frontend 
* figure out where to catch/block improper file formats
* write tests
