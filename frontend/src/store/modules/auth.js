import axios from "axios";
import { vm } from "../../main";
import { tokenConfig } from "../utils";

const state = {
  token: localStorage.getItem("token") || null,
  status: "",
  user: null
};

const getters = {
  isAuthenticated: state => !!state.user,
  authStatus: state => state.status
};

const actions = {
  loadUser({ commit }) {
    commit("auth_request");
    axios
      .get("api/auth/user/", tokenConfig(state))
      .then(resp => {
        commit("auth_success", resp.data);
      })
      .catch(err => {
        commit("auth_error");
      });
  },

  login({ commit, dispatch }, user) {
    commit("auth_request");
    axios
      .post("api/auth/login/", user, tokenConfig(state))
      .then(resp => {
        commit("login_success", resp.data);
        vm.$router.replace(vm.$route.query.redirect || { name: "home" });
      })
      .catch(err => {
        commit("auth_error");
        const errors = {
          // type:'error',
          messages: err.response.data,
          status: err.response.status
        };
        dispatch("populateAlert", errors);
      });
  },

  logout({ commit, dispatch }) {
    commit("auth_request");
    axios
      .post("api/auth/logout/", null, tokenConfig(state))
      .then(() => {
        commit("logout_success");
      })
      .catch(err => {
        commit("auth_error");
        const errors = {
          messages: err.response.data,
          status: err.response.status
        };
        dispatch("populateAlert", errors);
      });
  },

  register({ commit, dispatch }, user) {
    const body = JSON.stringify(user);
    commit("auth_request");
    axios
      .post("api/auth/register/", body, tokenConfig(state))
      .then(resp => {
        commit("register_success", resp.data);
        vm.$router.replace({ name: "home" });
      })
      .catch(err => {
        commit("auth_error");
        const errors = {
          messages: err.response.data,
          status: err.response.status
        };
        dispatch("populateAlert", errors);
      });
  },
  resetPassword({ commit, dispatch }, email) {
    const body = JSON.stringify(email);
    commit("auth_request");
    axios
      .post("api/auth/password/reset/", body, tokenConfig(state))
      .then(resp => {
        commit("password_reset_send");
        vm.$router.replace({ name: "reset_password_commit" });
      })
      .catch(err => {
        commit("auth_error");
        const errors = {
          messages: err.response.data,
          status: err.response.status
        };
        dispatch("populateAlert", errors);
      });
  },
  confirmPassword({ commit, dispatch }, data) {
    const body = JSON.stringify(data);
    commit("auth_request");
    axios
      .post("api/auth/password/reset/confirm/", body, tokenConfig(state))
      .then(resp => {
        commit("password_reset_success");
        console.log('resp',resp);
        // const msg = {
        //   status: resp.status,
        //   messages: resp.data
        // };
        // dispatch("populateAlert", msg);
        vm.$vueOnToast.pop("success", "Success", "Password has been reset with the new password.");
        vm.$router.replace({ name: "login" });
      })
      .catch(err => {
        commit("auth_error");
        const errors = {
          messages: err.response.data,
          status: err.response.status
        };
        dispatch("populateAlert", errors);
      });
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
