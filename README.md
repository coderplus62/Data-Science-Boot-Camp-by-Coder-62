#  Data Science Boot-Camp by Coder+62
Belajar dasar-dasar machine learning dari nol. Untuk fase pertama, kita akan mempelajari teknik-teknik supervised learning menggunakan scikit-learn dan jcopml.

# Starter Guide
## 1. Instalasi Miniconda
### **1a. Windows user**
- Download miniconda untuk Python 3.9
    - Klik link ini untuk download: [Miniconda Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Windows-x86_64.exe)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Ketika ada pilihan `install for`, pilih `Just Me (recommended)`
    - Untuk `Advanced Options`, silahkan centang `Register Anaconda as my default Python 3.9`
    - Tunggu hingga instalasi selesai

- Jalankan `Anaconda Prompt`

### **1b. Mac user**
- Download miniconda untuk Python 3.9
    - Klik link ini untuk download: [Miniconda Mac OS X 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-MacOSX-x86_64.pkg)
    - 
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Install tanpa mengubah opsi apapun
    - Tunggu hingga instalasi selesai

- Jalankan terminal

### **1c. Linux user**
- Download miniconda untuk Python 3.9
    - Klik link ini untuk download: [Miniconda Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-x86_64.sh)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.
    
- Install miniconda
    - jalankan terminal
    - Install miniconda menggunakan command berikut
        ```
        bash Miniconda3-py39_23.3.1-0-Linux-x86_64.sh
        ```
    - Ketik `yes` untuk agree dengan license nya, kemudian `yes` lagi untuk `prepend miniconda install location to PATH`
    - Tunggu hingga instalasi selesai
- hanya untuk memastikan, tutup dan buka terminal lagi

## 2. Download materi
- Klik disini untuk [Download Materi (ZIP)](https://github.com/coderplus62/Data-Science-Boot-Camp-by-Coder-62.git), atau
- Bagi yang familiar dengan git, boleh menggunakan clone
    ```
    git clone https://github.com/coderplus62/Data-Science-Boot-Camp-by-Coder-62.git
    ```

## 3. Instalasi jupyterlab 
- Kita akan install 2 hal di base environment
    ```
    conda install -n base -c conda-forge jupyterlab
    ```

## 4. Instalasi Environment
- Change directory `cd` ke folder kerja ini
    ```
    cd Data Science Boot-Camp by Coder+62/
    ```
- Jalankan command ini untuk menginstall environment `coder+62`
    ```
    conda env create -f env_coder+62.yml
    ```

## 5. Memastikan environment terinstall dengan baik
- Jalankan command berikut untuk mengecek instalasi dan ikuti instruksi yang dihasilkan
    ```
    python check_installation.py
    ```
- Jika sudah aman, maka akan muncul keterangan berikut, dan kita bisa mulai belajar. Semangat!
    ```
    ✓ jupyterlab telah terinstall dengan baik
    ✓ nb_conda_kernels telah terinstall dengan baik
    ✓ Environment coder+62 terdeteksi
    ✓ Package telah terinstall dengan baik di dalam environment coder+62
    ✓ Instalasi berjalan dengan baik. Selamat belajar!
    ```