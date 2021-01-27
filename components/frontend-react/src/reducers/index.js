import { combineReducers } from 'redux';

import userReducer from './userReducer';
import downloadReducer from './downloadReducer';

const rootReducer = combineReducers({
  userReducer,
  downloadReducer
})

export default rootReducer;