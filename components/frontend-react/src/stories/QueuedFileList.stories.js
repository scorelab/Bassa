import React from 'react';
import { storiesOf } from '@storybook/react';
import { array } from '@storybook/addon-knobs';

import QueuedFileList from '../containers/QueuedFileList';

export const dummyFiles = [
  'filename.png',
  'anotherfilename.jpg',
  'anotherfilename.mp4',
  'anotherfilename.gif'
]

storiesOf('QueuedList', module)
.add('empty', () => <QueuedFileList files={[]} />)
.add('loading', () => <QueuedFileList files={[]} loading={true} />)
.add('default', () => <QueuedFileList files={array('list', dummyFiles)} />)
.add('limited list', () => <QueuedFileList files={array('list', dummyFiles.slice(0,2))} limit={2} />)
