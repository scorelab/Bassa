import { downloadActions } from '../constants';

const initialState = {
  completedDownloads: [],
  queuedDownloads: []
};

const userReducer = (state = initialState, action) => {
  switch(action.type) {

    case downloadActions.FETCH_DOWNLOADS:
      let completedList = action.data.filter(file => file.status === 3);
      let queuedList = action.data.filter(file => file.status === 0);
      return {...state, completedDownloads: completedList, queuedDownloads: queuedList}

    case downloadActions.ADD_NEW_DOWNLOAD:
      return state;

    case downloadActions.DELETE_DOWNLOAD:
      return state;

    case downloadActions.SINGLE_DOWNLOAD:
      console.log('downloading file ', action.payload);
      return state;

    case downloadActions.START_DOWNLOADS:
      return state;

    case downloadActions.KILL_DOWNLOADS:
      return state;

    default:
      return state;
  }
}

export default userReducer;