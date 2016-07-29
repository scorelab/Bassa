(function(){

  angular
    .module('app')
    .controller('LoginCtrl', [
      '$scope', '$state', 'userService',
      LoginCtrl
    ]);

  function LoginCtrl($scope, $state, userService) {
    console.log("In control");
    $scope.user = {};
    $scope.incorrectCredentials = false;

    userService.removeToken();

    $scope.login = function(){
      userService.login($scope.user, function(status) {
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
