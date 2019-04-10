/* global document */
(function(){
  'use strict';
  angular
    .module('app')
    .controller('LoginCtrl', ['$scope', '$state', 'UserService', LoginCtrl]);

  function LoginCtrl($scope, $state, UserService) {
    $scope.user = {};
    sessionStorage.setItem('isDarkThemeOn',false);
    $scope.data = {
      cb1: sessionStorage.getItem('isDarkThemeOn')
    }
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

    $scope.onChange = function toggleTheme(cbState) {
      const login_class = document.getElementsByClassName('login-class')[0];
      login_class.id = 'temp_id';
      if (cbState === true) {
        document.getElementById('temp_id').style.backgroundColor = '#404040';
        sessionStorage.setItem('isDarkThemeOn', true);
      } else {
        document.getElementById('temp_id').style.backgroundColor = '#fff';
        sessionStorage.setItem('isDarkThemeOn', false);
      }
    };

    UserService.cleanUpStorage();
  }

})();
