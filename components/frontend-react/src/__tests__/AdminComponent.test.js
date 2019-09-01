/* eslint-disable no-undef */
/* eslint-disable no-return-assign */
import React from 'react';
import { shallow } from 'enzyme';
import AdminComponent from '../containers/AdminComponent';

describe('Admin component', () => {
  let component;
  beforeEach(() => (component = shallow(<AdminComponent />)));

  it('should display Appbar component', () => {
    expect(component.find(`[data-test='component-appbar']`).length).toEqual(1);
  });

  it('should display start/kill download component', () => {
    expect(
      component.find(`[data-test='component-start-kill-downloads']`).length
    ).toEqual(1);
  });

  it('should display pending signup requests', () => {
    expect(
      component.find(`[data-test='component-pending-signup-requests']`).length
    ).toEqual(1);
  });

  it('should display usage statistics', () => {
    expect(
      component.find(`[data-test='component-usage-statistics']`).length
    ).toEqual(1);
  });
});
