/* eslint-disable no-shadow */
import React from 'react';
import Grid from '@material-ui/core/Grid';
import { connect } from 'react-redux';
import * as Yup from 'yup';
import { Formik } from 'formik';
import { Redirect } from 'react-router-dom';
import SnackbarComponent from '../components/ToastComponent';
import {
  verifyCredentials,
  authSuccess,
  addNewUser
} from '../actions/userActions';

import Appbar from '../components/Appbar';
import BassaIntroBox from '../components/BassaIntroBox';
import UserSignup from '../components/UserSignup';

const validationSchema = Yup.object({
  user_name: Yup.string('Enter a name').required('Name is required'),
  email: Yup.string('Enter your email')
    .email('Enter a valid email')
    .required('Email is required'),
  password: Yup.string('')
    .min(8, 'Password must contain atleast 8 characters')
    .required('Enter your password'),
  confirmPassword: Yup.string('Enter your password')
    .required('Confirm your password')
    .oneOf([Yup.ref('password')], 'Password does not match')
});

const LoginComponent = props => {
  const handleClickSubmit = details => {
    JSON.stringify(details);
    props.addNewUser(details);
  };

  const handleClickLogin = (username, pass) => {
    const usercreds = { username: '', password: '' };
    usercreds.username = username;
    usercreds.password = pass;
    props.verifyCredentials(usercreds);
  };

  const values = {
    user_name: '',
    email: '',
    password: '',
    confirmPassword: ''
  };
  const {
    isloggedIn,
    hasAuthFailed,
    errorMessage,
    hasSignupFailed,
    hasSignupSuccessful
  } = props;

  // eslint-disable-next-line consistent-return
  const renderSnackbar = () => {
    if (hasAuthFailed) {
      const msg = errorMessage.message;
      const displayMsg = msg.concat(
        ". Check the browser's console for more details.",
        ''
      );
      return (
        <SnackbarComponent
          didEventOccured={hasAuthFailed}
          variant="error"
          message={displayMsg}
        />
      );
    }
    if (hasSignupFailed) {
      const msg = errorMessage.message;
      const displayMsg = msg.concat(
        ". Check the browser's console for more details.",
        ''
      );
      return (
        <SnackbarComponent
          variant="error"
          didEventOccured={hasSignupFailed}
          message={displayMsg}
        />
      );
    }
    if (hasSignupSuccessful) {
      return (
        <SnackbarComponent
          variant="success"
          didEventOccured={hasSignupSuccessful}
          message="Account successfully created! Kindly wait for the Admin's approval"
        />
      );
    }
  };
  if (!isloggedIn) {
    return (
      <div>
        <Appbar
          isloggedIn={false}
          data-test="component-appbar"
          onClickLogin={handleClickLogin}
        />
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <BassaIntroBox />
          </Grid>
          <Grid item xs={6} style={{ marginTop: 40 }}>
            <Formik
              render={props => (
                <UserSignup
                  hasSignupFailed={hasSignupFailed}
                  errorMessage={errorMessage}
                  {...props}
                />
              )}
              initialValues={values}
              validationSchema={validationSchema}
              onSubmit={values => handleClickSubmit(values)}
            />
          </Grid>
        </Grid>
        {renderSnackbar()}
      </div>
    );
  }
  return <Redirect to="/home" />;
};

const mapStateToProps = state => ({
  isloggedIn: state.userReducer.isloggedIn,
  hasAuthFailed: state.userReducer.hasAuthFailed,
  hasSignupFailed: state.userReducer.hasSignupFailed,
  hasSignupSuccessful: state.userReducer.hasSignupSuccessful,
  errorMessage: state.userReducer.errorMessage,
  username: state.userReducer.username,
  details: state.userReducer.details
});

const mapDispatchToProps = dispatch => ({
  verifyCredentials: creds => dispatch(verifyCredentials(creds)),
  authSuccess: username => dispatch(authSuccess(username)),
  addNewUser: details => dispatch(addNewUser(details))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginComponent);
