import Vue from "vue";
import App from "./App.vue";
import VueOnToast from "vue-on-toast";
import VeeValidate from 'vee-validate';
import VueCookie from 'vue-cookie';
import Vuetify from 'vuetify'
import router from "./router";
import store from "./store";
import axios from 'axios';

Vue.use(Vuetify);
Vue.use(VeeValidate);
Vue.use(VueOnToast);
Vue.use(VueCookie);

Vue.config.productionTip = false;

// Vue.config.errorHandler = function(err, vm, info) {
//   console.log(`Error: ${err.toString()}\nInfo: ${info}`);
// }

// Vue.config.warnHandler = function(msg, vm, trace) {
//   console.log(`Warn: ${msg}\nTrace: ${trace}`);
// }




const vm =new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

export {vm}

// Django session authentication settings

const csrftoken = vm.$cookie.get('csrftoken');
// console.log(csrftoken)
axios.defaults.headers.common['X-CSRFToken'] = csrftoken;