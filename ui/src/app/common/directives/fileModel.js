(function() {
  'use strict';

  angular
    .module('app')
    .directive('fileModel', function ($parse) {
      return {
        restrict: 'A',
        link: function (scope, element, attrs) {
          var model = $parse(attrs.fileModel)
          var modelSetter = model.assign

          element.bind('change', function () {
            scope.$apply(function () {
                modelSetter(scope, element[0].files[0])
            })
          })
        }
      }
    })
})();