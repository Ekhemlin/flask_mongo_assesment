import React, { useState, useEffect } from 'react';
import './App.css';

function Home() {
    const [films, setFilms] = useState([]);
    const [filmBatchNumber, setFilmBatchNumber] = useState(0);
    const [filmBatchMax, setFilmBatchMax] = useState(0);
    const [filmData, setFilmData] = useState({});
    const [filmRenters, setFilmRenters] = useState([]);
    const [isFilmOpen, setIsFilmOpen] = useState(false);


    const BATCH_SIZE = 20;

    useEffect(() => {
        if (films.length) {
            document.getElementById("nextFilmBatch").disabled = (filmBatchMax == filmBatchNumber);
            document.getElementById("prevFilmBatch").disabled = (filmBatchNumber == 0);
        }
    }, [filmBatchNumber, filmBatchMax]);


    function fetchFilmData(id) {
        fetch(`http://127.0.0.1:5000/film?id=${id}`)
            .then(response => response.json())
            .then(data => {
                setFilmData(data["Body"]["info"]);
                setIsFilmOpen(true);
                setFilmRenters(data["Body"]["renters"]);
            })
    };

    function clearFilmData() {
        setFilmData({});
        setIsFilmOpen(false);
    }

    function fetchPrevBatch() {
        setFilmBatchNumber(filmBatchNumber - 1);
        fetchFilms();
    }

    function fetchNextBatch() {
        setFilmBatchNumber(filmBatchNumber + 1);
        fetchFilms();
    }

    function fetchFilms() {
        fetch(`http://127.0.0.1:5000/films?batchSize=${BATCH_SIZE}&batchNumber=${filmBatchNumber}`)
            .then(response => response.json())
            .then(data => {
                var newBatchMax = data["Body"]["Batches"]
                setFilmBatchMax(newBatchMax)
                setFilms(data["Body"]["Data"])
            });
    }


    return (
        <div className="App">
            <header className="App-header">
                {isFilmOpen && <div>
                    <div>
                        <h2>{filmData["Title"]}</h2>
                        <h3>Category: {filmData["Category"]}</h3>
                        <h3>Rating: {filmData["Rating"]}</h3>
                        <p>{filmData["Description"]}</p>
                    </div>
                    {filmRenters.map(renter => <li key={renter["First Name"]}>
                        {`${renter["First Name"]} ${renter["Last Name"]} rented this movie`}
                    </li>)}
                    <button id="clearFilmData" onClick={() => clearFilmData()}>Back to film list</button>
                </div>}
                {!isFilmOpen &&
                    <div>
                        <p>Film directory</p>
                        {films.map(film => <li onClick={() => fetchFilmData(film["id"])} key={film["id"]}>
                            {`${film["Title"]} rated  ${film["Rating"]} with duration of ${film["Rental Duration"]} hours`}
                        </li>)}
                        {!films.length && <button onClick={() => fetchFilms()}>Show {BATCH_SIZE} films</button>}
                        {films.length > 0 && <div>
                            <p>{filmBatchNumber} / {filmBatchMax}</p>
                            <button id="nextFilmBatch" onClick={() => fetchNextBatch()}>Next Films</button>
                            <button id="prevFilmBatch" onClick={() => fetchPrevBatch()}>Previous Films</button>
                        </div>
                        }
                    </div>
                }
            </header>
        </div>
    );
}

export default Home;