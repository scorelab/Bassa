angular.module('bassa', ['ui.router'])

.config(function($stateProvider, $urlRouterProvider) {
  // For any unmatched url, redirect to /app
  $urlRouterProvider.otherwise("/app");

  $stateProvider
    .state('app', {
      url: "/app",
      templateUrl: "views/home.html",
      controller: "RootCtrl"
    });
});
