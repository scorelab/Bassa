import { takeLatest, put, call, take } from 'redux-saga/effects';
import { userActions, downloadActions } from '../constants';
import { verifyUserCredentials, addNewUser, getSignupRequests, approveSignupRequest, getHeavyUsers } from '../services/Users';
import { fetchDownloads } from '../services/Downloads';

function* userLoginWorkerSaga (action) {
  const response = yield call(verifyUserCredentials, action);
  sessionStorage.setItem('token', response.headers.token);
  yield put({type: userActions.AUTH_SUCCESS, username: action.creds.username});
  const files = yield call(fetchDownloads);
  yield put({type: downloadActions.FETCH_DOWNLOADS, data: files.data});
  const users = yield call(getSignupRequests)
  yield put({type: userActions.GET_SIGNUP_REQUESTS, users: users.data})
  const stats = yield call(getHeavyUsers);
  yield put({type: userActions.FETCH_USERS_CONTRIBUTION, stats:stats.data});
}

function* addNewUserWorkerSaga (action) {
  yield call(addNewUser, action);
}

function* approveSignupRequestWorkerSaga (action) {
  yield call(approveSignupRequest, action);
  const users = yield call(getSignupRequests)
  yield put({type: userActions.GET_SIGNUP_REQUESTS, users: users.data})
}

function* userLoginWatcherSaga () {
  yield takeLatest(userActions.LOGIN_USER, userLoginWorkerSaga);
}

function* addNewUserWatcherSaga () {
  const action = yield take(userActions.ADD_NEW_USER);
  yield call(addNewUserWorkerSaga, action);
}

function* approveSignupRequestWatcherSaga () {
  const action = yield take(userActions.APPROVE_SIGNUP_REQUEST);
  yield call(approveSignupRequestWorkerSaga, action);
}

export {
  userLoginWatcherSaga,
  addNewUserWatcherSaga,
  approveSignupRequestWatcherSaga
};