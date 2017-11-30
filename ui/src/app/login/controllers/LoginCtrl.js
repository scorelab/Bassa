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
<<<<<<< HEAD
        if (status){
=======
        if (status.state === 200) {
          localStorage.setItem("user", JSON.stringify($scope.user));
>>>>>>> 3a59aff3856a5a392d63bc83705f444b06d0fbad
          $state.go('home.dashboard');
        } else if(status.state === 401) {
          $scope.unApproved = true;
        } else if(status.state === 403) {
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
