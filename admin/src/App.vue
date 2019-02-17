<template>
  <div id="app">
    <appHeader />
    <router-view/>
  </div>
</template>

<script>
import header from '@/components/Header'

export default {
  name: 'App',
  components: {
    appHeader: header
  }
}
</script>

<style></style>
