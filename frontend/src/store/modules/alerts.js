import { vm } from "@/main";
import { prepareAlertType } from "../utils";

const state = {
  messages: {},
  status: null,
  config: {}
};

const getters = {
  messages: state => state.messages,
  getType: state => state.color
};
const actions = {
  populateAlert: ({ commit }, data) => {
    if (!data['config']['color']) {
      data['config']["color"] = prepareAlertType(data.status);
    }
    commit("addAlert", data);
    commit("popAlert");
  }
};

const mutations = {
  addAlert: (state, data) => {
    Object.assign(state, data);
  },

  popAlert: state => {
    const msg = state.messages;
    for (let i in msg) {
      vm.$toast(msg[i]+'', { ...state.config });
    }
  }
};

export default {
  state,
  actions,
  getters,
  mutations
};
