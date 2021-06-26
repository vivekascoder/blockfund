<template>
  <div class="home">
    <!-- <jumbotron/> -->
    <div class="row q-mx-auto justify-center q-mt-lg">
      <div class="col-6">
        <create-cause 
          v-model:title="title" 
          v-model:cause_id="cause_id" 
          @submit="createCause()" 
          @connectToWallet="connectToWallet()"
          />
          <p class="q-mt-sm">This information will be stored on tezos blockchain. :) #crypto</p>
          <p>
            Title: {{title}}
          </p>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbotron from "../components/jumbotron.vue";
import { contractAddress } from "../config";
import CreateCause from "../components/CreateCause.vue";
import { TezosToolkit } from "@taquito/taquito";
import {BeaconWallet} from '@taquito/beacon-wallet'

export default {
  name: "Home",
  components: {
    Jumbotron,
    CreateCause,
  },
  data(){
    return {
      Tezos: null,
      title: '',
      cause_id: 0,
    }
  },
  methods: {
    async connectToWallet() {
      this.Tezos = new TezosToolkit("https://florencenet.smartpy.io");
      const wallet = new BeaconWallet({name: 'BlockFund'})
      this.wallet = await wallet.requestPermissions({network: {type: 'florencenet'}})
      // this.Tezos.setProvider({signer: this.wallet})
      this.Tezos.setWalletProvider(wallet)
    },
    createCause() {
      this.Tezos.wallet
      .at(contractAddress)
      .then((c) => {
        return c.methods.create_cause(this.cause_id, this.title).send()
      })
      .then((op) => {
        console.log(`Hash: ${op.opHash}`)
        return op.confirmation()
      })
      .then((result) => {
        if (result.completed) {
          console.log(`Transaction correctly processed!
          Block: ${result.block.header.level}
          Chain ID: ${result.block.chain_id}`);
        } else {
          console.log('An error.')
        }
      })
      .catch((error) => console.log(`Error: ${error.message}`));
    }
  }
};
</script>
