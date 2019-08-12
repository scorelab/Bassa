import React from 'react';
import { storiesOf } from '@storybook/react';
import { object } from '@storybook/addon-knobs';

import PendingSignupRequests from '../components/PendingSignupRequests';

export const requestsList = [
  {
    name: 'rush',
    email: 'rush@gmail.com'
  },
  {
    name: 'rome',
    email: 'rome@gmail.com'
  }
]

storiesOf('Pending Signup Requests', module)
.add('default', () => <PendingSignupRequests requestsList={object('list',requestsList)} />)