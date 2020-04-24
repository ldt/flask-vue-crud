<template>
  <b-container>
    <h1>{{ currentProject.name }}</h1>
    <p>{{ currentProject.summary }}</p>

    <b-row cols="2">
      <b-col>
        <h2><b-icon-tools /> Configuration</h2>
        <h3><b-icon-flag /> Language</h3>
        <b-form-group label="Choose the language of the model">
          <b-form-radio v-model="language" name="model-language" value="EN-us"
            >English</b-form-radio
          >
          <b-form-radio v-model="language" name="model-language" value="FR-fr"
            >Français</b-form-radio
          >
        </b-form-group>

        <h3><b-icon-tag-fill /> Classes</h3>
        <div>
          <vue-tags-input
            v-model="tag"
            :tags="tags"
            :allow-edit-tags="true"
            @tags-changed="handleTagsChanged"
            @before-deleting-tag="handleDeletionTag"
          />
        </div>
        <hr />
        <div class="mb-1">
          <b-button variant="danger" @click="showMsgBoxTwo">Delete</b-button>
        </div>
      </b-col>
      <b-col>
        <div>
          <h2><b-icon-file-text /> Test Zone</h2>
          <tiptap-ed />
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import { BIconTools, BIconFileText, BIconFlag, BIconTagFill } from "bootstrap-vue";
import VueTagsInput from "@johmun/vue-tags-input";
import TiptapEd from "@/components/TiptapEd.vue";
import _ from "lodash";

export default {
  props: {
    id: { type: String } // created by vue router
  },
  data() {
    return {
      language: "EN-us",
      boxTwo: "",
      tag: "",
      tags: []
    };
  },
  computed: {
    ...mapGetters(["currentProject"])
  },
  methods: {
    ...mapActions(["deleteProject", "updateProjectEntities", "deleteProjectEntity"]),
    handleTagsChanged(newTags) {
      const entities = _.map(newTags, "text");
      this.updateProjectEntities({
        projectId: this.currentProject.id,
        entities
      });
      this.tags = newTags;
    },
    handleDeletionTag(deletionTagData) {
      this.deleteProjectEntity({
        projectId: this.currentProject.id,
        entityName: deletionTagData.tag.text
      });
      deletionTagData.deleteTag();
    },
    async showMsgBoxTwo() {
      this.boxTwo = "";
      try {
        const value = await this.$bvModal.msgBoxConfirm(
          "Please confirm that you want to delete this project.",
          {
            title: "Please Confirm",
            size: "sm",
            buttonSize: "sm",
            okVariant: "danger",
            okTitle: "YES",
            cancelTitle: "NO",
            footerClass: "p-2",
            hideHeaderClose: false,
            centered: true
          }
        );
        this.boxTwo = value;
        if (value === true) {
          await this.deleteProject({ id: this.currentProject.id });
          this.$router.push({ path: "/projects" });
        }
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
      }
    }
  },
  created() {
    this.$store.commit("SET_CURRENT_PROJECT", { id: this.id });
  },
  mounted() {
    this.currentProject.entities.forEach(element => {
      this.tags.push({ text: element.name });
    });
  },
  components: {
    VueTagsInput,
    TiptapEd,
    BIconTools,
    BIconFileText,
    BIconFlag,
    BIconTagFill
  }
};
</script>

<style></style>
