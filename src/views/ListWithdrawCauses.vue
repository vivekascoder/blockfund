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
                Want to withdraw the your funds. <br />
                Select your cause from the following causes and withdraw the
                raised amount.
              </div>
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
        <div class="col">
          <q-list bordered separator>
            <q-item 
              v-for="cause in causes" 
              :key="cause.id" 
              :to="{name: 'Withdraw', params: {id: cause.key}}"
              clickable v-ripple
            >
              <q-item-section avatar>
                <q-avatar
                  color="primary"
                  text-color="white"
                  icon="volunteer_activism"
                />
              </q-item-section>
              <q-item-section>
                <q-item-label class="text-h6">
                  {{
                    cause.value.cause_title
                      ? cause.value.cause_title
                      : "Untitled"
                  }}
                </q-item-label>
                <q-item-label class="" caption>
                  <strong>Owner: </strong> {{cause.value.owner}} <br>
                  <span class="text-green">
                    Raised: + {{ cause.value.balance / 1000000 }} ꜩ
                  </span>
                </q-item-label>
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
.title {
  text-align: center;
}
</style>