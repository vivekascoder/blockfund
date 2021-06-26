<template>
    <q-form
      class="q-gutter-md"
    >
    <h2>Crate a new cause on blockchain</h2>
      <q-input
        filled
        :modelValue="title"
        @update:modelValue="(e) => $emit('update:title', e)"
        label="Cause Title "
        hint="Title for the cause."
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
    title: {
      type: String,
      required: true
    }
  }
}
</script>

<style>

</style>