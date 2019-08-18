/* eslint-disable import/prefer-default-export */
import { applyMiddleware, compose, createStore } from 'redux';
import createSagaMiddleware from 'redux-saga';
import rootReducer from './reducers';
import { rootSaga } from './sagas';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const initialState = {};

export const configureStore = () => {
  const sagaMiddleware = createSagaMiddleware();

  const getMiddleware = () => {
    return applyMiddleware(sagaMiddleware);
  };

  const store = createStore(
    rootReducer,
    initialState,
    composeEnhancers(getMiddleware())
  );

  sagaMiddleware.run(rootSaga);

  return store;
};
