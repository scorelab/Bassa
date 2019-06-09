import React from 'react';
import { shallow } from 'enzyme';
import QueuedFile from '../components/QueuedFile';

const clickDeleteFn = jest.fn();

const setupComponent = props => {
  const component = shallow(<QueuedFile {...props} />)
  return component;
}

const findByTestAttr = (component, attr) => {
  const wrapper = component.find(`[data-test='${attr}']`);
  return wrapper;
}

describe('Single queued file component', () => {
  it('should match with its snapshot', () => {
    const component = setupComponent({name: 'Name of the file'});
    expect(component).toMatchSnapshot();
  });

  it('should call onDelete function on button click', () => {
    const component = setupComponent({name: 'Name of the file', onDelete: clickDeleteFn()});
    const wrapper = findByTestAttr(component, 'button-delete');
    wrapper.simulate('click');
    expect(clickDeleteFn).toHaveBeenCalled();
  })
})