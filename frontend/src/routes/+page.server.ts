import { redirect } from '@sveltejs/kit'
import type { Action, Actions } from './$types';
import type { PageServerLoad } from './$types';

export const load = (async ( { fetch }) => {
    let userInfo = null
    let userPrefs = null
    let services = null

    const responseUserInfo = await fetch(
        "http://api:8000/user/", 
        { method: "get" }
    );
    
    if (responseUserInfo.ok) {
        userInfo = await responseUserInfo.json();
    }

    const responseUserPrefs = await fetch(
        "http://api:8000/preferences/", 
        { method: "get" }
    );
    
    if (responseUserPrefs.ok) {
        userPrefs = await responseUserPrefs.json();
    }

    const responseServices = await fetch(
        "http://api:8000/services/", 
        { method: "get" }
    );
    
    if (responseServices.ok) {
        services = (await responseServices.json()).services;
    }

    return {
        "userInfo": userInfo,
        "userPrefs": userPrefs,
        "services": services
    }
}) satisfies PageServerLoad;