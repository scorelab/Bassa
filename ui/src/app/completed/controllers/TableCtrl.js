(function(){

  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'ToastService', 'TableService', TableCtrl]);

  function TableCtrl($scope, ToastService, TableService) {
    $scope.dlink = {link: ''};
    $scope.downloads = [];

    var formatBytes = function(bytes, decimals) {
       if(bytes == 0) return '0 Byte';
       var k = 1000;
       var dm = decimals + 1 || 3;
       var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
       var i = Math.floor(Math.log(bytes) / Math.log(k));
       return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    var setSize = function(lst) {
      lst.data.forEach(function(download) {
        download.size = formatBytes(download.size);
      })
      return lst;
    };

    TableService.getCompletedDownloads().then(function (response) {
        response = setSize(response);
        $scope.downloads = response.data;
      }, function(error){
        ToastService.showToast("Oops! Something went wrong fetching data");
      });

  }

})();
