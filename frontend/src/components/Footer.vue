<template>
  <v-footer height="auto" color="#0F4559" style="z-index:12">
    <v-layout column row wrap class="align-center">
      <v-flex>
        <v-btn v-for="link in links" :key="link" class="white--text" text>{{ link }}</v-btn>
      </v-flex>
      <v-flex py-3 text-xs-center white--text xs12 class="#0F4559 darken-2 justify-center">
        &copy; {{ new Date().getFullYear() }} —
        MyPage
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
