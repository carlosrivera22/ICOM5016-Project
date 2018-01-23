app.service('disasterService', function($http){
	this.getData = function(){
        return $http.get('/DisasterApp/allResources').then(function(response){
            //angular.copy(response.data.Resources,resource_list);
            return response.data;
		})

	}

    this.getCreditCards = function(){
        return $http.get('/DisasterApp/creditcards').then(function(response){
            console.log(response.data)
            return response.data;
        })
    }

    this.sendCreditCardData = function(card_data,callback){

        $http.put('/DisasterApp/updatecreditcard', card_data).then(function(response){
            console.log(response.data)
            alert(JSON.stringify(response.data))
        })
    }

    this.sendResourceData = function(resource_data,callback){
        $http.post('/DisasterApp/seeResourceTransaction', resource_data).then(function(response){
            console.log(response.data)
            return response.data
        })
    }
	//get credit cards and use this information to show the fields
	//send back that data and update it in the database.

	//get


});