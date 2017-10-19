(function(){
  'use strict';

  angular.module('app')
    .service('UserService', ['$injector', 'BassaUrl', UserService]);

  function UserService($injector, BassaUrl){

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
        setToken(response.headers()['token']);
        setName(credentials.user_name);
        setAuthLevel(response.data.auth);
        cb(true);
      }, function(error){
        cb(false);
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

    var setAuthLevel = function(auth) {
      data.authLevel = auth;
    };

    var setToken = function(newToken) {
      localStorage.setItem('Token', newToken);
    };

    var removeToken = function() {
      localStorage.setItem('Token', '');
    }

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
      removeToken:removeToken,
      getUsername:getName,
      getAuthLevel:getAuthLevel,
      setToken:setToken,
      setUsername:setName,
      setAuthLevel:setAuthLevel
    };

  }
})();
