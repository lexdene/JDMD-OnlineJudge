all : main.py gui/client_hall.py \
	../client-build-desktop/ui_client_hall.py \
	../client-build-desktop/ui_show_problem.py \
	../client-build-desktop/ui_MainWindow.py
../client-build-desktop/ui_show_problem.py : ../client-build-desktop/show_problem.ui
	mkdir -p ../client-build-desktop
	pyuic4 $< >$@
../client-build-desktop/ui_client_hall.py : ../client-build-desktop/client_hall.ui
	mkdir -p ../client-build-desktop
	pyuic4 $< >$@
../client-build-desktop/ui_MainWindow.py : ../client-build-desktop/MainWindow.ui
	mkdir -p ../client-build-desktop
	pyuic4 $< >$@
../client-build-desktop/show_problem.ui : gui/show_problem.ui.php
	mkdir -p ../client-build-desktop
	php5 $< >$@
../client-build-desktop/client_hall.ui : gui/client_hall.ui.php
	mkdir -p ../client-build-desktop
	php5 $< >$@
../client-build-desktop/MainWindow.ui : gui/MainWindow.ui.php
	mkdir -p ../client-build-desktop
	php5 $< >$@
clean :
	rm -rvf ../client-build-desktop
