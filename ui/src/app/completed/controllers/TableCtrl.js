(function(){
  'use strict';
  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'BassaUrl', 'ToastService', 'TableService', 'UtilityService', TableCtrl]);

  function TableCtrl($scope, BassaUrl, ToastService, TableService, UtilityService) {
    $scope.downloads = [];
    var fileTypeArray = ['_blank', '_page', 'aac', 'ai', 'aiff', 'avi', 'bmp',
        'c', 'cpp', 'css', 'csv', 'dat', 'dmg', 'doc', 'dotx', 'dwg',
        'dxf', 'eps', 'exe', 'flv', 'gif', 'h', 'hpp', 'html',
        'ics', 'iso', 'java', 'jpg', 'js', 'key', 'less', 'mid',
        'mp3', 'mp4', 'mpg', 'odf', 'ods', 'odt', 'otp', 'ots',
        'ott', 'pdf', 'php', 'png', 'ppt', 'psd', 'py', 'qt',
        'rar', 'rb', 'rtf', 'sass', 'scss', 'sql', 'tga', 'tgz',
        'tiff', 'txt', 'wav', 'xls', 'xlsx', 'xml', 'yml', 'zip'];
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

    $scope.formatFileName = function (name) {
        var extensionName = getExtension(name);
        if (extensionName === '_page') {
            extensionName = "";
        }
        if(name.length >= 30){
            name = name.split('.')[0].slice(0, 30) + "...";
            return name + extensionName;
        }else{
            return name;
        }
    };
    $scope.startDownload = function (downloadGID) {
        window.location.href = BassaUrl+'/api/get/file?gid='+downloadGID;
    }

  }

})();
