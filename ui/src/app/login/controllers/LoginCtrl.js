(function(){

  angular
    .module('app')
    .controller('LoginCtrl', [
      '$scope', '$state', 'Security',
      LoginCtrl
    ]);

  function LoginCtrl($scope, $state, Security) {
    console.log("In control");
    $scope.user = {};
    $scope.incorrectCredentials = false;

    Security.removeToken();

    $scope.login = function(){
      Security.login($scope.user, function(status) {
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
