import React, { useState } from 'react';

//MUI imports
import {makeStyles} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Avatar from '@material-ui/core/Avatar';
import TextField from '@material-ui/core/TextField';

//Logo import
import logo from '../logo.png';

const colours = {
  somewhat_brown: '#625042',
  white: '#fff'
}

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    margin: theme.spacing(2),
    marginTop: theme.spacing(3)
  },
  avatar: {
    margin: 10,
  },
  bigAvatar: {
    margin: 10,
    width: 60,
    height: 60,
  },
}));

const BassaAppBar = (props) => {
  const classes = useStyles();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUserField = (event) => {
    setUsername(event.target.value);
  }

  const handlePassField = (event) => {
    setPassword(event.target.value);
  }

  const handleLoginButton = (event) => {
    event.preventDefault();
    props.onClickLogin(username, password);
  }

  if (!props.isloggedIn) {
    //If the user is not logged in, then return component for logged out user
  	return (
	  <div className={classes.root}>
	    <AppBar position="static" style={{background: colours.somewhat_brown}}>
	      <Toolbar>
		    <Avatar alt="Bassa" src={logo} className={classes.bigAvatar} />
	        <Typography variant="h4" color="inherit" className={classes.grow}>
	          Bassa
	        </Typography>
          <form onSubmit={handleLoginButton}>
            <TextField 
              id="username"
              data-test="input-username"
              margin="normal"
              variant="outlined"
              onChange={handleUserField}
              style={{background:colours.white}}
              placeholder="Username" />&nbsp;&nbsp;
            <TextField 
              id="password"
              data-test="input-password"
              type="password"
              variant="outlined"
              onChange={handlePassField}
              margin="normal"
              style={{background:colours.white}}
              placeholder="Password" />&nbsp;&nbsp;
            <Button type="submit" className={classes.menuButton} size="large" variant="contained" color="primary">Login</Button>
          </form>
	      </Toolbar>
	    </AppBar>
	  </div>
  	)
  }
  //Else return component for logged in user
  return (
  	<div className={classes.root}>
      <AppBar position="static" style={{background: colours.somewhat_brown}}>
        <Toolbar>
	      <Avatar alt="Bassa" src={logo} className={classes.avatar} />
          <Typography variant="h6" color="inherit" className={classes.grow}>
            Bassa
          </Typography>
          <Button data-test="button-dashboard" size="small" color="inherit">Dashboard</Button>
          <Button data-test="button-admin" size="small" color="inherit">Admin</Button>
          <Button data-test="button-logout" size="small" color="inherit">Logout</Button>
        </Toolbar>
      </AppBar>
    </div>
  )
}

export default BassaAppBar;