import React from 'react';
import { storiesOf } from '@storybook/react';
import { object } from '@storybook/addon-knobs';

import { completedList } from './CompletedFileList.stories';
import Completed from '../containers/Completed';

storiesOf('Completed', module)
.add('default', () => <Completed completedList={object('List', completedList)} />)