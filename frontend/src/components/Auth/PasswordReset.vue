<template>
  <Form>
    <template #title>Forgot Password</template>
    <template #text>Type your email address</template>
    <template #form>
      <v-form @submit.prevent="reset">
        <v-text-field
          v-model="email"
          v-validate="'required|email'"
          type="email"
          :error-messages="errors.collect('email')"
          data-vv-name="email"
          label="Email"
          required
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-card-text>
          <v-btn block color="info" type="submit" :loading="authStatus=='loading'">Send</v-btn>
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
      email: ""
    };
  },
  methods: {
    reset() {
      this.$validator.validateAll().then(result => {
        if (result) {
          const { email } = this;
          this.$store.dispatch("resetPassword", { email });
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
