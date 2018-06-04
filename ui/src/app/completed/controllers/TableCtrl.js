(function(){
  'use strict';
  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'ToastService', 'TableService', 'UtilityService', TableCtrl]);

  function TableCtrl($scope, ToastService, TableService, UtilityService) {
    $scope.downloads = [];
    var setSize = function(lst) {
      lst.data.forEach(function(download) {
        download.size = UtilityService.formatBytes(download.size);
      })
      return lst;
    };
    $scope.isGridOn = false;
    TableService.getCompletedDownloads().then(function (response) {
      response = setSize(response);
      $scope.downloads = response.data;
    }, function(error){
      ToastService.showToast('Oops! Something went wrong fetching data');
    });
    $scope.changeView = function () {
        if($scope.isGridOn) {
            document.getElementById('grid-button').innerText = 'view_module';
            $scope.isGridOn = false;
        }else{
            document.getElementById('grid-button').innerText = 'view_list';
            $scope.isGridOn = true;
        }
    };
    $scope.getImage = function (fileName) {
        var fileExtensionName = getExtension(fileName);
      return "../../../assets/images/file-images/"+fileExtensionName+".png";
    };
    function getExtension(fileName){
        var fileExtension = fileName.split('.');
        var fileExtensionName ;
        if(fileExtension){
            fileExtensionName = fileExtension[fileExtension.length-1];
            if(!isExtensionMatch(fileExtensionName)){
                fileExtensionName = '_page'
            }
        }else{
            fileExtensionName = '_page'
        }
        return fileExtensionName;
    }

    function isExtensionMatch(extensionName) {
        var checkExtension = fileTypeArray.indexOf(extensionName);
        return checkExtension !== -1;
    }

  }

})();
