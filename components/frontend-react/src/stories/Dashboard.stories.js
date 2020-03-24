import React from 'react';
import { storiesOf } from '@storybook/react';
import { object, array } from '@storybook/addon-knobs';

import completedList from './CompletedFileList.stories';
import dummyFiles from './QueuedFileList.stories';
import Dashboard from '../containers/Dashboard';

storiesOf('Dashboard', module).add('default', () => (
  <Dashboard
    completedList={object('Completed-List', completedList.slice(0, 2))}
    queuedList={array('Queued-List', dummyFiles.slice(0, 2))}
  />
));
