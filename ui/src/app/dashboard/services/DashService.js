(function(){
  'use strict';

  angular.module('app')
        .service('DashService', [
        '$http',
      dashService
  ]);

  function dashService($http){
    var addDownload = function(link) {
      return $http({
          method: 'POST',
          url: 'http://localhost:5000/api/download',
          data: JSON.stringify(link),
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      });
    };

    var getDownloads = function() {
      return $http({
        method: 'GET',
        url: 'http://localhost:5000/api/downloads/1'
      });
    };

    return {
      addDownload : addDownload,
      getDownloads : getDownloads
    };
  }
})();
