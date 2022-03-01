# ConsiderateBlueWhale
A RESTful CRUD API for audio files built with Django

Read back through django docs and drf docs

#### Storing audio files 
* as BLOBs (A binary large object - a collection of binary data stored as a single entity)
* in the filesystem of the server that hosts the API

You could store the relevant information like path, name, description, etc... in the database and keep the file itself on the server filesystem.

I used function based views 
I used the

## To Do
* develop bpm function in separate file then define it in views.py and call it within create view

* call bpm function from within update too
* change download column from list page to update and add a delete button

* possibly add music player to list page 

* look up where to specify specific file formats in the html file upload or in the django model
* clear existing records in database to change model so that every entry must have a valid file

* watch spotify clone video 
* watch javascript audio player video 
* write tests

* comment everythinhg
* readme explanation
* lucid chart design diagram

### Resources
* How to write an API in 3 lines of code https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4

* Views on views matt layman https://www.mattlayman.com/understand-django/views-on-views/
