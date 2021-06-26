<template>
  <div>
    <h1>
      {{$route.params.id}}
    </h1>
    <button @click="connectToWallet()">Connect to wallet.</button>
    <button @click="withdrawFunds()">Withdraw</button>
  </div>
</template>

<script>
import { contractAddress } from "../config";
import { TezosToolkit } from "@taquito/taquito";
import {BeaconWallet} from '@taquito/beacon-wallet'

export default {
  data() {
    return {
      Tezos: null
    }
  },
  methods: {
    async connectToWallet() {
      this.Tezos = new TezosToolkit("https://florencenet.smartpy.io");
      const wallet = new BeaconWallet({name: 'BlockFund'})
      this.wallet = await wallet.requestPermissions({network: {type: 'florencenet'}})
      this.Tezos.setWalletProvider(wallet)
    },
    withdrawFunds() {
      if (!this.Tezos) return null
      this.Tezos.wallet
        .at(contractAddress)
        .then((c) => {
          return c.methods.withdraw_funds(this.$route.params.id).send()
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
        .catch((err) => console.log(`Error: ${err.message}`))
    }
  }

}
</script>

<style>

</style>