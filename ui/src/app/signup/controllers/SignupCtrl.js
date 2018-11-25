(function () {
  'use strict';
  angular
    .module('app')
    .controller('SignupCtrl', ['$scope', '$state', 'UserService', 'ToastService', SignupCtrl]);

  function SignupCtrl($scope, $state, UserService, ToastService) {
    $scope.user = {
      user_name: '',
      email: '',
      password: '',
      confirm_password: ''
    };

    $scope.type = 'password';
    $scope.toggleType = function () {
      if ($scope.type == 'text') {
        $scope.type = 'password';
      } else {
        $scope.type = 'text';
      }
    }


    $scope.incorrectCredentials = false;

    var validate = function (obj) {
      for (var key in obj) {
        if (obj[key] === '' || obj[key] === undefined) {
          return false;
        }
        if (obj['confirm_password'] !== obj['password']) {
          return false;
        }
      }
      return true;
    };

    $scope.back = function () {
      $state.go('login');
    };

    $scope.signup = function () {
      if (validate($scope.user)) {
        UserService.signup($scope.user).then(function (response) {
          ToastService.showToast('Success');
          $state.go('login');
        }, function (error) {
          ToastService.showToast('Username already exists');
        });
      } else {
        ToastService.showToast('Please ensure entered details are correct');
      }
    };
  };

})();
