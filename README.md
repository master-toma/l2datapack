# L2DataPack
Data package for LineageII. Contains original CHN C1 script files, splitted by entities, plus build system, which allows to integrate it to any IDE, which supports CMake files. Files are kept in UTF-8 encoding, which allows to have nice history view in git.

## Content
All script entities are original C1 files with fixes only (like typos in name IDs, removals of legacy items/npcs, etc).
For other chronicles new branches will be created

## L2DataPack in QtCreator IDE
[Youtube presentation](https://www.youtube.com/watch?v=K6QPWLvnduc&feature=youtu.be)
1. File fuzzy search
2. Syntax hightlighting
3. Code block folding
4. UTF8 to UTF16 encoding
5. AI merging + compilation
6. File merging
7. PCH compilation

## Next steps
1. Syntax hightlighting for all scripts, not AI only
2. Extracting quests from AI scritps into separate `questdata`
3. More precise file separation (e.g. separating weapons and armors by types, spell-boocks by chants/books/blueprints, etc)
4. C4+ support

## How to integrate L2DataPack in QtCreator IDE
1. Download and install [QtCreator](https://download.qt.io/official_releases/qtcreator/4.10/4.10.1/qt-creator-opensource-windows-x86_64-4.10.1.exe)
2. Download and install [CMake](https://github.com/Kitware/CMake/releases/download/v3.16.0-rc3/cmake-3.16.0-rc3-win64-x64.msi)
3. Download [Ninja](https://github.com/ninja-build/ninja/releases/download/v1.9.0/ninja-win.zip) and copy it into `C:\Program Files\CMake\bin`
4. Download [AI merger and NASC](https://drive.google.com/drive/u/1/folders/1ETtuXnaO4RYle9mq_iT1FwCamkF85G-h)
5. Download [L2CC](https://drive.google.com/drive/u/1/folders/1MXRThY9Cizp7t8wwIT7XMgQoTQFjzNSq)
6. Copy `ais.xml` to `C:\Users\<username>\AppData\Roaming\QtProject\qtcreator\generic-highlighter\ais.xml`
7. Create `DataPack Kit` in `QtCreator` (`Tools -> Options -> Kits`)
![DataPack Kit](https://i.ibb.co/XzR8psz/data-pack-kit.png)
click `Apply` and `OK` to close the window
8. Clone this repo
   ```
   git clone https://github.com/master-toma/l2datapack.git
   ```
9. Open `<path>/l2datapack/CMakeLists.txt` by `File -> Open File Or Project`
10. Select `DataPack` kit, choose `Default` or `Release` and uncheck all other configurations
![Configuration](https://i.ibb.co/DYF0D5v/data-pack-kit.png)
11. Click `Configure Project`. First configuration will take some time
12. Unselect `Hide Generated Files`, now you will see all targets for building scripts
![Hide Generated Files](https://i.ibb.co/khhRQKG/hidegen.png)
13. Setup tools (`L2CC`, `NASC`, `AI Merger`)
![Setup tools](https://i.ibb.co/QH25TQZ/tools.png)

That's it. Now you will be able to "`build`" script files by right-cliking on the "Hammer icon" and choosing `Build <target name>`, e.g.
```
build 1-basics
build 2-complex
build 3-ai
```
Those three commands will do full script deployment.

