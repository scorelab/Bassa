/* global document */
(function(){
  'use strict';
  angular
    .module('app')
    .controller('LoginCtrl', ['$scope', '$state', 'UserService', LoginCtrl]);

  function LoginCtrl($scope, $state, UserService) {
    $scope.user = {};
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

    $scope.signup = function() {
      $state.go('signup');
    };

    $scope.toggle = function toggleTheme() {
      const x = document.getElementsByClassName('login-container')[0]; /* trying to get login page parent node */
      x.id = 'temp_id';
      if (document.getElementById('temp_id').style.backgroundColor === 'rgb(25, 34, 60)') { /* checking if present mode is dark */
        document.getElementById('temp_id').style.backgroundColor = '#fff'; /* If it is true, then change it to light theme */
      } else { document.getElementById('temp_id').style.backgroundColor = '#19223c'; }
    };

    UserService.cleanUpStorage();
  }

})();
