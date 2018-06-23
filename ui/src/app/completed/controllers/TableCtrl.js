(function(){
  'use strict';
  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'BassaUrl', 'ToastService', 'TableService', 'UtilityService', TableCtrl]);

  function TableCtrl($scope, BassaUrl, ToastService, TableService, UtilityService) {
    $scope.downloads = [];
    $scope.isGridVisible = false;
    var setSize = function(lst) {
      lst.data.forEach(function(download) {
        download.size = UtilityService.formatBytes(download.size);
      });
      return lst;
    };
    TableService.getCompletedDownloads().then(function (response) {
      response = setSize(response);
      $scope.downloads = response.data;
    }, function(error){
      ToastService.showToast('Oops! Something went wrong fetching data');
    });
    $scope.startDownload = function (downloadGID) {
      let token = window.localStorage.getItem("Token");
      if(token) {
        window.location.href = BassaUrl + '/api/file?gid=' + downloadGID + "&token=" + token;
      }else{
        ToastService.showToast("Unable to process your download request")
      }
    }
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
          fileExtensionName = '_page';
        }
      }else{
        fileExtensionName = '_page';
      }
      return fileExtensionName;
    }

    function isExtensionMatch(extensionName) {
      return fileTypeArray.indexOf(extensionName) !== -1;
    }
  }
})();

