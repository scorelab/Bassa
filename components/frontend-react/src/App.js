import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import LoginComponent from './containers/LoginComponent';
import AdminComponent from './containers/AdminComponent';
import Dashboard from './containers/Dashboard';
import QueuedComponent from './containers/QueuedComponent';
import CompletedComponent from './containers/CompletedComponent';

const App = () => (
  <Switch>
    <Route exact path='/' component={LoginComponent} />
    <PrivateRoute exact path='/admin' component={AdminComponent} />
    <PrivateRoute exact path='/home' component={Dashboard} />
    <PrivateRoute exact path='/queued' component={QueuedComponent} />
    <PrivateRoute exact path='/completed' component={CompletedComponent} />
  </Switch>
)

const PrivateRoute = ({component: Component, ...rest }) => (
  <Route
  {...rest}
  render={props =>
  sessionStorage.getItem('token') ? (
  <Component {...props} />
  ) : (
  <Redirect
  to={{pathname:'/'}}/>
  )}/>
);

export default App;