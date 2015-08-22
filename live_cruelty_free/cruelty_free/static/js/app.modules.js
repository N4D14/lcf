'use strict';

/* App Modules */

angular.module('searchApp', []);
angular.module('searchFactory', []);

angular.module('mainApp', [
  'ui.router',
  'restangular',
  'searchApp',
  'searchFactory'
]);
