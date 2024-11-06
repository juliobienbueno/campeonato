from supabase import create_client
from django.conf import settings

url = settings.SUPABASE_URL
key = settings.SUPABASE_KEY
supabase = create_client(url, key)