/* eslint-disable no-undef */
/* eslint-disable no-return-assign */
import React from 'react';
import { mount } from 'enzyme';
import CompletedFileList from '../containers/CompletedFileList';
import completedList from '../stories/CompletedFileList.stories';

const findByTestAttr = (component, attr) => {
  const wrappr = component.find(`[data-test='${attr}']`);
  return wrappr;
};

describe('List of complete downloaded files', () => {
  describe('When the list is loading', () => {
    let component;
    beforeEach(() => (component = mount(<CompletedFileList loading />)));

    it('should show loading message', () => {
      const wrapper = findByTestAttr(component, 'text-loading');
      expect(wrapper.at(2).props().children).toBe('Loading...');
    });
  });

  describe('When the list is empty', () => {
    let component;
    beforeEach(() => (component = mount(<CompletedFileList files={[]} />)));

    it('should show empty list message', () => {
      const wrapper = findByTestAttr(component, 'text-empty');
      expect(wrapper.at(2).props().children).toBe('No completed downloads');
    });
  });

  describe('When the list is loaded', () => {
    let component;
    beforeEach(
      () => (component = mount(<CompletedFileList files={completedList} />))
    );

    it('should display all the items in the list', () => {
      const wrapper = findByTestAttr(component, 'element-item');
      // Since completedList had 4 items, so we expect files to be list of 4 items
      expect(wrapper.length).toBe(4);
    });
  });

  describe('When list is given a limit ', () => {
    let component;
    beforeEach(
      () =>
        (component = mount(
          <CompletedFileList files={completedList} limit={2} />
        ))
    );

    it('should display limited list of the items', () => {
      const wrapper = findByTestAttr(component, 'element-item');
      // Since we added limit of 2, we render first 2 items from the list
      expect(wrapper.length).toBe(2);
    });
  });
});
