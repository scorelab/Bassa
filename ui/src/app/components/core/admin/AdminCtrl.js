(function(){
  'use strict';
  angular
    .module('app')
    .controller('AdminCtrl', [ '$scope', 'ToastService', 'AdminService', 'UtilityService', 'NotifService', 'UserService', AdminCtrl]);

  function AdminCtrl($scope, ToastService, AdminService, UtilityService, NotifService, UserService) {

    $scope.signup_requests = [];
    $scope.usageChartData = [];
    var username = UserService.getUsername()

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

    $scope.approve = function(user) {
      AdminService.approve(user.user_name).then(function (response) {
        var notif = 'Your signup request was approved by ' + username
        if (response.status == 200) {
          ToastService.showToast('Approved', user.user_name);
          $scope.signup_requests.splice(user, 1);
          NotifService.create_notification(user.user_name, notif)
        }
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
