import React from 'react';
import PropTypes from 'prop-types';

//MUI imports
import { withStyles, makeStyles } from '@material-ui/core/styles';
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

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  row: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.background.default,
    },
  },
  button: {
    margin: theme.spacing(2)
  },
  icon: {
    marginRight: theme.spacing(2),
    fontSize:20
  }
}));

const CompletedFile = (props) => {
  const classes = useStyles();
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
            <CustomTableCell align="right">
              <Button data-test="button-download" variant="outlined" size="small" color="primary" className={classes.button} onClick={props.onDownload}>
              <SaveIcon className="icon" /> Download
            </Button>
            </CustomTableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  )
}

CompletedFile.propTypes = {
  file: PropTypes.object
};


export default CompletedFile;