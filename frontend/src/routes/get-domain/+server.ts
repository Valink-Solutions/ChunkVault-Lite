import { json } from '@sveltejs/kit';
import { env as privEnv } from '$env/dynamic/private';
import { env as pubEnv } from '$env/dynamic/public';

export async function GET() {
	const domain = pubEnv.PUBLIC_SHARE_DOMAIN || `https://${privEnv.DETA_SPACE_APP_HOSTNAME}`;

	if (!domain) {
		return json({
			status: 500,
			body: { error: 'Error: Neither private nor public domain is available.' }
		});
	}

	return json({
		status: 200,
		body: { domain }
	});
}
