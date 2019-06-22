import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";
import alerts from "./modules/alerts";

import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: { auth, alerts, },
  plugins: [createPersistedState()]
});
