# BraneNumPy

## Prerequisites
To build, test and develop this project, you will have to satisfy the following prerequisites:
* A stable Internet connection.
* A working Docker installation. You can refer to [the official guide](https://docs.docker.com/engine/install/) for more information. 
* Brane fully installed with Docker as the default container back-end, and `buildx` as the default builder for Docker images. You can refer to [the official guide](https://wiki.enablingpersonalizedinterventions.nl/user-guide/software-engineers/installation.html) for more information. 

## Building and Running BraneNumPy
1. Clone our BraneNumPy repository
    ```bash
    git clone https://github.com/Derk-B/BraneNumPy.git
    cd BraneNumPy
    ```
    
2. Build the runtime container
    ```bash
    brane build numpy/container.yml
    ```

3. To run our example, run:
    ```bash
    brane run example.bs
    ```

4. To use our package in your own Brane project, first add 
    ```python
    import numpy;
    ```
   to the beginning of your BraneScript file, then call implemented NumPy functions in your data processing pipeline.