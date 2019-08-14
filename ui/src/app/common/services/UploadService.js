(function () {
    'use strict';
    angular.module('app')
      .service('UploadService', ['BassaUrl', '$http', '$q', 'UserService', UploadService])

    function UploadService(BassaUrl, $http, $q, UserService) {
        var user_id = UserService.getUserId()

        var uploadFile = function (file, parent_id) {

            var uploadUrl = BassaUrl + '/api/user/' + user_id + '/drive/' + parent_id + '/upload'
            var fileFormData = new FormData()
            fileFormData.append('file', file)

            var deferred = $q.defer()
            $http.post(uploadUrl, fileFormData, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}

            }).then(function (response) {
                deferred.resolve(response)

            }).catch(function (response) {
                deferred.reject(response)
            });

            return deferred.promise
        }

        return {
          uploadFile: uploadFile
        }
    }
})();