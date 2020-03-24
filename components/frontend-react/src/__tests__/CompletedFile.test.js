/* eslint-disable no-undef */
import React from 'react';
import { shallow } from 'enzyme';
import CompletedFile from '../components/CompletedFile';

import fileObject from '../stories/CompletedFile.stories';

const clickDownloadFn = jest.fn();

const findByTestAttr = (component, attr) => {
  const wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
};

describe('Completed single file component', () => {
  let component;
  beforeEach(
    // eslint-disable-next-line no-return-assign
    () =>
      (component = shallow(
        <CompletedFile file={fileObject} onDownload={clickDownloadFn()} />
      ))
  );

  it('should match with its snapshot', () => {
    expect(component).toMatchSnapshot();
  });

  it('should call onDownload function on click', () => {
    const wrapper = findByTestAttr(component, 'button-download');
    wrapper.simulate('click');
    expect(clickDownloadFn).toHaveBeenCalled();
  });
});
