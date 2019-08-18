import React from 'react';
// eslint-disable-next-line import/no-extraneous-dependencies
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

// MUI imports
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import { deleteDownload } from '../actions/downloadActions';

// Component import
import QueuedFile from '../components/QueuedFile';

const styles = theme => ({
  root: {
    width: '100%'
  },
  button: {
    margin: theme.spacing(2)
  },
  icon: {
    marginRight: theme.spacing(2),
    fontSize: 20
  }
});

class QueuedFileList extends React.Component {
  renderDownloadedList = () => {
    const { loading, limit, queuedDownloads } = this.props;
    if (loading) {
      return (
        <Typography data-test="text-loading" variant="h5" color="inherit">
          Loading...
        </Typography>
      );
    }
    if (queuedDownloads.length === 0) {
      return (
        <Typography data-test="text-empty" variant="h5" color="inherit">
          No queued downloads
        </Typography>
      );
    }
    if (limit) {
      const list = queuedDownloads.slice(0, limit);
      return this.renderList(list);
    }
    return this.renderList(queuedDownloads);
  };

  renderList = list => {
    return list.map((row, id) => (
      <QueuedFile
        data-test="element-item"
        key={row.id}
        index={id}
        name={row.download_name}
        onDelete={() => {
          this.handleDelete(row.id);
        }}
      />
    ));
  };

  handleDelete = id => {
    const { deleteDownloadingFile } = this.props;
    deleteDownloadingFile(id);
  };

  render() {
    const { classes } = this.props;
    return <div className={classes.root}>{this.renderDownloadedList()}</div>;
  }
}

QueuedFileList.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  classes: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  queuedDownloads: state.downloadReducer.queuedDownloads
});

const mapDispatchToProps = dispatch => ({
  deleteDownloadingFile: id => dispatch(deleteDownload(id))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(withStyles(styles)(QueuedFileList));
