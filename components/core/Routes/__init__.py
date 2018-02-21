'''this directory is for download API endpoint and user API endpoint. Download can be imported simply by 
>> import Routes.Download
>> import Routes.User
these files are included with main server using BluePrint in flask, like this

>> from Routes.Download import download_blueprint

In Downlaod.py, blueprint is defined by this line
` download_blueprint = Blueprint('download_blueprint', __name__) `
Same thing is for User.py
'''