import React from 'react';
import moment from 'moment';

// MUI imports
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
    color: theme.palette.common.white
  },
  body: {
    fontSize: 14
  }
}))(TableCell);

const useStyles = makeStyles(theme => ({
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
  button: {
    margin: theme.spacing(2)
  },
  icon: {
    marginRight: theme.spacing(2),
    fontSize: 20
  }
}));

const CompletedFile = props => {
  const classes = useStyles();
  const { file, onDownload } = props;
  const timeStamp = new Date(file.completed_time * 1000);
  return (
    <div className={classes.root}>
      <Table>
        <TableBody>
          <TableRow>
            <CustomTableCell>{file.id}</CustomTableCell>
            <CustomTableCell className="row" component="th" scope="row">
              {file.user_name}
            </CustomTableCell>
            <CustomTableCell align="left">{file.download_name}</CustomTableCell>
            <CustomTableCell align="left">
              {file.size / 1024} KB
            </CustomTableCell>
            <CustomTableCell align="left">
              {moment(timeStamp).fromNow()}
            </CustomTableCell>
            <CustomTableCell align="right">
              <Button
                data-test="button-download"
                variant="outlined"
                size="small"
                color="primary"
                className={classes.button}
                onClick={onDownload}
              >
                <SaveIcon className="icon" /> Download
              </Button>
            </CustomTableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  );
};

export default CompletedFile;
