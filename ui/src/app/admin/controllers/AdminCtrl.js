(function(){

  angular
    .module('app')
    .controller('AdminCtrl', [ '$scope', 'ToastService', 'AdminService', AdminCtrl]);

  function AdminCtrl($scope, ToastService, AdminService) {

    $scope.signup_requests = [];
    $scope.usageChartData = [];

    var formatBytes = function(bytes, decimals) {
       if(bytes == 0) return '0 Byte';
       var k = 1000;
       var dm = decimals + 1 || 3;
       var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
       var i = Math.floor(Math.log(bytes) / Math.log(k));
       return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    $scope.chartOptions = {
        chart: {
            type: 'pieChart',
            height: 510,
            donut: true,
            x: function (d) { return d.user_name; },
            y: function (d) { return d.size; },
            valueFormat: (d3.format(".0f")),
            color: ['rgb(0, 150, 136)', '#E75753'],
            showLabels: false,
            showLegend: false,
            title: 'Usage statistics',
            margin: { top: -10 },
            tooltips: true,
            tooltip: {
              contentGenerator: function(d) { return d.data.user_name + ' (' + formatBytes(d.data.size) + ')'; }
            }
        }
    };

    $scope.start = function() {
      AdminService.startDownloads().then(function (response) {
        ToastService.showToast("Downloading");
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    $scope.kill = function() {
      AdminService.killDownloads().then(function (response) {
        ToastService.showToast("Paused all downloads");
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    $scope.approve = function(username) {
      AdminService.approve(username).then(function (response) {
        ToastService.showToast("Approved", username);
        getRequests();
      }, function(error){
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    var getRequests = function() {
      AdminService.getSignupRequests().then(function (response) {
        $scope.signup_requests = response.data;
      });
    };

    var getHeavyUsers = function() {
      AdminService.getHeavyUsers().then(function (response) {
        $scope.usageChartData = response.data;
      });
    }

    getRequests();
    getHeavyUsers();


  }

})();
