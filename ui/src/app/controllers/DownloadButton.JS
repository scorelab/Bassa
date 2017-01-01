(function(){

  angular
    .module('app')
    .controller('Download', [ '$scope','UtilityService', 'TableService',]);

  function Download($scope, UtilityService, TableService,) {
    $scope.downloads = [];

    var get = function(src) {
      src.data.forEach(function(download) {
        download.size = UtilityService.formatBytes(download.size);
      })
      return src;
    };

    TableService.getCompletedDownloads().then(function (response) {
      dataList = get(response);
      $scope.downloads = dataList.data;
    }

  }

})();
