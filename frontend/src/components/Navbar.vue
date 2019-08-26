<template>
  <v-app-bar flat app dense fixed style="z-index:10;align-items:start">
    <v-container style="display:flex" class="py-0" fill-height>
      <v-toolbar-title>
        <router-link :to="{ name: 'home' }" class="text-uppercase grey--text">
          <span class="font-weight-light">My</span>
          <span>page</span>
        </router-link>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items v-if="isAuthenticated">
        <v-btn text color="grey" @click="logout">
          <span v-if="$vuetify.breakpoint.smAndUp">Sign out</span>
          <v-icon right>exit_to_app</v-icon>
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-items v-else>
        <v-btn text color="grey" :to="{ name: 'login' }">
          <span>Login</span>
        </v-btn>
        <v-btn text color="#25aad9" :to="{ name: 'register' }">
          <span>Register</span>
        </v-btn>
      </v-toolbar-items>
    </v-container>
  </v-app-bar>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      drawer: false,
      Links: [{ title: "Profile", icon: "account_box", link: { name: "home" } }]
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => {
        this.$router.replace("/");
      });
    }
  },
  computed: {
    ...mapGetters(["isAuthenticated", "User"]),
    drawerIcon() {
      return this.isAuthenticated && this.$vuetify.breakpoint.xsOnly;
    }
  }
};
</script>

<style >
.guestLinks {
  display: flex;
}
.logout {
  cursor: pointer;
}

.item {
  outline: none;
}
</style>