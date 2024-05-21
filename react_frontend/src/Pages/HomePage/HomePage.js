import React from "react";
import MainBody from "../../Components/MenuItems/MainBody/MainBody";
import "./HomePage.scss";
import Footer from "../../Components/Footer/Footer";
import { Header } from "../../Components/Header/Header";
import { Route, Router, Switch } from "react-router";

const HomePage = () => {
  return (
    <div className="homepage">
      <Header></Header>
      <MainBody></MainBody>
    </div>
  );
};

export default HomePage;
