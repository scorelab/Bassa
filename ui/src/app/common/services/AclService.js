'use strict;'

angular.module('app')
  .factory('AclService', ['BassaUrl', function(BassaUrl) {

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
      element = AclStack.pop()
      pushContext(element)
      return element
    };

    function clearContext() {
      AclStack.length = 0
      pushContext(Context.build(0,'owner'))
    };

    return {
      Context: Context,
      pushContext: pushContext,
      popContext: popContext,
      extractContext: extractContext,
      clearContext: clearContext
    };

  }

]);
