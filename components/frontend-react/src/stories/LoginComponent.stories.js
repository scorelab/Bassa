import React from 'react';
import { storiesOf } from '@storybook/react';

import LoginComponent from '../containers/LoginComponent';

storiesOf('Login Component', module)
.add('default', () => <LoginComponent/>)