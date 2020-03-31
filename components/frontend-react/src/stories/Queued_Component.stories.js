import React from 'react';
import { storiesOf } from '@storybook/react';
import { array } from '@storybook/addon-knobs';

import dummyFiles from './QueuedFileList.stories';
import Queued from '../containers/QueuedComponent';

storiesOf('Queued Component', module).add('default', () => (
  <Queued queuedList={array('List', dummyFiles)} />
));
