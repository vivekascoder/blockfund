<template>
  <div class="row q-mt-lg flex justify-center p-mx-sm">
    <div class="col-8">
      <div class="row">
        <div v-for="cause in causes" :key="cause.id" class="col-6">
          <q-card class="my-card bg-secondary text-white q-m-sm">
            <q-card-section>
              <div class="text-h6">{{ cause.value.cause_title }}</div>
              <div class="text-subtitle2">
                <strong>Owner: </strong>
                {{ cause.value.owner }}
              </div>
            </q-card-section>
            <q-card-section>
              <h3>{{ cause.value.balance/1000000 }} ꜩ</h3>
            </q-card-section>
            <q-separator dark />
            <q-card-actions>
              <q-btn
                flat
                :to="{name: 'FundCause', params: {cause_id: cause.key}}"
              >
                Donate
              </q-btn>
            </q-card-actions>
          </q-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from "../api";

export default {
  mounted() {
    api.get("/v1/bigmaps/77305/keys").then((response) => {
      this.causes = response.data;
    });
  },
  data() {
    return {
      causes: [],
    };
  },
};
</script>

<style lang="scss">
.q-card {
  margin: 0.2rem;
  h3 {
    margin: 0;
  }
}
</style>