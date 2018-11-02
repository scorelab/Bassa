(function(){
  'use strict';
  angular
    .module('app')
    .controller('TableCtrl', [ '$scope', 'ToastService', 'TableService', 'UtilityService', TableCtrl]);

  function TableCtrl($scope, ToastService, TableService, UtilityService) {
    $scope.downloads = [];
    $scope.defaultIcon = "arrow_drop_down";
    $scope.defaultDropdownClass = "dropdown-inactive"
    $scope.defaultInfoDivClass = "info-div-inactive"
    var setSize = function(lst) {
      lst.data.forEach(function(download) {
        download.size = UtilityService.formatBytes(download.size);
      })
      return lst;
    };

    $scope.toggleInfo = function(viewModel) {
      this.switchIcon(viewModel);
      this.dropDownDiv(viewModel);
      this.quickInfo(viewModel);

    }

  //Switches icon for red dropdown arrow
    $scope.switchIcon = function(viewModel) {
      var default_icon = "arrow_drop_down"
      var active_icon = "arrow_drop_up"
      if (viewModel.icon === default_icon) {
        viewModel.icon = active_icon;
      } else {
        viewModel.icon = default_icon;
      }
    };
    //Expands the div (changes css height)
    $scope.dropDownDiv = function(viewModel) {
      if (viewModel.DropdownClass === "dropdown-inactive")
        viewModel.DropdownClass = "dropdown-active";
      else
        viewModel.DropdownClass = "dropdown-inactive";
    };

    //Shows actual information
    $scope.quickInfo = function(viewModel) {
      if (viewModel.InfoClass === "info-div-inactive")
        viewModel.InfoClass = "info-div-active";
      else
        viewModel.InfoClass = "info-div-inactive";
    } ;

    //Function is called when remove button is clicked
    $scope.remove = function(viewModel) {
      //Using default confirm box, add in one later
      var answer = confirm("Remove download?");
      if (answer === true) {
        //User wants to remove row
        TableService.removeDownload(viewModel.id).then(function (response) {
          ToastService.showToast('Removed download');
        }, function(error) {
          ToastService.showToast('Oops! Something went wrong removing a download');
        });
      }

      else {}
    }

    TableService.getCompletedDownloads().then(function (response) {
      response = setSize(response);
      $scope.downloads = response.data;
    }, function(error){
      ToastService.showToast('Oops! Something went wrong fetching data');
    });

  }

})();
