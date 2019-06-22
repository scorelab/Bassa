import React from 'react';
import { shallow, mount } from 'enzyme';

import PendingSignupRequests from '../components/PendingSignupRequests';

import { requestsList } from '../stories/PendingSignupRequests.stories';

const findByTestAttr = (component, attr) => {
  const wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
}

const onApproveFn = jest.fn();

describe('PendingSignUpRequests component', () => {
  let component;
  beforeEach(() => component = shallow(<PendingSignupRequests requestsList={requestsList} onApprove={onApproveFn()}
   />));
  
  it('should list of requests', () => {
    let wrapper = findByTestAttr(component, 'item-requests');
    let mountedComp = mount(<PendingSignupRequests requestsList={requestsList} onApprove={onApproveFn()}
    />)
    let num_requests = mountedComp.props().requestsList.length
    //test that no. of requests passed as prop should be equal to number of request-items displayed 
    expect(num_requests).toEqual(wrapper.length);
  });

  it('should call onApprove function on tick button click', () => {
    let wrapper = findByTestAttr(component, 'button-approve');
    wrapper.at(0).simulate('click');
    expect(onApproveFn).toHaveBeenCalled();
  });
});