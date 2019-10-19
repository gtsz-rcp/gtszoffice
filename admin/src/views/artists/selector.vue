<template>
  <div class="form-group">
    <label>{{label}}</label>
    <select 
      v-bind:value="value" 
      v-on:change="updateValue($event.target.value)" 
      class="custom-select">
      <option value="">select {{label}}</option>
      <option 
        v-for="item in artistsList" 
        :key="item.id" 
        :value="item.id"
        v-bind:selected="item.id == value ? 'selected' : ''">{{item.name}}</option>
    </select>
  </div>
</template>

<script>
import {Artists} from '@/service/artists'

const artistsIO = new Artists()

export default {
  name: 'artistSelector',
  props: {
    value: [Number, String],
    label: {
      type: String,
      default: 'Artist'
    }
  },
  data() {
    return {
      artistsList: [],
    }
  },
  methods: {
    lists() {
      let vm = this
      return artistsIO.list()
        .then((result) => {
          vm.artistsList = result.data
        })
    },
    updateValue(value) {
      this.$emit('input', value)
    }
  },
  created() {
    this.lists()
  }
}
</script>

<style scoped>
label {text-transform: capitalize}
</style>>