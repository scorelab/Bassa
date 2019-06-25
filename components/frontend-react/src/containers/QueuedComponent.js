import React from 'react';

import Appbar from '../components/Appbar';

//MUI imports
import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';

//Component Import
import QueuedList from './QueuedFileList';


const styles = theme => ({
  root: {
    flexGrow: 1,
  },
  paper: {
  	padding: theme.spacing(2),
    textAlign: 'center',
  },
})

class QueuedComponent extends React.Component{
  render() {
  	const { classes } = this.props;
    return (
      <div className={classes.root}>
        <Appbar isloggedIn={true} />
          <div className={classes.paper}>
            <Paper className={classes.paper} elevation={15}>
              <Typography variant="h3" gutterBottom>
                Queued Downloads
              </Typography>
              <Divider/>
              <Typography variant="h5" gutterBottom>
                List of files required to be downloaded
              </Typography>
              <QueuedList files={this.props.queuedList}/>
            </Paper>
          </div>        
      </div>
    )	
  }
}

export default withStyles(styles)(QueuedComponent);