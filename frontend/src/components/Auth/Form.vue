<template>
  <v-layout justify-center align-center>
    <v-flex xs12 sm7 md5>
      <v-card ref="form">
        <v-card-title primary-title class="justify-center card-title text-uppercase">
          <h4 class="headline white--text" color="white">
            <slot name="title"></slot>
          </h4>
        </v-card-title>
        <v-card-text>
          <slot name="text"></slot>
        </v-card-text>
        <v-card-text>
          <slot name="form"></slot>
        </v-card-text>

        <v-card-actions >
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
