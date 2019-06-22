import React from 'react';

import Appbar from '../components/Appbar';

//MUI imports
import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';

//Component import
import CompletedList from './CompletedFileList';

const styles = theme => ({
  root: {
  	padding: theme.spacing(2),
    textAlign: 'center',
  },
})

class CompletedComponent extends React.Component{
  render() {
  	const { classes } = this.props;
    return (
      <div>
        <Appbar isloggedIn={true} />
        <div className={classes.root}>
          <Paper className={classes.root} elevation={15}>
            <Typography variant="h3" gutterBottom >
              Completed Downloads
            </Typography>
            <Divider/>
            <Typography variant="h5" gutterBottom >
              List of downloaded files
            </Typography>
            <CompletedList files={this.props.completedList}/>
          </Paper>
        </div>
      </div>
    )	
  }
}

export default withStyles(styles)(CompletedComponent);