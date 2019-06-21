<template>
  <div class="ui secondary pointing menu">
    <div class="ui container">
      <router-link :to="{ name: 'home' }" exact class="item">Home</router-link>
      <router-link v-if="isAuthenticated" :to="{ name: 'hidden' }" class="item">hidden</router-link>
      <div class="right menu">
        <div v-if="isAuthenticated" @click="logout" class="item logout">Logout</div>
        <div v-else class="guestLinks">
          <router-link :to="{ name: 'login' }" class="item">Login</router-link>
          <router-link :to="{ name: 'register' }" class="item">Register</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  methods: {
    logout() {
      this.$store.dispatch('logout').then(() => {
        this.$router.replace("/");
      });
    }
  },
  computed: {
    ...mapGetters(["isAuthenticated",])
  }
};
</script>

<style scoped>
.guestLinks{
  display: flex
}
.logout{
  cursor: pointer;
}

.item{
  outline: none;
}
</style>