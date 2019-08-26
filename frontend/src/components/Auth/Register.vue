<template>
  <Form>
    <template #title>Sign up</template>
    <template #form>
      <ValidationObserver ref="observer" v-slot="{ valid }" tag="form" @submit.prevent="register">
        <ValidationProvider rules="required|unique" name="username">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="username"
            label="Username"
            counter
          ></v-text-field>
        </ValidationProvider>

        <ValidationProvider rules="required|min:8" name="password" vid="confirmation">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="password1"
            :loading="password1.length>4"
            counter
            :append-icon="show ? 'visibility' : 'visibility_off'"
            :type="show ? 'text' : 'password'"
            label="Password"
            hint="At least 8 characters"
            @click:append="show = !show"
          >
            <template v-slot:progress>
              <v-progress-linear
                v-if="password1.length"
                :value="progress"
                :color="color"
                height="3"
              ></v-progress-linear>
            </template>
          </v-text-field>
        </ValidationProvider>

        <ValidationProvider rules="required|confirmed:confirmation" name="password">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="password2"
            counter
            :append-icon="show1 ? 'visibility' : 'visibility_off'"
            :type="show1 ? 'text' : 'password'"
            label="Confirm password"
            hint="Type password again"
            @click:append="show1 = !show1"
          ></v-text-field>
        </ValidationProvider>

        <ValidationProvider rules="required|email" name="email">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="email"
            type="email"
            label="Email"
          ></v-text-field>
        </ValidationProvider>

        <v-card-text>
          <v-btn
            block
            color="info"
            :disabled="!valid"
            type="submit"
            :loading="authStatus=='loading'"
          >Sign up</v-btn>
        </v-card-text>
      </ValidationObserver>
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
import { ValidationObserver } from "vee-validate/dist/vee-validate.full";
export default {
  components: { Form, ValidationObserver },
  data() {
    return {
      valid: true,
      show: false,
      show1: false,
      username: "",
      password1: "",
      password2: "",
      email: ""
    };
  },
  methods: {
    register() {
      const isValid = this.$refs.observer.validate();
      if (isValid) {
        const { username, password1, password2, email } = this;
        this.$store.dispatch("register", {
          username,
          password1,
          password2,
          email
        });
        this.username = "";
        this.password1 = "";
        this.password2 = "";
        this.email = "";
        requestAnimationFrame(() => {
          // https://baianat.github.io/vee-validate/guide/validation-observer.html#examples
          this.$refs.observer.reset();
        });
      }
    }
  },
  computed: {
    ...mapGetters(["authStatus"]),
    passwordStrength() {
      const strongRegex = new RegExp(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})"
      );
      const mediumRegex = new RegExp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])");
      if (strongRegex.test(this.password1)) {
        return this.password1.length * 0.7;
      } else if (mediumRegex.test(this.password1)) {
        return this.password1.length * 0.4;
      } else {
        return this.password1.length * 0.1;
      }
    },
    progress() {
      if (this.password1.length >= 8) {
        return Math.min(100, this.passwordStrength * 10);
      }
      return 0;
    },
    color() {
      return ["error", "warning", "success"][Math.floor(this.progress / 40)];
    }
  }
};
</script>

<style>
</style>
