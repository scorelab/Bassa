(function() {
  'use strict;'

  angular.module('app')
    .controller('NotifController', [ '$scope', '$mdDialog', 'UserService', 'NotifService', NotifController ]);

    function NotifController($scope, $mdDialog, UserService, NotifService) {

      $scope.notifs = []
      $scope.unread = false
      user_id = UserService.getUserId()

      $scope.checkNotifs = function($mdOpenMenu) {
        $scope.unread = false
        $mdOpenMenu()
      }

      var get_notifs = function () {
        NotifService.fetch_notifications(user_id).then(function(response) {
          if(response.data.length > $scope.notifs.length) $scope.unread = true
          $scope.notifs.length = 0
          for (notif in response.data) {
            $scope.notifs.push(notif[0])
          }
        }).catch(function(error) {
            console.error(error)
            ToastService.showToast('Couldn\'t load activity')
        })
        // poll function every 2 minutes
        setTimeout(get_notifs, 120000)
      }

      get_notifs()

    }
})();