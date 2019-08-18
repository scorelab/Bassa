import axios from 'axios';

const fetchDownloads = () => {
  const token = sessionStorage.getItem('token');
  return axios.get(`${process.env.REACT_APP_API_GET_DOWNLOADS}`, {
    headers: { token: `${token}` }
  });
};

const startAllDownloads = () => {
  return axios.get(`${process.env.REACT_APP_API_START_DOWNLOADS}`, {
    headers: { key: '123456789' }
  });
};

const killAllDownloads = () => {
  return axios.get(`${process.env.REACT_APP_API_KILL_DOWNLOADS}`, {
    headers: { key: '123456789' }
  });
};

const addNewDownload = link => {
  const obj = { link };
  const token = sessionStorage.getItem('token');
  JSON.stringify(obj);
  return axios.post(`${process.env.REACT_APP_API_DOWNLOAD}`, obj, {
    headers: { 'Content-Type': 'multipart/form-data', token: `${token}` }
  });
};

const deleteDownload = id => {
  const token = sessionStorage.getItem('token');
  return axios.delete(`${process.env.REACT_APP_API_DOWNLOAD}/${id}`, {
    headers: { token: `${token}` }
  });
};

export {
  fetchDownloads,
  startAllDownloads,
  killAllDownloads,
  addNewDownload,
  deleteDownload
};
