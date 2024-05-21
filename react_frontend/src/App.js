import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./App.css";
import RandomDiseaseDetection from "./Components/RandomDiseaseDetection/RandomDiseaseDetection";
import HomePage from "./Pages/HomePage/HomePage";
import HeartDiseaseInput from "./Components/HeartDieseaseInput/HeartDiseaseInput";
import DiabetesDetection from "./Components/DiabetesDetection/DiabetesDetection";
import LogIn from "./Components/LogIn/LogIn";
import SignUpPage from "./Pages/SignUpPage/SignUpPage";
import LandingPage from "./Pages/LandingPage/LandingPage";
import { Header } from "./Components/Header/Header";
import BreastCancerDetection from "./Components/BreastCancerDetection/BreastCancerDetection";
import SkinCancerDetection from "./Components/SkinCancerDetection/SkinCancerDetection";

const App = () => {
  const test = () => {
    localStorage.length === 0 ? (
      alert("You must login to access our services")
    ) : (
      <HomePage></HomePage>
    );
  };

  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/">
            <LandingPage></LandingPage>
          </Route>
          <Route path="/landingpage">
            <LandingPage></LandingPage>
          </Route>
          <Route path="/home">
            <HomePage />
          </Route>
          <Route path="/random-disease-detection">
            <RandomDiseaseDetection></RandomDiseaseDetection>
          </Route>
          <Route path="/heart-disease-detection">
            <HeartDiseaseInput></HeartDiseaseInput>
          </Route>
          <Route path="/diabetes-detection">
            <DiabetesDetection></DiabetesDetection>
          </Route>
          <Route path="/login">
            <LogIn></LogIn>
          </Route>
          <Route path="/signup">
            <SignUpPage></SignUpPage>
          </Route>
          <Route path="/breast-cancer-detection">
            <BreastCancerDetection></BreastCancerDetection>
          </Route>
          <Route path="/skin-cancer-detection">
            <SkinCancerDetection></SkinCancerDetection>
          </Route>
        </Switch>
      </Router>
    </div>
  );
};

export default App;
