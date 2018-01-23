var app = angular.module('DisasterApp',[]);


app.controller('RoutesController', function($scope,$http,disasterService){

	$scope.disaster_service = disasterService;


    $scope.resource_list = $scope.disaster_service.getData()

    $scope.update_card_information = {
        credit_card_id: "",
        field_list: {},
    }

    $scope.show_transaction_information = {
        resource_id: "",
    }

    $scope.sendCreditCardData = function(callback){
        console.log(JSON.stringify($scope.update_card_information))
        $scope.disaster_service.sendCreditCardData(JSON.stringify($scope.update_card_information),callback);
    }


    $scope.sendResourceData = function(callback){
        console.log(JSON.stringify($scope.show_transaction_information))
        $scope.disaster_service.sendResourceData(JSON.stringify($scope.show_transaction_information),callback);
    }

    /*
    $scope.dataReceived = function(data){
        $scope.data_received = data[0]
        console.log($scope.data_received.resource_list)
    }
        */


    $scope.goResourcesData = function(){
        $scope.disaster_service.getData().then(function(data){
            $scope.resource_list = data.Resources
            $scope.resource_id_names = []
            $scope.resource_id_list = []
            for(var i=0;i<$scope.resource_list.length;i++){
                $scope.resource_id_names[i] = "id:" + $scope.resource_list[i]['resource_id'] + " " + $scope.resource_list[i]['resource_name'];
            }
            for(var i=0;i<$scope.resource_list.length;i++){
                $scope.resource_id_list[i] = $scope.resource_list[i]['resource_id'];
            }

         $scope.selects = [
            {
                route:'/',
                name: 'See Transaction',
                resource_list: $scope.resource_id_names
            },
        ]

        $scope.changes = [
        {
            route:'/',
            name:'Change Product Information',
            product_list: $scope.resource_id_list,
        },
    ]
        });
    };


    $scope.goCreditCardData = function(){
        $scope.disaster_service.getCreditCards().then(function(data){
            $scope.credit_card_list = data.CreditCards

            $scope.updates = [
            {
                //quizas pueda ser un select
                route:'/DisasterApp/updatecreditcard',
                name: 'Update Credit Card',
                credit_card_list: $scope.credit_card_list,
            },
		/*
		{
			//puede ser un select
			route:'/',
			name: 'Update Product',
		},
    */
	    ]
        })
    }

    $scope.goCreditCardData()
    $scope.goResourcesData()

	//array of buttons without parameters
	$scope.buttons = [

		{
			route:'/DisasterApp/AvailableResources',
			name:'Available Resources',
		},
		{
			route: '/DisasterApp/RequestedResources',
			name: 'Requested Resources',
		},



	]



	$scope.inputs = [
		{
			route:'/',
			name: 'Register Administrator'
		}
		,
		{
			route:'/',
			name: 'Register Supplier'
		},
		{
			route:'/',
			name: 'Register Victim'
		},
		{
			route:'/',
			name: 'Add Resource'
		},
		{
			route:'/',
			name: 'Add Payment Method'
		},

	]



    $scope.run = function(){
      $scope.sendCreditCardData()
    }

    $scope.seeTransaction = function(){
        $scope.sendResourceData()
    }
})