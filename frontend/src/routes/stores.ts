import { writable } from 'svelte/store';

export let userInfo = writable(null);
export let userPrefs = writable(null)
export let serviceTasks = writable(null)
export let services = writable(null);
export let selectedService = writable("");

export let okShowAuthModal = writable(true)
export let okCloseAuthModal = writable(true)

export let okShowFeatureModal = writable(true)
export let okCloseFeatureModal = writable(true)