import React, { useState } from 'react';
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

  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setconfirmPassword] = useState('');

  const handleTextFields = (event) => {
    switch(event.target.id)
    {
      case 'name':
        setUsername(event.target.value);
        return;

      case 'email':
        setEmail(event.target.value);
        return;

      case 'pass':
        setPassword(event.target.value);
        return;

      case 'c_pass':
        setconfirmPassword(event.target.value);
        return;

      default:
        return;
    }
  }

  const handleSubmitButton = (event) => {
    event.preventDefault();
    let details = {user_name: username, email: email, password: password, confirm_password: confirmPassword};
    if(password !== confirmPassword)
    {
      alert('Passwords do not match');
    }
    props.onClickSubmit(details);
  }
  const classes = useStyles();
  return (
    <Container className={classes.container} maxWidth="xs">
      <Typography className={classes.title} variant="h4">Create An Account</Typography>
        <form className={classes.formContainer} onSubmit={(e) => handleSubmitButton(e)}>
          <input id="name" className={classes.inputField} type="text" placeholder="Username" onChange={handleTextFields} data-test="field-username"/>
          <input id="email" className={classes.inputField} type="text" placeholder="Email" onChange={handleTextFields} data-test="field-email"/>
          <input id="pass" className={classes.inputField} type="text" placeholder="Password" onChange={handleTextFields} data-test="field-password"/>
          <input id="c_pass" className={classes.inputField} type="text" placeholder="Re-enter Password" onChange={handleTextFields} data-test="field-re-password"/>
          <div className={classes.buttonContainer}>
            <input type="submit"className={classes.button} data-test="button-submit"/>
          </div>
        </form>
    </Container>
 )
}

export default UserSignup;