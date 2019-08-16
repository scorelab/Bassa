(function() {
  'use strict;'

  angular.module('app')
    .service('NotifService', ['$http', 'BassaUrl', NotifService]);

    function NotifService($http, BassaUrl) {

      var fetch_notifications = function(user_id) {
        return $http({
          method: 'GET',
          url: BassaUrl + '/api/user/' + user_id + '/notifications'
        })
      }

      var create_notification = function(user_name, notif) {
        var body = {
          notif: notif
        }
        return $http({
          method: 'POST',
          url: BassaUrl + '/api/user/' + user_name + '/notification/add',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: body
        }).then(function(response) {
            // handle success
            return 'success'
        }).catch(function(error) {
            console.error(error)
            return 'Error: ' + error
        })
      }

      return {
        fetch_notifications: fetch_notifications,
        create_notification: create_notification
      }
    }
})();