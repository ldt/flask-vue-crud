import Vue from "vue";
import Vuex from "vuex";

import project from "@/store/project";

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== "production";

const state = {};

export default new Vuex.Store({
  state,
  modules: {
    project
  },
  strict: debug
});
