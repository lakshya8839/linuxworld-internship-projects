import React from 'react';
import Lottie from 'lottie-react';
import dancingBug from './components/DancingBug.json';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Lottie
          animationData={dancingBug}
          loop
          autoplay
          style={{ height: 300, width: 300 }}
        />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
