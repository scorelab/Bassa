/* eslint-disable no-undef */
import React from 'react';
import { shallow } from 'enzyme';

import UserSignup from '../components/UserSignup';

const onSubmitFn = jest.fn();

const findByTestAttr = (component, attr) => {
  const wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
};

describe('Signup Component', () => {
  let component;
  beforeEach(
    // eslint-disable-next-line no-return-assign
    () => (component = shallow(<UserSignup onClickSubmit={onSubmitFn()} />))
  );

  it('should display form with all the fields', () => {
    const fieldUsername = findByTestAttr(component, 'field-username');
    const fieldEmail = findByTestAttr(component, 'field-email');
    const fieldPassword = findByTestAttr(component, 'field-password');
    const fieldRePassword = findByTestAttr(component, 'field-re-password');
    const buttonSubmit = findByTestAttr(component, 'button-submit');

    expect(fieldEmail.length).toEqual(1);
    expect(fieldUsername.length).toEqual(1);
    expect(fieldPassword.length).toEqual(1);
    expect(fieldRePassword.length).toEqual(1);
    expect(buttonSubmit.length).toEqual(1);
  });

  it('should call onSubmit function on submit button click', () => {
    const buttonSubmit = findByTestAttr(component, 'button-submit');
    buttonSubmit.simulate('click');
    expect(onSubmitFn).toHaveBeenCalled();
  });
});
