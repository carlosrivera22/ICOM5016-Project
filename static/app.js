var app = angular.module('DisasterApp',[]);


app.controller('RoutesController', function($scope){


	//array of buttons without parameters
	$scope.buttons = [
		{
			route:'/',
			name:'Greeting'
		},
		{
			route:'',
			name:'Available Resources',
		},
		{
			route: '',
			name: 'Requested Resources',
		},


	]


})