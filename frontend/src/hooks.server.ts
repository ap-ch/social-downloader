import { redirect, type Handle } from "@sveltejs/kit";
import type { HandleFetch } from '@sveltejs/kit';
import * as jwt from 'jsonwebtoken';
import { SECRET } from '$env/static/private';
import { getNewAccessToken, logOut } from '$lib/server/helpers.js';

import { userInfo } from "./routes/stores";

export const handle = (async ({ event, resolve }) => {

  let cookies = event.cookies;
  let access_token = cookies.get("access_token");
  let refresh_token = cookies.get("refresh_token");

  let secret: jwt.Secret = SECRET;

  let userInfoValue: any;

  userInfo.subscribe(value => {
		userInfoValue = value;
	});

  if (event.url.pathname.startsWith("/logout")) {
    logOut(cookies);
    throw redirect(302, '/');
  }

  if (event.url.pathname.startsWith("/login") || event.url.pathname.startsWith("/signup")) {
    if (userInfoValue != null) {
      throw redirect(302, '/');
    }
  }

  if (access_token != null && refresh_token != null) {
    try {
      let decoded_rt: any = jwt.verify(refresh_token, secret);
      let rt_expiration = new Date(decoded_rt.exp*1000);
      try {
        jwt.verify(access_token, secret);
      }
      catch (err: any) {
        if (err.name == "TokenExpiredError") {
          let newAccessToken = await getNewAccessToken(refresh_token);
          cookies.set(
            "access_token",
            newAccessToken,
            {
              path: '/',
              httpOnly: true,
              expires: rt_expiration
            }
          );
        }
        else {
          logOut(cookies);
        }
      }
    }
    catch (err) {
      logOut(cookies);
    }
  }
  else {
    logOut(cookies);
  }
  return await resolve(event);
}) satisfies Handle;

export const handleFetch = (async ({ event, request, fetch }) => {
  let cookies = event.cookies;
  let access_token = cookies.get("access_token")

  if (access_token != null) {
    if (!request.url.startsWith('http://api:8000/auth')) {
      request.headers.set('Authorization', `Bearer ${access_token}`);
    }
  }

  return fetch(request);
}) satisfies HandleFetch;
