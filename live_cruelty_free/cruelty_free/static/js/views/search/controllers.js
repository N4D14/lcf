'use strict';

/* Search Controller */
angular.module('searchApp').controller('searchController', ['$scope', 'Company',
  function($scope, Company) {

    $scope.getCompanies = function(search_text) {
        var companies = Company.all({limit: 10, name__icontains: search_text});
        return companies.then(function(companies) {
            return companies.map(function(item){
                return item.name;
            });
        });
    };

  }]);
