'use strict';

angular.module('searchFactory', []);

angular.module('searchApp', [
    'ui.router',
    'restangular',
    'ui.bootstrap.typeahead',
    'commonApp',
    'searchFactory',
    'template/typeahead/typeahead-popup.html',
    'template/typeahead/typeahead-match.html']);

angular.module('searchApp').config(['$stateProvider', '$urlRouterProvider', 'RestangularProvider',
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
    RestangularProvider.setDefaultHeaders({'X-Requested-With': 'XMLHttpRequest'});
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
}]);
