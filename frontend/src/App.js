import React, { useState, useEffect } from 'react';
import './App.css';



function App() {
  const [customers, setCustomers] = useState([]);
  const [customersBatchNum, setCustomersBatchNum] = useState(0);
  const [customersBatchMax, setCustomersBatchMax] = useState(0);
  const BATCH_SIZE = 20;
  
  useEffect(() => {
    if(customers.length){ 
      document.getElementById("nextCustomerBatch").disabled = (customersBatchMax==customersBatchNum);
      document.getElementById("prevCustomerBatch").disabled = (customersBatchNum==0);
    }
  }, [customersBatchNum, customersBatchMax])

  function alertMe() {
    alert("eitan")
  }


  function fetchPrevBatch(){
    setCustomersBatchNum(customersBatchNum-1);
    fetchCustomers();
  }

  function fetchNextBatch(){
    setCustomersBatchNum(customersBatchNum+1);
    fetchCustomers();
  }

  function fetchCustomers() {
    fetch(`http://127.0.0.1:5000/customers?batchSize=${BATCH_SIZE}&batchNumber=${customersBatchNum}`)
      .then(response => response.json())
      .then(data => {
        var newBatchMax = data["Body"]["Batches"]
        setCustomersBatchMax(newBatchMax)
        console.log(customersBatchNum)
        setCustomers(data["Body"]["Data"])});
        console.log(customers)
  }


  return (
    <div className="App">
      <header className="App-header">
        <p>View all customers</p>
        {customers.map(customer => <li onClick={() => alertMe()} key={customer["id"]}>{customer["First Name"] +  " " + customer["Last Name"]}</li>)}
        {!customers.length && <button onClick={() => fetchCustomers()}>Show {BATCH_SIZE} Customers</button>}
        {customers.length && <div>
          <p>{customersBatchNum} / {customersBatchMax}</p>
          <button id="nextCustomerBatch" onClick={() => fetchNextBatch()}>Next Customers</button>
          <button id="prevCustomerBatch" onClick={() => fetchPrevBatch()}>Previous Customers</button>
        </div>    
        }
      </header>
    </div>
  );
}

export default App;
