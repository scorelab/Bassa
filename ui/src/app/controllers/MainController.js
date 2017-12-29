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

    if(UserService.getAuthLevel() !== '0') {
      navService.loadAllItems().then(function(menuItems) {
        for(var i =0;i<menuItems.length;i++){
          if(menuItems[i].name == 'Admin'){
            menuItems.splice(i,1);
            break;
          }
        }
        $scope.menuItems = [].concat(menuItems);
      });
    }
    else {
      navService.loadAllItems().then(function(menuItems) {
        $scope.menuItems = [].concat(menuItems);
      });
    }

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
