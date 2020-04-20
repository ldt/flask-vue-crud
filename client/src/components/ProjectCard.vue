<template>
  <b-card
    :title="title"
    :img-src="img_src"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      {{ summary }}
    </b-card-text>

    <b-button href="#" variant="primary">
      <b-icon-box-arrow-in-right></b-icon-box-arrow-in-right
      ><router-link :to="'/project/' + project.id">Enter</router-link></b-button
    >
  </b-card>
</template>

<script>
import { BIconBoxArrowInRight } from "bootstrap-vue";

export default {
  props: {
    description: { type: String, default: "" },
    project: { type: Object, default: null }
  },
  data() {
    return {};
  },
  computed: {
    title() {
      return this.project.title;
    },
    summary() {
      if (!this.project) return this.description;
      return this.project.summary;
    },
    img_src() {
      if (this.title) {
        const firstWord = this.title.split(" ")[0];
        return `https://picsum.photos/seed/${firstWord}/200/200`;
      }
      return `https://picsum.photos/200/200`;
    }
  },
  methods: {},
  components: {
    BIconBoxArrowInRight
  }
};
</script>

<style></style>
