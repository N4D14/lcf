'use strict';

/* Search Controller */
angular.module('searchApp').controller('searchController', ['$scope', 'Company',
  function($scope, Company) {

    // Init (TODO: create method)
    $scope.foundResult = false;

    $scope.getCompanies = function(search_text) {
        $scope.foundResult = false;
        var result = Company.all({limit: 10, name__icontains: search_text});
        return result.then(function(companies) {
            if (companies.length != 0) {
                $scope.foundResult = false;
            };
            return companies;
        });
    };

    $scope.companySelected = function(item, model, label) {
        $scope.selectedCompany = item;
        $scope.canClearResult = false;
        $scope.selectedName = null;
        $scope.foundResult = true;
    };

    $scope.runSearch = function() {
        var result = Company.all({limit: 1, name__iexact: $scope.selectedName});
        result.then(function(companies) {
            $scope.selectedCompany = null;
            if (companies.length == 1) {
                $scope.selectedCompany = companies[0];
            };
            $scope.foundResult = true;
        });        
    };

    $scope.inputKeyPressed = function(key_event) {
        console.log($scope.selectedName);
        console.log(key_event);
        if ($scope.selectedName && key_event.keyCode === 13) {
            $scope.runSearch();
        }
    };

    $scope.canClearResult = true;
    $scope.$watch('selectedName', function(newValue, oldValue){
        if ($scope.canClearResult && !newValue && oldValue) {
            $scope.foundResult = false;            
        }
        $scope.canClearResult = true;
    });

  }]);
