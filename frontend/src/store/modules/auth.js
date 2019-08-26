import axios from "@/instance";
import { vm } from "@/main";
// import { tokenConfig } from "../utils";

const state = {
  token: localStorage.getItem("token") || null,
  status: "",
  user: null
};

const getters = {
  isAuthenticated: state => !!state.user && !!state.token,
  authStatus: state => state.status,
  User: state => state.user
};

const actions = {
  loadUser({ commit }) {
    commit("auth_request");
    axios
      .get("/api/auth/user/")
      .then(resp => {
        commit("auth_success", resp.data);
      })
      .catch(() => {
        commit("auth_error");
      });
  },

  login({ commit, dispatch }, user) {
    commit("auth_request");
    axios
      .post("/api/auth/login/", user)
      .then(resp => {
        commit("login_success", resp.data);
        vm.$router.replace(vm.$route.query.redirect || { name: "home" });
      })
      .catch(err => {
        dispatch("authAlert", err);
      });
  },

  logout({ commit, dispatch }) {
    commit("auth_request");
    axios
      .post("/api/auth/logout/", null)
      .then(() => {
        commit("logout_success");
        vm.$disconnect();
      })
      .catch(err => {
        dispatch("authAlert", err);
      });
  },

  register({ commit, dispatch }, user) {
    const body = JSON.stringify(user);

    commit("auth_request");
    axios
      .post("/api/auth/register/", body)
      .then(resp => {
        commit("register_success", resp.data);
        vm.$router.replace({ name: "home" });
      })
      .catch(err => {
        dispatch("authAlert", err);
      });
  },
  resetPassword({ commit, dispatch }, email) {
    const body = JSON.stringify(email);
    commit("auth_request");
    axios
      .post("/api/auth/password/reset/", body)
      .then(() => {
        commit("password_reset_send");
        vm.$router.replace({ name: "reset_password_commit" });
      })
      .catch(err => {
        dispatch("authAlert", err);
      });
  },
  confirmPassword({ commit, dispatch }, data) {
    const body = JSON.stringify(data);
    commit("auth_request");
    axios
      .post("/api/auth/password/reset/confirm/", body)
      .then(() => {
        commit("password_reset_success");
        vm.$router.replace({ name: "login" });
      })
      .catch(err => {
        dispatch("authAlert", err);
      });
  },

  authAlert({ commit, dispatch }, data) {
    commit("auth_error");
    const alert = {
      messages: data.response.data,
      status: data.response.status,
      config: { x: "right", y: "top", queueable: true }
    };
    dispatch("populateAlert", alert);
  }
};

const mutations = {
  auth_request(state) {
    state.status = "loading";
  },

  auth_success(state, payload) {
    state.status = "success";
    state.user = payload;
  },

  auth_error(state) {
    localStorage.removeItem("token");
    state.status = "error";
    state.token = null;
    state.user = null;
  },

  login_success(state, payload) {
    const { token, user } = payload;
    localStorage.setItem("token", token);
    state.status = "success";
    state.token = token;
    state.user = user;
  },

  register_success(state, payload) {
    const { token, user } = payload;
    localStorage.setItem("token", token);
    state.status = "success";
    state.token = token;
    state.user = user;
  },

  logout_success(state) {
    localStorage.removeItem("token");
    state.status = "";
    state.token = null;
    state.user = null;
  },
  password_reset_send(state) {
    state.status = "reset_password";
  },
  password_reset_success(state) {
    state.status = "reset_password_success";
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
