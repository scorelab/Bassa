import React from 'react';
import { shallow } from 'enzyme';
import Appbar from '../components/Appbar';

const findByTestAttr = (component, attr) => {
  const wrapper = component.find(`[data-test='${attr}']`);
  return wrapper;
}

describe('Appbar Component Testing', () => {
  let component;
  beforeEach(() => component = shallow(<Appbar />));

  it('should match with its snapshot', () => {
    expect(component).toMatchSnapshot();
  });
  
  describe('User is logged in', () => {
    
    let component;
    beforeEach(() => component = shallow(<Appbar isloggedIn={true} />));

    it('should display logged in view', () => {
      const buttonLogout = findByTestAttr(component, 'button-logout');
      const buttonDashboard = findByTestAttr(component, 'button-dashboard');
      const buttonAdmin = findByTestAttr(component, 'button-admin');
      
      expect(buttonLogout.props().children).toBe('Logout');
      expect(buttonDashboard.props().children).toBe('Dashboard');
      expect(buttonAdmin.props().children).toBe('Admin');
    });
  });

  describe('User is logged out', () => {

    let component;
    beforeEach(() => component = shallow(<Appbar isloggedIn={false} />));

    it('should display logged out view', () => {
      const inputUsername = findByTestAttr(component, 'input-username');
      const inputPassword = findByTestAttr(component, 'input-password');
      
      expect(inputUsername.props().id).toBe('username');
      expect(inputPassword.props().id).toBe('password');
    })
  })
});