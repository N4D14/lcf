'use strict';

/* App Modules */

angular.module('searchApp', ['template/typeahead/typeahead-popup.html',
                             'template/typeahead/typeahead-match.html']);
angular.module('searchFactory', []);

angular.module('mainApp', [
  'ui.router',
  'restangular',
  'ui.bootstrap.typeahead',
  'searchApp',
  'searchFactory'
]);
