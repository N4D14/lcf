'use strict';

angular.module('mainApp')
    .directive('header', function () {
        return {
            restrict: 'A', //This menas that it will be used as an attribute and NOT as an element.
            replace: true,
            scope: {user: '='}, 
            templateUrl: 'static/js/views/main/header.html',
            controller: ['$scope', '$filter', function ($scope, $filter) {
                // Your behaviour goes here :)
            }]
        }
    });

