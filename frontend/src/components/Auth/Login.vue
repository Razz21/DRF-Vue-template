<template>
  <Form>
    <template #title>Login</template>

    <template #form>
      <v-form @submit.prevent="login">
        <v-text-field
          v-model="username"
          v-validate="'required'"
          :error-messages="errors.collect('username')"
          label="Username"
          data-vv-name="username"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          v-validate="'required'"
          :append-icon="show ? 'visibility' : 'visibility_off'"
          :type="show ? 'text' : 'password'"
          :error-messages="errors.collect('password')"
          data-vv-name="password"
          label="Password"
          @click:append="show = !show"
          required
        ></v-text-field>

        <v-spacer></v-spacer>
        
        <p class="text-capitalize grey--text">
          Forgot
          <router-link :to="{ name: 'reset_password' }">Password?</router-link>
        </p>

        <v-card-text>
          <v-btn block color="info" type="submit" :loading="authStatus=='loading'">Login</v-btn>
        </v-card-text>
      </v-form>
    </template>

    <template #action>
      <p class="text-capitalize grey--text">
        Need an account?
        <router-link :to="{ name: 'register' }">Sign up</router-link>
      </p>
    </template>
  </Form>
</template>

<script>
import Form from "./Form.vue";
import { mapGetters } from "vuex";
export default {
  components: { Form },
  data() {
    return {
      show: false,
      username: "",
      password: "",

    };
  },
  methods: {
    login() {
      this.$validator.validateAll().then(result => {
        if (result) {
          const { username, password } = this;
          this.$store.dispatch("login", { username, password });
        }
      });
    }
  },
  computed: {
    ...mapGetters(["authStatus"])
  }
};
</script>

<style>
</style>
