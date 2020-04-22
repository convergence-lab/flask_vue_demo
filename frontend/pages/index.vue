<template>
  <v-layout column justify-center align-center>
    <v-col v-for="item in buttons" :key="item[0]">
      <v-btn>{{ item }}</v-btn>
    </v-col>
  </v-layout>
</template>

<script>
const url = "http://127.0.0.1:5000/";
export default {
  data() {
    return {
      buttons: {}
    };
  },
  mounted() {
    this.call_api();
  },
  methods: {
    call_api() {
      this.$axios.get(url).then(res => {
        this.buttons = res.data;
        console.log(this.buttons);
      });
    }
  }
};
</script>
