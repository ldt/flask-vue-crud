import Vue from "vue";
import VueRouter from "vue-router";
import Books from "@/components/Books.vue";
import Home from "@/views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/projects",
    name: "Projects",
    component: () => import(/* webpackChunkName: 'projects' */ "../views/Projects.vue")
  },
  {
    path: "/books",
    name: "Books",
    component: Books
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
