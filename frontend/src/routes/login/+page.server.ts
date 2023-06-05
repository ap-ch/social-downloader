import { redirect } from '@sveltejs/kit'
import type { Action, Actions } from './$types';

const login: Action = async ({ request, cookies }) => {
    const data = await request.formData()
    const response = await fetch("http://api:8000/auth/token", {
            method: "post",
            body: data
        }
    )
    if (response.ok) {
        const jsonData = await response.json()
        cookies.set(
            "access_token",
            jsonData["access_token"],
            { 
                path: '/',
                httpOnly: true,
                expires: new Date(Date.now()+15*86400*1000)
            }
        )
        cookies.set(
            "refresh_token",
            jsonData["refresh_token"],
            { 
                path: '/',
                httpOnly: true,
                expires: new Date(Date.now()+15*86400*1000)
            }
        )
        throw redirect(302, '/')
    }
}

export const actions: Actions = { login }