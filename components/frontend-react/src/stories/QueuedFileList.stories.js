import React from 'react';
import { storiesOf } from '@storybook/react';

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
.add('default', () => <QueuedFileList files={dummyFiles} />)
.add('limited list', () => <QueuedFileList files={dummyFiles} limit={2} />)
