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

    $scope.onChange = function(cbState) {
      //console.log(cbState)
      let x = document.getElementsByClassName("parent-container")[0];
      x.id = "temp_id";
      if(cbState === true) {
        //console.log('true value')
        document.getElementById("temp_id").style.backgroundColor="#19223c";
      } else {
        //console.log('false value')
        document.getElementById("temp_id").style.backgroundColor="#fff";
      }
    }

    UserService.cleanUpStorage();
  }

})();
