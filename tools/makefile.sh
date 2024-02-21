cd ..
rm -r src/__pycache__
wine C:/Python312/Scripts/pyinstaller.exe --onefile --windowed --workpath "Z:$(pwd)/psc_gui_tmp" --distpath "Z:$(pwd)" --specpath "Z:$(pwd)" "Z:$(pwd)/exercisesSolver.py"
rm -r psc_gui_tmp
rm exercisesSolver.spec

#zip
zip -r exercisesSolver.zip exercisesSolver.exe data/ src/

