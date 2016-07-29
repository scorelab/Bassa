(function(){

  angular
    .module('app')
    .controller('AdminCtrl', [ '$scope', 'ToastService', 'AdminService',
     AdminCtrl
    ]);

  function AdminCtrl($scope, ToastService, AdminService) {

    $scope.start = function() {
      console.log("start");
      AdminService.startDownloads().then(function (response) {
        console.log(response);
        ToastService.showToast("Downloading");
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    $scope.kill = function() {
      AdminService.killDownloads().then(function (response) {
        console.log(response);
        ToastService.showToast("Paused all downloads");
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };


  }

})();
