<template>
  <div>
    <p>{{ $route.params.cause_id }}</p>
    <div class="row q-mx-auto justify-center q-mt-lg">
      <div class="col-6">
        <CauseFunder 
          :amount="tezosAmount"
          @submit="printAmount()"
        />
        PArent: {{tezosAmount}}
      </div>
    </div>
  </div>
</template>

<script>
/*
@submit="transferFunds()" 
@connectToWallet="connectToWallet()" 
*/
import { contractAddress } from "../config";
import { TezosToolkit } from "@taquito/taquito";
import {BeaconWallet} from '@taquito/beacon-wallet'
import CauseFunder from '../components/CauseFunder.vue';

export default {
  name: "Home",
  components: {
    CauseFunder
  },
  data() {
    return {
      Tezos: null,
      tezosAmount: 0
    }
  },
  methods: {
    printAmount() {
      console.log(this.amount)
    },
    async connectToWallet() {
      this.Tezos = new TezosToolkit("https://florencenet.smartpy.io");
      const wallet = new BeaconWallet({name: 'BlockFund'})
      this.wallet = await wallet.requestPermissions({network: {type: 'florencenet'}})
      // this.Tezos.setProvider({signer: this.wallet})
      this.Tezos.setWalletProvider(wallet)
    },
    transferFunds(){
      console.log('Pesa', this.amount)
      this.Tezos.wallet
      .transfer({to: contractAddress, amount: this.amount})
      .send()
      .then((op) => {
        console.log(`Waiting for ${op.opHash} to be confirmed..`);
        return op.confirmation().then(() => op.opHash)
      })
      .then(() => {console.log(Done);})
      .catch((error) => console.log(`Error: ${error} ${JSON.stringify(error, null, 2)}`));
      // if (!this.Tezos) {
      //   return 
      // }
      // this.Tezos.wallet
      // .at(contractAddress)
      // .then((c) => {
      //   return c.methods.fund_cause(this.$route.params.cause_id).send(amount=this.amount*1000000)
      // })
      // .then((op) => {
      //   console.log(`Hash: ${op.opHash}`)
      //   return op.confirmation()
      // })
      // .then((result) => {
      //   if (result.completed) {
      //     console.log(`Transaction correctly processed!
      //     Block: ${result.block.header.level}
      //     Chain ID: ${result.block.chain_id}`);
      //   } else {
      //     console.log('An error.')
      //   }
      // })
      // .catch((error) => console.log(`Error: ${error.message}`));
    }
  }
};
</script>

<style>

</style>