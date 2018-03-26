(function(){
  'use strict';
  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', '$mdDialog', 'ToastService', 'TableService', 'UtilityService', TableCtrl]);

  function TableCtrl($scope, $mdDialog, ToastService, TableService, UtilityService) {
    $scope.downloads = [];

    var setSize = function(lst) {
      lst.data.forEach(function(download) {
        download.size = UtilityService.formatBytes(download.size);
      })
      return lst;
    };

    TableService.getCompletedDownloads().then(function (response) {
      if(response.status === 403){
        var confirm = $mdDialog.confirm()
          .title('Session expires')
          .textContent('This is session expire, please login back to continue')
          .ariaLabel('403 Alert')
          .ok('Take me to Login')
          .cancel('Stay here');
    
        $mdDialog.show(confirm).then(function() {
          location.href = "/#!/login";
        }, function() {
          // nothing to do with Stay here
        });
        return ;
      }else if(response.status !== 200){
        $mdDialog.show(
          $mdDialog.alert()
            .clickOutsideToClose(true)
            .title('Server has gone away')
            .textContent('There is something wrong with the server, please check the errors in log files')
            .ariaLabel('Server Disconnect Alert')
            .ok('Got it!')
        );
        return ;
      }
      response = setSize(response);
      $scope.downloads = response.data;
    }, function(error){
      ToastService.showToast('Oops! Something went wrong fetching data');
    });

  }

})();
