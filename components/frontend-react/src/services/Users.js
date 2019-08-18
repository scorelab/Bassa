import axios from 'axios';

// Log in the user
const verifyUserCredentials = action => {
  const formData = new FormData();
  formData.set('user_name', action.creds.username);
  formData.set('password', action.creds.password);
  return axios.post(`${process.env.REACT_APP_API_POST_LOGIN}`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
};

const addNewUser = action => {
  return axios.post(
    `${process.env.REACT_APP_API_ADD_NEW_USER}`,
    action.details,
    { headers: { 'Content-Type': 'multipart/form-data' } }
  );
};

const getSignupRequests = () => {
  const token = sessionStorage.getItem('token');
  return axios.get(`${process.env.REACT_APP_API_GET_SIGNUP_REQUESTS}`, {
    headers: { token: `${token}` }
  });
};

const approveSignupRequest = action => {
  const token = sessionStorage.getItem('token');
  return axios.post(
    `${process.env.REACT_APP_API_APPROVE_SIGNUP_REQUEST}/${action.username}`,
    action.username,
    { headers: { token: `${token}` } }
  );
};

const getHeavyUsers = () => {
  const token = sessionStorage.getItem('token');
  return axios.get(`${process.env.REACT_APP_API_GET_HEAVY_USERS}`, {
    headers: { token: `${token}` }
  });
};

export {
  verifyUserCredentials,
  addNewUser,
  getSignupRequests,
  approveSignupRequest,
  getHeavyUsers
};
