import React from 'react';
import Grid from '@material-ui/core/Grid';
import { withRouter } from 'react-router-dom';
import axios from 'axios';

import Appbar from '../components/Appbar';
import BassaIntroBox from '../components/BassaIntroBox';
import UserSignup from '../components/UserSignup';

const LoginComponent = (props) => {

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
      url: `${process.env.REACT_APP_API_URL}/api/login`,
      data: formData
      },
      {
        headers: {'Content-Type': 'multipart/form-data' }
      })
    .then(res => {
      sessionStorage.setItem('token',res.headers.token);
      return props.history.push('/home');
    })
    .catch(err => console.log(err));
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

export default withRouter(LoginComponent);