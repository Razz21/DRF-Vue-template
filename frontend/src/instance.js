import axios from "axios";

const client = axios.create({
  baseURL: "http://127.0.0.1:8000",
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
  headers:{
    "Content-Type":"application/json",
  },
  
});

client.defaults.headers.post["Accept"] = "application/json";

client.CancelToken = axios.CancelToken;
client.isCancel = axios.isCancel;

client.interceptors.request.use(
  config => {
    let token = localStorage.getItem("token") || null;
    if (token) {
      config.headers["Authorization"] = `Token ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default client;
