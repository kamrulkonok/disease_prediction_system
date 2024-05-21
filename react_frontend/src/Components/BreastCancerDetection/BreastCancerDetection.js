import React, { useState } from "react";
import { MDBInput } from "mdbreact";
import { Header } from "../Header/Header";
import axiosInstance from "../../axios";
import "./BreastCancerDetection.css";
import DonutChart from "react-donut-chart";

const BreastCancerDetection = () => {
  const [symptoms, setsymptoms] = useState({
    radius_mean: "",
    texture_mean: "",
    perimeter_mean: "",
    area_mean: "",
    smoothness_mean: "",
    compactness_mean: "",
    concavity_mean: "",
    concave_points_mean: "",
    symmetry_mean: "",
    fractal_dimension_mean: "",
    radius_se: "",
    texture_se: "",
    perimeter_se: "",
    area_se: "",
    smoothness_se: "",
    compactness_se: "",
    concavity_se: "",
    concave_points_se: "",
    symmetry_se: "",
    fractal_dimension_se: "",
    radius_worst: "",
    texture_worst: "",
    perimeter_worst: "",
    area_worst: "",
    smoothness_worst: "",
    compactness_worst: "",
    concavity_worst: "",
    concave_points_worst: "",
    symmetry_worst: "",
    fractal_dimension_worst: "",
  });

  const [result, setResult] = useState({
    score: null,
    comment: null,
    showResult: false,
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    axiosInstance
      .post("/breastcancer", {
        radius_mean: symptoms.radius_mean,
        texture_mean: symptoms.texture_mean,
        perimeter_mean: symptoms.perimeter_mean,
        area_mean: symptoms.area_mean,
        smoothness_mean: symptoms.smoothness_mean,
        compactness_mean: symptoms.compactness_mean,
        concavity_mean: symptoms.concavity_mean,
        concave_points_mean: symptoms.symmetry_mean,
        symmetry_mean: symptoms.symmetry_mean,
        fractal_dimension_mean: symptoms.fractal_dimension_mean,
        radius_se: symptoms.radius_se,
        texture_se: symptoms.texture_se,
        perimeter_se: symptoms.perimeter_se,
        area_se: symptoms.area_se,
        smoothness_se: symptoms.smoothness_se,
        compactness_se: symptoms.compactness_se,
        concavity_se: symptoms.concavity_se,
        concave_points_se: symptoms.concave_points_se,
        symmetry_se: symptoms.symmetry_se,
        fractal_dimension_se: symptoms.fractal_dimension_se,
        radius_worst: symptoms.radius_worst,
        texture_worst: symptoms.texture_worst,
        perimeter_worst: symptoms.perimeter_worst,
        area_worst: symptoms.area_worst,
        smoothness_worst: symptoms.smoothness_worst,
        compactness_worst: symptoms.compactness_worst,
        concavity_worst: symptoms.concavity_worst,
        concave_points_worst: symptoms.concave_points_worst,
        symmetry_worst: symptoms.symmetry_worst,
        fractal_dimension_worst: symptoms.fractal_dimension_worst,
      })
      .then(function (response) {
        console.log(response);
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

  const handleChange = (e) => {
    const newSymptoms = { ...symptoms };
    newSymptoms[e.target.id] = e.target.value;
    setsymptoms(newSymptoms);
    console.log(symptoms);
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
              value: score,
              color: ["red"],
            },
            {
              label: "Chance of not having cancer",
              value: 100 - score,
              isEmpty: true,
            },
          ]}
        />
      </div>
    );
  };

  return (
    <div className="breast-cancer">
      <Header></Header>
      <form onSubmit={handleSubmit} className="forms">
        <div className="input-groups">
          <MDBInput
            label="Radius Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.radius_mean}
            name="radius_mean"
            id="radius_mean"
          />
          <MDBInput
            label="Texture Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.texture_mean}
            name="texture_mean"
            id="texture_mean"
          />
          <MDBInput
            label="Perimeter Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.perimeter_mean}
            name="perimeter_mean"
            id="perimeter_mean"
          />
          <MDBInput
            label="Area Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.area_mean}
            name="area_mean"
            id="area_mean"
          />
          <MDBInput
            label="Smoothness Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.smoothness_mean}
            name="smoothness_mean"
            id="smoothness_mean"
          />
          <MDBInput
            label="Compactness Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.compactness_mean}
            name="compactness_mean"
            id="compactness_mean"
          />
          <MDBInput
            label="Concavity Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.concavity_mean}
            name="concavity_mean"
            id="concavity_mean"
          />
          <MDBInput
            label="Concave Points Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.concave_points_mean}
            name="concave_points_mean"
            id="concave_points_mean"
          />
          <MDBInput
            label="Symmetry Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.symmetry_mean}
            name="symmetry_mean"
            id="symmetry_mean"
          />
          <MDBInput
            label="Fractal Dimension Mean"
            onChange={(e) => handleChange(e)}
            value={symptoms.fractal_dimension_mean}
            name="fractal_dimension_mean"
            id="fractal_dimension_mean"
          />
          <MDBInput
            label="Radius Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.radius_se}
            name="radius_se"
            id="radius_se"
          />
          <MDBInput
            label="Texture Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.texture_se}
            name="texture_se"
            id="texture_se"
          />
          <MDBInput
            label="Perimeter Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.perimeter_se}
            name="perimeter_se"
            id="perimeter_se"
          />
          <MDBInput
            label="Area Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.area_se}
            name="area_se"
            id="area_se"
          />
          <MDBInput
            label="Smoothness Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.smoothness_se}
            name="smoothness_se"
            id="smoothness_se"
          />
          <MDBInput
            label="Compactness Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.compactness_se}
            name="compactness_se"
            id="compactness_se"
          />
          <MDBInput
            label="Concavity Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.concavity_se}
            name="concavity_se"
            id="concavity_se"
          />
          <MDBInput
            label="Concave Points Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.concave_points_se}
            name="concave_points_se"
            id="concave_points_se"
          />
          <MDBInput
            label="Symmetry Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.symmetry_se}
            name="symmetry_se"
            id="symmetry_se"
          />
          <MDBInput
            label="Fractal Dimension Se"
            onChange={(e) => handleChange(e)}
            value={symptoms.fractal_dimension_se}
            name="fractal_dimension_se"
            id="fractal_dimension_se"
          />
          <MDBInput
            label="Radius Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.radius_worst}
            name="radius_worst"
            id="radius_worst"
          />
          <MDBInput
            label="Texture Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.texture_worst}
            name="texture_worst"
            id="texture_worst"
          />
          <MDBInput
            label="Perimeter Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.perimeter_worst}
            name="perimeter_worst"
            id="perimeter_worst"
          />
          <MDBInput
            label="Area Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.area_worst}
            name="area_worst"
            id="area_worst"
          />
          <MDBInput
            label="Smoothness Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.smoothness_worst}
            name="smoothness_worst"
            id="smoothness_worst"
          />
          <MDBInput
            label="Compactness Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.compactness_worst}
            name="compactness_worst"
            id="compactness_worst"
          />
          <MDBInput
            label="Concavity Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.concavity_worst}
            name="concavity_worst"
            id="concavity_worst"
          />
          <MDBInput
            label="Concavity Points Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.concave_points_worst}
            name="concave_points_worst"
            id="concave_points_worst"
          />
          <MDBInput
            label="Symmetry Worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.symmetry_worst}
            name="symmetry_worst"
            id="symmetry_worst"
          />
          <MDBInput
            label="fractal_dimension_worst"
            onChange={(e) => handleChange(e)}
            value={symptoms.fractal_dimension_worst}
            name="fractal_dimension_worst"
            id="fractal_dimension_worst"
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

export default BreastCancerDetection;
