angular.module('app')

.factory('authorizationInterceptor', ['userService', function (userService) {
  return {
    request: function (config) {
      var token=userService.token();
      config.headers = config.headers || {};
      if (token) {
        config.headers.token = token;
      }
      return config;
    },

    response: function (config) {
      var newToken = config.headers()['token'];
      if (newToken) {
        userService.setToken(newToken);
      }
      return config;
    }
  };
}]);
