<template>
  <div class="home">
    <!-- <jumbotron/> -->
    <div class="row q-mx-auto justify-center q-mt-lg">
      <div class="col-6">
        <create-cause 
          v-model:title="title" 
          @submit="createCause()" 
          @connectToWallet="connectToWallet()"
          />
          <p v-if="hash" class="q-mt-lg">Hash: {{hash}}</p>
          <p v-if="block">BlockId: {{block}}</p>
          <p v-if="chainId">ChainId: {{chainId}}</p>
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
      hash: '',
      block: '',
      chainId: ''
    }
  },
  methods: {
    async connectToWallet() {
      this.Tezos = new TezosToolkit("https://florencenet.smartpy.io");
      const wallet = new BeaconWallet({name: 'BlockFund'})
      this.wallet = await wallet.requestPermissions({network: {type: 'florencenet'}})
      this.Tezos.setWalletProvider(wallet)
    },
    createCause() {
      this.Tezos.wallet
      .at(contractAddress)
      .then((c) => {
        return c.methods.create_cause(Date.now(), this.title).send()
      })
      .then((op) => {
        console.log(`Hash: ${op.opHash}`)
        this.hash = op.opHash
        return op.confirmation()
      })
      .then((result) => {
        if (result.completed) {
          console.log(`Transaction correctly processed!
          Block: ${result.block.header.level}
          Chain ID: ${result.block.chain_id}`);
          this.block = result.block.header.level
          this.chainId = result.block.chain_id
        } else {
          console.log('An error.')
        }
      })
      .catch((error) => console.log(`Error: ${error.message}`));
    }
  }
};
</script>
