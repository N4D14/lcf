'use strict';

angular.module('commonApp')
    .directive('header', function () {
        return {
            restrict: 'A', //This menas that it will be used as an attribute and NOT as an element.
            replace: true,
            scope: {user: '='}, 
            templateUrl: '/static/js/views/common/header.html',
            controller: ['$scope', '$filter', function ($scope, $filter) {
                // Your behaviour goes here :)
            }]
        }
    });

