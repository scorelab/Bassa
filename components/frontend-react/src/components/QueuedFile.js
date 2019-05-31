import React from 'react';
import PropTypes from 'prop-types';

//MUI imports
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';
import Fab from '@material-ui/core/Fab';
import DeleteIcon from '@material-ui/icons/DeleteOutlined';
import red from '@material-ui/core/colors/red';

const CustomTableCell = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const styles = makeStyles(theme => ({
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
  },
  fab: {
    color: theme.palette.getContrastText(red[500]),
    backgroundColor: red[500],
    '&:hover': {
      backgroundColor: red[700],
    },
  }
}));


const QueuedFile = (props) => {
  const classes = styles();
  return (
    <div className={classes.root}>
      <Table>
        <TableBody>
          <TableRow>
            <CustomTableCell>{props.index + 1}</CustomTableCell>
            <CustomTableCell className="row" component="th" scope="row">
              {props.name}
            </CustomTableCell>
            <CustomTableCell align="right">
              <Fab size="small" aria-label="Delete" className={classes.fab} onClick={props.onDelete}>
                <DeleteIcon />
              </Fab>
            </CustomTableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  )
}

QueuedFile.propTypes = {
  classes: PropTypes.object.isRequired,
  name: PropTypes.string.isRequired,
  onDelete: PropTypes.func
};


export default QueuedFile;