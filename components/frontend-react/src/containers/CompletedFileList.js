import React from 'react';
import PropTypes from 'prop-types';

//MUI imports
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

//Component import
import CompletedFile from '../components/CompletedFile';

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
  row: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.background.default,
    },
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
      return <Typography variant="h5" color="inherit">No completed downloads</Typography>
    } else {
        if (this.props.limit) {
          const list = this.props.files.slice(0,this.props.limit);
          return this.renderList(list)
        }
      return this.renderList(this.props.files)  
    }
  }

  handleDownloadButton = (id) => {
    console.log('Downloading', id)
  }

  renderList = (list) => {
  	return (
      list.map((row,id) => (
      	<CompletedFile key={id} file={row} onDownload={() => {this.handleDownloadButton(row.id)}}/>
      ))
    )
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