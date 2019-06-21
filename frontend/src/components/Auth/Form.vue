<template>
  <v-layout justify-center>
    <v-flex xs12 sm8 md6 lg5>
      <v-card ref="form">
        <v-card-title primary-title class="justify-center card-title text-uppercase" py-4>
          <h4 class="display-1 white--text" color="white">
            <slot name="title"></slot>
          </h4>
        </v-card-title>
        <v-card-text>
          <slot name="text"></slot>
        </v-card-text>
        <v-card-text>
          <slot name="form"></slot>
        </v-card-text>

        <v-card-actions class="pa-3">
          <v-spacer></v-spacer>
          <slot name="action"></slot>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {};
</script>

<style>
.card-title {
  background: linear-gradient(40deg, #ffd86f, #fc6262) !important;
}
</style>
