'use strict';

/* Search Controller */
angular.module('searchFactory')
    .factory('Company', ['Restangular', function(Restangular){
        var service = {};

        service.all = function(params) {
            params = params || {}
            params.format = 'json'
            return Restangular.all('company').getList(params);
        };

        return service;
    }]);