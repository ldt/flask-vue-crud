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
    dismissCountDown: { default: 1 }
  },
  data() {
    return {};
  },
  methods: {},
  created() {
    // eslint-disable-next-line
    console.log("alert created", this.message, this.dismissCountDown);
  }
};
</script>
