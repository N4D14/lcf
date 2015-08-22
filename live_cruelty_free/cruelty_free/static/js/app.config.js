'use strict';

angular.module('mainApp').config(['$stateProvider', '$urlRouterProvider', 'RestangularProvider',
  function($stateProvider, $urlRouterProvider, RestangularProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('search', {
            url: '/',
            templateUrl: 'static/js/views/search/index.html',
            module:      'searchApp',
            controller:  'searchController'
        });

    RestangularProvider.setBaseUrl('/api/cf');
    RestangularProvider.setResponseExtractor(function(response, operation, what, url) {
        var newResponse;
        if (operation === "getList") {
            newResponse = response.objects;
            newResponse.metadata = response.meta;
        } else {
            newResponse = response;
        }
        return newResponse;
    });
    RestangularProvider.setRequestSuffix('/?format=json');
}]);
