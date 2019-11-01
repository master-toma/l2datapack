# L2DataPack
Data package for LineageII. Contains original CHN C1 script files, splitted by entities, plus build system, which allows to integrate it to any IDE, which supports CMake files. Files are keept in UTF-8 endoding, which allows to have nice history view in git.

## L2DataPack in QtCreator IDE
[Youtube presentation](https://www.youtube.com/watch?v=K6QPWLvnduc&feature=youtu.be)
1. File fuzzy search
2. Syntax hightlighting
3. Code block folding
4. UTF8 to UTF16 encoding
5. AI merging + compilation
6. File merging
7. PCH compilation

## How to integrate L2DataPack in QtCreator IDE
1. Download and install [QtCreator](https://download.qt.io/official_releases/qtcreator/4.10/4.10.1/qt-creator-opensource-windows-x86_64-4.10.1.exe)
2. Download and install [CMake](https://github.com/Kitware/CMake/releases/download/v3.16.0-rc3/cmake-3.16.0-rc3-win64-x64.msi)
3. Download and install [Ninja](https://github.com/ninja-build/ninja/releases/download/v1.9.0/ninja-win.zip)
4. Download [AI merger and NASC](https://drive.google.com/drive/u/1/folders/1ETtuXnaO4RYle9mq_iT1FwCamkF85G-h)
5. Download [L2CC](https://drive.google.com/drive/u/1/folders/1MXRThY9Cizp7t8wwIT7XMgQoTQFjzNSq)
6. Copy ais.xml to C:\Users\<username>\AppData\Roaming\QtProject\qtcreator\generic-highlighter\ais.xml
7. Create DataPack Kit in QtCreator (Tools -> Options -> Kits)
![DataPack Kit](https://i.ibb.co/XzR8psz/data-pack-kit.png)
8. Clone this repo
   ```
   git clone https://github.com/master-toma/l2datapack.git
   ```
9. Open `CMakeLists.txt`
10. Select `DataPack` kit, choose `Default` 
![Configuration](https://i.ibb.co/DYF0D5v/data-pack-kit.png)
11. Click `Configure Project`. First configuration will take some time
12. Unselect `Hide Generated Files`, now you will see all targets for building scripts
13.

That's it. Now you will be able to "build" script files bu right-cliking on the "Hammer icon" and choosing `Build <target name>`
