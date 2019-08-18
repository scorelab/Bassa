import React from 'react';
// eslint-disable-next-line import/no-extraneous-dependencies
import PropTypes from 'prop-types';

// MUI imports
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
    color: theme.palette.common.white
  },
  body: {
    fontSize: 14
  }
}))(TableCell);

const styles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto'
  },
  row: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.background.default
    }
  },
  icon: {
    marginRight: theme.spacing(2),
    fontSize: 20
  },
  fab: {
    color: theme.palette.getContrastText(red[500]),
    backgroundColor: red[500],
    '&:hover': {
      backgroundColor: red[700]
    }
  }
}));

const QueuedFile = props => {
  const classes = styles();
  const { index, name, onDelete } = props;
  return (
    <div className={classes.root}>
      <Table>
        <TableBody>
          <TableRow>
            <CustomTableCell>{index + 1}</CustomTableCell>
            <CustomTableCell className={classes.row} component="th" scope="row">
              {name}
            </CustomTableCell>
            <CustomTableCell align="right">
              <Fab
                data-test="button-delete"
                size="small"
                aria-label="Delete"
                className={classes.fab}
                onClick={onDelete}
              >
                <DeleteIcon />
              </Fab>
            </CustomTableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  );
};

QueuedFile.propTypes = {
  name: PropTypes.string.isRequired
};

export default QueuedFile;
