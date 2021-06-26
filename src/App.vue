
<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered class="bg-secondary text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-btn flat :to="{ name: 'Home' }">
            <q-avatar>
              <img src="@/assets/logo.png" />
            </q-avatar>
            <span class="q-ml-sm text-h6">
              BlockFund
            </span>
          </q-btn>
        </q-toolbar-title>
        <q-btn class="q-mx-sm" flat dense icon="add" :to="{name: 'AddCause'}">Add Cause</q-btn>
        <q-btn class="q-mx-sm" flat dense icon="flight_takeoff" to="/withdraw">Withdraw</q-btn>
        <q-btn class="q-mx-sm" flat dense icon="lightbulb" to="/about">About Us</q-btn>
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
  components: {},

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
  font-family: "Ubuntu", sans-serif;
}
</style>