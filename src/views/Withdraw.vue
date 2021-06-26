<template>
  <div class="flex justify-center q-mt-xl">
    <div class="col-8">
      <div class="row">
        <h4>Withdraw total funds.</h4>
      </div>
      <div class="row q-mb-xl">
        <div class="col">
          <q-card class="my-card bg-primary text-white q-m-sm" v-if="cause">
            <q-card-section>
              <div class="text-h4 q-mb-md">
                {{ cause.value.cause_title }}
              </div>
              <div class="text-subtitle2 q-mb-sm text-h6">
                <strong>Owner: </strong> {{cause.value.owner}}
              </div>
              <div class="text-subtitle1">
                <strong>Funds:</strong> {{cause.value.balance / 1000000}}
              </div>
            </q-card-section>
            <q-separator dark />
            <q-card-actions>
              <q-btn @click="withdrawFunds()" icon="flight_takeoff" flat
                >Withdraw</q-btn
              >
              <q-btn
                @click="connectToWallet()"
                class="bg-teal"
                icon="money"
                flat
                >Connect to Wallet</q-btn
              >
            </q-card-actions>
          </q-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { contractAddress } from "../config";
import { TezosToolkit } from "@taquito/taquito";
import { BeaconWallet } from "@taquito/beacon-wallet";
import { api } from "../api";

export default {
  data() {
    return {
      Tezos: null,
      cause: null,
    };
  },
  mounted() {
    api
      .get(`/v1/bigmaps/77305/keys/${this.$route.params.id}`)
      .then((response) => {
        this.cause = response.data;
      });
  },
  methods: {
    async connectToWallet() {
      this.Tezos = new TezosToolkit("https://florencenet.smartpy.io");
      const wallet = new BeaconWallet({ name: "BlockFund" });
      this.wallet = await wallet.requestPermissions({
        network: { type: "florencenet" },
      });
      this.Tezos.setWalletProvider(wallet);
    },
    withdrawFunds() {
      if (!this.Tezos) {
        return null;
      }
      this.Tezos.wallet
        .at(contractAddress)
        .then((c) => {
          return c.methods.withdraw_funds(this.$route.params.id).send();
        })
        .then((op) => {
          console.log(`Hash: ${op.opHash}`);
          return op.confirmation();
        })
        .then((result) => {
          if (result.completed) {
            console.log(`Transaction correctly processed!
            Block: ${result.block.header.level}
            Chain ID: ${result.block.chain_id}`);
          } else {
            console.log("An error.");
          }
        })
        .catch((err) => console.log(`Error: ${err.message}`));
    },
  },
};
</script>

<style>
</style>