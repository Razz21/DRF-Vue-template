<template>
  <Form>
    <template #title>Set new password</template>
    <!-- <template #text>Your Email address</template> -->
    <template #form>
      <ValidationObserver ref="observer" v-slot="{ valid }" tag="form" @submit.prevent="reset">
        <ValidationProvider rules="required|min:8" name="password" vid="confirmation">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="new_password1"
            counter
            :append-icon="show ? 'visibility' : 'visibility_off'"
            :type="show ? 'text' : 'password'"
            label="Password"
            hint="At least 8 characters"
            @click:append="show = !show"
          ></v-text-field>
        </ValidationProvider>

        <ValidationProvider rules="required|confirmed:confirmation" name="password">
          <v-text-field
            slot-scope="{errors}"
            :error-messages="errors"
            v-model="new_password2"
            counter
            :append-icon="show1 ? 'visibility' : 'visibility_off'"
            :type="show1 ? 'text' : 'password'"
            label="Confirm password"
            hint="Type password again"
            @click:append="show1 = !show1"
          ></v-text-field>
        </ValidationProvider>
        <v-spacer></v-spacer>
        <v-card-text>
          <v-btn
            type="submit"
            color="info"
            :disabled="!valid"
            block
            :loading="authStatus=='loading'"
          >Submit</v-btn>
        </v-card-text>
      </ValidationObserver>
    </template>
  </Form>
</template>

<script>
import Form from "./Form.vue";
import { ValidationObserver } from "vee-validate/dist/vee-validate.full";
import { mapGetters } from "vuex";
export default {
  components: { Form, ValidationObserver },
  data() {
    return {
      new_password1: "",
      new_password2: "",
      show: false,
      show1: false
    };
  },
  methods: {
    reset() {
      const isValid = this.$refs.observer.validate();
      if (isValid) {
        const data = {
          new_password1: this.new_password1,
          new_password2: this.new_password2,
          uid: this.$route.params.uid,
          token: this.$route.params.token
        };
        this.$store.dispatch("confirmPassword", data);
      }
      this.new_password1 = "";
      this.new_password2 = "";
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
