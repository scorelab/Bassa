(function(){

  angular
    .module('app')
    .controller('AdminCtrl', [ '$scope', 'ToastService', 'AdminService', AdminCtrl]);

  function AdminCtrl($scope, ToastService, AdminService) {

    $scope.signup_requests = [];

    $scope.start = function() {
      AdminService.startDownloads().then(function (response) {
        ToastService.showToast("Downloading");
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    $scope.kill = function() {
      AdminService.killDownloads().then(function (response) {
        ToastService.showToast("Paused all downloads");
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    $scope.approve = function(username) {
      AdminService.approve(username).then(function (response) {
        ToastService.showToast("Approved", username);
        getRequests();
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    var getRequests = function() {
      AdminService.getSignupRequests().then(function (response) {
        $scope.signup_requests = response.data;
      });
    };

    getRequests();


  }

})();
