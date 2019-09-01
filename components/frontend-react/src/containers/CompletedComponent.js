import React from 'react';
import axios from 'axios';

// MUI imports
import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import Appbar from '../components/Appbar';

// Component import
import CompletedList from './CompletedFileList';

const styles = theme => ({
  root: {
    padding: theme.spacing(2),
    textAlign: 'center'
  }
});

class CompletedComponent extends React.Component {
  state = {
    files: []
  };

  componentWillMount() {
    const token = sessionStorage.getItem('token');
    axios({
      method: 'get',
      url: `${process.env.REACT_APP_API_GET_DOWNLOADS}`,
      headers: { token: `${token}` }
    })
      .then(res => {
        const array = res.data.filter(file => file.status === 3);
        this.setState({ files: array });
      })
      // eslint-disable-next-line no-console
      .catch(err => console.log(err));
  }

  render() {
    const { classes } = this.props;
    const { files } = this.state;
    if (files.length !== 0) {
      return (
        <div>
          <Appbar isloggedIn />
          <div className={classes.root}>
            <Paper className={classes.root} elevation={15}>
              <Typography variant="h3" gutterBottom>
                Completed Downloads
              </Typography>
              <Divider />
              <Typography variant="h5" gutterBottom>
                List of downloaded files
              </Typography>
              <CompletedList files={files} />
            </Paper>
          </div>
        </div>
      );
    }
    return <div>Loading</div>;
  }
}

export default withStyles(styles)(CompletedComponent);
