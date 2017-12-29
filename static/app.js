var app = angular.module('DisasterApp',[]);


app.controller('RoutesController', function($scope){


	//array of buttons without parameters
	$scope.buttons = [
		{
			route:'/',
			name:'Greeting'
		},
		{
			route:'/DisasterApp/suppliers',
			name:'All Suppliers',
		},
		{
			route: '/DisasterApp/users',
			name: 'All Users',
		},
		{
			route: '/DisasterApp/addresses',
			name: 'All Addresses',
		},
		{
			route: '/DisasterApp/bankAccounts',
			name: 'All Bank Accounts',
		},
		{
			route: '/DisasterApp/categories',
			name: 'All Categories',
		},
		{
			route: '/DisasterApp/subCategories',
			name: 'All Sub-Categories',
		},
		{
			route: '/DisasterApp/creditCards',
			name: 'All Credit Cards',
		},
		{
			route: '/DisasterApp/requestsCompleted',
			name: 'All Requests Completed',
		},
		{
			route: '/DisasterApp/Requests',
			name: 'All Resources',
		},
		{
			route: '/DisasterApp/admins',
			name: 'All Admins',
		},

	]


})