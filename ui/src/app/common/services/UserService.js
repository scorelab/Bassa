(function(){
  'use strict';

  angular.module('app')
    .service('UserService', ['$injector', 'BassaUrl', 'AclService', UserService]);

  function UserService($injector, BassaUrl, AclService){

    var data = {
      name: '',
      authLevel: ''
    };

    var login = function(credentials, cb) {
      var $http = $injector.get('$http');

      return $http({
          method: 'POST',
          url: BassaUrl + '/api/login',
          transformRequest: function(obj) {
            var str = [];
            for(var p in obj)
            str.push(encodeURIComponent(p) + '=' + encodeURIComponent(obj[p]));
            return str.join('&');
          },
          data: credentials,
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (response) {
        if(response.status === 200) {
          setToken(response.headers()['token']);
          setName(credentials.user_name);
          setAuthLevel(response.data.auth);
          setUserId(response.data.id);
          AclService.clearContext();
          cb({
            state: response.status
          });
        }
        else {
          cb({
            state: response.status
          });
        }
      }, function(error){
        cb({
          state: 403
        });
      });
    };

    var signup = function(obj) {
      var $http = $injector.get('$http');
      return $http({
        method: 'POST',
        url: BassaUrl + '/api/regularuser',
        data: JSON.stringify(obj),
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      });
    };

    var setName = function(name) {
      localStorage.setItem('UserName', name);
    };

    var getName = function() {
      return localStorage.getItem('UserName');

    };

    var getAuthLevel = function() {
      return data.authLevel;
    };

    var setUserId = function(id) {
      localStorage.setItem('UserId', id);
    };

    var setAuthLevel = function(auth) {
      data.authLevel = auth;
    };

    var setToken = function(newToken) {
      localStorage.setItem('Token', newToken);
    };

    var cleanUpStorage = function() {
      localStorage.setItem('UserId', '');
      localStorage.setItem('Token', '');
      localStorage.setItem('UserName', '');
    }

    var getUserId = function(){
      return localStorage.getItem('UserId');
    };

    var getToken = function(){
      return localStorage.getItem('Token');
    };

    var loggedIn = function() {
      return getToken() !== '';
    };

    return {
      loggedIn: loggedIn,
      login:login,
      signup:signup,
      token:getToken,
      cleanUpStorage:cleanUpStorage,
      getUsername:getName,
      getAuthLevel:getAuthLevel,
      getUserId: getUserId,
      setToken:setToken,
      setUsername:setName,
      setAuthLevel:setAuthLevel
    };

  }
})();
