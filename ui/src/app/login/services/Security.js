(function(){
  'use strict';

  angular.module('app')
        .service('Security', [
        '$injector',
      Security
  ]);

  function Security($injector){

    function login(credentials, cb) {
      var $http = $injector.get('$http');

      return $http({
          method: 'POST',
          url: 'http://localhost:5000/api/login',
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
        cb(true);
      }, function(error){
        console.log("Oops");
        cb(false);
      });
    };

    function setToken(newToken) {
      localStorage.setItem("Token", newToken);
    };

    function removeToken() {
      localStorage.setItem("Token", '');
    }

    function getToken(){
      return localStorage.getItem("Token");
    };

    function loggedIn() {
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
