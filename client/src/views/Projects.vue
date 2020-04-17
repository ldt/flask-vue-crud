<template>
  <div>
    <alert :message="alert.message" :dismissCountDown="alert.dismissCountDown"></alert>
    <b-container class="project-container">
      <b-row cols="3">
        <b-col>
          <b-card
            title="Start a new project"
            :img-src="require('@/assets/img/begin.jpeg')"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              click here to start
            </b-card-text>

            <b-button href="#" variant="success" v-b-modal.project-modal
              ><b-icon-file-plus></b-icon-file-plus> Create</b-button
            >
          </b-card>
        </b-col>
        <b-col v-for="p in projects" :key="p.id">
          <project-card :project="p" />
        </b-col>
        <b-col><project-card :project="{ title: 'MIAM', summary: 'research project' }"/></b-col>
        <b-col><project-card :project="{ title: 'KONE', summary: 'SMART prototype' }"/></b-col>
      </b-row>
    </b-container>
    <b-modal ref="addProjectModal" id="project-modal" title="Add a new project" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addProjectForm.title"
            required
            placeholder="Enter title"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-summary-group" label="Summary:" label-for="form-summary-input">
          <b-form-input
            id="form-summary-input"
            type="text"
            v-model="addProjectForm.summary"
            required
            placeholder="Enter summary"
          >
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import { BIconFilePlus } from "bootstrap-vue";

import Alert from "@/components/Alert.vue";
import ProjectCard from "@/components/ProjectCard.vue";

export default {
  data() {
    return {
      projects: [],
      addProjectForm: {
        title: "",
        summary: "",
        user_id: 1
      },
      alert: {
        message: "",
        dismissCountDown: 0
      }
    };
  },
  computed: {},
  methods: {
    async getProjects() {
      const path = "http://localhost:5000/project/";
      try {
        const response = await axios.get(path);
        this.projects = response.data.projects;
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
      }
    },
    async addProject(payload) {
      const path = "http://localhost:5000/project/";
      try {
        const response = await axios.post(path, payload);
        // eslint-disable-next-line
        console.log("add project response", response);
        this.alert.message = response.data.message;
        this.alert.dismissCountDown = 4;
        this.getProjects();
      } catch (error) {
        // eslint-disable-next-line
        console.log(error);
        this.getProjects();
      }
    },
    initForm() {
      this.addProjectForm.title = "";
      this.addProjectForm.summary = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addProjectModal.hide();
      const payload = {
        title: this.addProjectForm.title,
        summary: this.addProjectForm.summary,
        user_id: this.addProjectForm.user_id
      };
      // eslint-disable-next-line
      console.log("add project payload", payload);
      this.addProject(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addProjectModal.hide();
      this.initForm();
    }
  },
  created() {
    this.getProjects();
  },

  components: {
    ProjectCard,
    Alert,
    BIconFilePlus
  }
};
</script>

<style>
.project-container {
  margin-top: 90px;
}
</style>
