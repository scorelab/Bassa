/* eslint-disable no-undef */
import React from 'react';
import { mount } from 'enzyme';
import Dashboard from '../containers/Dashboard';
import completedList from '../stories/CompletedFileList.stories';
import dummyFiles from '../stories/QueuedFileList.stories';

describe('Dashboard Component', () => {
  let component;
  beforeEach(
    // eslint-disable-next-line no-return-assign
    () =>
      (component = mount(
        <Dashboard
          completedList={completedList.slice(0, 2)}
          queuedList={dummyFiles.slice(0, 2)}
        />
      ))
  );

  it('should display logged in view of Appbar', () => {
    const buttonLogout = component.find(`[data-test='button-logout']`);
    const buttonDashboard = component.find(`[data-test='button-dashboard']`);
    const buttonAdmin = component.find(`[data-test='button-admin']`);
    expect(buttonLogout.at(1).props().children).toBe('Logout');
    expect(buttonDashboard.at(1).props().children).toBe('Dashboard');
    expect(buttonAdmin.at(1).props().children).toBe('Admin');
  });
  it('should display limited list of queued and completed downloads', () => {
    const wrapper = component.find(`[data-test='element-item']`);
    expect(wrapper.length).toBe(4);
  });
});
