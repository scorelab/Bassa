import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import { object } from '@storybook/addon-knobs';

import CompletedFile from '../components/CompletedFile';

const fileObject = {
  id: '1',
  user: 'some_user_name',
  name: 'some_file_name',
  size: '120.23 KB',
  time: 'some_hours_ago'
};

export { fileObject as default };

storiesOf('CompletedFile', module).add('default', () => (
  <CompletedFile
    file={object('file', { ...fileObject })}
    onDownload={action('download')}
  />
));
