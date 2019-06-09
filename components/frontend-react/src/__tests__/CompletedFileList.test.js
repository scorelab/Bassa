import React from 'react';
import { mount } from 'enzyme';
import CompletedFileList from '../containers/CompletedFileList';
import { completedList } from '../stories/CompletedFileList.stories';

const setupComponent = (props) => {
  const comp = mount(<CompletedFileList {...props} />);
  return comp;
}

const findByTestAttr = (component, attr) => {
  const wrappr = component.find(`[data-test='${attr}']`);
  return wrappr; 
} 

describe('List of complete downloaded files', () => {
  
  describe('When the list is loading', () => {
    it('should show loading message', () => {
      const component = setupComponent({ loading: true});
      const wrapper = findByTestAttr(component, 'text-loading');
      expect(wrapper.at(2).props().children).toBe('Loading...');
    });
  });

  describe('When the list is empty', () => {
    it('should show empty list message', () => {
      const component = setupComponent({files:[]})
      const wrapper = findByTestAttr(component, 'text-empty');
      expect(wrapper.at(2).props().children).toBe('No completed downloads');
    });
  });

  describe('When the list is loaded', () => {
    it('should display all the items in the list', () => {
      const component = setupComponent({files: completedList});
      const wrapper = findByTestAttr(component, 'element-item');
      //Since completedList had 4 items, so we expect files to be list of 4 items
      expect(wrapper.length).toBe(4);
    });
  });

  describe('When list is given a limit ', () => {
    it('should display limited list of the items', () => {
      const component = setupComponent({files: completedList, limit:2});
      const wrapper = findByTestAttr(component, 'element-item');
      //Since we added limit of 2, we render first 2 items from the list
      expect(wrapper.length).toBe(2);
    })
  })

})