import React from 'react';
import DoctorSignUp from '../../Components/DoctorSignUp/DoctorSignUp';
import PatientSignUp from '../../Components/PatientSignUp/PatientSignUp';
import './SignUp.css';

const SignUpPage = () => {
    return (
        <div className='sign-up-page'>
            <DoctorSignUp></DoctorSignUp>
            <PatientSignUp></PatientSignUp>
        </div>
    );
};

export default SignUpPage;