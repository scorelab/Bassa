import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';

import LoginComponent from './containers/LoginComponent';
import AdminComponent from './containers/AdminComponent';
import Dashboard from './containers/Dashboard';
import QueuedComponent from './containers/QueuedComponent';
import CompletedComponent from './containers/CompletedComponent';

const App = ({isloggedIn}) => (
  <Switch>
    <Route exact path='/' isloggedIn={isloggedIn} component={LoginComponent} />
    <PrivateRoute exact path='/admin' isloggedIn={isloggedIn} component={AdminComponent} />
    <PrivateRoute exact path='/home' isloggedIn={isloggedIn} component={Dashboard} />
    <PrivateRoute exact path='/queued' isloggedIn={isloggedIn} component={QueuedComponent} />
    <PrivateRoute exact path='/completed' isloggedIn={isloggedIn} component={CompletedComponent} />
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