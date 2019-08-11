(function() {
  'use strict;'

  angular.module('app')
    .controller('DriveCtrl', [ '$scope', 'ToastService', 'DriveService', 'AclService', 'UserService', DriveCtrl ]);

    function DriveCtrl($scope, ToastService, DriveService, AclService, UserService) {

      $scope.folders = []
      $scope.files = []
      $scope.showBackNav = true

      var user_id = UserService.getUserId()

      this.init = function () {
        $scope.children(0)
        checkBackNav()
      }

      $scope.children = function (id) {
        DriveService.fetch_entity_children(id, user_id).then(function(response) {
          data = response.data
          $scope.folders.length = 0
          $scope.files.length = 0
          data.forEach(function(elem) {
            if (elem['type'] == 'fr') $scope.folders = elem['items']
            else if (elem['type'] == 'fl') $scope.files = elem['items']
          })
          AclService.pushContext(AclService.Context.build(id, 'owner'))
          checkBackNav()
        }, function(error) {
          ToastService.showToast(error)
        })
      }

      $scope.get = function (id, e_type) {
        DriveService.fetch_entity(id, user_id, e_type).then(function(response) {
          ToastService.showToast('Success')
        }, function(error) {
            ToastService.showToast(error)
        })
      }

      $scope.add = function (name, e_type) {
        id = AclService.extractContext().getParentId()
        DriveService.add_entity(user_id, e_type, name, id).then(function(response) {
          if (response.status == 200) {
            $scope.children(id)
            ToastService.showToast('Success')
          }
        }, function(error) {
            ToastService.showToast(error)
        })
      }

      $scope.edit = function (id, e_type, new_name) {
        DriveService.edit_entity(id, user_id, e_type, new_name).then(function(response) {
          if (response.status == 200) {
            $scope.children(id)
            ToastService.showToast('Success')
          }
        }, function(error) {
            ToastService.showToast(error)
        })
      }

      $scope.delete = function(id, e_type) {
        DriveService.remove_entity(id, user_id, e_type).then(function(response) {
          if(response.status == 200) {
            $scope.children(id)
            ToastService.showToast('Success')
          }
        }, function(error) {
            ToastService.showToast(error)
        })
      }

      $scope.navigateBack = function() {
        AclService.popContext()
        current = AclService.extractContext()
        current_id = AclService.getParentId(current)
        $scope.children(current_id)
        checkBackNav()
      }

      var checkBackNav = function() {
        current = AclService.extractContext()
        current_id = AclService.getParentId(current)
        if (current_id == 0) $scope.showBackNav = false
      }

      this.init()
    }
})();