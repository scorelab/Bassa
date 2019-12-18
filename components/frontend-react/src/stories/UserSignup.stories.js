import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import UserSignup from '../components/UserSignup';

storiesOf('User-Signup', module)
.add('default', () => <UserSignup onClickSubmit={action('submit')} />);