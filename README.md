ConsiderateBlueWhale

<p align="center">
<img src="/images/whale.jpg" style="width:200px;height:170px;"/>
</p>

This project marks my introduction to web development with the Django Web Framework. I've created a simple CRUD capable website made up of Django views that interact with the sqlite database to serve html templates. The website allows for upload and streaming of audio files while tracking the audio file bpm (this is a proof of concept for whatever other audio processing task I might want to perform). I've started to separate the front end and the backend to convert the current backend portion into a strict RESTful api with a separate application for the frontend but this separation is still under construction. I learned a lot more about web development during this project which makes it a smashing success. 

### Project structure
Project name: "ConsiderateBlueWhale"</br>
App name: "api"

#### Database
Default django sqlite3

#### Backend
* model forms for 'create' and 'update' functionality
* function based views that render html templates as their return value

#### Front End
django templates using:
* base html which is extended in each template
* some bootstrap css
* a little javascript

Templates:
* create file form
* list of files in database with options to play, update, or delete a given file
* update file form


### Uploading and storing audio files 
Files were saved on a Model with a FileField, using a ModelForm. When the user submits the form on the frontend, a connection is made between the local outgoing port and the server's incoming port. The file data is packetized, sent through the network, reassembled, and passed into the appropriate django view where it is converted to an instance of the model class. At this point the actual data is stored in RAM and is only written to the disk file system when the `.save()` function is called on the object instance. 


### What is Django?
Django is a python based web framework that can be used for many different kinds of web applications. Django (without any additional libraries) can be used to create REST compliant APIs. Django REST Framework is a popular library you install on top of Django that makes creating APIs that comply with RESTful rules much easier.

<img src="/images/djangoFlow.jpg" style="width:350px;height:590px;"/>

This drawing shows the general flow of django requests and responses. 

#### Django Rest Framework vs regular Django 
* normal Django uses HTTP response but Django REST API uses JSON response.
* models are the same
* add model serializers 
* make generic views that are slightly different 
* no templates b/c its just data

### What is an API?
An API, or application programming interface, is a set of rules that define how applications or devices can connect to and communicate with each other. APIs are the code that governs the access points between a database and a server.

It’s sometimes referred to as a contract between an information provider and an information user—establishing the content required from the consumer (the call) and the content required by the producer (the response). 

An interface creates a box around part of a program and says "here is what can go in and out of this box". An Application Programming Interface is an interface used in big applications to decouple/abstract/seperate different parts of a codebase while ensuring many different application components communicate safely and correctly. If you need a frontend and a backend it might be best to establish an interface between the frontend and backend so the two parts can be developed independently as long as the rules of the interface are followed. 

<img src="/images/webServer.jpeg" style="width:720px;height:442px;"/>

This diagram shows the API as a regulated gateway between the frontend and the database.

### What is a CRUD API? 
A CRUD API is an API that establishes the rules for/allows for create, read, update, and delete communications to occur between the the entities on either side of the API. 

CRUD stands for:
* CREATE - generate new records via INSERT statements.
* READ - reads the data based on input parameters. Similarly, RETRIEVE procedures grab records based on input parameters.
* UPDATE - modify records without overwriting them.
* DELETE - delete where specified.

### What is a RESTful API?
REST is a set of architectural constraints of the representational state transfer architectural style. The principles of RESTful architecture serve to create a stable and reliable application that offers simplicity and end-user satisfaction.

#### RESTful criteria:
* A client-server architecture made up of clients, servers, and resources, with requests managed through HTTP.
* Stateless client-server communication, meaning no client information is stored between get requests and each request is separate and unconnected.
* A uniform interface between components so that information is transferred in a standard form. This requires that:
resources requested are identifiable and separate from the representations sent to the client. 
* Self-descriptive messages returned to the client have enough information to describe how the client should process it.
* Hypertext/hypermedia is available, meaning that after accessing a resource the client should be able to use hyperlinks to find all other currently available actions they can take.
* A layered system that organizes each type of server (those responsible for security, load-balancing, etc.) involved in the retrieval of requested information into hierarchies, invisible to the client.

---------------------------------------------------------------------
## To Do

https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/

What is the best way to get form data from frontend app to api?


* add edit and delete button actions
* add file update and file upload html pages 
* api overview should get a json response form the api 

* add tailwind css to style everything
1. comment new javascript
2. test all functions and write down all weaknesses and flaws 

* create a view that allows you to filter records by title or artist
* figure out where to catch/block improper file formats
* write tests


----------
Briefly go through and comment code 

try returning json to detail view 

make a new app called frontend and try to pass detail view to frontend 

regroup