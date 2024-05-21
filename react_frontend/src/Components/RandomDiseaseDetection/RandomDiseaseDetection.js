import React, { useState } from "react";
import Select from "react-select";
import makeAnimated from "react-select/animated";
import { diseaseData } from "../../Data/DiseaseData";
import DonutChart from "react-donut-chart";
import "./RandomDiseaseDetection.css";
import { Header } from "../Header/Header";
import axiosInstance from "../../axios";

const RandomDiseaseDetection = () => {
  const options = diseaseData;

  const animatedComponents = makeAnimated();

  const [symptoms, setsymptoms] = useState([]);

  const [result, setResult] = useState({
    predicteddisease: null,
    confidencescore: null,
    consultdoctor: null,
    showResult: false,
  });

  const handleSubmit = (e) => {
    setResult({ loading: true });
    e.preventDefault();

    axiosInstance
      .post("/checkdisease", JSON.stringify({ symptoms }))
      .then((res) => {
        setResult({
          predicteddisease: res.data.predicteddisease,
          confidencescore: res.data.confidencescore,
          consultdoctor: res.data.consultdoctor,
          showResult: true,
        });
      })
      .catch((err) => {
        alert("You must login to access this service");
        window.location = "/login";
      });
  };

  const handleChange = (symptoms) => {
    let catArray = [];
    symptoms.map((o) => catArray.push(o.value));

    setsymptoms(catArray);
  };

  const FinalResult = (props) => {
    const { predicteddisease, confidencescore, consultdoctor } = props.result;
    console.log(predicteddisease, confidencescore);
    return (
      <div className="main-div">
        <div className="first-part">
          <p>Predicted Disease: {predicteddisease}</p>
          <p>Accuracy Score: {confidencescore}% </p>
          <p>Suggested Doctor: {consultdoctor}</p>
        </div>

        <DonutChart
          emptyColor="green"
          emptyOffset={0.2}
          data={[
            {
              label: predicteddisease,
              value: parseFloat(confidencescore),
            },
            {
              label: "Safe Zone",
              value: 100 - confidencescore,
              isEmpty: true,
            },
          ]}
        />
      </div>
    );
  };

  // const handleOnClick = () => {
  //   setShowResult(true);
  // }
  return (
    <div className="outer">
      <Header></Header>
      <div className="holder">
        <div className="main">
          <form onSubmit={handleSubmit} className="form">
            <Select
              closeMenuOnSelect={false}
              components={animatedComponents}
              isMulti
              options={options}
              onChange={handleChange}
            />

            <button className="btn btn-primary submit-btn">Submit</button>
            {result.showResult ? <FinalResult result={result} /> : null}
            {/* <Link to = '/detection-result'>
                
                </Link> */}
          </form>
        </div>
      </div>
    </div>
  );
};

export default RandomDiseaseDetection;
