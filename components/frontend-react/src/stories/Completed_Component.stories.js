import React from 'react';
import { storiesOf } from '@storybook/react';
import { object } from '@storybook/addon-knobs';

import completedList from './CompletedFileList.stories';
import Completed from '../containers/CompletedComponent';

storiesOf('Completed Component', module).add('default', () => (
  <Completed completedList={object('List', completedList)} />
));
