import React from 'react';
// eslint-disable-next-line import/no-extraneous-dependencies
import PropTypes from 'prop-types';

// MUI imports
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

// Component import
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Checkbox from '@material-ui/core/Checkbox';
import CompletedFile from '../components/CompletedFile';

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto'
  },
  checkbox: {
    backgroundColor: '#ff6600'
  }
});

class CompletedFileList extends React.Component {
  constructor() {
    super();
    this.state = { sharingList: [] };
  }

  componentWillMount() {
    const { files } = this.props;
    for (let index = 0; index < files.length; index += 1) {
      const element = files[index];
      element.checked = false;
      files.splice(index, 1, element);
    }
    this.setState({ sharingList: files });
  }

  handleDownloadButton = id => {
    // eslint-disable-next-line no-console
    console.log('Downloading', id);
  };

  handleChecked = id => {
    const { sharingList } = this.state;
    const listItem = sharingList.find(item => item.id === id);
    const index = sharingList.indexOf(listItem);
    listItem.checked = !listItem.checked;
    sharingList.splice(index, 1, listItem);
    this.setState({ sharingList });
  };

  handleSharingFiles = () => {
    const { sharingList } = this.state;
    // const chosenList = sharingList.filter(item => item.checked === true);
    // console.log('files to be shared: ', chosenList);
    for (let index = 0; index < sharingList.length; index += 1) {
      sharingList[index].checked = false;
    }
    this.setState({ sharingList });
  };

  renderDownloadedList = () => {
    const { limit } = this.props;
    const { sharingList } = this.state;
    if (limit) {
      const chosenList = sharingList.slice(0, limit);
      return this.renderList(chosenList);
    }
    return this.renderList(sharingList);
  };

  renderList = list => {
    return list.map(row => (
      <ListItem key={row.id}>
        <Checkbox
          style={{ marginTop: 25 }}
          checked={row.checked}
          onChange={() => {
            this.handleChecked(row.id);
          }}
        />
        <CompletedFile
          data-test="element-item"
          file={row}
          onDownload={() => {
            this.handleDownloadButton(row.id);
          }}
        />
      </ListItem>
    ));
  };

  render() {
    const { classes } = this.props;
    const { sharingList } = this.state;
    return (
      <div className={classes.root}>
        <Button
          variant="outlined"
          size="small"
          color="primary"
          onClick={() => this.handleSharingFiles()}
          disabled={
            sharingList.filter(item => item.checked === true).length === 0
          }
          aria-label="share files"
        >
          Share
        </Button>
        <List>{this.renderDownloadedList()}</List>
      </div>
    );
  }
}

CompletedFileList.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(CompletedFileList);
