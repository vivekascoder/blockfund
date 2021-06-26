<template>
  <q-form>
    <q-input 
      type="number"
      v-model="number"
      @input:number="$emit('update:number', $event.target.value)"
      label="Enter a number."
      hint="Your secret number."
    />
    <!-- <input 
      type="number"
      v-model="number"
      @input="$emit('update:number', parseInt($event.target.value || 0))"
    /> -->
    Child: {{number}}
  </q-form>
</template>

<script>
export default {
  props: {
    number: {
      type: Number,
      required: true
    }
  }
}
</script>

<style>

</style>