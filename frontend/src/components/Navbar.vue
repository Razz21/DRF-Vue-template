<template>
  <nav >
    <v-toolbar flat app>
      <v-toolbar-side-icon class="grey--text" @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>
        <router-link :to="{ name: 'home' }" class="text-uppercase grey--text">
          <span class="font-weight-light">page</span>
          <span>title</span>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items v-if="isAuthenticated">
        <v-btn flat color="grey" @click="logout">
          <span>Sign out</span>
          <v-icon right>exit_to_app</v-icon>
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-items v-else>
        <v-btn flat color="grey" :to="{ name: 'login' }">
          <span>Login</span>
        </v-btn>
        <v-btn flat color="indigo" :to="{ name: 'register' }">
          <span>Register</span>
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-navigation-drawer v-model="drawer" app >
      <p>test</p>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      drawer: false
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
    ...mapGetters(["isAuthenticated"])
  }
};
</script>

<style scoped>
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