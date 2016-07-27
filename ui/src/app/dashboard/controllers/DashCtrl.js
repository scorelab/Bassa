(function(){

  angular
    .module('app')
    .controller('DashCtrl', [ '$scope', 'ToastService', 'DashService',
      DashCtrl
    ]);

  function DashCtrl($scope, ToastService, DashService) {
    $scope.dlink = {link: ''};
    $scope.downloads = [];
    $scope.username = localStorage.getItem('Username');


    var socket = io.connect('http://localhost:5000/progress');

    socket.on('connect', function(){
      socket.emit('join', {room: $scope.username});
    });

    socket.on('status', function(data) {
      _.forEach($scope.downloads, function(obj){
        if (obj.id == data.id) {
          obj.progress = data.progress;
          $scope.$apply();
        }
      });
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
      $scope.downloads = _.filter(data, function(d) {return d.status==0});
      $scope.downloads = _.map($scope.downloads, function(element) {
           return _.extend({}, element, {progress: 0});
      });
    }, function(error){
      ToastService.showToast("Oops! Something went wrong when fetching data");
    });

  }

})();
