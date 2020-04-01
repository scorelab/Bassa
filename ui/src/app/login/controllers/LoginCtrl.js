(function(){
  'use strict';
  angular
    .module('app')
    .controller('LoginCtrl', ['$scope', '$state', 'UserService', LoginCtrl]);

  function LoginCtrl($scope, $state, UserService) {
    $scope.user = {};
    $scope.inputType = 'password';
    $scope.login = function(){
      $scope.incorrectCredentials = false;
      $scope.unApproved = false;
      UserService.login($scope.user, function(status) {
        if (status.state == 200) {
          $state.go('home.dashboard');
        } else if(status.state == 401) {
          $scope.unApproved = true;
        } else if(status.state == 403) {
          $scope.incorrectCredentials = true;
        }
      });
    };

    $scope.hideShowPassword = () => {
      if ($scope.inputType === 'password') {
        $scope.inputType = 'text';
      } else {
        $scope.inputType = 'password';
      }
    };

    $scope.signup = function() {
      $state.go('signup');
    };

    UserService.cleanUpStorage();
  }

})();
