import Vue from "vue";
import App from "./App.vue";
import VueOnToast from "vue-on-toast";
import VeeValidate from "vee-validate";
import { Validator } from "vee-validate";
import Vuetify from "vuetify";

import router from "./router";
import store from "./store";
import axios from "./instance";

Vue.use(VueOnToast);
Vue.use(VeeValidate);
Vue.use(Vuetify);

const isUnique = value => {
  const body = JSON.stringify({ username: value });
  return axios
    .post("/api/auth/user/validate_username/", body)
    .then(res => {
      return { valid: !res.data.is_taken, data: { message: res.data.message } };
    })
    .catch(err => console.log(err));
};

Validator.extend("unique", {
  validate: isUnique,
  getMessage: (field, params, data) => {
    return data.message;
  }
});

Vue.config.productionTip = false;

const vm = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

export { vm };
