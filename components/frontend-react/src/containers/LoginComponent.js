import React from 'react';
import Grid from '@material-ui/core/Grid';

import Appbar from '../components/Appbar';
import BassaIntroBox from '../components/BassaIntroBox';
import UserSignup from '../components/UserSignup';

const LoginComponent = () => {
  
  const handleClickSubmit = (e) => {
    e.preventDefault()
    console.log('Handling button submit click')
  }
  return (
    <div>
      <Appbar isloggedIn={false} data-test="component-appbar" />
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