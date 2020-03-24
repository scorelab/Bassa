import { downloadActions } from '../constants';

const fetchDownloads = data => ({
  type: downloadActions.FETCH_DOWNLOADS,
  data
});

const addNewDownload = link => ({
  type: downloadActions.ADD_NEW_DOWNLOAD,
  link
});

const deleteDownload = id => ({
  type: downloadActions.DELETE_DOWNLOAD,
  id
});

const singleDownload = payload => ({
  type: downloadActions.SINGLE_DOWNLOAD,
  payload
});

const startAllDownloads = () => ({
  type: downloadActions.START_DOWNLOADS
})

const killAllDownloads = () => ({
  type: downloadActions.KILL_DOWNLOADS
})

export {
  fetchDownloads,
  addNewDownload,
  deleteDownload,
  singleDownload,
  startAllDownloads,
  killAllDownloads
}
