(function() {
  'use strict;'

  angular.module('app')
    .controller('DriveCtrl', [ '$scope', 'ToastService', 'DriveService', 'AclService', 'UserService', 'UploadService', DriveCtrl ]);

    function DriveCtrl($scope, ToastService, DriveService, AclService, UserService, UploadService) {

      $scope.folders = []
      $scope.files = []
      $scope.sharedFolders = []
      $scope.sharedFiles = []
      $scope.showBackNav = true
      $scope.rootLevel = false

      var user_id = UserService.getUserId()

      this.init = function () {
        $scope.children(0)
        $scope.shared(user_id)
        checkIfRootLevel()
      }

      $scope.shared = function (user_id) {
        DriveService.fetch_shared(user_id).then(function(response) {
          data = response.data
          $scope.sharedFolders.length = 0
          $scope.sharedFiles.length = 0
          data.forEach(function(elem) {
            if (elem['type'] == 'fr') $scope.sharedFolders = elem['items']
            else if (elem['type'] == 'fl') $scope.sharedFiles = elem['items']
          })
          checkIfRootLevel()
        }, function(error) {
            ToastService.showToast(error)
        })
      }

      $scope.children = function (id, access) {
        DriveService.fetch_entity_children(id, user_id).then(function(response) {
          var access_level = compareAccess(id, 'fr', access)
          data = response.data
          $scope.folders.length = 0
          $scope.files.length = 0
          data.forEach(function(elem) {
            if (elem['type'] == 'fr') $scope.folders = elem['items']
            else if (elem['type'] == 'fl') $scope.files = elem['items']
          })
          AclService.pushContext(AclService.Context.build(id, access_level))
          checkIfRootLevel()
        }, function(error) {
            ToastService.showToast(error)
        })
      }

      $scope.get = function (id, e_type) {
        DriveService.fetch_entity(id, user_id, e_type).then(function(response) {
          // TODO: Display information/open file
          ToastService.showToast('Success')
        }, function(error) {
            ToastService.showToast(error)
        })
      }

      $scope.add = function (name, e_type) {
        current = AclService.extractContext()
        current_id = AclService.getParentId(current)
        current_access = AclService.getAccessLevel(current)

        if (current_access != 'read') {

            if (e_type == 'fr') {
              DriveService.add_entity(user_id, e_type, name, current_id).then(function(response) {
                if (response.status == 200) {
                  $scope.children(current_id,current_access)
                  ToastService.showToast('Success')
                }
              }, function(error) {
                  ToastService.showToast(error)
              })
            } else {
                uploadFile(current_id)
            }

        } else {
            ToastService.showToast('You don\'t have permission for this action!')
        }
      }

      $scope.edit = function (id, e_type, new_name, access) {
        var access_level = compareAccess(id, e_type, access)
        if (access_level != 'read') {
          DriveService.edit_entity(id, user_id, e_type, new_name).then(function(response) {
            if (response.status == 200) {
              $scope.children(id)
              ToastService.showToast('Success')
            }
          }, function(error) {
              ToastService.showToast(error)
          })
        } else {
            ToastService.showToast('You don\'t have permission for this action!')
        }
      }

      $scope.delete = function(id, e_type, access) {
        var access_level = compareAccess(id, e_type, access)
        if (access_level != 'owner') {
          DriveService.remove_entity(id, user_id, e_type).then(function(response) {
            if(response.status == 200) {
              $scope.children(id)
              ToastService.showToast('Success')
            }
          }, function(error) {
              ToastService.showToast(error)
          })
        } else {
            ToastService.showToast('You don\'t have permission for this action!')
        }
      }

      $scope.navigateBack = function() {
        AclService.popContext()
        current = AclService.extractContext()
        current_id = AclService.getParentId(current)
        current_access = AclService.getAccessLevel(current)
        $scope.children(current_id, current_access)
        if (current_id == 0) $scope.shared(user_id)
        checkIfRootLevel()
      }

      var uploadFile = function (parent_id) {
        var file = $scope.fileToUpload
        UploadService.uploadFile(file, parent_id).then(function (response) {
            $scope.serverResponse = response
            ToastService.showToast('Upload successful')
        }, function (error) {
            $scope.serverResponse = error
            ToastService.showToast('Upload failed')
        })
      }

      var checkIfRootLevel = function() {
        current = AclService.extractContext()
        current_id = AclService.getParentId(current)
        if (current_id == 0) {
          $scope.showBackNav = false
          $scope.rootLevel = true
        }
      }

      var compareAccess = function(id, e_type, access) {
        current = AclService.extractContext()
        current_access = AclService.getAccessLevel(current)
        access_level = (typeof access !== 'undefined')? access : current_access
        var fetch_access = ''
        DriveService.check_access(id, user_id, e_type).then(function(response) {
          if(response.data.length) fetch_access = response.data[0][0]
        }, function(error) {
          ToastService.showToast(error)
        })
        access_level = fetch_access || access_level
        return access_level
      }

      this.init()
    }
})();