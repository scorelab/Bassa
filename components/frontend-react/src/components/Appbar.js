import React from 'react';
import PropTypes from 'prop-types';

//MUI imports
import {withStyles} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Avatar from '@material-ui/core/Avatar';
import TextField from '@material-ui/core/TextField';

//Logo import
import logo from '../logo.png';

const styles = {
  root: {
    flexGrow: 1,
    backgroundColor: '#ff5500'
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
};

function BassaAppBar(props) {
  const { classes } = props;

  if (!props.isloggedIn) {
  	return (
	  <div className={classes.root}>
	    <AppBar position="static" style={{background: '#625042'}}>
	      <Toolbar>
		    <Avatar alt="Bassa" src={logo} className={classes.bigAvatar} />
	        <Typography variant="h4" color="inherit" className={classes.grow}>
	          Bassa
	        </Typography>
          <TextField 
            id="username"
            variant="outlined"
            style={{background:'#625042', color:'#fff'}}
            label="Username" />&nbsp;&nbsp;
          <TextField 
            id="password"
            type="password"
            label="Password" />&nbsp;&nbsp;
	        <Button size="small" variant="contained" color="primary">Login</Button>
	      </Toolbar>
	    </AppBar>
	  </div>
  	)
  }
  return (
  	<div className={classes.root}>
      <AppBar position="static" style={{background: '#625042'}}>
        <Toolbar>
	      <Avatar alt="Bassa" src={logo} className={classes.avatar} />
          <Typography variant="h6" color="inherit" className={classes.grow}>
            Bassa
          </Typography>
          <Button size="small" color="inherit">Dashboard</Button>
          <Button size="small" color="inherit">Admin</Button>
          <Button size="small" color="inherit">Logout</Button>
        </Toolbar>
      </AppBar>
    </div>
  )
}


BassaAppBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(BassaAppBar);