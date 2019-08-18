import { takeLatest, put, call, take } from 'redux-saga/effects';
import { userActions, downloadActions } from '../constants';
import {
  verifyUserCredentials,
  addNewUser,
  getSignupRequests,
  approveSignupRequest,
  getHeavyUsers
} from '../services/Users';
import { fetchDownloads } from '../services/Downloads';

function* userLoginWorkerSaga(action) {
  try {
    const response = yield call(verifyUserCredentials, action);
    sessionStorage.setItem('token', response.headers.token);
    yield put({
      type: userActions.AUTH_SUCCESS,
      username: action.creds.username
    });
    yield put({ type: userActions.CHECK_ADMIN, payload: response.data.auth });
  } catch (error) {
    yield put({ type: userActions.AUTH_FAILURE, error });
  }
  try {
    const files = yield call(fetchDownloads);
    yield put({ type: downloadActions.FETCH_DOWNLOADS, data: files.data });
  } catch (error) {
    yield put({ type: 'FETCH_DOWNLOADS_FAILED' });
  }

  try {
    const users = yield call(getSignupRequests);
    yield put({ type: userActions.GET_SIGNUP_REQUESTS, users: users.data });
  } catch (error) {
    yield put({ type: 'GET_SIGNUP REQUESTS_FAILED' });
  }
  try {
    const stats = yield call(getHeavyUsers);
    yield put({
      type: userActions.FETCH_USERS_CONTRIBUTION,
      stats: stats.data
    });
  } catch (error) {
    yield put({ type: 'FETCH_USERS_CONTRI_FAILED' });
  }
}

function* addNewUserWorkerSaga(action) {
  try {
    yield call(addNewUser, action);
    yield put({ type: userActions.ADD_NEW_USER_SUCCESS });
  } catch (error) {
    yield put({ type: userActions.ADD_NEW_USER_FAILED, error });
  }
}

function* approveSignupRequestWorkerSaga(action) {
  try {
    yield call(approveSignupRequest, action);
    yield put({ type: userActions.APPROVE_SIGNUP_REQUEST_SUCCESS });
  } catch (error) {
    yield put({ type: userActions.APPROVE_SIGNUP_REQUEST_FAILED, error });
  }
  try {
    const users = yield call(getSignupRequests);
    yield put({ type: userActions.GET_SIGNUP_REQUESTS, users: users.data });
  } catch (error) {
    yield put({ type: 'GET_SIGNUP REQUESTS_FAILED' });
  }
}

function* userLoginWatcherSaga() {
  yield takeLatest(userActions.LOGIN_USER, userLoginWorkerSaga);
}

function* addNewUserWatcherSaga() {
  const action = yield take(userActions.ADD_NEW_USER);
  yield call(addNewUserWorkerSaga, action);
}

function* approveSignupRequestWatcherSaga() {
  const action = yield take(userActions.APPROVE_SIGNUP_REQUEST);
  yield call(approveSignupRequestWorkerSaga, action);
}

export {
  userLoginWatcherSaga,
  addNewUserWatcherSaga,
  approveSignupRequestWatcherSaga
};
