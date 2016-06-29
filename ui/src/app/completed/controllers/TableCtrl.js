(function(){

  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'ToastService', 'DashService',
      TableCtrl
    ]);

  function TableCtrl($scope, ToastService, DashService) {
    $scope.dlink = {link: ''};
    $scope.downloads = [];

    DashService.getDownloads().then(function (response) {
        $scope.downloads = response.data;
      }, function(error){
        ToastService.showToast("Oops! Something went wrong fetching data");
      });

  }

})();
