'use strict;'

angular.module('app')
  .factory('AclService', ['BassaUrl', function(BassaUrl) {

    AclStack = []

    function Context(parent_id, access) {
      this.parent_id = parent_id
      this.access = access
    };

    Context.build = function(parent_id, access) {
      return new Context (
        parent_id,
        access
      );
    };

    function getParentId(context) {
      return context.parent_id
    };

    function getAccessLevel(context) {
      return context.access
    };

    function pushContext(context) {
      AclStack.push(context)
    };

    function popContext() {
      serialize()
      return AclStack.pop()
    };

    function extractContext() {
      element = popContext()
      pushContext(element)
      return element
    };

    function clearContext() {
      AclStack.length = 0
      pushContext(Context.build(0,'owner'))
    };

    function equal(a, b) {
      return (a.parent_id == b.parent_id) && (a.access == b.access)
    }

    function serialize() {
      for(var i=0; i<AclStack.length; i++) {
        for(var j=i+1; j<AclStack.length; j++) {
          if(equal(AclStack[i], AclStack[j])) AclStack.splice(j,1)
        }
      }
    };

    return {
      Context: Context,
      getParentId: getParentId,
      getAccessLevel: getAccessLevel,
      pushContext: pushContext,
      popContext: popContext,
      extractContext: extractContext,
      clearContext: clearContext
    };

  }

]);
