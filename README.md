[![Build Status](https://travis-ci.org/scorelab/Bassa.svg?branch=master)](https://travis-ci.org/scorelab/Bassa)
[![PyPI](https://img.shields.io/pypi/dm/Bassa.svg)]()
[![PyPI](https://img.shields.io/pypi/v/Bassa.svg)]()
![logo](http://gdurl.com/7XYK)

Automated Download Queue for Enterprise to take the best use of Internet bandwidth

### About 
Bassa solves the problem of wasting internet bandwidth by queuing a download if it is larger than a given threshold value in high traffic and when the traffic is low, it completes the download of the files. After the files are downloaded, the users can get their files from the local servers which do not require external internet bandwidth.

## Installation

Use python 3 instead of Python 2

```
  $ ./setup.sh
  $ cd components/core/
  $ sudo python setup.py develop
```
## Database Setup

1. Type below in a MySql terminal.

```
create database Bassa
```

2. Type below in the root of project.

```
mysql -u root -p  Bassa < Bassa.sql
```

3. Open components/core/DBCon.py and setup database username and password.


## Test Server
```
  $ cd components/core/
  $ python Main.py
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

### How to Use Bassa
* After Setting up Bassa, Login/Register.There are two types of users in Bassa- (1) The Admin and (2) The Normal Users.
* A user can add a link through the webapp and Bassa stores it in the local server right away. This way multiple users can add various links, but the downloads won’t start right away. 
* The organisation admin can start the downloads at a time of his/her liking. 
* Then the users who had added links for certain files can download them from the local servers at a much higher speed.

## URL endpoints

**/api/login**

Form data: user_name, password
Returns a auth token in response header for a successful login

**/api/user**
###### POST
Headers: Content-type : Application/JSON, token: <auth token>
JSON: ```{"user_name":"<username>", "password":"<password>", "auth":<authleval>, "email":"<email>"}  ```

*Auth levels*
* 0:ADMIN
* 1:STUDENT
* 2:ACADEMIC
* 3:NONACADEMIC

###### GET
Headers: token: <auth token>
Returns a JSON of all the users
###### DELETE
```/api/user/<username>  ```
Deletes the user from system. Adviced not to use.

###### PUT
```/api/user/<username>  ```
Headers: Content-type : Application/JSON, token: <auth token>
JSON: ```{"user_name":"<username>", "password":"<password>", "auth":<authleval>, "email":"<email>"}  ```
Update the given user

**/api/regularuser**
###### POST
Headers: Content-type : Application/JSON
JSON: ```{"user_name":"<username>", "password":"<password>", "email":"<email>"}  ```

**/api/user/blocked**
###### GET
Headers: token: <auth token>
Returns a JSON of all the blocked users
###### POST
```/api/user/blocked/<username>  ```
Headers: token: <auth token>
Blocks the given user

**/api/download**
###### POST
Headers: Content-type : Application/JSON, token: <auth token>
JSON: ```{"link":"<download link>"}  ```
###### GET
```/api/download/<page> ```
Headers: token: <auth token>
Returns JSON of all the completed downloads. Page contains 15 records ordered by added time. Page number is a int.

*Status*
* 0:DEFAULT- not started
* 1:STARTED - started ot finished yet
* 2:DELETED - download completed but deleted from disk
* 3:COMPLETED - download completed
* 4:ERROR - download error

###### DELETE
```/api/download/<id>  ```
Deletes the download only if it is not started.

**/api/download/rate/<id>**
###### POST
Headers: Content-type : Application/JSON, token: <auth token>
JSON: ```{"rate":"<rating between 0-5>"}  ```
Adds the rating to download. If exists, update.

**/api/user/downloads/<page>**
###### GET
Headers: token: <auth token>
Returns a JSON of all the downloads of current user. Page contains 15 records ordered by added time. Page number is a int.

**/api/download/<id>**
###### GET
Headers: token: <auth token>
Returns file as multipart form data. Does not return a new auth token header

**/api/user/requests**
###### GET
Headers: token: <auth token>
Returns a JSON of all the users who has signed up and not been approved yet

**/api/user/approve/<username>**
###### POST
Headers: Content-type : Application/JSON, token: <auth token>
Approve the user with given username

# Bassa UI

### Install dependencies with


```
$ cd ui/
$ npm install
```

### Autoformat JS with Prettier

- [Sublime Text Plugin](https://github.com/jonlabelle/SublimeJsPrettier)
- [Atom Plugin](https://github.com/prettier/prettier-atom)

Find more plugins [here](https://github.com/prettier/prettier#editor-integration)

### To start
run `gulp serve`

In the first time you login, the credentials would be as follows.

username - rand
password - pass

### Make sure you have aria2 installed.
run `aria2c --enable-rpc`

### Run UI unit tests
```
	$ cd ui/
	$ npm test OR $ yarn test 
```
