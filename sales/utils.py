
from django.shortcuts import reverse


def reverse_querystring(view, querys_list={}):
	base_url = reverse(view)
	query_url = ''
	queries = []
	for query_name, query in querys_list.items():
		queries.append(f"{query_name}={query}")
	for query in queries:
		query_url +=f"{query}&"
	if not query_url:
		return base_url
	return f"{base_url}?{query_url}"
