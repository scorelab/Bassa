import { userActions } from '../constants';

const initialState = {
  isloggedIn: false,
  username: 'sample',
  details: {},
  requests: [],
  stats: [],
};

const userReducer = (state = initialState, action) => {
  switch(action.type) {
    case userActions.AUTH_SUCCESS:
      return {...state, isloggedIn: true, username: action.username};

    case userActions.LOGOUT_USER:
      return {...state, isloggedIn: false};

    case userActions.ADD_NEW_USER:
      return {...state, details: action.details};

    case userActions.GET_SIGNUP_REQUESTS:
      return {...state, requests: action.users}

    case userActions.APPROVE_SIGNUP_REQUEST:
      return state;

    case userActions.FETCH_USERS_CONTRIBUTION:
      return {...state, stats: action.stats};

    default:
      return state;
  }
}

export default userReducer;