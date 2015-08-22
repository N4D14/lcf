'use strict';

/* Search Controller */
angular.module('searchApp').controller('searchController', ['$scope', 'Company',
  function($scope, Company) {

    // TODO: only fill as they type and filter by letters
    // must be at least one letter to start a request
    $scope.companies = Company.all();

  }]);
