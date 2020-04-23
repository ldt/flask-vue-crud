<template>
  <b-card
    :title="project.name"
    :img-src="img_src"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      {{ project.summary }}
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
    project: { type: Object, default: null }
  },
  data() {
    return {};
  },
  computed: {
    img_src() {
      if (this.project.name) {
        const firstWord = this.project.name.split(" ")[0];
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
