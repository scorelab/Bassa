angular.module('bassa')

.factory('authorizationInterceptor', ['Security', function (Security) {
  return {
    request: function (config) {
      var token=Security.token();
      config.headers = config.headers || {};
      if (token) {
        config.headers.Authorization = 'Bearer ' + token;
      }
      return config;
    }
  };
}]);
