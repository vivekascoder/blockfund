<template>
    <q-form
      class="q-gutter-md"
    >
    <h2>Crate a new cause on blockchain</h2>
      <q-input
        filled
        v-model="title"
        label="Cause Title "
        hint="Title for the cause."
      />

      <q-input
        filled
        type="number"
        v-model="cause_id"
        label="Your Cause Id *"
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
    cause_id: {
      type: Number,
      required: true
    },
    title: {
      type: String,
      required: true
    }
  }
}
</script>

<style>

</style>