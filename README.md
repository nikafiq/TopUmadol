# TopUmadol
## Fan count tools for Uma Musume Pretty Derby
A automatic fan counter to manage circle fan count to help you get that monthly goal in check

### Project feature:
- Reading your screenshot folder
- Extracting name and fan numbers through ocr
- Compiling data into an excel spreadsheet

### Installation:
1. Clone the code as .zip file and unpack TopUmadol
2. Install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) into the TopUmadol folder
3. Run `main.py` with Python

*Due to Tesseract OCR not being a python module, compiling the project have been halt for now until a stable compiler option have been found*

### How to use:
1. Screenshot your game windows using `Alt+Windows+Prnt Scrn`
2. Make sure the player card are aligned perfectly like this:  
<img src="https://drive.google.com/uc?export=view&id=1UjGUdic0DXqikaqIuepaqIVy1hUxX_43" width="250">

3. Since you can only view 2 player card per screenshot, you need 15 screenshot for 30 circle member
4. Move all the screenshot to `pic` folder
5. Run the program
6. Confirm all the screenshot are in the `/pic` folder, press `Start scanning`
7. Click on `Export data` to save the data read as Excel file

### Future plan:
- Better User Interface 
- Screenshotting umamusume.exe windows directly
- linking exported data with Google Sheets

**Project are incomplete**  
**Contact ["nik70#2970"](https://discordapp.com/users/182801655711006721/) on Discord if you wanted to commit to the project**
