(function(){
  'use strict';
  angular
       .module('app')
       .controller('MainController', [
          'navService', '$mdSidenav', '$mdBottomSheet', '$log', '$q', '$state','$scope' , 'ToastService', 'UserService',
          MainController
       ]);

  function MainController(navService, $mdSidenav, $mdBottomSheet, $log, $q, $state, $scope, ToastService, UserService) {
    var vm = this;
    console.log("console " + localStorage.getItem("user"));
    var usernm = JSON.parse(localStorage.getItem("user"));

    vm.menuItems = [ ];
    vm.selectItem = selectItem;
    vm.title = $state.current.data.title;
    vm.showSimpleToast = ToastService.showToast;
    vm.toggleRightSidebar = toggleRightSidebar;
    vm.logout = logout;

    $scope.username =  usernm.user_name;
    //$scope.username =  "hll";

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
