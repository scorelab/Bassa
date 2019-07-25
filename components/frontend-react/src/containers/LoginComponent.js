import React from 'react';
import Grid from '@material-ui/core/Grid';
import { connect } from 'react-redux';
import {verifyCredentials, authSuccess, addNewUser} from '../actions/userActions';
import * as Yup from 'yup';
import { Formik } from 'formik';

import Appbar from '../components/Appbar';
import BassaIntroBox from '../components/BassaIntroBox';
import UserSignup from '../components/UserSignup';
import { Redirect } from 'react-router-dom';

const validationSchema = Yup.object({
  user_name: Yup.string("Enter a name").required("Name is required"),
  email: Yup.string("Enter your email")
    .email("Enter a valid email")
    .required("Email is required"),
  password: Yup.string("")
    .min(8, "Password must contain atleast 8 characters")
    .required("Enter your password"),
  confirm_password: Yup.string("Enter your password")
    .required("Confirm your password")
    .oneOf([Yup.ref("password")], "Password does not match")
});

const LoginComponent = (props) => {

  const handleClickSubmit = (details) => {
    JSON.stringify(details);
    props.addNewUser(details);
  }

  const handleClickLogin = (username, pass) => {
    let usercreds = {username:'', password: ''};
    usercreds.username = username;
    usercreds.password = pass;
    props.verifyCredentials(usercreds);
  }

  const values = { user_name: "", email: "", password: "", confirm_password: "" };

  if (!props.isloggedIn) {
    return (
      <div>
        <Appbar isloggedIn={false} data-test="component-appbar" onClickLogin={handleClickLogin} />
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <BassaIntroBox/>
          </Grid>
          <Grid item xs={6} style={{marginTop:40}}>
            <Formik
              render={props => <UserSignup {...props} />}
              initialValues={values}
              validationSchema={validationSchema}
              onSubmit={(values) => handleClickSubmit(values)}
            />
          </Grid>
        </Grid>
      </div>
    )
  } else {
    return <Redirect to='/home'/>
  }
}

const mapStateToProps = (state) => ({
  isloggedIn: state.userReducer.isloggedIn,
  username: state.userReducer.username,
  details: state.userReducer.details
});

const mapDispatchToProps = dispatch => ({
  verifyCredentials: creds => dispatch(verifyCredentials(creds)),
  authSuccess: username => dispatch(authSuccess(username)),
  addNewUser: details => dispatch(addNewUser(details))
})

export default connect(mapStateToProps, mapDispatchToProps)(LoginComponent);