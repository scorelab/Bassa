import { configure, addDecorator } from '@storybook/react';
import { withKnobs } from '@storybook/addon-knobs';

const req = require.context('../src/stories', true, /.stories.js$/);

addDecorator(withKnobs);

function loadStories() {
  req.keys().forEach(filename => req(filename));
}

configure(loadStories, module);
