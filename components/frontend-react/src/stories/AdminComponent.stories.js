import React from 'react';
import { storiesOf } from '@storybook/react';

import AdminComponent from '../containers/AdminComponent';

storiesOf('AdminComponent', module)
.add('default', () => <AdminComponent/>);