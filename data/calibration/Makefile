all: _fig_calibration.pdf _fig_calibration_compare.pdf

_fig_calibration.pdf:
	python calibration.py

_fig_calibration_compare.pdf:
	python calibration_compare.py

clean:
	$(RM) _fig_calibration.pdf _fig_calibration_compare.pdf
