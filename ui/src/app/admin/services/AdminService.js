(function(){
  'use strict';

  angular.module('app')
    .service('AdminService', ['$http', 'BassaUrl', AdminService]);

  function AdminService($http, BassaUrl){
    var startDownloads = function() {
      return $http({
          method: 'GET',
          url: BassaUrl + '/api/download/start',
          headers: {'key': '123456789'}
      });
    };

    var killDownloads = function() {
      return $http({
        method: 'GET',
        url: BassaUrl + '/api/download/kill',
        headers: {'key': '123456789'}
      });
    };

    var getSignupRequests = function() {
      return $http({
        method: 'GET',
        url: BassaUrl + '/api/user/requests'
      });
    }

    var approve = function(username) {
      return $http({
        method: 'POST',
        url: BassaUrl + '/api/user/approve/' + username,
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      });
    }

    var getHeavyUsers = function() {
      return $http({
        method: 'GET',
        url: BassaUrl + '/api/user/heavy'
      });
    }

    var visitMinio = function() {
      var url = 'http://127.0.0.1:9000/'
      setTimeout(function(){
        window.open(url, '_blank');
         },1100)
    };

    return {
      startDownloads : startDownloads,
      killDownloads : killDownloads,
      getSignupRequests : getSignupRequests,
      approve: approve,
      visitMinio : visitMinio,
      getHeavyUsers: getHeavyUsers
    };
  }
})();
