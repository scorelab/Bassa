(function(){

  angular
    .module('app')
    .controller('DashCtrl', [ '$scope', '$http', 'ToastService',
      DashCtrl
    ]);

  function DashCtrl($scope, $http, ToastService) {
    $scope.dlink = {link: ''}
    console.log(ToastService);

    $scope.addLink = function() {

      return $http({
          method: 'POST',
          url: 'http://localhost:5000/api/download',
          data: JSON.stringify($scope.dlink),
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (response) {
        console.log("Success");
        $scope.dlink.link = '';
        ToastService.showToast("Link added");
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
        $scope.dlink.link = '';
        console.log("Oops!", error);
      });
    };
  }

})();
