angular.module('app')

.factory('authorizationInterceptor', ['UserService', function (UserService) {
  return {
    request: function (config) {
      var token=UserService.token();
      config.headers = config.headers || {};
      if (token) {
        config.headers.token = token;
      }
      return config;
    },

    response: function (config) {
      var newToken = config.headers()['token'];
      if (newToken) {
        UserService.setToken(newToken);
      }
      return config;
    }
  };
}]);
