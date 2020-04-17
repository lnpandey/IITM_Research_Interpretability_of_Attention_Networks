You have trained a network on the CIFAR FG BG mosaic.

~ 85% accuracy : 

70 : FTPT
15 : FFPT
2 :   FTPF
13:  FFPF

Do this split for each Foreground class. 

Given a mosaic image like: 0,4,5,4,5,6,7,8

Let’s say : 
FG 0
80,5,2,13
FG 1
80,5,2,13
FG 2
60,25,2,13

Drill further:
Most of FFPT: 



You have FG=2. In the BG you have both classes 7,8. :
You have FG=2. In the BG you have both classes 4,8. :
You have FG=1. In the BG you have both classes 6,7. : 7^6/7^8 * 8 choose 2 > 1/50 = 2% 

7 choose 3 possible subsets of 3 background images: 35 sets

Note the split for all 3 FGs, and all 35 BG subsets : 

Total cases = 3* 35 as following:: (Repeat for both train set and test set)

FG=1, (3,4,5)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,4,6)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,4,7)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,4,8)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,4,9)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,5,6)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,5,7)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,5,8)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,5,9)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,6,7)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,6,8)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,6,9)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,7,8)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,7,9)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (3,8,9)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
FG=1, (4,5,6)\in BG : #FTPT, #FFPT, # FTPF, #FFPF
