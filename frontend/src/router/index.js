import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home.vue";
import store from "../store";
import { authRoutes } from "./auth";

Vue.use(VueRouter);

let routes = [
  { path: "/", name: "home", component: Home },
];

routes.push(...authRoutes);
routes.push({ path: "*", redirect: { name: "home" } });

const router = new VueRouter({
  mode: "history",
  base: "/",
  routes: routes,
  linkActiveClass: "active",
  linkExactActiveClass: "active"
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.guest)) {
    // access only for guests; redirect to home page if authenticated
    if (store.getters.isAuthenticated) {
      next({ name: "home" });
    } else {
      next();
    }
  } else if (to.matched.some(record => record.meta.requiresAuth)) {
    // access only for authenticated users
    if (!store.getters.isAuthenticated) {
      next({ name: "login", query: { redirect: to.fullPath.slice(1) } });
    } else next();
  } else next();
});

export default router;
