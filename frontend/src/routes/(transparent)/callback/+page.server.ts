import type { PageServerLoad } from './$types';

export const load = (async ({url, cookies}) => {
    let token = url.searchParams.get("token")
    if (token != null){
		cookies.set("token", token, {
			httpOnly:true
		})
		cookies.set("loggedIn", "true", {
			httpOnly:false
		})
		return {
			status:200
		}
	}
}) satisfies PageServerLoad;