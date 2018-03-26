(function(){
  'use strict';
  angular
    .module('app')
    .controller('SignupCtrl', ['$scope', '$state', '$mdDialog','UserService', 'ToastService', SignupCtrl]);

  function SignupCtrl($scope, $state, $mdDialog,UserService, ToastService) {
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
          if(response.status === 403){
    
            var confirm = $mdDialog.confirm()
              .title('Session expires')
              .textContent('This is session expire, please login back to continue')
              .ariaLabel('403 Alert')
              .ok('Take me to Login')
              .cancel('Stay here');
    
            $mdDialog.show(confirm).then(function() {
              location.href = "/#!/login";
            }, function() {
              // nothing to do with Stay here
            });
            return ;
          }else if(response.status !== 200){
            $mdDialog.show(
              $mdDialog.alert()
                .clickOutsideToClose(true)
                .title('Server has gone away')
                .textContent('There is something wrong with the server, please check the errors in log files')
                .ariaLabel('Server Disconnect Alert')
                .ok('Got it!')
            );
            return ;
          }
          ToastService.showToast('Success');
          $state.go('login');
        }, function(error) {
          ToastService.showToast('Username already exists');
        });
      } else {
        ToastService.showToast('Please ensure entered details are correct');
      }
    };
  };

})();
