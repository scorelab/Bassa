import React from 'react';
import PropTypes from 'prop-types';

import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

//Component import
import QueuedFile from '../components/QueuedFile';

const styles = theme => ({
  root: {
    width: '100%',
    maxWidth: 560,
  },
  button: {
    margin: theme.spacing.unit
  },
  icon: {
    marginRight: theme.spacing.unit,
    fontSize:20
  }
});

class CompletedFileList extends React.Component {

  renderDownloadedList = () => {
    if (this.props.loading) {
      return <Typography variant="h5" color="inherit">Loading...</Typography>
    } else if (this.props.files.length === 0) {
      return <Typography variant="h5" color="inherit">No queued downloads</Typography>
    } else {
        if (this.props.limit) {
          const list = this.props.files.slice(0,this.props.limit);
          return (
            list.map((row,id) => (
                <QueuedFile key={id} index={id} name={row} onDelete={this.handleDelete(id)} />
            ))
          )
        }
      return (
        this.props.files.map((row,id) => (
            <QueuedFile key={id} index={id} name={row} onDelete={() => this.handleDelete(id)}/>
        ))
      )
    }
  }

  handleDelete = (id) => {
    console.log('deleting', id)
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

CompletedFileList.propTypes = {
  classes: PropTypes.object.isRequired,
}

export default withStyles(styles)(CompletedFileList);