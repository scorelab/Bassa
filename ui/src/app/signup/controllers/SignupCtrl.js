(function(){
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

    $scope.incorrectCredentials = false;
    $scope.errorMsg = '';

    var validate = function(obj) {
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

    $scope.back = function() {
     $state.go('login');
   };

    $scope.signup = function() {
      if(validate($scope.user)) {
        UserService.signup($scope.user).then(function(response) {
          if (response.status === 200) {
            ToastService.showToast('Success');
          } else if (response.status === 400) {
            ToastService.showToast('Username already exists');
          } else {
            ToastService.showToast('Something went wrong :(');
          }
          $state.go('login');
        });
      } else {
        ToastService.showToast('Please ensure entered details are correct');
      }
    };


    function passwordValid() {
      $scope.loginForm.password.$valid = true;
      $scope.loginForm.password.$dirty = false;
      $scope.loginForm.password.$invalid = false;
    }
    function passwordInValid() {
      $scope.loginForm.password.$valid = false;
      $scope.loginForm.password.$invalid = true;
      $scope.loginForm.password.$dirty = true;
    }

    $scope.validatePwd = function () {
      const lowerCaseLetters = /[a-z]/g;
      const upperCaseLetters = /[A-Z]/g;
      const numbers = /[0-9]/g;
      if (typeof $scope.user.password !== 'undefined') {
        if ($scope.user.password.length < 8) {
          passwordInValid();
          $scope.errorMsg = 'Password must contains Minimum <b>8 characters</b>';
        } else if (!$scope.user.password.match(upperCaseLetters)) {
          passwordInValid();
          $scope.errorMsg = 'Password must contains a <b>uppercase</b> letter';
        } else if (!$scope.user.password.match(lowerCaseLetters)) {
          passwordInValid();
          $scope.errorMsg = 'Password must contains a <b>lowercase</b> letter';
        } else if (!$scope.user.password.match(numbers)) {
          passwordInValid();
          $scope.errorMsg = 'Password must contains a <b>number</b>';
        } else {
          passwordValid();
          $scope.errorMsg = '';
        }
      }
    };
  }

})();
