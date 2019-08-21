(function() {
  'use strict;'

  angular.module('app')
    .controller('NotifController', ['$mdDialog', 'UserService', 'NotifService', NotifController]);

    function NotifController($mdDialog, UserService, NotifService) {
      var nf = this;
      var menuEv = null

      nf.notifs = []
      nf.unread = false
      var user_id = UserService.getUserId()

      nf.checkNotifs = function($mdMenu, event) {
        nf.unread = false
        menuEv = event
        $mdMenu.open(event)
      }

      var get_notifs = function() {
        NotifService.fetch_notifications(user_id).then(function(response) {
          if(response.data.length > nf.notifs.length) nf.unread = true
          nf.notifs.length = 0
          _.forEach(response.data, function(notif) {
              nf.notifs.push(notif[0])
          })
        }).catch(function(error) {
            console.error(error)
            ToastService.showToast('Couldn\'t load activity')
        })
        setTimeout(get_notifs, 60000)
      }

      get_notifs()

    }
})();