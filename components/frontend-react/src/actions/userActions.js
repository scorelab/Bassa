import { userActions } from '../constants';

const verifyCredentials = creds => ({
  type: userActions.LOGIN_USER,
  creds
});

const logoutUser = () => ({
  type: userActions.LOGOUT_USER
})

const authSuccess = username => ({
  type: userActions.AUTH_SUCCESS,
  username
});

const addNewUser = details => ({
  type: userActions.ADD_NEW_USER,
  details
});

const getSignupRequests = users => ({
  type: userActions.GET_SIGNUP_REQUESTS,
  users
})

const approveSignupRequest = username => ({
  type: userActions.APPROVE_SIGNUP_REQUEST,
  username
});

const fetchUsersContribution = stats => ({
  type: userActions.FETCH_USERS_CONTRIBUTION,
  stats
})
export {
  verifyCredentials,
  logoutUser,
  authSuccess,
  addNewUser,
  getSignupRequests,
  approveSignupRequest,
  fetchUsersContribution
};