var app = angular.module('JabApp', ['ngMaterial','ngRoute']);

app.config(function($routeProvider) {
  $routeProvider

      .when("/", {
    templateUrl : "/templates/demo.html"
  })
  .when("/alternative", {
    templateUrl : "templates/alternative.html"
  })
  .when("/solution", {
    templateUrl : "templates/solution.html"
  })
  .when("/cost", {
    templateUrl : "templates/cost.html"
  })
  .when("/about", {
    templateUrl : "/templates/about.html"
  })
  .when("/demo", {
    templateUrl : "/templates/demo.html"
  });
});



app.controller('AppCtrl', ['$scope','$http', '$mdSidenav','$log','$window', function($scope,$http, $mdSidenav,$log,$window,$httpParamSerializerProvider){
  $scope.toggleSidenav = function(menuId) {
    $mdSidenav(menuId).toggle();
  };
  $scope.menu=[
      {
        link:'/about',
          title:'about'
      },
      {
        link:'/demo',
          title:'demo'
      },
      {
        link:'/alternative',
          title:'about'
      },
      {
        link:'/cost',
          title:'cost'
      },
      {
        link:'/solution',
          title:'about'
      }

  ]
  $scope.query = function(searchText) {
    var main_search='?q={"filters":[{"name":"name","op":"like","val":"'+searchText+'%"}],"limit":10}';
      return $http
      .get("/api/product"+main_search)
      .then(function(data) {
        // Map the response object to the data object.
        return data.data.objects;
      });

  };
  $scope.selectedItemChange = function(item) {
		$log.info(item.url);
  $window.location =item.url;
	};
}]);

