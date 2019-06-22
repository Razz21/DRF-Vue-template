
const Login = () => import("../components/Auth/Login.vue");
const Register = () => import("../components/Auth/Register.vue");

const PasswordReset = () => import("../components/Auth/PasswordReset.vue");
const PasswordResetCommit = () =>
  import("../components/Auth/PasswordResetCommit.vue");
const PasswordConfirm = () => import("../components/Auth/PasswordConfirm.vue");


export const authRoutes = [
  {
    path: "/login",
    component: Login,
    name: "login",
    meta: {
      guest: true
    }
  },
  {
    path: "/logout",
    name: "logout",
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/register",
    component: Register,
    name: "register",
    meta: {
      guest: true
    }
  },
  {
    path: "/password/reset",
    component: PasswordReset,
    name: "reset_password",
    meta: {
      guest: true
    }
  },
  {
    path: "/password/reset/commit",
    component: PasswordResetCommit,
    name: "reset_password_commit",
    meta: {
      guest: true
    }
  },
  {
    path: "/password/reset/confirm/:uid/:token",
    component: PasswordConfirm,
    name: "reset_password_confirm",
    meta: {
      guest: true
    }
  }
];
