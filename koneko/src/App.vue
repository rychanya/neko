<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const router = useRouter()

onMounted(() => router.push({ name: 'lobby' }))
</script>

<template>
  <RouterView></RouterView>
</template>
