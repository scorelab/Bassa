
![logo](http://gdurl.com/7XYK)
-


Automated Download Queue for Enterprise to take the best use of Internet bandwidth.

###This is the sourecode of Bassa for Windows users.  
The master branch's sourcecode is for Linux users only.  
Follow these instructions to setup and run Bassa on your Windows machine  


## Installation

1. Download python 3.6.0 [here](https://www.python.org/downloads/) (Make sure you download the correct bit distribution).
2. Download (save as) this [file](https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py) -> open up a command prompt with Administrator privileges at its directory -> run `python get-pip.py`  
3. Install NodeJS [here](https://nodejs.org/en/download/)  
4. Execute these codes to install dependencies:  
```
> pip install setuptools
> pip install Flask
> pip install pymysql  
> pip install gulp
> npm install aria2
> npm install -g bower
```

### Main functionalities
* Provides an interface for users to add their downloads as links or torrent magnet links
* Provide users  an interface to view and download the files in local server
* Provide a rating system to users to rate the files residing in local server
* Automatically start and stop downloading in given time frame
* Automatically clean the disks and make room for new downloads
* Notify user when his/her download is completed
* Mark inappropriate downloads
* Provides admins an interface to deal with inappropriate files

====
# Running Bassa

1. Open up a command prompt and redirect to components/core, execute: `python Main.py`. ***Note:*** All server logs go in here.  
2. Open up another command prompt and redirect to components/core, execute:  
`aria2c --enable-rpc --rpc-listen-all --dir <YOUR_DOWNLOAD_DIRECTORY>`
3. Open up another command prompt and redirect to ui/, execute:  
`gulp serve`  
If it's your first time running Bassa, run `npm install` first - this will install all the dependencies for web components used by Bassa (this is a one-time step). Execute `gulp serve` afterwards.  
4. Open up a browser and direct to "localhost/3000", you should be able to use Bassa now. 



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

**http://localhost:5000/api/regularuser**
###### POST
Headers: Content-type : Application/JSON
JSON: ```{"user_name":"<username>", "password":"<password>", "email":"<email>"}  ```

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

**http://localhost:5000/api/download/rate/<id>**
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
Returns file as multipart form data. Does not return a new auth token header

**http://localhost:5000/api/user/requests**
###### GET
Headers: token: <auth token>
Returns a JSON of all the users who has signed up and not been approved yet

**http://localhost:5000/api/user/approve/\<username\>**
###### POST
Headers: Content-type : Application/JSON, token: <auth token>
Approve the user with given username


