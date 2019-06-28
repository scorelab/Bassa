import React from 'react';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import green from '@material-ui/core/colors/green';

const useStyles = makeStyles(theme => ({
  container: {
    backgroundColor:'#eae0d8',
    maxHeight: '100vh',
  },
  title: {
    padding: 20,
  },
  formContainer: {
    padding: 20,
  },
  inputField: {
    width: '80%',
    padding: 10,
    margin: 10,
  },
  buttonContainer: {
    padding:10,
    display: 'flex',
    flexDirection: 'center',
    justifyContent: 'center',
    alignItems: 'center',
  },
  button: {
    color: theme.palette.getContrastText(green[500]),
    backgroundColor: green[500],
    '&:hover': {
      backgroundColor: green[600],
    },
    fontWeight:'600',
    border:0,
    margin:10,
    padding: 15,
  },
}));

const UserSignup = (props) => {

  const handleSubmitButton = (event) => {
    event.preventDefault();
    props.onClickSubmit();
  }
  const classes = useStyles();
  return (
    <Container className={classes.container} maxWidth="xs">
      <Typography className={classes.title} variant="h4">Create An Account</Typography>
        <form className={classes.formContainer} onSubmit={(e) => handleSubmitButton(e)}>
          <input className={classes.inputField} type="text" placeholder="Username" data-test="field-username"/>
          <input className={classes.inputField} type="text" placeholder="Email" data-test="field-email"/>
          <input className={classes.inputField} type="text" placeholder="Password" data-test="field-password"/>
          <input className={classes.inputField} type="text" placeholder="Re-enter Password" data-test="field-re-password"/>
          <div className={classes.buttonContainer}>
            <input type="submit"className={classes.button} data-test="button-submit"/>
          </div>
        </form>
    </Container>
 )
}

export default UserSignup;