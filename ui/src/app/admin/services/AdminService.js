(function(){
  'use strict';

  angular.module('app')
        .service('AdminService', [
        '$http', 'BassaUrl',
     AdminService
  ]);

  function AdminService($http, BassaUrl){
    var startDownloads = function() {
      return $http({
          method: 'GET',
          url: BassaUrl + '/download/start',
          headers: {'key': '123456789'}
      });
    };

    var killDownloads = function() {
      return $http({
        method: 'GET',
        url: BassaUrl + '/download/kill',
        headers: {'key': '123456789'}
      });
    };

    return {
      startDownloads : startDownloads,
      killDownloads : killDownloads
    };
  }
})();
