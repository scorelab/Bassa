import React from 'react';
import { mount } from 'enzyme';
import { BrowserRouter } from 'react-router-dom';

import LoginComponent from '../containers/LoginComponent';

const findByTestAttr = (component, attr) => {
  let wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
}

describe('Login Component', () => {
  let component;
  beforeEach(() => component = mount(<BrowserRouter><LoginComponent /></BrowserRouter>));

  it('should display appbar with not logged in view', () => {
    let wrapper = findByTestAttr(component, 'component-appbar');
    expect(wrapper.at(0).props().isloggedIn).toBe(false);
  });
})