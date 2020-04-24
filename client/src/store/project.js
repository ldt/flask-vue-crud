import Vue from "vue";
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
    currentEntities: state => {
      return state.currentProject.entities;
    }
  },
  mutations: {
    SET_PROJECTS(state, data) {
      state.projects = data.projects;
    },
    SET_CURRENT_PROJECT(state, data) {
      Vue.set(state, "currentProject", state.projects[data.id]);
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
    async addProject({ dispatch }, data) {
      try {
        const response = await axios.post(path, data);
        // eslint-disable-next-line
        console.log("add project response", response);
        dispatch("loadProjects");
      } catch (error) {
        // eslint-disable-next-line
        console.log(error);
      }
    },
    async deleteProject({ dispatch }, data) {
      try {
        const projectPath = `${path}${data.id}`;
        const response = await axios.delete(projectPath);
        // eslint-disable-next-line
        console.log("delete project back end response", response);
        // update the list of project
        dispatch("loadProjects");
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
      }
    },
    async updateProjectEntities({ commit, dispatch }, data) {
      try {
        const projectPath = `${path}${data.projectId}/entities`;
        await axios.post(projectPath, data);
        // console.log("updateProjectEntities", response);
        await dispatch("loadProjects");
        commit("SET_CURRENT_PROJECT", { id: data.projectId });
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
      }
    },
    async deleteProjectEntity({ commit, dispatch }, data) {
      try {
        const projectPath = `${path}${data.projectId}/entity/${data.entityName}`;
        await axios.delete(projectPath, data);
        // console.log("deleteProjectEntity", response);
        await dispatch("loadProjects");
        commit("SET_CURRENT_PROJECT", { id: data.projectId });
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
      }
    }
  } // end of actions
};
