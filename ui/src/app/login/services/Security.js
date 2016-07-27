(function(){
  'use strict';

  angular.module('app')
        .service('Security', [
        '$injector', 'BassaUrl',
      Security
  ]);

  function Security($injector, BassaUrl){

    var login = function(credentials, cb) {
      var $http = $injector.get('$http');

      return $http({
          method: 'POST',
          url: BassaUrl + '/api/login',
          transformRequest: function(obj) {
            var str = [];
            for(var p in obj)
            str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
            return str.join("&");
          },
          data: credentials,
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (response) {
        setToken(response.headers()['token']);
        setUsername(credentials.user_name);
        cb(true);
      }, function(error){
        console.log("Oops");
        cb(false);
      });
    };

    var setUsername = function(name) {
      localStorage.setItem("Username", name);
    };

    var setToken = function(newToken) {
      localStorage.setItem("Token", newToken);
    };

    var removeToken = function() {
      localStorage.setItem("Token", '');
    }

    var getToken = function(){
      return localStorage.getItem("Token");
    };

    var loggedIn = function() {
      return getToken() !== '';
    };

    return {
      loggedIn: loggedIn,
      login:login,
      token:getToken,
      removeToken:removeToken,
      setToken:setToken
    };

  }
})();
