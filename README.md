# App-detector-malicious-URL

Web untuk mendeteksi URL berbahaya, web ini di dedikasikan untuk pengajuan HKI dalam rangka peningkatan akreditasi pada PT Institut Teknologi Nasional Bandung.

Website dibangun dengan framework flask pada server-side dan pada client-side dibangung menggunakan html dan framework css (tailwind). Model machine learning hasil training sudah tersedia di folder `ML`. Model ini di-import dan digunakan di bagian server-side untuk melakukan deteksi URL berbahaya. Anda dapat menemukan kode terkait pengolahan model di `app.py`.

## Tampilan
- Home

![Screenshot 2024-07-16 182546](https://github.com/user-attachments/assets/81e7f5ef-12a9-471e-9017-451c000d4bd9)

- FAQ

![Screenshot 2024-07-16 182750](https://github.com/user-attachments/assets/5ccf81d2-4e70-41cd-9683-952ab90a1287)

- Contact

![Screenshot 2024-07-16 182915](https://github.com/user-attachments/assets/00e0d703-16fb-46d1-8cf2-285649438db0)


- Detect

![detect](https://github.com/user-attachments/assets/f7be943a-1a32-4d4e-8a1b-145e00968a59)

- Result

![result](https://github.com/user-attachments/assets/66091f09-d333-42cb-b1fb-4b2d8cecc1e0)

## Prasyarat

Sebelum melanjutkan, pastikan Anda telah memenuhi persyaratan berikut pada mesin Anda.

- Python version > 3
- git
- pip
- text editor -> Visual Studio Code for me
- Model ML
  _note: model hasil training sudah tersedia di folder ML_

## Cara install di local

- Clone repository ini

```bash
$ git clone https://github.com/FuadGrimaldi/App-detector-malicious-URL.git
```

- Ubah direktori ke folder tempat Anda ingin meletakkan kode

```bash
$ cd App-detector-malicious-URL
```

- buat python virtual environment pada folder tersebut kemudian aktifkan

```bash
$ python -m venv myenv
$ source myenv/bin/activate  # Untuk Unix/MacOS
$ source myenv/Scripts/activate  # Untuk windows git bash
```

- install depedencies pada requirement.txt

```bash
$ pip install -r requirements.txt
```

- Jalankan server pengembangan di mesin Anda

```bash
$ flask --app app run --debug
```

- Kunjungi aplikasi melalui [localhost:5000](localhost:5000)

## Package utama

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Tailwind](https://tailwindcss.com/)
- [sklearn](https://scikit-learn.org/stable/)

## opsi

- nonaktifkan virtual environment

```bash
$ deactivate
```

- nonaktifkan server (ctrl + c)

```bash
$ ^C
```

### Dengan perubahan ini, dokumentasi akan lebih mudah diikuti dan memberikan panduan yang lebih jelas bagi pengguna.
