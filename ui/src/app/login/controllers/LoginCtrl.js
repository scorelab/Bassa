(function(){

  angular
    .module('app')
    .controller('LoginCtrl', ['$scope', '$state', 'UserService', LoginCtrl]);

  function LoginCtrl($scope, $state, UserService) {
    $scope.user = {};
    $scope.incorrectCredentials = false;

    $scope.login = function(){
      UserService.login($scope.user, function(status) {
        if (status){
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
