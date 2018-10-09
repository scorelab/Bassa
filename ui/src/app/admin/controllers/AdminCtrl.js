(function(){
  'use strict';
  angular
    .module('app')
    .controller('AdminCtrl', [ '$scope', '$mdDialog', 'ToastService', 'AdminService', 'UtilityService', AdminCtrl]);

  function AdminCtrl($scope, $mdDialog, ToastService, AdminService, UtilityService) {

    $scope.signup_requests = [];
    $scope.usageChartData = [];

    $scope.chartOptions = {
        chart: {
            type: 'pieChart',
            height: 510,
            donut: true,
            x: function (d) { return d.user_name; },
            y: function (d) { return d.size; },
            valueFormat: (d3.format('.0f')),
            color: ['rgb(0, 150, 136)', '#E75753'],
            showLabels: false,
            showLegend: false,
            title: 'Usage statistics',
            margin: { top: -10 },
            tooltips: true,
            tooltip: {
              contentGenerator: function(d) { return d.data.user_name + ' (' + UtilityService.formatBytes(d.data.size) + ')'; }
            }
        }
    };

    $scope.start = function() {
      AdminService.startDownloads().then(function (response) {
        if(response.status === 403){
    
          var confirm = $mdDialog.confirm()
            .title('Session expires')
            .textContent('This is session expire, please login back to continue')
            .ariaLabel('403 Alert')
            .ok('Take me to Login')
            .cancel('Stay here');
    
          $mdDialog.show(confirm).then(function() {
            location.href = "/#!/login";
          }, function() {
            // nothing to do with Stay here
          });
          return ;
        }else if(response.status !== 200){
          $mdDialog.show(
            $mdDialog.alert()
              .clickOutsideToClose(true)
              .title('Server has gone away')
              .textContent('There is something wrong with the server, please check the errors in log files')
              .ariaLabel('Server Disconnect Alert')
              .ok('Got it!')
          );
          return ;
        }
        ToastService.showToast('Downloading');
      }, function(error){
        ToastService.showToast('Oops! Something went wrong');
      });
    };

    $scope.kill = function() {
      AdminService.killDownloads().then(function (response) {
        if(response.status === 403){
    
          var confirm = $mdDialog.confirm()
            .title('Session expires')
            .textContent('This is session expire, please login back to continue')
            .ariaLabel('403 Alert')
            .ok('Take me to Login')
            .cancel('Stay here');
    
          $mdDialog.show(confirm).then(function() {
            location.href = "/#!/login";
          }, function() {
            // nothing to do with Stay here
          });
          return ;
        }else if(response.status !== 200){
          $mdDialog.show(
            $mdDialog.alert()
              .clickOutsideToClose(true)
              .title('Server has gone away')
              .textContent('There is something wrong with the server, please check the errors in log files')
              .ariaLabel('Server Disconnect Alert')
              .ok('Got it!')
          );
          return ;
        }
        ToastService.showToast('Paused all downloads');
      }, function(error){
        ToastService.showToast('Oops! Something went wrong');
      });
    };

    $scope.approve = function(user) {
      AdminService.approve(user.user_name).then(function (response) {
        if(response.status === 403){
    
          var confirm = $mdDialog.confirm()
            .title('Session expires')
            .textContent('This is session expire, please login back to continue')
            .ariaLabel('403 Alert')
            .ok('Take me to Login')
            .cancel('Stay here');
    
          $mdDialog.show(confirm).then(function() {
            location.href = "/#!/login";
          }, function() {
            // nothing to do with Stay here
          });
          return ;
        }else if(response.status !== 200){
          $mdDialog.show(
            $mdDialog.alert()
              .clickOutsideToClose(true)
              .title('Server has gone away')
              .textContent('There is something wrong with the server, please check the errors in log files')
              .ariaLabel('Server Disconnect Alert')
              .ok('Got it!')
          );
          return ;
        }
        ToastService.showToast('Approved', user.user_name);
        $scope.signup_requests.splice(user, 1);
        getRequests();
      }, function(error){
        ToastService.showToast('Oops! Something went wrong');
      });
    };

    this.getRequests = function() {
      AdminService.getSignupRequests().then(function (response) {
        $scope.signup_requests = response.data;
      });
    };

    this.getHeavyUsers = function() {
      AdminService.getHeavyUsers().then(function (response) {
        $scope.usageChartData = response.data;
      });
    }

    this.getRequests();
    this.getHeavyUsers();


  }

})();
