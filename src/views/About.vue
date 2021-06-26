<template>
  <div class="about">
    <!-- <number :number="numberOne" @update:number="numberOne = $event" /> -->
    <Number v-model:number="numberOne" />
    <h1>This is an about page {{numberOne}}</h1>
  </div>
</template>

<script>
import Number from '../components/Number.vue'
export default {
  components: { Number },
  data() {
    return {
      numberOne: 0
    }
  },
  methods: {
    getNumber() {
      console.log('Hello World')
    }
  }
}
</script>