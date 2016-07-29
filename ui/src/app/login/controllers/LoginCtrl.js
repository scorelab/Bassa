(function(){

  angular
    .module('app')
    .controller('LoginCtrl', [
      '$scope', '$state', 'UserService',
      LoginCtrl
    ]);

  function LoginCtrl($scope, $state, UserService) {
    console.log("In control");
    $scope.user = {};
    $scope.incorrectCredentials = false;

    UserService.removeToken();

    $scope.login = function(){
      UserService.login($scope.user, function(status) {
        if (status){
          $state.go('home.dashboard');
        } else {
          console.log("Incorrect auth");
          $scope.incorrectCredentials = true;
        }
      });
    };
  }

})();
