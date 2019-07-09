<template>
  <Form>
    <template #title>Set new password</template>
    <!-- <template #text>Your Email address</template> -->
    <template #form>
      <v-form @submit.prevent="reset">
        <v-text-field
          v-model="new_password1"
          v-validate="'required'"
          :append-icon="show ? 'visibility' : 'visibility_off'"
          :type="show ? 'text' : 'password'"
          :error-messages="errors.collect('new_password1')"
          data-vv-name="new_password1"
          label="Password"
          @click:append="show = !show"
          ref="new_password1"
          required
        ></v-text-field>

        <v-text-field
          v-model="new_password2"
          v-validate="'required|confirmed:new_password1'"
          :append-icon="show1 ? 'visibility' : 'visibility_off'"
          :type="show1 ? 'text' : 'password'"
          :error-messages="errors.collect('new_password2')"
          data-vv-name="new_password2"
          label="Confirm password"
          hint="Type password again"
          @click:append="show1 = !show1"
          required
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-card-text>
          <v-btn  block color="info" type="submit" :loading="authStatus=='loading'">Submit</v-btn>
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
      new_password1: "",
      new_password2: "",
      uid: this.$route.params.uid,
      token: this.$route.params.token,
      show: false,
      show1: false,
      dictionary: {
        custom: {
          new_password1: {
            required: () => "This field is required"
          },
          new_password2: {
            required: () => "This field is required",
            confirmed: () => "Passwords did not match"
          }
        }
      }
    };
  },
  methods: {
    reset() {
      this.$validator.validateAll().then(result => {
        if (result) {
          const data = {
            new_password1:this.new_password1,
            new_password2:this.new_password2,
            uid: this.$route.params.uid,
            token: this.$route.params.token
          };
          this.$store.dispatch("confirmPassword", data);
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
