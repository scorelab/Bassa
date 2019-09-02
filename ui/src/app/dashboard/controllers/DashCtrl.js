(function(){
  'use strict';
  angular
    .module('app')
    .controller('DashCtrl', [ '$scope','$window','ToastService', 'DashService', 'UserService', 'BassaUrl', DashCtrl]);

  function DashCtrl($scope, $window , ToastService, DashService, UserService, BassaUrl) {
    var socket = io.connect(BassaUrl + '/progress');
    $scope.dlink = {link: ''};
    $scope.downloads = [];
    $scope.username = UserService.getUsername();

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

    var linkvalidator = function(link){
      var urlvalidator =/^(?:(?:https?|ftp):\/\/)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/[^\s]*)?$/i;
      var magnetvalidator = /magnet:\?xt=/i;
      if (urlvalidator.test(link) || link.match(magnetvalidator) !== null){
        return true;
      }
      else{
        return false;
        }
    }

    $scope.addLink = function() {
      if ($scope.dlink.link === '' || $scope.dlink.link === undefined || !linkvalidator($scope.dlink.link)) {
        ToastService.showToast('Please check your url');
      } else {
        DashService.addDownload($scope.dlink).then(function (response) {
          $scope.dlink.link = '';
          ToastService.showToast("Link added");
          getActiveDownloads();
        }, function(error){
          $scope.dlink.link = '';
          if (error.data.quota) {
            ToastService.showToast("Your monthly quota has been exceeded");
          } else {
            ToastService.showToast("Oops! Something went wrong :(");
          }
        });
      }
    };

    $scope.addDownload = function(keyEvent) {
  if (keyEvent.which === 13)
    $scope.addLink();
  }
  var getActiveDownloads = function() {
    DashService.getDownloads().then(function (response) {
      var data = response.data;
      $scope.filterdownloads = _.filter(data, function(d) {return d.status==0});
      $scope.downloads = _.map($scope.filterdownloads, function(obj) {
           return _.extend({}, obj, {progress: 0});
      });
    }, function(error){
      ToastService.showToast("Oops! Something went wrong when fetching data");
    });
}

    $scope.removeLink = function (index, id) {
      // Shows window confirmation before deleting download.
      var deleteDownload = $window.confirm('Confirm download task deletion !');

      if(deleteDownload){
        DashService.removeDownload(id).then(function(response){
          if(response.status === 200){
            $scope.downloads.splice(index, 1);
            ToastService.showToast("Download removed");
          }else{
            ToastService.showToast("Download could not be removed. Please try again!");
          } },
          function (error){
          ToastService.showToast("Download started. Entry cannot be deleted.");
        });
      }
     };

    getActiveDownloads();

  }

})();
