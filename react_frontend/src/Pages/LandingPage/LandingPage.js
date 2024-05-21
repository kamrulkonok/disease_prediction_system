import React from "react";
import "./LandingPage.css";
import bg from "./bg.jpg";

const LandingPage = () => {
  return (
    <div>
      <div>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta
          name="description"
          content="A layout example that shows off a responsive product landing page."
        />
        <link rel="stylesheet" href="/css/pure/pure-min.css" />
        <link rel="stylesheet" href="/css/pure/grids-responsive-min.css" />
        <link
          rel="stylesheet"
          href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css"
        />
        <link rel="stylesheet" href="/layouts/marketing/styles.css" />
        <div className="header">
          <div className="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
            {/* <a className="pure-menu-heading" href>
              Your Site
            </a> */}
            <ul className="pure-menu-list">
              <li className="pure-menu-item pure-menu-selected">
                <a href="#" className="pure-menu-link">
                  Home
                </a>
              </li>
              <li className="pure-menu-item">
                <a href="/login" className="pure-menu-link">
                  LogIn
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div
          className="splash-container bg-image"
          style={{ backgroundImage: `url(${bg})` }}
        >
          <div className="splash">
            <h1 className="splash-head">AI Based Disease Prediction System</h1>
            <p>
              <a href="/signup" className="pure-button pure-button-primary">
                Get Started
              </a>
            </p>
          </div>
        </div>
        {/*  */}
      </div>
    </div>
  );
};

export default LandingPage;
