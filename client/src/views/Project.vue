<template>
  <div>
    <h1>{{ currentProject.name }} {{ id }}</h1>
    <p>{{ currentProject.summary }}</p>
    <div class="mb-1">
      <b-button variant="danger" @click="showMsgBoxTwo">Delete</b-button>
      Return value: {{ String(boxTwo) }}
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: {
    id: { type: String },
    project: {
      type: Object
    }
  },
  data() {
    return {
      boxTwo: ""
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
  }
};
</script>

<style></style>
