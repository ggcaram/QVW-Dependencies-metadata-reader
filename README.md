# QVW-Dependencies-metadata-reader
Python script to obtain the consumed and generate .QVDs in a QVW file

This script performs the following steps:
1) Scroll through the selected folder to get all files with .QVW extension.
2) Prints the path and name of the selected .QVW's
3) Using the <LineageInfo> and <Discriminator> tags it takes all the paths of the consumed .QVDS and stores them in a list. 
4) Using the STORE statement it takes all the paths of the saved .QVDS's and stores them in a list. 
5) Extract the names of the files
6) Print the following data
- Name of the .QVW
- Path of the .QVW
- Name of the consumed .QVDS
- Path of the consumed .QVDS
- Name of the Generated .QVDS
- Store Sentence of each .QVD Generated

Translated with DeepL.com (free version)
