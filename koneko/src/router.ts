import { createMemoryHistory, createRouter } from 'vue-router'

import HomePage from './pages/HomePage.vue'
import LobbyPage from './pages/LobbyPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/lobby', name: 'lobby', component: LobbyPage }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes
})
export { router }
