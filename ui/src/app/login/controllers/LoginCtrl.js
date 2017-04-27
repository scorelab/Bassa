(function(){
  'use strict';
  angular
    .module('app')
    .controller('LoginCtrl', ['$scope', '$state', 'UserService', LoginCtrl]);

  function LoginCtrl($scope, $state, UserService) {
    $scope.user = {};
    //$rootScope.usernme = $scope.user.user_name;;
    console.log("hello" + $scope.user.user_name);


    $scope.login = function(){
      $scope.incorrectCredentials = false;
      UserService.login($scope.user, function(status) {
        if (status){
          console.log("user: " + JSON.stringify($scope.user));
          localStorage.setItem("user", JSON.stringify($scope.user));
          $state.go('home.dashboard');
        } else {
          $scope.incorrectCredentials = true;
        }
      });
    };

    $scope.signup = function() {
      $state.go('signup');
    };

    UserService.removeToken();
  }

})();
