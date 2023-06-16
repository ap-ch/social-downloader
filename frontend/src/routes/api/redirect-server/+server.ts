// /api/redirect-server POST

export async function POST(event: any) {
	let res = event.url.href.split("=")[1].split("&")[0];
	let params;
	if (event.url.href.includes("&")) {
		params = "?" + event.url.href.replace(event.url.href.split("&")[0]+"&", "");
	}
	else {
		params = "";
	}

	let access_token = event.cookies.get("access_token");
	event.request.headers.set('Authorization', `Bearer ${access_token}`);

	let options = {
		method: "post",
		headers: event.request.headers,
		body: event.request.body,
		duplex: "half"
	}

	let response = await fetch(`http://api:8000${res}${params}`, options);

	return response	
}

// /api/redirect-server GET

export async function GET(event: any) {
	const res = event.url.href.split("=")[1].split("&")[0];
	let params;
	if (event.url.href.includes("&")) {
		params = "?" + event.url.href.replace(event.url.href.split("&")[0]+"&", "");
	}
	else {
		params = "";
	}

	const access_token = event.cookies.get("access_token");
	event.request.headers.set('Authorization', `Bearer ${access_token}`);

	console.log(res)
	console.log(params)

	let response = await fetch(`http://api:8000${res}${params}`, {
		method: "get",
		headers: event.request.headers
		}
	);

	return response	
}