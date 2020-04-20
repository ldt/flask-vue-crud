import axios from "axios";
import _ from "lodash";

const path = "http://localhost:5000/project/";

export default {
  state: {
    projects: null,
    currentProject: null,
    alert: {
      message: "",
      dismissCountDown: 0
    }
  },
  getters: {
    projects: state => {
      return state.projects;
    },
    currentProject: state => {
      return state.currentProject;
    },
    alert: state => {
      return state.alert;
    }
  },
  mutations: {
    SET_PROJECTS(state, data) {
      state.projects = data.projects;
    },
    SET_CURRENT_PROJECT(state, data) {
      state.currentProject = state.projects[data.id];
    },
    SET_ALERT(state, data) {
      state.alert = data.alert;
    }
  },
  actions: {
    async loadProjects({ commit }) {
      try {
        const response = await axios.get(path);
        const projectDict = _.keyBy(response.data.projects, "id");
        commit("SET_PROJECTS", { projects: projectDict });
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
      }
    },
    async addProject({ commit, dispatch }, payload) {
      try {
        const response = await axios.post(path, payload);
        // eslint-disable-next-line
        console.log("add project response", response);
        commit("SET_ALERT", { message: response.data.message, dismissCountDown: 4 });
        dispatch("loadProjects");
      } catch (error) {
        // eslint-disable-next-line
        console.log(error);
      }
    }
  }
};
