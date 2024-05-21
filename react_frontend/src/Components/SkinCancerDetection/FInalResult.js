import React from "react";
import DonutChart from "react-donut-chart";
import "./FinalResult.css";
import "./finalResult.scss";

const FInalResult = (props) => {
  return (
    <div className="result">
      <div class="card">
        <h1 class="entry-title">
          <p>{props.comment}</p>
        </h1>
      </div>
    </div>
  );
};

export default FInalResult;
