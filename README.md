
![logo](http://gdurl.com/7XYK)
Automated Download Queue for Enterprise to take the best use of Internet bandwidth

## Installation
```
	$ sudo apt-get install libmysqlclient-dev
	$ sudo apt-get install python-dev
	$ cd components/core/
	$ sudo python setup.py develop
```

## Test Server
```
	$ cd components/core/
	$ python Main.py
```

###Main functionalities
* Provides an interface for users to add their downloads as links or torrent magnet links
* Provide users  an interface to view and download the files in local server
* Provide a rating system to users to rate the files residing in local server
* Automatically start and stop downloading in given time frame
* Automatically clean the disks and make room for new downloads
* Notify user when his/her download is completed
* Mark inappropriate downloads
* Provides admins an interface to deal with inappropriate files

## URL endpoints
  
**http://localhost:5000/api/login**  
  
Form data: user_name, password  
Returns auth token in response header for successful login

**http://localhost:5000/api/user**  
###### POST 
Headers: Content-type : Application/JSON, token: <auth token>  
JSON: ```{"user_name":"<username>", "password":"<password>", "auth":<authleval>, "email":"<email>"}  ```   
  
*Auth levals*  
* 0:ADMIN
* 1:STUDENT
* 2:ACADEMIC
* 3:NONACADEMIC
  
###### GET
Headers: token: <auth token>  
Returns JSON of all the users  
###### DELETE
```http://localhost:5000/api/user/<username>  ```  
Deletes the user from system. Adviced not to use.

###### PUT
```http://localhost:5000/api/user/<username>  ```  
Headers: Content-type : Application/JSON, token: <auth token>  
JSON: ```{"user_name":"<username>", "password":"<password>", "auth":<authleval>, "email":"<email>"}  ```   
Update the given user  

**http://localhost:5000/api/user/blocked**  
###### GET
Headers: token: <auth token>  
Returns JSON of all the blocked users  
###### POST  
```http://localhost:5000/api/user/blocked/<username>  ```  
Headers: token: <auth token>  
Block the given user  
  
**http://localhost:5000/api/download**  
###### POST 
Headers: Content-type : Application/JSON, token: <auth token>  
JSON: ```{"link":"<download link>"}  ```   
###### GET
```http://localhost:5000/api/download/<page> ```
Headers: token: <auth token>  
Returns JSON of all the completed downloads. Page contains 15 records ordered by added time. Page number is a int.
  
*Status*  
* 0:DEFAULT- not started
* 1:STARTED - started ot finished yet
* 2:DELETED - download completed but deleted from disk
* 3:COMPLETED - download completed
* 4:ERROR - download error  
  
###### DELETE
```http://localhost:5000/api/download/<id>  ```  
Deletes the download only if it is not starteed  
  
**http://localhost:5000/api/download/rate/<id>  **  
###### POST 
Headers: Content-type : Application/JSON, token: <auth token>  
JSON: ```{"rate":"<rating between 0-5>"}  ```  
Adds the rating to download. If exists, update.  
  
**http://localhost:5000/api/user/downloads/\<page\>**  
###### GET
Headers: token: <auth token>  
Returns JSON of all the downloads of current user. Page contains 15 records ordered by added time. Page number is a int.  
  
**http://localhost:5000/api/download/\<id\>**  
###### GET
Headers: token: <auth token>  
Returns fileas multipart form data. Dose not return a new auth token header


# Bassa UI

### Install dependencies with

`npm install`
`bower install`

### To start
run `gulp`
