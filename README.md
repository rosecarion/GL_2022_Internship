# GL 2022 Internship
[Mike Lee's GeneLab 2022 Summer Internship Wiki](https://github.com/AstrobioMike/GL-2022-summer-internship/wiki)

# HackMD Pages
[First HackMD Page](https://hackmd.io/@rcarion/SkCS__mK9)

[GeneLab Amplicon Processing](https://hackmd.io/@rcarion/r1aWS4Wq9)

[GeneLab Metagenomics Processing](https://hackmd.io/@rcarion/rJTULUb9c)

[Test Dataset Metagenomics Processing Code](https://hackmd.io/xRYblztARdyBqLCYuEZn7A)

# Code Use Instructions
To test the above codes (metagenomics_user_input_validation.py, amplicon_user_input_validation.py):

## Installation:
- Install conda [as described by Mike Lee](https://astrobiomike.github.io/unix/conda-intro#getting-and-installing-conda)

- Install dp_tools [as explained by Mike Lee](https://github.com/AstrobioMike/GL-2022-summer-internship/wiki/Working-towards-Jonathan's-validation-structure)
```
curl -L -o dp_tools-condaEnv.yaml https://raw.githubusercontent.com/J-81/dp_tools/main/condaEnv.yaml
conda env create -f dp_tools-condaEnv.yaml
conda activate dp_tools
```

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
1. **GLDS ID** <br />  e.g. 'GLDS-276'
2. **Path to the sample names file**
<br />  e.g. '/Users/rosecarion/Desktop/GL-metagenomics-output-for-validation-testing/unique-sample-IDs.txt'
3. **Expected additional filename prefix that was added to the files that describe multiple samples (default is a back slash)** <br />Press 'return' key if none
4. **Specify whether the test data is single-ended**
<br />   e.g. 'y' for 'yes'
     <br />'n' for 'no'
<br />*Information regarding the downloaded test data:<br />
GLDS ID is 'TEST'<br />
there is no expected additional filename prefix<br />
not single-ended*

## Amplicon Code 
After running the code, the user will be asked to input data.
1. **GLDS ID**
<br />  e.g. 'GLDS-276'
2. **Path to the sample names file**
<br />  e.g. '/Users/rosecarion/Desktop/Amplicon_validation/GL-amplicon-output-for-validation-testing/unique-sample-IDs.txt'
3. **Output file prefix if there is one** <br /> Press 'return' key if none
4. **Specify whether primers trimmed prior to GeneLab processing** 
<br />  e.g. 'y' for 'yes'
     <br />'n' for 'no'
5. **Specify whether the test data is single-ended**
<br /> e.g. 'y' for 'yes'
     <br />'n' for 'no'
<br />*Information regarding the downloaded test data:<br />
GLDS ID is 'TEST'<br />
there is no output file prefix<br />
primers are not trimmed <br />
not single-ended*
