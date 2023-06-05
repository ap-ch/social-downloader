import { redirect } from '@sveltejs/kit'
import type { Action, Actions } from './$types';

const signup: Action = async ({ request }) => {
    const data = await request.formData();
    const registerData = Object.fromEntries(data.entries());
    console.log(registerData);
    const response = await fetch("http://api:8000/user/register", {
            method: "post",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(registerData)
        }
    );
    if (response.ok) {
        throw redirect(302, '/login');
    }
}

export const actions: Actions = { signup }