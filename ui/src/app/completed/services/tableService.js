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
   var removeDownload = function(id) {
      console.log(id);
      return $http({
        method: 'DELETE',
        url: BassaUrl + '/api/downloads/' + id
      });
    };

    return {
      getCompletedDownloads : getCompletedDownloads,
      removeDownload : removeDownload
    };


  }
})();
