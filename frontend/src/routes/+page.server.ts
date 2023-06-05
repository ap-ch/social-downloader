import type { PageServerLoad } from './login/$types';

export const load = (async ( { fetch }) => {
    let user_info = null
    const response = await fetch(
        "http://api:8000/user/", 
        { method: "get" }
    );
    if (response.ok) {
        user_info = await response.json();
    }
    return {
        "user_info": user_info
    }
}) satisfies PageServerLoad;
