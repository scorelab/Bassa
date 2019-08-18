/* eslint-disable no-case-declarations */
import { userActions, downloadActions } from '../constants';

const initialState = {
  completedDownloads: [],
  queuedDownloads: [],
  haveDownloadsStarted: false,
  haveDownloadsKilled: false,
  haveFetchingDownloadsFailed: false,
  hasAddingDownloadFailed: false,
  errorMessage: ''
};

const QUEUED = 0;
const DOWNLOADING = 3;

const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case downloadActions.FETCH_DOWNLOADS:
      const completedList = action.data.filter(
        file => file.status === DOWNLOADING
      );
      const queuedList = action.data.filter(file => file.status === QUEUED);
      return {
        ...state,
        completedDownloads: completedList,
        queuedDownloads: queuedList
      };

    case downloadActions.ADD_NEW_DOWNLOAD:
      return state;

    case userActions.LOGOUT_USER:
      return {
        ...state,
        haveDownloadsStarted: false,
        haveDownloadsKilled: false,
        haveFetchingDownloadsFailed: false,
        hasAddingDownloadFailed: false,
        errorMessage: ''
      };

    case downloadActions.FETCH_DOWNLOADS_FAILED:
      return { ...state, haveFetchingDownloadsFailed: true };

    case downloadActions.FAILED_ADDING_DOWNLOAD:
      return {
        ...state,
        hasAddingDownloadFailed: true,
        errorMessage: action.error.message
      };

    case downloadActions.DELETE_DOWNLOAD:
      return state;

    case downloadActions.SINGLE_DOWNLOAD:
      // console.log('downloading file ', action.payload);
      return state;

    case downloadActions.START_DOWNLOADS:
      return { ...state, haveDownloadsStarted: true };

    case downloadActions.KILL_DOWNLOADS:
      return { ...state, haveDownloadsKilled: true };

    default:
      return state;
  }
};

export default userReducer;
