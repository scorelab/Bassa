(function(){
  'use strict';
  angular
       .module('app')
       .controller('MainController', [
          'navService', '$mdSidenav', '$mdBottomSheet', '$log', '$q', '$state','$scope' , 'ToastService', 'UserService',
          MainController
       ]);

  function MainController(navService, $mdSidenav, $mdBottomSheet, $log, $q, $state, $scope, ToastService, UserService) {
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
        if (UserService.getAuthLevel() !== 0) {
          var index = 0;
          let no_of_menu_items = menuItems.length;
          for (; index < no_of_menu_items; index=index+1) {
            if (menuItems[index].name === 'Admin') {
              menuItems.splice(index, 1);
              break;
            }
          }
        }
        $scope.menuItems = [].concat(menuItems);
      });

    var logout = function () {
      UserService.cleanUpStorage();
    };

    function toggleRightSidebar() {
        $mdSidenav('right').toggle();
    }

    function selectItem (item) {
      $scope.title = item.name;
      $scope.showSimpleToast($scope.title);
    }

  }

})();
