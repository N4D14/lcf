'use strict';

angular.module('authFactory', []);

angular.module('loginApp', [
    'ui.router',
    'restangular',
    'commonApp',
    'authFactory',
    'ng.django.forms']);


angular.module('loginApp').config(['$stateProvider', '$urlRouterProvider', 'RestangularProvider',
  function($stateProvider, $urlRouterProvider, RestangularProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('login', {
            url: '/',
            templateUrl: '/static/js/views/auth/login.html',
            module:      'loginApp',
            controller:  'loginController'
        });

    RestangularProvider.setDefaultHeaders({'X-Requested-With': 'XMLHttpRequest'});
}]);
