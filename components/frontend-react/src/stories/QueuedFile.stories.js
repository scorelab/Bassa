import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import { text } from '@storybook/addon-knobs';

import QueuedFile from '../components/QueuedFile';

storiesOf('QueuedFile', module)
.add('default', () => <QueuedFile index={0} name={text('name', 'abc.png')} onDelete={action('delete')}/>)