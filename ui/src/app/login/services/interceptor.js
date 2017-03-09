'use strict';
angular.module('app')
.factory('authorizationInterceptor', ['UserService', '$injector', function (UserService, $injector) {
  return {
    request: function (config) {
      var token = UserService.token();
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
    },

    responseError: function(res) {
      if (res.status === 403) {
        $injector.get('$state').transitionTo('login');
        $scope.incorrectCredentials=true;
      }
      return res;
    },
  };
}]);
