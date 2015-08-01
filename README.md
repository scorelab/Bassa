# Bassa
Automated Download Queue for Enterprise to take the best use of Internet bandwidth

##URL endpoints
  
**http://localhost:5000/api/login**  
  
Form data: user_name, password  
Returns auth token in response header for successful login

**http://localhost:5000/api/user**  
######POST 
Headers: Content-type : Application/JSON, token: <auth token>  
JSON: ```{'username':'<username>', 'password':'<password>', 'auth':'<authleval>', 'email':'<email>'}  ```   
  
*Auth levals*  
* 0:ADMIN
* 1:STUDENT
* 2:ACADEMIC
* 3NONACADEMIC
  
######GET
Headers: token: <auth token>  
Returns JSON of all the users  
######DELETE
```http://localhost:5000/api/user/<username>  ```  
Deletes the user from system. Adviced not to use.
######PUT
```http://localhost:5000/api/user/<username>  ```  
Headers: Content-type : Application/JSON, token: <auth token>  
JSON: ```{'username':'<username>', 'password':'<password>', 'auth':'<authleval>', 'email':'<email>'}  ```   
Update the given user  

**http://localhost:5000/api/user/blocked**  
######GET
Headers: token: <auth token>  
Returns JSON of all the blocked users  
######POST 
```http://localhost:5000/api/user/blocked/<username>  ```  
Headers: token: <auth token>  
Block the given user
