(function(){
  'use strict';
  angular
       .module('app')
       .controller('MainController', [
          'navService', '$mdSidenav', '$mdBottomSheet', '$log', '$q', '$state', 'ToastService', 'UserService',
          MainController
       ]);

  function MainController(navService, $mdSidenav, $mdBottomSheet, $log, $q, $state, ToastService, UserService) {
    var vm = this;

    vm.menuItems = [ ];
    vm.selectItem = selectItem;
    vm.title = $state.current.data.title;
    vm.showSimpleToast = ToastService.showToast;
    vm.toggleRightSidebar = toggleRightSidebar;
    vm.logout = logout;

    navService
      .loadAllItems()
      .then(function(menuItems) {
        vm.menuItems = [].concat(menuItems);
      });

    var logout = function () {
      UserService.removeToken();
    };

    function toggleRightSidebar() {
        $mdSidenav('right').toggle();
    }

    function selectItem (item) {
      vm.title = item.name;
      vm.showSimpleToast(vm.title);
    }

  }

})();
