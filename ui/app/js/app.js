angular.module('bassa', ['ui.router', 'ngMaterial'])

.config(function($stateProvider, $urlRouterProvider, $httpProvider) {

  $httpProvider.interceptors.push('authorizationInterceptor');

  // Routes
  $urlRouterProvider.otherwise("/login");

  $stateProvider
    .state('app', {
      url: "/app",
      templateUrl: "views/home.html",
      controller: "RootCtrl",
      authenticate: true
    })
    .state('login', {
      url: "/login",
      templateUrl: "views/login.html",
      controller: "LoginCtrl",
      authenticate: false
    });
})

.run(function ($rootScope, $state, Security) {
  $rootScope.$on("$stateChangeStart", function(event, toState, toParams, fromState, fromParams){
    if (toState.authenticate && !Security.loggedIn()) {
      // User isn’t authenticated
      $state.transitionTo("login");
      event.preventDefault();
    }
  });
});
