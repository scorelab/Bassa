import React from 'react';
import Grid from '@material-ui/core/Grid';
import { connect } from 'react-redux';
import {verifyCredentials, authSuccess, addNewUser} from '../actions/userActions';

import Appbar from '../components/Appbar';
import BassaIntroBox from '../components/BassaIntroBox';
import UserSignup from '../components/UserSignup';
import { Redirect } from 'react-router-dom';

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

  if (!props.isloggedIn) {
    return (
      <div>
        <Appbar isloggedIn={false} data-test="component-appbar" onClickLogin={handleClickLogin} />
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <BassaIntroBox/>
          </Grid>
          <Grid item xs={6} style={{marginTop:40}}><UserSignup onClickSubmit={(e) => handleClickSubmit(e)}/></Grid>
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