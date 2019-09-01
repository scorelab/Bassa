/* eslint-disable camelcase */
import React from 'react';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import InputAdornment from '@material-ui/core/InputAdornment';
import NameIcon from '@material-ui/icons/SupervisorAccount';
import LockIcon from '@material-ui/icons/Lock';
import EmailIcon from '@material-ui/icons/Email';
import green from '@material-ui/core/colors/green';

const useStyles = makeStyles(theme => ({
  container: {
    backgroundColor: '#eae0d8',
    maxHeight: '100vh'
  },
  title: {
    padding: 20
  },
  formContainer: {
    padding: 20
  },
  inputField: {
    width: '80%',
    padding: 5,
    margin: 5
  },
  buttonContainer: {
    padding: 10,
    display: 'flex',
    flexDirection: 'center',
    justifyContent: 'center',
    alignItems: 'center'
  },
  button: {
    color: theme.palette.getContrastText(green[500]),
    backgroundColor: green[500],
    '&:hover': {
      backgroundColor: green[600]
    },
    fontWeight: '600',
    border: 0,
    margin: 10,
    padding: 15
  }
}));

const UserSignup = props => {
  const {
    values: { user_name, email, password, confirmPassword },
    errors,
    touched,
    handleSubmit,
    handleChange,
    isValid
  } = props;

  const classes = useStyles();
  return (
    <Container className={classes.container} maxWidth="xs">
      <Typography className={classes.title} variant="h4">
        Create An Account
      </Typography>
      <form className={classes.formContainer} onSubmit={handleSubmit}>
        <TextField
          name="user_name"
          className={classes.inputField}
          helperText={touched.user_name ? errors.user_name : ''}
          error={Boolean(errors.user_name)}
          label="Name"
          value={user_name}
          onChange={handleChange}
          fullWidth
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <NameIcon />
              </InputAdornment>
            )
          }}
        />

        <TextField
          name="email"
          className={classes.inputField}
          helperText={touched.email ? errors.email : ''}
          error={Boolean(errors.email)}
          label="Email"
          value={email}
          onChange={handleChange}
          fullWidth
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <EmailIcon />
              </InputAdornment>
            )
          }}
        />

        <TextField
          name="password"
          className={classes.inputField}
          type="password"
          helperText={touched.password ? errors.password : ''}
          error={Boolean(errors.password)}
          label="Password"
          value={password}
          onChange={handleChange}
          fullWidth
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <LockIcon />
              </InputAdornment>
            )
          }}
        />

        <TextField
          name="confirmPassword"
          className={classes.inputField}
          type="password"
          helperText={touched.confirmPassword ? errors.confirmPassword : ''}
          error={Boolean(errors.confirmPassword)}
          label="Confirm Password"
          value={confirmPassword}
          onChange={handleChange}
          fullWidth
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <LockIcon />
              </InputAdornment>
            )
          }}
        />
        <div className={classes.buttonContainer}>
          <Button className={classes.button} type="submit" disabled={!isValid}>
            Submit
          </Button>
        </div>
      </form>
    </Container>
  );
};

export default UserSignup;
