(function(){

  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'ToastService', 'TableService',
      TableCtrl
    ]);

  function TableCtrl($scope, ToastService, TableService) {
    $scope.dlink = {link: ''};
    $scope.downloads = [];

    TableService.getCompletedDownloads().then(function (response) {
        $scope.downloads = response.data;
      }, function(error){
        ToastService.showToast("Oops! Something went wrong fetching data");
      });

  }

})();
