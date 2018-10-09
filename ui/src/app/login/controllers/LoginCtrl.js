(function(){
  'use strict';
  angular
    .module('app')
    .controller('LoginCtrl', ['$scope', '$state', '$mdDialog', 'UserService', LoginCtrl]);

  function LoginCtrl($scope, $state, $mdDialog, UserService) {
    $scope.user = {};
    $scope.login = function(){
      $scope.incorrectCredentials = false;
      $scope.unApproved = false;
      UserService.login($scope.user, function(status) {
        if (status.state === 200) {
          $state.go('home.dashboard');
        } else if(status.state === 401) {
            $mdDialog.show(
              $mdDialog.alert()
                .clickOutsideToClose(true)
                .title('Server has gone away')
                .textContent('There is something wrong with the server, please check the errors in log files')
                .ariaLabel('Server Disconnect Alert')
                .ok('Got it!')
            );
          $scope.unApproved = true;
        } else if(status.state === 403) {
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
          $scope.incorrectCredentials = true;
        }
       });
    };

    $scope.signup = function() {
      $state.go('signup');
    };

    UserService.cleanUpStorage();
  }

})();
