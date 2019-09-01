/* eslint-disable no-return-assign */
/* eslint-disable no-undef */
import React from 'react';
import { shallow, mount } from 'enzyme';
import { BrowserRouter } from 'react-router-dom';
import Appbar from '../components/Appbar';

const findByTestAttr = (component, attr) => {
  const wrapper = component.find(`[data-test='${attr}']`);
  return wrapper;
};

describe('Appbar Component Testing', () => {
  let component;
  beforeEach(() => (component = shallow(<Appbar />)));

  it('should match with its snapshot', () => {
    expect(component).toMatchSnapshot();
  });

  describe('User is logged in', () => {
    beforeEach(
      () =>
        (component = mount(
          <BrowserRouter>
            <Appbar isloggedIn />
          </BrowserRouter>
        ))
    );

    it('should display logged in view', () => {
      const buttonDashboard = findByTestAttr(component, 'button-dashboard').at(
        4
      );
      const buttonAdmin = findByTestAttr(component, 'button-admin').at(4);
      const buttonLogout = findByTestAttr(component, 'button-logout').at(4);

      expect(buttonDashboard.props().children[0].props.children).toBe(
        'Dashboard'
      );
      expect(buttonAdmin.props().children[0].props.children).toBe('Admin');
      expect(buttonLogout.props().children[0].props.children).toBe('Logout');
    });
  });

  describe('User is logged out', () => {
    beforeEach(
      () =>
        (component = mount(
          <BrowserRouter>
            <Appbar isloggedIn={false} />
          </BrowserRouter>
        ))
    );

    it('should display logged out view', () => {
      const inputUsername = findByTestAttr(component, 'input-username').at(4);
      const inputPassword = findByTestAttr(component, 'input-password').at(4);

      expect(inputUsername.props().children[1].props.id).toBe('username');
      expect(inputPassword.props().children[1].props.id).toBe('password');
    });
  });
});
