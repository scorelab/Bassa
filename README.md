![logo](http://gdurl.com/7XYK)

[![Build Status](https://travis-ci.org/scorelab/Bassa.svg?branch=master)](https://travis-ci.org/scorelab/Bassa)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7de63c7b9a69448787e8014a12a260b1)](https://www.codacy.com/app/SCoRe-Lab/Bassa?utm_source=github.com&utm_medium=referral&utm_content=scorelab/Bassa&utm_campaign=badger)
[![Docker Build](https://img.shields.io/docker/automated/scoreucsc/bassa.svg)]()
[![PyPI](https://img.shields.io/pypi/v/Bassa.svg)](https://pypi.python.org/pypi/bassa)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/scorelab/scorelab)
[![](https://images.microbadger.com/badges/image/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/commit/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own commit badge on microbadger.com")

Automated Download Queue for Enterprise to take the best use of Internet bandwidth

# About
Bassa solves the problem of wasting internet bandwidth by queuing a download if it is larger than a given threshold value in high traffic and when the traffic is low, it completes the download of the files. After the files are downloaded, the users can get their files from the local servers which do not require external internet bandwidth.

## Main functionalities
* Provides an interface for users to add their downloads as links or torrent magnet links
* Provide users with an interface to view and download the files in the local server
* Provide a rating system for users to rate the files residing in local server
* Automatically start and stop downloading in given time frame
* Automatically clean the disks and make room for new downloads
* Notify the users when his/her download is completed
* Mark inappropriate downloads
* Provides admins with an interface to deal with inappropriate files

## Installation

Note: 
* Windows users can check the installation guide [here](https://github.com/scorelab/Bassa/wiki/Windows-Installation-Guide).
* MacOS users can check the installation guide [here](https://github.com/scorelab/Bassa/wiki/MacOS-Installation-Guide).


First clone the Repository
``` git clone https://github.com/scorelab/Bassa.git```
``` cd Bassa```

![gitclone](https://user-images.githubusercontent.com/28682735/35194406-2f6f08e2-fed9-11e7-8411-86d83bed6507.gif)

Use python 3 instead of Python 2

```
  $ ./setup.sh

  $ cd components/core/
  $ sudo python3 setup.py develop
```
![setupsh](https://user-images.githubusercontent.com/28682735/35194409-2ffbca66-fed9-11e7-9242-ffe036067d18.gif)

Bassa has 4 main compoenents, 
1. Database
2. Bassa API
3. Bassa UI
4. aria2


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


## Bassa API
```
  $ cd components/core/
  $ python3 Main.py
```
![python3main](https://user-images.githubusercontent.com/28682735/35194408-2fce9136-fed9-11e7-80e6-fac5e6f54bc7.gif)


## Bassa UI

### Install dependencies with


```
$ cd ui/
$ npm install
```

### To start
run `gulp serve`


![gulp_serve](https://user-images.githubusercontent.com/28682735/35194407-2fa172e6-fed9-11e7-9e89-065ecb3cbf87.gif)


In the first time you log in, the credentials would be as follows.

- username - rand
- password - pass


![bassaui](https://user-images.githubusercontent.com/28682735/35193753-667c7e0c-fecd-11e7-918f-13ce1d00d055.gif)


## Make sure you have aria2 installed.
run `aria2c --enable-rpc`

Read more on installing `aria2` [here](https://aria2.github.io/manual/en/html/README.html)


![aria2c](https://user-images.githubusercontent.com/28682735/35193755-709e92ee-fecd-11e7-8dd0-412304853c8c.gif)


## Using Docker-Compose

Run the `docker-compose` at the project directory to deploy the core API, UI and the DB.

`$ docker-compose up`

### How to Use Bassa
* After Setting up Bassa, Login/Register.
  There are two types of users in Bassa
  1. The Admin
  2. The Normal Users
* A user can add a link through the webapp and Bassa stores it in the local server right away. This way multiple users can add various links, but the downloads won’t start right away. 
* The organisation admin can start the downloads at a time of his/her liking. 
* Then the users who had added links for certain files can download them from the local servers at a much higher speed.
* You can even watch a video tutorial for the same on [Youtube](https://www.youtube.com/watch?v=NxS8T1EphCA)


# Developers

Please go through the developer guides in [Bassa wiki](https://github.com/scorelab/Bassa/wiki)
