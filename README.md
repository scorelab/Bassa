![logo](http://gdurl.com/7XYK)

[![Build Status](https://travis-ci.org/scorelab/Bassa.svg?branch=master)](https://travis-ci.org/scorelab/Bassa)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7de63c7b9a69448787e8014a12a260b1)](https://www.codacy.com/app/SCoRe-Lab/Bassa?utm_source=github.com&utm_medium=referral&utm_content=scorelab/Bassa&utm_campaign=badger)
[![Docker Build Status](https://img.shields.io/docker/build/scoreucsc/bassa.svg)]()
[![PyPI](https://img.shields.io/pypi/dm/Bassa.svg)](https://pypi.python.org/pypi)
[![PyPI](https://img.shields.io/pypi/v/Bassa.svg)](https://pypi.python.org/pypi)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/scorelab/scorelab)
[![](https://images.microbadger.com/badges/image/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/commit/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own commit badge on microbadger.com")

Automated Download Queue for Enterprise to take the best use of Internet bandwidth

# About 
Bassa solves the problem of wasting internet bandwidth by queuing a download if it is larger than a given threshold value in high traffic and when the traffic is low, it completes the download of the files. After the files are downloaded, the users can get their files from the local servers which do not require external internet bandwidth.

## Main functionalities
* Provides an interface for users to add their downloads as links or torrent magnet links
* Provide users  an interface to view and download the files in local server
* Provide a rating system to users to rate the files residing in local server
* Automatically start and stop downloading in given time frame
* Automatically clean the disks and make room for new downloads
* Notify user when his/her download is completed
* Mark inappropriate downloads
* Provides admins an interface to deal with inappropriate files

## Installation

Use python 3 instead of Python 2 </br>
You can check it which Python version are you using by default by typing
```
  $ python --version
```

Install python 3 if not installed and change your by default Python 2 to Python 3 by typing below command in terminal.
```
  $ alias python=python3
```
And then type
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

## Bassa UI

### Install dependencies with


```
$ cd ui/
$ npm install
```

### To start
run `gulp serve`

In the first time you login, the credentials would be as follows.

username - rand
password - pass

### Make sure you have aria2 installed.
run `aria2c --enable-rpc`

### How to Use Bassa
* After Setting up Bassa, Login/Register.There are two types of users in Bassa- (1) The Admin and (2) The Normal Users.
* A user can add a link through the webapp and Bassa stores it in the local server right away. This way multiple users can add various links, but the downloads won’t start right away. 
* The organisation admin can start the downloads at a time of his/her liking. 
* Then the users who had added links for certain files can download them from the local servers at a much higher speed.

### Autoformat JS with Prettier

- [Sublime Text Plugin](https://github.com/jonlabelle/SublimeJsPrettier)
- [Atom Plugin](https://github.com/prettier/prettier-atom)

Find more plugins [here](https://github.com/prettier/prettier#editor-integration)



### Run UI unit tests
```
	$ cd ui/
	$ npm test OR $ yarn test 
```
