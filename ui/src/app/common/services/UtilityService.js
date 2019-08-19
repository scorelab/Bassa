(function(){
  'use strict';

  angular.module('app')
    .service('UtilityService', [UtilityService]);

  function UtilityService(){

    var fileTypeArray = ['aac', 'ai', 'aiff', 'avi', 'bmp',
        'c', 'cpp', 'css', 'csv', 'dat', 'dmg', 'doc', 'dotx', 'dwg',
        'dxf', 'eps', 'exe', 'flv', 'gif', 'h', 'hpp', 'html',
        'ics', 'iso', 'java', 'jpg', 'js', 'key', 'less', 'mid',
        'mp3', 'mp4', 'mpg', 'odf', 'ods', 'odt', 'otp', 'ots',
        'ott', 'pdf', 'php', 'png', 'ppt', 'psd', 'py', 'qt',
        'rar', 'rb', 'rtf', 'sass', 'scss', 'sql', 'tga', 'tgz',
        'tiff', 'txt', 'wav', 'xls', 'xlsx', 'xml', 'yml', 'zip'];


    function isExtensionMatch(extensionName) {
      return fileTypeArray.indexOf(extensionName) !== -1;
    }

    var getExtension = function(fileName){
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


    var formatBytes = function(bytes) {

      if(bytes == 0) return '0 Byte';
      var k = 1000,
          dm = 3,
          sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
          i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    };

    return {
      getExtension: getExtension,
      formatBytes: formatBytes
    };

  }
})();
