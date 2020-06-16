import { userActions } from '../constants';

const initialState = {
  isUserAdmin: false,
  isloggedIn: false,
  hasAuthFailed: false,
  hasSignupFailed: false,
  hasSignupSuccessful: false,
  hasUserApprovalFailed: false,
  errorMessage: {},
  username: 'sample',
  details: {},
  requests: [],
  stats: []
};

const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case userActions.AUTH_SUCCESS:
      return { ...state, isloggedIn: true, username: action.username };

    case userActions.CHECK_ADMIN:
      if (action.payload === '0') {
        return { ...state, isUserAdmin: true };
      }
      return { ...state };

    case userActions.LOGOUT_USER:
      return { state: initialState, isloggedIn: false };

    case userActions.ADD_NEW_USER:
      return { ...state, details: action.details };

    case userActions.ADD_NEW_USER_FAILED:
      return { ...state, hasSignupFailed: true, errorMessage: action.error };

    case userActions.ADD_NEW_USER_SUCCESS:
      return { ...state, hasSignupSuccessful: true };

    case userActions.GET_SIGNUP_REQUESTS:
      return { ...state, requests: action.users };

    case userActions.AUTH_FAILURE:
      return { ...state, hasAuthFailed: true, errorMessage: action.error };

    case userActions.APPROVE_SIGNUP_REQUEST_FAILED:
      return {
        ...state,
        hasUserApprovalFailed: true,
        errorMessage: action.error
      };

    case userActions.APPROVE_SIGNUP_REQUEST:
      return state;

    case userActions.FETCH_USERS_CONTRIBUTION:
      return { ...state, stats: action.stats };

    default:
      return state;
  }
};

export default userReducer;
