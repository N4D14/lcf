'use strict';

/* Authorization Service */
angular.module('authFactory')
    .factory('Auth', ['Restangular', function(Restangular){
        var service = {};

        service.login = function(form_data) {
            return Restangular.all('/login').post(form_data);
        };

        return service;
    }]);