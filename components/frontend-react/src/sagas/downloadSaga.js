import { take, takeEvery, put, call } from 'redux-saga/effects';
import {
  startAllDownloads,
  killAllDownloads,
  addNewDownload,
  fetchDownloads,
  deleteDownload
} from '../services/Downloads';
import { downloadActions } from '../constants';

function* startAllDownloadsWorkerSaga() {
  try {
    yield call(startAllDownloads);
    yield put({ type: 'STARTED_ALL_DOWNLOADS_SUCCESS' });
  } catch (error) {
    yield put({ type: 'ERROR_STARTING_DOWNLOADS' });
  }
  try {
    const files = yield call(fetchDownloads);
    yield put({ type: downloadActions.FETCH_DOWNLOADS, data: files.data });
  } catch (error) {
    yield put({ type: downloadActions.FETCH_DOWNLOADS_FAILED });
  }
}

function* killAllDownloadsWorkerSaga() {
  try {
    yield call(killAllDownloads);
    yield put({ type: 'KILLED_DOWNLOADS_SUCCESS' });
  } catch (error) {
    yield put({ type: 'FAILED_KILLING_DOWNLOADS' });
  }
  try {
    const files = yield call(fetchDownloads);
    yield put({ type: downloadActions.FETCH_DOWNLOADS, data: files.data });
  } catch (error) {
    yield put({ type: downloadActions.FETCH_DOWNLOADS_FAILED });
  }
}

function* addNewDownloadWorkerSaga(action) {
  try {
    yield call(addNewDownload, action.link);
  } catch (error) {
    yield put({ type: downloadActions.FAILED_ADDING_DOWNLOAD, error });
  }
  try {
    const files = yield call(fetchDownloads);
    yield put({ type: downloadActions.FETCH_DOWNLOADS, data: files.data });
  } catch (error) {
    yield put({ type: downloadActions.FETCH_DOWNLOADS_FAILED });
  }
}

function* deleteDownloadWorkerSaga(action) {
  try {
    yield call(deleteDownload, action.id);
    yield put({ type: 'DELETE_DOWNLOAD_SUCCESS' });
  } catch (error) {
    yield put({ type: 'FAILED_DELETING_DOWNLOAD' });
  }
  try {
    const files = yield call(fetchDownloads);
    yield put({ type: downloadActions.FETCH_DOWNLOADS, data: files.data });
  } catch (error) {
    yield put({ type: downloadActions.FETCH_DOWNLOADS_FAILED });
  }
}

function* startAllDownloadsWatcherSaga() {
  yield take(downloadActions.START_DOWNLOADS);
  yield call(startAllDownloadsWorkerSaga);
}

function* killAllDownloadsWatcherSaga() {
  yield take(downloadActions.KILL_DOWNLOADS);
  yield call(killAllDownloadsWorkerSaga);
}

function* addNewDownloadWatcherSaga() {
  yield takeEvery(downloadActions.ADD_NEW_DOWNLOAD, addNewDownloadWorkerSaga);
}

function* deleteDownloadWatcherSaga() {
  yield takeEvery(downloadActions.DELETE_DOWNLOAD, deleteDownloadWorkerSaga);
}
export {
  startAllDownloadsWatcherSaga,
  killAllDownloadsWatcherSaga,
  addNewDownloadWatcherSaga,
  deleteDownloadWatcherSaga
};
