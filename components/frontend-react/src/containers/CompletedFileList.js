import React from 'react';
import PropTypes from 'prop-types';

//MUI imports
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

//Component import
import CompletedFile from '../components/CompletedFile';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Checkbox from '@material-ui/core/Checkbox';

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  checkbox: {
    backgroundColor: '#ff6600'
  }
});

class CompletedFileList extends React.Component {

  constructor(){
    super();
    this.state = {list:[]}
  }

  componentDidMount(){
    let CompletedFileList = this.props.files;
    for (let index = 0; index < CompletedFileList.length; index++) {
      let element = CompletedFileList[index];
      element.checked = false;
      CompletedFileList.splice(index, 1, element)
    }
    this.setState({list: CompletedFileList});
  }

  renderDownloadedList = () => {
  	if (this.props.loading) {
      return <Typography data-test="text-loading" variant="h5" color="inherit">Loading...</Typography>
    } else if (this.state.list.length === 0) {
      return <Typography data-test="text-empty" variant="h5" color="inherit">No completed downloads</Typography>
    } else {
        if (this.props.limit) {
          const list = this.state.list.slice(0,this.props.limit);
          return this.renderList(list)
        }
      return this.renderList(this.props.files)  
    }
  }

  handleDownloadButton = (id) => {
    console.log('Downloading', id)
  }

  handleChecked = (id) => {
    let list =  this.state.list;
    let listItem = list.find(item => item.id === id);
    let index = list.indexOf(listItem);
    listItem.checked = !listItem.checked;
    list.splice(index, 1, listItem);
    this.setState({list});
  }

  renderList = (list) => {
  	return (
      list.map((row,id) => (
        <ListItem key={id}>
          <Checkbox
            style={{marginTop:25}}
            checked={row.checked}
            onChange={() => {this.handleChecked(row.id)}}
          />
      	  <CompletedFile data-test="element-item" file={row} onDownload={() => {this.handleDownloadButton(row.id)}}/>
        </ListItem>
      ))
    )
  }

  handleSharingFiles = () => {
    let chosenList = this.state.list.filter(item => item.checked === true);
    console.log("list of files to be shared: ", chosenList);
    let list = this.state.list;
    for (let index = 0; index < list.length; index++) {
      list[index].checked = false;
    }
    this.setState({list})
  }

  render() {
  	const {classes} = this.props;
  	return (
  	  <div className={classes.root}>
        <Button
          variant="outlined"
          size="small"
          color="primary"
          onClick={() => this.handleSharingFiles()}
          disabled={this.state.list.filter(item => item.checked === true).length === 0}
          aria-label="share files"
        >
          Share
        </Button>
        <List>
          {this.renderDownloadedList()}
        </List>
  	  </div>
  	)
  }
}

CompletedFileList.propTypes = {
	classes: PropTypes.object.isRequired,
}

CompletedFileList.defaultProps = {
  files: []
}

export default withStyles(styles)(CompletedFileList);