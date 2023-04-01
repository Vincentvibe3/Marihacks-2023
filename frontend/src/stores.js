import { writable } from 'svelte/store'
export const transparent = writable(true)
export const userToken = writable("")
export const loggedIn = writable(false)