import { defineStore } from 'pinia'
import { v4 } from "uuid"

export const useLobbyStore = defineStore("lobbyStore", {
    state: () => {
        return { lobby: new Set<string>, uid: v4() as String }
    }
})
