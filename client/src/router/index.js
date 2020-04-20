import Vue from "vue";
import VueRouter from "vue-router";
import Books from "@/components/Books.vue";
import Home from "@/views/Home.vue";

import store from "@/store";

Vue.use(VueRouter);
async function loadProjects(to, from, next) {
  if (!store.getters.projects) {
    await store.dispatch("loadProjects");
    next();
  }
}
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
    path: "/project/:id",
    name: "Project",
    props: true,
    beforeEnter: loadProjects,
    component: () => import(/* webpackChunkName: 'projects' */ "../views/Project.vue")
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
