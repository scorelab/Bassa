import React from 'react';
import { storiesOf } from '@storybook/react';

import Appbar from '../components/Appbar';

storiesOf('Appbar', module)
  .add('loggedOff', () => <Appbar isloggedIn={false} />)
  .add('loggedIn', () => <Appbar isloggedIn />);
