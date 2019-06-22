import React from 'react';

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
    marginLeft: -12,
    marginRight: 20,
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
          <TextField 
            id="username"
            data-test="input-username"
            margin="normal"
            variant="outlined"
            style={{background:colours.white}}
            placeholder="Username" />&nbsp;&nbsp;
          <TextField 
            id="password"
            data-test="input-password"
            type="password"
            variant="outlined"
            margin="normal"
            style={{background:colours.white}}
            placeholder="Password" />&nbsp;&nbsp;
	        <Button size="large" variant="contained" color="primary">Login</Button>
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