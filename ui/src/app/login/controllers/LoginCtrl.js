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

    $scope.toggle = function () {
      let x = document.getElementsByClassName("login-container")[0];
      x.id = "temp_id";
      let y = document.getElementById("temp_id").style.backgroundColor;
      if(document.getElementById("temp_id").style.backgroundColor === "rgb(25, 34, 60)")
      {
        document.getElementById("temp_id").style.backgroundColor="#fff";
      }
      else
      {
        document.getElementById("temp_id").style.backgroundColor="#19223c";
      }
    }

    UserService.cleanUpStorage();
  }

})();
