(function(){
  'use strict';

  angular.module('app')
    .service('TableService', ['$http', 'BassaUrl', TableService]);

  function TableService($http, BassaUrl){

    var getCompletedDownloads = function() {
      return $http({
        method: 'GET',
        url: BassaUrl + '/api/downloads/1'
      });
    };
    var startCompression = function (gids) {
      return $http({
          method: 'POST',
          url : BassaUrl + '/api/compress',
          data : {'gid' : gids}
      })
    };
    var compressionProgress = function (progressId) {
      return $http({
          method: 'GET',
          url : BassaUrl + '/api/compression-progress?gid=' + progressId
      })
    };

    return {
      getCompletedDownloads : getCompletedDownloads,
      startCompression : startCompression,
      compressionProgress : compressionProgress
    };
  }
})();
