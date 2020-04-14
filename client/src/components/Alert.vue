<template>
  <div>
    <b-alert variant="success" :show="dismissCountDown" dismissible fade>{{ message }}</b-alert>
    <br />
  </div>
</template>

<script>
export default {
  props: {
    message: { default: "" },
    dismissCountDown: { default: 0 }
  },
  data() {
    return {};
  },
  methods: {}
};
</script>
