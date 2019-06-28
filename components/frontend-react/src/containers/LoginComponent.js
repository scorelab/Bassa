import React from 'react';
import Grid from '@material-ui/core/Grid';
import axios from 'axios';

import Appbar from '../components/Appbar';
import BassaIntroBox from '../components/BassaIntroBox';
import UserSignup from '../components/UserSignup';

const APIURL = "http://0.0.0.0:5000/api";

const LoginComponent = () => {

  const handleClickSubmit = () => {
    console.log('Handling button submit click')
  }

  const handleClickLogin = (username, pass) => {
    //making axios POST call
    let formData = new FormData();
    formData.set("user_name", username);
    formData.set("password", pass);
    
    axios({
      method: 'post',
      url: `${APIURL}/login`,
      data: formData
      },
      {
        headers: {'Content-Type': 'multipart/form-data' }
      })
    .then(res => {
      makeGetRequest(res.headers.token);
    })
    .then(err => console.log(err));
  }

  const makeGetRequest = (token) => {
    //Testing a GET request
    axios({
      method: 'get',
      url: `${APIURL}/user`,
      headers: {'token': `${token}`}
      })
    .then(res => console.log(res))
    .then(err => console.log(err));
  }
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
}

export default LoginComponent;