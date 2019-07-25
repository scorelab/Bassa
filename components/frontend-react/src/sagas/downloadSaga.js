import { take, takeEvery, put, call } from 'redux-saga/effects';
import { startAllDownloads, killAllDownloads, addNewDownload, fetchDownloads, deleteDownload } from '../services/Downloads';
import { downloadActions } from '../constants';

function* startAllDownloadsWorkerSaga () {
  yield call(startAllDownloads);
}

function* killAllDownloadsWorkerSaga () {
  yield call(killAllDownloads);
  const files = yield call(fetchDownloads);
  yield put({type: downloadActions.FETCH_DOWNLOADS, data: files.data});
}

function* addNewDownloadWorkerSaga (action) {
  yield call(addNewDownload, action.link);
  const files = yield call(fetchDownloads);
  yield put({type: downloadActions.FETCH_DOWNLOADS, data: files.data});
}

function* deleteDownloadWorkerSaga (action) {
  yield call(deleteDownload, action.id);
  const files = yield call(fetchDownloads);
  yield put({type: downloadActions.FETCH_DOWNLOADS, data: files.data});
}

function* startAllDownloadsWatcherSaga () {
  yield take(downloadActions.START_DOWNLOADS);
  yield call(startAllDownloadsWorkerSaga);
}

function* killAllDownloadsWatcherSaga () {
  yield take(downloadActions.KILL_DOWNLOADS);
  yield call(killAllDownloadsWorkerSaga);
}

function* addNewDownloadWatcherSaga () {
  yield takeEvery(downloadActions.ADD_NEW_DOWNLOAD, addNewDownloadWorkerSaga);
}

function* deleteDownloadWatcherSaga () {
  yield takeEvery(downloadActions.DELETE_DOWNLOAD, deleteDownloadWorkerSaga);
}
export {
  startAllDownloadsWatcherSaga,
  killAllDownloadsWatcherSaga,
  addNewDownloadWatcherSaga,
  deleteDownloadWatcherSaga,
}