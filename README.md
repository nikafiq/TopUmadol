# TopUmadol
## Fan count tools for Uma Musume Pretty Derby
A automatic fan counter to manage circle fan count to help you get that monthly goal in check

### Project feature:
- Take screenshot as you scroll down the circle member
- Extracting name and fan numbers through ocr
- Compiling data into an excel spreadsheet

### Installation:
1. Download the TopUmadol.exe from the [Releases](https://github.com/nikafiq/TopUmadol/releases)
2. Install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) into the same folder as TopUmadol.exe, **OR** you can download it [here](https://drive.google.com/file/d/1t1Z776bp3w2CxKmc0E4LPNpNBsYanngD/) and unzip it into same folder as the exe
3. Run `TopUmadol.exe` and check if the program can detect Tesseract-OCR folder. If no error or warning displayed on the app, you are good to go

### How to use:
1. Screenshot your game windows with `Take screenshot` button
2. Make sure the player card are aligned perfectly like this:  
<img src="https://drive.google.com/uc?export=view&id=1A1kj2x4RChr3HjnUBLXD7b6JaRp7YyoE" width="250">

3. Since you can only view 2 player card per screenshot, you need **15 screenshot for 30 circle member**
4. Click on the `Scan screenshot` to read fan numbers
5. Save the data as an excel file with `Export data`

### Future plan:
- Better User Interface 
- Smoother screenshot funtion
- linking exported data with Google Sheets

**Known issues**
- Program will only work if the circle display order (表示順) is set as position (役職)
- screenshot button will always take 15 screenshot (30 members)
- Player name not read correctly. You can easily overwrite the player name and save the excel as a quick fix
- If a player leave the circle, the program will have problem to overwrite the previous excel. Delete the excel file and `Scan screenshot` again


**Project are incomplete**  
Contact ["nik70#2970"](https://discordapp.com/users/182801655711006721/) on Discord for any question
