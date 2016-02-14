delMig:
	rm -rf */migrations/*
	touch complaint/migrations/__init__.py
	touch review/migrations/__init__.py
	touch user/migrations/__init__.py
