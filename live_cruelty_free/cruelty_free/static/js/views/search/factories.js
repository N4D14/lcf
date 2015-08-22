'use strict';

/* Search Controller */
angular.module('searchFactory')
    .factory('Company', ['Restangular', function(Restangular){
        var service = {};

        service.all = function() {
            return Restangular.all('company').getList().$object;
        };

        return service;
    }]);