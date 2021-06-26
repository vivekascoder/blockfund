
<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered class="bg-secondary text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="@/assets/logo.png" />
          </q-avatar>
          BlockFund
        </q-toolbar-title>
        <q-btn flat dense icon="whatshot">About Us</q-btn>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";

export default {
  name: "LayoutDefault",
  components: {
  },

  setup() {
    return {
      leftDrawerOpen: ref(false),
    };
  },
};
</script>

<style >
/* @import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,400;1,500&display=swap'); */
* {
  font-family: 'Ubuntu', sans-serif;
}
</style>