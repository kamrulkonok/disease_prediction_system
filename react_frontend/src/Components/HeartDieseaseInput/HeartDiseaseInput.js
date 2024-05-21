import axiosInstance from "../../axios";
import React, { useState } from "react";
import { MDBInput } from "mdbreact";
import "./HeartDiseaseInput.css";
import DonutChart from "react-donut-chart";
import { Header } from "../Header/Header";

const HeartDiseaseInput = () => {
  const [symptoms, setsymptoms] = useState({
    age: null,
    sex: null,
    cp: null,
    trestbps: null,
    chol: null,
    fbs: null,
    restecg: null,
    thalach: null,
    exang: null,
    oldpeak: null,
    slope: null,
    ca: null,
    thal: null,
  });

  const [result, setResult] = useState({
    score: null,
    comment: null,
    showResult: false,
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    axiosInstance
      .post("/heart", {
        age: symptoms.age,
        sex: symptoms.sex,
        cp: symptoms.cp,
        trestbps: symptoms.trestbps,
        chol: symptoms.chol,
        fbs: symptoms.fbs,
        restecg: symptoms.restecg,
        thalach: symptoms.thalach,
        exang: symptoms.exang,
        oldpeak: symptoms.oldpeak,
        slope: symptoms.slope,
        ca: symptoms.ca,
        thal: symptoms.thal,
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
      <div>
        <p>{comment}</p>
        <DonutChart
          emptyColor="#98FB98"
          emptyOffset={0.2}
          data={[
            {
              label: "Score",
              value: parseFloat(score),
              color: ["red"],
            },
            {
              label: "Chance of not having heart disease",
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
    <div className="heart-disease">
      <Header></Header>
      <form onSubmit={handleSubmit} className="form">
        <div className="input-group">
          <MDBInput
            label="Age"
            onChange={(e) => handleChange(e)}
            value={symptoms.age}
            name="age"
            id="age"
          />
          <MDBInput
            label="Sex"
            onChange={(e) => handleChange(e)}
            value={symptoms.sex}
            name="sex"
            id="sex"
          />
          <MDBInput
            label="Cerebral Palsy"
            onChange={(e) => handleChange(e)}
            value={symptoms.cp}
            name="cp"
            id="cp"
          />
          <MDBInput
            label="Resting Blood Pressure(TrestBPS)"
            onChange={(e) => handleChange(e)}
            value={symptoms.trestbps}
            name="trestbps"
            id="trestbps"
          />
          <MDBInput
            label="Cholesterol Level"
            onChange={(e) => handleChange(e)}
            value={symptoms.chol}
            name="chol"
            id="chol"
          />
          <MDBInput
            label="Fasting Blood Sugar(FBS)"
            onChange={(e) => handleChange(e)}
            value={symptoms.fbs}
            name="fbs"
            id="fbs"
          />
          <MDBInput
            label="RESTECG"
            onChange={(e) => handleChange(e)}
            value={symptoms.restecg}
            name="restecg"
            id="restecg"
          />
          <MDBInput
            label="Thalach"
            onChange={(e) => handleChange(e)}
            value={symptoms.thalach}
            name="thalach"
            id="thalach"
          />
          <MDBInput
            label="Exercise Induced Angina(Exang)"
            onChange={(e) => handleChange(e)}
            value={symptoms.exang}
            name="exang"
            id="exang"
          />
          <MDBInput
            label="OldPeak"
            onChange={(e) => handleChange(e)}
            value={symptoms.oldpeak}
            name="oldpeak"
            id="oldpeak"
          />
          <MDBInput
            label="Slope"
            onChange={(e) => handleChange(e)}
            value={symptoms.slope}
            name="slope"
            id="slope"
          />
          <MDBInput
            label="CA"
            onChange={(e) => handleChange(e)}
            value={symptoms.ca}
            name="ca"
            id="ca"
          />
          <MDBInput
            label="Thalassemia"
            onChange={(e) => handleChange(e)}
            value={symptoms.thal}
            name="thal"
            id="thal"
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

export default HeartDiseaseInput;
