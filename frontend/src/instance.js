import axios from "axios";


const client = axios.create({
  baseURL: "/",
  // enable settings below, if you use DRF SessionAuthentication
  // xsrfCookieName: "csrftoken",
  // xsrfHeaderName: "X-CSRFToken",
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
