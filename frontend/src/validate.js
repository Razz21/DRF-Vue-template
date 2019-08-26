import axios from "./instance";
import {
  ValidationProvider,
  extend
} from "vee-validate/dist/vee-validate.full";

const isUnique = value => {
  const body = JSON.stringify({ username: value });
  return axios
    .post("/api/auth/user/validate_username/", body)
    .then(res => {
      return { valid: !res.data.is_taken, data: { message: res.data.message } };
    })
    .catch(() => {
      // console.log(err);
      return true;
    });
};

extend("unique", {
  validate: isUnique,
  message: (_, params) => {
    return params.message;
  }
});

export { ValidationProvider };
