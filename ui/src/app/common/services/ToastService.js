(function(){
  'use strict';

  angular.module('app')
        .service('ToastService', [
        '$mdToast',
      toast
  ]);

  function toast($mdToast){

    return {
      showToast : function(title) {
        $mdToast.show(
          $mdToast.simple()
            .content(title)
            .hideDelay(2000)
            .position('bottom right')
        );
      }
    };
  }
})();
