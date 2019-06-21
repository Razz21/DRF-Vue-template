<template>
  <Form>
    <template #title>Sign up</template>
    <template #form>
      <v-form @submit.prevent="register">
        <v-text-field
          v-model="username"
          v-validate="'required|max:10'"
          :counter="10"
          :error-messages="errors.collect('username')"
          label="Username"
          data-vv-name="username"
          required
        ></v-text-field>

        <v-text-field
          v-model="password1"
          v-validate="'required|min:5'"
          counter
          :append-icon="show ? 'visibility' : 'visibility_off'"
          :type="show ? 'text' : 'password'"
          :error-messages="errors.collect('password1')"
          data-vv-name="password1"
          label="Password"
          hint="At least 5 characters"
          @click:append="show = !show"
          ref="password1"
          required
        ></v-text-field>

        <v-text-field
          v-model="password2"
          v-validate="'required|confirmed:password1'"
          counter
          :append-icon="show1 ? 'visibility' : 'visibility_off'"
          :type="show1 ? 'text' : 'password'"
          :error-messages="errors.collect('password2')"
          data-vv-name="password2"
          label="Confirm password"
          hint="Type password again"
          @click:append="show1 = !show1"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          v-validate="'required|email'"
          type="email"
          :error-messages="errors.collect('email')"
          data-vv-name="email"
          label="Email"
          required
        ></v-text-field>

        <v-checkbox
          v-model="terms"
          v-validate="'required'"
          :error-messages="errors.collect('terms')"
          value="1"
          data-vv-name="terms"
          type="checkbox"
          label="Accept the Terms and Conditions"
          required
        ></v-checkbox>
        <v-card-text>
          <v-btn block large color="info" type="submit" :loading="authStatus=='loading'">Sign up</v-btn>
        </v-card-text>
      </v-form>
    </template>

    <template #action>
      <p class="text-capitalize grey--text">
        Have an account?
        <router-link :to="{ name: 'login' }">Login</router-link>
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
      show1: false,
      username: "",
      password1: "",
      password2: "",
      email: "",
      terms: null,
      dictionary: {
        custom: {
          terms: {
            required: () => "You must agree to continue"
          },
          password1: {
            required: () => "This field is required",
            min: () => "Password must be at least 5 characters long",
          },
          password2: {
            confirmed: () => "Passwords did not match",
            required: () => "This field is required",
          }
        }
      }
    };
  },
  methods: {
    register() {
      this.$validator.validateAll().then(result => {
        if (result) {
          const { username, password1, password2, email } = this;
          this.$store.dispatch("register", {
            username,
            password1,
            password2,
            email
          });
        }
      });
    }
  },
  computed: {
    ...mapGetters(["authStatus"])
  },
  mounted() {
    this.$validator.localize("en", this.dictionary);
  }
};
</script>

<style>
</style>
