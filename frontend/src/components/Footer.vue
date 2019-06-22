<template>
  <v-footer height="auto" color="#0F4559">
    <v-layout justify-center row wrap>
      <v-btn v-for="link in links" :key="link" dark color="gray" flat >{{ link }}</v-btn>
      <v-flex py-3 text-xs-center white--text xs12 class="#0F4559 darken-2 justify-center">
        &copy; {{ new Date().getFullYear() }} —
        Page
        <strong>Title</strong>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    links: ["Home", "About Us", "Team", "Services", "Blog", "Contact Us"]
  })
};
</script>

<style>
</style>
