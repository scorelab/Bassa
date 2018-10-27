(function() {
  "use strict";
  angular
    .module("app")
    .controller("TableCtrl", [
      "$scope",
      "ToastService",
      "TableService",
      "UtilityService",
      TableCtrl
    ]);

  function TableCtrl($scope, ToastService, TableService, UtilityService) {
    $scope.downloads = [];
    $scope.myFunction = function(idd) {
      document.getElementById(idd).classList.toggle("show");
    };
    var setSize = function(lst) {
      lst.data.forEach(function(download) {
        download.size = UtilityService.formatBytes(download.size);
      });
      return lst;
    };

    TableService.getCompletedDownloads().then(
      function(response) {
        response = setSize(response);
        $scope.downloads = response.data;
      },
      function(error) {
        ToastService.showToast("Oops! Something went wrong fetching data");
      }
    );
  }
})();