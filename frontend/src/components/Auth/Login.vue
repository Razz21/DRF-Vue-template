<template>
  <Form>
    <template #title>Login</template>

    <template #form>
      <ValidationObserver ref="observer" v-slot="{ valid }" tag="form" @submit.prevent="login">
        <ValidationProvider rules="required|max:10" name="username">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="username"
            label="Username"
          ></v-text-field>
        </ValidationProvider>
        <ValidationProvider rules="required" name="password">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="password"
            :append-icon="show ? 'visibility' : 'visibility_off'"
            :type="show ? 'text' : 'password'"
            label="Password"
            @click:append="show = !show"
          ></v-text-field>
        </ValidationProvider>
        <v-spacer></v-spacer>
        <p class="text-capitalize grey--text">
          Forgot
          <router-link :to="{ name: 'reset_password' }">Password?</router-link>
        </p>
        <v-card-text>
          <v-btn
            block
            color="info"
            type="submit"
            :disabled="!valid"
            :loading="authStatus=='loading'"
          >Login</v-btn>
        </v-card-text>
      </ValidationObserver>
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
import { ValidationObserver } from "vee-validate/dist/vee-validate.full";
export default {
  components: { Form, ValidationObserver },
  data() {
    return {
      show: false,
      username: "",
      password: "",
      errors: null
    };
  },
  methods: {
    login() {
      const isValid = this.$refs.observer.validate();
      console.log(isValid);
      if (isValid) {
        const { username, password } = this;
        this.$store.dispatch("login", { username, password });
        this.username = "";
        this.password = "";
      }
      requestAnimationFrame(() => {
        // https://baianat.github.io/vee-validate/guide/validation-observer.html#examples
        this.$refs.observer.reset();
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
