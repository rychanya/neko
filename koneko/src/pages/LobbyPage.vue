<script setup lang="ts">
import { useLobbyStore } from '@/store/lobbyStore'
import { onMounted } from 'vue'

const lobbyStore = useLobbyStore()
async function join() {
  await fetch(`http://127.0.0.1:8080/lobby/join?uid=${lobbyStore.uid}`)
}
async function createGame(uid: string) {
  const url = new URL('http://127.0.0.1:8080/game')
  url.searchParams.append('uid', lobbyStore.uid.toString())
  url.searchParams.append('player', uid)
  // await fetch(`http://127.0.0.1:8080/game?uid=${lobbyStore.uid}&player=${uid}`)
  await fetch(url)
}
onMounted(async () => {
  const sse = new EventSource(`http://127.0.0.1:8080/events?uid=${lobbyStore.uid}`)
  sse.addEventListener('lobby', (event) => {
    const data = JSON.parse(event.data)
    console.log(data['uid'])
    lobbyStore.lobby.add(data['uid'])
  })

  const res = await fetch('http://127.0.0.1:8080/lobby')
  lobbyStore.lobby = new Set(await res.json())
})
</script>

<template>
  <div>lobby</div>
  <div v-for="user in lobbyStore.lobby" :key="user.toString()">
    <div v-if="user == lobbyStore.uid">you</div>
    <div v-else @click="createGame(user)">{{ user }}</div>
  </div>
  <button @click="join">join</button>
</template>
