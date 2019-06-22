import React from 'react';
import { shallow } from 'enzyme';
import CompletedFile from '../components/CompletedFile';

import { fileObject } from '../stories/CompletedFile.stories';

const clickDownloadFn = jest.fn();

const setupComponent = props => {
  const component = shallow(<CompletedFile {...props} />);
  return component;
}

const findByTestAttr = (component, attr) => {
  const wrapper = component.find(`[data-test='${attr}']`);
  return wrapper;
}

describe('Completed single file component', () => {
  it('should match with its snapshot', () => {
    const component = setupComponent({file: fileObject});
    expect(component).toMatchSnapshot();
  });
  
  it('should call onDownload function on click', () => {
    const component = setupComponent({file: fileObject, onDownload:clickDownloadFn()});
    const wrapper = findByTestAttr(component, 'button-download');
    wrapper.simulate('click');
    expect(clickDownloadFn).toHaveBeenCalled();
  })
});