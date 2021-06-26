<template>
  <div>
    <p>{{ $route.params.cause_id }}</p>
    <div class="row q-mx-auto justify-center q-mt-lg">
      <div class="col-6">
        <div class="row q-mb-sm">
          <div class="col">
            <q-card class="my-card bg-primary text-white q-m-sm" v-if="cause">
              <q-card-section>
                <div class="text-h4 q-mb-md">
                  Fund <strong>{{ cause.value.cause_title }}</strong>
                </div>
                <div class="text-subtitle2 q-mb-sm text-h6">
                  <strong>Owner: </strong> {{ cause.value.owner }}
                </div>
                <div class="text-subtitle1">
                  <strong>Funds:</strong> {{ cause.value.balance / 1000000 }} ꜩ
                </div>
              </q-card-section>
              <q-separator dark />
            </q-card>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <CauseFunder
              v-model:amount="tezosAmount"
              @submit="transferFunds()"
              @connectToWallet="connectToWallet()"
            />
            <p v-if="hash" class="q-mt-lg">Hash: {{hash}}</p>
            <p v-if="block">BlockId: {{block}}</p>
            <p v-if="chainId">ChainId: {{chainId}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/*

*/
import { contractAddress } from "../config";
import { TezosToolkit } from "@taquito/taquito";
import { BeaconWallet } from "@taquito/beacon-wallet";
import CauseFunder from "../components/CauseFunder.vue";
import { api } from "../api";

export default {
  name: "Home",
  components: {
    CauseFunder,
  },
  data() {
    return {
      Tezos: null,
      tezosAmount: "",
      contractBalance: 0,
      cause: null,
      hash: '',
      block: '',
      chainId: ''
    };
  },
  mounted() {
    api
      .get(`/v1/bigmaps/77305/keys/${this.$route.params.cause_id}`)
      .then((response) => {
        this.cause = response.data;
      });
  },
  // async mounted() {
  //   const tezos = new TezosToolkit('https://florencenet.smartpy.io')
  //   const balance = await tezos.tz.getBalance(contractAddress)
  //   this.contractBalance = balance
  // },
  methods: {
    async connectToWallet() {
      this.Tezos = new TezosToolkit("https://florencenet.smartpy.io");
      const wallet = new BeaconWallet({ name: "BlockFund" });
      this.wallet = await wallet.requestPermissions({
        network: { type: "florencenet" },
      });
      this.Tezos.setWalletProvider(wallet);
    },
    transferFunds() {
      // console.log('Pesa', this.tezosAmount)
      // this.Tezos.wallet
      // .transfer({to: contractAddress, amount: parseInt(this.tezosAmount)})
      // .send()
      // .then((op) => {
      //   console.log(`Waiting for ${op.opHash} to be confirmed..`);
      //   return op.confirmation().then(() => op.opHash)
      // })
      // .then(() => {console.log("Done");})
      // .catch((error) => console.log(`Error: ${error} ${JSON.stringify(error, null, 2)}`));
      if (!this.Tezos) {
        return;
      }
      this.Tezos.wallet
        .at(contractAddress)
        .then((c) => {
          return c.methods
            .fund_cause(this.$route.params.cause_id)
            .send({ amount: this.tezosAmount });
        })
        .then((op) => {
          console.log(`Hash: ${op.opHash}`);
          this.hash = op.opHash
          return op.confirmation();
        })
        .then((result) => {
          if (result.completed) {
            console.log(`Transaction correctly processed!
          Block: ${result.block.header.level}
          Chain ID: ${result.block.chain_id}`);
          this.block = result.block.header.level
          this.chainId = result.block.chain_id
          } else {
            console.log("An error.");
          }
        })
        .catch((error) => console.log(`Error: ${error.message}`));
    },
  },
};
</script>

<style>
</style>