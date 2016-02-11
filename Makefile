delMig:
	rm -rf Plan/migrations/*
	rm -rf itinerary/migrations/*
	rm -rf signup/migrations/*
	touch Plan/migrations/__init__.py
	touch itinerary/migrations/__init__.py
	touch signup/migrations/__init__.py