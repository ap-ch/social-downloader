import type { Cookies } from "@sveltejs/kit"

export const getNewAccessToken = async (refreshToken: string) => {
  let response = await fetch("http://api:8000/auth/refresh", {
    method: "post",
    headers: {
      "Authorization": `Bearer ${refreshToken}`
    }
  }
  )
  if (response.ok) {
    let jsonData = await response.json()
    return jsonData["access_token"]
  }
  else {
    return null
  }
}

export const logOut = async ( cookies: Cookies ) => {
  cookies.delete("access_token")
  cookies.delete("refresh_token")
}