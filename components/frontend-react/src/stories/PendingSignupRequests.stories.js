import React from 'react';
import { storiesOf } from '@storybook/react';
import { object } from '@storybook/addon-knobs';

import PendingSignupRequests from '../components/PendingSignupRequests';

const requestsList = [
  {
    name: 'rush',
    email: 'rush@gmail.com'
  },
  {
    name: 'rome',
    email: 'rome@gmail.com'
  }
];

export { requestsList as default };

storiesOf('Pending Signup Requests', module).add('default', () => (
  <PendingSignupRequests requestsList={object('list', requestsList)} />
));
