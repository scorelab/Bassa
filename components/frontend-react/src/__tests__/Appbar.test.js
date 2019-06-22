import React from 'react';
import { shallow } from 'enzyme';
import Appbar from '../components/Appbar';

const setupComponent = props => {
  const component = shallow(<Appbar {...props} />);
  return component;
}

const findByTestAttr = (component, attr) => {
  const wrapper = component.find(`[data-test='${attr}']`);
  return wrapper;
}

describe('Appbar Component Testing', () => {
  it('should match with its snapshot', () => {
    const component = setupComponent()
    expect(component).toMatchSnapshot();
  });
  describe('User is logged in', () => {
    it('should display logged in view', () => {
      const component = setupComponent({isloggedIn: true});
      const buttonLogout = findByTestAttr(component, 'button-logout');
      const buttonDashboard = findByTestAttr(component, 'button-dashboard');
      const buttonAdmin = findByTestAttr(component, 'button-admin');
      
      expect(buttonLogout.props().children).toBe('Logout');
      expect(buttonDashboard.props().children).toBe('Dashboard');
      expect(buttonAdmin.props().children).toBe('Admin');
    });
  });

  describe('User is logged out', () => {
    it('should display logged out view', () => {
      const component = setupComponent({isloggedIn: false});
      const inputUsername = findByTestAttr(component, 'input-username');
      const inputPassword = findByTestAttr(component, 'input-password');
      
      expect(inputUsername.props().id).toBe('username');
      expect(inputPassword.props().id).toBe('password');
    })
  })
});