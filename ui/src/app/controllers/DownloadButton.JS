(function(){

  angular
    .module('app')
    .controller('Download', [ '$scope','$http','BassaUrl']);

  function Download($scope, '$http','BassaUrl') {
    $scope.downloads = [];

    function downloadFiles(files) {
            return $http.get(BassaUrl + 'api/use/downloads', files);
        }
  }

})();
