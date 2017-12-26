(function(){
  'use strict';
  angular
    .module('app')
    .controller('AdminCtrl', [ '$scope', 'ToastService', 'AdminService', 'UtilityService', AdminCtrl]);

  function AdminCtrl($scope, ToastService, AdminService, UtilityService) {

    $scope.signup_requests = [];
    $scope.usageChartData = [];
    $scope.blocked_users = [];
    $scope.unblocked_users = [];

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
        ToastService.showToast('Downloading');
      }, function(error){
        ToastService.showToast('Oops! Something went wrong');
      });
    };

    $scope.kill = function() {
      AdminService.killDownloads().then(function (response) {
        ToastService.showToast('Paused all downloads');
      }, function(error){
        ToastService.showToast('Oops! Something went wrong');
      });
    };

    $scope.approve = function(username) {
      AdminService.approve(username).then(function (response) {
        ToastService.showToast('Approved', username);
        getRequests();
      }, function(error){
        ToastService.showToast('Oops! Something went wrong');
      });
    };

    $scope.block = function(username) {
      AdminService.block(username).then(function (response) {
        ToastService.showToast('Blocked', username);
        //reloading data
        AdminService.getBlockedUsers().then(function (response) {
          $scope.blocked_users = response.data;
        });

        AdminService.getUnblockedUsers().then(function (response) {
          $scope.unblocked_users = response.data;
        });
      }, function(error){
        ToastService.showToast('Oops! Something went wrong');
      });
    };

    $scope.unblock = function(username) {
      AdminService.unblock(username).then(function (response) {
        ToastService.showToast('Unblocked', username);
        //reloading data
        AdminService.getBlockedUsers().then(function (response) {
          $scope.blocked_users = response.data;
        });

        AdminService.getUnblockedUsers().then(function (response) {
          $scope.unblocked_users = response.data;
        });
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

    this.getBlockedUsers = function() {
      AdminService.getBlockedUsers().then(function (response) {
        $scope.blocked_users = response.data;
      });
    }

    this.getUnblockedUsers = function() {
      AdminService.getUnblockedUsers().then(function (response) {
        $scope.unblocked_users = response.data;
      });
    }

    this.getRequests();
    this.getBlockedUsers();
    this.getUnblockedUsers();
    this.getHeavyUsers();


  }

})();
