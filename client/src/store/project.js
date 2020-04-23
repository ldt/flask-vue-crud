import axios from "axios";
import _ from "lodash";

const path = "http://0.0.0.0:5000/project/";

export default {
  state: {
    projects: null,
    currentProject: null
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
    async addProject({ dispatch }, payload) {
      try {
        const response = await axios.post(path, payload);
        // eslint-disable-next-line
        console.log("add project response", response);
        dispatch("loadProjects");
      } catch (error) {
        // eslint-disable-next-line
        console.log(error);
      }
    },
    async deleteProject({ dispatch }, payload) {
      try {
        const projectPath = `${path}${payload.id}`;
        const response = await axios.delete(projectPath);
        // eslint-disable-next-line
        console.log("delete project back end response", response);
        // update the list of project
        dispatch("loadProjects");
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
      }
    }
  }
};
