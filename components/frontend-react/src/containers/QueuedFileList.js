import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { deleteDownload } from '../actions/downloadActions';

//MUI imports
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

//Component import
import QueuedFile from '../components/QueuedFile';

const styles = theme => ({
  root: {
    width: '100%',
  },
  button: {
    margin: theme.spacing(2)
  },
  icon: {
    marginRight: theme.spacing(2),
    fontSize:20
  }
});

class QueuedFileList extends React.Component {

  renderDownloadedList = () => {
    if (this.props.loading) {
      return <Typography data-test="text-loading" variant="h5" color="inherit">Loading...</Typography>
    } else if (this.props.files.length === 0) {
      return <Typography data-test="text-empty" variant="h5" color="inherit">No queued downloads</Typography>
    } else {
        if (this.props.limit) {
          const list = this.props.files.slice(0,this.props.limit);
          return this.renderList(list);
        }
      return this.renderList(this.props.files);
    }
  }

  renderList = (list) => {
  	return (
      list.map((row,id) => (
      	<QueuedFile data-test="element-item" key={id} index={id} name={row.download_name} onDelete={() => {this.handleDelete(row.id)}}/>
      ))
    )
  }

  handleDelete = (id) => {
    this.props.deleteDownload(id);
  }

  render() {
    const {classes} = this.props;
    return (
      <div className={classes.root}>
        {this.renderDownloadedList()}
      </div>
    )
  }
}

QueuedFileList.propTypes = {
  classes: PropTypes.object.isRequired,
}

const mapDispatchToProps = dispatch => ({
  deleteDownload: (id) => dispatch(deleteDownload(id)),
})

export default connect(null, mapDispatchToProps)(withStyles(styles)(QueuedFileList));