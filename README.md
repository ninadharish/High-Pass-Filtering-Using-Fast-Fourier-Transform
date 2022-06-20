# High Pass Filtering Using Fast Fourier Transform

## Description

An image consists of elements of various frequencies. This image can be processed if the image, which is originally in the spatial domain be converted to the frequency domain using the Fast Fourier Transform. A High pass filter only lets elements of high frequency pass through. This is done here without using any OpenCV functions.


## Data

* Standard Test Image "Lenna"

![alt text](/data/Lenna.png)


## Approach

* Read image.

* Convert to frequency domain using the Fast Fourier Transform and shift the origin.

* Remove the lower frequencies (Portion at the center of the frequency domain)

* Convert back to the spatial domain using the Inverse Fast Fourier Transform.


## Output

* Frequency Domain Image

![alt text](/output/output1.png)

* Removing Low Frequencies

![alt text](/output/output2.png)

* Final Output

![alt text](/output/output3.png)


## Getting Started

### Dependencies

<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>&ensp; </a>
<a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://www.codebykelvin.com/learning/python/data-science/numpy-series/cover-numpy.png" alt="numpy" width="40" height="40"/>&ensp; </a>
<a href="https://matplotlib.org/" target="_blank" rel="noreferrer"> <img src="https://static.javatpoint.com/tutorial/matplotlib/images/matplotlib-tutorial.png" alt="matplotlib" width="40" height="40"/>&ensp; </a>
</p>

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

### Executing program

* Clone the repository into any folder of your choice.
```
git clone https://github.com/ninadharish/High-Pass-Filtering-Using-Fast-Fourier-Transform.git
```

* Open the repository and navigate to the `src` folder.
```
cd High-Pass-Filtering-Using-Fast-Fourier-Transform/src
```

* Run the program.
```
python main.py
```


## Authors

👤 **Ninad Harishchandrakar**

* [GitHub](https://github.com/ninadharish)
* [Email](mailto:ninad.harish@gmail.com)
* [LinkedIn](https://linkedin.com/in/ninadharish)
