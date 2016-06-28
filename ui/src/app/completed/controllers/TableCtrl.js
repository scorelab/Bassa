(function(){

  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'ToastService', 'DashService',
      TableCtrl
    ]);

  function TableCtrl($scope, ToastService, DashService) {
    $scope.dlink = {link: ''};
    $scope.downloads = [];
    console.log(ToastService);


    DashService.getDownloads().then(function (response) {
        console.log(response);
        $scope.downloads = response.data;
      }, function(error){
        console.log(error);
        ToastService.showToast("Oops! Something went wrong fetching data");
      });

  }

})();
