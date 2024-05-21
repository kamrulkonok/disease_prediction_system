import React, { useState } from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import axiosInstance from "../../axios";
import { useHistory } from "react-router";

const DoctorSignUp = () => {
  const history = useHistory();

  const useStyles = makeStyles((theme) => ({
    paper: {
      marginTop: theme.spacing(8),
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
    },
    avatar: {
      margin: theme.spacing(1),
      backgroundColor: theme.palette.primary.main,
    },
    form: {
      width: "100%", // Fix IE 11 issue.
      marginTop: theme.spacing(1),
    },
    submit: {
      margin: theme.spacing(3, 0, 2),
    },
  }));

  const classes = useStyles();

  const [doctorData, setDoctorData] = useState({
    email: "",
    user_name: "",
    first_name: "",
    password: "",
    dob: "",
    registration_no: "",
    year_of_registration: "",
    qualification: "",
    State_Medical_Council: "",
    specialization: "",
  });

  const handleChange = (e) => {
    const newData = { ...doctorData };
    newData[e.target.id] = e.target.value;
    setDoctorData(newData);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const data = {
      user: {
        email: doctorData.email,
        user_name: doctorData.user_name,
        first_name: doctorData.first_name,
        password: doctorData.password,
      },
      dob: doctorData.dob,
      registration_no: doctorData.registration_no,
      year_of_registration: doctorData.year_of_registration,
      qualification: doctorData.qualification,
      State_Medical_Council: doctorData.State_Medical_Council,
      specialization: doctorData.specialization,
    };

    axiosInstance
      .post("/user/create-doc/", JSON.stringify(data))
      .then((res) => {
        alert("User is created successfully! Click OK to login");
        window.location = "/login";
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}></Avatar>
        <Typography component="h1" variant="h5">
          Sign Up As A Doctor
        </Typography>
        <form className={classes.form} noValidate onSubmit={handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="first_name"
            label="Name"
            name="first_name"
            autoComplete="name"
            autoFocus
            value={doctorData.first_name}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="user_name"
            label="User Name"
            id="user_name"
            autoComplete="user_name"
            value={doctorData.user_name}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="email"
            label="Email"
            type="email"
            id="email"
            autoComplete="email"
            value={doctorData.email}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="password"
            value={doctorData.password}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="dob"
            label="Date Of Birth(YY-MM-DD)"
            id="dob"
            autoComplete="dob"
            value={doctorData.dob}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="registration_no"
            label="Registration Number"
            id="registration_no"
            autoComplete="registration_no"
            value={doctorData.registration_no}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="year_of_registration"
            label="Year of Registration(YY-MM-DD)"
            id="year_of_registration"
            autoComplete="year_of_registration"
            value={doctorData.year_of_registration}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="qualification"
            label="Qualification"
            id="qualification"
            autoComplete="qualification"
            value={doctorData.qualification}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="State_Medical_Council"
            label="State Medical Council"
            id="State_Medical_Council"
            autoComplete="State_Medical_Council"
            value={doctorData.State_Medical_Council}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="specialization"
            label="specialization"
            id="specialization"
            autoComplete="specialization"
            value={doctorData.specialization}
            onChange={(e) => handleChange(e)}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Sign Up
          </Button>
          <Grid container>
            <Grid item>
              <Link href="/login" variant="body2">
                {"Already have an account? LogIn Here"}
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
    </Container>
  );
};

export default DoctorSignUp;
