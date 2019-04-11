/* global document, sessionStorage */
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
    const x = document.getElementsByClassName('parent-container')[0];
    x.id = 'temp_parent_id';
    const isDarkThemeOn = sessionStorage.getItem('isDarkThemeOn');
    if (isDarkThemeOn === 'true') {
      document.getElementById('temp_parent_id').style.backgroundColor = '#404040';
      $scope.sidenavTheme = 'dark';
    }

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

    function selectItem (item) {
      $scope.title = item.name;
      $scope.showSimpleToast($scope.title);
    }

  }

})();
