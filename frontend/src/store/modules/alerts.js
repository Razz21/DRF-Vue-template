import { vm } from "@/main";
import { prepareAlertType } from "../utils";

const state = {
  messages: {},
  status: null,
  type: null
};

const getters = {
  messages: state => state.messages,
  getType: state => state.type
};
const actions = {
  populateAlert: ({ commit }, config) => {
    // console.log(config);
    if (!config.type) {
      config["type"] = prepareAlertType(config.status);
    }
    commit("addAlert", config);
    commit("popAlert");
  }
};

const mutations = {
  addAlert: (state, config) => {
    Object.assign(state, config);
  },

  popAlert: state => {
    const msg = state.messages;
    
    for (let i in msg) {
      const title = i === "non_field_errors" ? "Error" : i;
      console.log(msg[i])
      vm.$vueOnToast.pop(state.type, title, msg[i]+'\n');
    }
  }
};

export default {
  state,
  actions,
  getters,
  mutations
};
