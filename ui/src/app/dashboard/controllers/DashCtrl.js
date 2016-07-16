(function(){

  angular
    .module('app')
    .controller('DashCtrl', [ '$scope', 'ToastService', 'DashService',
      DashCtrl
    ]);

  function DashCtrl($scope, ToastService, DashService) {
    $scope.dlink = {link: ''};
    $scope.downloads = []

    var socket = io.connect('http://localhost:5000');

    socket.on('connect', function() {
      console.log("conneted");
    });

    socket.on('daemon', function(data) {
      console.log("daemon activated", data);
      _.forEach($scope.downloads, function(obj){
        console.log(obj);
        if (obj.id == data.id) {
          console.log(obj.progress, data.progress);
          obj.progress = data.progress;
          $scope.$apply();
        }
      });
      console.log($scope.downloads);
    });



    $scope.addLink = function() {
      DashService.addDownload($scope.dlink).then(function (response) {
        $scope.dlink.link = '';
        ToastService.showToast("Link added");
      }, function(error){
        $scope.dlink.link = '';
        ToastService.showToast("Oops! Something went wrong");
      });
    };

    DashService.getDownloads().then(function (response) {
      var data = response.data;
      console.log(data);
      $scope.downloads = _.filter(data, function(d) {return d.status==0});
      $scope.downloads = _.map($scope.downloads, function(element) {
           return _.extend({}, element, {progress: 0});
      });
    }, function(error){
      ToastService.showToast("Oops! Something went wrong when fetching data");
    });

  }

})();
