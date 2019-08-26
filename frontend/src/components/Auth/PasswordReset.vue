<template>
  <Form>
    <template #title>Forgot Password</template>
    <!-- <template #text>Type your email address</template> -->
    <template #form>
      <v-form @submit.prevent="sendResetRequest" ref="observer" v-model="valid">
        <ValidationProvider rules="required|email" name="password field" mode="aggressive">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="email"
            type="email"
            label="Email"
            required
          ></v-text-field>
        </ValidationProvider>
        <v-spacer></v-spacer>
        <v-card-text>
          <v-btn
            block
            :disabled="!valid"
            color="info"
            type="submit"
            :loading="authStatus=='loading'"
          >Send</v-btn>
        </v-card-text>
      </v-form>
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
      valid: false,
      email: ""
    };
  },
  methods: {
    sendResetRequest() {
      const isValid = this.$refs.observer.validate();
      if (isValid) {
        const { email } = this;
        this.$store.dispatch("resetPassword", { email });
      }
      this.email = "";
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
