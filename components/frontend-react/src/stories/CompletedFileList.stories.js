import React from 'react';
import { storiesOf } from '@storybook/react';
import { object } from '@storybook/addon-knobs';

import CompletedFileList from '../containers/CompletedFileList';

const completedList = [
  {
    id: '1',
    user: 'some_user_name',
    name: 'some_file_name',
    size: '120.23 KB',
    time: 'some_days_ago'
  },
  {
    id: '2',
    user: 'some_user_name',
    name: 'some_file_name',
    size: '120.23 KB',
    time: 'some_hours_ago'
  },
  {
    id: '3',
    user: 'some_user_name',
    name: 'some_file_name',
    size: '120.23 KB',
    time: 'some_mins_ago'
  },
  {
    id: '4',
    user: 'some_user_name',
    name: 'some_file_name',
    size: '1320.23 KB',
    time: 'some_seconds_ago'
  }
];

export { completedList as default };

storiesOf('CompletedList', module)
  .add('default', () => (
    <CompletedFileList files={object('list', completedList)} />
  ))
  .add('limited list', () => (
    <CompletedFileList
      files={object('list', completedList.slice(0, 2))}
      limit={2}
    />
  ));
