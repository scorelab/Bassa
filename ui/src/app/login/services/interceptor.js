angular.module('app')

.factory('authorizationInterceptor', ['Security', function (Security) {
  return {
    request: function (config) {
      var token=Security.token();
      config.headers = config.headers || {};
      if (token) {
        config.headers.token = token;
      }
      return config;
    },

    response: function (config) {
      var newToken = config.headers()['token'];
      if (newToken) {
        Security.setToken(newToken);
      }
      return config;
    }
  };
}]);
