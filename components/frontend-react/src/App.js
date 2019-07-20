import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';

import LoginComponent from './containers/LoginComponent';
import AdminComponent from './containers/AdminComponent';
import Dashboard from './containers/Dashboard';
import QueuedComponent from './containers/QueuedComponent';
import CompletedComponent from './containers/CompletedComponent';

const App = (props) => (
  <Switch>
    <Route exact path='/' isloggedIn={props.isloggedIn} component={LoginComponent} />
    <PrivateRoute exact path='/admin' isloggedIn={props.isloggedIn} component={AdminComponent} />
    <PrivateRoute exact path='/home' isloggedIn={props.isloggedIn} component={Dashboard} />
    <PrivateRoute exact path='/queued' isloggedIn={props.isloggedIn} component={QueuedComponent} />
    <PrivateRoute exact path='/completed' isloggedIn={props.isloggedIn} component={CompletedComponent} />
  </Switch>
)

const PrivateRoute = ({component: Component, isloggedIn, ...rest }) => (
  <Route
  {...rest}
  render={props =>
  isloggedIn ? (
  <Component {...props} />
  ) : (
  <Redirect
  to={{pathname:'/'}}/>
  )}/>
);

const mapStateToProps = state => ({
  isloggedIn: state.userReducer.isloggedIn
})

export default connect(mapStateToProps, null)(App);