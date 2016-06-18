(function(){

  angular
    .module('app')
    .controller('DashCtrl', [ '$scope', '$http',
      DashCtrl
    ]);

  function DashCtrl($scope, $http) {
    $scope.dlink = {link: ''}

    $scope.addLink = function() {

      return $http({
          method: 'POST',
          url: 'http://localhost:5000/api/download',
          data: JSON.stringify($scope.dlink),
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (response) {
        console.log("Success");
      }, function(error){
        console.log("Oops!", error);
      });
    };
  }

})();
