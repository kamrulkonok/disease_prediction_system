import React, { useState } from "react";
import DonutChart from "react-donut-chart";
import { MDBInput } from "mdbreact";
import axios from "axios";
import "./Diabetes.css";
import { Header } from "../Header/Header";
import axiosInstance from "../../axios";

const DiabetesDetection = () => {
  const [symptoms, setsymptoms] = useState({
    age: "",
    pregnancies: "",
    glucose: "",
    bloodpressure: "",
    skinthickness: "",
    bmi: "",
    insulin: "",
  });

  const [result, setResult] = useState({
    score: null,
    comment: null,
    showResult: false,
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    axiosInstance
      .post("/diabetes", {
        age: symptoms.age,
        pregnancies: symptoms.pregnancies,
        glucose: symptoms.glucose,
        bloodpressure: symptoms.bloodpressure,
        skinthickness: symptoms.skinthickness,
        bmi: symptoms.bmi,
        insulin: symptoms.insulin,
      })
      .then(function (response) {
        setResult({
          score: response.data.score,
          comment: response.data.comment,
          showResult: true,
        });
      })
      .catch((err) => {
        alert("You must login to access this service");
        window.location = "/login";
      });
  };

  const FinalResult = (props) => {
    const { score, comment } = props.result;

    return (
      <div className="chart-main">
        <p>{comment}</p>
        <DonutChart
          emptyColor="#98FB98"
          emptyOffset={0.2}
          data={[
            {
              label: "Danger Zone",
              value: parseFloat(score),
              color: ["red"],
            },
            {
              label: "Safe Zone",
              value: 100 - score,
              isEmpty: true,
            },
          ]}
        />
      </div>
    );
  };

  const handleChange = (e) => {
    const newSymptoms = { ...symptoms };
    newSymptoms[e.target.id] = e.target.value;
    setsymptoms(newSymptoms);
  };

  return (
    <div className="diabetes">
      <Header></Header>
      <form onSubmit={handleSubmit} className="form">
        <div className="input-group">
          <MDBInput
            className="form-input"
            label="Age"
            onChange={(e) => handleChange(e)}
            value={symptoms.age}
            name="age"
            id="age"
          />
          <MDBInput
            className="form-input"
            label="Pregnancies"
            onChange={(e) => handleChange(e)}
            value={symptoms.sex}
            name="pregnancies"
            id="pregnancies"
          />
          <MDBInput
            className="form-input"
            label="Glucose Level"
            onChange={(e) => handleChange(e)}
            value={symptoms.cp}
            name="glucose"
            id="glucose"
          />
          <MDBInput
            className="form-input"
            label="Blood Pressure"
            onChange={(e) => handleChange(e)}
            value={symptoms.trestbps}
            name="bloodpressure"
            id="bloodpressure"
          />
          <MDBInput
            className="form-input"
            label="Skin Thickness"
            onChange={(e) => handleChange(e)}
            value={symptoms.chol}
            name="skinthickness"
            id="skinthickness"
          />
          <MDBInput
            className="form-input"
            label="BMI"
            onChange={(e) => handleChange(e)}
            value={symptoms.fbs}
            name="bmi"
            id="bmi"
          />
          <MDBInput
            className="form-input"
            label="Insulin"
            onChange={(e) => handleChange(e)}
            value={symptoms.restecg}
            name="insulin"
            id="insulin"
          />
        </div>
        <div className="submit-btn">
          <button className="btn btn-primary">Submit</button>
        </div>
        {result.showResult ? <FinalResult result={result} /> : null}
      </form>
    </div>
  );
};

export default DiabetesDetection;
