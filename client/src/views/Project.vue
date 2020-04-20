<template>
  <b-container>
    <h1>{{ currentProject.title }}</h1>
    <p>{{ currentProject.summary }}</p>

    <h2>Configuration</h2>
    <h3>Language</h3>
    <b-form-group label="Choose the language of the model">
      <b-form-radio v-model="language" name="model-language" value="EN-us">English</b-form-radio>
      <b-form-radio v-model="language" name="model-language" value="FR-fr">Français</b-form-radio>
    </b-form-group>

    <h3>Classes</h3>
    <div>
      <vue-tags-input
        v-model="tag"
        :tags="tags"
        :allow-edit-tags="true"
        @tags-changed="newTags => (tags = newTags)"
      />
    </div>
    <div>
      <h2>Test Zone</h2>
      <p>Insert here text editore configured with the classes set above</p>
    </div>
    <div class="mb-1">
      <b-button variant="danger" @click="showMsgBoxTwo">Delete</b-button>
      Return value: {{ String(boxTwo) }}
    </div>
  </b-container>
</template>

<script>
import { mapGetters } from "vuex";
import VueTagsInput from "@johmun/vue-tags-input";

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
    ...mapGetters(["currentProject", "alert"])
  },
  methods: {
    showMsgBoxTwo() {
      this.boxTwo = "";
      this.$bvModal
        .msgBoxConfirm("Please confirm that you want to delete this project.", {
          title: "Please Confirm",
          size: "sm",
          buttonSize: "sm",
          okVariant: "danger",
          okTitle: "YES",
          cancelTitle: "NO",
          footerClass: "p-2",
          hideHeaderClose: false,
          centered: true
        })
        .then(value => {
          this.boxTwo = value;
          // eslint-disable-next-line
          console.log("value", value, "was clicked");
        })
        .catch(err => {
          // eslint-disable-next-line
          console.err(err);
        });
    }
  },
  created() {
    this.$store.commit("SET_CURRENT_PROJECT", { id: this.id });
  },
  components: {
    VueTagsInput
  }
};
</script>

<style></style>
