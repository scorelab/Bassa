(function(){
  'use strict';
  angular
    .module('app')
    .controller('DashCtrl', [ '$scope','$window','ToastService', 'DashService', 'UserService', 'BassaUrl', '$mdDialog', DashCtrl]);
  
  function DashCtrl($scope, $window , ToastService, DashService, UserService, BassaUrl, $mdDialog) {
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
    
    socket.on('disconnect', function () {
      ToastService.showToast('server has gone away');
      $mdDialog.show(
        $mdDialog.alert()
          .clickOutsideToClose(true)
          .title('Server has gone away')
          .textContent('There is something wrong with the server, please check the errors in log files')
          .ariaLabel('Server Disconnect Alert')
          .ok('Got it!')
      );
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
    var getActiveDownloads = function() {
      DashService.getDownloads().then(function (response) {
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
        var data = response.data;
        $scope.downloads = _.filter(data, function(d) {return d.status==0});
        $scope.downloads = _.map($scope.downloads, function(element) {
          return _.extend({}, element, {progress: 0});
        });
      }, function(error){
        ToastService.showToast("Oops! Something went wrong when fetching data");
      });
    }
    $scope.removeLink = function (id) {
      // Shows window confirmation before deleting download.
      var deleteDownload = $window.confirm('Confirm download task deletion !');
      
      if(deleteDownload){
        DashService.removeDownload(id).then(function(response){
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
            ToastService.showToast("Download removed");
            getActiveDownloads();},
          function (error){
            ToastService.showToast("Download started. Entry cannot be deleted.");
          });
      }
    };
    
    getActiveDownloads();
    
  }
  
})();
