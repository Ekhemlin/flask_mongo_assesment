# API Endpoints doc 

##  /customers 
Method: GET
Mandatory args: N/A 
Optional args: batchSize, batchNumber 
batchSize: how many customers are returned with each request
batchNumber: which batch is returned from the overall list of customers 
Return codes: 200 (Success), 500 (Internal error) 
 

##  /customer 
Method: GET
Mandatory args: id
id: Id for customer 
Optional args: N/A
Return codes: 200 (Success), 404(Customer not found), 500 (Internal error) 


##  /films 
Method: GET
Mandatory args: N/A 
Optional args: batchSize, batchNumber 
batchSize: how many films are returned with each request
batchNumber: which batch is returned from the overall list of films 
Return codes: 200 (Success), 500 (Internal error) 
 

##  /film 
Method: GET
Mandatory args: id
id: Id for film 
Optional args: N/A
Return codes: 200 (Success), 404(Film not found), 500 (Internal error) 
