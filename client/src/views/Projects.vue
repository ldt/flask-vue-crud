<template>
  <div>
    <!-- <alert :message="alert.message" :dismissCountDown="alert.dismissCountDown"></alert> -->
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
      </b-row>
    </b-container>
    <b-modal ref="addProjectModal" id="project-modal" title="Add a new project" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group" label="Title:" label-for="form-name-input">
          <b-form-input
            id="form-name-input"
            type="text"
            v-model="addProjectForm.name"
            required
            placeholder="Enter name"
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
import { BIconFilePlus } from "bootstrap-vue";

// import Alert from "@/components/Alert.vue";
import ProjectCard from "@/components/ProjectCard.vue";

import { mapGetters, mapActions } from "vuex";

export default {
  data() {
    return {
      addProjectForm: {
        name: "",
        summary: "",
        user_id: 1
      }
    };
  },
  computed: {
    ...mapGetters(["projects"])
  },
  methods: {
    ...mapActions(["loadProjects", "addProject"]),
    initForm() {
      this.addProjectForm.name = "";
      this.addProjectForm.summary = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addProjectModal.hide();
      const payload = {
        name: this.addProjectForm.name,
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
    this.loadProjects();
  },

  components: {
    ProjectCard,
    // Alert,
    BIconFilePlus
  }
};
</script>

<style>
.project-container {
  margin-top: 90px;
}
</style>
