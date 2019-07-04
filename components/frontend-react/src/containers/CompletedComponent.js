import React from 'react';
import axios from 'axios';
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
  constructor(){
    super();
    this.state = {
      files: [],
    }
    let token = sessionStorage.getItem('token')
    axios({
      method:'get',
      url:`${process.env.REACT_APP_API_URL}/api/user/downloads/1`,
      headers: {'token': `${token}`}
    })
    .then(res => {
      let array = res.data.filter(file => file.status === 3);
      this.setState({files: array});
    })
    .catch(err => console.log(err));
  }

  render() {
    const { classes } = this.props;
    if(this.state.files.length !== 0)
    {
      console.log(this.state.files)
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
              <CompletedList files={this.state.files}/>
            </Paper>
          </div>
        </div>
      )
    }
    else {
      return <div>Loading</div>
    }	
  }
}

export default withStyles(styles)(CompletedComponent);