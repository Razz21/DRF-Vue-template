<template>
  <div id="app">
    <v-app>
      <Navbar />
      <v-content>
        <v-layout>
          <v-container class="py-0" fill-height>
            <router-view></router-view>
          </v-container>
        </v-layout>
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
  }
};
</script>

<style >
@import url("~vuetify/dist/vuetify.min.css");

.container {
  max-width: 1200px;
}
</style>
