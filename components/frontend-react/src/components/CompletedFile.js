import React from 'react';
import PropTypes from 'prop-types';

//MUI imports
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';
import Button from '@material-ui/core/Button';
import SaveIcon from '@material-ui/icons/Save';

const CustomTableCell = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
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

function QueuedFile(props) {
  const { classes } = props;
  return (
    <div className={classes.root}>
      <Table>
        <TableBody>
          <TableRow>
            <CustomTableCell>{props.file.id}</CustomTableCell>
            <CustomTableCell className="row" component="th" scope="row">
              {props.file.user}
            </CustomTableCell>
            <CustomTableCell align="left">{props.file.name}</CustomTableCell>
            <CustomTableCell align="left">{props.file.size}</CustomTableCell>
            <CustomTableCell align="left">{props.file.time}</CustomTableCell>
            <CustomTableCell align="left">
              <Button variant="outlined" size="small" color="primary" className="button" onClick={props.onDownload}>
              <SaveIcon className="icon" /> Download
            </Button>
            </CustomTableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  )
}

QueuedFile.propTypes = {
  classes: PropTypes.object.isRequired,
  file: PropTypes.object
};


export default withStyles(styles)(QueuedFile);