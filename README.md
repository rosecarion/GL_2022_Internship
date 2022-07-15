# GL_2022_Internship
[Mike Lee's GeneLab 2022 Summer Internship Wiki](https://github.com/AstrobioMike/GL-2022-summer-internship/wiki)

# HackMD_Pages
[First HackMD Page](https://hackmd.io/@rcarion/SkCS__mK9)

[GeneLab Amplicon Processing](https://hackmd.io/@rcarion/r1aWS4Wq9)

[GeneLab Metagenomics Processing](https://hackmd.io/@rcarion/rJTULUb9c)

[Test Dataset Metagenomics Processing Code](https://hackmd.io/xRYblztARdyBqLCYuEZn7A)

# Code Use Instructions
To test the above codes (metagenomics_user_input_validation.py, amplicon_user_input_validation.py):

## Installation:
- Install dp_tools and set up the conda environment [as explained by Mike Lee](https://github.com/AstrobioMike/GL-2022-summer-internship/wiki/Working-towards-Jonathan's-validation-structure))

- Download, unpack, and move metagenomics test data to an output directory with:
```
curl -L -o GL-metagenomics-output-for-validation-testing.tar.gz https://figshare.com/ndownloader/files/36039989
tar -xzvf GL-metagenomics-output-for-validation-testing.tar.gz
cd GL-metagenomics-output-for-validation-testing/
```

- Download, unpack, and move amplicon test data to an output directory with:
```
curl -L -o GL-amplicon-output-for-validation-testing.tar.gz https://figshare.com/ndownloader/files/36252156
tar -xzvf GL-amplicon-output-for-validation-testing.tar.gz
cd GL-amplicon-output-for-validation-testing/
```

## Metagenomics Code 
After running the code, the user will be asked to input data.
1. **GLDS ID** <br /> ###### e.g. 'GLDS-276'
2. **Path to the sample names file**
<br /> ###### e.g. '/Users/rosecarion/Desktop/unique-sample-IDs.txt'
3. **Expected additional filename prefix that was added to the files that describe multiple samples (default: \"\")** Press 'return' key if none
4. **Specify whether the test data is single-ended**
<br /> ######  e.g. 'y' for 'yes'
     'n' for 'no'

## Amplicon Code 
After running the code, the user will be asked to input data.
1. **GLDS ID**
<br /> ###### e.g. 'GLDS-276'
2. **Path to the sample names file**
<br /> ###### e.g. '/Users/rosecarion/Desktop/unique-sample-IDs.txt'
3. **Output file prefix if there is one** Press 'return' key if none
4. **Specify whether primers trimmed prior to GeneLab processing** 
<br /> ###### e.g. 'y' for 'yes'
     'n' for 'no'
5. **Specify whether the test data is single-ended**
<br /> ###### e.g. 'y' for 'yes'
     'n' for 'no'

