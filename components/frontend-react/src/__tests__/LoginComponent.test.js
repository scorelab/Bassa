import React from 'react';
import { shallow } from 'enzyme';

import LoginComponent from '../containers/LoginComponent';

const findByTestAttr = (component, attr) => {
  let wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
}

describe('Login Component', () => {
  let component;
  beforeEach(() => component = shallow(<LoginComponent/>));

  it('should display appbar with not logged in view', () => {
    let wrapper = findByTestAttr(component, 'component-appbar');
    expect(wrapper.props().isloggedIn).toBe(false);
  });
})