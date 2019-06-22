<template>
  <nav style="z-index:10">
    <v-toolbar flat app prominent>
      <v-toolbar-side-icon v-if="isAuthenticated" class="grey--text" @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>
        <router-link :to="{ name: 'home' }" class="text-uppercase grey--text">
          <span class="font-weight-light">page</span>
          <span>title</span>
        </router-link>
      </v-toolbar-title>

      <v-spacer></v-spacer>
      
      <v-toolbar-items v-if="isAuthenticated">
        <v-btn flat color="grey" @click="logout">
          <span v-if="$vuetify.breakpoint.smAndUp">Sign out</span>
          <v-icon right>exit_to_app</v-icon>
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-items v-else>
        <v-btn flat color="grey" :to="{ name: 'login' }">
          <span>Login</span>
        </v-btn>
        <v-btn flat color="#25aad9" :to="{ name: 'register' }">
          <span>Register</span>
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>

     <v-navigation-drawer v-model="drawer" app v-if="isAuthenticated">
      <v-layout column align-center>
        <v-flex class="mt-5">
          <v-avatar size="100">
            <img src="https://randomuser.me/api/portraits/men/9.jpg" />
          </v-avatar>
          <p class="subheading mt-2">{{User.username}}</p>
        </v-flex>
      </v-layout>

      <v-list class="pt-1">
        <v-list-tile v-for="item in Links" :key="item.title" exact router :to="item.link">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

  </nav>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      drawer: false,
       Links: [
        { title: "Profile", icon: "account_box", link: { name: "home" } }
      ]
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => {
        this.$router.replace("/");
      });
    },
  },
  computed: {
    ...mapGetters(["isAuthenticated", "User"]),
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