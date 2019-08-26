import Vue from "vue";
import App from "./App.vue";

import Vuetify from "vuetify";
import VuetifyToast from "vuetify-toast-snackbar";
import { ValidationProvider } from "./validate";

import router from "./router";
import store from "./store";

Vue.use(Vuetify);
const opts = { theme: { dark: false } };
Vue.use(VuetifyToast);

Vue.component("ValidationProvider", ValidationProvider);

Vue.config.productionTip = false;
window.EventBus = new Vue();

const vm = new Vue({
  vuetify: new Vuetify(opts),
  router,
  store,
  render: h => h(App)
}).$mount("#app");

export { vm };
