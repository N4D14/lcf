'use strict';

/* Search Controller */
angular.module('loginApp').controller('loginController', ['$scope', 'Auth',
  function($scope, Auth) {

    console.log('Here in login controller!');

    $scope.submit = function() {
        var result = Auth.login($scope.login);
        result.then(function() {
            console.log('User logged in!');
        });
    };

  }]);
