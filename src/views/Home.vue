<template>
  <div class="row q-mt-lg flex justify-center p-mx-sm">
    <div class="col-8">
      <div class="row q-mb-xl">
        <div class="col">
          <q-card class="my-card bg-primary text-white q-m-sm">
            <q-card-section>
              <div class="text-h4 q-mb-sm">
                BlockFund, Raise Crypto, Save World
              </div>
              <div class="text-subtitle2">
                We're the modern social cause fund raiser to help you and
                everyone else, to save the world, save lives and make it a
                better place.
              </div>
            </q-card-section>
            <q-card-section>
              <h3></h3>
            </q-card-section>
            <q-separator dark />
            <q-card-actions>
              <q-btn flat> Learn More </q-btn>
            </q-card-actions>
          </q-card>
        </div>
      </div>
      <div class="row">
        <div class="col"><h4 class="title">Latest Causes</h4></div>
      </div>
      <div class="row q-mb-xl">
        <div v-for="cause in causes" :key="cause.id" class="col-6">
          <q-card class="my-card bg-secondary text-white q-m-sm">
            <q-card-section>
              <div class="text-h6">
                {{
                  cause.value.cause_title ? cause.value.cause_title : "Untitled"
                }}
              </div>
              <div class="text-subtitle2">
                <strong>Owner: </strong>
                {{ cause.value.owner }}
              </div>
            </q-card-section>
            <q-card-section>
              <h3>Total: {{ cause.value.balance / 1000000 }} ꜩ</h3>
            </q-card-section>
            <q-separator dark />
            <q-card-actions>
              <q-btn
                flat
                :to="{ name: 'FundCause', params: { cause_id: cause.key } }"
              >
                Donate
              </q-btn>
            </q-card-actions>
          </q-card>
        </div>
      </div>

      <div class="row">
        <div class="col"><h4 class="title">Latest Funds</h4></div>
      </div>
      <div class="row q-mb-xl">
        <div class="col">
          <q-list bordered separator>
            <q-item 
              v-for="fund in fundings"
              :key="fund.id"
              clickable 
              v-ripple
            >
              <q-item-section avatar>
                <q-avatar color="primary" text-color="white" icon="volunteer_activism" />
              </q-item-section>
              <q-item-section>
                <q-item-label>
                  <strong>From:</strong>
                  {{fund.key.funder}}
                </q-item-label>
                <q-item-label class="text-green" caption>Funded: + {{fund.value / 1000000}} ꜩ</q-item-label>
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple>
              <q-item-section>
                <q-item-label>Visualize the Contract</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
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
    api.get('/v1/bigmaps/77306/keys').then((response) => {
      this.fundings = response.data
    })
  },
  data() {
    return {
      causes: [],
      fundings: []
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
.title {
  text-align: center;
}
</style>