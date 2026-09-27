/* ORION analytics config.
 *
 * MANUAL STEP: paste the Supabase ANON (publishable) key below.
 * Supabase dashboard → Project Settings → API → "anon public" key.
 * Same project/key as the Golden Hour site — one `page_views` table
 * serves all publications via the `site` column.
 * The anon key is designed to be public in client code — but NEVER put the
 * service_role key here. Until a real key is pasted, the beacon silently
 * does nothing.
 */
window.ORION_ANALYTICS_KEY = "__PASTE_SUPABASE_ANON_KEY_HERE__";
