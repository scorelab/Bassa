(function(){
  'use strict';

  angular.module('app')
    .service('UtilityService', [UtilityService]);

  function UtilityService(){

    var formatBytes = function(bytes, decimals) {

      if(bytes == 0) return '0 Byte';
      var k = 1000,
          dm = decimals + 1 || 3,
          sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
          i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    };

    return {
      formatBytes: formatBytes
    };

  }
})();
