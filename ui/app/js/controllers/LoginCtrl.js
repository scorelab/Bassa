angular.module('bassa')

.controller('LoginCtrl', function($scope, $state, Security) {
  $scope.user = {};

  $scope.login = function(){
    Security.login($scope.user, function() {
      $state.go('app');
    });
  };



});
