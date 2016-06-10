angular.module('bassa')

.factory('Security', ['$injector', function ($injector) {

  var token;

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
    }).success(function (data, status, headers, config) {
      token = headers()['token'];
      cb();
    });
  };

  function getToken(){
    return token;
  };

  function loggedIn() {
    return token !== undefined;
  };

  return {
    loggedIn: loggedIn,
    login:login,
    token:getToken
  };
}]);
