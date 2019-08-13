(function() {
  'use strict;'

  angular.module('app')
    .service('DriveService', ['$http', 'UserService', 'BassaUrl', DriveService]);

    function DriveService($http, UserService, BassaUrl) {
      var user_id = UserService.getUserId()

      var fetch_shared = function(user_id) {
        return $http({
          method: 'GET',
          url: BassaUrl + '/api/user/' + user_id + '/drive/shared'
        })
      }

      var fetch_entity_children = function(id, user_id) {
        return $http({
          method: 'GET',
          url: BassaUrl + '/api/user/' + user_id + '/drive/' + id + '/children'
        })
      }

      var fetch_entity = function(id, user_id, e_type) {
        return $http({
          method: 'GET',
          url: BassaUrl + '/api/user/' + user_id + '/drive/' + id,
          params: { type: e_type }
        })
      }

      var add_entity = function(user_id, e_type, name, parent_id) {
        var body = {
          name: name,
          parent_id: parent_id
        }
        return $http({
          method: 'POST',
          url: BassaUrl + '/api/user/' + user_id + '/drive/add',
          params: { type: e_type },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: body
        })
      }

      var edit_entity = function(id, user_id, e_type, new_name) {
        var body = {
          new_name: new_name
        }
        return $http({
          method: 'POST',
          url: BassaUrl + '/api/user/' + user_id + '/drive/' + id + '/edit',
          params: { type: e_type },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: body
        })
      }

      var remove_entity = function(id, user_id, e_type) {
        return $http({
          method: 'DELETE',
          url: BassaUrl + '/api/user/' + user_id + '/drive/' + id + '/remove',
          params: { type: e_type }
        })
      }

      var move_entity = function(id, user_id, parent_name) {
        var body = {
          parent_name: parent_name
        }
        return $http({
          method: 'POST',
          url: BassaUrl + '/api/user/' + user_id + '/drive/' + id + '/move',
          params: { type: e_type },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: body
        })
      }

      var check_access = function(id, user_id, e_type) {
        return $http({
          method: 'GET',
          url: BassaUrl + '/api/user/' + user_id + '/drive/' + id + '/check',
          params: { type: e_type }
        })
      }

      var grant_access = function(id, user_name, e_type, access) {
        var body = {
          user_name: user_name,
          access: access
        }
        return $http({
          method: 'POST',
          url: BassaUrl + '/api/user/drive/' + id + '/grant',
          params: { type: e_type },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: body
        })
      }

      return {
        fetch_shared: fetch_shared,
        fetch_entity_children: fetch_entity_children,
        fetch_entity: fetch_entity,
        add_entity: add_entity,
        edit_entity: edit_entity,
        remove_entity: remove_entity,
        move_entity: move_entity,
        check_access: check_access,
        grant_access: grant_access
      }
    }
})();