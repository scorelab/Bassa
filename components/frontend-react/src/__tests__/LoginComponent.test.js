/* eslint-disable no-undef */
import React from 'react';
import { mount } from 'enzyme';
import { BrowserRouter } from 'react-router-dom';

import LoginComponent from '../containers/LoginComponent';

const findByTestAttr = (component, attr) => {
  const wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
};

describe('Login Component', () => {
  let component;
  beforeEach(
    // eslint-disable-next-line no-return-assign
    () =>
      (component = mount(
        <BrowserRouter>
          <LoginComponent />
        </BrowserRouter>
      ))
  );

  it('should display appbar with not logged in view', () => {
    const wrapper = findByTestAttr(component, 'component-appbar');
    expect(wrapper.at(0).props().isloggedIn).toBe(false);
  });
});
