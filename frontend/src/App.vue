<template>
  <div id="app">
    <toast-container :toastConfig="customConfig"></toast-container>
    <v-app>
        <Navbar />
        <v-content app>
          <v-container class="px-0">
          <router-view></router-view>
          </v-container>
        </v-content>
        <Footer />
    </v-app>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";

import { mapActions } from "vuex";

export default {
  name: "app",
  components: {
    Navbar,
    Footer
  },
  methods: mapActions(["loadUser"]),

  created() {
    this.loadUser();
  },
  computed: {
    customConfig() {
      return {
        positionClass: "vot-top-center",
        iconClasses: {
          error: "vot-icon-error",
          info: "vot-icon-info",
          wait: "ui active inline inverted loader",
          success: "vot-icon-success",
          warning: "vot-icon-warning"
        }
      };
    }
  }
};
</script>

<style >
@import url("~vue-on-toast/dist/vue-on-toast.css");
@import url("~vuetify/dist/vuetify.min.css");
#app{
  background: #fdfdfd
}

.toast-container {
  left: 50%;
  transform: translate(-50%);
}


.container{
  max-width: 900px !important
}
</style>
