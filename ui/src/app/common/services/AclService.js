'use strict;'

angular.module('app')
  .factory('AclService', ['BassaUrl', 'UserService', function(BassaUrl, UserService) {

    var AclStack = []

    function Context(parent_id, access) {
      this.parent_id = parent_id
      this.access = access
    };

    Context.prototype.getParentId = function() {
      return this.parent_id
    };

    Context.prototype.getAccessLevel = function() {
      return this.access
    };

    Context.build = function(parent_id, access) {
      return new Context (
        parent_id,
        access
      );
    };

    function pushContext(context) {
      AclStack.push(context)
    };

    function popContext() {
      AclStack.pop()
    };

    function extractContext() {
      return AclStack.pop()
    };

    function clearContext() {
      AclStack.length = 0
    };

  }

]);
