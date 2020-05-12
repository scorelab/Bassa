'use strict';
// import { constants } from "./config";

angular.module('bassa', ['ngAnimate', 'ngCookies', 'ngTouch',
  'ngSanitize', 'ui.router', 'ngMaterial', 'nvd3', 'app'])

  .value('BassaUrl', "http://localhost:5000")

  .config(function ($stateProvider, $httpProvider, $urlRouterProvider, $mdThemingProvider,
                    $mdIconProvider, $qProvider) {

    $qProvider.errorOnUnhandledRejections(false);
    
    $httpProvider.interceptors.push('authorizationInterceptor');

    $stateProvider
      .state('home', {
        url: '',
        templateUrl: 'app/views/main.html',
        controller: 'MainController',
        controllerAs: 'vm',
        abstract: true,
        authenticate: true
      })
      .state('home.dashboard', {
        url: '/dashboard',
        templateUrl: 'app/views/dashboard.html',
        controller: 'DashCtrl',
        authenticate: true,
        data: {
          title: 'Dashboard'
        }
      })
      .state('home.admin', {
        url: '/admin',
        templateUrl: 'app/views/admin.html',
        controller: 'AdminCtrl',
        controllerAs: 'vm',
        authenticate: true,
        data: {
          title: 'Profile'
        }
      })
      .state('home.table', {
        url: '/table',
        controller: 'TableCtrl',
        controllerAs: 'vm',
        templateUrl: 'app/views/table.html',
        authenticate: true,
        data: {
          title: 'Table'
        }
      })
      .state('login', {
        url: '/login',
        controller: 'LoginCtrl',
        controllerAs: 'vm',
        templateUrl: 'app/views/login.html',
        authenticate: false,
        data: {
          title: 'Login'
        }
      })
      .state('signup', {
        url: '/signup',
        controller: 'SignupCtrl',
        controllerAs: 'vm',
        templateUrl: 'app/views/signup.html',
        authenticate: false,
        data: {
          title: 'Signup'
        }
      });

    $urlRouterProvider.otherwise('/login');

    $mdThemingProvider
      .theme('default')
        .primaryPalette('grey', {
          'default': '600'
        })
        .accentPalette('teal', {
          'default': '500'
        })
        .warnPalette('defaultPrimary');

    $mdThemingProvider.theme('dark', 'default')
      .primaryPalette('defaultPrimary')
      .dark();

    $mdThemingProvider.theme('grey', 'default')
      .primaryPalette('grey');

    $mdThemingProvider.theme('custom', 'default')
      .primaryPalette('defaultPrimary', {
        'hue-1': '50'
    });

    $mdThemingProvider.definePalette('defaultPrimary', {
      '50':  '#FFFFFF',
      '100': 'rgb(255, 198, 197)',
      '200': '#E75753',
      '300': '#E75753',
      '400': '#E75753',
      '500': '#E75753',
      '600': '#E75753',
      '700': '#E75753',
      '800': '#E75753',
      '900': '#E75753',
      'A100': '#E75753',
      'A200': '#E75753',
      'A400': '#E75753',
      'A700': '#E75753'
    });

    $mdIconProvider.icon('user', 'assets/images/user.svg', 64);
  })


.run(function ($rootScope, $state, UserService, ToastService) {
  $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams){
    if (toState.authenticate && !UserService.loggedIn()) {
      // User isn’t authenticated
      $state.transitionTo('login');
      event.preventDefault();
    } else if (toState.name === 'home.admin' && UserService.getAuthLevel() !== '0') {
      ToastService.showToast('Sorry you don\'t have admin priviledges');
      if (fromState.name === '') {
        $state.transitionTo('home.dashboard');
      } else {
        $state.transitionTo(fromState.name);
      }
      event.preventDefault();
    }
  });
});
