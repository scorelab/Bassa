(function(){
  'use strict';
  angular
       .module('app')
       .controller('MainController', [
          'navService', '$mdSidenav', '$mdBottomSheet', '$log', '$q', '$state', '$scope', 'ToastService', 'UserService',
          'AclService', MainController
       ]);

  function MainController(navService, $mdSidenav, $mdBottomSheet, $log, $q, $state, $scope, ToastService, UserService, AclService) {
    $scope.menuItems = [ ];
    $scope.selectItem = selectItem;
    $scope.title = $state.current.data.title;
    $scope.showSimpleToast = ToastService.showToast;
    $scope.toggleRightSidebar = toggleRightSidebar;
    $scope.logout = logout;
    $scope.username =  UserService.getUsername();

    navService
      .loadAllItems()
      .then(function(menuItems) {
        $scope.menuItems = [].concat(menuItems);
      });

    var logout = function () {
      UserService.cleanUpStorage();
    };

    function toggleRightSidebar() {
        $mdSidenav('right').toggle();
    }

    function initDrive() {
      AclService.clearContext()
      $state.transitionTo('home.drive', {}, {
          reload: true,
          inherit: false,
          notify: true
      });
    }

    function selectItem (item) {
      if (item.name == 'Drive') initDrive()
      $scope.title = item.name;
      $scope.showSimpleToast($scope.title);
    }

  }

})();
