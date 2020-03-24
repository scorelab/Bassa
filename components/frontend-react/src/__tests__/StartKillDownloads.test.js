/* eslint-disable no-undef */
import React from 'react';
import { shallow } from 'enzyme';

import StartKillDownloads from '../components/StartKillDownloads';

const findByTestAttr = (component, attr) => {
  const wrapper = component.find(`[data-test='${attr}']`);
  return wrapper;
};

const clickStartFn = jest.fn();
const clickKillFn = jest.fn();

describe('StartKillDownloads Component', () => {
  let component;
  beforeEach(
    // eslint-disable-next-line no-return-assign
    () =>
      (component = shallow(
        <StartKillDownloads
          onStart={() => clickStartFn()}
          onKill={() => clickKillFn()}
        />
      ))
  );

  it('should call onStart function on Start button click', () => {
    const button = findByTestAttr(component, 'button-start');
    button.simulate('click');
    expect(clickStartFn).toHaveBeenCalled();
  });

  it('should call onKill function on Kill button click', () => {
    const button = findByTestAttr(component, 'button-kill');
    button.simulate('click');
    expect(clickKillFn).toHaveBeenCalled();
  });
});
