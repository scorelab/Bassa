angular.module('bassa', ['ui.router', 'ngMaterial'])

.config(function($stateProvider, $urlRouterProvider, $httpProvider) {

  $httpProvider.interceptors.push('authorizationInterceptor');

  // Routes
  $urlRouterProvider.otherwise("/login");

  $stateProvider
    .state('app', {
      url: "/app",
      templateUrl: "views/home.html",
      controller: "RootCtrl"
    })
    .state('login', {
      url: "/login",
      templateUrl: "views/login.html",
      controller: "LoginCtrl"
    });
});
