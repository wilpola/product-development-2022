import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Navigation, Home } from "./components";

import "./App.scss";

function App() {
  return (
    <Router>
      <Navigation />
      <div className='App'>
        <Routes>
          <Route exact path='/' element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
