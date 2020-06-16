(function(){
  'use strict';
  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', '$mdToast', '$mdDialog','BassaUrl', 'ToastService', 'TableService', 'UtilityService', TableCtrl]);

  function TableCtrl($scope, $mdToast, $mdDialog, BassaUrl, ToastService, TableService, UtilityService) {
    $scope.downloads = [];
    $scope.isGridVisible = false;
    $scope.zipProcessCounter = 0;
    $scope.isShowingActions = false;
    $scope.checkedFileArray = [];
    $scope.shareLink = BassaUrl;
    $scope.isShowingCheckbox = false;
    let progressDialog = {
      controller: DialogController,
      template: '<md-progress-linear md-mode="indeterminate"/>', // later change it to a template URL
      parent: angular.element(document.body),
      clickOutsideToClose: false,
      locals : {}
    };
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
        window.location.href = BassaUrl + '/api/file?gid=' + downloadGID + "&share=" + token;
      }else{
        ToastService.showToast("Unable to process your download request")
      }
    };
    $scope.compressFiles = function(listOfGid){
      TableService.startCompression(listOfGid).then(function (response) {
        $mdToast.show($scope.zipToast).then(function (toastResponse) {
        if(toastResponse === 'ok'){
          ToastService.showToast('Download will start in a while');
        }
        });
        if(response.data['process_id'] != null) {
          $scope.zipProcessCounter++;
          if(response.data['progress'] === 1){
            $scope.startDownload(response.data['process_id']);
            return;
          }
          compressionProgressHandler(response.data['process_id']);
        }else{
          ToastService.showToast('Oops! Something went wrong fetching data');
        }
      }, function(error){
        ToastService.showToast('Oops! Something went wrong fetching data');
      });
    };
    $scope.generateSharingLink = function(){
      if($scope.checkedFileArray.length === 0){
        ToastService.showToast("Please checkbox some files to share");
        return;
      }

      TableService.startCompression($scope.checkedFileArray).then(function (response) {
        $mdDialog.show(progressDialog);
        if(response.data['process_id'] != null) {
          $scope.shareLink = BassaUrl;
          $scope.shareLink += "/api/file?gid="+response.data['process_id']+"&share=true";
          $mdDialog.hide(progressDialog);
          progressDialog.locals = {
            params:[$scope.shareLink]
          };
          progressDialog.template = '<div>' +
            '<div style="margin-top: 20px; margin-left: 20px;"><input style="margin-left: 10px" readonly value="'+$scope.shareLink+'"><div>'+
            '<div>'+
            '<md-button ng-click="copyText()">Copy it</md-button>'+
            '<md-button ng-click="closeDialog()">Close</md-button>'+
            '</div>'+
            '</div>';
          $mdDialog.show(progressDialog);
          // FIXME :: we can either give the link after it gets compressed, which might be a slow process
        }else{
          ToastService.showToast('Oops! Something went wrong fetching data');
        }
      }, function(error){
        ToastService.showToast('Oops! Something went wrong fetching data');
      });
    };
    function DialogController($scope, $mdDialog, params){
      $scope.copyText = function () {
        const tmpElement = document.createElement('textarea');
        tmpElement.value = params[0]; // share link
        document.body.appendChild(tmpElement);
        tmpElement.select();
        document.execCommand('copy');
        document.body.removeChild(tmpElement);
        $scope.closeDialog();
      };
      $scope.closeDialog = function () {
        $mdDialog.hide(progressDialog);
        resetVariables();
      };
      function resetVariables() {
        progressDialog = {
          controller: DialogController,
          template: '<md-progress-linear md-mode="indeterminate"/>', // later change it to a template URL
          parent: angular.element(document.body),
          clickOutsideToClose: false,
          locals : {}
        };
      }
    }
    $scope.deselectAll = function(){
      $scope.isShowingActions = false;
      angular.forEach($scope.downloads, function (item) {
        item.checked = false;
      });
      $scope.checkedFileArray = []; // using initialization technique instead of popping out
    };
    $scope.selectAll = function(){
      $scope.checkedFileArray = [];
      $scope.isShowingActions = true;
      angular.forEach($scope.downloads, function (item) {
        item.checked = true;
        $scope.checkedFileArray.push(item.gid);
      });
    };
    $scope.onFileItemClick = function () {
      $scope.isShowingCheckbox = true;
      if($scope.checkedFileArray.length === 0) {
	      $scope.isShowingActions = false;
      }else{
        $scope.isShowingActions = true;
      }
    };
    $scope.selectThisItem = function (item) {
      if(item.checked){
        $scope.checkedFileArray.push(item.gid);
      }else{
        $scope.checkedFileArray.pop(item.gid);
        if($scope.checkedFileArray.length === 0){
          $scope.isShowingActions = false;
        }
      }
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

    $scope.downloadFromMinio = function (downloadId) {
      ToastService.showToast('Generating download link');
      TableService.downloadFromMinio(downloadId).then( function(response) {
        let urlData = response.data;
        let url = urlData['url'];
        window.open(url)
      })
    };

  }
})();

