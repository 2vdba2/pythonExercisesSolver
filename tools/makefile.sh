cd ..
wine C:/Python312/Scripts/pyinstaller.exe --onefile --windowed --workpath "Z:$(pwd)/psc_gui_tmp" --distpath "Z:$(pwd)" --specpath "Z:$(pwd)" "Z:$(pwd)/exercisesSolver.py"
rm -r psc_gui_tmp
rm exercisesSolver.spec
