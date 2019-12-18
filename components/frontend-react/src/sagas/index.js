/* eslint-disable import/prefer-default-export */
import { all } from 'redux-saga/effects';
import {
  userLoginWatcherSaga,
  addNewUserWatcherSaga,
  approveSignupRequestWatcherSaga
} from './userSaga';
import {
  startAllDownloadsWatcherSaga,
  killAllDownloadsWatcherSaga,
  addNewDownloadWatcherSaga,
  deleteDownloadWatcherSaga
} from './downloadSaga';

export function* rootSaga() {
  yield all([
    userLoginWatcherSaga(),
    addNewUserWatcherSaga(),
    approveSignupRequestWatcherSaga(),
    startAllDownloadsWatcherSaga(),
    killAllDownloadsWatcherSaga(),
    addNewDownloadWatcherSaga(),
    deleteDownloadWatcherSaga()
  ]);
}
