/* global document, sessionStorage */
(function(){
  'use strict';
  angular
    .module('app')
    .controller('LoginCtrl', ['$scope', '$state', 'UserService', LoginCtrl]);

  function LoginCtrl($scope, $state, UserService) {
    $scope.user = {};
    sessionStorage.setItem('isDarkThemeOn', false);
    $scope.data = {
      cb1: sessionStorage.getItem('isDarkThemeOn'),
    };
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
      const loginClass = document.getElementsByClassName('login-class')[0];
      loginClass.id = 'temp_id';
      const inputClass = document.querySelectorAll('.login-input');
      if (cbState === true) {
        document.getElementById('temp_id').style.backgroundColor = '#404040';
        document.getElementById('temp_id').style.color = '#fff';
        for (let i =  0; i < inputClass.length; i++) {
          inputClass[i].style.color = '#fff';
        }
        sessionStorage.setItem('isDarkThemeOn', true);
      } else {
        document.getElementById('temp_id').style.backgroundColor = '#fff';
        document.getElementById('temp_id').style.color = '#9e9e9e';
        for (let i =  0; i < inputClass.length; i++) {
          inputClass[i].style.color = '#000';
        }
        sessionStorage.setItem('isDarkThemeOn', false);
      }
    };

    UserService.cleanUpStorage();
  }

})();
