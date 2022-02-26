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
* remove migrations dir from github 
* google wether you should perform computations on a POST resource in the model or view (probably view)
* look up where to specify specific file formats in the html file upload or in the django model
* look up how to add bpm in the view (don't include it in the form and add it to the file variable in the view?)
* clear existing records in database to change model so that every entry must have a valid file
* understand librosa music library
* put create update delete forms on one page and list on another?
* look up how to separate frontend and backend into separate apps 
* watch spotify clone video 
* watch javascript audio player video 
* figure out how to track bpm etc
* write tests

* comment everythinhg
* readme explanation
* lucid hart design diagram

Resources
* How to write an API in 3 lines of code https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4

* Views on views matt layman https://www.mattlayman.com/understand-django/views-on-views/
