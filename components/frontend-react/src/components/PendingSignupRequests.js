import React from 'react';
import PropTypes from 'prop-types';
import Box from '@material-ui/core/Box';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import FAB from '@material-ui/core/Fab';
import DoneIcon from '@material-ui/icons/Done';

const CustomTableCell = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
    marginRight: 140
  },
}))(TableCell);

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3, 2),
    overflowX: 'auto',
  },
  row: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.background.default,
    },
  },

  button: {
    marginRight: theme.spacing(2),
    maxWidth:50,
    maxHeight:50
  }
}));

const PendingSignupRequests = (props) => {
  const classes = useStyles();
  return (
    <Box className={classes.root}>
      <p>Signup Requests</p>
        {props.requestsList.map((elem, index) => 
        <Table key={index} data-test="item-requests">
          <TableBody>
          <TableRow className={classes.row}>
              <CustomTableCell align="left">{index+1}</CustomTableCell>
              <CustomTableCell align="left">{elem.name}</CustomTableCell>
              <CustomTableCell align="left">{elem.email}</CustomTableCell>
              <CustomTableCell align="left">
                <FAB data-test="button-approve" className={classes.button} onClick={props.onSubmit}><DoneIcon/></FAB>
              </CustomTableCell>
          </TableRow>
          </TableBody>
        </Table>)}
    </Box>
  );
}

PendingSignupRequests.propTypes = {
  requestsList: PropTypes.array.isRequired,
}

export default PendingSignupRequests;