(function(){
  'use strict';
  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', '$mdToast','BassaUrl', 'ToastService', 'TableService', 'UtilityService', TableCtrl]);

  function TableCtrl($scope, $mdToast,BassaUrl, ToastService, TableService, UtilityService) {
    $scope.downloads = [];
    $scope.isGridVisible = false;
    $scope.zipProcessCounter = 0;
    $scope.zipToast =
      $mdToast.simple()
            .content('Zipping Files')
            .hideDelay(0)
            .action('OK')
            .position('bottom right');
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
      $scope.zipProcessCounter--;
      let token = window.localStorage.getItem("Token");
      if($scope.zipProcessCounter <= 0) {
        $mdToast.hide($scope.zipToast);
      }
      if(token) {
        window.location.href = BassaUrl + '/api/file?gid=' + downloadGID + "&token=" + token;
      }else{
        ToastService.showToast("Unable to process your download request")
      }
    };
    $scope.compressFiles = function(listOfGid){
      TableService.startCompression(listOfGid).then(function (response) {
        if(response.data['process_id'] != null) {
          $scope.zipProcessCounter++;
          if(response.data['progress'] === 1){
            $scope.startDownload(response.data['process_id']);
            return;
          }
          compressionProgressHandler(response.data['process_id']);
        }else{
          ToastService.showToast('Oops! Something went wrong fetching data');
          return;
        }
        $mdToast.show($scope.zipToast).then(function (toastResponse) {
        if(toastResponse === 'ok'){
          ToastService.showToast('Download will start in a while');
        }
      });
      }, function(error){
        ToastService.showToast('Oops! Something went wrong fetching data');
      });
    };
    var compressionProgressHandler = function(downloadGid){
      var processInterval = setInterval(function () {
        TableService.compressionProgress(downloadGid).then(function (response){
          let progress = response.data['progress'];
          if(progress != null && progress === 1){
            clearInterval(processInterval);
            $scope.startDownload(downloadGid);
          }
        }, function(error){
        ToastService.showToast('Oops! Something went wrong fetching data');
      });
      }, 5000);
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

