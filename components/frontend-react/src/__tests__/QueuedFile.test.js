/* eslint-disable no-undef */
import React from 'react';
import { shallow } from 'enzyme';
import QueuedFile from '../components/QueuedFile';

const clickDeleteFn = jest.fn();

const findByTestAttr = (component, attr) => {
  const wrapper = component.find(`[data-test='${attr}']`);
  return wrapper;
};

describe('Single queued file component', () => {
  let component;

  beforeEach(
    // eslint-disable-next-line no-return-assign
    () =>
      (component = shallow(
        <QueuedFile name="Name of the file" onDelete={clickDeleteFn()} />
      ))
  );

  it('should match with its snapshot', () => {
    expect(component).toMatchSnapshot();
  });

  it('should call onDelete function on button click', () => {
    const wrapper = findByTestAttr(component, 'button-delete');
    wrapper.simulate('click');
    expect(clickDeleteFn).toHaveBeenCalled();
  });
});
