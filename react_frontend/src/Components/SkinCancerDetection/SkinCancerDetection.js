import React, { Component } from "react";
import axiosInstance from "../../axios";
import FInalResult from "./FInalResult";
import { Header } from "../Header/Header";
import "./skin.css";

class SkinCancerDetection extends Component {
  constructor(props) {
    super(props);

    this.state = {
      image: null,
      title: "",
      isResult: false,
      comment: "",
    };
  }

  handleInputChange = async (event) => {
    // event.preventDefault();
    await this.setState({
      [event.target.name]: event.target.files[0],
      //image: event.target.files[0]
      // image: event.target.files[0]
    });
  };

  handleChange = async (event) => {
    // event.preventDefault();
    await this.setState({
      [event.target.name]: event.target.value,

      //image: event.target.files[0]
      // image: event.target.files[0]
    });
  };

  handleFormSubmit = (event) => {
    event.preventDefault();

    let data = new FormData(); // creates a new FormData object

    data.append("image", this.state.image); // add your file to form data
    // data.append("title", this.state.title);

    axiosInstance
      .post("/skincancer", data)
      .then((res) => {
        console.log(res.data.comment);
        this.setState({ isResult: true });
        this.setState({ comment: res.data.comment });
      })
      .catch((err) => {
        alert("You must login to access this service");
        window.location = "/login";
      });
  };

  render() {
    return (
      <div>
        <Header></Header>
        <div className="mainDiv">
          <div id="other" className="skinMain" style={{}}>
            <h3 className="mod" style={{ marginTop: "5px" }}>
              Upload Tumor Image For Detecting Skin Cancer
            </h3>

            <form
              onSubmit={this.handleFormSubmit}
              style={{ marginTop: "60px" }}
            >
              <div style={{ marginBottom: "10px" }}>
                <input type="text" name="title" onChange={this.handleChange} />
                <input
                  type="file"
                  name="image"
                  onChange={this.handleInputChange}
                />
              </div>
              <button className="btn btn-primary">Submit</button>
            </form>
            {this.state.isResult ? (
              <FInalResult comment={this.state.comment} />
            ) : null}
          </div>
        </div>
      </div>
    );
  }
}

export default SkinCancerDetection;
