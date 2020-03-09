import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles(theme => ({
  root: {
    margin: theme.spacing(3, 2)
  },
  button: {
    margin: theme.spacing(1)
  }
}));

const StartKillDownloads = props => {
  const classes = useStyles();
  const { onStart, onKill } = props;
  return (
    <div>
      <Box className={classes.root}>
        <p>Start/Kill all downloads</p>
        <Button
          data-test="button-start"
          className={classes.button}
          color="primary"
          variant="outlined"
          onClick={onStart}
        >
          Start
        </Button>
        <Button
          data-test="button-kill"
          className={classes.button}
          color="secondary"
          variant="outlined"
          onClick={onKill}
        >
          Kill
        </Button>
      </Box>
    </div>
  );
};

export default StartKillDownloads;
