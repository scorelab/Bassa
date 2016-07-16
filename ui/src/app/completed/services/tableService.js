(function(){
  'use strict';

  angular.module('app')
        .service('TableService', [
        '$http', 'BassaUrl',
      tableService
  ]);

  function tableService($http, BassaUrl){

    var getCompletedDownloads = function() {
      return $http({
        method: 'GET',
        url: BassaUrl + '/api/downloads/1'
      });
    };

    return {
      getCompletedDownloads : getCompletedDownloads
    };
  }
})();
