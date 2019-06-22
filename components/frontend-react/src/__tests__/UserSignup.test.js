import React from 'react';
import { shallow } from 'enzyme';

import UserSignup from '../components/UserSignup';

const onSubmitFn = jest.fn();

const findByTestAttr = (component, attr) => {
  let wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
}

describe('Signup Component', () => {
 let component;
 beforeEach(() => component = shallow(<UserSignup onClickSubmit={onSubmitFn()}/>));

 it('should display form with all the fields', () => {
   let fieldUsername = findByTestAttr(component, 'field-username');
   let fieldEmail = findByTestAttr(component, 'field-email');
   let fieldPassword = findByTestAttr(component, 'field-password');
   let fieldRePassword = findByTestAttr(component, 'field-re-password');
   let buttonSubmit = findByTestAttr(component, 'button-submit');

   expect(fieldEmail.length).toEqual(1);
   expect(fieldUsername.length).toEqual(1);
   expect(fieldPassword.length).toEqual(1);
   expect(fieldRePassword.length).toEqual(1);
   expect(buttonSubmit.length).toEqual(1);

 });

 it('should call onSubmit function on submit button click', () => {
   let buttonSubmit = findByTestAttr(component, 'button-submit');
   buttonSubmit.simulate('click');
   expect(onSubmitFn).toHaveBeenCalled();
 })
})