/* eslint-disable no-shadow */
import React from 'react';
// eslint-disable-next-line import/no-extraneous-dependencies
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

// Component imports

// MUI imports
import { withStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import FAB from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';
import Input from '@material-ui/core/Input';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import green from '@material-ui/core/colors/green';
import Button from '@material-ui/core/Button';
import QueuedFileList from './QueuedFileList';
import Appbar from '../components/Appbar';
import CompletedFileList from './CompletedFileList';
import { addNewDownload } from '../actions/downloadActions';

import '../index.css';
import SnackbarComponent from '../components/ToastComponent';

const styles = theme => ({
  grid: {
    flexGrow: 1,
    marginTop: 20
  },
  paper: {
    padding: theme.spacing(3),
    textAlign: 'center',
    maxHeight: 500,
    overflow: 'auto',
    overflowX: 'none',
    color: theme.palette.text.secondary
  },
  heading: {
    padding: 20
  },
  paperAdd: {
    textAlign: 'center',
    paddingBottom: 20
  },
  link: {
    width: 850,
    borderTop: 2
  },
  fab: {
    marginLeft: 30,
    color: theme.palette.getContrastText(green[500]),
    backgroundColor: green[500],
    '&:hover': {
      backgroundColor: green[600]
    }
  },
  card: {
    padding: 10
  }
});

class Dashboard extends React.Component {
  state = {
    link: '',
    hasFetchingDataFailed: false
  };

  renderCompletedDownloads = () => {
    const { completedDownloads } = this.props;
    if (completedDownloads.length === 0)
      return <div> No completed downloads </div>;
    if (completedDownloads.length !== 0) {
      return <CompletedFileList files={completedDownloads} limit={20} />;
    }
    return <div>Loading...</div>;
  };

  handleLinkField = event => {
    const link = event.target.value;
    this.setState({ link });
  };

  handleAddButton = () => {
    const { link } = this.state;
    const { addNewDownload } = this.props;
    addNewDownload(link);
  };

  // eslint-disable-next-line consistent-return
  renderSnackbar = () => {
    const { hasFetchingDataFailed } = this.state;
    const {
      haveFetchingDownloadsFailed,
      hasAddingDownloadFailed,
      errorMessage
    } = this.props;
    // the local state "hasFetchingDataFailed" checks: when the component gets mounted,
    // are we able to fetch files? Whereas, the prop "haveFetchingDownloadsFailed" checks
    // for all the API requests made to the server via user are we able to fetch files?
    // Check downloadSaga file in ../sagas to see how they both differ
    if (hasFetchingDataFailed || haveFetchingDownloadsFailed) {
      return (
        <SnackbarComponent
          variant="error"
          didEventOccured={hasFetchingDataFailed}
          message="Error fetching data. Check if server is started and DB is connected"
        />
      );
    }
    if (hasAddingDownloadFailed) {
      return (
        <SnackbarComponent
          variant="error"
          didEventOccured={hasAddingDownloadFailed}
          message={errorMessage}
        />
      );
    }
  };

  render() {
    const { classes, username, queuedDownloads } = this.props;
    const { link } = this.state;
    return (
      <div className={classes.root}>
        <Appbar isloggedIn />
        <Typography variant="h5" className={classes.heading}>
          Hi {username}!
        </Typography>
        <Paper className={classes.paperAdd}>
          <Typography variant="h5">ADD DOWNLOAD</Typography>
          <form>
            <Input
              type="text"
              className={classes.link}
              value={link}
              onChange={this.handleLinkField}
              placeholder="Enter or paste the link below"
            />
            <FAB
              color="primary"
              size="small"
              className={classes.fab}
              aria-label="add-download"
              onClick={this.handleAddButton}
            >
              <AddIcon />
            </FAB>
          </form>
        </Paper>
        <Grid container className={classes.grid} spacing={1}>
          <Grid item xs={6} sm={6}>
            <Paper className={classes.paper}>
              <Card className={classes.card}>
                <Typography variant="h5">
                  Completed Downloads&nbsp;
                  <Link to="/completed">
                    <Button size="small" variant="outlined" color="primary">
                      show all
                    </Button>
                  </Link>
                </Typography>
              </Card>
              {this.renderCompletedDownloads()}
            </Paper>
          </Grid>
          <Grid item xs={6} sm={6}>
            <Paper className={classes.paper}>
              <Card className={classes.card}>
                <Typography variant="h5">
                  In Queue&nbsp;
                  <Link to="/queued">
                    <Button size="small" variant="outlined" color="primary">
                      show all
                    </Button>
                  </Link>
                </Typography>
              </Card>
              <QueuedFileList files={queuedDownloads} limit={20} />
            </Paper>
          </Grid>
        </Grid>
        {this.renderSnackbar()}
      </div>
    );
  }
}

Dashboard.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  classes: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  username: state.userReducer.username,
  queuedDownloads: state.downloadReducer.queuedDownloads,
  completedDownloads: state.downloadReducer.completedDownloads,
  haveFetchingDownloadsFailed:
    state.downloadReducer.haveFetchingDownloadsFailed,
  hasAddingDownloadFailed: state.downloadReducer.hasAddingDownloadFailed,
  errorMessage: state.downloadReducer.errorMessage
});

const mapDispatchToProps = dispatch => ({
  addNewDownload: link => dispatch(addNewDownload(link))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(withStyles(styles)(Dashboard));
