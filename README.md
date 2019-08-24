<hr>

![logo](http://gdurl.com/7XYK)

[![Build Status](https://travis-ci.org/scorelab/Bassa.svg?branch=master)](https://travis-ci.org/scorelab/Bassa)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7de63c7b9a69448787e8014a12a260b1)](https://www.codacy.com/app/SCoRe-Lab/Bassa?utm_source=github.com&utm_medium=referral&utm_content=scorelab/Bassa&utm_campaign=badger)
[![Docker Build](https://img.shields.io/docker/automated/scoreucsc/bassa.svg)]()
[![PyPI](https://img.shields.io/pypi/v/Bassa.svg)](https://pypi.python.org/pypi/bassa)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/scorelab/scorelab)
[![](https://images.microbadger.com/badges/image/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/commit/scoreucsc/bassa.svg)](https://microbadger.com/images/scoreucsc/bassa "Get your own commit badge on microbadger.com")
[![Backers on Open Collective](https://opencollective.com/Bassa/backers/badge.svg)](#backers) 
[![Sponsors on Open Collective](https://opencollective.com/Bassa/sponsors/badge.svg)](#sponsors) 

Automated Download Queue for Enterprise to take the best use of Internet bandwidth

<hr>

# About
Bassa solves the problem of wasting internet bandwidth by queuing a download if it is larger than a given threshold value in high traffic and when the traffic is low, it completes the download of the files. After the files are downloaded, the users can get their files from the local servers which do not require external internet bandwidth.

### Main functionalities
* Provides an interface for users to add their downloads as links or torrent magnet links
* Provide users with an interface to view and download the files in the local server
* Provide a rating system for users to rate the files residing in local server
* Automatically start and stop downloading in given time frame
* Automatically clean the disks and make room for new downloads
* Notify the users when his/her download is completed
* Mark inappropriate downloads
* Provides admins with an interface to deal with inappropriate files

### Architecture

Bassa is a multi-tier application which can serve users through dedicated Web, Android and iOS clients. 

<br>

![Bassa Architecture](https://b.imge.to/2019/07/28/kNdAC.png)

<br>

**Components**
* Bassa API server is implemented as a [flask-socketio](https://flask-socketio.readthedocs.io/en/latest/) server written in Python.
* Bassa web client is implemented using Angular written in JavaScript. (*Moving to create-react-app very soon*)
* Bassa [Android and iOS mobile clients](https://github.com/scorelab/Bassa-mobile) are implemented using react native written in JavaScript.
* Bassa uses MySQL 5.X as database server.
* Bassa uses [Aria2c RPC server](https://aria2.github.io/) to download files.
* Bassa can be used with [Minio](https://github.com/minio/minio) file storage server as a file system and also for storing files to Amazon S3 cloud storage.
<hr>

# Getting Started
## Installation Guide

### Setting up Bassa using Docker and docker-compose [Recommended]
In order to setup Bassa using docker, install the latest version of [docker](https://docs.docker.com/install/) with [docker-compose tool](https://docs.docker.com/compose/install/) on your machine.
Clone the [Bassa GitHub repository](https://github.com/scorelab/Bassa).
Run the below command to move into the root folder. 
```
cd Bassa
```
We will be using docker-compose tool to build images and finally spin up all our containers and then we can start using Bassa. *docker-compose configuration file* has configuration for each container and you are free to modify it. You can run the below command. <br>

For development:
```bash
docker-compose -f docker-compose.dev.yml up --build
```
You can access the Bassa Web Client at port **3000** served by Gulp. <br>
For production:
```bash
docker-compose up --build
```
You can access the Bassa Web Client at port **80** served by Nginx. <br>
You can run a specific container using docker-compose tool. You can do that using the service names. 

| Service   |      Service Name      |
|----------|:-------------:|
| API server |  api |
| Web client |  web   |
| Database server | db |
| Aria2c | aria2c |
| Minio server | minio |

**Usage**
```bash
docker-compose build [SERVICE NAME]
docker-compose run [SERVICE NAME]
```

### Setting up Bassa from the source code
In order to to setup Bassa from the source code, you need a machine with either Linux, MacOS or Windows operating system.
Keep an eye on the configuration files such as dl.conf as they are specific to docker environment.

### Setting up Bassa on Linux based operating systems

First clone and move to the project repository 

```
git clone https://github.com/scorelab/Bassa.git && cd Bassa
```

Install Bassa dependencies.
```
sudo ./setup.sh
```

#### Setting up Aria2c RPC server

Open a new terminal window, move to downloads folder and start Aria2c server.
```
cd downloads/
aria2c --enable-rpc --rpc-listen-all
```

#### Setting up Bassa Database

Start the MySQL service on your machine and open the MySQL terminal to type the command for creating the Bassa Database.
```
create database Bassa;
```
Exit from MySQL terminal and insert the Bassa database schema in to the created database.
```
cd db_schema/
mysql -u root -p  Bassa < Bassa.sql
```
Configure the Bassa database credentials in *components/core/DBCon.py* database connector file.

If the environment variables are being used, modify as following :
```python
_db=MySQLdb.connect("db", os.environ.get('YOUR_DB_USERNAME'), os.environ.get('YOUR_DB_PASSWORD'), os.environ.get('Bassa')) 
```

If the environment variables are not configured and hardcoded strings are being used, replace as :
```python
_db=MySQLdb.connect(host="localhost", user="YOUR_DB_USERNAME", passwd="YOUR_DB_PASSWORD",db= "Bassa")
```
#### Setting up Bassa API server

Change directory to API code base and install python modules
```
cd components/core/ 
sudo python3 setup.py develop
```
Start Bassa API server 
```
sudo python3 Main.py
```
#### Setting up Minio server

Execute the following command to start Minio server
 
```
export MINIO_ACCESS_KEY=bassa
export MINIO_SECRET_KEY=bassa123
./minio server /data
```
#### Setting up Bassa Web client and Gulp

Open a new terminal window, move to UI code base and install node modules.
```bash
cd ui/
sudo npm install
sudo npm install --global bower gulp-cli
```
Start the Bassa Web Client
```bash 
gulp serve
```
You can access the Bassa Web Client at port **3000**.


### Setting up Bassa on MacOS

First clone and move to the project repository 

```
git clone https://github.com/scorelab/Bassa.git && cd Bassa
```

Install Bassa dependencies.
```
sudo ./setup.sh
```

#### Setting up Aria2c RPC server

Open a new terminal window, move to downloads folder and start Aria2c server.
```
cd downloads/
aria2c --enable-rpc --rpc-listen-all
```

#### Setting up Bassa Database

Start the MySQL service on your machine and open the MySQL terminal to type the command for creating the Bassa Database.
```
create database Bassa;
```
Exit from MySQL terminal and insert the Bassa database schema in to the created database.
```
cd db_schema/
mysql -u root -p  Bassa < Bassa.sql
```
Configure the Bassa database credentials in *components/core/DBCon.py* database connector file.

If the environment variables are being used, modify as following :
```python
_db=MySQLdb.connect("db", os.environ.get('YOUR_DB_USERNAME'), os.environ.get('YOUR_DB_PASSWORD'), os.environ.get('Bassa')) 
```

If the environment variables are not configured and hardcoded strings are being used, replace as :
```python
_db=MySQLdb.connect(host="localhost", user="YOUR_DB_USERNAME", passwd="YOUR_DB_PASSWORD",db= "Bassa")
```
#### Setting up Bassa API server

Change directory to API code base and install python modules
```
cd components/core/ 
sudo python3 setup.py develop
```
Start Bassa API server 
```
sudo python3 Main.py
```
#### Setting up Minio server

Execute the following command to start Minio server
 
```
export MINIO_ACCESS_KEY=bassa
export MINIO_SECRET_KEY=bassa123
minio server /data
```
#### Setting up Bassa Web client and Gulp

Open a new terminal window, move to UI code base and install node modules.
```bash
cd ui/
sudo npm install
sudo npm install --global bower gulp-cli
```
Start the Bassa Web Client
```bash 
gulp serve
```
You can access the Bassa Web Client at port **3000**.

### Setting up Bassa on Windows operating system

First clone and move to the project repository 

```
git clone https://github.com/scorelab/Bassa.git && cd Bassa
```

Install latest [python3](https://www.python.org/downloads/release/python-363/) on your machine. \
Install latest version of [Aria2](https://aria2.github.io/) and add the executable to the [PATH variable]( https://msdn.microsoft.com/en-us/library/office/ee537574(v=office.14).aspx). \
Install the [MySQl Server](https://dev.mysql.com/downloads/installer/) and make sure to check MySQL component and C connectors during installation. \
Install [Node](https://nodejs.org/en/) on your windows machine.\

#### Setting up Aria2c RPC server

Open a new CMD window, move to downloads folder and start Aria2c server.
```
cd downloads/
aria2c --enable-rpc --rpc-listen-all
```

#### Setting up Bassa Database

Open the MySQL command line client to type the command for creating the Bassa Database.
```
create database Bassa;
```
Exit from MySQL client and insert the Bassa database schema in to the created database.
```
cd db_schema/
mysql -u root -p  Bassa < Bassa.sql
```
Configure the Bassa database credentials in *components/core/DBCon.py* database connector file.

If the environment variables are being used, modify as following :
```python
_db=MySQLdb.connect("db", os.environ.get('YOUR_DB_USERNAME'), os.environ.get('YOUR_DB_PASSWORD'), os.environ.get('Bassa')) 
```

If the environment variables are not configured and hardcoded strings are being used, replace as :
```python
_db=MySQLdb.connect(host="localhost", user="YOUR_DB_USERNAME", passwd="YOUR_DB_PASSWORD",db= "Bassa")
```
#### Setting up Bassa API server

Change directory to API code base and install python modules
```
cd components/core/ 
sudo python setup.py develop
```
Start Bassa API server 
```
sudo python Main.py
```
#### Setting up Minio server

Download and run Minio.exe using following link
```
https://dl.min.io/server/minio/release/windows-amd64/minio.exe
```

Change the directory to folder where Minio.exe is downloaded and Execute the following command to start Minio server
 
```
set MINIO_ACCESS_KEY=bassa
set MINIO_SECRET_KEY=bassa123
minio.exe server /data

```
#### Setting up Bassa Web client and Gulp

Open a new terminal window, move to UI code base and install node modules.
```bash
cd ui/
sudo npm install
sudo npm install --global bower gulp-cli
```
Start the Bassa Web Client
```bash 
gulp serve
```
You can access the Bassa Web Client at port **3000**.

## Usage 
Please use the mock-up username and password to try and develop Bassa.

| Key   |      Value     |
|----------|:-------------:|
| user_name |  rand |
| password |  pass   |

You can even refer to a Video tutorial on how to use Bassa, available on [Youtube](https://youtu.be/NxS8T1EphCA) <br><br>
Once developed, Bassa will save internet bandwidth by downloading files when the traffic is low. In the current build, you can log in either as a user or as an admin and add links for files to download. The admin can start the downloads as and when he/she likes or when he/she feels that the traffic on the network is low. After the download, the users can get their files from local servers which does not need internet bandwidth.

#### If you’re a user
- If you’re a new user, you need to sign up first and can only login after the admin has approved your account.

#### If you’re an admin
- Only an admin account can access the “Admin” tab in Bassa
- In the admin tab, you have four available processes- <br>
     **a) Start/Kill downloads-** You can start the downloads queued at the time of your liking <br>
     **b) Sign up Requests-** As an admin, you need to approve the accounts of all the new users before they can start using Bassa <br>
     **c) Usage of top heaviest users-** You get access to a graph that shows the usage percentage of the heaviest users <br>
     **d) Visit minio-** As an admin, you can visit minio and monitor the downloaded files

#### Common Functionalities
- Once logged in, navigate to the dashboard section. You can add a link to a file or a magnet link in the text field labeled “Add download*”. You can then see the link added under the “Ongoing downloads tab” <br>
- After the admin has approved the download, your file begins to download. It gets saved on the local servers from which you can get your files without the use of external bandwidth <br>
- In the “Completed” section, you can view all the details of downloads that Bassa has completed till now

Bassa is an essential tool for managing downloads and to make the best use of Internet Bandwidth. It is also compatible with Amazon cloud storage.

## Running Tests

### API Tests
* Make sure the python server is working and you have an open connection to the database.
* Open the python console in your terminal by running the command `python3`.
* In the console that opens, import the test files, like so:

```
 from tests.Bassa_endpoint_test import *
 from tests.login_test import *
```

### UI Tests

```
cd ui
npm test OR yarn test
```

## Troubleshooting
Incase if you are stuck up with any issues during the setup or usage, look in to the [troubleshooting](https://github.com/scorelab/Bassa/issues/375) list for help or file a new issue on the project repository.

<hr>

# Communication
Feel free to discuss on our [Bassa gitter channel](https://gitter.im/scorelab/Bassa).
You can also discuss about other projects on [SCoRe Lab gitter channel](https://gitter.im/scorelab/scorelab).

# Developers

Please go through the developer guides in [Bassa wiki](https://github.com/scorelab/Bassa/wiki)


# Contributors

This project exists thanks to all the people who contribute. 
<a href="https://opencollective.com/Bassa#contributors" target="_blank"><img src="https://opencollective.com/Bassa/contributors.svg?width=890&button=false" /></a>


# Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/Bassa#backer)]

<a href="https://opencollective.com/Bassa#backers" target="_blank"><img src="https://opencollective.com/Bassa/backers.svg?width=890"></a>


# Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/Bassa#sponsor)]

<a href="https://opencollective.com/Bassa/sponsor/0/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/1/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/2/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/3/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/4/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/5/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/6/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/7/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/8/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/Bassa/sponsor/9/website" target="_blank"><img src="https://opencollective.com/Bassa/sponsor/9/avatar.svg"></a>


