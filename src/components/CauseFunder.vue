<template>
  <q-form
      class="q-gutter-md"
    >
      <q-input
        filled
        type="number"
        :modelValue="amount"
        @update:modelValue="(e) => $emit('update:amount', e)"
        label="Amount of tezos"
      />
      <div>
        <q-btn label="Submit" type="submit" color="primary" class="q-mr-lg"/>
        <q-btn label="Connect to Wallet" color="secondary" icon="money" @click="this.$emit('connectToWallet')"/>
      </div>
    </q-form>
</template>

<script>
export default {
  props: {
    amount: {
      type: String,
      required: true
    },
  }
}
</script>

<style>

</style>