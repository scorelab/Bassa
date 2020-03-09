import React from 'react';
import Box from '@material-ui/core/Box';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import bassaImg from '../bassa.png';

const BassaGitHubRepoLink = 'https://github.com/scorelab/Bassa';

const useStyles = makeStyles(() => ({
  root: {
    marginTop: 40,
    marginLeft: 20,
    padding: 30
  },
  image: {
    maxWidth: '70%',
    maxHeight: '70%'
  }
}));

const BassaIntroBox = () => {
  const classes = useStyles();
  return (
    <Box className={classes.root}>
      <img alt="bassa" src={bassaImg} className={classes.image} />
      <br />
      <Typography variant="body1">
        Automated Download Queue for Enterprise to take the best use of Internet
        bandwidth.
      </Typography>
      <br />
      <br />
      <Typography variant="body1">
        Bassa solves the problem of wasting Internet bandwidth by queuing a
        download if it is larger than a given threshold value in high traffic
        and when the traffic is low, it completes the download of the files.
      </Typography>
      <br />
      <br />
      <Typography variant="body1">
        For more details, click <a href={BassaGitHubRepoLink}>here</a>
      </Typography>
    </Box>
  );
};

export default BassaIntroBox;
