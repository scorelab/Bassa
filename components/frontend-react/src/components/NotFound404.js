import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  container: {
    backgroundColor: '#19243c',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: '100%',
    height: '100vh'
  },
  content: {
    color: '#fff'
  }
});

const NotFound404 = () => {
  const classes = useStyles();
  return (
    <div className={classes.container}>
      <Typography variant="h5" className={classes.content}>
        <b>404</b> | This route does not exist, kindly switch to the root (/)
        route, and explore the app
      </Typography>
    </div>
  );
};

export default NotFound404;
