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
import { useHistory } from "react-router";
import axiosInstance from "../../axios";

const PatientSignUp = () => {
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
      backgroundColor: theme.palette.secondary.main,
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

  const [patientData, setPatientData] = useState({
    email: "",
    user_name: "",
    first_name: "",
    password: "",
    dob: "",
  });

  const handleChange = (e) => {
    const newData = { ...patientData };
    newData[e.target.id] = e.target.value;
    setPatientData(newData);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const data = {
      user: {
        email: patientData.email,
        user_name: patientData.user_name,
        first_name: patientData.first_name,
        password: patientData.password,
      },
      dob: patientData.dob,
    };

    console.log(data);

    axiosInstance.post("/user/create-patient/", JSON.stringify(data));

    alert("User is created successfully! Click OK to login");
    window.location = "/login";
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}></Avatar>
        <Typography component="h1" variant="h5">
          Sign Up As A Patient
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
            autoComplete="first_name"
            autoFocus
            value={patientData.first_name}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="user_name"
            label="User Name"
            name="user_name"
            autoComplete="user_name"
            autoFocus
            value={patientData.user_name}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
            value={patientData.email}
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
            autoComplete="current-password"
            value={patientData.password}
            onChange={(e) => handleChange(e)}
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="dob"
            name="dob"
            autoComplete="date"
            label="Date of Birth(YY-MM-DD)"
            autoFocus
            value={patientData.dob}
            onChange={(e) => handleChange(e)}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="secondary"
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

export default PatientSignUp;
