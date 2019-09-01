import React from 'react';
// eslint-disable-next-line import/no-extraneous-dependencies
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

// MUI imports
import Box from '@material-ui/core/Box';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import FAB from '@material-ui/core/Fab';
import DoneIcon from '@material-ui/icons/Done';
import { approveSignupRequest } from '../actions/userActions';

const CustomTableCell = withStyles(theme => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white
  },
  body: {
    fontSize: 14,
    marginRight: 140
  }
}))(TableCell);

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3, 2),
    overflowX: 'auto'
  },
  row: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.background.default
    }
  },

  button: {
    marginRight: theme.spacing(2),
    maxWidth: 50,
    maxHeight: 50
  }
}));

const PendingSignupRequests = props => {
  const classes = useStyles();
  const { requestsList } = props;
  return (
    <Box className={classes.root}>
      <p>Signup Requests</p>
      {requestsList.map((elem, index) => (
        <Table key={elem.email} data-test="item-requests">
          <TableBody>
            <TableRow className={classes.row}>
              <CustomTableCell align="left">{index + 1}</CustomTableCell>
              <CustomTableCell align="left">{elem.user_name}</CustomTableCell>
              <CustomTableCell align="left">{elem.email}</CustomTableCell>
              <CustomTableCell align="right">
                <FAB
                  data-test="button-approve"
                  className={classes.button}
                  onClick={() => props.onSubmit(elem.user_name)}
                >
                  <DoneIcon />
                </FAB>
              </CustomTableCell>
            </TableRow>
          </TableBody>
        </Table>
      ))}
    </Box>
  );
};

PendingSignupRequests.propTypes = {
  // eslint-disable-next-line react/forbid-prop-types
  requestsList: PropTypes.array.isRequired
};

const mapDispatchToProps = dispatch => ({
  onSubmit: username => dispatch(approveSignupRequest(username))
});

export default connect(
  null,
  mapDispatchToProps
)(PendingSignupRequests);
