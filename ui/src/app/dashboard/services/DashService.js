(function(){
  'use strict';

  angular.module('app')
        .service('DashService', [
        '$http', 'BassaUrl',
      dashService
  ]);

  function dashService($http, BassaUrl){
    var addDownload = function(link) {
      return $http({
          method: 'POST',
          url: BassaUrl + '/api/download',
          data: JSON.stringify(link),
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      });
    };

    var getDownloads = function() {
      return $http({
        method: 'GET',
        url: BassaUrl + '/api/downloads/1'
      });
    };

    return {
      addDownload : addDownload,
      getDownloads : getDownloads
    };
  }
})();
