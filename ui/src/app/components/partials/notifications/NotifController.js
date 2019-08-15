(function() {
  'use strict;'

  angular.module('app')
    .controller('NotifController', [ '$scope', 'UserService', 'NotifService', NotifController ]);

    function NotifController($scope, UserService, NotifService) {

      $scope.notifs = []
      $scope.unread = true
      user_id = UserService.getUserId()

      this.init = function () {
        get_notifs(user_id)
      }

      var generate_notif = function (name, notif) {
        return NotifService.create_notification(name, notif)
          .then(function(response) {
            // handle success
            return 'success'
        }).catch(function(error) {
            // handle error
            return 'Error:' + error
        })
      }

      var get_notifs = function () {
        NotifService.fetch_notifications(user_id).then(function(response) {
          $scope.notifs.length = 0
          $scope.notifs = response.data
        })
        // polling function
      }

      this.init()
    }
})();