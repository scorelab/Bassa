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
  }

})();
