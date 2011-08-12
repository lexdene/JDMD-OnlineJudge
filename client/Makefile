all : main.py gui/client_hall.py ../client-build-desktop/ui_client_hall.py
../client-build-desktop/ui_client_hall.py : ../client-build-desktop/client_hall.ui
	mkdir -p ../client-build-desktop
	pyuic4 $< >$@
../client-build-desktop/client_hall.ui : gui/client_hall.ui.php
	mkdir -p ../client-build-desktop
	php5 $< >$@
clean :
	rm -rvf ../client-build-desktop/client_hall.ui ../client-build-desktop/ui_client_hall.py ../client-build-desktop/*.pyc
