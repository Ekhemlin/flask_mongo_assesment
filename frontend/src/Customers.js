import React, { useState, useEffect } from 'react';
import './App.css';

function Customers() {
    const [customers, setCustomers] = useState([]);
    const [customersBatchNum, setCustomersBatchNum] = useState(0);
    const [customersBatchMax, setCustomersBatchMax] = useState(0);
    const [customerData, setCustomerData] = useState({});
    const [customerRentals, setCustomerRentals] = useState([]);
    const [isCustomerOpen, setIsCustomerOpen] = useState(false);


    const BATCH_SIZE = 20;

    useEffect(() => {
        if (customers.length) {
            document.getElementById("nextCustomerBatch").disabled = (customersBatchMax == customersBatchNum);
            document.getElementById("prevCustomerBatch").disabled = (customersBatchNum == 0);
        }
    }, [customersBatchNum, customersBatchMax]);


    function fetchCustomerData(id) {
        fetch(`http://127.0.0.1:5000/customer?id=${id}`)
            .then(response => response.json())
            .then(data => {
                setCustomerData(data["Body"]["info"]);
                setCustomerRentals(data["Body"]["rentals"]);
                console.log(data["Body"]);
                setIsCustomerOpen(true);
            })
    };

    function clearUserData() {
        setCustomerData({});
        setIsCustomerOpen(false);
        setCustomerRentals([]);
    }

    function fetchPrevBatch() {
        setCustomersBatchNum(customersBatchNum - 1);
        fetchCustomers();
    }

    function fetchNextBatch() {
        setCustomersBatchNum(customersBatchNum + 1);
        fetchCustomers();
    }

    function fetchCustomers() {
        fetch(`http://127.0.0.1:5000/customers?batchSize=${BATCH_SIZE}&batchNumber=${customersBatchNum}`)
            .then(response => response.json())
            .then(data => {
                var newBatchMax = data["Body"]["Batches"]
                setCustomersBatchMax(newBatchMax)
                console.log(customersBatchNum)
                setCustomers(data["Body"]["Data"])
            });
        console.log(customers)
    }


    return (
        <div className="App">
            <header className="App-header">
                {isCustomerOpen && <div>
                    <p>Customer data</p>
                    <p>{JSON.stringify(customerData)}</p>
                    {customerRentals.map(rental => <li key={rental["Film Title"]}>
                        {`${rental["Film Title"]} rented for \$${parseFloat(rental["Cost"]).toFixed(2)} for ${rental["Rented For"]["days"]} days`}
                        </li>)}
                        <button id="clearUserData" onClick={() => clearUserData()}>Back to customer list</button>
                </div>}
                {!isCustomerOpen &&
                    <div>
                        <p>Customers directory</p>
                        {customers.map(customer => <li onClick={() => fetchCustomerData(customer["id"])} key={customer["id"]}>{customer["First Name"] + " " + customer["Last Name"]}</li>)}
                        {!customers.length && <button onClick={() => fetchCustomers()}>Show {BATCH_SIZE} Customers</button>}
                        {customers.length > 0 && <div>
                            <p>{customersBatchNum} / {customersBatchMax}</p>
                            <button id="nextCustomerBatch" onClick={() => fetchNextBatch()}>Next Customers</button>
                            <button id="prevCustomerBatch" onClick={() => fetchPrevBatch()}>Previous Customers</button>
                        </div>
                        }
                    </div>
                }
            </header>
        </div>
    );
}

export default Customers;