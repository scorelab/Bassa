(function(){

  angular
    .module('app')
    .controller('DashCtrl', [ '$scope', 'ToastService', 'DashService',
      DashCtrl
    ]);

  function DashCtrl($scope, ToastService, DashService) {
    $scope.dlink = {link: ''};
    $scope.downloads = [];
    console.log(ToastService);

    $scope.addLink = function() {
      DashService.addDownload($scope.dlink).then(function (response) {
        $scope.dlink.link = '';
        ToastService.showToast("Link added");
      }, function(error){
        $scope.dlink.link = '';
        ToastService.showToast("Oops! Something went wrong");
      });
    };

  }

})();
